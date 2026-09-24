# 2026-09-24 — Litigation recheck (Section 301 picks up one new routine entry; other three dockets fully unchanged) + two new verified literature leads + a stale SUBMISSION_TRACKER.md item fixed

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session. Four parts, same
scope as recent nights: (1) the standing four-docket litigation recheck;
(2) a further access attempt on the Morwitz/Fitzsimons MarketWatch op-ed
flagged 09-23 as real-but-not-yet-citable; (3) a literature-currency
scouting pass specific to tariff messaging / consumer blame attribution /
corporate crisis communication; (4) a check on SUBMISSION_TRACKER.md's
standing open items, which turned up one item that was actually already
resolved and just not reflected in the tracker — fixed below.

## 1. Litigation recheck — Section 301 picks up one new, routine entry; all three others fully unchanged

Same four CourtListener docket URLs as every prior night, fetched via
plain `curl` with a browser User-Agent, parsed with `beautifulsoup4`
(installed fresh this session, as usual for this container):

1. Section 301 forced-labor master docket — `https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`
2. Section 122 appeal, *State of Oregon v. Trump* (CAFC 26-1804/-1805) — `https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`
3. V.O.S. Selections (CAFC 26-1895) — `https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`
4. Axle of Dearborn (CIT 1:25-cv-00091) — `https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

All four returned a real HTTP/2 200 (confirmed past the proxy's own
`HTTP/1.1 200 Connection Established` CONNECT line — checked explicitly
this time by grepping for the second status line in each header dump)
with `x-cache: Miss from cloudfront` and `date:` headers of `Thu, 24 Sep
2026 05:15:3[2-6] GMT`, matching tonight's actual fetch time within
4 seconds across all four — fresh, not cached, responses.

| Docket | Entries 09-23 | Entries tonight | Change |
|---|---|---|---|
| Section 301 | 53 | **54** | +1 (new) |
| Section 122 | 106 | 106 | None |
| V.O.S. Selections | 26 | 26 | None |
| Axle of Dearborn | 79 | 79 | None |

**Section 301 — one new entry, routine, not a ruling.** Entry #54, filed
and entered 09/23/2026:

> Form 11 Notice of Appearance — Additional Appearance for Eric J.
> Hamilton. Filed by Douglas Glenn Edelschick of U.S. Department of
> Justice on behalf of All Defendants. (Entered: 09/23/2026)

This is a DOJ attorney adding himself to the case (a second/additional
appearance for the defense side) — standard housekeeping, not a
substantive filing. No deadline is created or changed by it. For
context, entry #53 (Sep 21 Joint Appendix, unchanged from 09-23) remains
the last substantive filing.

**Section 122, V.O.S. Selections, Axle of Dearborn — fully unchanged,
reread directly.** Pulled entries #104-106 (Section 122), #24-26 (V.O.S.),
and #77-79 (Axle) as full text, not just counts, and compared verbatim
against the 09-23 account — identical in every case:

- **Section 122**: entry #99 (the actual order text, re-pulled and
  quoted directly tonight rather than assumed unchanged) confirms:
  *"ORDER filed granting Appellants' motion [96] to extend the time to
  file the response and reply brief by 30 days, until 11/12/2026. By:
  Per Curiam."* Government brief deadline still 11/12/2026, directly
  reconfirmed in docket text (not inferred from absence of a new order).
- **V.O.S. Selections**: entry #26 (Sep 15 text-only order) unchanged —
  response brief still due 10/05/2026. **This is now 11 days out** from
  tonight (2026-09-24). Still only 26 entries; no new filing since the
  Sep 15 order.
- **Axle of Dearborn**: entries #77-79 (reassignment + stay/reliquidation
  order pair) — unchanged verbatim.

Checked all four dockets programmatically (case-insensitive search of the
full extracted page text) for "date terminated" or any termination-status
string — none found on any of the four; all remain open/active.

**Bottom line: nothing that changes either pending deadline.** Section
301's new entry is a defense-side notice of appearance, not a ruling. The
two dates still worth watching: **V.O.S. Selections' 10/05/2026 response
brief (11 days out)** and **Section 122's 11/12/2026 government brief
(~7 weeks out)**.

## 2. Morwitz/Fitzsimons op-ed — tried five alternate access routes tonight, still not independently readable

Per tonight's task, tried to get past the Cloudflare block on Columbia's
mirror and read the actual op-ed text (or find an underlying paper),
beyond what 09-23 already confirmed (real authorship/venue/date, via
Morwitz's own CV).

**Routes tried tonight, all unsuccessful:**
1. **Columbia's own article-mirror URL** (a more specific URL than the
   generic "faculty awards" page tried 09-22/09-23 —
   `business.columbia.edu/faculty/research/opinion-rising-prices-upset-
   shoppers-do-retailers-dare-tell-truth-about-whos-blame`, surfaced by
   WebSearch tonight): still HTTP 403 with `cf-mitigated: challenge` on
   direct fetch — same Cloudflare bot-block as before, different specific
   URL, same result.
2. **Wayback Machine** — the Wayback availability API confirms a real
   snapshot exists (`web.archive.org/web/20260421185900/...`, status 200,
   captured 2026-04-21), but `web.archive.org` is blocked at the network
   level in this container (`x-block-reason: hostname_blocked` from the
   egress proxy, confirmed both via direct `curl` and via the WebFetch
   tool, which returned "unable to fetch from web.archive.org"). This is
   an environment restriction, not evidence the content doesn't exist —
   flagging for Britton: if he has unrestricted web access, that Wayback
   snapshot URL is a real, findable capture worth trying himself.
3. **archive.ph / archive.today** — connection reset by the proxy on two
   separate attempts (`ws_closed_mid_exchange`); could not determine
   whether a snapshot exists there.
4. **Direct MarketWatch fetch** (guessed canonical URL,
   `marketwatch.com/story/rising-prices-upset-shoppers-do-retailers-dare-
   tell-the-truth-about-whos-to-blame-2025-09-03`) — HTTP 401
   (subscriber paywall), via WebFetch and via `curl`. Also moot re: this
   repo's own no-paywalled-full-text rule even if it had loaded.
5. **The allpennystocks.com newswire mirror** flagged dead 09-23 — retried
   tonight, still 302-redirects to that site's own internal 404 message
   page. Confirmed dead, not a transient failure.
6. **SSRN author pages** (Morwitz, `per_id=95189`) and a **ResearchGate**
   search for "Morwitz Fitzsimons tariff" — both returned HTTP 403
   (bot-protection pages, not found/paywall).

**No underlying working paper or peer-reviewed article was located** via
several further WebSearch angles tonight either (author-name + "tariff,"
+ "disclosure," + "1500," + "2026" combinations) — search-engine
synthesis still only reproduces the same claims already logged 09-23
(itemized-disclosure blame-shift, fairness/purchase-intent cost, partisan
moderation), with no new citing source. Also re-checked: no new
title matching this project on Morwitz's Columbia CV or Fitzsimons' Duke
faculty/Scholars@Duke page as of tonight's search (not re-fetched
directly tonight since 09-23 already pulled the CV as a primary source
and nothing suggests it changed; flagging this as unconfirmed-tonight
rather than reasserting it as freshly checked).

**Conclusion: still not citable as content.** Existence, authorship,
venue, and date remain the only independently confirmed facts (per
09-23's CV-sourced verification). Recommend Britton try the Wayback
snapshot URL above directly (`web.archive.org/web/20260421185900/https://
business.columbia.edu/faculty/research/opinion-rising-prices-upset-
shoppers-do-retailers-dare-tell-truth-about-whos-blame`) from a normal
browser, since this session's network cannot reach it but a human browser
likely can — that's a concrete, specific next step, not just "keep
checking."

## 3. Literature-currency scouting pass — two new verified leads, one prior lead's citation formally confirmed

Searched several angles combining tariff messaging, consumer blame
attribution, price-increase justification, and corporate crisis
communication, per tonight's task scope.

**New lead A — Damavandi, Antia, & Kopalle (2026), "Cushioning the Blow:
Reducing Customer Attrition in Response to Price Increase Notifications,"**
*Journal of Marketing*, published online 2026-05-11, DOI
`10.1177/00222429261451752`. Confirmed directly via the Crossref API
(not inferred from a search snippet) — real citation, with full author
names (Hoorsana Damavandi, Kersi D. Antia, Praveen K. Kopalle) and
abstract pulled from Crossref's own metadata. Per the abstract: a
field experiment with a "multisite Canadian storage provider," three
randomized studies (a field experiment with 10 cohorts of 1,626 actual
customers, plus two online scenario experiments) comparing **cost,
market, and quality justifications** for price increases, finding
market-based justification produces the *lowest* customer attrition —
mediated by customers' switching-cost perceptions, not by fairness
perceptions directly. **Why relevant:** this is a direct empirical
parallel to this project's core manipulation (how a firm frames/
justifies a price increase — attribution frame — affects consumer
response), from the same top-tier venue (JM) and same 2026 window,
though the mechanism it foregrounds (switching costs) differs from this
project's fairness/opportunism mediators. Not the same theoretical
model, but a citable, on-point comparison/contrast paper for the
Discussion or a "related approaches" paragraph. Abstract quoted above is
from Crossref's own metadata field, not paraphrased into a stronger
claim.

**New lead B — Sheibani Moghadam, Keimasi, & Hendijani (2026), "Matching
crisis response strategies to crisis types: insights from construal
level theory and situational crisis communication theory for
understanding consumer responses,"** *Italian Journal of Marketing*,
published online 2026-04-15, DOI `10.1007/s43039-026-00133-5`. Confirmed
via Crossref (author names, venue, date) and abstract/content summary
via the article's own SpringerLink page (open-access; no paywall
encountered past the standard session-cookie redirect). Uses
**Situational Crisis Communication Theory (SCCT)** — the foundational
corporate-crisis-communication framework this project's "corporate
crisis communication" framing sits in — crossed with **Construal Level
Theory**, examining individual-threatening vs. society-threatening
crises and private vs. public apology strategies; finds apology-type
effectiveness depends on crisis-type alignment, mediated by anger. **Not
about tariffs or pricing** (confirmed directly — no mention of either in
the full-text summary pulled) but a recent, on-point *theoretical
framework* citation if Britton wants to explicitly ground the paper's
"is a tariff price increase a corporate crisis" framing in SCCT
scholarship rather than assuming the connection. Flagging as a framework
lead, not a findings lead — do not conflate with leads A or the Campbell/
Morwitz threads, which are about price-fairness/blame mechanisms
specifically.

**Prior lead formally verified tonight:** 09-23's note flagged Ohlwein &
Bruno (2025), "Algorithms of (un)fairness – Is personalized pricing fair
game or foul play?" as a DOI-only, not-yet-Crossref-verified lead.
Verified tonight via the Crossref API: real, DOI
`10.1177/14707853251338579` resolves to *International Journal of
Market Research* (not directly journals.sagepub.com-branded, though
SAGE-published), authors Martin Ohlwein and Pascal Bruno, published
online 2025-05-03. This closes the verification gap 09-23 left open;
still the same caveat as 09-23 — a different pricing context
(algorithmic/personalized pricing, not tariffs) — so it remains a
structurally-similar-mechanism lead, not a directly on-topic one.

**No other new, clearly on-point 2025-2026 paper surfaced** beyond these
three and the already-logged Campbell et al. (2025) JCR paper (09-22) and
the still-unconfirmed Morwitz/Fitzsimons thread (above). One broader
search on "tariff surcharge disclosure" mostly surfaced law-firm client
alerts (Katten Muchin Rosenman) and industry pulse surveys (Simon-Kucher,
First Insight) rather than peer-reviewed work — noting these exist as
practitioner-facing context, not as citable academic sources, and not
pursuing them further.

## 4. SUBMISSION_TRACKER.md open items — one stale item found and fixed, others reconfirmed unchanged

**Purchase Intention item count — found already resolved and built,
tracker language was stale.** The tracker's open-questions list (item 4)
still read "Only remaining choice is 5 items vs. a 3-item subset — a
quick yes/no, not a blind pick," framing it as outstanding. Checked the
actual instrument files: `Study2_Qualtrics_Instrument_READY_2026-09-09.md`
Block 8 states explicitly *"Britton's 2026-09-07 call: use all 5 original
items (not the trimmed 3-item subset)"* and lists all 5 Dodds/Monroe/
Grewal (1991) items verbatim. Cross-checked against the actual Qualtrics
import file, `Study2_Qualtrics_IMPORT_2026-09-11.txt` — grepped directly
and confirmed all 5 items (including both "at the price shown" variants)
are present in the built `[[Block:Purchase Intention]]` section. **This
decision was made 2026-09-07 and is already implemented in the built
survey; the tracker's "still outstanding" framing was drift from an
earlier version.** Fixed in `SUBMISSION_TRACKER.md` tonight (see below) —
this is a concrete correction, not a new decision made on Britton's
behalf; the choice itself is fully attributable to Britton's own
2026-09-07 call, already on record in the instrument file.

**CITI Comprehensive-vs-Basic / HSIRB turnaround — reconfirmed
unchanged, two dead-link leads closed off.** Refetched the same McNeese
policy page directly; exact text unchanged from every prior check back
to 09-09 (same "Enacted February 28, 2023; Revised July 28, 2025;
February 19, 2026" revision history, same Comprehensive-module language,
same `irbchair@mcneese.edu` contact — already known since the 09-10
blocker-briefing note, not new tonight). Tried two additional URLs a
fresh WebSearch surfaced tonight — a `mcneese.edu/hsirb/
institutional_review_board/` "Home" page and an `IRB-Flowchart.pdf`
decision-tree document — both returned McNeese's generic 404 page on
direct fetch. **Both are dead links, not new sources**; closing them off
so a future session doesn't re-try the same two dead ends. No turnaround
time is stated anywhere public; still genuinely requires a direct ask to
irbchair@mcneese.edu, same conclusion as every check since 09-09.

**Jason's blind-coding worksheet** — checked locally:
`Study1_Validation_Pilot_BLIND_CODING_WORKSHEET_2026-08-27_FULL_CORPUS.md`
still shows the same file modification time as the rest of the initial
repo checkout (2026-09-20 05:05, i.e., unchanged since this repo's last
bulk sync) and, read through, is still the blank instruction/template
version, not a filled-in comparison — no coded entries, no Gwet's AC1
inputs present. This is purely a local-file check; it cannot tell us
whether Jason has since sent Britton a filled version through some other
channel (email, a separate doc) that hasn't reached this repo — genuinely
not resolvable from here, same as every prior night.

**Banked scales and the two Qualtrics-build decisions** — not touched
tonight; both are explicitly Britton's design calls per
`notes/2026-08-13-design-confirmed-3x2-word-budget.md` and
`Study2_Qualtrics_POST_IMPORT_CHECKLIST_2026-09-11.md`, and neither has
a useful non-decision groundwork step left to do (the banked-scale
candidates are already named/scoped in the 08-13 note; sourcing full
item sets for all of them before Britton picks one would be speculative
work, not groundwork). Consistent with task scope not to make these
calls.

## Project-file drift check

`git log` for `TARIFF_PAPER` shows the 09-23 note as the last commit;
`git status` on the folder is clean going into tonight's session. No
files touched tonight other than this note and `SUBMISSION_TRACKER.md`
(one specific, concrete correction — see above).

## For Britton

- **Litigation: one new but routine entry on Section 301** (a DOJ
  attorney's notice of appearance, 09/23) — not a ruling, no deadline
  change. Section 122, V.O.S. Selections, and Axle of Dearborn are fully
  unchanged from 09-23. **V.O.S. Selections' 10/05/2026 response brief is
  now 11 days out**; Section 122's 11/12/2026 government brief is
  ~7 weeks out, reconfirmed directly in the docket's order text tonight.
  All four dockets remain open, no terminations.
- **Morwitz/Fitzsimons op-ed: tried five more access routes tonight
  (Columbia's specific article-mirror URL, Wayback Machine, archive.ph,
  direct MarketWatch, SSRN/ResearchGate) — still can't independently read
  the text.** One concrete lead for you specifically: the Wayback Machine
  confirms a real archived snapshot of Columbia's mirror page exists
  (`web.archive.org/web/20260421185900/https://business.columbia.edu/
  faculty/research/opinion-rising-prices-upset-shoppers-do-retailers-
  dare-tell-truth-about-whos-blame`) — this session's network can't reach
  web.archive.org at all (environment-level block), but your own browser
  likely can. Worth two minutes if you want the actual text before
  deciding whether/how to reference this thread.
- **Two new, verified 2026 literature leads worth a look:**
  (1) Damavandi, Antia, & Kopalle, *Journal of Marketing* (2026), on cost/
  market/quality justifications for price increases and customer
  attrition — a directly comparable empirical design (different
  mechanism: switching costs, not fairness) from a top venue, good for a
  "related approaches" citation. (2) Sheibani Moghadam, Keimasi, &
  Hendijani, *Italian Journal of Marketing* (2026), applying Situational
  Crisis Communication Theory + Construal Level Theory to crisis-response
  matching — not about tariffs, but a live 2026 SCCT application if you
  want to more explicitly ground this paper's "tariff pricing as
  corporate crisis communication" framing in that literature.
- **One tracker correction made tonight, not a new decision:** the
  Purchase Intention "5 items vs. 3-item subset" open question was
  actually already decided by you on 2026-09-07 and is already built into
  the live Qualtrics import file — the tracker just hadn't caught up.
  Fixed in `SUBMISSION_TRACKER.md` tonight.
- **CITI/HSIRB: still unchanged, still needs your direct email to
  irbchair@mcneese.edu** — two more search leads chased tonight both
  turned out to be dead links, closing those off for future sessions.
- Everything else (Jason's worksheet, banked scales, the two Qualtrics
  decisions) is unchanged — not resolvable from this end tonight, same
  as prior nights.
