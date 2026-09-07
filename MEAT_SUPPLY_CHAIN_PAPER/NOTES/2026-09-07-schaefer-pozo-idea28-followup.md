# 2026-09-07 — Schaefer/Pozo retry pass, idea 28 (beef price-fixing saga) primary-source verification, Tyson FY2026 update

Third research session on this project. Follow-up to the 2026-09-05
primary-source retry pass. Three lines of work, per that night's status
doc and the scouting log's idea 28: (1) another legitimate-open-access
retry on the two sources still confirmed blocked as of 2026-09-05 —
Schaefer et al. (2024, *Review of Industrial Organization*) and Pozo,
Bachmeier & Schroeder (2021, *Journal of Commodity Markets*); (2)
primary-source verification of scouting-log idea 28 (the 2025-26 beef
price-fixing saga) as potential Study 1/2 material — verification only,
not an adoption decision; (3) a quick check of Tyson/JBS SEC data for
anything newer than FY2023. No git commands were run this pass (per
standing instructions for this session) — the repo has uncommitted changes
as of this note.

## 1. Pozo, Bachmeier & Schroeder (2021) — RESOLVED via the authors' own institutional-repository working paper

**Status change: from "AI-tool-mediated read, treat with some caution" to
directly, independently verified.**

The published version (`doi.org/10.1016/j.jcomm.2020.100127`) remains
paywalled at ScienceDirect, and WebFetch 403'd on it directly. A search for
alternate open-access channels turned up the authors' own pre-publication
working paper hosted on **Kansas State University's KREx institutional
repository** — a legitimate, standard open-access channel (an author's
home institution's repository), not previously tried:

`https://krex.k-state.edu/bitstream/handle/2097/39780/revised_bachmeier_pozo_schroeder.pdf`

WebFetch 403'd on this URL too, but `curl` with a standard browser
User-Agent header succeeded (HTTP 200, 44-page PDF). `poppler-utils` was
unavailable this session (a concurrent `apt-get` process elsewhere in the
container held the package-manager lock the whole session, so `pdftotext`
was never installed), so text was extracted locally with Python's `pypdf`
library instead — worked fine for this file. Full 44 pages read.

**Findings, confirming the project's existing characterization almost
exactly:**
- Compares beef price-transmission asymmetry using BLS-collected retail
  prices vs. quantity-weighted scanner retail prices, at both monthly and
  weekly frequency, using a threshold VECM with a novel nonlinear-impulse-
  response-based symmetry test (an improvement on older slope-based tests).
- **Scanner-data models fail to reject the null of symmetry** at any
  frequency tested (monthly or weekly) — "farm, wholesale, and retail beef
  prices respond symmetrically to price changes at each market level."
- **BLS-data models DO show statistically significant asymmetry**: retail
  prices respond asymmetrically to farm-price shocks, wholesale-price
  shocks, AND their own past shocks.
- Mechanism, in the paper's own words: BLS retail prices "do not accurately
  reflect volume-weighted sales of beef products. Instead, BLS price data
  simply reflect posted shelf prices on beef products with limited
  adjustment for actual volume of beef that is sold at each price level,
  particularly at discounted prices during retail specials," causing "a
  significant upward bias."
- Counterfactual analysis (imposing symmetric responses and re-simulating):
  if any asymmetry the test can't detect exists, it appears to have
  **benefited consumers** at the retail level (simulated symmetric retail
  price is higher than the actual historical price). At the farm level the
  counterfactual is genuinely mixed/ambiguous depending on which shock is
  isolated — the paper's own preferred interpretation is that the
  relationship is symmetric, consistent with their formal hypothesis tests.
- The paper directly engages the older Goodwin & Holt (1999) asymmetry
  finding by re-running its own method on GH's original 1981-1998 data and
  replicating GH's asymmetric result — concluding the difference from GH is
  driven by newer/different (scanner) data, not a methodology artifact.

This is now a directly-read primary source rather than a Consensus.app
synthesis. Updated: `SOURCE_VERIFICATION/Evidence_Table.md` (Pozo row
rewritten), `NOTES/Claim_Fact_Check.md` (Claim #5 "still open" list item
resolved).

## 2. Schaefer et al. (2024) — still blocked, but the poultry-concentration discrepancy investigation moved forward materially

**Status: NOT resolved. Still do not use "78%" for poultry anywhere in
this project without the caveat below.**

### What was tried this pass (five more channels, all exhausted)

1. **USDA-hosted preprint mirror** (`usda.gov/.../schaefer-et-al-2023.pdf`)
   — this worked via `curl`+UA on 2026-09-05 for other sources, but this
   specific file now returns an Akamai "Access Denied" page (HTTP 403) to
   both WebFetch and `curl` with multiple browser/Googlebot User-Agents.
   Whatever allowed this particular USDA file through before is no longer
   working — treat USDA PDF mirrors as inconsistently accessible over time,
   not permanently open once confirmed once.
2. **Wayback Machine / archive.org** — found a working archived snapshot of
   the same USDA PDF via the Wayback Machine's own `/wayback/available`
   API. However, `web.archive.org` itself is **blocked by this cloud
   environment's own egress policy** ("Blocked by egress policy" from
   `curl`; WebFetch returns "unable to fetch from web.archive.org"). This
   is an environment limitation, not a source-access problem — worth
   knowing for any future session in this repo that finds a Wayback lead.
