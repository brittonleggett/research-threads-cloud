# 2026-09-20 — IL Mahomet Aquifer effective date confirmed (Jan 1, 2026); Terwel/de Best-Waldhober literature lead identified and clarified (three distinct Terwel papers, none open access); standing litigation rechecks (POET v. Wabash, ND amalgamation, CA Shafter, LA Save My Louisiana) all unchanged

**AI involvement disclosure:** this note was produced by an AI agent (Claude) doing autonomous
overnight verification work on this repo, per the project's standing conventions. All claims below
are labeled by source type (primary/secondary/AI-search-summary) as found tonight; nothing here was
fabricated, and anything not independently confirmed is flagged as such. No theory-chain, Phase-3,
or design decision was made — this is verification legwork only, per this project's standing
human-only-Phase-3 rule.

**Orientation:** read the repo README, `CCS_PAPER/README.md` (no `CLAUDE.md` exists in this project
folder — checked directly, only `README.md`), and the newest `notes/` file (2026-09-18, POET v.
Wabash pull attempt + litigation recheck) before starting. Tonight's assignment per that note's open
items: prioritize (3) IL Mahomet Aquifer effective-date confirmation and (4) the Terwel/de
Best-Waldhober literature lead — both genuinely new ground — plus quick standing rechecks of (1)
POET v. Wabash, (2) ND amalgamation appeal, (5) CA Shafter / LA Save My Louisiana.

