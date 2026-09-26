# 2026-09-26 — Farm-bill deadline (4 days out), a real 2020s-era import "natural experiment" for Claim #7, Brester & Marsh retry, new Tyson litigation detail, Schaefer/idea-28 recheck

Twelfth research session. Orientation: read `CLAUDE.md`, `PROJECT_STATUS.md` in full (through the
2026-09-24 pass), `NOTES/Claim_Fact_Check.md`, and the 2026-09-24 dated note before starting. Today is
2026-09-26 — the farm bill's Sept. 30, 2026 extension deadline (distinct from the Dec. 11, 2026
government-funding deadline) is 4 days away. Scope tonight, per the brief: (1) farm-bill floor-vote
timing given the imminent deadline; (2) a fresh, targeted search for 2020s-era Australia/Brazil-mix
evidence on Claim #7 ("corporations gouge consumers" via imports); (3) another Brester & Marsh (1999)
PDF retry, with the specific failure mode logged if still blocked; (4) advance the Schaefer/poultry and
idea-28 threads; (5) primary-source verification of other open claims. Method: `WebSearch` + `WebFetch`
for most sources; `curl` with a browser User-Agent for sources WebFetch couldn't reach; `pdftotext -layout`
(via freshly-reinstalled `poppler-utils` — missing again from this session's container, same recurring
gap noted in several prior sessions) for two PDFs. No design decisions made. No external contact, no
money spent, nothing submitted anywhere.

## 1. Farm-bill floor-vote timing — a real correction and a genuinely unresolved discrepancy

**A genuinely new, well-corroborated clarification of the Aug. 6, 2026 markup**, previously described in
this project's notes as a single event ("committee markup Aug. 6, 2026" passing the labeling amendment).
Reading a fresh Sept. 15, 2026 article (`wwbl.com`/Hoosier Ag Today, fetched directly via `curl` after a
WebFetch summary of it initially looked contradictory) surfaced a claim that "the Farm Bill failed to
advance during the committee's Aug. 6 markup" on a "10-11 vote amid a partisan dispute over changes to
... SNAP." This looked at first like it might conflict with the already-verified "S.421 labeling
amendment passed 17-6 on Aug. 6" finding — it does not. Cross-checked directly against five independent,
contemporaneous Aug. 6-7, 2026 sources (DTN, Iowa Capital Dispatch, American Ag Network, Farm Progress,
Ag Bull Trading — read via `WebSearch` synthesis of multiple hits, consistent across all of them): the
Aug. 6 markup session held **multiple separate votes**. The Thune MCOOL/labeling amendment (S.421) passed
17-6 within that session (already independently verified in this project). But the **final vote to
advance the whole farm bill package out of committee that same day failed, 10-11**, on a straight party
line, because Sens. McConnell and Tuberville (R) were absent/left before the final vote — leaving
Democrats able to block final passage even though most individual amendment votes ran 12-11 GOP. Chairman
Boozman **recessed (not adjourned) the committee** rather than treat this as a dead bill, explicitly to
preserve the option of a later vote once the absent senators returned. That is exactly what then happened:
McConnell's return let the committee pass the full bill out of committee 12-11 on Sept. 16 — the event
this project already had recorded. **Net effect: this resolves what looked like tension between two facts
already in this project's notes (a 17-6 passing vote and a "still stalled as of mid-Sept." framing) into a
single coherent timeline, and adds a genuinely new fact (the Aug. 6 overall-bill vote failed 10-11 and the
committee was recessed, not concluded) that should be in the manuscript's background section if this
farm-bill fight is ever narrated in detail.** No Claim verdict changes; this only sharpens the mechanism.

