# CCS Track A — Overnight Method Research (2026-07-08 night)

## What was asked
Find a better quantitative text-analysis method than VADER for the Track A corpus (18 Louisiana
CCS legislative/regulatory PDFs) — VADER's sentiment scores saturate near ±1 on this formal
register and are meaningless past a page or two.

## What I tried, and why VADER's replacement isn't "a different sentiment tool"

First read the existing pipeline (`extract_corpus.py`, `analyze_corpus.py`, `signal_terms.py`)
and the shared AI-assisted TA method doc (`Claude Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md`).
Two things changed my approach from "find a better sentiment model" to "drop sentiment as the
frame entirely":

1. **The genre problem, not just the tool problem.** Sentiment analysis measures emotional
   valence. Legislative bills, agency orders, and fiscal notes don't express emotion — they're
   procedural. Even a much better sentiment model (see SiEBERT note below) would mostly return
   "neutral" on this corpus, which isn't wrong, just uninformative. The shared TA method doc
   already flags this exact problem and points at Hartmann et al. (2023)'s SiEBERT transformer
   model as a better-performing *general* sentiment tool — I looked into running it (see
   "Technical dead end" below), but even if it ran, it's still the wrong construct for this genre.

2. **`signal_terms.py` already started the right pivot** (built 2026-07-07, one day before this):
   category-based keyword frequency instead of polarity. It was explicitly marked as
   "illustrative starting points... not a validated coding scheme" with generic categories
   (safety/risk, transparency, community, regulatory authority, economic benefit).

## What I actually built: theory-grounded coding mapped onto Track B's own framework

Rather than invent new categories, I pulled the actual theoretical model from
`CCS_Lit_Review_Foundation.docx` (Track B, the ERSS vignette paper) — its governance model is:

```
Governance frame -> Procedural justice perception -> Recognition justice perception
                  -> Institutional trust -> Perceived legitimacy -> Support for CCS
```

with six governance-frame vignette conditions (state regulator approval, industry/technical
expertise, local referendum/voting, property-rights protection, affected-community consultation,
Tribal/Indigenous consultation), Tyler's (2003) four procedural-justice criteria (voice,
neutrality, trustworthiness, dignitary treatment), and Terwel et al.'s (2009) competence-based
vs. integrity-based institutional trust distinction.

I built `theory_grounded_coding.py`, which counts these exact categories' keyword signatures
across the Track A corpus. This does double duty:
- Gives Track A a defensible, theory-anchored quantitative pass instead of ad hoc categories.
- Gives Track B empirical grounding it doesn't currently have: evidence that its six vignette
  governance frames aren't invented conditions but actually appear (in varying strength) in the
  real LA CCS regulatory corpus — a citable methods justification for frame selection.

**This ran successfully tonight** — output at `theory_grounded_coding_by_doc.csv` (per-document,
34 coding columns) and `theory_grounded_coding_corpus_summary.csv` (corpus-wide rollup with the
specific terms driving each count, for face-validity checking).

## Results (corpus-wide, N=18 documents) — genuinely interesting, not just plumbing

- **State regulator approval frame dominates**, appearing in all 18 documents (secretary,
  permit, "Class VI," authorization language) — expected for a regulatory corpus, but confirms
  this frame has strong ecological validity as a vignette condition.
- **Tribal/Indigenous consultation is thin**: only 5 of 18 documents, 62 total hits corpus-wide
  (vs. 2,938 for state-regulator language). **Named LA tribal nations appear by name only
  twice in the entire corpus** — one instance of "Tunica-Biloxi," nothing else. Coushatta,
  Chitimacha, Jena Band of Choctaw, and United Houma Nation are not named anywhere in these 18
  regulatory documents.
- This is a striking, directly citable finding for Track B's Indigenous-rights section: it
  empirically supports the lit review's own cautionary argument that Tribal consultation in CCS
  regulatory practice tends toward generic/token stakeholder framing rather than substantive,
  named engagement with specific sovereign nations — without you having to claim anything about
  Indigenous attitudes (the corpus is state/regulatory documents, not Tribal voices, so this
  stays safely in "what the regulatory text does/doesn't say" territory, consistent with the
  scope limitations Track B's lit review already insists on).
- **"Legitimacy" as a word barely appears** (6 hits total, 3 documents) — regulatory text is
  descriptive/procedural, not evaluative. Useful methodological note: legitimacy has to be
  theorized from the corpus, not directly measured from it — this corpus can't answer "is CCS
  seen as legitimate," only "what governance frames and procedural signals does the regulatory
  apparatus actually emphasize."
- Institutional trust language skews heavily toward integrity-based signals (367 hits:
  violation, penalty, enforcement) over competence-based signals (58 hits: qualified,
  expertise, certified) — the regulatory corpus talks much more about compliance/enforcement
  than about technical competence, which is itself an interesting asymmetry.

## Technical dead end worth flagging (reusable finding for future overnight work)

Tried `scikit-learn` for LDA/topic modeling as a statistical complement (mirroring the shared
method's "Phase 0 quantitative triage" concept, which calls for JMP Text Explorer — not
available/scriptable here). `pip install scikit-learn` succeeded, but importing it failed:
`ImportError: DLL load failed while importing _qmvnt_cy: An Application Control policy has
blocked this file.` This is the same family of problem already documented for `pdfplumber`/
`cryptography` on this ARM64 Windows machine — some compiled-extension packages get blocked at
the OS/policy level, not just an ARM64 wheel-availability problem. `torch` also isn't installed
and would likely hit the same wall. **Don't spend more time trying to install compiled
statistical/ML packages on this machine without checking this first** — pure-Python approaches
(regex/dict-based, like this script and the existing pipeline) are the reliable path here.

Separately: with only 18 documents, LDA/topic modeling would likely have been unstable/
uninterpretable anyway — topic models generally need many more documents to find stable topics.
The theory-driven coding frame is arguably the methodologically correct choice for this corpus
size regardless of the technical blocker, not just a workaround for it.

## Next steps for Britton

1. **Face-validity check the category term lists** in `theory_grounded_coding.py` — I built
   these from Track B's own construct definitions, but you know this corpus and this domain
   far better than I do. Terms are easy to add/remove (they're plain lists at the top of the
   script).
2. **Decide whether the Tribal-consultation/named-tribes finding belongs in Track A's own
   write-up, Track B's motivation section, or both.** It's a genuinely strong empirical anchor
   for the "consultation without jurisdictional engagement" argument already in the Track B lit
   review.
3. If you want true sentiment/tone scoring on some *other* text in this project later (e.g., a
   public comment, news coverage, or social-media text for Track C) — SiEBERT (Hartmann et al.,
   2023) is the citable, better-performing alternative to VADER. Not recommended for Track A's
   formal regulatory text itself, for the genre reasons above.
4. Existing VADER outputs (`sentiment_by_document.csv`, `sentiment_by_page.csv`) don't need to
   be deleted — just don't lead with them in the write-up; this new coding is the primary
   quantitative layer now.
