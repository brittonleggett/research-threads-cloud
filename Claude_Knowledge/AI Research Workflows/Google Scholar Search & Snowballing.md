# Faster literature search: Google Scholar operators + snowballing (2026-08-11)

Source: real transcripts, not just titles —
- "The Insanely Effective Way to Use Google Scholar" (youtube.com/watch?v=dsBzBvbtGO4)
- "A Complete Guide to using Google Scholar for Advanced Literature Search" (youtube.com/watch?v=omycDeF_soI)
- Oxford Bodleian Libraries, "Introduction to Systematic Reviews and Evidence
  Syntheses — Video 4: Snowballing and write up" (official transcript PDF)

Two techniques that stack: **search operators** to get a sharper first cut, then
**snowballing** to fill the gaps a keyword search always misses.

## Google Scholar search operators (most researchers never learn these)

- `AND` / `OR` / `-` (minus, no space before the excluded term) — must be
  **capital letters** to register as Boolean logic, not literal words.
  Example: `(cancer OR oncology OR tumor) AND "drug resistance"`
- Quotation marks force an exact phrase match — dramatically narrows noisy results.
- Parentheses group terms, same as algebra — needed once you combine AND/OR.
- `intitle:"social media"` — restricts the match to the paper's title, not
  abstract/body. Very high-precision filter when you know the term should be
  central to the paper, not incidental.
- `author:"Last First"` — pulls everything by a specific author.
- `source:` — restricts to a specific publisher/journal platform (e.g. Springer).
- Minus a topic to kill an ambiguous-term problem, e.g. `mercury -planet` to
  keep the chemical and drop the astronomy hits.
- Minus `-review` to exclude review articles and get only original studies, or
  minus `-research` to flip it and surface mainly reviews — good for finding a
  review article to orient yourself before diving into primary studies.
- **Keyword discovery when starting a new area:** type a root term into Scholar's
  or Google's search box and watch autosuggest, or walk the alphabet after the
  term (`solar cell a...`, `solar cell b...`) to surface field-specific vocabulary
  you wouldn't have guessed; or pull terms off the topic's Wikipedia page; or ask
  Claude directly for the standard keyword set in a field before you start searching.
- **Advanced Search panel** (hamburger menu, top-left) exposes all of the above as
  a form: exact phrase / at least one of the words / without the words / where
  words occur (title vs. anywhere) / author / published in / date range — worth
  using directly instead of hand-building query strings.
- **Follow an author**: click their name on a result (if underlined/linked) →
  it opens their Scholar profile → you can follow them and get emailed when
  they publish. Good for staying current on the 3-4 researchers who anchor a
  given literature.

## Snowballing (backward + forward citation chaining)

The Oxford library's own framing: **up to 51% of a systematic review's final
reference list is typically found via snowballing, not the original keyword
search.** It's not optional polish — it's how you catch what the search misses.

- **Backward snowballing** — read the reference list of a paper you've already
  confirmed is relevant (or a good review article) and check those citations too.
- **Forward snowballing** — click "Cited by" on Google Scholar (or "Similar
  articles"/"Cited by" on PubMed) to see who has cited that paper *since* it
  came out. This is how you find work newer than your original search date.
- You can chain further: inside a "Cited by" results page, run a **second
  search within those citing articles** to narrow toward a sub-topic, sorted
  by date for the most recent angle.
- Also check "Related articles" — Scholar/PubMed's own similarity algorithm,
  a free second opinion on top of your own search terms.
- Compare source-by-source: the same paper can show very different "Cited by"
  counts on Scholar vs. PubMed (e.g. 52 vs. 15 in the demo) — worth checking
  both if a topic matters enough.
- **Grey literature** (conference abstracts, dissertations, preprints like
  medRxiv/SSRN, registered-but-unpublished protocols, organization reports)
  sits outside normal database indexing — matters more for qualitative/mixed-
  methods work, less for straightforward empirical studies. Worth a targeted
  pass only when a topic seems thin in the standard databases.
- **Keep a running log while doing this** — what you searched, on which
  platform, how many "cited by"/"related" results you screened, how many you
  kept. This is exactly the kind of paper trail a Methods/PRISMA-style writeup
  wants, and it's much easier to log as you go than to reconstruct later.

## How this fits with Claude

Once you've pulled a shortlist of papers via search + snowballing, drop them
into a project's local folder and use the structured-annotation prompt from
`Zotero-Claude Structured Annotation Template.md` (works the same pointed at
local PDFs — see [[feedback_zotero_deprioritized]]) to get per-paper theme
relevance, then ask me directly to compare/synthesize across the set or spot
gaps, the same way the Zotero-library workflows did — just without Zotero.
