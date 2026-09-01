# 2026-09-01 — FAA docket post-deadline close confirmed (comment surge) + Louisiana aerospace liability-shield laws added to corpus

Follow-up to `2026-08-31-faa-docket-deadline-check-and-boca-chica-cwa-verification.md`, which
checked the docket ~22-23 hours before its stated close (`commentEndDate: 2026-09-01T03:59:59Z`,
i.e. 11:59:59 PM Eastern / 10:59:59 PM Central on 2026-08-31) and found it still open. Tonight's
top-priority task, per instructions, was the post-deadline recheck. **No theory chain, coding
scheme, or Study 1 option (A/B/C) decided or touched here — still Britton's call**, per standing
project rules.

## 1. FAA-2026-8614 — CONFIRMED CLOSED, with a large late-breaking comment surge

Checked at approximately 2026-09-01T05:15 UTC — about 1 hour 15 minutes after the docket's own
stated close time (2026-09-01T03:59:59Z). Two independent methods used, both direct-fetch, not
AI-summarized (see method note below on why this matters):

**Method A — regulations.gov's own docket HTML page**, fetched via the `r.jina.ai` reader proxy
(`curl -s https://r.jina.ai/https://www.regulations.gov/docket/FAA-2026-8614`; direct WebFetch to
regulations.gov itself still 403s, consistent with every prior session). Fetched a clean,
verbatim page — not an AI summary — showing:

- **Status banner: "Closed for Comments"** (this is the literal text label the page displays;
  this is the confirmation the docket is now closed for comment).
- **"Number of Comments Posted to this Docket: 2,785"**
- **"Number of Comments Received: 14,669"** — the page's own caption clarifies this count is
  "as of 11:59 PM yesterday" (i.e., as of the actual close of the comment window), and that
  "posted" comments (the publicly viewable subset) typically lag behind "received" because
  agencies process/moderate before posting.

**Method B — the regulations.gov public REST API** (`api.regulations.gov/v4`, `DEMO_KEY`),
fetched the same way as the 08-30/08-31 notes' documented technique (curl through the
`r.jina.ai` proxy — note: **direct `curl` to the API, and direct WebFetch to the API, both hit
`429 OVER_RATE_LIMIT` tonight** with the shared `DEMO_KEY` — `Retry-After: 39176` seconds
[~10.9 hours], confirming the demo key's shared global rate limit is currently exhausted,
presumably from this same project's own repeated nightly use of it. The `r.jina.ai`-proxied path
still worked cleanly, so this remains the reliable technique — flagging that direct API access
without the proxy is not currently usable and may need to wait out the `Retry-After` window in a
future session, or use the proxy as done here). The API's `/v4/documents` endpoint for the
document record itself now shows:

```
"commentEndDate" : "2026-09-01T03:59:59Z"
"openForComment" : false
"withinCommentPeriod" : false
"allowLateComments" : false
```

This directly confirms `openForComment` flipped from `true` (08-31 check) to `false` (tonight) —
exactly the transition the task was watching for.

**The surge, quantified:**

| Metric | 2026-08-30 check | 2026-08-31 check (~22h before close) | 2026-09-01 check (~1h after close) |
|---|---|---|---|
| Total comments (posted/indexed) | 1,453 | 1,453 (unchanged) | **2,785** |
| Comments mentioning "Vermilion" | 141 | 141 (unchanged) | **345** |
| Total comments *received* (incl. unposted backlog) | not tracked previously | not tracked previously | **14,669** |

Posted comments nearly **doubled** (1,453 → 2,785) between the 08-31 early-morning check and
tonight — the API's own posted-date aggregation confirms **1,332 of the 2,785 total posted
comments were posted in the last 3 days** (08-30 through 09-01), and 1,971 in the last 7 days —
i.e., the overwhelming majority of everything ever posted to this docket landed in the final
72 hours before the deadline. "Vermilion"-mentioning comments (a proxy for Louisiana-site-specific
engagement vs. the docket's broader national NPRM scope) also more than doubled (141 → 345).

**The 14,669-received figure is the more striking number and needs a clear caveat stated
plainly**: it is more than 5x the 2,785 currently posted, meaning the large majority of what was
actually submitted has not yet cleared regulations.gov's posting/moderation queue and is not yet
individually readable. This is consistent with the posting-lag behavior flagged in the 08-30 and
08-31 notes, just at a much larger scale given the deadline-day volume. **Do not report "14,669
comments" as "14,669 readable/analyzable comments" in any manuscript language** — it is FAA's own
reported received-count, not a count of comments a Study 1 corpus could currently code. The 2,785
posted figure is the ceiling of what's currently readable via the API/docket comments tab.

**Targeted searches rerun post-close, all still empty** (same technique as 08-30/08-31): no
comment found matching `StopSpaceX` (0), `Hensgens` (0), or `"police jury"` (0) — no organized
filing from the local opposition group or a named Vermilion Parish official has surfaced under
those search terms even after the deadline surge. This doesn't rule out organic individual-name
comments from local officials/StopSpaceX members that a name search can't practically enumerate,
same caveat as before.

**What this doesn't do**: it doesn't identify *who* filed in the surge (a full read of the
2,785 posted comments, let alone a wait for the remaining ~11,900 to post, is out of scope for
tonight) — that's flagged below as the open item for whenever this paper's Study 1 corpus work
resumes.

## 2. New corpus material: Louisiana's aerospace liability-shield legislative package

While the docket surge itself hasn't yet been covered by news (checked tonight — the deadline had
only just passed and this is a fast-moving story), a WebSearch pass surfaced a substantive new
primary-source thread not previously in this project's notes: **Louisiana passed a package of
aerospace-industry-specific state laws in its 2026 regular session (signed by Gov. Landry,
finalized by late June 2026) that directly bear on the paper's regulatory-venue-shifting /
procedural-justice frame candidate** — and directly corroborates a detail the 08-30 note flagged
as "not yet independently checked" (the Wesolick FAA comment's claim about a Louisiana law
"exempting some aerospace projects from public review").

