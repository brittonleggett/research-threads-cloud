# 2026-08-21 — Study 1 corpus addendum: firming up #20-21 and five new candidate artifacts

Addresses two open items from `Study1_Corpus_and_Coding_DRAFT_2026-08-16.md`'s "what's Britton's
to do next" list (#4: firm up thin/carried artifacts with direct-fetch-equivalent verification)
and the task's mandate to continue expanding real-world grounding, matching how Data Center
Paper's corpus has been expanded over time. **All sourcing below is WebSearch-summary
confidence, not direct fetch** — WebFetch confirmed egress-blocked again this session (10th
straight), same flag as `2026-08-21-literature-verification-pass.md`. Multiple independent
outlets corroborate each item below, which is stronger than single-source WebSearch color, but
still short of the direct-fetch standard #1-16 in the original corpus met.

**This is an addendum, not an edit to `Study1_Corpus_and_Coding_DRAFT_2026-08-16.md` itself** —
per the project's "new dated files, not overwrites" convention. If Britton wants these folded
into the main corpus table, that's a small mechanical edit once he's reviewed this.

---

## Part 1 — Firming up #20 (El Cerrito) and #21 (Appleton), previously "WebSearch-confidence
only, not re-verified"

**#20. El Cerrito, CA** — multiple corroborating outlets (KALW, Local News Matters, NBC Bay Area,
Contra Costa News, ccpulse.org) confirm and sharpen the original entry: City Council voted **3-2**
in May 2026 not to renew its Flock contract; cameras (40 total) went dark **June 7, 2026**, full
removal completed by end of July. Driving issue: an internal review found **federal agencies had
accessed the city's camera data without local police knowledge** — the same "undisclosed default
access" pattern as Theme 2 (Bend, Evanston, Syracuse, etc.), not a new mechanism. More than an
hour of public comment, dozens of speakers opposing on privacy/unauthorized-sharing grounds.
Contract termination saves the city an estimated $315K over three years. **Upgrade from
"WebSearch-confidence only" to "multi-source WebSearch-triangulated," matching the confidence
tier of #3/#6/#7/#8/etc. in the original corpus** — still recommend a direct fetch of one primary
source (e.g., the ccpulse.org or Local News Matters piece) before treating it as citation-grade
for a specific quote.

**#21. Appleton, WI** — multiple corroborating outlets (WBAY, WFRV, Fox11, WTMJ, NBC26) confirm
and sharpen: **Mayor Jake Woodford** announced the city would stop using Flock cameras, citing
"concerns about the integrity of Flock's underlying system" that eroded trust — matching the
original entry's paraphrase almost exactly, now with the mayor's name attached. Cameras stopped
June 30, 2026 and were physically covered. Notably, Woodford's stated reasoning explicitly cites
**the Menasha and Milwaukee officer-misuse cases below** as evidence of accountability problems
"not under the City of Appleton's control as a customer" — i.e., Appleton's rejection is
partly *caused by* the individual-misuse pattern that Part 2 below documents, a real
cross-artifact link worth noting in write-up. **Upgrade to multi-source WebSearch-triangulated,
same caveat as El Cerrito above.**

---

## Part 2 — New candidate artifacts (not yet in the corpus; recommend adding, pending Britton's
review)

### #23. Menasha, WI — officer convicted of stalking ex-girlfriend via Flock network (individual
misuse)

Former Menasha PD officer **Cristian Morales** was charged with misconduct in office for using
the Flock network to track his ex-girlfriend — reportedly **7 off-duty searches spanning between
~15,000 and ~92,000 individual cameras nationwide**, attempting her specific vehicle plate 5 times
in early October. Pleaded no contest; a judge **rejected a lighter plea-deal recommendation and
sentenced him to 6 months in jail**, 3 years' probation, a $250 fine, and a permanent bar from law
enforcement work or Flock system access (sentencing reported 2026-08-17/18, multiple outlets:
Fox11, Wisconsin Examiner, WTAQ, WHBY, others). **Real, named, adjudicated, multi-sourced — this
is a materially stronger evidentiary anchor for Theme 3 (function creep/individual misuse) than
either #5 (Texas, thin/single-source) or #19 (ABC, headline-only) in the original corpus.**
→ Codes: `individual-misuse-function-creep` (existing code, now with a much stronger anchor),
`dread-risk-personal`, `formal-legal-accountability-individual` (new — this is the first corpus
artifact where an individual misuser, not an institution, faced formal legal consequences).

### #24. Milwaukee, WI — two separate officers charged with Flock misuse (individual misuse, same
pattern, independent instances)

- **Officer Josue Ayala**, charged with attempted misconduct in public office: used Flock readers
  **179 times** to track someone he was dating and that person's ex. Misuse surfaced after the
  victim checked their own plate on a public tracker (**haveibeenflocked.com**) and reported it —
  itself a notable detail: public-facing self-audit tools are now part of how these cases surface.
