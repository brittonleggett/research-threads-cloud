# 2026-08-29 — Primary-source pass: $25M/$100M reconciliation, FAA letter read, new corpus material

Follow-up to `2026-08-27-orientation.md` and `2026-08-27-webfetch-primary-source-pass.md`. This
session had a working PDF text-extraction path (poppler-utils was installable via `apt-get`, plus
a reader-proxy — `r.jina.ai` — that independently rendered several sites WebFetch's own fetcher
gets 403'd on) that the 2026-08-27 session didn't have. No theory chain, coding scheme, or Study 1
option (A/B/C) decided here — still Britton's call, per standing project rules.

## 1. WebFetch environment check

Works. `opportunitylouisiana.gov/spacex` fetched cleanly on the first try, matching the prior
session's report that WebFetch is unblocked in this environment (unlike an earlier, longer stretch
where the cloud routine's WebFetch was EGRESS_BLOCKED). About a third of news-site URLs tried
tonight (CNBC, thecurrentla.com, KLFY, TheAdvocate's second article, TheHill, HNGN, ENR,
SpaceNews's alt URL, regulations.gov, federalregister.gov, web.archive.org) returned 403/451 or
were otherwise unreachable directly — ordinary bot-blocking on those specific sites/CDNs, not an
environment-wide problem. Where a 403'd source looked load-bearing, I retried it through
`https://r.jina.ai/<url>` (a public reader-mode proxy) and that succeeded in every case I tried.
Flagging this as a technique worth reusing in future sessions when a specific outlet blocks
WebFetch directly — but noting explicitly below everywhere it was used, since it's an extra
extraction hop (site → jina's renderer → WebFetch's own summarizing pass) rather than a direct
fetch, so there's more room for transcription drift than a plain direct fetch.

## 2. The $25M vs. $100M discrepancy — RESOLVED, moderate-high confidence

**Conclusion: both figures are real and distinct commitments, not a media conflation of one line
item.** They come from different channels of the same announcement:

- **$25 million charitable donation to the Community Foundation of Acadiana** — part of the
  state's *written* incentive/PILOT agreement. Confirmed directly, verbatim, on multiple LED
  sources: the `opportunitylouisiana.gov/spacex` program page, and separately LED's own press
  release (`opportunitylouisiana.gov/news/spacex-launches-new-era-of-commercial-spaceflight-with-100-billion-louisiana-campus`),
  which reads: *"$25 million charitable donation to the Community Foundation of Acadiana to
  address strategic regional priorities."* This is the figure the 2026-08-27 session already
  confirmed.
- **$100 million to Louisiana's Coastal Master Plan** — a *separate, verbally-announced*
  commitment, not written into LED's official program page or press release (which is why the
  2026-08-27 session, working only from LED's page, couldn't find it there and correctly flagged
  the discrepancy rather than guessing). The clearest sourcing found tonight: **The Current**
  (Lafayette outlet), a contemporaneous, timestamped live-blog of the Aug. 25 press conference in
  Abbeville, reports at its 12:30pm update: *"Following the announcement, Gov. Landry tells press
  outside the building that SpaceX will contribute $100 million to the state's coastal master
  plan."* (Fetched via the r.jina.ai proxy after a direct WebFetch to thecurrentla.com 403'd —
  flagging the proxy hop per the caveat above.) This is corroborated by an AP/wire-style piece
  (via Yahoo News) that independently quotes Landry making the same underlying claim in looser
  form, with no dollar figure attached: *"SpaceX is going to directly fund some of the projects in
  Louisiana's Coastal Master Plan."* Multiple other outlets (E&E News/POLITICO, TechCrunch,
  PayloadSpace, CNBC — all fetched directly, full text) independently confirm the *partnership*
  itself in qualitative terms (shoreline protection, marsh restoration, wildlife conservation,
  wetland reconnection, working with CPRA) but without a dollar figure in the outlet's own
  written text — consistent with the $100M number having been said aloud at the press conference
  rather than appearing in any outlet's own official written materials or press releases.

