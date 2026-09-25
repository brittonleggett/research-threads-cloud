# 2026-09-25 — Litigation recheck (all four dockets fully stable), Wayback Machine network block appears lifted and yields a citable Morwitz/Fitzsimons abstract, literature scouting (one new-to-project lead)

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session, same scope as recent
nights: (1) a note on this session's git/worktree base, which matters for
anyone reconciling notes; (2) the standing four-docket litigation recheck;
(3) a further access attempt on the Morwitz/Fitzsimons MarketWatch op-ed,
per the 09-24 note's specific next step; (4) a literature-currency scouting
pass on tariff messaging / consumer blame attribution / price-increase
justification / corporate crisis communication.

## 0. A note on this session's starting point (important for reconciling notes)

This session's git worktree was branched from `origin/main` at commit
`70f6cdb` ("Add 2026-09-19 overnight summary") — **before** the 09-20
through 09-24 nightly work on this paper. That work exists in this
machine's git object store (readable via `git show <sha>:<path>`, e.g.
`git show 498378b:TARIFF_PAPER/notes/2026-09-24-litigation-recheck-...md`)
but is **not present as files in this worktree** and was not merged into
this branch. I read the 09-24 note that way, as context, per this task's
instructions, but did **not** copy it or its same-night `SUBMISSION_TRACKER.md`
fix into this branch — that would risk duplicate/conflicting content when
this branch and the 09-20–09-24 branch both eventually get merged. One
concrete effect: **`SUBMISSION_TRACKER.md` in this checkout still shows the
stale "5 items vs. 3-item subset still outstanding" language that the 09-24
note found and fixed on its own branch** — this is not a regression I
caused or a fact I'm re-asserting as open; it's just this branch's base
predating that fix. Whoever reconciles/merges these branches should be
aware there are (at least) two parallel forward-moving branches for this
project's `notes/` and tracker right now. I did not touch
`SUBMISSION_TRACKER.md` tonight.

## 1. Litigation recheck — all four dockets fully unchanged since 09-24

Same four CourtListener dockets as every prior night. Direct-fetched
tonight (2026-09-25) with a browser User-Agent via plain `curl`; the plain
docket-page 403 that showed up on a bare first attempt went away once
`Accept`/`Accept-Language` headers were added alongside the UA (same
CloudFront-WAF-sensitive pattern noted in earlier sessions). All four
returned a real, fresh `HTTP/2 200` (`x-cache: Miss from cloudfront`,
`date:` headers all `Fri, 25 Sep 2026 05:15:5[9]`–`05:16:00 GMT`, within one
second of each other and of the actual fetch time) — not cached, not
CAPTCHA/challenge pages.

| Docket | Entries 09-24 | Entries tonight (09-25) | Change |
|---|---|---|---|
| Section 301 forced-labor master docket | 54 | **54** | None |
| Section 122 appeal (*Oregon v. Trump*, CAFC 26-1804/-1805) | 106 | **106** | None |
| V.O.S. Selections (CAFC 26-1895) | 26 | **26** | None |
| Axle of Dearborn (CIT 1:25-cv-00091) | 79 | **79** | None |

Not just counts — pulled the actual entry text for the latest entry on
each docket (and the specific order text on Section 122/V.O.S.) and
diffed against the 09-24 note's verbatim quotes. All identical:

- **Section 301, entry #54** (Sep 23, 2026): *"Form 11 Notice of Appearance
  Additional Appearance for Eric J. Hamilton. Filed by Douglas Glenn
  Edelschick of U.S. Department of Justice on behalf of All
  Defendants...(Entered: 09/23/2026)"* — same DOJ notice-of-appearance
  housekeeping entry flagged 09-24, still the last entry, nothing filed
  since.
- **Section 122, entry #106** (Sep 18, 2026, notice of correction to an
  amicus filing) and **entry #99** (the actual order: *"ORDER filed
  granting Appellants' motion [96] to extend the time to file the
  response and reply brief by 30 days, until 11/12/2026. By: Per
  Curiam."*) — both verbatim-identical to 09-24. Government brief deadline
  still 11/12/2026.
