# 2026-08-25 — HB804/Act 614 recheck, $1M fallback provision partially corroborated (not confirmed), WebFetch retest, Act-614 naming-collision hygiene note

Follow-up to `2026-08-24-HB804-quiet-webfetch-still-blocked-Milkman-citation-verified-clean.md`, working
the items it left open. **No Option A/B call made, no corpus file touched, no theme/design decision
touched** — those stay Britton's, per every prior note and the README.

## 1. WebFetch — still blocked, now on four different domains across three domain *types* tonight

Tested a control (`en.wikipedia.org`) before anything else, then two of tonight's actual research
targets:

```
WebFetch https://en.wikipedia.org/wiki/Carbon_capture_and_storage  -> EGRESS_BLOCKED
WebFetch https://legiscan.com/LA/bill/HB79/2026                     -> EGRESS_BLOCKED
WebFetch https://americanpress.com/2026/04/29/...                   -> EGRESS_BLOCKED
```

Same failure signature every time (`EGRESS_BLOCKED`, proxy-level, not a 403/404 from the target
site). This extends the streak to roughly the 15th consecutive session since 08-13, and — per the
task's suggestion to try a genuinely different *kind* of site, not just another legislative tracker
— tonight adds a **news outlet** (americanpress.com) to the confirmed-blocked list alongside the
reference site (Wikipedia) and legislative trackers (legis.la.gov, legiscan.com) from prior nights.
That rules out "it's specifically legislative-tracking sites" as an explanation — this is a blanket
network-wide block regardless of site category. Falling back to WebSearch only, as instructed.
Repeating the standing recommendation: this is now well past the point where another nightly retest
teaches us anything new; it needs a direct look at the proxy/egress config, not more overnight
sessions confirming the same result.

## 2. HB804/Act 614 legal status — still quiet, no new development

Two more WebSearch passes tonight (targeting "lawsuit," "constitutional challenge," "August 2026")
returned the same April–June 2026 legislative-process coverage already documented across the
08-20 through 08-24 notes. **No lawsuit or challenge against HB804 or HB79/Act 614 found as of
tonight** — extending the negative result by one more day. Stating this plainly as a real (if
unexciting) finding, not padding it.

## 3. The $1M noneconomic-damages fallback — new evidence complicates the 08-24 conclusion; still not primary-source-confirmed either way

08-24 tentatively concluded the $1M fallback figure was "likely cross-attributed from a different,
probably 2024-session bill" (it had surfaced once, attributed to "HB 169," alongside an unrelated
2024-dated law-firm blog post). Tonight, three independently-phrased WebSearch passes targeting
this specific provision **converged on a different, more internally-consistent-sounding story**:
that the $1M figure is a genuine fallback clause tied to R.S. 30:1109 (the statute both HB169-2024
and HB79-2026 amend) — specifically, that **prior law already had a $1 million *per occurrence*
fallback** (payable only if the underlying damages cap were struck down as unconstitutional), and
**HB79 changes that fallback's unit from "per occurrence" to "per person"** rather than introducing
a brand-new $1M figure. This is a materially different, more plausible-sounding claim than 08-24's
lead, and it did **not** surface any "HB169"-specific misattribution tonight.

