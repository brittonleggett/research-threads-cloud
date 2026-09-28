# 2026-09-28 — Litigation recheck (all four dockets stable, VOS brief 7 days out), Dai et al. (2026) re-confirmed still unverifiable, one strong new literature find (Campbell, Pomerance & Percival Carter 2025/2026, *JCR*), JCM deadline not re-attempted per task instruction

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session, continuing directly
from `notes/2026-09-27-litigation-stable-davidson-schaefer-deep-read-jcm-
deadline-partial-lead.md`. Scope tonight: (1) recheck the standing four
CourtListener dockets; (2) re-attempt verification of the Dai, Xiang, Gu &
Zhou (2026, *JRCS*) lead via open-access/independent-verification routes
only (no paywall bypass attempted); (3) do **not** re-attempt the JCM/AMS
deadline question a third time via the same methods, per this task's
explicit instruction — noted as still open below and left for Britton; (4)
scan for new literature (last ~2 years) relevant to the project's
tariff-messaging/price-attribution/consumer-trust model. All claims below
are either (a) direct-fetch primary-source data (`curl` with a browser
User-Agent against CourtListener; Crossref/OpenAlex/Semantic Scholar/
Unpaywall API records) or (b) explicitly labeled as an unverified WebSearch
AI-summary where one is quoted.

## 1. Litigation recheck — all four dockets fully unchanged since 09-27

Direct-fetched all four CourtListener dockets tonight (2026-09-28, ~05:15-
05:16 GMT) with a browser User-Agent via `curl`. All four returned fresh,
genuine `HTTP/2 200`s (`x-cache: Miss from cloudfront`, `date:` headers
matching the fetch time) on the first attempt — no WAF challenge, no retries
needed.

| Docket | Entries 09-27 | Entries tonight (09-28) | Change |
|---|---|---|---|
| Section 301 forced-labor master docket (`courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`) | 54 | **54** | None |
| Section 122 appeal, *Oregon v. Trump* (CAFC 26-1804/-1805) (`courtlistener.com/docket/73318531/state-of-oregon-v-trump/`) | 106 | **106** | None |
| V.O.S. Selections (CAFC 26-1895) (`courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`) | 26 | **26** | None |
| Axle of Dearborn (CIT 1:25-cv-00091) (`courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`) | 79 | **79** | None |

Extracted and diffed the full HTML block for the latest entry on each docket
against the exact text quoted in the 09-27 note — all four are byte-for-byte
identical:

- **Section 301, entry #54** (Sep 23, 2026): same DOJ notice-of-appearance
  entry (Eric J. Hamilton) — unchanged, still the last entry.
- **Section 122, entry #106** (Sep 18, 2026, notice of correction to the
  Cato Institute/Ilya Somin amicus filing) — unchanged.
- **V.O.S. Selections, entry #26** (Sep 15, 2026 text-only order):
  *"...The response brief is due 10/05/2026..."* — verbatim-identical. **This
  is now 7 days out** from tonight (2026-09-28), down from 8 as of 09-27.
  No new filing, extension request, or oral-argument date on this docket —
  re-checked the page for "oral argument" hits; still only navigation-menu
  boilerplate, no scheduled date.
- **Axle of Dearborn, entry #79** (the Aug 25 reliquidation order) —
  unchanged.

Checked all four docket pages for a "date terminated" / "terminated" string
— none found on any of the four; all remain open/active.

**Bottom line: nothing new on any of the four dockets tonight.** No rulings,
no new substantive filings, no terminations — consistent with every night
since 09-19. **V.O.S. Selections' response brief (10/05/2026) is now 7 days
out — this is the one genuinely worth a same-day check around that date**,
per 09-27's note; not yet warranted tonight.

## 2. Davidson & Schaefer (2025, SSRN) — not re-attempted, per standing instruction

Per this task's explicit instruction ("don't waste more time on it"), the
SSRN paper itself was not re-attempted tonight. Nothing new to add beyond
09-27's finding (the genuinely open-access companion piece, Schaefer &
Davidson 2026, *Choices* 41(2), DOI 10.22004/ag.econ.369403, already read in
full and logged).

## 3. Dai, Xiang, Gu & Zhou (2026, *JRCS*) — independently re-confirmed still unverifiable, no change

Re-ran the verification (not a repeat of the same single check — hit four
independent routes plus one new one tonight) for **Dai, Luote; Xiang,
Kangli; Gu, Shengyu; Zhou, Xiao-Min (2026). "To serve the country or avoid
risk? The effects of strategic versus responsive CSR on consumer trust under
high tariff salience." *Journal of Retailing and Consumer Services*, Vol.
89(Part A), Feb. 2026, first published online 2025-10-18. DOI:
10.1016/j.jretconser.2025.104582.**