3. **Springer (the actual journal page)** — `link.springer.com` 303-
   redirects to `idp.springer.com/authorize`, an institutional-login wall.
   No abstract or first-page preview text was retrievable without
   authenticating.
4. **ResearchGate** ("Request PDF" page) — 403 to WebFetch. ResearchGate's
   "Request PDF" pages generally require the paper to have been uploaded by
   an author and require an account to request it; not a genuine
   open-access channel even when it loads.
5. **Google Scholar's "All versions" listing** — only surfaced the same two
   already-tried hosts (USDA mirror, Springer), no additional free-PDF
   mirror.
6. **SSRN** — searched specifically for an SSRN preprint of this paper; none
   found (the search did surface a *different*, related SSRN paper by an
   overlapping author subset on poultry wages — see below).
7. **NBER working paper w29103** ("Concentration and Resilience in the US
   Meat Supply Chains") — read in full as a plausible related lead, but
   this is a different paper entirely (Meilin Ma & Jayson Lusk, Purdue,
   2021, a Cournot-competition simulation study of plant-shutdown risk, not
   an empirical concentration-measurement paper) — it cites a *different*
   Saitone/Schaefer paper (McKendree, Saitone & Schaefer 2020, "Oligopsonistic
   Input Demand") but contains no broiler CR4 figures itself. Not useful for
   this specific discrepancy.

### What was found instead: a 2025 open-access companion paper that independently confirms "78%" is real — but flags a likely methodology mismatch

A search for the exact author team's other poultry-specific work surfaced:

**Saitone, T.L., Schaefer, K.A., Scheitrum, D., Arita, S., Breneman, V., &
Nemec Boehm, R. (2025). "Consolidation, productivity, and downstream prices
in the US poultry industry." *Agricultural and Resource Economics Review*,
54, 157–178.** Published **open access under a CC-BY license** by Cambridge
University Press — no paywall. PDF fetched directly via `curl` and read in
full (22 pages after text extraction).

This is five of the same authors as the RIO 2024 paper (Saitone, Schaefer,
Scheitrum, Arita, Breneman, Nemec Boehm — RIO 2024 additionally lists Josh
G. Maples), studying the poultry industry specifically, published one year
later. Two sentences from this paper, read directly and quoted verbatim:

> "In 2019, the CR-4 for the US poultry industry was 0.78. In the absence
> of consolidation, the CR-4 for 2019 would have been 0.60."

**This confirms the 78% figure is a real number this author team has
published, not an AI-tool fabrication or misread** — the original
2026-09-03 Consensus.app synthesis correctly extracted a real figure. The
question is which paper it actually belongs to.

**Critically, this paper's own methodology section states plainly what
data it uses:**

> "To do so, we use plant-level data from the NETS for all poultry
> processing facilities in the United States from 1991 to 2019. This
> dataset contains a unique identification number (known as the DUNS
> number), as well as ownership and sales for each processing plant in
> each year of the analysis."

**NETS = National Establishment Time-Series**, a private commercial
database (Dun & Bradstreet/DUNS-based) tracking establishment-level
ownership and sales — a fundamentally different data source and market
concept (private ownership/sales records, ORCID/DUNS-linked corporate
identity) than **USDA/FSIS federally-inspected slaughter-volume data**,
which is what both (a) USDA AMS PSD's own official CR4 figures and (b), per
its own publicly available abstract (still only read via repeated,
independent search-engine syntheses — not yet a primary read), the actual
RIO 2024 paper claim to use: "annual plant-level food safety and inspection
service (FSIS) data that cover all federally inspected livestock processing
facilities in the U.S."

**Working hypothesis — flagged as a hypothesis, not a finding:** the 78%
figure may have been correctly extracted by the original AI search, but
attributed to the wrong paper within this author team's closely related
body of work — i.e., it may be this 2025 NETS-based, poultry-only paper's
figure, not the 2024 FSIS-based, all-three-commodity paper's figure that
was actually cited in this project. If that's right, the *actual* Schaefer
et al. (2024) broiler CR4 for 2019 is plausibly much closer to PSD's
official 53%, since both would be built from the same underlying FSIS data
family PSD itself regulates and reports from. This would resolve the whole
discrepancy as a citation mix-up rather than a genuine contradiction
between two credible primary sources measuring the same thing differently.

**This is still unconfirmed.** It requires an actual direct read of RIO
2024's own Table/figures to settle, which remains blocked. Do not treat
this hypothesis as resolving the discrepancy in the manuscript — it only
narrows what's most likely going on and gives Britton (or a future session
with library access) a much more specific thing to check for: *does RIO
2024's own broiler CR4 for 2019 read closer to 53% or 78%?*

A secondary, tangential finding while searching: this author team has a
**third** related paper — "The Effects of the U.S. Poultry Industry
Consolidation on Employee Productivity and Wages" (Saitone, Schaefer,
Scheitrum, Arita, Breneman, Nemec Boehm — SSRN 5188460) — a labor-market
companion piece, not fetched this pass (out of scope for the concentration
question), but worth knowing this author team has published at least three
distinct poultry/meat-processing papers using at least two different
datasets (FSIS and NETS) since 2023 — a real source of citation-confusion
risk for anyone (human or AI) summarizing "the Schaefer paper" from
memory rather than a direct read.

