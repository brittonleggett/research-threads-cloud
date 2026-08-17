# 2026-08-16 — Orientation: Flock Safety Cameras Paper

Exploratory. Nothing below is locked — same stage the Data Center Paper was
at in its own 2026-08-12 orientation note, before its design-lock
conversation. Purpose here is real-world grounding and candidate theory
options so Britton can make the same kind of design call he's made for the
other three papers.

## The real-world hook

**Flock Safety** is an Atlanta-based company whose automated license-plate-
reader (ALPR) camera network has spread to thousands of US cities, HOAs, and
police departments. Four real, documented controversy threads:

### 1. ICE/federal immigration data access — the dominant national story
- 4,000+ nationwide lookups conducted at federal government behest via
  Flock's network, described by the ACLU as "side-door access" without a
  formal ICE contract. Flock's admin panel reportedly has a one-click toggle
  comparing every plate read against the FBI's NCIC Immigration Violator
  file. [ACLU](https://www.aclu.org/news/privacy-technology/flock-roundup)
- **Syracuse, NY:** local data searched 4.4M times by outside police without
  warrants, shared with ICE despite prior promises otherwise.
- **Bend, OR:** 161-279 third-party lookups (CBP/ICE/HSI) in a few weeks.
- **Evanston, IL:** revoked outside access after 7 ICE searches despite a
  state law banning ICE data-sharing.
- **Richmond, VA:** cut off ATF after undisclosed immigration searches.
- A Texas officer reportedly used Flock to search nationwide for a woman who
  had had an abortion.
  [ACLU](https://www.aclu.org/news/privacy-technology/flock-pushback),
  [Star Tribune](https://www.startribune.com/police-search-immigration-twin-cities-flock-license-plate-cameras-ice-dhs-metro-surge/601807825),
  [Bend Source](https://www.bendsource.com/news/localnews/federal-immigration-officials-made-279-queries-into-bends-flock-safety-data-in-its-first-three-weeks/)
- **Flock's own public position** ("ICE does not have direct access... data
  is owned and controlled by the customer") sits in tension with its own
  internal indirect-access mechanism — a real, citable corporate-trust-
  violation narrative. Structurally close to Tariff Paper's dual-entitlement
  framing, but with Flock itself (not a diffuse government body) as the
  accountable brand — this may be the single cleanest "broken promise"
  storyline of any of the four papers.

### 2. Distributive/environmental-justice-style disparity
- **Christopher Newport University study** (Finn, Baird, Keener), Hampton
  Roads: Black neighborhoods surveilled at ~4x the rate of white ones; 75%
  of high-poverty tracts have a camera vs. <40% of low-poverty tracts; in
  70%-Black vs. 70%-white tracts, ~8x camera share relative to population
  share.
  [13newsnow](https://www.13newsnow.com/article/news/local/study-finds-flock-cameras-disproportionately-surveil-black-and-high-poverty-neighborhoods-in-hampton-roads/291-2507318e-ae53-4bd5-bff1-87ca89421b37),
  [WHRO](https://www.whro.org/business-growth/2026-01-20/flock-cameras-in-hampton-roads-surveil-black-communities-more-intensely-than-white-ones-cnu-study-says)
- Similar pattern independently reported in Tulsa, OK. Directly parallels
  Data Center Paper's Theme 1 (distributive/environmental injustice) —
  worth noting as a second paper where the same structural finding recurs,
  strengthening the case for it as a generalizable mechanism across very
  different infrastructure types, not a Louisiana-specific artifact.

### 3. Wrongful-stop/accuracy harms — vivid, high-salience
- **Toledo, OH:** a misread "7" as "2" led to a driver being mauled by a
  police K9 and jailed; $35,000 settlement.
- **LAPD:** internal audit found a 32.3% false-positive rate on stolen-
  vehicle flags (161 false alerts in two months); LA let its Flock contract
  expire July 2026.
  [IJ.org](https://ij.org/dozens-of-innocent-motorists-have-been-pulled-over-detained-at-gunpoint-or-jailed-due-to-ai-license-plate-camera-errors/)

### 4. Formal legal/regulatory fights and a large, growing rejection wave
- EFF + ACLU of Northern California sued San Jose (Santa Clara Co. Superior
  Court) on behalf of SIREN and CAIR-CA over warrantless ALPR searches —
  SJPD alone logged 3,965,519 searches in one year.
- A California class action against Flock directly (Gibbs Mura, filed Feb
  26 2026, amended Apr 3) over illegal sharing of Californians' movement
  data.
- Illinois Secretary of State launched an audit after EFF found CBP had
  accessed Illinois data in violation of state law.
  [EFF](https://www.eff.org/press/releases/lawsuit-challenges-san-joses-warrantless-alpr-mass-surveillance)
- **Municipal rejection wave, per the DeFlock tracker:** 95 cities rejected
  ALPR systems, 47 canceled contracts, 25 rejected proposals, 22 deactivated
  pending review, one full ban so far (Ypsilanti, MI). Named 2026 votes:
  Ord NE (5-0, first in Nebraska), Stoughton, Denver (unanimous contract
  rejection), Chandler AZ, El Cerrito CA (Mayor Pro Tem: "my biggest concern
  is the federal government could access the data"), Appleton WI (Mayor:
  "concerns about the integrity of Flock's underlying system have eroded
  our trust"), Bloomington IN, Tompkins Co./Ithaca/Saranac Lake NY,
  **Menominee, MI (cameras had been activated without council approval** —
  a direct secrecy/procedural-exclusion parallel to Data Center Paper's
  leading theme). League City, TX is putting it to a November voter
  referendum. [Newsweek map](https://www.newsweek.com/map-cities-rejected-deactivated-flock-cameras-12253499)

## Literature/novelty check — quick first pass only, not a deep scan

Found real policy/legal literature (Brennan Center, Congressional Research
Service, a SAGE criminal-justice-journal piece on ALPR security/privacy
tradeoffs, one qualitative study interviewing law-enforcement/Flock
stakeholders) — all policy/criminology-framed. **No evidence found that
marketing's existing contextual-integrity (Nissenbaum) or privacy-calculus
literature has been applied specifically to government/police ALPR
surveillance** — that literature's usual target is corporate/commercial
data collection, not police surveillance tech. Reads as a plausible real
gap, but **this was a shallow pass, not the deep multi-source scan Data
Center Paper got on 2026-08-16 — don't treat "looks novel" as confirmed
until a proper scan is run**, same standard as that paper.

## Candidate theoretical frames (pick one primary chain, not all of these)

Same recurring shape as Britton's other papers — antecedent → psychological
mediator → downstream outcome, often with a moderator:

1. **Contextual integrity violation** (Nissenbaum) — data flows to ICE or
   out-of-state agencies beyond the consented "local crime-solving" context
   → privacy-violation perception / institutional distrust → opposition
   intention (removal support, political mobilization), moderated by
   community immigration-enforcement exposure.
2. **Distributive injustice** — disproportionate camera placement in Black/
   high-poverty neighborhoods (directly evidenced by the CNU study) →
   perceived distributive injustice → reduced trust in local police/
   government → opposition. Near-exact structural transfer from Data
   Center Paper's Theme 1.
3. **Function creep / broken purpose-limitation promise** — sold as "find
   stolen cars," used for immigration/abortion-related searches →
   perceived corporate/institutional betrayal → distrust → opposition.
   Closest to Tariff Paper's dual-entitlement/trust logic, with Flock
   Safety itself as the accountable brand.
4. **Dread risk** (Slovic) — wrongful-detention incidents (Toledo) as
   vivid, involuntary, high-dread harms driving opposition independent of
   aggregate accuracy statistics.
5. **Procedural exclusion/secrecy** — cameras activated without council
   approval (Menominee), or ICE access discovered despite explicit
   no-sharing promises (Evanston) — a clean, direct parallel to Data
   Center Paper's leading theme, reinforcing cross-paper template reuse.

## Candidate venue fit

May be an *even cleaner* marketing-journal fit than Data Center Paper:
Flock Safety is a single identifiable corporate brand making public trust/
purpose-limitation promises to both government customers and citizens, then
visibly breaking them — closer to classic consumer-trust/corporate-
communication territory than Data Center's utility-regulator-heavy case.
**JPP&M** looks like the strongest fit — and would let Britton run a
consistent venue strategy across both this and Data Center Paper, worth
noting that pattern is forming across his pipeline. **Journal of Public
Policy** and **Journal of Consumer Affairs** are plausible policy-tilted
alternates; **Surveillance & Society** or **Big Data & Society** if he wants
a more critical/interdisciplinary framing instead; **Journal of Business
Ethics** stays viable given Flock is a clear corporate actor, not just
infrastructure.

## What's needed to move this forward

1. Britton picks a Study 1 corpus option — same A/B/C-style call as the
   other papers (corporate/Flock messaging vs. public/resident discourse vs.
   both paired). Given Flock is a much more identifiable, quotable corporate
   actor than a utility or oil company, Option A (or C) may be more viable
   here than it was for Data Center Paper.
2. Confirm which theory frame(s) to lead with — distributive injustice and
   procedural exclusion/secrecy are the two that most directly echo Data
   Center Paper's already-validated structure; function-creep/broken-promise
   is the most distinctively *this paper's own* angle.
3. Run a proper literature novelty scan (like the 2026-08-16 Data Center
   one) before locking design — this orientation pass's check was shallow.
4. Once a direction is picked, follows the same six-phase protocol as the
   other three papers.
5. Not yet checked: state-level legislative restriction detail (CA SB34,
   Virginia court rulings on ALPR searches) beyond confirming they exist —
   worth a follow-up pass if it matters for the Theory section.
