"""
Theory-grounded quantitative coding pass over the Louisiana CCS legislative/regulatory
corpus (Track A), replacing VADER sentiment as the primary quantitative layer.

Rationale (see Overnight_Method_Research_2026-07-08.md for full writeup):
VADER is a lexicon sentiment tool built for expressive text (reviews, tweets); it doesn't
fit formal legal/legislative register, which rarely expresses emotional valence at all.
Rather than swap in a different sentiment tool, this maps the corpus onto the SAME
governance-frame / procedural-justice / recognition-justice taxonomy already built for
Track B's vignette experiment (CCS_Lit_Review_Foundation.docx, Part 8: governance frame ->
procedural justice -> recognition justice -> institutional trust -> legitimacy -> support).

This lets Track A do double duty: (1) a defensible quantitative pass for Track A itself,
and (2) empirical grounding evidence for Track B's 6 governance-frame vignette conditions
(state regulator approval, industry expertise, local referendum, property rights,
affected-community consultation, Tribal consultation) — i.e., "these frames were selected
because they appear in the actual LA CCS regulatory corpus," which is a citable methods
justification Track B doesn't currently have.

Categories are still an illustrative starting coding frame for Britton to refine/validate,
NOT a validated instrument — same caveat as the earlier signal_terms.py draft.
"""
import csv
import re
from collections import defaultdict

csv.field_size_limit(2**31 - 1)

ANALYSIS_DIR = r"C:\Users\britt\Desktop\Claude global\CCS PAPER\Analysis"

# --- Governance frames (Track B's 6 vignette conditions + control) ---------------------
GOVERNANCE_FRAMES = {
    "State regulator approval": [
        "commissioner of conservation", "office of conservation", "department of energy and natural resources",
        "secretary", "permit", "authoriz", "approv", "regulatory authority", "class vi",
    ],
    "Industry/technical expertise": [
        "engineering", "technical", "geologic", "geological", "feasibility", "monitoring plan",
        "operator", "best available technology", "site characterization",
    ],
    "Local referendum/voting": [
        "election", "referendum", "ballot", "vote", "local governing authority", "parish council",
        "police jury",
    ],
    "Property rights protection": [
        "property right", "mineral right", "surface right", "landowner", "unitiz", "eminent domain",
        "just compensation", "pore space", "servitude",
    ],
    "Affected-community consultation": [
        "public comment", "public hearing", "public notice", "notify the public", "stakeholder",
        "community", "opportunity to be heard", "public participation",
    ],
    "Tribal/Indigenous consultation": [
        "tribe", "tribal", "indigenous", "sovereign nation", "coushatta", "chitimacha",
        "tunica", "biloxi", "jena band", "houma nation", "consultation with",
    ],
}

# --- Procedural justice: Tyler (2003) four criteria -------------------------------------
PROCEDURAL_JUSTICE = {
    "Voice/participation": [
        "public comment", "public hearing", "opportunity to comment", "opportunity to be heard",
        "submit comments", "testimony", "participate",
    ],
    "Neutrality": [
        "impartial", "unbiased", "independent review", "conflict of interest", "objective",
    ],
    "Trustworthiness": [
        "good faith", "accountab", "integrity", "transparent", "transparency", "disclos",
    ],
    "Dignitary treatment": [
        "respect", "dignity", "fair treatment", "due process", "notice and", "adequate notice",
    ],
}

# --- Recognition justice / Indigenous sovereignty (distinct from generic consultation) --
RECOGNITION_JUSTICE = {
    "Named LA tribal nations": [
        "coushatta", "chitimacha", "tunica-biloxi", "tunica biloxi", "jena band", "united houma",
    ],
    "Sovereignty language": [
        "sovereign", "sovereignty", "self-determination", "government-to-government",
        "federally recognized", "tribal government", "tribal nation",
    ],
    "Generic stakeholder framing (contrast case)": [
        "stakeholder", "interested part", "affected part",
    ],
}

# --- Institutional trust: competence-based vs. integrity-based (Terwel et al., 2009) ----
INSTITUTIONAL_TRUST = {
    "Competence-based trust signals": [
        "qualified", "expertise", "certified", "technical review", "demonstrated ability",
        "capacity to",
    ],
    "Integrity-based trust signals": [
        "accountab", "honest", "good faith", "integrity", "enforcement", "penalt", "violat",
    ],
}

# --- Legitimacy / outcome language -------------------------------------------------------
LEGITIMACY_SUPPORT = {
    "Legitimacy/license language": [
        "legitima", "social license", "public trust", "in the public interest",
    ],
    "Support/opposition language": [
        "support", "oppose", "objection", "approve", "reject", "protest",
    ],
}

ALL_GROUPS = {
    "Governance frame": GOVERNANCE_FRAMES,
    "Procedural justice": PROCEDURAL_JUSTICE,
    "Recognition justice": RECOGNITION_JUSTICE,
    "Institutional trust": INSTITUTIONAL_TRUST,
    "Legitimacy/support": LEGITIMACY_SUPPORT,
}


def count_terms(text_low, terms):
    total = 0
    hits = {}
    for term in terms:
        n = len(re.findall(re.escape(term), text_low))
        if n:
            hits[term] = n
        total += n
    return total, hits


def main():
    with open(f"{ANALYSIS_DIR}\\corpus_documents.csv", encoding="utf-8") as f:
        docs = list(csv.DictReader(f))

    per_doc_rows = []
    term_hit_log = defaultdict(lambda: defaultdict(int))  # group -> term -> total count across corpus

    for doc in docs:
        text_low = doc["text"].lower()
        n_words = int(doc["n_words"]) or 1
        row = {"filename": doc["filename"], "n_words": doc["n_words"]}
        for group_name, categories in ALL_GROUPS.items():
            for cat_name, terms in categories.items():
                total, hits = count_terms(text_low, terms)
                col = f"{group_name} :: {cat_name}"
                row[col] = total
                row[f"{col} (per 1k words)"] = round(1000 * total / n_words, 2)
                for term, n in hits.items():
                    term_hit_log[col][term] += n
        per_doc_rows.append(row)

    fieldnames = ["filename", "n_words"]
    for group_name, categories in ALL_GROUPS.items():
        for cat_name in categories:
            col = f"{group_name} :: {cat_name}"
            fieldnames += [col, f"{col} (per 1k words)"]

    out_path = f"{ANALYSIS_DIR}\\theory_grounded_coding_by_doc.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(per_doc_rows)
    print(f"Wrote {out_path} ({len(per_doc_rows)} documents x {len(fieldnames)-2} coding columns)")

    # corpus-wide rollup: which governance frames / justice categories appear at all,
    # and which specific terms drove each category (useful for face-validity checking)
    rollup_path = f"{ANALYSIS_DIR}\\theory_grounded_coding_corpus_summary.csv"
    with open(rollup_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["group_category", "total_hits_corpus_wide", "n_docs_with_any_hit", "top_terms"])
        for group_name, categories in ALL_GROUPS.items():
            for cat_name in categories:
                col = f"{group_name} :: {cat_name}"
                total = sum(row[col] for row in per_doc_rows)
                n_docs = sum(1 for row in per_doc_rows if row[col] > 0)
                top_terms = sorted(term_hit_log[col].items(), key=lambda kv: -kv[1])[:5]
                top_terms_str = "; ".join(f"{t}({n})" for t, n in top_terms)
                writer.writerow([col, total, n_docs, top_terms_str])
    print(f"Wrote {rollup_path}")


if __name__ == "__main__":
    main()