**The Sept. 30 deadline itself**: multiple independent sources (Iowa Capital Dispatch/AP-syndicated
wire coverage, Farm Progress, the wwbl.com/Hoosier Ag Today piece) confirm the current farm-bill
extension (the third since the 2018 Farm Bill expired) lapses Sept. 30, 2026, and that a new
five-year bill cannot possibly be enacted in time — it still needs a full Senate floor vote (60-vote
threshold), House-Senate reconciliation between two substantively different bills (House passed
H.R. 7567/"Farm, Food, and National Security Act of 2026," 224-200, April 30; Senate committee passed
the differently-named "Agricultural Act of 2026," 12-11, Sept. 16), and a presidential signature — none
of which has started. Consistent with the practical (not existential) consequence already noted in this
project's 2026-09-24 pass: most core programs (crop insurance, SNAP, 2031-authorized commodity
reference prices) do **not** lapse; what actually stops are smaller programs (Specialty Crop Block
Grants, several research/outreach lines), and the real long-run risk is the "dairy cliff" (permanent
1930s-era law reverting Jan. 1, 2027 for dairy, later for wheat/corn) if no bill or further extension
passes by year-end.

**A genuine, unresolved discrepancy about the recess calendar, flagged rather than picked**: one source
found tonight (`themoneyoverview.com`, a personal-finance content site — not a specialist ag- or
Capitol-Hill outlet, and its own "About" page and reader-offer boilerplate read like a content-marketing
operation, not a newsroom) states, citing "a Senate aide quoted by AgWeb," that "both chambers of Congress
would be out of Washington for the next six weeks, a recess window that begins before the September 30
deadline and runs well past it" — i.e., no floor action is even physically possible before the deadline.
**This could not be independently verified tonight.** AgWeb itself (`agweb.com`) is bot-blocked by a
PerimeterX CAPTCHA challenge page (confirmed via direct `curl`, HTTP 403, page title "Access to this page
has been denied," `px-captcha` in the page metadata) to both `curl` and WebFetch, so the underlying aide
quote could not be checked at its own nearer-to-primary source. Separately, an AP-wire article (via
newschannel9.com, read directly) covering the same Sept. 16 committee vote does **not** mention any
recess timing at all. And a `WebSearch` synthesis of multiple hits on the Senate's own published 2026
calendar (Roll Call, Bloomberg Government reporting on it) states the Senate is "scheduled to remain in
session until October 2" before the pre-midterm recess — i.e., **through**, not before, the Sept. 30
deadline — which is hard to reconcile with "recess begins before Sept. 30." Neither the Roll Call nor
Bloomberg Government articles gave the exact calendar dates in their own fetchable text (both were
read directly via WebFetch and neither stated a specific October start date for the recess), and two
further attempts to reach a page giving the Senate's exact day-by-day October calendar
(`factually.co`, `thewellnews.com`) were both blocked by a Cloudflare "Enable JavaScript and cookies to
continue" challenge page. **Stated plainly: this project cannot currently confirm the exact date the
Senate's pre-midterm recess begins, and the two claims in circulation ("in session through Oct. 2" vs.
"recess begins before Sept. 30") are in tension. Do not use either specific framing in the manuscript
without further verification** — the safest defensible statement remains what the 2026-09-24 note already
established: a real, narrow pre-midterm floor-vote window exists in principle, Grassley/Republicans are
publicly pushing to use it, Democratic leadership is not committing to any date, and no vote has actually
been scheduled either way.

**New, not previously tracked — an administrative-path development worth flagging to Britton**: USDA
Secretary Brooke Rollins, speaking at the Farm Progress Show on Sept. 1, 2026 (per Ag Bull Trading,
read directly), told Fox Business she would raise mandatory country-of-origin labeling with President
Trump "later this week" and said, when asked directly, "100%. All Americans should know where their food
comes from." She did not announce a Trump decision or an imminent executive order — this is Rollins
signaling personal/administration sympathy and a possible **administrative** (non-legislative) path
alongside the stalled Senate bill, not a new fact about the bill itself. Claim #11's verdict is unchanged
(nothing enacted, legislative or administrative), but this is a real, dated data point about the
political momentum around COOL that could matter for how Study 1 frames NCBA/R-CALF/USDA discourse.

