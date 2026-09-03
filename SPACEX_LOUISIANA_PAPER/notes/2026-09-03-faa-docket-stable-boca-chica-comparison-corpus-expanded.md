# 2026-09-03 — FAA docket flat, Stop SpaceX coalition partially identified, $25M/$100M reconfirmed, Boca Chica comparison corpus substantially expanded

## What this is
Continuation of the nightly FAA-docket/comparison-case tracking series. Read-only research pass
(background agent), findings written up here by the coordinating session.

## 1. FAA docket (FAA-2026-8614) — flat since 09-02

Direct-fetch confirmed (regulations.gov 403s directly; fetched via r.jina.ai reader proxy, consistent
with every prior session):
- Status: **"Closed for Comments"**
- **Posted: 3,201** (vs. 3,200 on 09-02 — noise-level, +1)
- **Received: 14,670** (vs. 14,669 on 09-02 — noise-level, +1)

Corroborates the 09-02 finding that the single moderation-queue release batch (Sept 1, ~17:15-17:18
UTC) is the last thing that's happened to this docket — nothing new posted since. The 14,670 "received"
figure is still shown only on the client-rendered docket page, not exposed via the public v4 API —
same caveat as before, treat as "shown on the page, not API-verified."
Source: https://www.regulations.gov/docket/FAA-2026-8614 (via r.jina.ai proxy)

## 2. "Stop SpaceX" coalition — partially identified via its own site, still no news-verified scale

New find: the coalition's own website, **stopspacex.com** ("Save Pecan Island and the Migratory
Flyway — Stop SpaceX"), fetched directly. It does not name a lead organizer/person or parent
organization — describes itself as uniting sportsmen/hunters, conservation NGOs, scientists, local
Vermilion Parish residents, outdoor-economy businesses, and elected officials. Stated claims: 300+ bird
species at risk, 130,000 acres of threatened wetland habitat, Central Flyway significance. Carried an
active call-to-action during the comment period ("There is still time to 'public comment' on the FAA
Waiver, Deadline August 31, 2026") — direct evidence the coalition was driving comment-docket
submissions, consistent with the trendingtopics.eu profile already in the 09-02 note — but still no
quantified scale (no follower counts, no claimed comment totals, no named leader).
Source: https://stopspacex.com/

Could not fetch The Hill's "SpaceX launch facility concerns draw muted response from Jeff Landry"
(403'd both directly and via proxy) — title/URL only from a WebSearch snippet, **not verified, do not
cite content**. Flag as a lead for a future session with different fetch tooling.

**Net: no news source found (tonight or 09-02) that characterizes the surge's organizers or scale with
real numbers.** Unchanged gap.

## 3. $25M vs. $100M discrepancy — reconfirmed stable, no new written source for $100M

Re-fetched LED's own program page (opportunitylouisiana.gov/spacex) directly tonight. Verbatim content
confirmed: "$25 million charitable donation to the Community Foundation of Acadiana"; "$20 million
upfront payment" to local taxing bodies; "at least $25 million annually for 25 years, generating more
than $825 million"; 3,000 direct jobs, ~8,100 indirect, $92,600 avg. salary. **Still no mention of a
coastal master plan or $100M figure anywhere on this page.**

This matches the 08-29 note's resolution exactly: **both figures are real and distinct**, not a
conflation — $25M is a written/formal LED commitment; $100M is Gov. Landry's verbal press-conference
statement about SpaceX contributing to the state's Coastal Master Plan, reported contemporaneously by
The Current (Lafayette) and corroborated qualitatively (no dollar figure) by AP/Yahoo. Tonight's search
found the same $100M figure repeated in secondary coverage (ENR: CPRA Communications Director Ryan
Shaw confirming coastal work is likely but "CPRA has not designed any projects specifically for
SpaceX") but **no new primary/written source** stating $100M in writing. Confidence unchanged from
08-29: moderate-high, verbal-tier sourcing for the $100M figure specifically.
Sources: https://www.opportunitylouisiana.gov/spacex ,
https://www.enr.com/articles/63567-spacexs-100b-louisiana-spaceport-takes-aim-at-industrial-scale

## 4. Boca Chica/Starbase comparison-case corpus — substantially expanded

**a) Federal land-swap lawsuit (new to this project, directly relevant to the comparison frame).**
June 1, 2026: U.S. Fish and Wildlife Service approved the "Boca Chica Land Exchange" — 715 acres of
Lower Rio Grande Valley National Wildlife Refuge land to SpaceX in exchange for 683 acres of
SpaceX-owned land near a separate refuge. June 10-11, 2026: Center for Biological Diversity, Save RGV,
the Carrizo/Comecrudo Nation of Texas, and the South Texas Environmental Justice Network sued U.S. Fish
and Wildlife Service, alleging violations of the National Wildlife Refuge System Improvement Act,
NHPA, NEPA, and the APA — citing a 2024 study finding shorebird nest/egg damage near launch sites,
threats to ocelots/aplomado falcons/piping plovers, and risk to the Palmito Ranch Battlefield National
Historic Landmark. July 20, 2026: same coalition filed an emergency injunction to halt the exchange
pending the ruling. **No ruling found as of tonight** — case remains pending. A docket number
("1:26-cv-02053, D.D.C.") appeared in one AI-search summary but is **unverified — do not cite**.
Sources: https://www.tpr.org/environment/2026-06-11/lawsuit-seeks-to-block-spacex-land-exchange-in-south-texas-wildlife-refuge (direct),
https://biologicaldiversity.org/w/news/press-releases/emergency-injunction-sought-to-protect-texas-wildlife-refuge-from-spacex-2026-07-20/ (snippet only)

**b) Texas Supreme Court beach-closure standing ruling (new, directly usable).** June 19, 2026: Texas
Supreme Court ruled unanimously (opinion by Justice Rebeca Huddle) that SaveRGV, the Sierra Club, and
the Carrizo/Comecrudo Nation lack standing to sue over Boca Chica Beach closures during launches —
holding the 2009 constitutional public-beach-access amendment contains no private right to sue, and
that a 2013 state law (HB 2623) authorized SpaceX-related beach/road closures. Plaintiffs' attorney
Marisa Perales: the ruling "elevates SpaceX's interests over Texans' rights" and renders the
beach-access amendment "toothless." Directly usable for the paper's environmental-justice/procedural-
access framing at the comparison site.
Source: https://www.texastribune.org/2026/06/19/texas-spacex-elon-musk-boca-chica-beach-supreme-court/ (direct, full text)

**c) Mercury/wastewater pollution story — not new, now dated.** The mercury water-pollution allegation
(TCEQ/EPA Region 6 notices, no wastewater discharge permit) referenced in the 08-29 note's FAA comment
letter as "2024 CWA violations" traces to an **August 2024** CNBC exclusive — over two years old.
SpaceX disputed the reported concentration, attributing part of the figure to a decimal-point
transcription error (0.113 μg/L vs. a misreported 113 μg/L) in some coverage.
Sources: https://www.popsci.com/science/spacex-mercury-water-pollution/ ,
https://www.nbcnews.com/science/environment/spacex-polluted-waters-texas-regulators-rcna166283 (snippet-level)

