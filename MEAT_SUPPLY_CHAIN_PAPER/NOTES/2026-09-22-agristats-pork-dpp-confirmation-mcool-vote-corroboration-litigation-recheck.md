# 2026-09-22 — Pork DPP Agri Stats settlement confirmed, MCOOL vote count further corroborated, litigation recheck

Tenth research session. Scope: the four items flagged as open in the 2026-09-19 pass, worked in the
order given. Method: `WebSearch` plus `WebFetch` against news outlets, a specialist antitrust newswire,
a policy-nonprofit markup tracker, and an official settlement-class notice site. No `curl`/`pdftotext`
needed tonight — no new primary court document was pulled (the existing 2026-09-19 primary read of
Doc. 3472 already covers the court order itself); tonight's work corroborates and sharpens dates/terms
around it. No design decisions touched, no external contact made, nothing submitted anywhere.

## 1. Pork Direct Purchaser Plaintiffs' Agri Stats settlement — CONFIRMED final, with one useful date refinement

The 2026-09-19 pass read the court's written order (Doc. 3472, D. Minn., 18-1776, filed 9/10/26) granting
final approval, but that order's own text did not state a fixed hearing date and the settlement's actual
dollar terms weren't independently pulled. Tonight, two additional sources close both gaps:

- **MLex** (specialist antitrust newswire, same outlet this project already treats as an acceptable
  same-day source per the End-User Consumer Agri Stats precedent): article "Agri Stats settlement ends
  direct purchasers' US pork price-fixing claims," byline/timestamp confirmed directly as
  "September 8, 2026, 18:27 GMT." Quote: "Agri Stats' settlement with direct purchasers got final
  approval from a US judge Tuesday..."
- **porkantitrustlitigation.com** (the official settlement-administrator site for this specific track,
  found via search, not previously checked): states the Fairness Hearing was held **September 8, 2026,
  at 11:00 a.m. Central Time, Courtroom 14E, U.S. District Court for the District of Minnesota** — and,
  critically, gives the settlement's actual terms in its own words: **"There is no money available from
  the Agri Stats Settlement... Agri Stats will make significant and substantial conduct reforms"**
  (removing participant lists, stopping sales reports, removing suspect fields if it ever resumes pork
  reports). This directly confirms, from the settlement's own official notice rather than by inference
  from the pattern elsewhere, the "behavioral/injunctive only, no cash" characterization this project has
  applied to Agri Stats across all four tracks — closing the specific residual gap the 2026-09-19 note
  flagged ("Doc. 3381 ... not pulled tonight ... doesn't independently confirm that pattern").
- **Reconciling the two dates**: verified via `date -d` that September 8, 2026 is a Tuesday and
  September 10, 2026 is a Thursday. Reading both sources together, the most coherent picture is: the
  Fairness Hearing was held and approval granted from the bench on **Tuesday, September 8, 2026**; the
  formal written order was entered on the docket two days later, **Thursday, September 10, 2026** (the
  date this project's 2026-09-19 note recorded from the order's own filing stamp). This is an ordinary
  hearing-then-written-order lag, not a contradiction between sources — but it's worth recording both
  dates precisely (hearing 9/8, order entry 9/10) rather than treating them as the same event.

**Net effect**: this settlement track is now fully confirmed — final approval granted, no cash to the
class, conduct-reform terms specified in the settlement's own official notice — closing out the one
open item flagged as needing a check this session. No appeal or other post-approval development found.

## 2. Tyson $82.5M DPP settlement — no change, reconfirmed via a different outlet

IndexBox and beefdirectpurchasersettlement.com content surfaced via search (the settlement-administrator
site itself remained JS-rendered/unfetchable directly, same as 2026-09-19) both state the Fairness
Hearing remains scheduled for **November 12, 2026, Courtroom 15, District of Minnesota**, claims deadline
November 30, 2026. No new reschedule found — still the November 12 date set by the September 14, 2026
amended class notice. Nothing further to report; not yet decided.

## 3. MCOOL 17-6 vs. 16-7 vote count — one more independent source found, strengthening 17-6; official committee record still a hard wall