**Primary source #1 — the actual enrolled bill text**, fetched directly (`curl` + `r.jina.ai`
proxy after direct WebFetch to `legis.la.gov` 403'd): **Act 874 (2026 Regular Session), House
Bill 1098, by Reps. McFarland and Chassion** (`legis.la.gov/legis/ViewDocument.aspx?d=1481505`).
Enacts La. R.S. 9:2800.31. Verbatim key provision (Section B): "no aerospace flight entity that
owns and occupies a minimum of twenty thousand contiguous acres in this state shall be liable for
any cause of action arising from nuisance, trespass, inverse condemnation, strict liability, or
any other claim based upon noise, sonic booms, overflight, vibration, light, heat, exhaust,
smoke, odor, visual intrusion, temporary access restrictions, or any other disturbance resulting
from aerospace flight activities." Exceptions (Section D): gross negligence/willful misconduct,
intentional injury, violation of an FAA license/permit/authorization condition, or falling-debris
injury exceeding normal risk. Section F creates a presumption of lawful conduct where the entity
is in "substantial compliance" with applicable licenses/permits — which matters directly for this
paper's framing, since the pending federal waiver (FAA-2026-8614) would reduce exactly which
license conditions exist to be "in compliance" with or "in violation" of.

**Primary source #2 — companion bill**: Act 343 / House Bill 1250 (per news coverage below;
enrolled bill text itself not independently fetched tonight, flag as B-tier pending direct
verification) — creates a "special motion to strike" mechanism letting aerospace companies get
nuisance suits dismissed early with fee-shifting onto the losing plaintiff, and blocks injunctions
against aerospace activity.

**Primary source #3 — a separate public-records exemption**, per news coverage (not yet
independently fetched as enrolled text — B-tier): another McFarland-authored bill
(`legis.la.gov/legis/BillInfo.aspx?i=251285`) exempts aerospace company records — described as
"ranging from facility blueprints to flight logs" — from the Louisiana Public Records Law. This
is a second, distinct transparency-curtailing mechanism alongside the NDA pattern the 08-29 note
already found (elected officials required to sign NDAs to receive project information) — worth
keeping as a separate code if a future opposition/transparency theme is coded, since one is a
contractual/administrative practice (NDAs) and the other is now statutory.

**News coverage, both fetched directly (tier A):**
- **The Current (Lafayette), "What does SpaceX's legal shield mean for Vermilion Parish
  residents?"** (published 2026-08-31T17:19:57Z — same day as the FAA deadline, genuinely
  new/current), fetched via `r.jina.ai` proxy after direct WebFetch 403'd. Names both acts, quotes
  Lafayette environmental attorney Bill Goodell calling them likely unconstitutional ("I think
  [Acts] 343 and 874 are both unconstitutional") and describing a "double shield" (the Industrial
  Development Board of the Parish of Vermilion holds the spaceport land under a long-term lease,
  adding a second layer of insulation). Quotes State Rep. Tehmi Chassion (D-Lafayette, Act 874
  co-author) defending the bill's carve-outs; Goodell rebuts that the gross-negligence standard is
  "a very high bar to hurdle" requiring "smoking-gun evidence." Explicitly connects the state
  shield to the federal FAA waiver fight this paper is already tracking: the state law's liability
  shield has an exception for FAA-license violations, but the pending federal waiver would reduce
  what those license conditions even require — Goodell: "With the pending FAA waiver, that
  instrument [NEPA disclosure] is now at risk." Notes Landry's public claim the bills are modeled
  on Texas/Florida statutes, but reports Texas's own liability statute is narrower (nuisance
  claims only) than Louisiana's (which also bars inverse condemnation and strict-liability
  claims).