## 2. Claim #7 (2020s Australia/Brazil-era import effect) — real advance: a live natural experiment, not an econometric study

The brief asked for a fresh, targeted search for current-era evidence and said a genuine negative result
(nothing found) would be a valid outcome, not a failure. **Tonight's search found something better than
"nothing" but still short of a peer-reviewed econometric estimate: a real, dated, ongoing 2025-2026
policy natural experiment, directly on point, with actual observational data already being tracked by
name economists — not yet a study, but real primary-source material that should go in the manuscript's
background/motivation section regardless of what Study 1-3 end up testing.**

**The policy itself, read directly from primary sources (not secondary paraphrase):**
- **Proclamation 11010** ("Ensuring Affordable Beef for the American Consumer"), signed Feb. 6, 2026:
  increased the in-quota tariff-rate-quota (TRQ) amount for lean beef trimmings from **Argentina** by
  80,000 metric tons for calendar year 2026.
- **Proclamation 11059** ("Further Ensuring Affordable Beef for the American Consumer"), signed Aug. 26,
  2026, published in the Federal Register Aug. 31, 2026 (Vol. 91, No. 167, pp. 55989-55994) — **read in
  full directly** (govinfo.gov PDF, `curl` succeeded at HTTP 200/6 pages where the Federal Register's own
  HTML/XML endpoints now return an anti-bot CAPTCHA page, a change from earlier sessions when the
  XML/API endpoint reliably bypassed the interstitial — worth knowing this specific bypass channel may
  no longer be reliable). This proclamation invokes section 404(b) of the Uruguay Round Agreements Act
  (19 U.S.C. 3601) to temporarily increase the beef TRQ's in-quota amount by an **additional 300,000
  metric tons of lean beef trimmings**, administered first-come-first-served, for 90 days beginning
  Sept. 1, 2026. The proclamation's own stated rationale (its own text, quoted): the U.S. cattle herd "has
  fallen to its lowest level in 75 years"; USDA forecasts 2026 beef output to fall ~4% from 2025; and the
  goal is that "the importation of ground beef ... will be sold at a discounted price compared to current
  sale prices" — with an explicit self-imposed condition that the President "may end the action ... in
  order to ... prevent a windfall to foreign producers" if that discount does not materialize. **This is
  the U.S. government itself treating "will more imports actually lower retail beef prices?" as an open,
  falsifiable, time-boxed question** — a remarkably direct real-world version of this project's own
  Claim #6/#7.
- These proclamations were **not previously tracked anywhere in this project** — a genuinely new
  addition to the import/pricing section, not a re-verification of an existing claim.

**Early tracking data on whether it worked (American Farm Bureau Federation, read directly, both
pieces):**
- AFBF economists Bernt Nelson and Faith Parum tracked **41 supermarkets across 22 states** for the
  first three weeks of the September 300,000-mt action (Sept. 2-23, 2026): average ground-beef price
  fell from $7.29/lb to $7.13/lb — **a 2% decline**, far short of the 25% discount the proclamation
  itself was designed to produce. At 30 of the 41 stores, the price literally did not move. Only 3 of 41
  stores hit anything close to the targeted discount. AFBF's own interpretation: "tight cattle supplies
  and strong consumer demand continue to support higher consumer beef prices" and the policy should be
  "rolled back."
- The same reporting states **cattle prices (the producer side) fell $300-400 per head over roughly the
  same two-month window** — R-CALF USA's Bill Bullard and others attribute this to the policy itself
  (the *announcement* of expanded import supply depressing futures/cash cattle prices, independent of
  actual physical import flow) rather than to realized import volumes. A separate, earlier (Oct. 29,
  2025) Nelson piece on the Argentina-specific tariff-quota expansion makes the same point even more
  starkly: he wrote that the announcement alone "caused future prices for feeder cattle to fall by 7%"
  before any beef had actually moved, while concluding the expanded quota itself "will not have a
  measurable impact on prices consumers pay for beef."
