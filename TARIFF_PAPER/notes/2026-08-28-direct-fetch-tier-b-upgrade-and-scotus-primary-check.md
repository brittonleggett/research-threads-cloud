# 2026-08-28 — Direct-fetch verification of the 4 Tier-B artifacts + SCOTUS/IEEPA primary check

**Tooling note:** unlike the nightly cloud routine (still `EGRESS_BLOCKED` as of 2026-08-27),
this session's `WebFetch` works normally against most domains. Some individual sites still
blocked this pass for unrelated reasons (paywalls, bot-detection redirects) — noted per artifact
below, not a repeat of the routine's network-wide block.

## Tier-B artifacts — 3 of 4 upgraded to Tier A, 1 stays mixed

### La-Z-Boy — upgraded to Tier A
Direct-fetched [Supply Chain Dive](https://www.supplychaindive.com/news/la-z-boy-volumes-remain-steady-tariff-driven-price-hike/806496/)
and [the delay piece](https://www.supplychaindive.com/news/trump-furniture-cabinets-tariffs-delay/808681/).
Both confirm the existing draft's facts and add precision:
- **Names the executive for the first time**: SVP/CFO **Taylor Luebke** (not previously named in
  the corpus entry) — quote: 2025 price increases were "in the single digits," "the very low end
  of what we're hearing is out in the market." On future pricing: "we feel really good and
  well-positioned with 90% of our product made in the U.S." (the domestic-manufacturing-insulation
  angle already flagged holds up, now with the exact rationale in Luebke's own words).
- **Delay details are more specific than previously recorded**: the original planned Jan 1, 2026
  increase wasn't just "furniture" — it was kitchen cabinets/vanities going 25%→**50%** *and*
  upholstered furniture to **30%**. The White House's own fact sheet (per the article, published
  Jan 1, 2026) cites "ongoing productive negotiations regarding the imports of wood products"
  with the UK, Japan, and the EU as the stated reason for the delay, holding the 25% rate for
  another year.
- Recommend the corpus table's Tier column change B → A for row 9.

### Birkenstock — upgraded to Tier A
WWD and BoF both blocked (402/403 — paywall/bot-gate, not a content problem), but
[Supply Chain Dive](https://www.supplychaindive.com/news/birkenstock-2026-margin-hit-tariffs-bite/809309/)
fetched directly and confirms every element of the existing draft verbatim or near-verbatim: CFO
**Ivica Krolo**, ~100bp gross-margin/EBITDA decline expected, "the price increase would have to be
2.5x the tariffs. This is not something we would do to our customers, being a democratic brand,"
style-by-style seasonal pricing review. **New precision**: pins the statement to Birkenstock's
**December 18, 2025 earnings call** (article published Jan 15, 2026) — the corpus entry currently
just says "FY2026." Also surfaces one previously-uncaptured quote on long-term mitigation: growing
Asia-Pacific sales share will "for the longer term, reduce our exposure to the U.S. dollar and to
U.S. tariffs regime."
- Recommend the corpus table's Tier column change B → A for row 12.

### Insteel Industries — upgraded to Tier A, with one word-level flag worth a manual look
Direct-fetched the [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/07/23/insteel-industries-iiin-q3-2026-earnings-call-transcript/).
Confirms CEO **Howard Osler Woltz**'s freight-cost quote and the July 13, 2026 price-increase
date. **New precision**: the steel tariff is quantified at **50% on steel imports**, driving
domestic hot-rolled wire rod prices **50-100% above global market prices** — richer than the
original entry's generic "Section 232 steel tariffs" framing.
- **Flag, not resolved**: this session's fetch returned the quote as "when a **profit** cost
  $1,500 to send... now $3,000" — but this project's own standing correction (per
  `[[project_tariff_paper_pipeline]]` memory, applied 2026-08-18) already established the word
  should be **"freight,"** not "profit." My fetch used a summarization pass over the page rather
  than a verbatim capture, so "profit" here is *this fetch's* transcription, not independent
  confirmation of the original error. Don't treat either version as settled without a direct
  human read of the actual page — recommend whoever finalizes this quote for the manuscript opens
  the Motley Fool page directly and reads the sentence themselves rather than trusting either
  AI-mediated version.
- Recommend the corpus table's Tier column change B → A for row 14, with the above caveat
  attached to the exact quote wording specifically (not the underlying fact, which is solid).

### Home Depot — stays mixed confidence, but the standing correction is independently re-confirmed
The Hill (403) and CFO Dive were the two targets; CFO Dive fetched successfully and Yahoo Finance
(not in the original source list, found via the same search) also fetched successfully. Both
**independently reconfirm** the 2026-08-18 correction already on record: the Aug 2025 "modest
price movement... not broad-based" quote belongs to **EVP William Bastek**, not CFO Richard
McPhail — Yahoo Finance's own framing: "Billy Bastek, Home Depot's merchandising chief" made the
May 2025 no-broad-increases statement, and CFO Dive's direct fetch is explicit that "McPhail's
quoted comments focused on customer strength and macroeconomic confidence rather than tariff
pricing specifically," while the actual pricing quote is Bastek's.
- **Action needed, not taken here (out of scope for this pass):** `Study1_Corpus_and_Coding_
  DRAFT_2026-08-21.md`, artifact 15's Phase-1-codes writeup (line ~142) still says "CFO Richard
  McPhail reversed" — the 08-18 correction did not get carried into the 08-21 consolidation.
  This is a real, if small, drift between two of the project's own documents; flagging plainly
  rather than silently fixing it, since it touches Phase 1 coding text, not just a source-tier
  label. Two independent re-fetches tonight agree with the 08-18 correction, so confidence this
  needs fixing is high.
- Digital Commerce 360 (the fourth source for this artifact) not re-checked this pass — time
  budget went to the other three artifacts and the SCOTUS check instead.

## SCOTUS/IEEPA — case name and docket numbers pinned down; opinion PDF itself still not reached

`supremecourt.gov`'s slip-opinion index and `federalregister.gov`'s search both blocked this pass
(403 and a bot-detection redirect respectively) — the actual primary documents remain unreached,
same gap the 08-14 note flagged. But WebSearch this session surfaced the exact case name and
docket numbers, which the prior WebSearch-only pass didn't have, and a Wikipedia fetch (treat as
tertiary, not primary, but useful for orientation and citation-hunting) added real precision:

