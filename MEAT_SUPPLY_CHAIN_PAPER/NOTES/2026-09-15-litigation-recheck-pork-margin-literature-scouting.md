# 2026-09-15 — Litigation recheck, pork-margin follow-up closed, consumer-marketing literature scouting

Seventh research session. Scope tonight: (1) recheck the two litigation threads flagged for
tonight's pass (Agri Stats DOJ case, Tyson $82.5M DPP settlement); (2) confirm the status of the
Schaefer/poultry-concentration and idea-28 threads named in `PROJECT_STATUS.md`; (3) continue
primary-source follow-ups still open in `NOTES/Claim_Fact_Check.md`; (4) literature-gap scouting
for the price-fairness/COO-disclosure marketing angle. Method: CourtListener docket pages fetched
directly via `curl` with a browser User-Agent (same technique as prior sessions), `pdftotext` on
a freshly-downloaded court PDF, `WebSearch`/`WebFetch` for everything else. No design decisions
touched, no external contact made.

## 1. Agri Stats DOJ case — correcting this session's own starting brief, not a new finding

Tonight's task brief described this thread as "as of 09-13, still not granted/no outcome found."
That is **not what this project's own 2026-09-13 note and `PROJECT_STATUS.md` actually say** —
they already record the DOJ case as **resolved**: Judge Tunheim signed the Final Judgment
September 10, 2026 (Doc. 763), read in full that session. I'm flagging this discrepancy plainly
rather than silently redoing already-finished work or silently ignoring the brief: whatever
generated tonight's framing (likely a summary written before the 09-13 pass completed) is stale;
this project's own primary-source record is the more current and more authoritative one.

What I did tonight was a **light forward-check** for anything post-September-10 that the 09-13
note couldn't have known about yet, since 09-13 to 09-15 is new ground:

- **Secondary corroboration found, not previously in this project**: Law360, "DOJ Gets Final OK
  For Agri Stats Antitrust Settlement," independently confirms final approval was granted (dates
  it September 11, 2026 — one day after the signed date of September 10 found in the primary PDF;
  most likely the difference between the judge signing the order and the clerk entering/dating it
  on the docket, not a contradiction). PYMNTS coverage of the same event is consistent.
