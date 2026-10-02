# Decision Log — Data Center Paper (EMPIRICAL, JPP&M target)

*Created 2026-10-02 by Claude (Opus 5.5) from `_RESEARCH_SYSTEM/templates/DECISION_LOG_TEMPLATE.md`. Earlier decisions (08-17 restructure, 09-10 scope lock) are recorded in `CLAUDE.md` and have not been back-filled here.*

Append-only. Newest at the top. Never rewrite history — supersede it.

This is the EMPIRICAL paper. The conceptual CSREM paper ("The Cloud Has a Zip Code…", BBA, P1–P6) has its own log at `DATA_CENTER_LEGITIMACY_PAPER\00_START_HERE\DECISION_LOG.md`. Do not mix the two.

---

## 2026-10-02 — Corpus breadth: include more, not less
- **Decision:** NY (#26), IN (#27) and MS/TN (#28) stay in the corpus. Breadth is the default: a verified case is added, not held out. The canonical count is now **28 case entries** (#16b is merged into #16 as an update).
- **Decided by:** Britton, in chat: "I would think more in the corpus is better as a general rule".
- **Why:** Britton's general preference for breadth.
- **Supersedes:** the 2026-09-10 scope-lock clause "Do not automatically expand Tier 2 into exhaustive artifact collection unless the emerging analysis shows that we need it", and its restriction of Tier 2 to GA/UT/VA/AZ. Louisiana stays the anchor/deep-dive case.
- **Consequences:**
  - The bookkeeping that still said 26 or "6 states" is corrected (corpus file, CLAUDE.md, Dashboard).
  - #25 (AZ) now has source URLs, taken from the 2026-08-19 note.
  - The notes' backlog of candidate leads is being inventoried in `04_DATA\candidate_leads_inventory_2026-10-02.csv`.
  - PROPOSED inclusion rule, NOT yet approved by Britton: a U.S. local or state data-center siting dispute from 2025–26, with at least one direct-fetched source (news or official record). WebSearch-summary-only leads stay out until fetched. Every added case gets Phase 1 codes before Phase 3. JPP&M reviewers will ask how cases were selected, so methods must state this rule.

## 2026-10-02 (later) — Inclusion rule APPROVED; full verification pass ordered
- **Decision:** The inclusion rule is approved. A case qualifies if it is a 2025–26 U.S. data-center siting dispute (local or state) with at least one source someone actually opened: a news article or an official record. Leads backed only by a WebSearch summary stay candidates until fetched. Separately, nightly sweeps must write their leads into structured files in `04_DATA\`, not only into narrative notes.
- **Decided by:** Britton, in chat: "yep, do it, need to get as much verified as possible and fix issues we keep seemingly having when it comes to nightly sweeps and not collecting that info into the correct folders for later use".
- **Why:** About 150 leads had piled up in `notes\` and never reached the corpus.
- **Supersedes:** the "proposed, awaiting OK" status of the rule in the entry above (this log is appended in order today; newest is at the bottom).
- **Consequences:**
  - A re-fetch pass is under way: the existing 28 entries plus the candidate leads. Output goes to `04_DATA\verification_2026-10-02\`.
  - `04_DATA\corpus_inventory.csv` becomes the single source of truth for N.
  - The nightly routine instructions are being changed to require structured lead capture.

## 2026-10-02 (evening) — Verification pass merged; corpus_inventory.csv is the corpus of record
- **Decision (bookkeeping under the approved rule, not a new design call):**
  - `04_DATA/corpus_inventory.csv` is built by `04_DATA/build_corpus_inventory.py` from fetch receipts. It holds **138 INCLUDED cases**: 27 of the original #1–28 plus 111 new (#29+).
  - #11 is **REMOVED**: its Axios source is a national polling story, not a July New Orleans pause.
  - 41 leads were EXCLUDED, each with its reason.
- **Decided by:** Claude, applying the rule Britton approved earlier today. Case typing is Claude's first pass, flagged `case_type_reviewed_by_britton=N`.
- **OPEN, Britton's call: which case types count toward the reported N?**
  - SITE_DISPUTE (a fight over a named project): 57
  - LOCAL_POLICY (moratorium/ban/ordinance/tax freeze): 72, of which NC 39 and KY 25 are mostly moratoria
  - STATEWIDE_POLICY: 9
  - The southern-states agent excluded pre-emptive moratoria with no opposed site. The NC/KY agent included them. Until Britton decides, report counts by type.
- **Corrections to the original entries:** see `verification_2026-10-02/verified_corpus_existing.csv`.
  - #21 is Box Elder County, not Millard.
  - #28 is the Oxford division, not Greenville. DOJ's intervention was denied 08-24 and DOJ appealed 09-18.
  - #6 is from 2025.
  - #27's vote was 01-20.
  - #23: the Oct 20 date is unsupported by its cited source (FOX 5 says Oct 13).
  - #9's "disproportionate share" quote and #18's income gap were not found in their sources.
  - #20: HB1063 is not in its sources.
- **Also built:**
  - `candidate_leads.csv` (living)
  - `watchlist.csv` (8 pending items with next_check)
  - `additional_sources_unverified.csv` (53 extra sources for existing cases)
  - `url_ignore.txt`
  - `tools/check_leads_captured.py` now reports UNCAPTURED: 0 across all 43+ notes.