- **Case: *Learning Resources, Inc. v. Trump* and *Trump v. V.O.S. Selections, Inc.*** (consolidated),
  docket **24-1287 and 25-250**. Argued Nov 5, 2025, decided Feb 20, 2026.
- **Vote structure is more nuanced than "6-3" alone conveys**: 6-justice majority (Roberts,
  Sotomayor, Kagan, Gorsuch, Barrett, Jackson) on the bottom-line holding, but only a
  **3-justice plurality** (Roberts, Gorsuch, Barrett) on the major-questions-doctrine reasoning.
  Two dissents, not one bloc: Thomas solo, and Kavanaugh joined by Thomas and Alito. Worth knowing
  if the paper ever characterizes the ruling's reasoning, not just its outcome.
- **Direct quote from the opinion** (via Wikipedia, not independently verified against the slip
  opinion itself — flag before quoting in a manuscript): Roberts — "Based on two words separated
  by 16 others in [IEEPA]—'regulate' and 'importation'—the President asserts the independent power
  to impose tariffs on imports from any country, of any product, at any rate, for any amount of
  time. Those words cannot bear such weight."
- **New macro-context fact, independently cross-corroborated via two sources tonight** (Wikipedia
  and a WebSearch pass over law-firm client alerts — White & Williams, Holland & Knight, Snell &
  Wilmer, Norton Rose Fulbright, Ginger Control): CBP estimates **~330,000 importers paid or
  deposited approximately $166 billion in IEEPA duties across 53+ million entries**. CBP's CAPE
  refund system went live April 20, 2026; **as of July 10, 2026, CBP had accepted ~$121.75 billion
  in refund claims and repaid ~$86.3 billion (including statutory interest)** — a close match to
  Wikipedia's "~$81 billion by July 2026" figure, different snapshot dates, consistent order of
  magnitude. **This is a genuinely useful macro-context number for the refund-era-wave corpus-scope
  question** (the individual company disclosures already gathered — Target $994M, Home Depot,
  Walmart, Lowe's $80M, Williams-Sonoma $47M+$10M — are now placeable against a real aggregate:
  they're a handful of named data points inside a $166B/330,000-importer universe, which is a much
  stronger framing sentence than citing the individual companies alone). Not yet added to any
  corpus file — flagging here for whoever writes up the refund-wave section next.
- **Still not done**: an actual primary-text read of the SCOTUS slip opinion, the Section 122/301
  Federal Register notices, and the CIT's May 7, 2026 ruling. Recommend trying `supremecourt.gov`'s
  specific opinion PDF URL directly (not the index page, which 403'd) once the exact PDF filename
  is known, and trying a Federal Register direct-document URL rather than its search endpoint
  (which triggered a bot-check redirect) next time this is attempted.

## What's still open (unchanged from before this pass, restated)

- Home Depot's McPhail→Bastek correction needs to actually get applied to the 08-21 consolidated
  draft — a small edit, not a judgment call, but real work not done in this pass.
- Insteel's "freight" vs. "profit" quote wording needs one human eyeball on the actual transcript
  page before it goes in a manuscript.
- The corpus-scope question (does the refund-era wave get added as new rows?) is unchanged and
  still Britton's call — the new $166B/$86.3B macro figures found tonight make the case for
  inclusion stronger, not weaker, but that's an observation, not a decision made here.
- SCOTUS/Federal Register primary-text reads are still outstanding.