- **Source-type caveat, stated explicitly per this project's standing practice of distinguishing source
  types precisely**: the American Farm Bureau Federation is a farmer/rancher interest group, not a
  neutral academic body — but the specific numbers here (a documented retail price survey across a named
  number of stores/states, with an exact before/after methodology) are closer to raw observational data
  than to advocacy framing, and multiple named economists put their names on the methodology. Treat the
  *data* (41-store price survey, $300-400/head cattle-price move) as real and citable; treat AFBF's own
  *policy recommendation* ("roll this back") as advocacy, not as this project's conclusion.

**Net effect on Claim #7**: the 2026-09-24 note's "no 2020s-era equivalent econometric estimate was
found" finding **still holds** — nothing found tonight rises to the level of a peer-reviewed or even a
government econometric model of the current Australia/Brazil/Argentina-era import effect. But "genuinely
unresolved, no evidence at all" is no longer quite accurate either: there is now real, dated, primary/
near-primary observational evidence from an actual government policy experiment explicitly designed to
test this exact question, with early results (2% retail decline vs. a 25% target; a sharper move in
cattle/feeder prices than in retail prices) that are directly consistent with this project's already-
established GAO-02-246 finding that import effects, if any, are theorized to hit cattle prices before they
reach (or fully reach) retail prices — i.e., new evidence that fits the existing theoretical framework
rather than contradicting it. **Recommend upgrading the current-era portion of Claim #7 from "no evidence
exists" to "no peer-reviewed econometric estimate exists yet, but real, current, primary-sourced
observational evidence from an active 2025-2026 policy natural experiment is now available and points in
the same direction (weak/no retail pass-through so far) as the existing theoretical framework" — a more
precise, more useful statement, not a verdict upgrade to "supported."** See
`SOURCE_VERIFICATION/Evidence_Table_Imports.md` for two new rows (the proclamations) and
`NOTES/Claim_Fact_Check.md` for the Claim #7 row update.

## 3. Brester & Marsh (1999) — still blocked, specific failure mode confirmed and one new channel closed off

Retried per the brief's instruction to log the specific failure mode rather than just re-stating
"blocked." Result: **the exact same failure mode as 2026-09-24, confirmed again tonight, plus two new
channels tried and closed off:**

- `ageconsearch.umn.edu` (both the specific PDF URL and, tonight, the bare record page
  `/record/29162` itself) returns **HTTP 202 Accepted with an empty response body** to `curl` with a
  full browser User-Agent — not a 403, not a paywall redirect, not a DNS failure. HTTP 202 normally means
  "request accepted, processing asynchronously" — this is consistent with an anti-bot challenge/queue
  page that never resolves for an automated client, rather than an ordinary block. Tried twice more
  tonight (once against the record page, once against the previously-tried PDF path) with the same
  result both times.
- `ageconsearch.umn.edu`'s own API endpoint (`/api/records/29162`) returned `{"error": "Unresolvable
  route"}` (HTTP 404) — confirms this specific record ID isn't reachable through that channel either,
  not just rate-limited.
- RePEc's own record page (`ideas.repec.org/p/ags/motpip/29162.html`, fetched fresh, HTTP 200) contains
  only an in-page anchor (`#download`) pointing back at the same broken AgEconSearch host — **no
  alternate mirror or direct file link exists on RePEc's own page**, closing off one channel that seemed
  promising.
- CORE.ac.uk's search endpoint returned an HTTP 308 permanent-redirect loop that did not resolve to
  actual results within this session's tooling — a new, different failure mode from AgEconSearch's 202,
  not yet root-caused.
- Semantic Scholar's public API returned HTTP 429 ("Too Many Requests... apply for a key for higher rate
  limits") tonight — a rate limit, not a permanent block; worth one more try in a future session,
  ideally with a longer gap between calls, since this is the one channel tonight that failed for a
  reason that might resolve on its own.