- **Detective Tehrangi Chapman**, charged with misconduct in public office: used the department's
  Flock system to track two people (20 unauthorized searches), including placing a **physical GPS
  tracker** on one person's car and monitoring it 17 times from 2019-2025. Reported irony,
  multi-sourced: Chapman had been the officer **assigned to investigate the department's earlier
  Flock-misuse case** (presumably Ayala's) before being charged with the same conduct himself.
  Sourced across FOX6, NBC26, WTMJ, WPR, SAN, Fox11, ACLU-WI, CNN, Gadget Review.

**Aggregate figure worth citing, if it holds up on a direct-fetch check:** the search summary
attributes to the **Institute for Justice** a count of **"at least 21 cases since 2024 in which
officers were accused of accessing Flock data for personal use, with most facing criminal
charges"** — if verified, this converts Theme 3 from "two thin anecdotes" into a documented
national pattern with a real denominator, a significant upgrade. **Flag clearly: this specific
number was not independently confirmed beyond the WebSearch summary attributing it to IJ — treat
as WebSearch-confidence pending a direct-fetch check of the actual IJ source before it appears in
any draft as a citation-grade statistic.**
→ Codes: same as #23, plus `self-audit-tool-discovery` (new — haveibeenflocked.com as a
discovery mechanism, worth naming as its own detail).

### #25. Mountain View, CA — federal/state agencies accessed camera data without city or PD
consent (institutional secrecy, new state actor detail)

City officials found, via internal audit, that **multiple federal agencies** (ATF field offices
in Kentucky and Tennessee, Langley Air Force Base, a U.S. GSA Office of Inspector General office,
Lake Mead National Recreation Area, and an Ohio Air Force base) accessed data from a single
Mountain View Flock camera **August-November 2024**, via the same kind of nationwide-search
default (enabled by Flock, not approved by Mountain View PD) as Bend's "National Lookup" case.
**A second, distinct finding in the same story:** a separate statewide search function let
**California law-enforcement agencies** access data from **29 of the city's 30 cameras**, also
without city approval — a state-level, not just federal-level, version of the same undisclosed-
default mechanism. City response: suspended and is shutting down the LPR system. Multi-sourced
(ABC7 News, Yahoo, AOL). **This is a strong, specific, multi-agency addition to Theme 2** —
arguably the single most granular "who exactly accessed the data, and how many cameras" account
in the corpus so far, stronger on specificity than several of the original six Theme-2 artifacts.
→ Codes: `default-opt-in-secrecy` (existing), `state-level-undisclosed-access` (new — the
original six Theme-2 cases are federal-only; this is the first with a documented state-level
parallel mechanism in the same case).

### Other candidates surfaced but not written up in full (lower priority / needs more sourcing
before inclusion)

- **Asheville, NC** — mayor called for ending the city's Flock contract and removing cameras
  after backlash; notably, an official is quoted saying a moratorium alone wouldn't work because
  "our contract does not allow for removal of the technology unless we terminate the contract" —
  a genuinely new detail (contract-structure lock-in as its own opposition friction point) worth
  a future pass.
- **Harrisonburg, VA** — residents cited Fourth Amendment concerns and eroded trust in law
  enforcement; council voted to end its Flock agreement.
- **South Kingstown, Narragansett, and Glocester, RI** — three more 2026 unanimous-vote contract
  terminations (July-August), part of what one aggregator (MSN, citing an unnamed count) describes
  as roughly 23 city/town councils cancelling, not renewing, or deactivating Flock contracts since
  the start of 2026 — consistent with, and modestly larger than, the corpus's existing "95+ cities
  per DeFlock" framing from the original 2026-08-16 orientation note. Worth a future pass to
  reconcile the two counts (95+ DeFlock-tracker vs. ~23 aggregator-counted formal council votes —
  likely measuring different things: total deactivations/non-renewals of any kind vs. formal
  recorded council votes specifically) rather than citing both uncritically as if interchangeable.

---

## Recommendation for Britton, not a decision made here

The Menasha/Milwaukee/Mountain View material (#23-25) is materially stronger evidence than what
Phase 3 had in front of it on 2026-08-16 for two of the three points that pass explicitly flagged
as weak:
1. **Theme 3 (function creep/individual misuse)** was demoted to "reported finding, not built
   into the primary Study 2 design" specifically because it rested on only two thin, single-source
   artifacts (`2026-08-16-phase3-theme-review-and-theory-lock.md`). It no longer rests on only
   those two — #23/#24 add three named, adjudicated-or-charged, multi-sourced cases, plus a
   possible 21-case aggregate pattern pending verification.
2. **Theme 2 (institutional secrecy)** gains a second, state-level mechanism variant (Mountain
   View's California statewide search function) beyond the federal-only pattern the original six
   artifacts documented.

**This pass does not re-open or re-run Phase 3** — that was a completed, disclosed, one-time-
exception decision, not something to silently redo because new evidence turned up later the same
project. But the evidentiary basis for one specific call (Theme 3's thin-sourcing rationale for
staying out of the primary design) has materially changed, and that's worth Britton's own
gut-check the next time he looks at this project — flagged here plainly rather than either quietly
upgrading Theme 3 into a hypothesis myself or staying silent about the new evidence.