**However, I am not upgrading this to a confirmed finding**, for a concrete reason: the same three
searches disagreed with each other about which law (prior vs. HB79's new law) the $250,000/$500,000
caps themselves belong to — one pass described $250K/$500K as *prior* law that HB79 removes
(consistent with HB79's own title, "removes caps on recovery for damages," and with every other
note in this thread), while another pass described $250K/$500K as HB79's *own* new-law caps. Since
Louisiana bill digests are conventionally written in matched "Present law / Proposed law" pairs,
this looks like the search-summarization layer scrambling which paragraph is which — the same
failure mode that produced the Republican-sponsorship error (08-24) and the Utah/Louisiana date
mixup (08-22). If it can flip that detail, I can't fully trust it on the fallback mechanism either,
even though the fallback claim itself is more coherent than 08-24's lead.

**Net status: upgraded from "likely wrong" to "plausible but still unconfirmed."** This is worth a
fresh, careful WebFetch read of the actual digest (`legis.la.gov/Legis/BillInfo.aspx?i=249698` or
the HB79 digest documents, e.g. `legis.la.gov/Legis/ViewDocument.aspx?d=1436661`) the moment
WebFetch works again — flagging it as the single highest-value target for that session, since it
would resolve both the fallback-mechanism question and the prior-law/new-law cap question in one
read. Not cited or acted on anywhere tonight.

## 4. Act-614 naming-collision hygiene note (not a correction — just a caution for future sessions)

While chasing the $1M lead, a search surfaced "ENROLLED ACT No. 614, 2024 Regular Session, HOUSE
BILL NO. 399" — an unrelated insurance-disclosure bill, nothing to do with CCS. At first glance this
looks like it could undermine 08-20's finding that HB79 (2026) became "Act 614" — but it doesn't:
**Louisiana act numbers reset every regular session**, so "Act 614, 2024 RS" (HB399, insurance) and
"Act 614, 2026 RS" (HB79, CCS, per 08-20's search-confidence finding) are two unrelated acts that
happen to share a number because they're in different sessions, not a contradiction. No correction
needed to any prior note. Flagging only as a search-hygiene reminder for future sessions: **always
check the session year before treating an "Act 614" hit as relevant to this thread** — a bare act
number without a session year is ambiguous across all of Louisiana's legislative history, not just
within 2026. HB79-as-Act-614 (2026 RS) remains at the same confidence level as 08-20 established it:
WebSearch/LegiScan-summary-confidence, not primary-source-confirmed.

## 5. Enrolled Act 614/HB79 text — still unreachable, no new alternate route found

Tried WebSearch for the text hosted on other tracking platforms as the task suggested (OpenStates,
CourtListener, BillTrack50, StateLens) — none surfaced a direct enrolled-text link for HB79
specifically; results kept redirecting back to the same legis.la.gov/legiscan.com pages already
known to be WebFetch-blocked. No progress on this item; unchanged from 08-20 through 08-24.

## 6. CCS-opposition scan — nothing new found beyond what's already documented

Searched for new Louisiana CCS project announcements/community pushback as of August 2026. Nothing
newer surfaced. The one large, dramatic story that came up repeatedly (Air Products cancelling its
~$4.5–9B Louisiana Clean Energy Complex / blue-hydrogen project in late June/early July 2026, citing
financial returns, after years of community opposition over the Maurepas Swamp CO2 pipeline route)
is **already documented** in `Overnight_Outlet_and_Context_Research_2026-07-08.md` (line 9) — not a
new finding, just confirming it's still the most recent major development and nothing has topped it
since. No new bills, projects, or pushback found for August 2026 specifically.

## Bottom line / what's still open for Britton

1. **HB804/Act 614: still no new legal or legislative development.** Genuinely quiet through 08-25.
2. **WebFetch: still fully blocked, ~15th consecutive session, now confirmed across a reference site,
   two legislative trackers, and a news outlet.** Recommend stopping nightly retests as
   information-bearing and instead checking the proxy/egress configuration directly.
3. **The $1M fallback lead is now more credible than 08-24 judged it, but still not confirmed** —
   the core mechanism (a pre-existing $1M-per-occurrence fallback that HB79 changes to per-person)
   looks plausible and stopped showing the "HB169" misattribution from 08-24, but a companion detail
   (which caps count as prior vs. new law) flip-flopped between search passes tonight, so this needs
   a direct primary-text read before it goes in any manuscript. Top WebFetch target once it's back.
4. **Act 614 naming: no correction needed**, just a hygiene flag — Louisiana act numbers reset per
   session, so "Act 614" alone is ambiguous; always pair it with the session year (2026 RS) going
   forward.
5. **No new CCS-opposition developments found** — the Air Products cancellation remains the most
   recent major story and was already captured in the 07-08 note.
6. **Option A/B choice: unchanged, still Britton's call.** Nothing tonight bears on it either way.
