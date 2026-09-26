# 2026-09-26 — Litigation recheck (all four dockets stable), Wayback/Morwitz re-verified, new Bernstein Center grant-page find, new Davidson & Schaefer (2025) lit lead, and a possible critical JCM deadline discrepancy

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session. Scope, per this
task's open items from the 2026-09-25 note: (1) the standing four-docket
litigation recheck; (2) re-verify the Morwitz/Fitzsimons Wayback route is
still accessible; (3) a literature-currency scouting pass, Crossref-verified;
(4) a check for JCM special issue / AMS 2026 news. Item (4) turned up
something that needs Britton's direct attention — see §4 and the new
flagged section added to `SUBMISSION_TRACKER.md`.

## 1. Litigation recheck — all four dockets fully unchanged since 09-25

Same four CourtListener dockets as every prior night, direct-fetched
tonight (2026-09-26) with a browser User-Agent via `curl`. Section 301 and
Axle of Dearborn returned real `HTTP/2 200`s on the first attempt; Section
122 and V.O.S. Selections each hit AWS WAF's `202`/challenge response
(`x-amzn-waf-action: challenge`) on the first try but returned real,
fresh `200`s on a retry a few seconds later (same pattern noted in past
sessions — not a new or worsening block, just the normal CloudFront-WAF
noise).

| Docket | Entries 09-25 | Entries tonight (09-26) | Change |
|---|---|---|---|
| Section 301 forced-labor master docket | 54 | **54** | None |
| Section 122 appeal (*Oregon v. Trump*, CAFC 26-1804/-1805) | 106 | **106** | None |
| V.O.S. Selections (CAFC 26-1895) | 26 | **26** | None |
| Axle of Dearborn (CIT 1:25-cv-00091) | 79 | **79** | None |

Pulled and diffed the actual text of the latest entry on each docket
against the 09-25 note's verbatim quotes — all identical, word for word:

- **Section 301, entry #54** (Sep 23, 2026): same DOJ notice-of-appearance
  housekeeping entry (Eric J. Hamilton), still the last entry.
- **Section 122, entry #106** (Sep 18, 2026, notice of correction to an
  amicus filing) and entry #99 (the Sep 14 order granting the
  government's 30-day extension, response/reply now due 11/12/2026) —
  both verbatim-identical to 09-25.
- **V.O.S. Selections, entry #26** (Sep 15, 2026 text-only order):
  *"...granting motion to extend time to file brief [25] filed by Appellee
  V.O.S. Selections, Inc. The response brief is due 10/05/2026..."* —
  verbatim-identical. **This is now 9 days out** from tonight
  (2026-09-26), down from 10 days as of 09-25.
- **Axle of Dearborn, entry #79** (the Aug 25 reliquidation order, full
  text re-pulled tonight) — verbatim-identical to 09-25.

Checked all four docket pages' full text tonight for a "date terminated"
string (case-insensitive) — none found on any of the four; all remain
open/active. Also searched each page for "oral argument" — the only hits
are old Axle of Dearborn entries already known from months ago (a 2025
motion-hearing item and a rescheduling request); no new oral-argument date
has been set on any of the four dockets, including V.O.S. Selections
(CAFC 26-1895), which the task specifically asked about.

**Bottom line: nothing new on any of the four dockets tonight.** No
rulings, no new substantive filings, no terminations. The two dates still
worth watching are unchanged in kind from prior nights: V.O.S. Selections'
10/05/2026 response brief (9 days out) and Section 122's 11/12/2026
government brief (~7 weeks out).

## 2. Morwitz/Fitzsimons op-ed — Wayback route re-verified, still accessible tonight

Re-fetched the exact Wayback snapshot URL from the 09-25 note
(`web.archive.org/web/20260421185900/https://business.columbia.edu/
faculty/research/opinion-rising-prices-upset-shoppers-do-retailers-dare-
tell-truth-about-whos-blame`). **Still returns a real `HTTP 200`** with
the same genuine `memento-datetime: Tue, 21 Apr 2026 18:59:00 GMT` and
`x-archive-orig-*` headers as 09-25 — not a fluke, still real archived
content. Directly confirmed the abstract text quoted in the 09-25 note
(*"Our studies examine how consumer attribution..."* and the
*"Trump supporters less likely to blame..."* partisan-moderation sentence)
is present verbatim in tonight's fetch, byte-for-byte matching what was
quoted before. The live (non-archived) Columbia URL is **still blocked**
— direct fetch returns Cloudflare's `HTTP 403` bot-challenge page tonight,
same as every prior session. So: Wayback access held up for a second
consecutive night on this specific snapshot — still not something to
assume is permanently reliable, but two-for-two now.

