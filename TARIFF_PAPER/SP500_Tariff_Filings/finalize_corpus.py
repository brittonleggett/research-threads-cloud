"""
Final pass: retry fetch_failed rows, split the classified index into
TRADE (primary corpus) / EXCLUDED_utility (false positives) /
AMBIGUOUS_needs_review, and compute company-level summary stats.
"""
import csv
import json
import re
import time
import urllib.request
import pathlib
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).parent
IN_CSV = HERE / "sp500_tariff_filings_classified.csv"
UA = "Britton Leggett Research britton.leggett@gmail.com"

TRADE_SIGNALS = [
    "trade polic", "trade war", "trade agreement", "trade action", "trade tension",
    "trade barrier", "trade restrict", "import", "export", "dut", "customs",
    "china", "ieepa", "section 301", "section 232", "section 122", "retaliat",
    "trading partner", "supply chain", "countervailing", "antidumping",
    "sourcing", "reciprocal tariff", "geopolitic", "cost of goods",
    "manufactur", "gross margin", "price increase",
]
UTILITY_SIGNALS = [
    "ferc", "puc ", "public utility commission", "rate case", "commodity supply",
    "feed-in", "distribution tariff", "transmission tariff", "iso-ne", " pjm",
    " miso", " nyiso", "large load tariff", "electric tariff", "gas tariff",
    "rate schedule", "tariff filing", "tariff sheet", "retail tariff",
    "delivery tariff", "capacity market", "utility commission",
]


def classify_doc(text):
    low = text.lower()
    windows = []
    for m in re.finditer(r"tariff", low):
        start = max(0, m.start() - 200)
        end = min(len(low), m.end() + 200)
        windows.append(low[start:end])
        if len(windows) >= 8:
            break
    if not windows:
        return "no_match", ""
    trade_hit = utility_hit = None
    for w in windows:
        if any(s in w for s in TRADE_SIGNALS) and trade_hit is None:
            trade_hit = w
        if any(s in w for s in UTILITY_SIGNALS) and utility_hit is None:
            utility_hit = w
    if trade_hit:
        return "trade", trade_hit.strip()
    if utility_hit:
        return "utility_only", utility_hit.strip()
    return "ambiguous", windows[0].strip()


def fetch_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    text = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", text)


def main():
    with open(IN_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())

    retried = 0
    for r in rows:
        if r["classification"] != "fetch_failed":
            continue
        for attempt in range(2):
            try:
                text = fetch_text(r["doc_url"])
                classification, snippet = classify_doc(text)
                r["classification"] = classification
                r["matched_snippet"] = snippet[:500]
                retried += 1
                break
            except Exception as e:
                time.sleep(2)
                r["matched_snippet"] = f"[retry failed: {e}]"
        time.sleep(0.3)
    print(f"Retried fetch_failed rows: {retried} recovered a classification.")

    with open(IN_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    buckets = defaultdict(list)
    for r in rows:
        buckets[r["classification"]].append(r)

    def write_bucket(name, key):
        path = HERE / name
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in buckets.get(key, []):
                w.writerow(r)
        print(f"{name}: {len(buckets.get(key, []))} rows")

    write_bucket("sp500_tariff_TRADE_corpus.csv", "trade")
    write_bucket("sp500_tariff_EXCLUDED_utility.csv", "utility_only")
    write_bucket("sp500_tariff_AMBIGUOUS_needs_review.csv", "ambiguous")
    write_bucket("sp500_tariff_NO_MATCH_or_failed.csv", "no_match")
    fetch_failed_rows = buckets.get("fetch_failed", [])
    if fetch_failed_rows:
        path = HERE / "sp500_tariff_NO_MATCH_or_failed.csv"
        with open(path, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            for r in fetch_failed_rows:
                w.writerow(r)
        print(f"  + {len(fetch_failed_rows)} still-failed rows appended")

    trade_rows = buckets.get("trade", [])
    companies_trade = set((r["cik"], r["company"]) for r in trade_rows)
    sector_company = defaultdict(set)
    sector_filing = Counter()
    year_counts = Counter()
    form_counts = Counter()
    for r in trade_rows:
        sector_company[r["gics_sector"]].add(r["cik"])
        sector_filing[r["gics_sector"]] += 1
        year_counts[r["file_date"][:4]] += 1
        form_counts[r["form"]] += 1

    stats = {
        "total_filings_all_classifications": len(rows),
        "classification_breakdown": {k: len(v) for k, v in buckets.items()},
        "trade_corpus_filings": len(trade_rows),
        "trade_corpus_unique_companies": len(companies_trade),
        "trade_corpus_form_breakdown": dict(form_counts),
        "trade_corpus_year_breakdown": dict(sorted(year_counts.items())),
        "trade_corpus_sector_filing_counts": dict(sector_filing),
        "trade_corpus_sector_company_counts": {k: len(v) for k, v in sector_company.items()},
    }
    with open(HERE / "final_summary_stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