- **Louisiana Illuminator, "Louisiana launches immunity law to lure aerospace companies"**
  (published 2026-05-29T18:55:04Z, contemporaneous with the bill's Senate passage), fetched
  directly via the same proxy technique. Reports HB 1098 passed the Senate 33-3. Names the direct
  real-world trigger this bill responds to: **a group of Texas residents who filed suit against
  SpaceX in 2026 (Texas Tribune, 2026-05-01, cited in-article) over rocket noise/shock waves that
  allegedly cracked home structures near Boca Chica** — the article states plainly that under
  McFarland's Louisiana bill, "if something similar were to happen in Louisiana, the company would
  not have to pay for the damages." This is a directly citable instance of the Boca-Chica-
  precedent-awareness mechanism already central to this paper's candidate theory frames: Louisiana
  legislators are shown, in their own on-the-record floor debate, explicitly legislating in
  anticipation of a Texas-style harm recurring in Louisiana, and choosing to immunize it in
  advance rather than mitigate it. Quotes Sen. Jay Luneau (D-Alexandria) opposing an earlier,
  broader draft ("If a rocket falls on your house and kills your family, you should be able to
  recover for that") and Sen. Patrick Connick (R-Marrero), who led narrowing the bill's scope,
  on the record after the vote: "No other state gives immunity away like we just did." Also
  confirms the public-records exemption (source #3 above) and a separate April 2026 tax-break
  package (property/sales tax exemptions for the aerospace industry) as part of the same broader
  legislative push — not independently fetched tonight, flagged for a future pass if useful.

**Why this matters for the paper, without picking a theory chain**: this material gives
concrete, dated, quotable, primary-sourced content for whichever frame Britton eventually locks —
it's simultaneously (a) direct evidence for regulatory-venue-shifting (a federal review waiver
paired with a state liability shield that widens exactly where the federal waiver narrows), (b)
direct evidence for Boca-Chica-precedent-awareness (legislators citing an active Texas lawsuit as
their explicit reason for acting), and (c) a second, statutory transparency-curtailment mechanism
alongside the already-documented NDA pattern. It's flagged here as corpus material only — no
theory-chain or Study 1 option decision is made or implied.

## 3. Discrepancy and PDF-extraction items from the task briefing — status check, no new work needed

The task briefing described two open items as of 2026-08-27/08-28: the $25M/$100M figure
discrepancy, and the FAA comment letter PDF needing extraction. Checking the notes folder tonight
confirms **both were already resolved by intervening sessions**, before tonight's run:
- The $25M (Community Foundation of Acadiana donation, written/LED-confirmed) vs. $100M (coastal
  master plan, verbal/Gov. Landry press-conference-sourced) discrepancy was resolved
  2026-08-29 — see `2026-08-29-primary-source-pass-and-discrepancy-resolution.md`, section 2.
  Both figures are real and distinct; the sourcing-tier difference (written vs. verbal) is itself
  flagged there as a data point worth coding. Nothing new to add tonight — no new sourcing for the
  $100M figure was found or attempted, since the 08-29 note already reached moderate-high
  confidence and this session's priority was the FAA docket close.
- The FAA comment letter PDF (LWF/NWF/Pontchartrain Conservancy joint letter) was fully extracted
  and read 2026-08-29 (`pdftotext` + independent proxy cross-check) — see that note for the full
  extracted content and the corpus table's row 4.
Both are noted here only so this session's own record is self-contained; no rework was done on
either.

## 4. What's still open

- **The identity/composition of the 2,785 posted (and eventual up-to-14,669 total) comments in
  the deadline surge is not yet characterized.** Tonight only quantified the surge and reran the
  same three targeted name/org searches from prior nights (all still empty). A genuinely useful
  next step, once Study 1 corpus scope is set, would be pulling a random or systematic sample of
  the newly-posted comments (especially the 345 "Vermilion"-mentioning ones) to see whether the
  surge is organic, template/form-letter-driven (as the 08-30 note found some evidence of), or
  both, and in what proportion.
- **A later re-check of the same docket** (a day or more from now) would show the gap between the
  2,785 currently-posted and 14,669 received close as the moderation backlog clears — worth noting
  as the true "final" posted count if the paper ever needs to cite one, since 2,785 is very much
  a still-rising snapshot immediately after close, not likely the eventual settled figure.
- **Act 343 / HB 1250's enrolled text** and **the public-records-exemption bill's enrolled text**
  (source #3 above) were not independently fetched tonight — only reported via news coverage
  (tier B for those two specifically; Act 874/HB 1098 is tier A, fetched directly).
- **The `DEMO_KEY` regulations.gov API rate limit is currently exhausted** (`Retry-After: 39176`
  seconds from tonight's check, ~10.9 hours) for *direct* (non-proxied) access — the `r.jina.ai`
  proxy route still works and was used throughout, so this didn't block tonight's work, but a
  future session attempting the historically-preferred direct-curl technique from the 08-30 note
  should expect it to fail until the window clears, and should default to the proxy path instead.
- No theory chain, coding scheme, or Study 1 option (A/B/C) decided — unchanged, still Britton's
  call.