- **Crossref**: title/authors/venue/dates confirmed again; no abstract field.
- **OpenAlex**: confirmed again; `open_access.is_oa: false`, `oa_status:
  closed`, no PDF URL anywhere.
- **Unpaywall**: re-confirmed `is_oa: false`, `oa_status: closed`, zero OA
  locations.
- **Semantic Scholar** (not checked 09-27, new tonight): confirmed same
  title/authors/DOI; `abstract: null`; its `openAccessPdf` field is present
  but empty/placeholder (points back to Unpaywall, no actual PDF).
- **Direct `curl` fetch of the ScienceDirect abstract page**: `HTTP 403`,
  genuine Cloudflare bot-challenge page (`cf-mitigated: challenge`).
- **`r.jina.ai` reader-proxy fetch of the same URL** (new tonight, a
  genuinely different route, same logic 09-27 used on the Emerald CFP page):
  also hit Cloudflare's challenge page server-side (confirmed via the
  response itself: "Are you a robot? ... Verification successful. Waiting
  for www.sciencedirect.com to respond" — jina's own fetch got challenged,
  not a failure on this container's end).

**A WebSearch AI-summary tonight repeated the same specific claims flagged
as unverified on 09-27** (104% tariff on Chinese products as the
manipulation, three situational experiments, moral-affect/anger mediator,
tariff salience as an institutional-pressure variable). Per this project's
standing rule, still **not treating any of that as confirmed** — no primary
source (Crossref, OpenAlex, Semantic Scholar, Unpaywall, or a direct fetch)
has ever returned actual abstract or findings text for this paper. Status
unchanged from 09-27: real, verified existence and bibliographic details
only; content genuinely inaccessible from this container. **Still needs
Britton's own ScienceDirect/library access before citing anything beyond
title/authors/venue/DOI.**

## 4. JCM/AMS special-issue deadline — not re-attempted tonight, per task instruction

Per this task's explicit instruction (flagged two consecutive nights running
in `SUBMISSION_TRACKER.md`, needs Britton's own access/direct check, "don't
try a third time with the same methods"), **no new attempt was made tonight**
on this question. Status is exactly as 09-27 left it: genuinely unresolved,
one non-primary-source data point (a CFP-aggregator site) suggesting Oct 15,
2026 may be a real closing date on a single Aug 15–Oct 15, 2026 window, but
not confirmed from Emerald's own page (still Cloudflare-blocked) or
ResearchGate. **This remains open and needs Britton directly** — see
`SUBMISSION_TRACKER.md`'s flagged section, updated below with a short
pointer rather than a new attempt.

## 5. Literature scan — one strong new find, one secondary/lower-confidence lead, nothing else new

Ran targeted Crossref queries (2024-01-01 / 2024-06-01 onward filters)
across: "tariff price increase attribution fairness consumer," "corporate
tariff messaging framing consumer response," "tariff surcharge disclosure
consumer trust," "price increase blame attribution retailer," "tariff
pass-through consumer perception fairness," "consumer trust corporate
response tariff experiment," "attribution theory corporate blame price
increase consumer," and "tariff consumer trust brand experiment." Most
results were noise (CSR-messaging-in-general, drip-pricing, macro
pass-through econometrics unrelated to consumer psychology, and one
already-logged item, Kim & Moon 2025 egg-market/tariff-concern paper —
confirmed via `grep` of prior notes as already found 2026-09-25, not
re-logged as new). Two real, new-to-this-project hits:

### 5a. Campbell, Pomerance & Percival Carter (2025/2026, *Journal of Consumer Research*) — strong, verified, high-priority new find

**Campbell, Margaret C.; Pomerance, Justin; Percival Carter, Erin L. "Painful
Prices: The Moral Harm Model of Price Fairness." *Journal of Consumer
Research*, Vol. 53, Issue 3 (October 2026), pp. 444–466. Published online
2025-07-09 (advance article ahead of print). DOI: 10.1093/jcr/ucaf045.**