Updated: `PROJECT_STATUS.md` (Open Decision #6, rewritten),
`NOTES/Claim_Fact_Check.md`, `SOURCE_VERIFICATION/Evidence_Table.md`,
`LITERATURE/Market_Concentration_Evidence.md` (caveat added at the top),
`NOTES/Commodity_Structure_Comparison.md` (concentration-ratio table cells
rewritten with the caveat inline, not just cross-referenced).

## 3. Idea 28 (2025-26 beef price-fixing saga) — primary-source fact verification

Per the task brief: verify the actual facts behind
`Claude_Knowledge/Research_Stream_Ideas.md`'s idea 28 (added 2026-09-05,
explicitly flagged there as "WebSearch only" and unverified) via primary
sources — DOJ press releases/documents, actual court filings, NCBA's own
public statements — **without** making or leaning toward the adoption
decision the scouting log itself correctly identified as Britton's to
make (whether this becomes new Study 1 corpus material / a Study 2
antecedent for `MEAT_SUPPLY_CHAIN_PAPER`, or nothing).

### Executive Order 14364

Read directly via the Federal Register's API/XML endpoints (the same
technique that worked on 2026-09-05 for the COOL rule — the HTML document
page still redirects to an anti-bot interstitial):
- Metadata: `federalregister.gov/api/v1/documents/2025-22537.json`
- Full text: `federalregister.gov/documents/full_text/xml/2025/12/10/2025-22537.xml`

**Confirmed directly**: "Addressing Security Risks From Price Fixing and
Anti-Competitive Behavior in the Food Supply Chain," signed **December 6,
2025**, published **December 10, 2025** (90 FR 57349). Directs DOJ/FTC task
forces to investigate anticompetitive practices in food-related industries,
naming meat processing, seeds, fertilizer, and agricultural equipment as
sectors of particular concern.

### DOJ's own statements on the investigation

- DOJ's own OPA video page confirms a **May 4-5, 2026** press conference
  (Acting AG Todd Blanche, Secretary of Agriculture Brooke Rollins, Director
  of Trade and Manufacturing Peter Navarro) on "antitrust investigations and
  meatpacking operations" — page loaded and speaker/date confirmed directly,
  but carries no transcript text, so the specific content of what was said
  could not be extracted from DOJ's own page.