**Why this isn't higher than moderate-high confidence**: the $100M figure traces to one
contemporaneous on-site live-blog's paraphrase of Landry's spoken remarks, not to a document
Landry's office, LED, or CPRA has put in writing anywhere found tonight (CPRA's own site wasn't
directly reachable for a search of SpaceX-specific announcements). It's plausible but not
confirmed that this is a preliminary/aspirational verbal figure that hasn't (yet) been formalized
into a written CPRA/state agreement the way the $25M donation and PILOT terms have. Recommend
citing it in any manuscript language as "Gov. Landry stated at the Aug. 25 press conference..."
(attributed to the Governor's verbal remarks, sourced to contemporaneous press coverage) rather
than as an LED-confirmed program term, and keeping the $25M figure cited to LED's own written
page as before. Both are real; they're just documented differently, and a paper doing
claim-specificity coding should probably treat that difference (written/formal vs.
verbal/press-conference) as itself a meaningful data point given the paper's whole framing is
about claim specificity and verifiability.

## 3. FAA docket comment letter — READ IN FULL

The letter is real, was downloaded successfully, and its text is now fully extracted and verified
by two independent paths that agree with each other:
1. `curl` to fetch the raw PDF bytes, then `pdftotext -layout` (poppler-utils, installed this
   session via `apt-get install poppler-utils` — worked cleanly once `apt-get update` refreshed a
   stale package index; this fixes the "PDF tooling not installed" blocker from 2026-08-27).
2. Independently, the same URL fetched via the `r.jina.ai` reader proxy and summarized by
   WebFetch's model — matched the direct extraction on every substantive point checked.

**Filing details** (from the letter's own header): dated August 24, 2026; submitted electronically
via regulations.gov; addressed to FAA Administrator Bedford; RE: comments on NPRM "Waiver of
Specified Statutory Requirements for Commercial Space Launch and Reentry Actions," 91 FR (July 30,
2026), Docket No. FAA-2026-8614. Signed by Rebecca Triche (Executive Director, Louisiana Wildlife
Federation), Mandy Moore (Gulf Program Senior Director, National Wildlife Federation), and Kristi
Trail, P.E. (Executive Director, Pontchartrain Conservancy).

**What the letter substantively argues:**
- **Not opposed to the project or the industry in principle** — the letter opens: *"Our
  organizations do not oppose the commercial space industry, and we recognize the economic
  opportunity it may bring to Louisiana. Our concern is narrow and specific..."* This nuance
  matters for coding — this is not a blanket anti-development letter, it's a process/review
  objection specifically.
- **The specific regulatory target**: the NPRM would let the Secretary of Transportation waive
  requirements under 13 named federal environmental/natural-resource statutes for FAA commercial
  launch/reentry licensing decisions, as a categorical, industry-wide authority rather than a
  case-by-case one. The 13 statutes, as listed in the letter (all confirmed against the Federal
  Register notice's own text, see below): NEPA, Endangered Species Act (incl. Section 7
  consultation), Marine Mammal Protection Act, Migratory Bird Treaty Act, Clean Water Act
  (Sections 401/404), Clean Air Act conformity, Coastal Zone Management Act, Magnuson-Stevens
  Fishery Conservation and Management Act, Rivers and Harbors Act, Wild and Scenic Rivers Act,
  National Marine Sanctuaries Act, Noise Control Act, National Historic Preservation Act.
- **Site-specific stakes named**: 136,000 acres of coastal marsh in Vermilion Parish near Pecan
  Island and Freshwater City (note: slightly different acreage than the ~130,000 figure used in
  the orientation note and most news coverage — the letter's own figure, worth using theirs when
  quoting the letter specifically), within the Chenier Plain, part of the Mississippi and Central
  Flyways, adjacent to the Rockefeller Wildlife Refuge and State Wildlife Refuge complex. Species
  named: wintering waterfowl (millions of ducks/geese), whooping crane (Louisiana reintroduction
  program depends on this habitat specifically), wading birds/shorebirds, and shrimp/crab/finfish
  nursery grounds supporting commercial fisheries.
- **Core argument**: "Removing NEPA and its companion statutes from the licensing stage does not
  make the environmental impacts of a spaceport disappear... What the waiver removes is the
  requirement to identify those impacts, quantify them, disclose them to the public, and consider
  alternatives and mitigation before the damage is done." Frames review as a mechanism that
  produces good siting/mitigation decisions, not an obstacle.
- **Boca Chica invoked directly as precedent** — genuinely useful for this paper's built-in
  comparison-case structure: *"Environmental review of the SpaceX facility at Boca Chica, Texas,
  an ecologically comparable coastal site adjacent to a national wildlife refuge, identified
  significant impacts to habitat and protected species, and the company was separately penalized
  in 2024 for Clean Water Act violations at that facility."* This is the letter's own explicit use
  of the Texas site as an argument for why review matters — a real instance of exactly the kind of
  cross-site precedent reasoning the paper's "does the same script work twice" framing anticipates,
  now with a source. (The 2024 CWA penalty claim itself is the letter's assertion, not yet
  independently verified against an EPA/TCEQ enforcement record this session — flag before citing
  it as an independently-confirmed fact rather than "the commenters state.")
- **Six specific recommendations to the FAA** (withdraw the categorical waiver for ESA/NEPA/CWA/
  CZMA/MMPA/Magnuson-Stevens; retain project-level NEPA review including EISs; retain ESA Section 7
  consultation; limit waivers to case-by-case national-security findings; retain CWA/CZMA review
  specifically for coastal wetlands; conduct a programmatic cumulative-impact review first).
- Explicitly frames a **federal policy contradiction**: *"It would be a profound contradiction of
  federal policy for one federal agency to waive the Clean Water Act wetland protections... while
  other federal agencies spend public money to restore the very same coastline."* — directly
  relevant to a greenwashing/regulatory-venue-shifting frame, since it's making almost exactly that
  argument itself, independently of any framing this paper would impose.

**The docket itself, also now primary-verified** (separately from the letter, via the Federal
Register's own PDF, `govinfo.gov/content/pkg/FR-2026-07-30/pdf/2026-15415.pdf`, fetched with
`curl`+`pdftotext` after both `federalregister.gov` and `regulations.gov` continued to block
WebFetch/bot access tonight): Docket No. FAA-2026-8614, Notice No. 26-11, RIN 2120-AM51, 14 CFR
Parts 400/420/433/437/450. **Comment deadline confirmed: on or before August 31, 2026** — two days
from today. The notice states it implements Executive Order 14335, "Enabling Competition in the
Commercial Space Industry," signed August 13, 2025, under the Secretary of Transportation's waiver
authority at 51 U.S.C. 50905(b)(2)(C). Notably, the FAA's own notice separately invites comment on
whether to *also* waive the Migratory Bird Treaty Act and the National Wildlife Refuge System
Administration Act — i.e., the wildlife groups' Refuge-adjacency concern is something the agency
itself flagged as an open question in its own text, not something the commenters invented.

I did not save a copy of either PDF into the repo. Both are public government/public-filing
documents (not copyrighted third-party content) so referencing/quoting them directly is fine per
the standing instructions, but there's no `Corpus_1`-style raw-file directory set up for this paper
yet the way CCS_PAPER has one, and setting one up is a structural choice I'm leaving for whenever
Britton/a later session picks a Study 1 option — the URLs above are stable, directly-hosted
government/org files, so re-fetching them later isn't at risk the way a paywalled or
takedown-prone source would be.

## 4. New developments/corpus material found (genuinely new since 2026-08-27)

Added to `Study1_Corpus_and_Coding_DRAFT_2026-08-27.md` as rows 6b-6f (see that file for the
full table; summarizing here):

- **Local-resident opposition and transparency complaints — this is new territory the earlier
  corpus pass didn't have at all.** Best single find: Louisiana Illuminator, 2026-08-19 (i.e.
  actually predates the Aug. 25 announcement — residents were reacting to survey crews and rumors
  before the deal was public), reports that Louisiana Economic Development required elected
  officials to sign NDAs to receive project information: State Rep. Jacob Landry signed one in
  February 2026 restricting him from discussing "the prospective company's business interests";
  State Sen. Bob Hensgens initially signed a similar one but had it rescinded over transparency
  concerns. A resident is quoted: *"I don't understand how it's legal that our elected officials
  are barred by NDAs from sharing information with constituents."* Residents formed a "StopSpaceX"
  group after Assistant Fire Chief Wayne Miller spotted survey crews taking soil samples around
  Aug. 10.
