"""
Cleanup pass for the S&P 500 tariff-filing pull:
1. Dedupe the index CSV (a concurrent-run bug wrote some rows twice).
2. Retry companies that errored (SEC HTTP 500s) or were never reached.
3. Recompute summary stats (filings, companies-with-hits, form/year/sector breakdown).
4. Pull a random validation sample of actual filing text around "tariff" mentions,
   so false positives (e.g. utility/rate "tariffs" vs trade tariffs) can be checked.
"""
import csv
import json
import random
import re
import time
import urllib.request
import urllib.parse
import pathlib
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).parent
CONSTITUENTS = HERE / "sp500_constituents.csv"
RAW_CSV = HERE / "sp500_tariff_filings_index.csv"
CLEAN_CSV = HERE / "sp500_tariff_filings_index.csv"  # overwrite with clean version
VALIDATION_MD = HERE / "validation_sample.md"
STATS_JSON = HERE / "summary_stats.json"
UA = "Britton Leggett Research britton.leggett@gmail.com"
API = "https://efts.sec.gov/LATEST/search-index"
STARTDT = "2025-01-01"
ENDDT = "2026-07-24"
FORMS = "10-K,10-Q,8-K"

FIELDS = ["company", "ticker", "cik", "gics_sector", "form", "file_date",
          "period_ending", "accession_number", "file_id", "file_type",
          "filing_index_url", "doc_url"]


def query(cik):
    params = {"q": '"tariff"', "forms": FORMS, "ciks": cik.zfill(10),
              "startdt": STARTDT, "enddt": ENDDT}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def filing_index_url(cik, adsh):
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh.replace('-', '')}/{adsh}-index.htm"


def doc_url(cik, adsh, file_id):
    doc_name = file_id.split(":", 1)[1] if ":" in file_id else file_id
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh.replace('-', '')}/{doc_name}"


def step1_dedupe():
    with open(RAW_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    seen = set()
    clean = []
    for r in rows:
        key = (r["cik"], r["accession_number"], r["file_id"])
        if key in seen:
            continue
        seen.add(key)
        clean.append(r)
    print(f"Dedupe: {len(rows)} raw rows -> {len(clean)} unique rows "
          f"({len(rows) - len(clean)} duplicates removed).")
    return clean


def step2_retry_missing(clean_rows, constituents):
    have_ciks = set(r["cik"] for r in clean_rows)
    # a company counts as "attempted" if it has rows OR is confirmed zero-hit;
    # we don't have a clean record of zero-hit companies separately, so retry
    # anyone from the known error list plus anyone with zero rows at all.
    known_errors = ["14693", "1043277", "900075", "97476", "1035002", "1014473"]  # BF.B, CHRW, CPRT, TXN, VLO, VRSN
    retry_ciks = [c for c in known_errors if c not in have_ciks]
    new_rows = []
    for cik in retry_ciks:
        row = next((c for c in constituents if c["CIK"].strip() == cik), None)
        if not row:
            continue
        ticker = row["Symbol"].strip()
        for attempt in range(3):
            try:
                data = query(cik)
                break
            except Exception as e:
                print(f"  retry {attempt+1} failed for {ticker}: {e}")
                time.sleep(3)
        else:
            print(f"  giving up on {ticker} (CIK {cik}) after 3 attempts")
            continue
        hits = data.get("hits", {}).get("hits", [])
        for h in hits:
            src = h["_source"]
            adsh = src.get("adsh", "")
            file_id = h.get("_id", "")
            new_rows.append({
                "company": row["Security"], "ticker": ticker, "cik": cik,
                "gics_sector": row.get("GICS Sector", ""), "form": src.get("form", ""),
                "file_date": src.get("file_date", ""), "period_ending": src.get("period_ending", ""),
                "accession_number": adsh, "file_id": file_id, "file_type": src.get("file_type", ""),
                "filing_index_url": filing_index_url(cik, adsh) if adsh else "",
                "doc_url": doc_url(cik, adsh, file_id) if adsh and file_id else "",
            })
        print(f"  retried {ticker}: {len(hits)} hits")
        time.sleep(0.3)
    print(f"Retry recovered {len(new_rows)} additional rows from {len(retry_ciks)} companies.")
    return clean_rows + new_rows


def step3_stats(clean_rows, constituents):
    companies_with_hits = set((r["cik"] for r in clean_rows))
    form_counts = Counter(r["form"] for r in clean_rows)
    year_counts = Counter(r["file_date"][:4] for r in clean_rows if r["file_date"])
    sector_counts = Counter()
    sector_company_sets = defaultdict(set)
    for r in clean_rows:
        sector_counts[r["gics_sector"]] += 1
        sector_company_sets[r["gics_sector"]].add(r["cik"])
    stats = {
        "total_filings": len(clean_rows),
        "total_constituents": len(constituents),
        "companies_with_at_least_one_hit": len(companies_with_hits),
        "form_breakdown": dict(form_counts),
        "year_breakdown": dict(sorted(year_counts.items())),
        "sector_filing_counts": dict(sector_counts),
        "sector_company_counts": {k: len(v) for k, v in sector_company_sets.items()},
    }
    with open(STATS_JSON, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)
    print(json.dumps(stats, indent=2))
    return stats


def step4_validation_sample(clean_rows, n=25):
    random.seed(42)
    sample = random.sample(clean_rows, min(n, len(clean_rows)))
    results = []
    for r in sample:
        url = r["doc_url"]
        if not url:
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw = resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            results.append((r, [f"[fetch failed: {e}]"]))
            time.sleep(0.3)
            continue
        text = re.sub(r"<[^>]+>", " ", raw)
        text = re.sub(r"\s+", " ", text)
        contexts = []
        for m in re.finditer(r"tariff", text, re.IGNORECASE):
            start = max(0, m.start() - 180)
            end = min(len(text), m.end() + 180)
            contexts.append("..." + text[start:end].strip() + "...")
            if len(contexts) >= 2:
                break
        results.append((r, contexts if contexts else ["[no literal match found in fetched doc]"]))
        time.sleep(0.3)

    with open(VALIDATION_MD, "w", encoding="utf-8") as f:
        f.write("# Validation Sample — Random 25 Filings, Manual False-Positive Check\n\n")
        f.write("Purpose: spot-check whether \"tariff\" hits are genuine trade-tariff discussion "
                "vs. false positives (e.g. utility/rate tariffs, unrelated boilerplate).\n\n")
        for r, contexts in results:
            f.write(f"## {r['company']} ({r['ticker']}) — {r['form']}, {r['file_date']}\n")
            f.write(f"[Filing index]({r['filing_index_url']}) | [Document]({r['doc_url']})\n\n")
            for c in contexts:
                f.write(f"> {c}\n\n")
    print(f"\nValidation sample written: {VALIDATION_MD} ({len(results)} filings sampled)")


def main():
    with open(CONSTITUENTS, encoding="utf-8") as f:
        constituents = list(csv.DictReader(f))

    clean_rows = step1_dedupe()
    clean_rows = step2_retry_missing(clean_rows, constituents)

    with open(CLEAN_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for r in clean_rows:
            writer.writerow({k: r.get(k, "") for k in FIELDS})
    print(f"Wrote clean CSV: {CLEAN_CSV} ({len(clean_rows)} rows)")

    step3_stats(clean_rows, constituents)
    step4_validation_sample(clean_rows, n=25)


if __name__ == "__main__":
    main()