- Deputy Assistant Attorney General Nicole Sarrine's remarks at the R-CALF
  USA 2026 Annual National Convention (April 2026), read directly from
  DOJ's own speech-transcript page: confirms "the investigation is well
  under way," following President Trump's November 2025 directive re:
  "potential collusion, price fixing, and price manipulation," and that DOJ
  is separately monitoring the private *Cattle and Beef Antitrust
  Litigation* civil case. **Does not explicitly use the word "criminal"**
  in the portion extracted.
- The **"criminal"** characterization in the scouting log traces to
  reputable press (the Wall Street Journal, per multiple secondary sources)
  quoting DOJ officials/sources describing "criminal anticompetitive
  conduct" under Sherman Act §1. This is credible (multiple independent
  outlets, DOJ's own whistleblower-reward-program promotion for the case is
  consistent with a criminal referral pathway) but **was not independently
  confirmed against a DOJ document read directly this pass** — flag this
  precision gap if the manuscript ever states flatly that DOJ's beef
  investigation is "criminal" rather than "reported to be criminal."

### A brand-new development, not in the 2026-09-05 scouting log

DOJ's Antitrust Division **expanded its beef-affordability investigation to
eight major retailers** — Kroger, Walmart, Aldi, Costco, Publix,
Albertsons, Ahold Delhaize USA, and Amazon — via information-request
letters from Associate Attorney General Stanley Woodward, reported by
multiple reputable outlets (Forbes, Bloomberg, Fox Business, Meatingplace)
around **September 1-3, 2026** — i.e., within the last week. Average retail
ground-beef price cited: $3.95/lb (Dec. 2020) → $6.89/lb (July 2026). **Not
independently traced to a DOJ document this pass** (time-boxed; a DOJ press
release or the actual Woodward letters were not located/fetched) — flagged
as a good target for a future session. If confirmed, this genuinely
broadens idea 28's "three competing narratives" framing (DOJ/collusion,
administration/imports, NCBA/thin-margins) to include retailers as a fourth
scrutinized actor.

### The civil litigation — read directly from the actual court docket, not news summaries