- ResearchGate has a page for this exact paper (confirmed via search snippet) but was not re-tried
  tonight given this project's prior sessions' consistent experience of ResearchGate 403-blocking
  automated fetches for paywalled/gated items generally.

**Recommendation, restated plainly**: this is now the third session (2026-09-24, tonight) failing on
this specific paper via automated tooling, with a consistent and unusual failure signature
(HTTP 202/empty from the one host that actually hosts the file, not an ordinary paywall 403). This does
not look like something further automated retries will fix. The existing citation (RePEc's own
abstract restatement of the paper's headline ~4.4%/$0.35-per-cwt figure) remains the best available
sourcing and is already correctly flagged in the Evidence Table as secondary, not a direct primary read.
If this exact figure needs to go into the manuscript with primary sourcing, the most promising remaining
path is Britton's own institutional access (the same solution that resolved the Schaefer et al. 2024
blockage) — not further automated retry time.

## 4. Schaefer/poultry-concentration thread and idea 28 — rechecked, nothing new, no further automated action needed

Per the brief's instruction to advance these threads: read the existing chain (`PROJECT_STATUS.md` Open
Decision #6, the 2026-09-24 note's own review of it) and ran fresh searches rather than assuming nothing
has changed.

- **Schaefer/poultry-concentration (Open Decision #6)**: no new search attempted tonight beyond
  confirming, via the 2026-09-24 note's own already-thorough review, that this remains as resolved as it
  can get without Britton re-checking the paper's own footnotes. Consistent with that note's own
  recommendation ("no further automated-retry time"), tonight's session did not re-attempt the same
  exhausted channels (Springer, Unpaywall `is_oa: false`, Semantic Scholar, RePEc, the USDA mirror) a
  fourth time. **Genuinely nothing left to do here without Britton's input.**
- **Idea 28 / DOJ retailer probe**: re-searched fresh. No indictments, no new DOJ.gov document. New
  detail, not previously in this project's notes: Acting Attorney General Todd Blanche stated
  (per multiple trade/business outlets — Yahoo Finance, Fortune, Fox Business, Forbes, Newsweek, all
  broadly consistent) that DOJ has "reviewed more than 3 million documents and conducted interviews" as
  part of the broader beef-pricing investigation (which now spans the original "Big Four" processor
  probe from May 2026 plus the eight-retailer expansion from September). Also newly noted: average
  ground-beef retail price cited in this coverage as $6.89/lb in July 2026, +10% YoY — a useful,
  independently-sourced retail-price data point that happens to sit right in between the AFBF 41-store
  average ($7.29→$7.13/lb, Sept. 2026) — consistent, not contradictory, given the different measurement
  windows. This is secondary press coverage of DOJ statements, not a DOJ document read directly —
  flagged as such, matching this project's existing standard for this specific investigation thread.
- **Genuinely new, substantial litigation detail found directly in Tyson's own SEC 10-Q** (see Section 5
  below) that materially expands what this project has tracked for both the beef and pork antitrust
  litigation threads — a bigger and more useful find than a routine "no change" recheck would have been.

## 5. New primary-source litigation detail — Tyson's own 10-Q reveals two previously-untracked settlement classes (beef and pork)

