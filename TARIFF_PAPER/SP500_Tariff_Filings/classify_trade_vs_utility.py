"""
Second-pass disambiguation: the raw "tariff" full-text search catches both
trade tariffs (the phenomenon Study 1/companion analysis cares about) and
utility/regulatory rate tariffs (FERC filings, "large load tariff", commodity
supply tariffs, feed-in tariffs) which are a different sense of the word
entirely. The validation sample (validation_sample.md) confirmed this
contamination is real and concentrated in the Utilities sector.

For every filing in the index, fetch the document, find each "tariff"
occurrence, and classify based on nearby keyword co-occurrence:
  - "trade"        : at least one occurrence has trade-tariff signal words nearby
  - "utility_only"  : occurrences only show utility/rate-tariff signal words
  - "ambiguous"     : neither signal set fires clearly (kept, flagged for manual review)
  - "fetch_failed"  : could not retrieve/parse the document

Resumable: writes incrementally, skips CIK+accession+file_id already logged.
"""
import csv
import re
import time
import urllib.request
import pathlib

HERE = pathlib.Path(__file__).parent
IN_CSV = HERE / "sp500_tariff_filings_index.csv"
OUT_CSV = HERE / "sp500_tariff_filings_classified.csv"
PROGRESS_LOG = HERE / "classify_progress.log"
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

FIELDS = ["company", "ticker", "cik", "gics_sector", "form", "file_date",
          "period_ending", "accession_number", "file_id", "file_type",
          "filing_index_url", "doc_url", "classification", "matched_snippet"]


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

    trade_hit = None
    utility_hit = None
    for w in windows:
        has_trade = any(s in w for s in TRADE_SIGNALS)
        has_util = any(s in w for s in UTILITY_SIGNALS)
        if has_trade and trade_hit is None:
            trade_hit = w
        if has_util and utility_hit is None:
            utility_hit = w

    if trade_hit:
        return "trade", trade_hit.strip()
    if utility_hit:
        return "utility_only", utility_hit.strip()
    return "ambiguous", windows[0].strip()


def fetch_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text)
    return text


def main():
    with open(IN_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    done_keys = set()
    if PROGRESS_LOG.exists():
        with open(PROGRESS_LOG, encoding="utf-8") as f:
            done_keys = set(line.strip() for line in f if line.strip())

    write_header = not OUT_CSV.exists()
    out_f = open(OUT_CSV, "a", newline="", encoding="utf-8")
    writer = csv.DictWriter(out_f, fieldnames=FIELDS)
    if write_header:
        writer.writeheader()
    log_f = open(PROGRESS_LOG, "a", encoding="utf-8")

    counts = {"trade": 0, "utility_only": 0, "ambiguous": 0, "no_match": 0, "fetch_failed": 0}
    n_done = 0
    for i, r in enumerate(rows):
        key = f"{r['cik']}|{r['accession_number']}|{r['file_id']}"
        if key in done_keys:
            continue
        if not r["doc_url"]:
            classification, snippet = "fetch_failed", "[no doc_url]"
        else:
            try:
                text = fetch_text(r["doc_url"])
                classification, snippet = classify_doc(text)
            except Exception as e:
                classification, snippet = "fetch_failed", f"[error: {e}]"
        counts[classification] = counts.get(classification, 0) + 1
        out_row = {k: r.get(k, "") for k in FIELDS if k in r}
        out_row["classification"] = classification
        out_row["matched_snippet"] = snippet[:500]
        writer.writerow(out_row)
        out_f.flush()
        log_f.write(key + "\n")
        log_f.flush()
        n_done += 1
        if n_done % 50 == 0:
            print(f"[{n_done} done, {i+1}/{len(rows)} scanned] running counts: {counts}")
        time.sleep(0.2)

    out_f.close()
    log_f.close()
    print(f"\nDONE. {n_done} newly classified this run. Final running counts: {counts}")


if __name__ == "__main__":
    main()