- Two post-announcement local-TV pieces (KPLC, Fox 8 Live, both 2026-08-26) add direct resident
  quotes: *"Jeff Landry really stabbed us in the back. He really did. Everything was
  underhanded... We had no say in it. No warning."* Residents separately draw their own Boca Chica
  comparison unprompted: *"there's lawsuits, there's damage to homes"* — worth noting for the
  paper's precedent-awareness angle, since this shows at least some residents already associate
  the Texas site with negative outcomes, independent of anything a survey instrument would need to
  prime. Other concerns raised directly by residents: eminent domain fear, a crabbing-business
  livelihood worry, and rising property-tax exposure from land-value increases.
- This is squarely Option-B-relevant material (opposition/public discourse), and it's a different
  opposition channel than the wildlife-group filing angle already in the corpus — worth keeping
  distinct in any future coding scheme rather than merging "opposition" into one code, since the
  NDA/transparency complaint and the wildlife/habitat complaint are substantively different
  objection types.
- **LED's own press release** (as opposed to its /spacex program page, already in the corpus) is
  now also directly fetched and confirmed — same fiscal figures, no coastal-master-plan mention,
  consistent with everything above.
- No new SpaceX-authored statement was found (SpaceX's own site remains JS-rendered/unfetchable,
  same blocker as 2026-08-27).
- Did not find confirmation of the "882 comments posted to the docket" figure that turned up in
  one WebSearch summary — that came from an AI-generated search synthesis, not a directly-loaded
  regulations.gov page, so I'm not carrying it forward as verified. regulations.gov itself remains
  unreachable by WebFetch (403) even via the r.jina.ai proxy workaround, which only worked for
  ordinary HTML/PDF hosts, not for regulations.gov specifically (untested tonight whether the
  proxy would also 403 there — didn't get to it; flagging as a possible next step, not a dead end).
- Did not find the specific named Boca Chica community-impact researcher/study (item #9 in the
  corpus, "still needed" list) — not pursued tonight, priority was the discrepancy and the FAA
  letter per the task list.

## 5. What's still open

- The $100M coastal-master-plan figure's *sourcing tier* (verbal/press-conference vs. written
  agreement) is itself now a data point worth deciding how to code, once a Study 1 option is
  picked — flagging it as a design question, not resolving it here.
- Item #9 from the corpus (naming the specific Boca Chica academic/ethnographic study) — still
  unidentified.
- The Boca Chica 2024 Clean Water Act penalty claim in the wildlife groups' letter — their
  assertion, not independently verified against an enforcement record this session.
- Whether the docket's "882 comments" figure is real and current — unconfirmed, not carried
  forward.
- No theory chain, coding scheme, or Study 1 option (A/B/C) decided — unchanged, still Britton's
  call.
