"""
Pulls tariff-mention SEC filings (10-K, 10-Q, 8-K) for all S&P 500 constituents
via EDGAR full-text search, Jan 2025 - Jul 2026. Writes incrementally to CSV.
"""
import csv
import json
import time
import urllib.request
import urllib.parse
import pathlib

HERE = pathlib.Path(__file__).parent
CONSTITUENTS = HERE / "sp500_constituents.csv"
OUT_CSV = HERE / "sp500_tariff_filings_index.csv"
PROGRESS_LOG = HERE / "fetch_progress.log"
UA = "Britton Leggett Research britton.leggett@gmail.com"
API = "https://efts.sec.gov/LATEST/search-index"
STARTDT = "2025-01-01"
ENDDT = "2026-07-24"
FORMS = "10-K,10-Q,8-K"

FIELDS = ["company", "ticker", "cik", "gics_sector", "form", "file_date",
          "period_ending", "accession_number", "file_id", "file_type",
          "filing_index_url", "doc_url"]


def load_constituents():
    with open(CONSTITUENTS, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def query(cik):
    cik_padded = cik.zfill(10)
    params = {
        "q": '"tariff"',
        "forms": FORMS,
        "ciks": cik_padded,
        "startdt": STARTDT,
        "enddt": ENDDT,
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def filing_index_url(cik, adsh):
    adsh_nodash = adsh.replace("-", "")
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh_nodash}/{adsh}-index.htm"


def doc_url(cik, adsh, file_id):
    adsh_nodash = adsh.replace("-", "")
    doc_name = file_id.split(":", 1)[1] if ":" in file_id else file_id
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh_nodash}/{doc_name}"


def main():
    constituents = load_constituents()
    write_header = not OUT_CSV.exists()
    csv_f = open(OUT_CSV, "a", newline="", encoding="utf-8")
    writer = csv.DictWriter(csv_f, fieldnames=FIELDS)
    if write_header:
        writer.writeheader()

    # resume support: skip CIKs already fully logged
    done_ciks = set()
    if PROGRESS_LOG.exists():
        with open(PROGRESS_LOG, encoding="utf-8") as f:
            done_ciks = set(line.strip() for line in f if line.strip())

    log_f = open(PROGRESS_LOG, "a", encoding="utf-8")

    total_filings = 0
    companies_with_hits = 0
    errors = []

    for i, row in enumerate(constituents):
        cik = row["CIK"].strip()
        ticker = row["Symbol"].strip()
        if cik in done_ciks:
            continue
        try:
            data = query(cik)
        except Exception as e:
            errors.append(f"{ticker} (CIK {cik}): {e}")
            time.sleep(1)
            continue

        hits = data.get("hits", {}).get("hits", [])
        if hits:
            companies_with_hits += 1
        for h in hits:
            src = h["_source"]
            adsh = src.get("adsh", "")
            file_id = h.get("_id", "")
            writer.writerow({
                "company": row["Security"],
                "ticker": ticker,
                "cik": cik,
                "gics_sector": row.get("GICS Sector", ""),
                "form": src.get("form", ""),
                "file_date": src.get("file_date", ""),
                "period_ending": src.get("period_ending", ""),
                "accession_number": adsh,
                "file_id": file_id,
                "file_type": src.get("file_type", ""),
                "filing_index_url": filing_index_url(cik, adsh) if adsh else "",
                "doc_url": doc_url(cik, adsh, file_id) if adsh and file_id else "",
            })
            total_filings += 1
        csv_f.flush()
        log_f.write(cik + "\n")
        log_f.flush()
        if (i + 1) % 25 == 0:
            print(f"[{i+1}/{len(constituents)}] {ticker} done. "
                  f"Running totals: {total_filings} filings, {companies_with_hits} companies with hits.")
        time.sleep(0.15)  # ~6-7 req/sec, well under SEC's 10/sec guidance

    csv_f.close()
    log_f.close()

    print(f"\nDONE. Total filings: {total_filings}. Companies with >=1 hit: {companies_with_hits} / {len(constituents)}.")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors[:30]:
            print(" ", e)
        with open(HERE / "fetch_errors.log", "w", encoding="utf-8") as f:
            f.write("\n".join(errors))


if __name__ == "__main__":
    main()
