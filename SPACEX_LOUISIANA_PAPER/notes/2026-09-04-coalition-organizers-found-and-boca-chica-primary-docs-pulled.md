# 2026-09-04 — Stop SpaceX organizers identified, Boca Chica case docket number and TX Supreme
# Court opinion primary-verified, TCEQ penalty order pulled directly, FAA docket still flat

Follow-up to `2026-09-03-faa-docket-stable-boca-chica-comparison-corpus-expanded.md`. Read-only
research pass (background agent). Tooling note: `poppler-utils` was not preinstalled tonight —
reinstalled via `apt-get update && apt-get install -y poppler-utils` (the first attempt without
`update` hit a stale-index 404; refreshing fixed it). All PDFs below were fetched with `curl`
directly (not through a proxy — none of tonight's PDF hosts blocked `curl`) and read with
`pdftotext -layout`, i.e. direct text extraction, not an AI-summarized read, except where noted.
**No theory chain, coding scheme, or Study 1 option (A/B/C) decided or touched here — still
Britton's call**, per standing project rules.

## 1. FAA docket (FAA-2026-8614) — still flat

Direct fetch via `r.jina.ai` proxy (regulations.gov itself still 403s directly, unchanged from
every prior session):
- Status: **"Closed for Comments"**
- **Posted: 3,201** (identical to 09-03's figure — no movement)
- **Received: 14,670** (identical to 09-03's figure — no movement)

Nothing has moved on this docket since the Sept 1 moderation-queue release. Three consecutive
nightly checks (09-02, 09-03, 09-04) now show the exact same numbers. Recommend not re-checking
nightly going forward unless something external suggests renewed activity (e.g. a news story
about the docket) — this is about as flat as a finding gets.
Source: https://www.regulations.gov/docket/FAA-2026-8614 (via r.jina.ai proxy)

## 2. "Stop SpaceX" — the evidence gap substantially closes, at the local-organizer level

Three prior nights (09-01, 09-02, 09-03) found the coalition's website and a national-NGO
umbrella framing but no named leader and no scale figure. Tonight, searching specifically for
local-news interviews (rather than the coalition's own site or national press) surfaced this
directly:

**Named local organizers, corroborated across two independent outlets:**
- **Brennon "Bruno" Sagrera** — "a ninth-generation Island local and fifth-generation rice and
  crawfish farmer," quoted in both the Louisiana Illuminator (2026-08-19) and KLFY
  (economic-growth-coastal-preservation-conflict piece). Illuminator quotes him directly: *"I
  don't think they understand that residents want to be part of these talks too... We're a
  democracy."* Also: *"With all this secrecy, no one in the community has had real information
  shared with us,"* and he raises the NDA complaint already in the corpus (*"I don't understand
  how it's legal that our elected officials are barred by NDAs..."*).
- **Brooke Broussard** — named in the Illuminator piece as **"a founding member with family on
  Pecan Island,"** who coordinated the initial organizing meetings: *"There wasn't a real agenda
  beyond opening a room, because nobody — no community leader, no public official — was providing
  one."* Also quoted: *"They're drunk on dollar signs,"* and *"I've got, as I put it, war drums
  beating in my heart — because my family is at stake."*
- **Wayne Miller** — assistant chief, Pecan Island Volunteer Fire Department, already in the
  08-29 note as the person who first spotted survey crews (Aug. 10); the Illuminator piece
  confirms he's part of the same organizing effort, not just the initial trigger.

**A genuine scale figure, the first found in four nights of trying:** the Illuminator reports
**Sagrera estimated 20 to 30 people joined each nightly video call** during the group's active
organizing phase in early-to-mid August 2026 — before the Aug. 25 announcement.

Source (fetched via r.jina.ai proxy, direct WebFetch 403'd both times):
https://lailluminator.com/2026/08/19/pecan-island-spacex/ — same article already cited in the
08-29 note for the NDA material, so this is a re-read of an already-corpus source that turns out
to also carry the leadership/scale detail the project had been separately searching for since
09-01. Worth flagging that lesson explicitly: three nights searched national/wire coverage and
the coalition's own site for this; the answer was in a local outlet already in the corpus, just
not read for this specific detail before.

**What's still not resolved, so the gap isn't fully closed:** this identifies the founders/
organizers of the *local Pecan Island resident group* and a call-attendance estimate for its
*organic pre-announcement phase*. It does **not** give a membership/follower count for the
`stopspacex.com` website or its Facebook page (a WebSearch specifically for Facebook
member/follower counts tonight returned nothing usable), and it does not name a single leader of
the *broader coalition* stopspacex.com itself describes (sportsmen/hunters, national conservation
NGOs, scientists, outdoor-economy businesses, elected officials) — that wider coalition still has
no named single leader or total-scale figure across all constituencies. Recommend treating this
as: **local-group leadership — resolved; broader-coalition leadership/scale — still open.**

## 3. Boca Chica comparison corpus — primary court/agency documents pulled directly (not news summaries)

This was the explicit ask tonight: strengthen the two items flagged 09-03 as news-summary-only by
pulling the actual filings. Three primary documents were fetched and read directly via
`curl` + `pdftotext`.

### 3a. Land-exchange lawsuit — case number now primary-verified, claims read in full

The 09-03 note flagged docket number "1:26-cv-02053, D.D.C." as **unverified, from an AI-search
summary — do not cite**. Tonight, fetched the actual stamped complaint PDF directly (Center for
Biological Diversity's own hosted copy) and extracted it with `pdftotext`:
https://biologicaldiversity.org/programs/government-affairs/pdfs/Stamped-Complaint-FWS-Land-Exchange-Suit-20260609.pdf
(619KB, HTTP 200, direct `curl`, not proxied).

**Confirmed directly from the document's own caption page**, verbatim:
- Court: **United States District Court for the District of Columbia**
- **Case No. 1:26-cv-02053** — the previously-unverified number is now primary-source confirmed.
- Filed **June 10, 2026** ("Document 1 Filed 06/10/26").
- Plaintiffs: Center for Biological Diversity, Save RGV, the Carrizo/Comecrudo Nation of Texas
  Inc., South Texas Environmental Justice Network.
- Defendants: Brian Nesvik (in his official capacity as Director, U.S. Fish and Wildlife Service)
  and the U.S. Fish and Wildlife Service itself.
- Title: "Complaint for Declaratory and Injunctive Relief."
- Signed by Ivan R. Ditmars, Center for Biological Diversity, dated June 10, 2026.

**Five claims for relief, read directly from the document (headers verbatim):**
1. Failure to demonstrate a net conservation benefit to the Lower Rio Grande Valley NWR
   (National Wildlife Refuge System Improvement Act).
2. Inconsistency with the 1997 Interim Comprehensive Management Plan for the refuge (same Act).
3. Failure to revise/update that 1997 management plan (same Act).
4. Failure to ensure comparable historic property in exchange for 700+ acres of the **Palmito
   Ranch Battlefield National Historic Landmark** (National Historic Preservation Act).
5. Failure to take the required "hard look" / ensure scientific integrity of the Environmental
   Assessment (NEPA).

Relief requested (WHEREFORE clause, read directly): declare the Service violated all four named
statutes (Refuge Improvement Act, NHPA, NEPA, APA), set aside and enjoin the exchange, compel a
revised management plan, and award attorney fees under the Equal Access to Justice Act.

**No ruling found on this specific case as of tonight** — same negative finding as 09-03, but now
resting on a primary document read rather than search snippets. One important disambiguation
tonight: several search hits ("SpaceX withdraws from land swap," "Somehow, the Boca Chica land
swap is off," dated Nov. 2024) are **not** about this case — they're about a separate, older
(2024) Texas Parks & Wildlife Department land swap involving Boca Chica *State Park* and *Laguna
Atascosa*, which SpaceX withdrew from in September 2024, over a year before this suit was filed.
Confirmed via direct fetch of krgv.com's own withdrawal story (dated 2024-11-20) and a second
independent piece (offthekuff.com) — both explicitly TPWD, not U.S. Fish and Wildlife Service, and
both about a 477-acre-for-43-acre deal, not the 715-for-683-acre exchange in the 2026 suit. **Do
not conflate these two land swaps** — flagging this clearly since the search terms overlap enough
that it's an easy mistake. Similarly, three other search hits describing a federal judge
("Nichols") "rejecting" a conservation-group challenge and clearing the way for expanded Starship
testing are **also a different, older case** — the already-known 2025-09-17 NEPA lawsuit dismissal
(FAA's 2022 approval of 5→25 launches/year), re-confirmed tonight via two independent fetches
(one gave a plainly wrong date, "March 5, 2026," which is actually this same underlying case's
oral-argument date reused in error by the summarizing pass — the article's own dateline reads
September 2025; flagging the date inconsistency rather than trusting either number blindly). Not
new, not the land-exchange case — same background item the 09-03 note already had.

### 3b. Texas Supreme Court beach-closure ruling — full opinion pulled and read

Found and fetched the actual opinion PDF directly from the court's own site:
https://www.txcourts.gov/media/1462904/24-0237-0407-0457.pdf (215KB, HTTP 200, direct `curl`).

**Confirmed directly from the opinion text:**
- Three consolidated cases: **No. 24-0237** (Texas GLO/Commissioner Buckingham v. SaveRGV et al.),
  **No. 24-0407** (Cameron County v. same), **No. 24-0457** (Ken Paxton, AG, v. same).
- Argued March 5, 2026; **opinion delivered June 19, 2026** (matches the date already in the
  09-03 note).
- Authored by **Justice Rebeca Huddle**; no dissent or concurrence appears in the document (text
  scanned directly for dissent/concurrence markers — none found), consistent with "unanimous" as
  reported in the Texas Tribune coverage already cited.
- **Holding, quoted directly**: the 2009 constitutional beach-access amendment's own text
  (Art. I, § 33(d)) "does not create a private right of enforcement" — the Court held this
  "forecloses" SaveRGV/Sierra Club/the Tribe's suit as "facially invalid," reversed the court of
  appeals, and reinstated the trial court's dismissal for lack of jurisdiction.
- **Two nuances not previously in this project's notes, both directly relevant to how precisely
  the paper should characterize this ruling:**
  - Footnote 9: the Court explicitly did **not** reach the merits of whether HB 2623 (the beach-
    closure law itself) is constitutional — it dismissed only on the private-right-of-enforcement
    jurisdictional ground, expressly declining to rule on whether the closures themselves violate
    the "unrestricted" access right in Section 33(b). The prior note's framing ("SpaceX's
    interests over Texans' rights") is the plaintiffs' attorney's characterization of the outcome,
    not something the opinion itself claims to have decided on the merits.
  - Footnote 10: the Court explicitly preserves a *different* potential claim for the
    Carrizo/Comecrudo Nation specifically — religious-practice interference — stating "today's
    holding should not be construed to prohibit the Tribe... from seeking relief for such
    injuries." I.e., this ruling forecloses the beach-access constitutional theory, not every
    possible legal theory the Tribe could bring.
- HB 2623's own 2013 legislative history, read directly from the opinion's citations: the bill
  analysis the Court quotes states legislators "understood that HB 2623 would apply only to
  Cameron County as it was drafted" — worth noting for the paper if a "written into law with the
  specific company/site already known" framing point is useful.

### 3c. Boca Chica TCEQ wastewater penalty — full agreed order pulled, plus a new corpus item

The 08-31 note flagged the **$3,750 TCEQ state fine** (distinct from the $148,378 federal EPA
penalty already primary-verified) as "sourced only to news coverage, not a directly-fetched TCEQ
record." Tonight, fetched TCEQ's own hosted PDF directly:
https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2024/2024-1282-iwd-e.pdf
(13MB, HTTP 200, direct `curl` — a large multi-document agenda-backup file; the actual Agreed
Order and penalty calculation worksheet are within it, located and extracted successfully).

**Confirmed directly from the Agreed Order text (Docket No. 2024-1282-IWD-E):**
- Total administrative penalty: **$3,750**, of which **$750 is deferred**, contingent on
  compliance, and **$3,000 was actually paid**. Matches the reported $3,750 figure, with the
  deferred-portion detail now primary-confirmed rather than secondary-sourced.
- Violation: failure to obtain authorization to discharge industrial wastewater, 30 TEX. ADMIN.
  CODE § 305.42(a), documented by a TCEQ investigator during a record review conducted **July 25
  through July 30, 2024**.
- Same admission-avoidance language pattern as the federal EPA CAFO already in the corpus:
  Section I.3 states "entry of this Order shall not constitute an admission by the Respondent of
  any violation."
- Order terminates five years from its effective date or upon full compliance, whichever is later.

**New corpus item, genuinely useful for the paper's "does the same coalition keep showing up"
angle**: the same multi-document PDF contains a formal public comment (dated October 1, 2024)
objecting to the $3,750 penalty as inadequate, filed on behalf of **Save RGV, the
Carrizo/Comecrudo Nation of Texas, South Texas Environmental Justice Network, and Clean Water
Action** — i.e., the *same coalition* (minus Center for Biological Diversity, plus Clean Water
Action) that later filed the 2026 land-exchange lawsuit above. The comment argues the penalty
"fails to even approach" its deterrent purpose, calls it "absurdly low," and specifically notes
SpaceX had already completed three test launches and multiple static-fire tests from the deluge
system before obtaining a permit. Directly useful, primary-sourced evidence that this is a
recurring coalition across multiple Boca Chica enforcement/litigation fights over several years
(2024 penalty objection → 2026 land-exchange suit), not a series of unrelated one-off actions —
relevant to whatever "does prior knowledge of the pattern change reception" framing Britton may
eventually pick, without this note picking it.

## 4. What's still open

- Broader "Stop SpaceX" coalition-wide leadership/scale (beyond the local Pecan Island group
  identified tonight) — still no single named leader or total membership figure.
- No ruling yet on the pending land-exchange case, 1:26-cv-02053 — now case-number-verified, still
  status "pending" as of tonight.
- The Exxon-Vermilion-Parish wetland-loss lawsuit detail from the Wesolick FAA comment (flagged
  08-30) — still not independently checked against a court record.
- Act 343/HB 1250 and the aerospace public-records-exemption bill's enrolled text (flagged 09-01)
  — still not independently fetched, only news-sourced.
- "Golden Eagles' Conservation Society" (an FAA docket filer name flagged 09-02 as unfamiliar) —
  still not independently verified.
- No theory chain, coding scheme, or Study 1 option (A/B/C) decided — unchanged, still Britton's
  call.

## Summary: what's new vs. stable since 09-03

| Item | Status |
|---|---|
| FAA docket counts | Stable — flat at 3,201/14,670, third consecutive identical reading |
| Stop SpaceX coalition leadership | **Meaningfully advanced** — local organizers named (Sagrera, Broussard, Miller) with a call-attendance scale figure (20-30/call); broader coalition-wide leadership/scale still open |
| Boca Chica land-exchange lawsuit | Case number now primary-verified (was "unverified, do not cite"); full claims read from the complaint itself; still no ruling |
| TX Supreme Court beach ruling | Full opinion primary-verified; two scope-limiting nuances found (merits not reached; Tribe's religious-practice claim expressly preserved) |
| Boca Chica TCEQ penalty | Primary agreed-order document pulled directly; new corpus item found (Save RGV/Tribe/STEJN/Clean Water Action's own penalty-inadequacy objection) |
| Other Vermilion Parish news | Stable — broad search found nothing dated after 08-27 |

All claims above are labeled by tier: primary document, directly fetched and text-extracted
(stamped complaint, TX Supreme Court opinion, TCEQ agreed order) vs. local-news direct fetch
(Louisiana Illuminator, via proxy) vs. WebSearch-snippet-only (nothing load-bearing relied on
snippets alone tonight without a follow-up direct fetch).