Per the brief's instruction to try one more different route: agriculture.senate.gov and congress.gov were
not re-attempted (already tried and blocked twice, 09-17 and 09-19 — no reason to expect a different
result a third time on the same URLs). Instead tried: (a) a direct Thune Senate press-release search —
found several general American Beef Labeling Act releases but none with the specific markup vote tally;
(b) C-SPAN's own video page for this markup — the page itself is now paywalled behind a "tollbit" gate
(HTTP 402), not accessible; (c) the **National Sustainable Agriculture Coalition's** own markup recap
blog post, a policy-nonprofit source that tracks committee markups directly (not news-wire syndication) —
this states explicitly, in its own voice: **"Approved by roll call vote, 17-6."**

This is a fourth independent source type now giving 17-6 (Capital Press, DTN's original Aug. 6 article,
Ag Bull Trading's detailed recap, and now NSAC), against the single outlier 16-7 figure (one later,
undetailed DTN piece) already identified 2026-09-19. **Assessment unchanged in direction, further
sharpened in confidence: 17-6 is very likely correct.** The committee's own official roll-call record
remains a genuine hard wall — not re-attempted tonight since the same two URLs were already tried twice
with no success; per the brief's own guidance, not spending further automated-retry time on this specific
record. Recommend the project treat 17-6 as settled-by-preponderance-of-independent-sourcing without
further overnight passes on this specific question unless Britton has non-automated access to
congress.gov or the committee's own site.

## 4. Farm-bill floor movement — confirmed still pending, one new fact worth flagging

No Senate floor vote has occurred as of this check. New detail not previously in this project's notes:
multiple outlets (Fox34, AgWired, Farm Policy News) note the **current farm bill extension expires
September 30, 2026**, adding real time pressure to when a floor vote might happen. The Sept. 16, 2026
committee-passage vote (12-11, party-line) and the "floor vote expected after the November 2026
midterms" framing both stand unchanged. No update needed to Claim #11's verdict.

## 5. General litigation/DOJ-probe recheck — nothing new

Searched fresh (not just re-reading prior notes) for: (a) DOJ's eight-retailer beef-price probe — no
indictments or new developments beyond what's already tracked (idea 28 remains open/ongoing, as of
09-19); (b) Smithfield ($75M) and JBS ($20M) pork settlements — both confirmed already closed/claims-
period-ended, consistent with existing notes, no new activity; (c) the $117.065M Consumer Indirect
Purchaser pork settlement's Final Approval Hearing — an additional outlet (classaction.org) now
independently corroborates the ~Dec. 11, 2026 date the 2026-09-19 note flagged as "secondary-sourced,
plausible, not primary-confirmed to the day" — still not a primary-document confirmation, but now
corroborated by more than one secondary source.

## What did NOT change tonight

- No design decisions made or needed.
- Claim_Fact_Check.md verdicts: not touched (no new evidence bearing on any claim's substantive verdict,
  only litigation-tracking and vote-count precision, which sit outside the claim ledger).
- `NOTES/Claim_Fact_Check_PriceTransmission_Draft.md` reviewed per this session's instructions; all of
  its claims are already resolved or explicitly flagged as open follow-ups in prior passes (e.g., the
  Balagtas & Cooper pork-specific figure gap was closed 2026-09-15 per `PROJECT_STATUS.md`). Nothing
  further actioned there tonight — judged lower priority than the four litigation/vote-count items the
  brief specifically flagged as open.

## Genuinely still open / hard walls, stated plainly

- MCOOL committee roll-call record: still inaccessible via automated tooling (agriculture.senate.gov,
  congress.gov), tried across three separate sessions now (09-17, 09-19, 09-22 — the latter two routes
  differed). Recommend Britton's own non-automated access if the exact figure needs primary confirmation
  before a manuscript citation.
- The pork DPP Agri Stats Settlement Agreement itself (Doc. 3381, the underlying contract exhibit) still
  was not directly pulled — the "no cash" term is now confirmed via the official settlement-notice site's
  own plain-language FAQ language, which is a good secondary-official source but not the contract exhibit
  itself. Low priority given the notice site's clarity, but noted for completeness.

## For Britton

Nothing that changes any headline verdict. Three confirmations/refinements: (1) the fourth Agri Stats
settlement track (pork DPP) is now fully closed out — no cash, conduct reforms only, hearing held Sept. 8,
order entered Sept. 10, 2026; (2) the MCOOL 17-6 vote count is now corroborated by a fourth independent
source and can reasonably be cited as the correct figure, with the official committee record still
unreachable by this environment's tooling; (3) the farm bill's floor-vote timeline now has one added
pressure point — the current farm bill extension expires Sept. 30, 2026 — worth knowing as background
context, not a scope-affecting development.

No money spent. No one contacted. Nothing submitted anywhere.