**One new, related, genuinely new-to-this-project find** (see §3 below,
this surfaced from a literature search, not a repeat of the 09-25 Wayback
check): a Columbia Business School **Bernstein Center for Leadership and
Ethics grant-award page** for what appears to be the funded academic
project behind the MarketWatch op-ed. Live URL
(`business.columbia.edu/faculty/awards/how-tariff-price-presentation-
affects-consumer-responses-fairness-perceptions-and`) is blocked the same
way as the op-ed citation page (`HTTP 403`, Cloudflare challenge,
confirmed tonight), but a Wayback snapshot from the same date
(2026-04-21) exists and was fetched successfully (after one retry — first
attempt hit a mid-exchange connection reset, consistent with the "Wayback
not fully reliable" caveat from 09-25; succeeded on retry). Full grant
description, quoted verbatim from the archived page:

> "Granting Agency: Bernstein Center for Leadership and Ethics. Grant
> Given On: 2025. Size of Award (in USD): $10,000. Grant Description:
> This project explores how consumers respond to tariff-related price
> increases and how their reactions depend on how those tariffs are
> presented at the point of purchase. It examines different pricing
> formats including whether tariffs are included in the base price or
> itemized separately, and investigates how political beliefs, fairness
> perceptions, and blame attributions shape consumer attitudes toward
> firms and government. The findings will inform ethical pricing
> strategies and help policymakers and firms better understand how to
> communicate trade-related costs transparently... Awardee: Vicki
> Morwitz, Bruce Greenwald Professor of Business, Marketing Division."

**Why this matters:** this confirms the MarketWatch op-ed is very likely
the public-facing summary of a real, funded (if modest — $10,000)
Columbia Business School research project on exactly this project's core
question (tariff price-presentation format → fairness perceptions →
blame attribution toward firm vs. government, with political-orientation
moderation). It also resolves a small open question from the 09-25 note:
the grant page lists **only Morwitz as awardee** (not Fitzsimons), so
either Fitzsimons was a co-author on the resulting op-ed/paper without
being a named grant PI, or this is a slightly different but clearly
related project — can't fully resolve which from a grant-database page
alone. **No published academic paper (as opposed to the grant description
and the op-ed) was found tonight** — this looks like it may still be a
working paper or in-progress project as of the April 2026 archive date;
worth a periodic check for whether it surfaces as a full paper later, but
not something to cite as more than a funded-project description tonight.

## 3. Literature-currency scouting pass — one strong new lead, prior leads reconfirmed, egg-market paper's fit reaffirmed as tangential

**New-to-this-project, directly on-point, verified via Crossref (not from
a search snippet):** **Davidson, Kelly & Schaefer, K. Aleks (2025),
"Consumer Behavior and the Incidence of Tariffs: Salience, Identity, and
the Politics of Paying More,"** SSRN working paper, DOI
`10.2139/ssrn.5713389`, posted 2025-12-11. Pulled directly from the
Crossref API (full author names, DOI, posting date, and abstract field).
Per the abstract: a randomized dichotomous-choice experiment on
consumers' willingness to pay for tariff-affected food/grocery prices,
where participants were randomly assigned one of several **political
tariff-justifications** (re-shoring, countering unfair trade, reducing
illegal immigration), crossed with exposure/non-exposure to an image of
President Trump. Key finding: **political rationales lowered willingness
to pay on average, driven by Democrats and (to a lesser extent)
Independents, with Republicans largely unaffected** — i.e., political
framing of a tariff justification can backfire rather than help, and the
effect is **partisan-moderated**.

**Why this is a strong fit, more so than the egg-market paper from
09-25:** this is structurally very close to this project's own H1a/H1b/H2a/
H2b chain — a manipulated framing/justification factor → consumer
response (WTP here; this project's fairness/opportunism/trust chain),
explicitly **partisan-moderated**, tested via a between-subjects randomized
experiment — the same design family, not just an analogous mediation
macro. It's a working paper (SSRN, not yet peer-reviewed as of this
posting), so cite it as such, not as a published journal article. Also
worth flagging for cross-project awareness (not pursued further here, out
of this paper's scope): **the second author, K. Aleks Schaefer, appears to
be the same Schaefer already tracked in `MEAT_SUPPLY_CHAIN_PAPER`'s
poultry-concentration thread** per this repo's root README — a
coincidental overlap worth knowing about if Britton ever wants to cite
across both projects, not something resolved or acted on tonight.

**Prior leads reconfirmed, no material changes:** Campbell, Pomerance, &
Percival Carter (2025/2026), "Painful Prices: The Moral Harm Model of
Price Fairness," *JCR* — re-pulled via Crossref tonight; confirms the
print-issue date is now set (**53(3), pp. 444-466, print date 2026-10-01**,
originally published online 2025-07-09) — same paper already logged
2026-09-22, just now with its final print-issue placement resolved. The
Damavandi, Antia, & Kopalle (*JM*) and Ohlwein & Bruno leads resurfaced in
tonight's searches with no changes; not re-verified line-by-line again
tonight since nothing in the search results suggested any update.

**Kim & Moon (2025, *Foods*, egg-market/tariff-concern moderator)** — not
independently re-verified tonight (already Crossref-confirmed 09-25); its
B/C-tier relevance assessment from that note stands unchanged.

**A quick additional Crossref sweep for "tariff blame attribution
consumer" (2026+ only)** surfaced nothing else on-point — mostly unrelated
AI/chatbot/algorithm blame-attribution literature (a busy adjacent
research area right now, coincidentally, but not this project's topic).

## 4. JCM special issue / AMS 2026 — a possible critical deadline discrepancy, flagged but not resolved

This is the most important thing from tonight and needs Britton's own eyes
— **also written into `SUBMISSION_TRACKER.md` as a new flagged section**
("⚠ Possible critical discrepancy found 2026-09-26"), not just here.

**What was directly fetched and read tonight (primary source):** the same
CFP PDF this project's `notes/2026-08-04-design-locked-jcm-fit.md` says it
"fetched and read 2026-08-04"
(`static1.squarespace.com/static/648893d9cbee3c0b58b73264/t/
68dc047b45ddc55e4c7a4014/1759249531662/JCM+SI+CFP+for+AMS+website.pdf`).
Read in full tonight. Its "Key Dates" section states, verbatim:

> Submission Deadline for Initial Full Manuscripts: **October 15, 2025**
> AMS 2026 Annual Conference: May 12–14, 2026
> Revised Manuscript Submission to JCM: Post-conference, **June 15-August
> 15, 2026**

That is **2025**, not 2026, for the AMS-conference-track full-manuscript
deadline this project's `CLAUDE.md`, root `README.md`, and
`SUBMISSION_TRACKER.md` all currently describe as "Oct 15, 2026." The
document's other listed date — the direct JCM ScholarOne window, June
15–Aug 15, 2026 — matches exactly what `SUBMISSION_TRACKER.md` already
separately (and, on this reading, correctly) describes as **already
closed** as of today. The string "October 15, 2026" does not appear
anywhere in this document. A second, independently-uploaded copy of what
looks like the same CFP (ResearchGate, publication ID 396046122) is
titled *"...Submission Deadline: August 15, 2026"* in its own header —
external, independent corroboration that August 15, 2026 (not October 15,
2026) is the terminal date as others have read this same document.

**Against that:** a WebSearch AI-generated summary tonight (explicitly
*not* a primary source, and this project's own rule is not to take a
search summary's word for a citation or fact) claimed the Emerald-hosted
version of the CFP shows "Special Issue submission deadline: 15 October
2026." Two attempts to verify this directly tonight both failed:

1. `emeraldgrouppublishing.com`'s CFP page redirects (real `301`, followed
   correctly) to `emerald.com/jcm/calls-for-submissions/1762/...`, which
   returned a Cloudflare `403` bot-challenge on every attempt tonight —
   never got real page content.
2. A second URL the same search surfaced
   (`ams-web.org/news/special-issue-of-the-journal-of-consumer-marketing`)
   returned a **genuine `404`** — actual "Page Not Found" site content,
   not a block/challenge page. That specific URL does not currently exist
   on the live AMS site, regardless of what a search index shows.

**Genuinely unresolved as of tonight — not spun toward either date.**
Three honest possibilities, in no particular order of likelihood: (a) the
squarespace/ResearchGate copy is accurate and this project has been
carrying a one-year date error (2025→2026) since the 2026-08-04
design-lock note, in which case both stated entry points into this special
issue may have **already closed**, months ago in one case and about six
weeks ago in the other; (b) the Emerald page genuinely shows a different,
later date (e.g., the whole timeline slipped a year and Emerald has the
corrected version while the squarespace/ResearchGate copies are stale
drafts) and Oct 15, 2026 is real; (c) the WebSearch summary is simply
wrong or is echoing back this project's own already-public GitHub-mirrored
"Oct 15, 2026" framing rather than an independent finding. This session
could not distinguish between these tonight given the access blocks on
both the Emerald page and the AMS URL.

**This was not resolved and was deliberately not "fixed" one way or the
other in `CLAUDE.md`/`SUBMISSION_TRACKER.md`'s existing deadline framing**
— given how much of this paper's entire critical path (IRB, Study 2/3,
write-up) is planned backward from that one date, this is squarely a
"needs Britton, not another automated guess" situation. See the new
`SUBMISSION_TRACKER.md` section for the specific, concrete next step
recommended (a direct human check of the Emerald URL from an ordinary
browser, or a direct email to the guest editors — contact info included
there).

## What's stable vs. what changed, summary

**Changed since 09-25:**
- Wayback Machine access held up for a second consecutive night (still not
  guaranteed going forward, but two-for-two now).
- New verified find: Columbia Bernstein Center grant-award page confirming
  a real, funded ($10,000) Morwitz project behind the MarketWatch op-ed,
  recovered via Wayback (live page still blocked).
- New verified lit lead: Davidson & Schaefer (2025, SSRN), tariff
  justification framing → WTP, partisan-moderated — a strong structural
  match to this project's own design, stronger fit than the 09-25 egg-
  market lead.
- Campbell et al.'s JCR paper now has a confirmed print-issue placement
  (53(3), pp. 444-466, Oct 2026 print date) — same paper, just fully
  resolved bibliographically now.
- V.O.S. Selections' response-brief countdown moved from 10 to 9 days out
  (expected, not a docket event).
- **A possible critical deadline discrepancy on the JCM special issue's
  actual submission date(s) — flagged, not resolved, needs Britton.**

**Fully stable / unchanged since 09-25:**
- All four litigation dockets — same entry counts, same verbatim text on
  the latest entries, no rulings, no terminations, no oral-argument date
  set on V.O.S. Selections.
- The live (non-Wayback) Columbia URL and the live Bernstein Center award
  page — both still `HTTP 403` Cloudflare-blocked.

**Still genuinely open:**
- **The JCM special issue's real deadline(s) — see §4. This is now the
  single most important open item for Britton to personally resolve**,
  independent of anything else in this project.
- Whether the Wayback access-restoration holds up beyond two nights.
- The full MarketWatch op-ed text — still paywalled, still out of scope.
- Whether Fitzsimons is formally attached to the Bernstein Center grant or
  only to the resulting op-ed — not resolved tonight.
- CITI/HSIRB turnaround, Jason's blind-coding worksheet, Study 2/3 data
  collection — not touched tonight, out of this session's task scope.

## For Britton

1. **Please personally check the JCM special-issue deadline before relying
   on "Oct 15, 2026" for anything else.** The actual CFP PDF this
   project's own notes cite as having been read on 2026-08-04 literally
   says "October 15, **2025**" for the AMS-track manuscript deadline (long
   past) and "June 15-August 15, **2026**" for the direct JCM ScholarOne
   window (also now past, about six weeks ago) — not October 15, 2026
   anywhere. A second independent copy of the same CFP (ResearchGate)
   agrees the real terminal date is August 15, 2026. I could not confirm
   or rule out a corrected "Oct 15, 2026" date on Emerald's own site
   tonight (it's Cloudflare-blocked from this container) or on the AMS
   page a search engine pointed to (genuinely a dead link). This is
   flagged in detail in `SUBMISSION_TRACKER.md` with the guest editors'
   contact info — please check directly (browser or email) rather than
   trusting either an old project note or an AI search summary on this
   one, given how much rides on it.
2. **All four litigation dockets are fully stable tonight** — nothing new
   since 09-25. V.O.S. Selections' Federal Circuit response brief is now 9
   days out (10/05/2026); no oral argument date has been set on that
   docket.
3. **Good news, second night running: the Morwitz/Fitzsimons Wayback
   route still works**, and tonight turned up a bonus — a Columbia
   Bernstein Center for Leadership and Ethics grant page (also via
   Wayback; live page still blocked) confirming the op-ed is backed by a
   real, named, funded academic project on exactly this paper's question.
   Quoted in full above.
4. **One strong new literature lead:** Davidson & Schaefer (2025, SSRN
   working paper) — tariff-justification framing lowers willingness to
   pay, driven by Democrats/Independents, partisan-moderated. Verified via
   Crossref. Worth a real read (not just a citation), given how closely it
   maps onto this project's own theory chain.
