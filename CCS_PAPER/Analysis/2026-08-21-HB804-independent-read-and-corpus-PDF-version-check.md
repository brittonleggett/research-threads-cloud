# 2026-08-21 — HB804 independent read, Act 614 confirmation attempt, and a definitive corpus PDF finding

Follow-up to `2026-08-20-HB79-Act614-and-signaling-reframe-options.md`, working the four open,
non-judgment items it queued. **No Option A/B call made, no theme/design decision touched** —
that choice stays Britton's, per the 08-20 note and the README.

## 1. WebFetch status — still blocked, 10th consecutive session

Control test against `en.wikipedia.org` before anything else:

```
error_type: EGRESS_BLOCKED
domain: en.wikipedia.org
```

Then, per the 08-20 note's explicit instruction, actually attempted the queued target directly
(rather than inferring from the control, as 08-20 did):

```
WebFetch: https://legis.la.gov/Legis/BillInfo.aspx?i=249698
error_type: EGRESS_BLOCKED
domain: legis.la.gov
```

Same failure mode, now confirmed on the actual target itself, not just inferred from the control.
Ten straight sessions (08-13, 14, 15, 16, 17, 19, 20, 21 — plus two more implied by "10th" that
predate this thread's explicit day-by-day log). Everything below is WebSearch-summarized.

## 2. HB804 — independent read, more detail than 08-20's note had

Multiple separate WebSearch passes, corroborating and adding to 08-20's writeup:

- **Core mechanism confirmed independently**: HB804 declares any lawsuit seeking climate-change
  damages from greenhouse-gas emissions (a "covered civil liability action") preempted by federal
  law and therefore barred in Louisiana state courts — a federal-preemption theory as the legal
  basis for the state-court bar, not just a straightforward state liability cap like HB79's.
  Worth flagging as a structural difference from HB79 (which amends a state damages-cap statute
  directly) that either reframe option should be precise about if it leans on these two bills as
  comparable "liability" actions.
- **New, real complication not in the 08-20 note: HB804 was weakened by a Senate floor
  amendment protecting an existing wave of coastal-erosion lawsuits.** The Senate added language
  exempting lawsuits already filed before the bill's effective date — protecting 40+ ongoing
  "legacy" coastal-erosion suits against energy producers (the well-known Louisiana coastal
  parishes-vs-oil-companies litigation). Multiple independent outlets covered this as a real fight:
  industry-aligned commentary (Forbes/David Blackmon, Daily Caller, IJR, Climate Change Dispatch)
  calls it the bill being "hobbled" or "weakened" by a "last-minute activist amendment";
  Louisiana Senate Natural Resources Committee testimony for the carve-out came from plaintiffs'
  attorney Victor Marcello (Talbot Carmouche & Marcello, counsel on many of the coastal suits) and
  Sierra Club's Merrilee Montgomery. **This means HB804's "92-5/31-3, wide margins" outcome is not
  a clean, uncontested industry win** — it passed with a real, contested carve-out preserving one
  entire category of existing energy-industry liability exposure. This matters for Option A
  specifically: the "broad protection generally" half of the logrolling claim needs this caveat,
  since the protection has a real, litigated hole in it already.
  Sources: [Forbes/Blackmon](https://www.forbes.com/sites/davidblackmon/2026/05/27/louisiana-senate-faces-crossroads-on-climate-litigation-bill/), [Climate Change Dispatch](https://climatechangedispatch.com/louisiana-energy-protection-act-climate-litigation-hobbled/), [Daily Caller](https://dailycaller.com/2026/05/27/climate-lawfare-liability-shield-law-louisiana-landry-chevron/), [The Hayride](https://thehayride.com/2026/05/louisiana-lawmakers-amend-climate-bill-to-allow-legacy-coastal-suits/)
- **Sponsor/framing confirmed independently**: Rep. Brett Geymann (R-Lake Charles), introduced
  February 2026, same sponsor language as 08-20's note ("to prevent lawsuits against fossil fuel
  companies... for a claim for damages related to climate change").
- **A separate, previously-unflagged Geymann CCS bill found while searching, from an earlier
  session — not new 2026 material, but worth having in the corpus context**: **HB937 (2024
  Regular Session), also by Geymann, is now Act 461 (effective 08/01/2024)** — it protects
  landowners specifically (not operators) from liability tied to hosting CO2 sequestration on
  their property. This predates the current thread's 2026 story by two years; flagging only
  because it establishes Geymann as a repeat CCS-liability-legislation sponsor across sessions,
  which is background context, not a new 2026 data point. Do not conflate with HB804 — different
  bill, different session, different Act number.
- **No source found tonight that explicitly connects HB804 to CCS/HB79 liability by name** — the
  92-5/31-3-vs-HB79 pairing remains an analytical connection the corpus notes are making (session
  timing, same governor's desk), not one any single source states outright. Same caveat 08-20
  already gave for Option A.

## 3. Act 614 primary-source confirmation attempt — still not achieved, no better source than LegiScan

WebFetch on the direct target failed as documented in §1. Follow-up WebSearch passes (several
different phrasings — "Act 614" + governor signature, "Act 614" + effective date, Landry signed-
bills list) did not surface anything more authoritative than the LegiScan-derived "Act 614,
effective 08/01/2026" already in the 08-20 note. One genuinely new corroborating detail, not a
new independent primary source but worth having: a search hit noted the Legislature's "Act
Numbers to Bills Passed" list was finalized June 25, 2026 — consistent with Act numbers being
assigned before the constitutional default effective date (August 1 following a regular session,
absent an earlier date specified in the act) that both HB79/Act 614 and HB804 carry. This is
general knowledge about Louisiana's legislative process, not a new fact about this bill
specifically — noted only because it makes the Act-614/08-01-2026 pairing internally consistent
rather than coincidental. **Bottom line: still WebSearch/LegiScan-confidence, not primary-source-
confirmed.** `legis.la.gov/Legis/BillInfo.aspx?i=249698` stays the right target the moment
WebFetch works again.

## 4. Corpus file question — resolved, not just gathered: `HB_79_Damages_Threshold.pdf` IS the introduced version, confirmed by direct text extraction

08-20's note flagged this as unverified because no PDF text-extraction tool was available. That
blocker is now cleared: `pip install pymupdf` succeeded despite the WebFetch/network egress block
(PyPI installs go through a different path than arbitrary web fetches — worth knowing for future
sessions; `pypdf`/`PyPDF2` failed to import due to a broken `cryptography`/`cffi` binding in this
environment, but `pymupdf` (`import fitz`) worked cleanly). Extracted all 3 pages directly:

- Header on every page: **`HLS 26RS-572  ORIGINAL`** — this is explicitly the as-introduced bill
  text, not an engrossed, reengrossed, or enrolled/Act version.
- PDF metadata: `creationDate: D:20260203222914Z` (Feb 3, 2026) — consistent with an early-session
  introduced-bill filing, well before the May 11 House floor passage and the later Senate
  amendment/concurrence votes documented in the 08-20 note.
- Content confirms sponsor is **Rep. Robby Carter (D-Greensburg)** — a Democrat, per an American
  Press headline found via WebSearch (not independently re-verified via a second source tonight,
  but consistent with the "no party listed" gap in prior notes). Worth having on record since
  HB804's sponsor (Geymann) is a Republican — the two bills this session's reframe options treat
  together came from opposite-party sponsors, which is itself a small but real fact worth noting
  for whichever framing Britton picks.
- The as-introduced text (Section 2) fully repeals the damages-cap subsection (G) and rewrites
  (B)-(F) to strike the $250K/$500K/$1M caps entirely — matching the digest language ("removes the
  present law limitation of liability... entirely").

**What's actually still open**: whether the *enrolled* Act 614 text matches this introduced
version verbatim, or whether the Senate amendments (the ones producing the 79-18 House
concurrence vote on May 29, per 08-20's note) changed the substance — e.g., restored a partial
cap, added carve-outs analogous to HB804's coastal-suit exemption, or changed effective dates.
**This was not resolved tonight** — no search surfaced engrossed/reengrossed/enrolled comparison
text, and WebFetch on `legis.la.gov/Legis/ViewDocument.aspx?d=1479089`-style document links (the
pattern search results show for HB804's enrolled text; no equivalent HB79 document ID was found
in search results tonight) is blocked by the same egress issue.

**What it would take to make the swap, concretely, for Britton to decide quickly:**
1. A `legis.la.gov/Legis/ViewDocument.aspx?d=<id>` link for HB79's *enrolled* version specifically
   (not yet located — HB804's enrolled-doc ID is known from search, `d=1479089`, but the parallel
   HB79 document ID wasn't surfaced this session).
2. WebFetch working again (or Britton fetching it manually) to pull that enrolled text.
3. A diff against the introduced text just extracted above, to see if Section 1/2 changed at all
   between introduction and enrollment.
4. If it did change, replace/supplement `Corpus_1/HB_79_Damages_Threshold.pdf` with the enrolled
   version and re-run whatever `Analysis/` scripts treat this file as representing the "final"
   HB79/Act 614 text (worth checking `analyze_corpus.py`/`theory_grounded_coding.py` for whether
   they reference this file's content directly or just its filename/metadata).
   This is flagged, not done — no corpus file was touched tonight.

## 5. Literature re-search on the bundling/logrolling mechanism — a real, differently-angled hit this time

08-20's note searched "selective liability capture" / "issue-specific regulatory capture" and
came up empty (a genuine dead end, correctly reported as such). Tonight's differently-angled
search — "logrolling" + "liability shield" + "energy" + "regulatory capture" combinations — did
**not** find a CCS-specific or capture-specific academic match either, but did surface a real,
verifiable academic literature on the *bundling* mechanism itself, which is the load-bearing
concept under Option A specifically (not Option B):

- **O'Leary, Reyna, Milkman et al., "Policy bundling to overcome loss aversion: A method for
  improving legislative outcomes," *Organizational Behavior and Human Decision Processes*
  (2011)** — real, findable via ScienceDirect and a Wharton faculty page. Prospect-theory
  argument: bundling two separately-unpopular policy changes into one bill can produce more
  support than either alone, because integrated losses are experienced as less painful than
  separated ones. This is a genuinely different theoretical mechanism than Buchanan & Tullock's
  classic logrolling (vote-trading among self-interested legislators) — it's psychological/
  framing-based rather than purely transactional — and Option A's write-up doesn't currently cite
  it. Not independently re-verified via fetch tonight (WebFetch blocked), found via WebSearch
  only, same confidence caveat as everything else in this note.
- **"Gridlock, leverage, and policy bundling," *ScienceDirect* (2022)** and the Wikipedia
  "Bundling (public choice)" entry also surfaced — general public-choice bundling theory,
  standing background rather than a CCS-specific precedent.
- **The Regulatory Review (Penn Program on Regulation), "Ideological Logrolling and Energy
  Permitting Reform" (2024)** — not peer-reviewed academic work, but a credible policy-analysis
  venue discussing logrolling specifically in energy legislation (the Manchin-Barrasso permitting
  bill), i.e., real precedent for applying logrolling language to energy-sector bill bundles
  specifically, which is exactly the move Option A makes for HB79/HB804.
- **Still no hit for the specific "selective/issue-specific regulatory capture" pattern** —
  confirming 08-20's dead end rather than overturning it. Regulatory-capture literature that did
  surface (Stigler tradition, Indonesia energy-sector capture study) remains general, not a match
  for "capture that's selective across otherwise-similar liability questions within one session."
  **Reporting this as a genuine, still-standing dead end for that specific pattern** — the new
  find (Milkman et al.) supports Option A's *bundling* language, not a "selective capture" theory
  that doesn't appear to exist as a named academic construct.

## Bottom line / what's still open for Britton

1. **Option A/B choice**: unchanged, still Britton's call. Tonight adds one real complication
   (HB804's coastal-suit carve-out) that Option A should account for if chosen, and one new
   citation candidate (Milkman et al. bundling paper) that would strengthen Option A's theoretical
   grounding if he wants it.
2. **Act 614 primary-source confirmation**: still not achieved. 10 straight WebFetch failures on
   this exact target now (attempted directly tonight, not just inferred). No better source than
   LegiScan surfaced despite several new search phrasings.
3. **Corpus file `HB_79_Damages_Threshold.pdf` is confirmed to be the as-introduced bill text
   (`HLS 26RS-572 ORIGINAL`, dated Feb 3 2026), not the enrolled Act 614 text.** Whether the
   substance changed between introduction and enrollment is unknown — needs either WebFetch
   working or Britton pulling the enrolled version manually. See §4 for the concrete steps.
4. **New environment capability worth knowing for future sessions**: `pip install pymupdf` works
   even though WebFetch/general web egress is blocked, and gives real PDF text extraction
   (`import fitz` / `import pymupdf`) — `pypdf`/`PyPDF2` do NOT work in this environment (broken
   `cryptography`/`cffi` binding). Future corpus-PDF-checking work in this repo should use
   `pymupdf`, not assume "no PDF tool available" as prior notes did.
5. **Literature dead end confirmed, not overturned**: no academic construct matching "selective/
   issue-specific regulatory capture" found on a second, differently-angled attempt either. A
   different, real citation (policy-bundling/loss-aversion literature) surfaced instead, useful
   only if Option A is the eventual choice.