Per the brief's instruction to do primary-source verification of open claims, and because a Tyson
settlement-status search surfaced Tyson's own most recent 10-Q (period ended June 27, 2026, filed via SEC
EDGAR), read in full directly (`curl` with an SEC-compliant descriptive User-Agent — SEC EDGAR requires
one and blocks requests without it, a mechanical detail worth remembering for future sessions; the
generic browser User-Agent that works for most other sites returned a bare HTTP 403 here). This filing is
squarely primary (a company's own audited-adjacent quarterly disclosure to the SEC) and reveals **two
settlement classes not previously tracked anywhere in this project's notes**, plus useful corroboration
of figures already tracked:

**Beef Antitrust Civil Litigation (Tyson's own disclosures)** — three distinct settled classes, not one:
1. Consumer Indirect Purchaser Plaintiff class: **$55 million**, agreement Sept. 29, 2025; preliminary
   approval Dec. 10, 2025; paid Nov. 26, 2025.
2. Direct Purchaser Plaintiff class: **$80 million plus $2.5 million in administrative expenses**
   (= $82.5 million total), agreement in principle Dec. 12, 2025; preliminary approval **May 14, 2026**;
   paid Jan. 7, 2026. **This is the exact settlement this project has already been tracking as "the Tyson
   $82.5M DPP settlement" (Nov. 12, 2026 Fairness Hearing)** — tonight's filing read confirms the $82.5M
   figure's own component breakdown ($80M settlement + $2.5M administrative expenses) for the first time
   and independently corroborates the May 14, 2026 preliminary-approval date already in this project's
   notes, straight from Tyson's own filing rather than only from court-docket/news sources.
3. **New: Commercial and Institutional Indirect Plaintiff (CIIPP) class — a third, previously-untracked
   beef settlement class**: $47 million, agreement in principle Dec. 12, 2025 (same day as the DPP
   settlement above); preliminary approval May 6, 2026; paid June 2, 2026. This class represents
   businesses/institutions (restaurants, food-service operators, etc.) that bought beef indirectly — a
   distinct legal category from both the direct-purchaser and the consumer-indirect-purchaser classes
   already tracked. Add to Claim #15's settlement inventory.
4. The July 16, 2026 class-certification ruling already characterized in this project (via the 2026-09-07
   note) as a "mixed ruling" is independently confirmed by Tyson's own filing in almost identical language:
   "the Court issued an order granting certain motions for class certification and denying others."
5. **Also newly noted, not previously tracked**: two Canadian putative class actions against Tyson
   Fresh Meats and other beef-packer defendants — *Bui v. Cargill, Incorporated et al.* (British Columbia
   Supreme Court, filed Feb. 18, 2022) and *De Bellefeuille v. Cargill, Incorporated et al.* (Quebec
   Superior Court, filed March 24, 2022) — alleging the same 2015-onward beef price-fixing conspiracy
   under Canadian competition/civil law. Both remain open per Tyson's own filing (no settlement disclosed
   for either). Purely informational for now — a possible cross-border comparison point if this project's
   scope ever extends there, not otherwise load-bearing for the U.S.-focused claims.

**Pork Antitrust Civil Litigation (Tyson's own disclosures)** — confirms and extends what's already
tracked:
1. Direct Purchaser class: $50 million, agreement April 11, 2025; preliminary approval April 28, 2025
   (already broadly consistent with this project's existing pork-DPP tracking, though this project's
   existing notes track the *Agri Stats* pork-DPP settlement specifically, which is behavioral/no-cash —
   this $50M Tyson-specific DPP settlement is a distinct defendant's own cash settlement within the same
   broader MDL, not a duplicate or contradiction).
2. Consumer Indirect Purchaser class: $85 million, agreement Sept. 25, 2025; preliminary approval Nov. 7,
   2025 — **this is the Tyson component of the already-tracked $117.065M five-defendant Consumer IPP
   settlement** (Tyson $85M + Clemens $13.5M + Seaboard $10M + Hormel $4.465M + Triumph $4.1M). Tyson's
   own filing independently corroborates its $85M share and both dates.
3. **New: Commercial and Institutional Indirect Plaintiff (CIIPP) class — a third, previously-untracked
   pork settlement class, parallel to the beef CIIPP class above**: $48 million, agreement executed
   Dec. 31, 2025; preliminary approval April 24, 2026. Add to Claim #15.
4. Also newly noted: two immaterial state-AG settlements — Alaska ("immaterial amount," settled Oct. 18,
   2024, court-approved Jan. 7, 2025) and New Mexico ("immaterial amount," agreement May 9, 2025,
   court-approved Aug. 11, 2025) — both distinct state-law claims (also naming Agri Stats and other pork
   processors), separate from the federal MDL classes above.
5. Legal contingency accrual for pork litigation: $83 million as of June 27, 2026, down from $268 million
   a year earlier — Tyson's own filing states it paid out $245 million against this matter in the first
   nine months of fiscal 2026, consistent with the DPP/CIPP/CIIPP settlements above actually being paid.
   Beef litigation's own contingency accrual: $215 million (June 27, 2026), down from $318 million,
   with $193 million paid out over the same nine months.

**Why this matters for the manuscript**: Claim #15 ("food monopolies" framing) already documents an
extensive, multi-commodity price-fixing settlement landscape: this adds two entire settlement classes
(commercial/institutional indirect purchasers, for both beef and pork) that existed and were being
actively paid out throughout 2025-2026 without this project previously knowing about them — a reminder
that the settlement landscape here is more extensive than even this project's own fairly thorough prior
tracking had captured, purely because this specific filing hadn't been read directly before. **Recommend
a future session cross-check whether other defendants (JBS, Cargill, National Beef, Smithfield) have
parallel CIIPP-class settlements not yet tracked, using the same "read the defendant's own 10-Q/10-K
directly" method that worked here.**

## What did NOT change tonight

- No Study 1/2/3 design decisions made or needed.
- Claim #11's core verdict (Unsupported, as commonly believed — mandatory COOL for beef repealed 2015,
  nothing enacted yet) is unchanged.
- Claim #7's split-verdict structure (historical NAFTA-era Canada case: real small-magnitude estimates;
  current 2020s Australia/Brazil/Argentina-era case: no peer-reviewed estimate) is unchanged in its
  bottom line — tonight adds real current-era observational evidence, not a formal estimate, so the
  verdict language is sharpened, not flipped.
