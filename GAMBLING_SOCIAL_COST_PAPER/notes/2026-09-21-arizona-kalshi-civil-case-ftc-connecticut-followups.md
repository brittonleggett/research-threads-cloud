# 2026-09-21 — Arizona/Kalshi "civil case" run down, FTC non-response recheck, Connecticut second-source confirmation, H.R. 10357 status recheck

This pass works the four concrete loose ends the 09-19 note left open, in the priority order it specified.
No design or scope decisions made — all findings below are flags for Britton, same as every prior pass.

## 1. Arizona's "separate civil case against Kalshi" — likely NOT a separate case; correcting the 09-19 note's reading

The 09-19 note read Mayes's Aug 28, 2026 press release as saying "Arizona has a separate, ongoing civil
case against Kalshi beyond the criminal charges" and flagged it as not yet located. Having now read that
press release's **exact verbatim text** directly (re-fetched this pass, quoted in full below), that
characterization looks like an overread of an ambiguous sentence — not a fabrication, but worth correcting
before it hardens into a project "fact."

**The actual sentence, verbatim**: "My office is reviewing today's opinion closely, including its
implications for our own ongoing litigation with Kalshi. I remain committed to enforcing Arizona's gaming
laws and will continue to defend the State's authority to do [so]." That is the entire relevant passage —
it does not say "civil case," does not say "separate," and does not say Arizona filed anything beyond what
was already known.

**What the litigation landscape actually looks like, reconstructed from primary and reputable secondary
sources this pass (azag.gov press releases read directly, Bloomberg, Courthouse News, DeFi Rate,
Tucson Sentinel, Covers.com, Bonus.com, AZ Mirror headlines)**:

- **March 12, 2026**: Kalshi filed a **preemptive federal civil suit against Arizona** (the case is
  captioned *KalshiEX LLC v. Johnson*, D. Ariz. — Johnson appears to be the Arizona Department of Gaming
  director being sued in an official capacity; caption not independently confirmed from a court filing
  this pass, only from secondary reporting that names it consistently), arguing the Commodity Exchange
  Act preempts Arizona's gambling law and that only the CFTC can regulate it.