**d) Beach "partial control" transfer to City of Starbase — flag correction, not recent.** A KRGV
headline that looked current is actually dated **September 2025** (Cameron County Commissioners Court
approved the interlocal agreement Sept. 23, 2025) — a full year old. Gives the City of Starbase
authority over beach maintenance/erosion/dune restoration and beachfront-construction rules, but
explicitly does not let Starbase restrict public beach access except during active testing/launches.
Not independently fetched (dead link on KRGV's new site) — relies on WebSearch synthesis of KSAT/
Insurance Journal coverage, flag as snippet-level.

**e) Older NEPA lawsuit dismissal — background only, also not recent.** A separate suit by Center for
Biological Diversity/American Bird Conservancy/Carrizo-Comecrudo Tribe against the FAA (over a 2023
test-launch environmental review) was dismissed — dated 2025-09-17, also about a year old. Useful
background pattern (opponents have lost at least one prior suit at this site) but not a recent
development.

**Bottom line:** the genuinely new-to-corpus, well-sourced material is (a) the land-swap
lawsuit/injunction (filed June-July 2026, still pending) and (b) the Texas Supreme Court's June 19,
2026 standing ruling. Both strengthen the comparison-case framing (regulatory/legal deference to
SpaceX over community/tribal/environmental-group standing) but are 2-3 months old, not "last few
weeks" — no genuinely new Boca Chica development was found dated after early August 2026.

## 5. Broad scan for other Vermilion Parish/Louisiana news since 09-02 — nothing new

Multiple targeted searches turned up only material already dated 08-25 through 08-27 and already
logged. No new Louisiana-specific story dated 09-02 or later was found.

## Summary: what's new vs. stable since 09-02

| Item | Status |
|---|---|
| FAA docket counts | Stable — flat at ~3,200/~14,670, no new posting activity |
| Stop SpaceX organizer identity | Partially advanced — found the coalition's own site, still no news-verified scale/leadership |
| $25M/$100M discrepancy | Stable — reconfirmed via fresh direct fetch, no new written $100M source |
| Boca Chica comparison corpus | Meaningfully expanded — land-swap lawsuit/injunction (pending) + TX Supreme Court standing ruling, both new to this project's notes though dated June-July 2026 |
| Other Vermilion Parish news | Stable — nothing new since 09-02 |

All claims labeled by confirmation tier: direct fetch (LED page, stopspacex.com, TPR article, Texas
Tribune Supreme Court article, regulations.gov via proxy) vs. WebSearch-snippet-only (The Hill piece —
unfetched; KRGV beach-control piece — unfetched; the D.D.C. case number — unverified).