**Environment note:** `ilga.gov` (the Illinois General Assembly's own site) was fully unreachable
tonight across every URL pattern tried — `Legislation/BillStatus`, `Legislation/PublicActs/View`,
and the PDF itself all returned either HTTP 503 (via WebFetch) or a raw TLS handshake failure
(`SSL_ERROR_SYSCALL`, via direct `curl` through the environment's proxy). This is a different, more
total failure mode than the 09-08 note logged (which successfully pulled the same PDF directly from
`ilga.gov` that night). Worked around it via the Wayback Machine's archived copy (see below) — flagging
in case `ilga.gov` accessibility is worth checking again in a future session rather than assuming
this pattern persists. Also needed to reinstall `cffi` again before `pypdf` would import (same
recurring tooling quirk the 09-07/09-08 notes flagged — PDF tooling availability varies session to
session; `pdftotext`/poppler-utils was not installed this time, `pypdf` was used instead after the
`cffi` fix).

---

## 1. Illinois Mahomet Aquifer ban (Public Act 104-0119 / SB1723 Enrolled) — effective date now confirmed as January 1, 2026

**Bottom line: primary-source-grounded confirmation that the Act's effective date is January 1, 2026**,
closing the open item logged 09-08. This wasn't a single document stating "effective January 1, 2026"
outright — it's a convergence of two things I verified independently tonight:

**(a) The Act's own text contains no effective-date override.** Since `ilga.gov` was unreachable live,
I pulled the enrolled Public Act PDF from the Internet Archive's Wayback Machine
(`web.archive.org/web/20251224061528/https://www.ilga.gov/Documents/Legislation/PublicActs/104/PDF/104-0119.pdf`
— a snapshot from Dec 24, 2025, of the same file the 09-08 note already primary-verified the substance
of) and re-extracted all 9 pages with `pypdf`. I searched the full extracted text specifically for a
"Section 99. Effective date" clause (the standard place Illinois enrolled bills specify an
earlier-than-default effective date, or "effective immediately" language) — **there is none.** The
only "effective date" references in the text (lines 115, 185 of the extraction) are internal
cross-references ("...effective date of this amendatory Act of the 104th General Assembly...", used
to set the Mahomet Aquifer Advisory Study Commission's 90-day first-meeting deadline), not a
Section-99-style declaration. PDF metadata (`/CreationDate: D:20250804160100-05'00'`) still shows the
Aug 4, 2025 processing date the 09-08 note already found — consistent, not new, but re-confirmed
independently tonight from a different copy of the file.

**(b) Illinois's own default effective-date statute resolves the date given (a).** Illinois's
"Effective Date of Laws Act" (5 ILCS 75/1) provides — quoted via FindLaw's mirror of the Illinois
Compiled Statutes, since the `ilga.gov`-hosted original was unreachable tonight — that *"A bill passed
prior to June 1 of a calendar year that does not provide for an effective date in the terms of the
bill shall become effective on January 1 of the following year, or upon its becoming a law, whichever
is later."* SB1723 passed the Illinois House 91-19 on May 20, 2025 (already logged, secondary-sourced,
in the 09-08 note) — **before** June 1 — and was signed by Gov. Pritzker Aug 1, 2025 (also already
logged) — well before Jan 1, 2026. Both conditions of the default rule are met, and neither trigger for
an earlier date (no Section 99 clause, no supermajority immediate-effect vote found) applies. That
makes the default outcome **January 1, 2026**, which matches — and now independently corroborates
rather than just repeats — the Illinois State Bar Association's secondary reporting the 09-08 note
had already flagged as unconfirmed.

**Residual caveat, stated plainly:** I did not find a document that says "effective January 1, 2026"
in so many words issued directly by `ilga.gov` itself (unreachable all session) — this is a reasoned
primary-source conclusion (the Act's own text + the statute FindLaw quotes) rather than a single
explicit government statement. I'm confident in it, but if Britton wants the last mile of certainty,
the live `ilga.gov` Public Act view page sometimes displays an "Effective Date" field directly in its
UI (separate from the PDF text) — worth a 30-second check next time that site is reachable, though I
don't think it's likely to contradict this.

## 2. Terwel/de Best-Waldhober literature lead — identified, but the description doesn't map onto a single paper; three real, distinct Terwel et al. papers exist, all paywalled

The 09-18 note flagged an unverified lead: a "Terwel/de Best-Waldhober-line paper" on how
"organizational motives and communications affect public trust" in CCS, comparing government/
industry/NGO actors, with Dutch respondents trusting NGOs more than industry. Tonight I chased this
down properly rather than leaving it as a search-summary claim. **Important finding: there isn't one
paper here — there are at least three real, distinct Terwel et al. papers that are easy to conflate,
plus a fourth that's a genuine Terwel + de Best-Waldhober co-authorship but on an unrelated topic.**
Documenting all four clearly so nobody (human or AI) merges them by mistake in a future citation pass:

1. **Terwel, Harinck, Ellemers & Daamen (2009), *Journal of Environmental Psychology* 29(2), 290–299,
   "How organizational motives and communications affect public trust in organizations: The case of
   carbon dioxide capture and storage," DOI 10.1016/j.jenvp.2008.11.004.** This is the one that best
   matches the 09-18 lead's description. **Confirmed real** via Semantic Scholar's API, ScienceDirect's
   own abstract page, ResearchGate, and Leiden University's own staff-publication listing for
   co-author Fieke Harinck (which lists it with no full-text link attached). Per an AI search-summary
   of the abstract (not a verified direct quote — flagging that distinction explicitly, same caution
   the 09-18 note used for its own lead): Study 1 (N=264) reportedly found Dutch citizens trust
   industrial organizations less than environmental NGOs involved in CCS, with the gap explained by
   *inferred organizational motives* (organization-serving vs. public-serving) rather than message
   content alone. **Not open access** — Semantic Scholar's API explicitly returns
   `openAccessPdf.status: "CLOSED"` for this DOI, and ScienceDirect requires purchase. I did not
   download or store anything for this one, consistent with this repo's no-paywalled-PDF rule.
2. **Terwel, Harinck, Ellemers & Daamen (2011), *International Journal of Greenhouse Gas Control*
   5(2), 181–188, "Going beyond the properties of CO2 capture and storage (CCS) technology: How trust
   in stakeholders affects public acceptance of CCS," DOI 10.1016/j.ijggc.2010.10.001.** Also
   **confirmed real** (Semantic Scholar, ScienceDirect, ResearchGate all agree on the citation). Its
   title alone suggests it may actually be **more directly on-point** for the implementing-body/
   operator-type open item than paper #1 — it's explicitly framed around stakeholder trust as a
   distinct acceptance driver beyond the technology's own properties, which is closer to what the
   Anders et al. (2024) implementing-body-constant design choice is about. I could not get an
   abstract for this one (ResearchGate blocked the fetch tonight, HTTP 403) so I can't characterize
   its findings even at second-hand — just confirming it exists and is on-topic by title. **Also not
   open access** — Semantic Scholar's API also returns `openAccessPdf.status: "CLOSED"` for this DOI.
   **If Britton wants one paper pulled via his own library access to move this open item forward,
   this is my recommendation over paper #1.**
3. **NOT the same as the Terwel et al. 2009 paper already cited in
   `Conceptual_Model_and_Theory_v2_DRAFT_2026-09-08.md`** for the institutional-trust mediator's
   competence/integrity split. That citation is a **third, separate paper**: Terwel, Harinck, Ellemers
   & Daamen (2009), *Risk Analysis* 29(8), 1129–1140, "Competence-Based and Integrity-Based Trust as
   Predictors of Acceptance of Carbon Dioxide Capture and Storage (CCS)." Same four authors, same
   year, **different journal**, easy to accidentally merge with paper #1 above — flagging this
   explicitly so a future pass doesn't conflate "the trust-scale source already in the design" with
   "the new organizational-trust lead."
4. **A genuine Terwel + de Best-Waldhober co-authorship does exist** — Brunsting, de Best-Waldhober &
   Terwel (2013), *Energy Procedia* 37, 7419–7427 (GHGT-11 conference proceedings), "'I reject your
   reality and substitute my own'. Why more knowledge about CO2 storage hardly improves public
   attitudes." Confirmed real via OSTI's ETDEWEB bibliographic record (which gave a working abstract)
   and independently via WebSearch/CyberLeninka/CORE listings. Energy Procedia's GHGT proceedings are
   genuinely open-access (Elsevier's open archive for that series), and OSTI's record actually
   supplied a candidate free-PDF link — but the link resolves to a legacy conference file server
   (`eventsinteractive.com`) that returned HTTP 503/an SSL error both via WebFetch and `curl` tonight,
   so I could not actually retrieve or read it. **More importantly, per OSTI's own abstract, this
   paper's topic is whether CCS-knowledge-test scores predict attitude change — not organizational
   trust, not government/industry/NGO comparison, not operator type.** So despite being the one real
   Terwel/de Best-Waldhober pairing I could confirm, it does not appear to be the paper the 09-18
   lead was actually describing, and isn't a good fit for the implementing-body-constant question
   regardless of its access status.

**Bottom line on this item:** the 09-18 lead most likely refers to paper #1 (or possibly #2) above,
not a literal Terwel+de Best-Waldhober co-authored piece — "Terwel/de Best-Waldhober-line" was
probably describing the same Dutch CCS-social-science research cluster rather than one specific
co-authorship, and that description turned out to be imprecise once checked against the real
literature. **None of papers #1 or #2 were read tonight** — both are paywalled (Elsevier), confirmed
via Semantic Scholar's own open-access-status field, not just inferred from a paywall hitting a
browser. Nothing was downloaded or stored. This closes the "verify it's a real paper" half of the
open item; the "read/summarize if accessible" half remains blocked on library access, same as the
already-cited Sovacool/Chailleux/Lefstad items in Section 8.6 of the conceptual model doc.

## 3. Standing rechecks (quick only, per instruction not to over-invest)

- **POET v. Wabash County (IN):** one quick attempt at CourtListener's docket page tonight —
  `courtlistener.com/docket/72366283/...` returned **HTTP 403** via WebFetch (the 09-18 session had
  gotten through to the HTML page itself, just found no free RECAP copies within it; tonight the page
  didn't load at all). Same underlying conclusion either way: no free copy available, no PACER
  credentials in this environment. Did not re-run the full multi-path effort from 09-18, per standing
  guidance. One unverified, secondary detail surfaced in a WebSearch synthesis tonight — a claim that
  "PACER systems underwent maintenance from September 18–20, 2026" — I'm flagging this explicitly as
  an **AI-search-summary claim I could not corroborate against any primary PACER source**, not
  something to treat as fact; it may or may not explain tonight's access trouble, or may be an
  artifact of the search summarization itself. Not worth chasing further tonight.
- **ND amalgamation appeal:** one quick re-check, `ndcourts.gov/supreme-court/opinions` — still
  **HTTP 403**, same bot-check block logged every session since ~09-05. No further attempt made,
  per standing guidance (this is now the 8th+ consecutive session blocked).
- **CA Committee for a Better Shafter v. County of Kern:** WebSearch found nothing dated later than
  the already-logged 2024 CEQA ruling and prior coverage. No new ruling found — still pending,
  unchanged.
- **LA Save My Louisiana eminent-domain suit (19th JDC):** WebSearch found the same already-logged
  coverage set (Louisiana Illuminator, American Press, Rapides Parish Journal, legalnewsline.com). No
  ruling reported — still pending, unchanged.

---

## What changed vs. what didn't

- **Newly resolved:** IL Mahomet Aquifer ban's effective date — January 1, 2026, via primary-source
  reasoning (Act's own text + Illinois's default effective-date statute), corroborating rather than
  just repeating the secondary ISBA source already logged 09-08.
- **Newly clarified (not a new grounding source, a disambiguation):** the "Terwel/de Best-Waldhober"
  lead maps most plausibly onto Terwel, Harinck, Ellemers & Daamen (2009, J. Environ. Psychol.) and/or
  the same authors' 2011 IJGGC paper — both real, both confirmed paywalled, neither read tonight. A
  genuine Terwel+de Best-Waldhober co-authored paper exists (Brunsting et al. 2013, open access) but
  is off-topic for this question. Flagged which of the two on-topic candidates (the 2011 IJGGC paper)
  looks like the stronger pull if Britton wants to spend his own library access on one of them.
- **Unchanged, reconfirmed:** POET v. Wabash (still no free copy, still no PACER access), ND
  amalgamation appeal (still blocked), CA Shafter (still pending), LA Save My Louisiana (still
  pending).
- **No theory-chain, Phase-3/theme, or design decision was touched.** Nothing here picks the
  implementing-body-constant choice one way or the other — the literature-identification work above
  is legwork for Britton's eventual judgment call, same framing as the 09-14 note.

## What's still open

1. **Terwel et al. (2011, IJGGC) and/or (2009, J. Environ. Psychol.)** — real, on-topic, paywalled;
   need Britton's library access to actually read either. Recommend the 2011 paper first if only one
   gets pulled.
2. **POET v. Wabash amended complaint / second SJ round** — still unread; hard PACER/RECAP wall,
   unchanged from 09-18. Not worth another full-effort pass without a credentialed PACER path.
3. **ND amalgamation appeal** — still structurally blocked; one quick check per session remains the
   right cadence.
4. **CA Shafter and LA Save My Louisiana** — both still pending, no ruling either way.
5. **Brunsting, de Best-Waldhober & Terwel (2013) open-access PDF** — the specific mirror link found
   tonight (`eventsinteractive.com`) was unreachable; if genuinely useful later (it currently doesn't
   look on-topic for the operator-type question), a future pass could retry that link or search for
   another host of the same open-access Energy Procedia article.
