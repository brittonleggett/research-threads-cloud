"""
Text mining + sentiment analysis over the Louisiana CCS legislative/regulatory corpus.

Inputs:
  Analysis/corpus_documents.csv  (one row per document, full text)
  Analysis/corpus_pages.csv      (one row per page, for finer-grained sentiment)

Outputs:
  Analysis/word_frequency_by_doc.csv   top terms per document
  Analysis/word_frequency_overall.csv  top terms across whole corpus
  Analysis/sentiment_by_document.csv   VADER sentiment per document
  Analysis/sentiment_by_page.csv       VADER sentiment per page (finer grain / trend within long docs)
"""
import csv
import re
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

csv.field_size_limit(2**31 - 1)

ANALYSIS_DIR = r"C:\Users\britt\Desktop\Claude global\CCS PAPER\Analysis"

STOP = set(stopwords.words("english"))
# domain/boilerplate noise common to legislative PDFs
EXTRA_STOP = {
    "shall", "may", "section", "act", "state", "louisiana", "provided",
    "provision", "provisions", "including", "law", "laws", "page", "et", "al",
    "pursuant", "hereby", "sec", "seq",
}
STOP |= EXTRA_STOP

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z\-']+[A-Za-z]|[A-Za-z]")


def tokenize(text: str):
    words = TOKEN_RE.findall(text.lower())
    return [w for w in words if w not in STOP and len(w) > 2]


def read_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def word_frequency(docs):
    per_doc_rows = []
    overall_counter = Counter()

    for doc in docs:
        tokens = tokenize(doc["text"])
        counter = Counter(tokens)
        overall_counter.update(counter)
        top20 = counter.most_common(20)
        for rank, (word, count) in enumerate(top20, start=1):
            per_doc_rows.append({
                "doc_id": doc["doc_id"],
                "filename": doc["filename"],
                "rank": rank,
                "word": word,
                "count": count,
            })

    overall_rows = [
        {"rank": i, "word": w, "count": c}
        for i, (w, c) in enumerate(overall_counter.most_common(100), start=1)
    ]
    return per_doc_rows, overall_rows


def sentiment_for_text(sia, text):
    scores = sia.polarity_scores(text)
    return scores


def sentiment_by_document(sia, docs):
    rows = []
    for doc in docs:
        text = doc["text"]
        scores = sentiment_for_text(sia, text)

        # also compute sentence-level distribution for nuance
        sentences = sent_tokenize(text) if text.strip() else []
        sent_scores = [sia.polarity_scores(s)["compound"] for s in sentences] if sentences else []
        pos_sent = sum(1 for s in sent_scores if s >= 0.05)
        neg_sent = sum(1 for s in sent_scores if s <= -0.05)
        neu_sent = len(sent_scores) - pos_sent - neg_sent

        rows.append({
            "doc_id": doc["doc_id"],
            "filename": doc["filename"],
            "n_words": doc["n_words"],
            "compound": round(scores["compound"], 4),
            "pos": round(scores["pos"], 4),
            "neu": round(scores["neu"], 4),
            "neg": round(scores["neg"], 4),
            "n_sentences": len(sentences),
            "pct_sentences_positive": round(100 * pos_sent / len(sent_scores), 1) if sent_scores else "",
            "pct_sentences_negative": round(100 * neg_sent / len(sent_scores), 1) if sent_scores else "",
            "pct_sentences_neutral": round(100 * neu_sent / len(sent_scores), 1) if sent_scores else "",
        })
    return rows


def sentiment_by_page(sia, pages):
    rows = []
    for p in pages:
        text = p["text"]
        if not text.strip():
            continue
        scores = sentiment_for_text(sia, text)
        rows.append({
            "doc_id": p["doc_id"],
            "filename": p["filename"],
            "page": p["page"],
            "n_chars": p["n_chars"],
            "compound": round(scores["compound"], 4),
            "pos": round(scores["pos"], 4),
            "neu": round(scores["neu"], 4),
            "neg": round(scores["neg"], 4),
        })
    return rows


def main():
    docs = read_csv(f"{ANALYSIS_DIR}\\corpus_documents.csv")
    pages = read_csv(f"{ANALYSIS_DIR}\\corpus_pages.csv")

    print("Running word frequency analysis...")
    per_doc_freq, overall_freq = word_frequency(docs)
    write_csv(f"{ANALYSIS_DIR}\\word_frequency_by_doc.csv", per_doc_freq,
              ["doc_id", "filename", "rank", "word", "count"])
    write_csv(f"{ANALYSIS_DIR}\\word_frequency_overall.csv", overall_freq,
              ["rank", "word", "count"])
    print(f"  -> word_frequency_by_doc.csv ({len(per_doc_freq)} rows)")
    print(f"  -> word_frequency_overall.csv ({len(overall_freq)} rows)")

    print("Running sentiment analysis (VADER)...")
    sia = SentimentIntensityAnalyzer()

    doc_sentiment = sentiment_by_document(sia, docs)
    write_csv(f"{ANALYSIS_DIR}\\sentiment_by_document.csv", doc_sentiment,
              ["doc_id", "filename", "n_words", "compound", "pos", "neu", "neg",
               "n_sentences", "pct_sentences_positive", "pct_sentences_negative", "pct_sentences_neutral"])
    print(f"  -> sentiment_by_document.csv ({len(doc_sentiment)} rows)")

    page_sentiment = sentiment_by_page(sia, pages)
    write_csv(f"{ANALYSIS_DIR}\\sentiment_by_page.csv", page_sentiment,
              ["doc_id", "filename", "page", "n_chars", "compound", "pos", "neu", "neg"])
    print(f"  -> sentiment_by_page.csv ({len(page_sentiment)} rows)")

    print("\nDocument-level sentiment summary:")
    for row in sorted(doc_sentiment, key=lambda r: float(r["compound"])):
        print(f"  {row['compound']:>7} | {row['filename']}")


if __name__ == "__main__":
    main()