- **March 17, 2026**: Arizona AG Mayes filed the 20-count **criminal** misdemeanor complaint (already
  well-documented in this project's prior notes).
- **April 2, 2026**: The CFTC itself filed its own federal complaint for declaratory/injunctive relief
  against Arizona (captioned around "Katie Hobbs" — Arizona's governor — per the CFTC's own hosted PDF at
  cftc.gov; I could not get clean text out of that PDF this pass — extraction tooling in this environment
  failed, see the technical note at the end — so I'm relying on secondary reporting, not the primary PDF,
  for this detail), consolidated with Kalshi's suit. This was filed the same week the CFTC also sued
  Connecticut and Illinois over similar prediction-market preemption disputes.
- **April 2026**: Judge Michael Liburdi (D. Ariz.) granted a **temporary restraining order** blocking
  Arizona's criminal prosecution.
- **May 5, 2026**: Liburdi converted that into a **permanent injunction**, ruling federal law preempts
  Arizona's gambling law as applied to CFTC-regulated derivatives exchanges — this is confirmed
  consistently across DeFi Rate, Tucson Sentinel, and Bonus.com/Covers.com reporting, though note one
  outlet (Covers.com, via this pass's fetch) called it a "preliminary injunction" while three others
  call it "permanent" and describe it as converting an earlier TRO — treating "permanent" as the better-
  supported reading given the 3:1 sourcing split and that it matches Liburdi's own quoted reasoning
  language ("federal law preempts state gambling laws insofar as they seek to regulate derivatives
  exchanged on markets regulated by the CFTC").
- **August 28, 2026**: The Ninth Circuit ruled the *opposite* way in a **different case** — *KalshiEX,
  LLC v. Assad* — which is about **Nevada**, not Arizona (Assad appears to be a Nevada gaming regulator).
  The Ninth Circuit held the CEA does *not* preempt state authority. AZ Mirror's own headline on this
  ruling is direct about the implication: "9th Circuit sides with states in Kalshi gambling fight,
  **potentially reviving Arizona's prosecution**" (I could not get past a 403 to read that AZ Mirror
  article's body text this pass, so I'm citing its headline only, not its full content).

**Bottom line for the project**: there is no independently-confirmed evidence of a *separate* civil suit
that Arizona itself filed against Kalshi. What exists is (a) the criminal case, currently under a federal
permanent injunction, and (b) the federal preemption litigation (*KalshiEX v. Johnson*, consolidated with
the CFTC's own suit) in which **Arizona is a defendant, not a civil plaintiff** — Kalshi and the CFTC sued
Arizona, not the reverse. Mayes's "our own ongoing litigation with Kalshi" line most plausibly refers to
that same preemption case, now newly favorable to Arizona's position post-Ninth-Circuit, not a new or
separate action. **Recommend the project's characterization be corrected from "separate civil case" to
"the federal preemption suit, in which Arizona is a defendant" if this shows up in any future manuscript
text or summary.** If Britton has PACER/Westlaw access, confirming the *KalshiEX v. Johnson* docket
directly (case number, current posture post-Ninth-Circuit) would fully close this out — this is exactly
the kind of case-caption/docket precision this project's own rules ask not to guess at.

**For the paper's mechanism**: this is genuinely interesting context (a live, unresolved circuit-level
tension between a district court's preemption ruling for Arizona specifically and the Ninth Circuit's
anti-preemption ruling in a sibling Nevada case), but it's about prediction markets/Kalshi specifically,
not sports-betting-operator policy stringency — same tier of relevance as previously scoped (background/
motivation material, not core panel data).

## 2. FTC non-response — still no response found

Rechecked via direct search of ftc.gov's press release listing and multiple targeted searches. **No FTC
response to the June 3, 2026 Mullin/Vasquez letter (9 House members, response requested by June 29, 2026)
has been found**, publicly or otherwise, as of this pass (2026-09-21) — nearly three months past the
requested deadline. FTC's own press release page (fetched directly) shows August-September 2026 releases
on FleetCor, Amway, Amazon Prime, firearm manufacturers, auto dealers, payment processors, and healthcare
mergers — nothing on prediction markets, Kalshi, Polymarket, or a response to Congress on this topic.
Kevin Mullin's own House website (which would be the most likely place to trumpet a response, favorable or
not) also shows no update since the original June 3 announcement. Treat as **still unanswered, genuinely
unresolved** — same status as 09-19, not a new finding, just a confirmed recheck. Worth another pass in a
few weeks if the project keeps tracking this thread; either a response or a continued silence past 90 days
would be a citable, dated fact for a regulatory-landscape paragraph.

## 3. Connecticut §12-867 — genuine second independent source found; upgrading from single-mirror to two-source confirmation

Per the assignment, tried routes other than cga.ct.gov (still 503s — confirmed again this pass, a third
consecutive hard wall) and Justia (not re-tried, per instruction to try a genuinely different route) and
codes.findlaw.com (already used 09-19, not re-used as the "second" source).

**Found a strong, genuinely independent second source: Connecticut's own official open-data portal**
(data.ct.gov, mirrored at catalog.data.gov/data.gov — a different Connecticut state server than
cga.ct.gov, so the .gov hard-wall problem is server-specific, not domain-wide). The dataset "Selected
Online Sport Wagering Data" carries this as an official methodology note in its own metadata (quoted
verbatim, note 6 of 7): **"Per Public Act 21-23, from October 2021 – September 2022 the promotional
deduction is limited to the lesser of 25% of sports wagering Win/Loss, or actual promotional coupons or
credits wagered. From October 2022 – September 2023 this limit drops to 20%, and to 15% thereafter."**
This is the same 25/20/15 figures the 09-19 note confirmed via the findlaw mirror of §12-867 — now matched
independently — and it explicitly ties the figure to the *sports wagering* dataset specifically (not
casino gaming), and cites the actual enacting law (**Public Act 21-23**, i.e. Substitute House Bill 6451,
signed by Gov. Lamont in 2021) rather than just the codified section number. The same metadata note also
gives the 13.75%-of-Gross-Gaming-Revenue payment rate, matching findlaw's §12-867 rendering exactly, and
confirms coupons/credits must be "issued for use for gaming in the state and redeemed in the State of
Connecticut" to count toward the deduction.