- Open Decision #6 (Schaefer): unchanged, nothing further for automated tooling to do.

## Genuinely still open, stated plainly

- The exact date the Senate's pre-midterm recess begins is unresolved between conflicting secondary
  sources (see Section 1) — needs either better tooling against agweb.com's CAPTCHA/PerimeterX challenge
  or thewellnews.com/factually.co's Cloudflare challenge, or Britton checking the Senate's own printed
  2026 calendar directly.
- Brester & Marsh (1999)'s own PDF remains unobtained, now confirmed blocked across two full sessions
  with the same specific HTTP-202-empty signature from the one host that hosts it — recommend no further
  automated-retry time barring a genuinely new channel, per Section 3.
- Whether other beef/pork defendants have their own untracked CIIPP-class (or similar) settlements is now
  an open, concrete follow-up (Section 5) rather than an assumption that this project's litigation
  tracking is complete.
- Farm-bill floor vote: still no date set either way, as of tonight — genuinely unresolved, not close to
  resolving in the next 4 days before the Sept. 30 deadline itself lapses.

## For Britton

Four things worth knowing: (1) the farm bill's Sept. 30 deadline will almost certainly lapse without a
new law in place — this affects some smaller programs, not the core commodity/crop-insurance/SNAP
programs, and a further extension remains the likely near-term outcome, though nobody has said so
explicitly yet; (2) there is now a real, live, dated 2025-2026 policy "natural experiment" directly
testing this project's own central question (do more beef imports actually lower consumer prices?) —
two Trump proclamations expanding the beef tariff-rate quota, with early tracking data (a 2% retail
decline against a targeted 25% discount) suggesting the answer, so far, is "not much" — worth citing in
the manuscript's motivation section regardless of which study design gets chosen; (3) reading Tyson's own
SEC 10-Q directly surfaced two entire settlement classes (commercial/institutional indirect purchasers,
beef and pork) this project didn't know existed — the litigation landscape here is bigger than previously
tracked, and the same read-the-primary-filing method is worth repeating for the other defendants; (4)
Brester & Marsh (1999) is very likely a dead end for automated tooling specifically — if that ~4.4%
Canadian-import figure ever needs a primary citation, it will probably need your own institutional access,
the same way Schaefer et al. (2024) did.

No money spent. No one contacted. Nothing submitted anywhere.