Found the real MDL docket via **CourtListener's RECAP archive**
(`courtlistener.com`, a free, legitimate aggregator of PACER federal-court
filings run by the nonprofit Free Law Project) — its search UI 403'd to
WebFetch, but its public search API worked via `curl`, and once the docket
ID was found, the actual signed PDF orders were downloadable directly from
`storage.courtlistener.com` (RECAP's document store) with no login needed.

**Case**: *In re: Cattle and Beef Antitrust Litigation*, MDL No. 22-3031
(JRT/JFD), U.S. District Court, District of Minnesota, Judge John R.
Tunheim.

**Settlement (Doc. 1597, signed 2026-05-27)** — read in full (22 pages):
Consumer Indirect Purchaser Plaintiffs' final-approval order for a **joint
Cargill + Tyson settlement of $87,500,000** ("a total cash payment of
$87.5 million which has been deposited into the Settlement Fund"). **This
corrects the scouting log's stated date of "May 29, 2026" to the actual
signed date of May 27, 2026** — the figure itself ($87.5M) is exactly
right. A separate, Tyson-only ~$82.5M settlement with grocer/distributor
(Commercial and Institutional Indirect Purchaser) classes was located at
the motion/notice docket-entry level (confirming it's real and in the same
MDL) but its own final-approval order was not pulled and read this pass —
a minor residual gap for a future session.

**Class certification (Docs. 1609 & 1610, both signed 2026-07-16)** — read
in full (48 + 64 pages). **This is a genuinely mixed ruling, not the
blanket "certified the remaining classes against all four defendants"
the scouting log's shorthand implied:**

- *Doc. 1609 (upstream/cattle-seller plaintiffs)*: the **Indirect Seller
  ("Feeder") Plaintiffs' motion was DENIED entirely** — both their Damages
  Class (lacks predominance, not clearly ascertainable) and Injunctive
  Relief Class (lacks cohesiveness). The **Cattle Plaintiffs' ("Producer")
  motion was GRANTED IN PART**: their proposed Damages Class was
  **certified**; their Injunctive Relief Class was declined *without
  prejudice* (may be renewed later); their "Exchange Class" (people who
  held long positions in live-cattle futures) was **denied** because "more
  than a de minimis portion of the proposed class is uninjured."
- *Doc. 1610 (downstream/beef-buyer plaintiffs)*: the Direct Purchaser
  Plaintiffs', Commercial & Institutional Indirect Purchaser Plaintiffs',
  and Consumer Indirect Purchaser Plaintiffs' **Damages Classes were each
  GRANTED** (against all four defendants: Cargill, JBS, National Beef,
  Tyson) under Rule 23(b)(3) — the court found the "less stringent Daubert
  standard employed at the class certification stage is satisfied" and
  denied defendants' motions to exclude plaintiffs' experts. The CIIPPs'
  proposed **Injunctive Relief Class was declined** *without prejudice*
  (may be renewed later under Rule 23(b)(2)).
- Class period: **June 1, 2015 – December 31, 2020** for the certified
  Cattle Plaintiffs' class; **January 1, 2015 – February 29, 2020** for the
  certified downstream damages classes (a genuine, if minor, date
  difference between the two orders — not a typo, both orders state their
  own period explicitly).

So: real classes against all four defendants were certified (the downstream
damages classes, plus the upstream Producer/Cattle damages class), but a
substantial chunk of what plaintiffs sought — the entire Feeder/Indirect
Seller theory, the futures-trader Exchange Class, and every injunctive-
relief class across both orders — was denied, at least for now. This
nuance matters if the litigation is ever used as Study 1 corpus material
(e.g., as a "confirmed adjudicated collusion" stimulus) or cited for its
outcome rather than just its existence — "certified" is doing less work
than a casual read of the scouting log's prose might suggest.

### Pilgrim's Pride / Agri Stats (broiler chicken, the multi-commodity-pattern claim)

- DOJ's own (archived) OPA press release confirms Pilgrim's Pride pled
  guilty and was sentenced to a **$107,923,572** criminal fine for
  broiler-chicken price-fixing/bid-rigging conduct (roughly 2012-2017).
  **This is a 2021 event** — a precision note, not a correction to idea 28
  itself: the scouting log's prose places this fine in the same paragraph
  as 2026 Agri Stats developments in a way that could read as
  contemporaneous. Keep the dates clearly separated in any manuscript use.
  (A retry WebFetch on the exact press-release date returned an empty page;
  the 2021 year is high-confidence via the "archives" URL path and
  corroborating secondary sources, but not re-confirmed to the exact day
  this pass.)
- The Agri Stats companion-case injunctive-relief settlement's **April 14,
  2026** oral preliminary approval, and the pre-existing **$203.35M**
  consumer settlement fund it clears the way for, are consistent with
  legal/trade press (Meatingplace, MLex, openclassactions.com) — not
  independently re-verified against the docket itself this pass (time-
  boxed). Worth noting: a **final approval hearing was scheduled for
  September 1, 2026** — six days before this note — so a future pass
  should check whether it actually occurred and with what outcome, rather
  than treating "preliminary approval" as the current status indefinitely.

### NCBA's own public statements

NCBA's own website (`ncba.org`) is **durably Cloudflare-blocked** to both
WebFetch and `curl` with browser User-Agent headers (a "Just a moment..."
JS-challenge page, structurally identical to the MDPI and settlement-
administrator blocks noted in the 2026-09-05 pass) — a genuine, not-yet-
solved access limitation for this environment, not a claim NCBA's
statements don't exist. Colin Woodall's quoted positions were relayed
instead via multiple reputable agricultural-trade-press outlets
(AgWeb, Drovers, ABC News, Beef Magazine) that themselves appear to be
quoting NCBA's press releases directly:
- An **August 21, 2026** NCBA statement expressing disappointment with a
  Trump social-media post on beef imports, arguing that "flooding the
  market with government-subsidized, below-market beef is not the way to
  rebuild the American cattle herd," and noting cattle markets had already
  turned sharply lower.
- Earlier 2026 statements opposing the Argentina beef-import plan
  specifically: "only creates chaos at a critical time of the year for
  American cattle producers, while doing nothing to lower grocery store
  prices," citing a $801M/$7M U.S.-Argentina beef trade imbalance over the
  past five years and foot-and-mouth-disease biosecurity risk.
- **Not independently confirmed this pass**: the scouting log's specific
  claim that NCBA points to "USDA data claiming packers are posting
  losses, not profiteering." A related, independently-sourced data point
  was found (Sterling Marketing's packer profit tracker, cited in ag press,
  showing beef packers losing $100-150/head for over a year as of 2026;
  Tyson's own Q3 FY2026 Beef segment margin is itself negative — see below)
  that is consistent with this framing, but it wasn't traced to an NCBA
  statement making that specific argument in those words.

### Sept. 4, 2026 White House executive orders — a genuinely new, directly relevant development found while researching this

While verifying idea 28, found that President Trump signed **two more
executive orders on September 4, 2026** (three days before this note) —
distinct from EO 14364 — on livestock-market competition and country-of-
origin labeling. Read the White House's own fact sheet directly
(`whitehouse.gov/fact-sheets/2026/09/...`):
- Directs the Secretary of Agriculture to "prioritize investigations into
  potential violations of the Packers and Stockyards Act, increase federal
  resources for these investigations, and review existing policies."
- Directs USDA, working with USTR, to **review existing legal authority for
  mandatory country-of-origin labeling on beef** and conduct an economic
  analysis of potential impacts — directly on-topic for this project's core
  COOL research question (mandatory beef COOL was repealed in 2015; this is
  a live 2026 signal it may be reconsidered).
- Directs USDA to "expand interstate market access for eligible meat
  products," removing a barrier that currently stops state-inspected small
  processors from selling across state lines.
- Cites beef CR4 concentration directly: "Over 40 years ago, the four
  largest beef packers accounted for 36 percent of all purchases of steers
  and heifers. Today, that has increased to 85 percent" — matching PSD's
  own official 2019 figure exactly, an independent (if not primary-
  measurement) corroboration of the beef number this project already
  relies on.

**This is genuinely new and directly relevant to the project's core
research questions (COOL, market concentration, market access) — not
adopted into any design decision here, but flagged for whoever next
touches `NOTES/COOL timeline` material or the project's "what's currently
live in policy" framing.** Not yet cross-referenced into
`NOTES/` COOL-timeline files or `RESEARCH_QUESTIONS.md` — a follow-up for a
future pass.

## 4. Tyson FY2026 update (Task 3)

Tyson Foods' own official Q3 FY2026 earnings release (investor-relations
PDF, fetched directly, not a news summary) extends the 2026-09-05
Tyson/JBS margin dataset (which stopped at FY2023) through FY2026:

| Beef segment operating margin (GAAP, as reported) | Q3 FY2025 | Q3 FY2026 | 9-mo FY2025 | 9-mo FY2026 |
|---|---|---|---|---|
| | (8.2)% | **(2.6)%** | (4.4)% | **(4.3)%** |

Tyson's own full-year FY2026 outlook (as of this release) projects a Beef
segment operating **loss** of $625-775 million, attributed to "significant
margin compression amid volatile cattle prices and one of the most severe
cattle shortages in U.S. history."

**This is a useful contrast case, not a contradiction, of the project's
existing FY2020-21 finding.** The 2020-21 COVID-era plant-disruption shock
widened Tyson's Beef margins (6.6%→18.0%). The 2025-26 cattle-supply shock
(the smallest U.S. cattle herd since 1951, discussed elsewhere in this
project) is producing sustained Beef losses instead. Both are real,
company-reported facts about the same segment at the same company — they
differ because the underlying shock is different (a processing-capacity
shock that widened the packer's spread vs. a cattle-supply shock that
appears to be compressing it). This is also relevant to evaluating NCBA's
public "packers are posting losses, not profiteering" framing (idea 28,
above) — Tyson's own current-period data is consistent with that framing
for *this* period, without in any way undermining the project's separate,
already-well-supported FY2020-21 finding. Don't let either finding be used
to smooth over or contradict the other in the manuscript — they're both
true, for different periods and different shock types.

## Files edited this pass

- `PROJECT_STATUS.md`
- `NOTES/Claim_Fact_Check.md`
- `SOURCE_VERIFICATION/Evidence_Table.md`
- `LITERATURE/Market_Concentration_Evidence.md`
- `NOTES/Commodity_Structure_Comparison.md`
- This file (new).

No git commands were run this pass — these changes are uncommitted as of
this note, per standing instructions for this session (a coordinating
process handles git centrally).