A third, independent journalism source (insideinvestigator.org, "Online gambling promotions cost
Connecticut millions") corroborates the same phase-down structure with real dollar figures: **$12.4
million in sports-wagering promotional deductions Jan–Jul 2022 alone ($1.7M in foregone state revenue)**,
plus $29.8M in online-casino-gaming deductions ($5.3M foregone) over the same window — independently
sourced to Connecticut's open-data site per that article's own account, not to the findlaw mirror.

**I still could not get a clean direct read of cga.ct.gov itself or the actual enrolled Public Act 21-23
PDF (hosted at cga.ct.gov/2021/ACT/PA/pdf/2021PA-00023-R00HB-06451-PA.pdf) — that PDF URL also 503'd this
pass.** So this is not a primary-statute-text read; it's now two independent sources (a verbatim statute
mirror, findlaw, from 09-19, plus the state's own official open-data metadata this pass) agreeing on the
same figures and citing the same public act, which is a real, meaningful upgrade from "one mirror site"
but still short of reading the enrolled bill or the statute on Connecticut's own primary server. Updated
`policy/state_policy_variables.md`'s Connecticut row accordingly (see below).

## 4. H.R. 10357 — no movement since 09-19; recheck confirms status quo

Rechecked via fresh search. **Status unchanged**: cleared the House Ways & Means Committee 38-5 on
September 16, 2026 (as part of the broader Digital Asset Tax Certainty Act package), now before the House
Rules Committee before it can reach the floor, and **lawmakers are still not expected to hold a floor vote
until after the November 2026 midterms** — consistent across fresh Sept 2026 coverage (Covers.com,
Hoodline, Las Vegas Sun, Yogonet, BettingNews, LegalSportsBetting.com, HorseRacingNation, Paulick Report,
all reporting the same 38-5 committee vote and the same post-midterm floor-vote expectation). One added
data point not previously in this project's notes: the Joint Committee on Taxation's own estimate is that
restoring the full 100% deduction would **reduce federal tax revenue by roughly $2 billion over the
2027–2036 window** — a real, citable fiscal-cost figure if this bill ever becomes relevant to the paper's
framing. No design implication drawn from this — informational only, per the standing rule.

## Technical note: PDF extraction failed again this pass

Consistent with this project's recurring pattern (Coombs/Madonia/Nencka/Smith, Michigan's legislature
site, the AGA guide, the Mullin/Vasquez FTC letter, Iowa's 99F.11), two PDFs (the CFTC's Hobbs complaint,
the AGA's Connecticut regulatory fact sheet) could not be read via WebFetch's own extraction. Unlike some
prior passes, **the local `pdftotext` workaround that worked previously was not available in this specific
session's environment** (no `poppler-utils`, no working Python PDF library — both `pip install pypdf` and
`apt-get install poppler-utils` failed in this sandbox, the latter on a package-repo 404). This is an
environment/tooling gap for this session specifically, not a finding about the documents themselves —
flagging so a future pass doesn't assume the workaround is always available.

## What's still open / unresolved after tonight

- **Arizona's actual *KalshiEX v. Johnson* docket** has not been read directly (PACER/court-site access,
  not this session's tools) — would confirm the exact caption, case number, and current post-Ninth-Circuit
  posture. This is the cleanest way to fully resolve item 1 above.
- **FTC non-response** — recheck again in a few weeks; either an eventual response or continued silence
  past 90 days becomes more citable as time passes.
- **Connecticut** — a Westlaw/Lexis query or a working direct cga.ct.gov fetch (by Britton, or a future
  session when the server isn't 503ing) would still be the cleanest way to fully close this out; two
  independent non-primary sources agreeing is good but not the same as reading the statute itself.
- **H.R. 10357** — no floor vote expected before the November midterms; next natural check-in point is
  after the midterms.

No fabricated citations, case names, dockets, or figures were introduced this pass. Where a route was
genuinely blocked (cga.ct.gov 503, the CFTC PDF, the AZ Mirror article behind a 403), that is stated
plainly above rather than worked around with an unverified guess.
