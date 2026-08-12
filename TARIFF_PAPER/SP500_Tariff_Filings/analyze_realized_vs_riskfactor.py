"""
v2 — fixes a precision bug found by manual spot-check: v1 combined all
tariff-occurrence windows into one blob before pattern-matching, so a dollar
figure anywhere in a large filing (e.g. an unrelated buyback amount) could
trigger "realized" even when nowhere near an actual tariff-cost claim.
Marvell/Duke Energy/PG&E generic risk-factor bullet lists were misclassified
as "realized" this way. v2 classifies each tariff-occurrence window
independently and requires the cost/action signal to be tightly co-located
with "tariff" within that same ~250-char window, not just present somewhere
in the document.

Second analytical layer on the trade-tariff corpus: most SEC filing "tariff"
mentions are boilerplate forward-looking risk-factor language, not disclosure
of an actually-realized price/cost action. Study 1's messaging typology was
built from REALIZED price-increase artifacts (Nike, Mattel, BMW, etc.), so
only the realized subset here is actually comparable to it. Within the
realized subset, also codes causation-attribution (Study 1 Theme 2): explicit
vs. vague/listed framing of tariffs as the cause.

Still a keyword/pattern heuristic, not semantic understanding — validate
against a fresh manual sample before trusting the numbers (see
validate_realized_classifier.py).
"""
import csv
import re
import time
import urllib.request
import pathlib

HERE = pathlib.Path(__file__).parent
IN_CSV = HERE / "sp500_tariff_TRADE_corpus.csv"
OUT_CSV = HERE / "sp500_tariff_TRADE_corpus_analyzed.csv"
PROGRESS_LOG = HERE / "analyze_progress.log"
UA = "Britton Leggett Research britton.leggett@gmail.com"
WINDOW_RADIUS = 250

# Strong signals: cost/price ACTION tightly tied to "tariff" in the SAME window.
# Deliberately narrower than v1 — precision over recall.
REALIZED_STRONG = [
    r"tariffs?[^.]{0,50}(cost|costs|added|contributed|resulted in)[^.]{0,30}\$",
    r"\$[^.]{0,60}(million|billion)?[^.]{0,40}tariffs?",
    r"(increased|raised)\s+(our\s+|its\s+)?prices?[^.]{0,60}(due to|because of|as a result of|to offset|to mitigate)[^.]{0,20}tariffs?",
    r"tariffs?[^.]{0,40}(increased|added|raised)[^.]{0,20}(our\s+)?costs?\s+by",
    r"(fully |partially |largely )?mitigat(ed|ing)[^.]{0,30}(impact|effect)s?\s+of[^.]{0,20}tariffs?",
    r"tariff[- ]related\s+(costs?|expenses?|charges?)\s+of\s+\$",
    r"(we\s+)?(raised|increased)\s+prices?\s+to\s+(offset|address|mitigate)[^.]{0,20}tariffs?",
    r"tariff\s+surcharge",
    r"passed\s+(on|through)[^.]{0,20}tariff",
    r"tariff\s+impact\s+of\s+\$",
    r"\$[\d,.]+\s?(million|billion)\s+(impact|cost|charge|expense)[^.]{0,30}tariffs?",
]
HYPOTHETICAL_PATTERNS = [
    r"\bcould\b", r"\bmay\b", r"\bmight\b", r"\bwould\b", r"potential(ly)?",
    r"if tariffs", r"in the event", r"risk factors?", r"forward-looking",
    r"could result in", r"could adversely affect", r"could have a material adverse effect",
    r"we cannot predict", r"it is impossible to (say|predict)", r"uncertain(ty)?",
]
CAUSATION_EXPLICIT = [
    r"due to tariffs?", r"as a result of tariffs?", r"because of tariffs?",
    r"tariff-related", r"tariff-driven", r"attributable to tariffs?",
    r"tariffs? contributed to", r"to offset tariffs?", r"tariff costs? of",
    r"driven by tariffs?", r"reflecting tariffs?", r"tariff impact of",
]


def fetch_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    text = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", text)


def get_windows(low_text, radius=WINDOW_RADIUS, cap=8):
    windows = []
    for m in re.finditer(r"tariff", low_text):
        start = max(0, m.start() - radius)
        end = min(len(low_text), m.end() + radius)
        windows.append(low_text[start:end])
        if len(windows) >= cap:
            break
    return windows


def classify_doc(windows):
    realized_window = None
    hypothetical_window = None
    for w in windows:
        if any(re.search(p, w, re.IGNORECASE) for p in REALIZED_STRONG):
            realized_window = w
            break
    if not realized_window:
        for w in windows:
            if any(re.search(p, w, re.IGNORECASE) for p in HYPOTHETICAL_PATTERNS):
                hypothetical_window = w
                break

    if realized_window:
        if any(re.search(p, realized_window, re.IGNORECASE) for p in CAUSATION_EXPLICIT):
            causation = "explicit"
        elif len(re.split(r"[,;]", realized_window)) >= 4:
            causation = "vague_listed"
        else:
            causation = "silent_or_unclear"
        return "realized", causation, realized_window
    if hypothetical_window:
        return "hypothetical_risk_factor", "n/a_not_realized", hypothetical_window
    return "unclear", "n/a_not_realized", (windows[0] if windows else "")


def main():
    with open(IN_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
    for extra in ["realized_classification", "causation_classification", "analysis_window"]:
        if extra not in fields:
            fields.append(extra)
    # dedupe fields in case rows already had them from v1 (they won't, we start fresh)
    fields = list(dict.fromkeys(fields))

    done_keys = set()
    if PROGRESS_LOG.exists():
        with open(PROGRESS_LOG, encoding="utf-8") as f:
            done_keys = set(l.strip() for l in f if l.strip())

    write_header = not OUT_CSV.exists()
    out_f = open(OUT_CSV, "a", newline="", encoding="utf-8")
    writer = csv.DictWriter(out_f, fieldnames=fields)
    if write_header:
        writer.writeheader()
    log_f = open(PROGRESS_LOG, "a", encoding="utf-8")

    n = 0
    for r in rows:
        key = f"{r['cik']}|{r['accession_number']}|{r['file_id']}"
        if key in done_keys:
            continue
        if not r.get("doc_url"):
            r["realized_classification"] = "fetch_failed"
            r["causation_classification"] = "fetch_failed"
            r["analysis_window"] = ""
        else:
            try:
                text = fetch_text(r["doc_url"])
                windows = get_windows(text.lower())
                realized_c, causation_c, window = classify_doc(windows)
                r["realized_classification"] = realized_c
                r["causation_classification"] = causation_c
                r["analysis_window"] = window[:700]
            except Exception as e:
                r["realized_classification"] = "fetch_failed"
                r["causation_classification"] = "fetch_failed"
                r["analysis_window"] = f"[error: {e}]"
        writer.writerow({k: r.get(k, "") for k in fields})
        out_f.flush()
        log_f.write(key + "\n")
        log_f.flush()
        n += 1
        if n % 100 == 0:
            print(f"[{n} processed]")
        time.sleep(0.2)

    out_f.close()
    log_f.close()
    print(f"DONE. {n} filings analyzed this run.")


if __name__ == "__main__":
    main()