Verified independently via Crossref (title/authors/venue/date/DOI),
OpenAlex (which reconstructs a full abstract from its
`abstract_inverted_index` field — structured metadata, not a paywall
bypass), Unpaywall, and a direct WebFetch of the Oxford Academic landing
page (`academic.oup.com/jcr/article/53/3/444/8195730`), which independently
confirmed the same title/authors/date/volume/issue/pages and gave a
paraphrased version of the same abstract. **The actual PDF is Cloudflare-
blocked from this container** (`HTTP 403` on direct `curl`, `cf-mitigated:
challenge`) despite OpenAlex/Unpaywall listing it as nominally "hybrid OA"
with a CC-BY-NC-ND license — so, consistent with this project's rule against
paywalled full text, **full text was not read**; what follows is from the
verified abstract (OpenAlex's reconstruction, quoted near-verbatim below)
and the landing page only, not the full paper.

**Verbatim abstract (reconstructed from OpenAlex's structured
`abstract_inverted_index` field, cross-checked against WebFetch's
independent paraphrase of the same landing page — both agree):**

> "Consumers' responses to seller's prices, including perceptions of price
> fairness (PPF) and unfairness, are a crucial aspect of the marketplace.
> Although past literature has uncovered a variety of factors that
> influence PPF, the lack of an overarching conceptual framework has
> constrained understanding of when and why consumers are more likely to
> perceive prices as fair or unfair. The authors develop a conceptual
> model of PPF as moral judgments and propose that these moral PPF arise
> from consumer inferences of potential harm from a price. The
> conceptualization suggests that inferred harm—and thereby, PPF—is
> influenced by consumer vulnerability, product welfare impact and firm
> price strategy (e.g., costs and prices, differential pricing, and price
> promotions). The authors also propose that consumer political
> orientation and inferred firm self-defense motives moderate the
> relationship between inferred harm and PPF and that inferred firm
> motives for prices influence PPF. Eight studies test this
> conceptualization. The results support the moral harm model and provide
> novel insights, showing when unchanged prices, price increases, and
> price decreases are likely to be perceived as more unfair and when
> differential prices (including paying more than others) are likely to
> be perceived as fairer than equal prices."

**Why this is a high-priority find, not just another adjacent hit:**

1. **Margaret C. Campbell is the same scholar** whose 1999 Perceived
   Fairness two-item scale (r=.84) this project already uses as its own
   H1a/H1b fairness measure (`notes/2026-08-04-full-instrument-assembly.md`
   item 6, `notes/2026-09-03-consensus-campbell-1999-fairness-scale-
   resolved.md`). A brand-new (2025 online-first, Oct 2026 print) JCR paper
   from the same author, extending her own fairness construct into a full
   "moral harm" conceptual model with **inferred firm motives** as an
   explicit moderator/mechanism, is about as close to this project's own
   theoretical lineage as a new citation gets.
2. **Inferred firm motive as a driver of fairness judgment** is directly
   structurally relevant to this project's own H1-H2 chain, where a firm's
   *attribution* of a price increase (to an existing tariff vs. its own
   decision) is exactly a firm-motive-inference manipulation. This paper
   gives a much more developed theoretical vocabulary ("moral harm,"
   "inferred firm self-defense motives") for what this project's Theory
   draft currently frames more narrowly around fairness/opportunism.
3. **Political orientation as a moderator of harm→fairness** is a second,
   independent piece of very recent top-tier literature (alongside Davidson
   & Schaefer 2025/Schaefer & Davidson 2026, logged 09-27) suggesting
   political identity belongs somewhere in this project's Discussion/
   Limitations, even though — as already flagged 09-27 — it is not
   currently a moderator in any of this project's own H1-H5 hypotheses.
   **Not proposing a design change; Study 2's instrument is already
   built/spec'd, and this is Britton's call.**

**Recommendation:** this is worth Britton pulling the full text directly via
his own JCR/Oxford Academic institutional access before the final citation
pass — of everything found across the last several nights' literature scans,
this is the single most theoretically load-bearing new citation candidate,
more so than the Dai et al. (2026) lead or the Davidson & Schaefer papers,
because it comes from the same scholarly lineage the project's own
instrument already depends on.

### 5b. Fami Tafreshi (2024, SSRN working paper) — real, existence-verified, but low-confidence/unverified-content, likely not peer-reviewed

**Fami Tafreshi, Parham (2024). "Understanding the Influence of Price
Increase Justifications and Price Increase Size on Perceived Price Fairness
and Customers' Intentions: The Moderating Role of Expected Future Prices and
Product Involvement." SSRN Working Paper. DOI: 10.2139/ssrn.4940659.**

Existence/title/author/DOI confirmed via Crossref, OpenAlex, and Semantic
Scholar (all three agree). Author appears (per a ResearchGate profile link
surfaced in search, not independently verified here) to be affiliated with
Kaunas University of Technology — **this looks like a single-author working
paper or dissertation chapter, not a peer-reviewed published article**; no
journal/container-title is given anywhere. **Content could not be verified
from any source tonight**: SSRN's own abstract page returned the same
Cloudflare bot-challenge (`HTTP 403`, `cf-mitigated: challenge`) that blocks
Davidson & Schaefer's SSRN page; Crossref, OpenAlex, and Semantic Scholar all
return no abstract text. A WebSearch AI-summary described the paper as
examining "firm control versus external factors" as justification types for
a price increase, and product involvement as a moderator — **this is
exactly the shape of this project's own manipulation (firm attributes a
price increase to an external tariff vs. its own decision)**, which is why
it's worth logging at all, but **per this project's standing rule, none of
that summary is being treated as confirmed** — it could be accurate, but
there is no primary-source confirmation of actual content, only of the
paper's real existence and bibliographic details, and its unclear
peer-review status makes it lower-priority than 5a above regardless. Not
recommending Britton spend real time on this one specifically unless 5a and
the existing leads are exhausted — flagging only for completeness.

