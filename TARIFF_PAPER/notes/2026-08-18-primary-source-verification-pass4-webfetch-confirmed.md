# 2026-08-18 — Primary-source verification, pass 4: WebFetch restored, upgrading pass 3's WebSearch-only entries

**Infrastructure note first, because it changes what's possible going forward:** `WebFetch` had
been blocked for 6+ consecutive overnight sessions (per the 2026-08-17 overnight summary and
pass 3's own caveat). It works again as of this session — tested and confirmed against
supplychaindive.com, fool.com, and cfodive.com. One source (thehill.com) still returned a
site-specific 403, which is a normal per-site block, not the network-wide egress failure seen
before. Worth telling Britton this changed, since several open items across Tariff/CCS/Data
Center have been sitting on "re-verify once WebFetch works again."

This pass re-fetches the sources pass 3 (2026-08-14) only had at WebSearch-summary confidence,
per the paper's own citation-rigor standard (`Overnight_Citation_Verification_2026-07-08.md`).
Not new corpus candidates — same four artifacts (La-Z-Boy, Birkenstock, Insteel, Home Depot),
now confirmed against the actual source pages.

## #9 La-Z-Boy — confirmed, no changes to pass 3's read

Fetched Supply Chain Dive's furniture-tariff-delay piece directly. Confirms: the Jan 1, 2026
furniture-tariff hike (cabinets/vanities 25%→50%, upholstered furniture →30%) was delayed a
year by the White House, "given the ongoing productive negotiations regarding the imports of
wood products." Confirms the La-Z-Boy line verbatim: "La-Z-Boy raised prices following the
implementation of the 25% furniture tariff, but the company expected to maintain its current
pricing even if the duty rate jumped further, executives said in November." Pass 3's read holds:
`causation-explicit` for the 2025 increase, but the "no further increase anticipated" /
domestic-manufacturing-insulation angle is real and complicates treating this as a clean
pass-through exemplar. Still a Phase 3 call.

## #12 Birkenstock — confirmed and one detail added

Fetched the Supply Chain Dive margin piece directly. All of pass 3's Krolo quotes confirmed
verbatim, including the "2.5x the tariffs... not something we would do to our customers, being a
democratic brand" quote and the 60%→54.5% margin math. **New from the direct fetch:** Krolo also
said "This will not be the case in 2026" — referring to 2025's frontloading/price-increase
strategy no longer being available as an offset — and "But this naturally takes time" on
longer-term mitigation (production efficiencies, logistics, supplier renegotiation). Source dated
to the December 18, 2025 earnings call. Strengthens the `partial-absorption-quantified` and
`mitigation-narrative` codes pass 3 proposed.

## #14 Insteel — confirmed, one wording discrepancy worth flagging

Fetched the Motley Fool transcript directly. Confirms Section 232 attribution and the domestic
steel price story: "the tariff caused market prices in the US for hot rolled wire rod...to rise
to a level that is 50% to 100% over the global market price," and "US hot rolled steel prices
have risen so high relative to world market levels that the effectiveness of the derivative
tariffs is compromised." **Wording discrepancy:** pass 3's quote reads "when a **freight** cost
$1,500 to send to a destination now $3,000 somebody's gotta pay the bill" — this fetch's OCR/
extraction rendered the same sentence as "when a **profit** cost $1,500..." "Freight" is almost
certainly correct (fits the sentence; "profit" doesn't make grammatical sense there) — flagging
so whoever quotes this in the manuscript pulls the $1,500/$3,000 freight-cost framing, not the
garbled "profit" version, and ideally checks the transcript once more before final citation.

## #15 Home Depot — one attribution correction

Fetched CFO Dive's coverage of the August 2025 earnings call directly. **Correction to pass 3:**
pass 3 attributed the "some modest price movement for some categories... not on a broad scale"
quote to CFO Richard McPhail. The direct fetch attributes it to **EVP William Bastek**, not
McPhail — McPhail's own remarks in this source focus on customer financial health ("very
healthy," citing home equity access) rather than pricing directly. The line pass 3 used to date
the reversal — "tariff rates are significantly higher today than they were when we spoke in
May" — is confirmed, dated to the August 20, 2025 (Q2) earnings call, but should be checked for
speaker attribution before it goes in a manuscript as a McPhail quote. Could not re-verify the
May 2025 "no broad-based price increases" original statement or the May 2026 follow-up in this
pass (The Hill's piece 403'd; didn't chase the other two pass-3 sources for those legs given time
— still open). Home Depot's three-beat reversal-arc story from pass 3 stands, but the August-2025
speaker needs fixing to Bastek (or a direct fetch of the actual earnings-call transcript, which
would be the cleanest fix) before manuscript use.

## What's still open

1. Home Depot's May 2025 and May 2026 legs weren't re-fetched this pass — only the August 2025
   middle beat was confirmed/corrected. Worth a follow-up pass if Home Depot stays in the corpus.
2. All four entries are now at "directly fetched, one hop from primary" confidence rather than
   WebSearch-summary confidence, but none of this is a fetch of the actual underlying transcript/
   press release — still one more hop below true primary-source confidence for a citation-rigor
   bar this strict. Fine for corpus/coding purposes; worth knowing before citing page/paragraph
   specifics in the manuscript.
3. La-Z-Boy's design question (pass-through exemplar vs. counter-example) is still Britton's
   Phase 3 call, untouched here.
4. The SCOTUS/IEEPA legal-sequence question flagged in `2026-08-14-scotus-ieepa-legal-sequence-
   confirmed.md` is still open and, with WebFetch now working, is probably the highest-value next
   research task — that note recommended a direct-fetch pass against the actual Supreme Court
   opinion and Federal Register notices once WebFetch was restored. That's now possible but
   wasn't attempted this pass (out of scope for what was asked — flagging, not doing).
