"""
Targeted keyword-frequency pass over the government-document corpus, grouped into
categories relevant to signaling theory / expectancy violation / greenwashing-skepticism
constructs (rather than generic VADER polarity, which doesn't fit this register).

Categories are illustrative starting points for Britton to refine, not a validated
coding scheme.
"""
import csv
import re
from collections import defaultdict

csv.field_size_limit(2**31 - 1)

ANALYSIS_DIR = r"C:\Users\britt\Desktop\Claude global\CCS PAPER\Analysis"

CATEGORIES = {
    "Safety/risk assurance": ["safe", "safety", "protect", "protection", "prevent", "secure", "integrity"],
    "Risk/hazard language": ["risk", "hazard", "leak", "leakage", "emergency", "contamina", "liabilit", "damage"],
    "Transparency/accountability": ["transparen", "disclos", "public record", "report", "notify", "notice", "monitor"],
    "Community/consent signals": ["consult", "consent", "community", "public comment", "hearing", "tribe", "tribal", "stakeholder"],
    "Regulatory/authority signals": ["permit", "commissioner", "secretary", "authority", "enforc", "violat", "compliance"],
    "Economic/benefit framing": ["revenue", "royalt", "job", "economic", "benefit", "compensation", "landowner"],
}


def count_categories(text):
    text_low = text.lower()
    counts = {}
    for cat, terms in CATEGORIES.items():
        total = 0
        for term in terms:
            total += len(re.findall(re.escape(term), text_low))
        counts[cat] = total
    return counts


def main():
    with open(f"{ANALYSIS_DIR}\\corpus_documents.csv", encoding="utf-8") as f:
        docs = list(csv.DictReader(f))

    rows = []
    for doc in docs:
        counts = count_categories(doc["text"])
        n_words = int(doc["n_words"]) or 1
        row = {"filename": doc["filename"], "n_words": doc["n_words"]}
        for cat, c in counts.items():
            row[cat] = c
            row[f"{cat} (per 1k words)"] = round(1000 * c / n_words, 2)
        rows.append(row)

    fieldnames = ["filename", "n_words"] + [c for cat in CATEGORIES for c in (cat, f"{cat} (per 1k words)")]
    out_path = f"{ANALYSIS_DIR}\\signal_terms_by_doc.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {out_path}\n")
    header = f"{'filename':<55}" + "".join(f"{c[:18]:>20}" for c in CATEGORIES)
    print(header)
    for row in rows:
        line = f"{row['filename'][:54]:<55}"
        for cat in CATEGORIES:
            line += f"{row[cat + ' (per 1k words)']:>20}"
        print(line)


if __name__ == "__main__":
    main()