- **Checked and could not confirm a specific "$350,000 payment to states" figure that surfaced in
  two secondary/AI-summarized sources** (an aggregated WebSearch answer and a legal-blog article,
  legalclarity.org) describing the settlement as including monetary compensation to the plaintiff
  states. I re-downloaded the actual signed Final Judgment PDF (Doc. 763, 993KB, the same document
  read in full on 09-13) and ran `pdftotext` + `grep` across all 2,597 lines of extracted text for
  any dollar figure. **The only dollar amounts anywhere in the Final Judgment are the $1,500/month
  and $18,000/year price-cap figures for Agri Stats' non-discriminatory report pricing** (already
  known from the 09-13 read) — no $350,000 figure, no payment-to-states clause, anywhere in the
  document. One of the two secondary sources (WilmerHale's own client alert) independently confirms
  "there is no monetary payment, fine, or dollar amount" in this settlement. **Recommend treating
  "$350,000 to states" as unverified and not using it** — it does not appear in the primary
  document and at least one professional secondary source (a law firm alert) explicitly contradicts
  it. This is exactly the kind of secondary-source drift the project's fact-checking process exists
  to catch.
- No further development (compliance-monitor appointment announcement, appeal, etc.) was found
  beyond the Final Judgment itself. **This thread remains closed** as of 09-13, now re-confirmed
  09-15.

**Separately, and outside tonight's requested scope**: `SOURCE_VERIFICATION/Evidence_Table.md`
(row added 2026-09-07) separately tracks a *different* Sept. 1, 2026 hearing — for the *private*
End-User Consumer class's own Agri Stats settlement (the one behind the $203.35M figure), not
DOJ's case. That row is still marked "not independently re-verified against the docket" and I did
not chase it further tonight (out of scope for what was asked; flagging so it isn't confused with
the DOJ thread, which is fully resolved).

## 2. Tyson $82.5M DPP settlement — real, material pre-hearing development found: hearing pushed back to November 12, 2026

This is the actual new finding of the night. Method: fetched the MDL master docket
(`courtlistener.com/docket/63363039/`, case 0:22-md-03031) directly, paging to the most recent
entries. Two new docket entries appeared **both dated September 14, 2026** — entry 1662 ("Order on
Stipulation," 11:54 AM) and entry 1663 ("Order on Motion for Miscellaneous Relief," 12:18 PM) — but
neither has a free-to-read docket-text line or RECAP PDF yet (only "Buy on PACER" links, which this
project doesn't have credentials for), so their content could not be read directly.

However, a targeted WebSearch found the actual **amended official class notice**, issued by
Co-Lead Class Counsel (Gustafson Gluek PLLC, Cotchett Pitre & McCarthy, Hartley LLP, Hausfeld LLP)
via PRNewswire, **published September 14, 2026, 10:00 AM ET** — the same day as, and roughly an
hour before, the two new docket entries. Fetched and read directly
(prnewswire.com/news-releases/gustafson-gluek-pllc-cotchett-pitre--mccarthy-llp-hartley-llp-and-
hausfeld-llp-announce-a-class-action-settlement-...-302876711.html). It confirms:

- This is the **same** $82.5M Tyson DPP settlement this project has been tracking (defendant:
  "Tyson Foods, Inc. and Tyson Fresh Meats, Inc."; settlement amount "$80,000,000" plus "$2,500,000"
  for notice/administration costs = $82.5M total; class period January 1, 2015 - February 29, 2020;
  class definition: purchasers of boxed or case-ready beef directly from Cargill, JBS, National
  Beef, or Tyson).
- It is explicitly labeled an **"AMENDED SHORT-FORM NOTICE"** that:
  - **Extends the objection/opt-out deadline from September 14, 2026 to October 23, 2026.**
  - **Moves the Final Approval ("Fairness") Hearing from October 1, 2026 to November 12, 2026.**
- The stated reason: the amendment "includes Co-Lead Counsel's request for incurred litigation
  costs and future litigation costs" — i.e., an added/updated fee-and-costs request required
  re-noticing the class before the court could rule, pushing the whole schedule back roughly six
  weeks.

**This directly and materially updates `PROJECT_STATUS.md`'s existing October 1, 2026 hearing
date, which is now wrong** — not because anything was miscounted previously (the October 1 date
was correctly read from the actual August 18, 2026 schedule order at the time), but because the
schedule itself changed on September 14, 2026, one day before this session ran. The September 14
timing of both the new docket entries and the amended-notice press release (same day, entries an
hour or so after the press release's 10:00 AM timestamp) is consistent with the court having
signed a schedule-modification order that morning, which class counsel then used to issue the
amended notice — I'm inferring that connection from the timing match, not confirming it from the
docket text itself, since that text isn't freely readable. Flagging that inference explicitly as
an inference, not a confirmed fact.

**Bottom line**: as of tonight, the Tyson $82.5M DPP settlement has **not yet received final
approval**, same as before, but the hearing is no longer October 1, 2026 — it is now **November
12, 2026**, with the objection/opt-out window extended to **October 23, 2026**. This is worth
correcting everywhere the October 1 date appears in this project's files. Recommend checking back
after November 12, 2026 rather than October 1.

## 3. Schaefer/poultry-concentration thread — confirmed already resolved, no new work needed

Read `PROJECT_STATUS.md`'s Open Decision #6 in full before doing anything else here, per the task
brief's instruction. It is already marked **RESOLVED 2026-09-08**: Britton retrieved Schaefer et
al. (2024, *Review of Industrial Organization*) directly via institutional access, and it was read
in full — the paper's own broiler CR4 for FY2021 is 52%, consistent with USDA PSD's 53-55% figure,
not the erroneous 78% figure. The CR4-vs-CR10 mix-up hypothesis (77% CR10 ≈ the erroneous "78%")
is the leading explanation. There is nothing left to advance on the core discrepancy — I did not
find anything tonight that changes this. The one small residual item under this general area
(the "Meat Institute rebuttal page," a different, minor open source) is covered in Section 5 below.

## 4. Idea 28 (beef price-fixing saga) — no material new developments since the last check

Checked for anything new since the 2026-09-08 DOJ-retailer-probe confirmation:

- **No criminal indictments have been filed** as of tonight (multiple independent outlets confirm
  the investigation remains in the document-review phase; AG Todd Blanche's office has described
  reviewing "more than 3 million documents" as of a May 2026 press conference, no update found on
  that count). This is consistent with, not a change from, what the project already has on record.
- No further DOJ.gov or DOJ-social-media statement was found beyond the already-confirmed September
  2, 2026 eight-retailer-probe post.
- The MDL docket paging done for Section 2 above (which covers the same case family as idea 28)
  didn't surface anything new relevant to idea 28 specifically beyond the DPP-hearing
  rescheduling itself.

**No update needed to idea 28's status.** Its home record is
`Claude_Knowledge/Research_Stream_Ideas.md` (idea 28, outside this project's folder) — per this
project's scope restriction (work only inside `MEAT_SUPPLY_CHAIN_PAPER/`), I did not edit that
file tonight even though it would ordinarily get an addendum for a scheduling change like this;
whoever next has write access to `Claude_Knowledge/` should port over the November 12, 2026 hearing
date if idea 28 gets touched again. The adoption decision for idea 28 remains entirely Britton's,
unchanged.

## 5. Claim_Fact_Check.md follow-ups

- **Pork-specific COVID-margin finding for Claim #13: RESOLVED.** The follow-up flagged in
  `Claim_Fact_Check.md` ("Extract pork-specific figures from Balagtas & Cooper (2021) to confirm
  or disconfirm a pork-specific COVID-margin finding") is now answered. Re-fetched the article
  directly (choicesmagazine.org, the same URL already in `LITERATURE/Price_Transmission_
  Literature.md`) and confirmed **Figure 3 in the article is explicitly titled "COVID-19 is
  Associated with a Spike in the Wholesale-Farm Price Margins for Beef and Pork"** — i.e., the
  article's own margin-widening finding is not beef-only, it explicitly covers pork too. Separately,
  the article's farm-price data shows hog (barrow/gilt) prices fell *more* than cattle prices during
  the same window (USDA's projected barrow/gilt price fell 20.9% January-May 2020, vs. 11.4% for
  steers), and pork-packing-plant capacity utilization bottomed out lower than the article's beef
  figures on April 29, 2020 (54%, vs. recovering to ~95% by mid-June) — both consistent with a
  pork-specific supply shock at least as severe as beef's. This resolves Claim #13's residual gap:
  the COVID-era margin-widening finding is now supported for pork specifically by the same primary
  source already anchoring the beef finding, not just inferred from the farm-share data. See the
  updated Claim #13 row in `Claim_Fact_Check.md`.
- **Meat Institute rebuttal page: still blocked, third attempt.** Retried
  `drovers.com/news/industry/meat-institute-disputes-white-house-analysis-packer-concentration`
  via both direct `curl` (browser UA) and `WebFetch` tonight — both returned HTTP 403 ("Access to
  this page has been denied"), same as the two prior sessions that tried it. This is a minor,
  low-value source (one piece of industry-counter-narrative discourse, not a load-bearing
  empirical claim) — **recommend deprioritizing further automated retries on this specific URL**;
  it appears to be a persistent bot-block on drovers.com itself, not an intermittent issue. If this
  discourse is needed later, it's more efficient to search for other outlets that covered the same
  Meat Institute statement than to keep retrying this one URL.

## 6. Literature-gap scouting: price-fairness / transparency / COO-disclosure marketing research

Per the README's item 4 for this project (do this "if real time remains" — it did tonight).
Searched specifically for recent (2024-2026) marketing/consumer-research literature adjacent to
the project's current best-marketing-contribution framing (transparency of value distribution →
price fairness/attribution → trust/purchase intention, moderated by COO/ethnocentrism). Three
genuinely relevant, verified finds, written up in full in the new file
`LITERATURE/Consumer_Marketing_Literature_Scan_2026-09-15.md`:

1. **Sun, K.-A., & Moon, J. (2025). "Exploring the antecedents and consequences of perceived
   fairness in beef pricing: The moderating role of freshness under conditions of information
   overload." *Foods*, 14(11), 1844.** U.S. beef consumers (n=415), price fairness as an outcome
   of organic perception, freshness as a moderator.
2. **Sun, K.-A., & Moon, J. (2025). "Structural relationship between beef food quality, trust, and
   revisit intention: The moderating role of price fairness based on heuristics effect." *Nutrients*,
   17(13), 2155.** Same U.S. beef consumer sample; price fairness as a *moderator* (not mediator)
   between quality attributes and trust/revisit intention, using covariance-based SEM + Hayes'
   PROCESS, not PLS-SEM.
3. **Casteran, G. (2024). "The central role of price fairness for cost transparency strategy: What
   is the effect of conventional versus Fairtrade products and construal level?" *Recherche et
   Applications en Marketing* (English ed.).** Two online experiments; cost transparency → price
   fairness, conventional vs. Fairtrade products, construal level as moderator — a real marketing
   journal (not food-science), structurally close to this project's own transparency→fairness
   chain, but general retail, not meat/food-specific and not COO-specific.

**Gap read (the actual point of this scouting, not just a citation dump)**: both Sun & Moon studies
show beef + price fairness is already being published, but in food-science/nutrition journals
(*Foods*, *Nutrients* — both MDPI), using organic/freshness/store-revisit framing, not this
project's marketing-theory framing (attribution of responsibility for the price, corporate
explanation type, channel-power/value-distribution transparency, COO disclosure specifically).
Casteran (2024) shows the transparency→price-fairness chain itself is publishable in a real
marketing journal, but for general retail/Fairtrade, not meat or COO. **Net read: the project's
specific angle — COO disclosure × corporate price-explanation type as antecedents of price-fairness
attribution in a meat/COO context, published in a marketing (not food-science) journal — still
appears to be a genuine, unoccupied gap**, not something a competing paper has already claimed.
This is a modestly reassuring finding for Britton, not a strong one — it's based on a targeted
search tonight, not a systematic review, and MDPI food-science journals move fast, so this should
be re-checked periodically rather than treated as a permanent clearance.

## For Britton

Two real, dated updates tonight, both litigation-tracking, both good-news-neutral (neither changes
the paper's substance, both are just docket housekeeping):

1. **The Agri Stats DOJ case was already resolved as of the last session (Final Judgment, September
   10, 2026) — tonight's task brief describing it as still-open was itself out of date, not a
   finding. Nothing further to decide here.** I did catch and rule out a "$350,000 payment to
   states" figure floating around some secondary sources — it's not in the actual signed judgment,
   don't use it.
2. **The Tyson $82.5M settlement's final-approval hearing moved from October 1 to November 12,
   2026** (objection/opt-out deadline moved from September 14 to October 23, 2026), because
   class counsel added a fee/costs request that required re-noticing the class. Still not decided.
   If this project's manuscript or any other document already has "October 1, 2026" written down
   anywhere as this hearing's date, it needs to change to November 12.

Also resolved a small evidence gap (pork shares in the COVID-era packer-margin-widening finding,
not just beef — same source that already anchors the beef version of that claim), and did a
literature-gap check that came back cautiously reassuring: nobody appears to have already published
this project's specific COO-disclosure/price-fairness-attribution angle in a marketing journal,
though two adjacent beef/price-fairness studies exist in food-science journals worth knowing about
and possibly citing as related work. The Schaefer/poultry-concentration thread needed no new work
tonight — it was already fully closed. The idea-28/DOJ-criminal-probe thread also needed no new
work — still no indictments, nothing changed. The Meat Institute rebuttal page is still blocked
after a third attempt; recommend not spending further automated-retry time on that specific URL.

No design decisions were made or needed. No money spent. No one contacted.