## What's stable vs. what changed, summary

**Changed since 09-27:**
- V.O.S. Selections' response-brief countdown moved from 8 to 7 days out
  (expected, not a docket event); still no filing, no oral-argument date.
- One new, high-priority literature find: Campbell, Pomerance & Percival
  Carter (2025/2026, *JCR*), "Painful Prices: The Moral Harm Model of Price
  Fairness" — verified abstract in hand (full text paywalled/Cloudflare-
  blocked here), directly relevant to this project's own fairness construct
  and attribution-based theory (see §5a).
- One secondary, lower-confidence literature lead: Fami Tafreshi (2024,
  SSRN working paper) on price-increase justification framing — real,
  existence-verified, content unverified, likely non-peer-reviewed (see
  §5b).
- Dai, Xiang, Gu & Zhou (2026, *JRCS*) independently re-confirmed via a
  fifth source (Semantic Scholar) and a new access attempt (`r.jina.ai`
  proxy) — same result as 09-27, still fully paywalled/unreachable, no
  change in status.

**Fully stable / unchanged since 09-27:**
- All four litigation dockets — same entry counts, same verbatim text on
  the latest entries, no rulings, no terminations.
- The JCM deadline discrepancy — not re-attempted tonight, per task
  instruction; genuinely still unresolved, still needs Britton directly.
- Davidson & Schaefer's SSRN paper — still unreachable, not re-attempted
  tonight (per standing instruction not to keep spending time on it).

**Still genuinely open:**
- **The JCM special-issue deadline** — flagged for THREE consecutive nights
  now (09-26, 09-27, 09-28). Per this task's explicit instruction, no
  further automated attempts should be made — this needs Britton's own
  direct check (a browser visit to the Emerald CFP page, or an email to the
  guest editors named in `SUBMISSION_TRACKER.md`) before either candidate
  date is treated as settled. Not attempting a fourth automated pass in
  future nightly runs either, absent new instruction.
- The Dai et al. (2026, *JRCS*) paper's actual abstract/findings — confirmed
  again tonight to need Britton's own ScienceDirect/library access; no
  further automated route exists that hasn't already been tried.
- The new Campbell, Pomerance & Percival Carter (2025/2026, *JCR*) paper's
  full text — needs Britton's own JCR/Oxford Academic access; abstract
  already in hand and logged above, so this is a "go read the full paper"
  task, not a "find out if it exists" task.
- CITI/HSIRB turnaround, Jason's blind-coding worksheet, Study 2/3 data
  collection — not touched tonight, out of this session's task scope.

## For Britton

1. **All four litigation dockets are fully stable tonight** — nothing new
   since 09-27. V.O.S. Selections' Federal Circuit response brief is now 7
   days out (10/05/2026); still no filing or oral-argument date on that
   docket — worth a same-day check around 10/05.
2. **Strongest new literature find in several nights: Campbell, Pomerance &
   Percival Carter (2025/2026, *Journal of Consumer Research*), "Painful
   Prices: The Moral Harm Model of Price Fairness"** (DOI:
   10.1093/jcr/ucaf045, Vol. 53(3), Oct 2026, pp. 444-466). Same Margaret C.
   Campbell whose 1999 fairness scale this project already uses. Proposes a
   "moral harm" model of price fairness with **inferred firm motives** and
   **political orientation** as explicit moderators — structurally very
   close to this project's own attribution-based theory. Full text is
   paywalled/Cloudflare-blocked from this container (despite being listed
   as nominally OA in some indexes) — worth pulling directly via your JCR
   access before the final citation pass. Verified abstract quoted in full
   above.
3. **JCM deadline: still unresolved after three nights of attempts — not
   re-attempted tonight per instruction.** This genuinely needs your own
   direct check (Emerald CFP page in an ordinary browser, or the guest
   editors' emails already listed in `SUBMISSION_TRACKER.md`) rather than a
   fourth automated pass. Nightly runs will stop re-trying this on their own
   going forward unless you ask for another attempt via a different method.
4. **Dai et al. (2026, *JRCS*) — still just a verified citation, no
   accessible content**, re-confirmed via a fifth independent source
   tonight. Don't cite its content until someone with ScienceDirect access
   reads it directly.
5. One low-confidence secondary lead logged for completeness: Fami Tafreshi
   (2024, SSRN working paper) on price-increase-justification framing —
   real but likely non-peer-reviewed, content unverified, not worth your
   time unless everything else is exhausted.