- **V.O.S. Selections, entry #26** (Sep 15, 2026, text-only order):
  *"...granting motion to extend time to file brief [25] filed by Appellee
  V.O.S. Selections, Inc. The response brief is due 10/05/2026..."* —
  verbatim-identical to 09-24. **This is now 10 days out** from tonight
  (2026-09-25), down from 11 days as of 09-24. Still only 26 entries, no
  new filing.
- **Axle of Dearborn, entry #79** (the Aug 25 reliquidation order,
  full text re-pulled tonight) — verbatim-identical to 09-24.

Checked all four docket pages' full text tonight for a "date terminated"
string (case-insensitive) — none found on any of the four; all remain
open/active.

**One terminology note, not a correction to anyone, just accuracy:** this
task's framing referred to "V.O.S. Selections' Supreme Court response
brief." Per this project's own primary-source record (see
`notes/2026-08-31-vos-selections-atmus-filtration-resolved.md`), the
Supreme Court already ruled on the underlying IEEPA tariff-authority
question in February 2026 (*Learning Resources*/*V.O.S. Selections*, Feb
20, 2026). What's currently pending and tracked in this project's docket
checks is a **different, later matter**: *V.O.S. Selections, Inc. v.
Trump*, Fed. Cir. No. 26-1895 — a Federal Circuit appeal of a CIT
liquidation/reliquidation order, with the appellee's response brief due
10/05/2026 (now 10 days out). Flagging this distinction plainly rather
than assuming the task description's "Supreme Court" framing and silently
citing the wrong court.

**Bottom line: nothing new on any of the four dockets tonight.** No
rulings, no new substantive filings, no terminations. The two dates still
worth watching are unchanged from 09-24: V.O.S. Selections' 10/05/2026
response brief (10 days out) and Section 122's 11/12/2026 government
brief (~7 weeks out).

## 2. Morwitz/Fitzsimons op-ed — the Wayback Machine network block appears to have lifted tonight, and it yields a real, citable abstract

Per the 09-24 note's specific next step, retried the exact Wayback
snapshot URL it had already identified but couldn't reach
(`web.archive.org/web/20260421185900/https://business.columbia.edu/
faculty/research/opinion-rising-prices-upset-shoppers-do-retailers-dare-
tell-truth-about-whos-blame`).

**Tonight this returned a real HTTP 200 with actual archived page
content** — not the `x-block-reason: hostname_blocked` proxy rejection
every prior session hit. Verified this wasn't a fluke or a misleading
proxy response: the response carries a genuine `memento-datetime: Tue, 21
Apr 2026 18:59:00 GMT` header and a full set of `x-archive-orig-*` headers
(`x-archive-orig-server: cloudflare`, `x-archive-orig-x-generator: Drupal
10`, etc.) consistent with a real archived Columbia Business School page,
not a synthetic/error response. This looks like the container's
network-level block on `web.archive.org` specifically has been lifted (or
loosened) since 09-24 — **this is a change worth noting, not something to
assume is now permanently fixed.** Two caveats on how far this extends:

1. **The live (non-archived) Columbia URL is still blocked** — direct
   fetch of `business.columbia.edu/faculty/research/opinion-...` still
   returns `HTTP 403` with Cloudflare's bot-challenge page tonight, same
   as every prior session. Only the Wayback path worked.
2. **Wayback's own service had a partial outage during this same
   session** — a follow-up query to the Wayback CDX search API (checking
   whether the actual MarketWatch article itself, not just Columbia's
   citation page, has any snapshot) returned an Internet Archive
   "Temporarily Offline" service page rather than real CDX data. So
   Wayback access is real tonight, but not fully reliable — didn't
   exhaustively retry the CDX endpoint, since the citation-page snapshot
   already answered tonight's actual question (see below) and burning
   more time chasing a paywalled news article's own snapshot isn't
   worthwhile per this repo's no-paywalled-full-text rule regardless.

**What the recovered snapshot actually contains — and why it matters:**
this is not the MarketWatch op-ed's own page. It's **Columbia Business
School's own faculty-research citation page** for the piece, archived
2026-04-21. Critically, that page includes a full author-written
**abstract of the op-ed's actual findings**, not just bibliographic
metadata. Quoted here in full, exactly as it appears on the archived
Columbia page (this is Columbia's own published abstract text, not a
paraphrase, and not the copyrighted MarketWatch article itself):

> "Our studies examine how consumer attribution of blame and purchasing
> behavior change when retailers provide transparent explanations for
> tariff-related price increases. Through two experiments involving over
> 1,500 U.S. adults, we found that when tariffs were explicitly disclosed
> on itemized bills, consumers were significantly more likely to blame
> the government rather than retailers or the broader economy for price
> hikes. However, transparency came with trade-offs: while it redirected
> blame away from retailers, consumers still perceived tariff-disclosed
> prices as less fair and showed reduced willingness to purchase, even
> when total costs remained identical. Our studies also revealed
> partisan differences, with Trump supporters less likely to blame the
> government for tariff costs compared to those with more negative views
> of the President. These findings suggest that as new U.S. tariffs
> begin to affect consumer prices, businesses face a complex decision
> about transparency—clear explanations can protect a retailer's
> reputation. Still, they may not fully mitigate adverse consumer
> reactions. Our research highlights the importance of attribution in
> consumer behavior and the political dimensions of economic policy
> implementation at the retail level."

Full citation, also pulled directly from the same archived page:

> Morwitz, Vicki and Gavan Fitzsimons. "Opinion: Rising prices upset
> shoppers. Do retailers dare tell the truth about who's to blame?"
> *MarketWatch*. September 03, 2025.

**This changes the status of this thread from "existence/authorship/
venue/date confirmed, content not citable" (09-22 through 09-24) to
"substantively citable via a real, Columbia-hosted abstract of the
authors' own two-experiment (n>1,500) design and findings."** The design
described (itemized tariff disclosure → blame redirected toward
government but away from retailers; disclosed prices perceived as less
fair and lower purchase-willingness despite identical total cost;
partisan moderation by Trump approval) is now something this project can
cite and characterize with actual content, not just as "a real op-ed that
exists." Note precisely what this is and isn't: it's the authors'/
Columbia's own published abstract of a two-study design, not the full
op-ed text and not a peer-reviewed paper — appropriate to cite as an
op-ed/research-summary source (as originally categorized), now with real
substance behind the citation rather than a blind reference. The
underlying MarketWatch article text itself remains behind a paywall (still
`HTTP 401` on direct fetch tonight) and out of scope to pursue further
regardless, per this repo's no-paywalled-full-text rule.

**Saved locally only:** the raw fetched HTML and extracted text are in
this session's scratchpad, not committed to the repo (consistent with
convention — this note is the citable record).

## 3. Literature-currency scouting pass — prior leads reconfirmed current, one new-to-this-project lead found

Ran several fresh angles (WebSearch and direct Crossref API queries) on
tariff messaging, consumer blame attribution, price-increase
justification, and corporate crisis communication.

**Prior leads reconfirmed as still the current state of the art** — both
Damavandi, Antia, & Kopalle (2026, *Journal of Marketing*, price-increase
notification justifications) and the Campbell et al. (2025, *JCR*) and
Ohlwein & Bruno (2025) threads resurfaced in tonight's searches with no
material changes; no indication any of these have been superseded or
retracted. Re-confirming via a fresh Crossref query rather than assuming
staleness.

**One new-to-this-project lead, verified directly via Crossref (not from
a search snippet):** **Kim, M.G. & Moon, J. (2025), "Price Fairness,
Consumer Attitude, and Loyalty in the U.S. Egg Market: The Moderating
Roles of Tariff Concern and Education Level,"** *Foods*, published
2025-06-25, DOI `10.3390/foods14132243`. Pulled directly from the Crossref
API (full author names, journal, date, and abstract field — not
paraphrased from a search result). Per the abstract: an online survey of
311 U.S. consumers (Clickworker platform), analyzed with Hayes's PROCESS
Macro (Model 7), testing **price fairness → consumer attitude → loyalty**
in the U.S. egg market, with **tariff concern and education level as
moderators**, finding both price fairness and attitude significantly
predict loyalty, and tariff concern significantly moderates the price
fairness → loyalty link. Checked this project's full `notes/` git history
(all commits, not just this branch) for any prior mention — genuinely not
previously logged.

**Why this is worth flagging, with the caveats stated plainly:**
structurally close to this project's own theoretical pattern (a fairness
variable → attitudinal/behavioral outcome, moderated by a tariff-related
variable, tested via a mediation/moderation macro on U.S. survey data) —
but it is about **eggs specifically** (a single-commodity food-price
context, not general retail tariff-pricing messaging), and *Foods* (MDPI)
is a food-science/agricultural-economics journal, not a marketing venue —
so this is a supporting/analogous-design citation at best, not a
head-to-head comparison paper like the Damavandi (JM) or Morwitz/
Fitzsimons leads. Flagging as B/C-tier relevance (real, verified,
on-point mechanism; off-topic venue and product category) rather than
overstating its fit.

**Nothing else new and clearly on-point surfaced tonight.** Repeated
searches mostly returned the same practitioner/industry-pulse sources
already logged as non-academic context in prior notes (Simon-Kucher, PMG,
Statista, eMarketer) — not pursued further as citations, consistent with
this project's standing distinction between practitioner commentary and
citable academic sources.

## What's stable vs. what changed, summary

**Changed since 09-24:**
- Wayback Machine access from this container appears to have opened up
  (at least for this specific, already-known snapshot URL) — this is new
  tonight, not something to assume is now permanently reliable.
- The Morwitz/Fitzsimons thread has real, citable content behind it now
  (Columbia's own abstract), not just bibliographic confirmation.
- One new-to-project literature lead (Kim & Moon 2025, egg market/tariff
  concern moderator) — real but tangential.
- V.O.S. Selections' response-brief countdown moved from 11 to 10 days
  out (expected, not a docket event).

**Fully stable / unchanged since 09-24:**
- All four litigation dockets — same entry counts, same verbatim text on
  the latest entries, no rulings, no terminations.
- The three previously-logged 2026 literature leads (Damavandi et al.,
  Sheibani Moghadam et al., Ohlwein & Bruno) — still current, no updates.
- `SUBMISSION_TRACKER.md` in this branch — not touched tonight (see §0
  for why its state may look behind what a different branch already
  fixed).

**Still genuinely open:**
- Whether the Wayback access-restoration holds up on a future session —
  not something this session can guarantee going forward.
- The full MarketWatch op-ed text itself — still paywalled, still out of
  scope regardless of Wayback access, per this repo's rules.
- The branch/worktree divergence noted in §0 — not something this session
  can resolve; flagging for whoever merges these parallel branches.
- CITI/HSIRB turnaround and Jason's blind-coding worksheet — not touched
  tonight, out of this session's task scope; last known status is in the
  09-24 note (read via `git show`, not duplicated into this branch).

## For Britton

1. **All four litigation dockets are fully stable tonight** — nothing new
   since 09-24 on Section 301, Section 122, V.O.S. Selections, or Axle of
   Dearborn. V.O.S. Selections' Federal Circuit response brief (not a
   Supreme Court filing — the Supreme Court already decided the underlying
   IEEPA question in February) is now 10 days out (10/05/2026).
2. **Good news on the Morwitz/Fitzsimons op-ed:** the Wayback Machine
   block that stopped every prior session seems to have lifted tonight,
   at least for the specific snapshot URL already identified. That
   snapshot is Columbia Business School's own faculty-research page for
   the piece, and it includes the authors' own abstract — a real,
   citable two-experiment (n>1,500) design and finding set, quoted in
   full above. This is a meaningfully stronger citation than what this
   project had before (existence/date/venue only). The MarketWatch
   article's own full text is still paywalled and still out of scope to
   pursue.
3. **One new, tangential literature lead:** Kim & Moon (2025, *Foods*) on
   price fairness/loyalty in the U.S. egg market with tariff concern as a
   moderator — verified real via Crossref, but off-topic venue/product
   category; a supporting citation at most, not a headline comparison.
4. **Housekeeping flag, not something for you to act on:** this session's
   git branch was created from an older point in the repo's history than
   the 09-20–09-24 nightly work on this paper (which exists elsewhere in
   the git history but isn't merged into `origin/main` yet). I read that
   work for context but didn't copy it into this branch, to avoid
   creating merge conflicts — whoever merges these parallel overnight
   branches should know there are two forward-moving threads on this
   paper's `notes/`/tracker right now that both need to land.
