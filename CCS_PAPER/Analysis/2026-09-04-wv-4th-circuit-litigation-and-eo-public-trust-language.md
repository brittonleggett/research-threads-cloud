# 2026-09-04 — WV 4th Circuit litigation (deep dive) + EO "public trust" language (primary-source pull) + light lit-gap scan

## What this is
Following up on the 09-03 refresh pass's two flagged-but-undeveloped threads. Both fully worked tonight.
Method: primary-source PDF extraction (project's own corpus PDF for the EO; the actual court filings for
the litigation, pulled via WebFetch and locally re-extracted with `pdfminer.six` when WebFetch's own PDF
parse failed) plus WebSearch corroboration. Everything below is sourced; anything not independently
confirmed is flagged as such.

---

## 1. West Virginia's 4th Circuit litigation — deep dive

### The actual case (now fully identified)

**West Virginia Surface Owners' Rights Organization, Sierra Club, West Virginia Rivers Coalition, Inc.,
and West Virginia Highlands Conservancy v. Lee Zeldin (EPA Administrator) and Amy Van Blarcom-Lackey
(EPA Region III Administrator)**, with the **State of West Virginia and the West Virginia Department of
Environmental Protection as Intervenors-Respondents**. **4th Circuit, No. 25-1384.** On petition for
review of a final EPA action, EPA docket No. EPA-HW-OW-2024-0357 (EPA approved WV Class VI primacy Feb.
26, 2025; petition filed April 11, 2025; 4th Circuit granted WV/WVDEP's motion to intervene May 9, 2025).
Petitioners are represented by Amanda Demmerle and Derek O. Teaney of Appalachian Mountain Advocates.

This is directly confirmed from the **actual "Petitioners' Rule 30(c) Page Proof Brief"** in the case
(PDF, dated/certified filed **January 21, 2026**), located via WebSearch and re-extracted locally with
`pdfminer.six` after WebFetch's built-in PDF parser choked on it (source:
https://cdn.climatepolicyradar.org/navigator/USA/2025/west-virginia-surface-owners-rights-organization-v-zeldin_40d11b22c2c9dc9166219a7d3c4a6d09.pdf).
**Correction to the 09-03 note:** that note called this a "reply brief filed May 20, 2026" per paywalled
InsideEPA coverage — the document I actually pulled and read is titled *Petitioners'* brief (not a reply
brief) and is dated January 21, 2026. I did not find and cannot confirm a separate May 20, 2026 reply
brief independently; it may exist as a later filing InsideEPA saw that I didn't find, or the note's date/
characterization may be off. Flagging rather than reconciling — don't cite "May 20, 2026 reply brief" as
confirmed.

### The legal theory, in detail

Two issues presented (verbatim from the brief's Statement of Issues):
1. Whether EPA arbitrarily and capriciously determined that West Virginia "will implement" its Class VI
   program effectively and consistent with the Safe Drinking Water Act (SDWA).
2. Whether EPA violated the SDWA when it approved WV's primacy application even though WV's program
   "violates federal laws and is less stringent than EPA's program."

Core substantive claim: WV's **liability-transfer and "amalgamation" provisions** make the state program
less stringent than the federal Class VI baseline (SDWA primacy requires a state program be "at least as
stringent as" federal regulation, 40 C.F.R. §145.11(b)(1)). Petitioners also point to WV's track record
under its existing Class II (oil/gas) UIC primacy — in place since 1983 — as evidence the state won't
adequately staff/enforce Class VI oversight (cited concern: ~18 inspector positions covering roughly
75,000 wells, per the Dominion Post's May 2025 reporting on the underlying petition).

**The standing theory — this is the structurally distinctive and most citable part** — and it turns out
to connect directly to Louisiana:

The brief spends its opening section (before even the Statement of Issues) making an Article III standing
argument, because the petitioners are explicitly trying to avoid the fate of an almost-identical
Louisiana case. Direct quote from the brief: *"Although the Fifth Circuit recently held that several
environmental organizations lacked standing to challenge EPA's approval of Louisiana's Class VI program,
see Deep South Center for Environmental Justice v. EPA, 138 F.4th 310, 320–26 (5th Cir. 2025), Petitioners'
injuries are materially different from those the Fifth Circuit found lacking."*

The brief then argues three distinguishing factors: (1) WV petitioners assert no *organizational*
injuries (unlike Deep South's "diversion of resources" theory, which failed); (2) they don't rely on
higher future utility bills as an injury (unlike Healthy Gulf/Alliance for Affordable Energy in the LA
case); (3) — "most importantly" — they assert a **procedural injury tied to a specific conflict-of-interest
theory**: that EPA's approval installs "a decisionmaker with a pecuniary interest" (the State of WV, which
petitioners argue benefits financially from CCS buildout) in charge of permitting, which they argue is a
*predictable*, non-speculative harm distinct from the "highly attenuated chain of possibilities" the
Fifth Circuit rejected in the Louisiana case.

### The Louisiana precedent this is answering — new finding, not in the 09-03 note

**Deep South Center for Environmental Justice, Healthy Gulf, and Alliance for Affordable Energy v. EPA,
No. 24-60084 (5th Cir., decided May 21, 2025), reported at 138 F.4th 310.** Panel: Circuit Judges Graves,
Engelhardt, and Oldham; opinion by Judge Oldham; Judge Graves concurred in the judgment only (found the
majority opinion "overstated"). I pulled and read the **official slip opinion directly from the Fifth
Circuit's own site** (https://www.ca5.uscourts.gov/opinions/pub/24/24-60084-CV0.pdf, re-extracted locally
after WebFetch's parser failed on it) — this is a primary source, not a summary.

This is the case where EJ groups petitioned for review of **EPA's 2024 grant of Class VI primacy to
Louisiana itself** — the same underlying regulatory action-type as the WV case, just for Louisiana. The
Fifth Circuit dismissed for lack of standing. Opening lines of the opinion, quoted exactly: *"In 2024, the
Environmental Protection Agency granted the State of Louisiana primary enforcement authority over a class
of underground carbon sequestration wells. Three environmental organizations petitioned for review of the
final rule granting that authorization. All three lack standing. We therefore dismiss the petition."*
Holding, quoted: *"Because all three petitioners fail to demonstrate Article III standing, the petitions
for review are DISMISSED."*

Key reasoning on Deep South's claimed injury (staff time/resources diverted to opposing the buildout,
~850 hours of "education and advocacy"): the court held this was **self-inflicted and not cognizable** —
quoted: *"Deep South's opposition to EPA's action, no matter how intense, amounts to 'a setback to \[its\]
abstract social interests,' which has never sufficed to confer standing."* Healthy Gulf and Alliance for
Affordable Energy's claimed injuries (higher future energy costs, future well mishaps) were held **too
speculative/attenuated** on both injury-in-fact and traceability grounds.

One footnote is worth flagging for the paper's comparative-stringency angle: the Fifth Circuit noted, in
dicta, that Louisiana's Class VI standards "generally mirror the federal regulations but are more
stringent in some ways" (per the state intervenor's brief, uncontested by petitioners on this point) —
the inverse of WV petitioners' central *less*-stringent claim. That's a genuine substantive difference
between the two states' programs as litigated, not just a standing-theory difference.

### Current status (and an unresolved discrepancy with the 09-03 note)

- Briefing: petitioners' brief filed/dated January 21, 2026 (confirmed, primary source). A more recent
  secondary source — Arnold & Porter's "CCUS State Update 2026" blog post, dated May 2026
  (https://www.arnoldporter.com/en/perspectives/blogs/environmental-edge/2026/05/ccus-state-update-2026)
  — states briefing **concluded in April 2026** and that **oral argument had not yet been scheduled** as
  of that post. EPA's response reportedly leaned on standing; WV intervened as respondent; amicus briefs
  were filed by industry groups and a coalition of nine states (per that same source, not independently
  verified beyond the summary WebFetch returned).
- I could not find any source — primary or secondary — confirming the 09-03 note's "oral arguments
  tentatively late October 2026." The most recent and most reliable secondary source I found (a law-firm
  blog dated after the note's presumed InsideEPA source) says argument was *not yet scheduled* as of
  May 2026. **Treat "late October 2026" as unconfirmed, possibly stale or paywall-source-specific — don't
  repeat it as fact without a fresher check closer to any actual write-up.**
- No decision, obviously, since no argument date is confirmed.

### Assessment: how this serves as a national comparison case

This is a stronger three-way comparative structure than "Louisiana eminent-domain suit vs. WV standing
fight" — it's actually a **sequential same-theory pair with a documented precedent relationship**:

1. **Louisiana — "Save My Louisiana" eminent-domain suit** (state court, 19th JDC, filed Nov 2025):
   *takings/property-rights* theory — plaintiffs as landowners subject to eminent domain for CO2 pipelines/
   pore space.
2. **Louisiana — Deep South Center v. EPA** (federal, 5th Cir., decided May 2025): *EJ-standing* challenge
   to the primacy grant itself — **failed**, dismissed on Article III grounds before reaching the merits.
3. **West Virginia — WVSORO v. Zeldin** (federal, 4th Cir., pending, No. 25-1384): the **same EJ-standing
   theory**, in a different circuit, with petitioners' own brief explicitly citing and trying to
   distinguish Deep South to avoid its fate, plus a substantive stringency claim.

For the paper, this gives a genuinely citable claim: **the EJ-standing route to challenging state Class VI
primacy has already been tried once (Louisiana) and failed on standing before reaching the merits, and a
second attempt is underway in a different circuit using a narrower, more specific injury theory
(pecuniary-interest-of-the-decisionmaker) explicitly designed to survive that precedent.** That's a much
richer national/legal-landscape point than "two different lawsuits in two states" — it's evidence of an
evolving, precedent-aware EJ litigation strategy, which fits a trust/legitimacy theory frame (both cases
turn on who the public can trust to police a self-interested permitting authority) better than a bare
comparison would. Recommend Britton consider citing both cases together rather than WV alone.

**Caveat:** the "pecuniary interest" framing quoted above is the *petitioners'* characterization of their
own theory (from their own brief) — it hasn't been tested by the 4th Circuit, and it explicitly has not
yet had oral argument. Don't present it as an established or credited legal theory, only as the theory
being argued.

---

## 2. Executive Order "public trust" language — primary-source pull, with a naming correction

### First, a correction the paper needs: there is no "Executive Order B-2025-01"

I opened the project's own corpus PDF — `CCS_PAPER/Corpus_1/Department-Directive-Order-No-B-2025-01-
combined.pdf` — and extracted its full text locally (`pdfminer.six`; WebFetch/Read's built-in PDF handling
wasn't available in this environment — poppler-utils couldn't be installed and pypdf's crypto backend was
broken, so I installed `pdfminer.six` + `cffi` via pip and extracted directly). It's a **39-page combined
PDF containing three distinct documents**, not one:

1. **Executive Order Number JML 25-119**, "CO₂ Capture and Storage Limits and Moratorium" — issued by
   **Governor Jeff Landry** ("NOW THEREFORE, I, JEFF LANDRY, Governor of the State of Louisiana...").
   This is the actual Class VI moratorium the project's notes have been calling "Executive Order
   B-2025-01" — **that name is wrong; the EO's real number is JML 25-119.**
2. **Department Guidance No. B-2025-01 (Rev. 1)** — issued by **Tyler Gray, Secretary** of the Department
   of Energy and Natural Resources (DENR/DCE), dated **September 1, 2025**. This is a sub-regulatory
   guidance document, not an executive order, and not signed by the Governor.
   "B-2025-01" is *this* document's number, and its predecessor (Department Directive Order No. B-2025-01,
   original, dated August 1, 2025) — a third, separate document also in the same combined PDF.

So "B-2025-01" and the Governor's Executive Order are two different documents that happen to be bundled
into one corpus PDF file whose filename conflates them. **For any citation in the manuscript, the
Governor's moratorium order should be cited as Executive Order Number JML 25-119 (Office of the Governor,
State of Louisiana), not "B-2025-01."** I could not extract a precise signing date from the PDF text
itself — the signature/seal page (page 11 of the combined PDF) extracted as empty, almost certainly
because the signature/date block is a scanned image, not text, and this environment has no OCR tooling
available. The Oct 15, 2025 date the project's notes already carry (from two independent live-source
checks per the 09-03 note) is still the best available date; I did not re-verify it tonight beyond
confirming it's not contradicted by anything in the PDF text.

### The actual "public trust" language — and it's not the exact phrase the 09-03 note quoted

I searched the full extracted text of the EO for "public trust," "foster," and "erode." Found: **"foster"**
appears twice, **neither** adjacent to "public trust." **"Erode"/"erodes"/"eroding" does not appear
anywhere in the 39-page combined document at all.** So the specific quoted phrase in the 09-03 note —
'"foster\[s\] or erode\[s\] public trust"' — **does not exist verbatim in this primary source.** I can't
verify it; treat it as unconfirmed and don't put it in quotation marks in the manuscript.

What the EO **actually** says (page 4 of the combined PDF, part of Executive Order JML 25-119's WHEREAS
clauses), extracted directly and quoted exactly:

> "WHEREAS, to support balanced economic growth and safeguard public trust, I, as Governor, have heard the
> concerns of citizens and communities and am stepping in to require agencies to work together—
> particularly the Department and Louisiana Economic Development ('LED') to: A. Evaluate economic
> potential for projects associated with Class VI applications... B. Ensure a process to incorporate
> stakeholder input from businesses, industry associations... [etc.]"

**Proper citation:** Executive Order Number JML 25-119, "CO₂ Capture and Storage Limits and Moratorium,"
Office of the Governor, State of Louisiana (Gov. Jeff Landry), p. 4 (as paginated in
`CCS_PAPER/Corpus_1/Department-Directive-Order-No-B-2025-01-combined.pdf`, the project's own corpus copy).
I did not find an independent, separately-hosted state government URL for this EO tonight (a Governor's-
office EO archive would be the ideal primary hosting location to cite alongside the corpus PDF, e.g. a
`gov.louisiana.gov` executive-orders page) — that's still worth a follow-up search if Britton wants a
public URL rather than only the corpus file as the source.

**Bottom line for Britton:** the "public trust" anchor is real and directly citable — but the exact
phrasing is "safeguard public trust" (single mention, in a WHEREAS clause about the Governor personally
stepping in after hearing citizen/community concerns), not "foster or erode public trust." Both readings
support the same trust/legitimacy theory-grounding use, but only the "safeguard public trust" wording can
actually go in quotation marks.

---

## 3. Light literature-gap scan

Three new candidates found tonight (Crossref-verified DOIs, metadata checked field-by-field against
Crossref's canonical record — none of these were in the 09-03 note's two candidates or the existing
58-entry list, though as before that existing list wasn't reopened/cross-checked directly):

- **Middleton, E., Miranda, M., & Mehdi, Q. (2025). "Environmental Justice and CCS Infrastructure:
  Overlaps and Oversights at the National and State Levels." *Journal of Climate Resilience and
  Justice*, 2, 57–72.** DOI 10.1162/crcj_a_00016. US national/state-level EJ + CCS infrastructure —
  closer to this paper's actual geography/scale than most of the existing lit review's Europe-heavy
  acceptance literature. Worth a look.
- **Chintam, K., & Seitz, L.C. (2026). "Carbon Capture Technology through an Environmental Justice
  Lens." *PRX Energy*, 5(1), 011002.** DOI 10.1103/c8vk-qr6h. Published Jan 30, 2026 — very recent.
- **Tiwari, S., Neville, K.J., Hoicka, C.E., Teelucksingh, C., Besco, L., Huang, S., Renowden, C., &
  Galloway, T. (2025). "From Capture to Conversion." *Environment and Society*, 16(1), 155–172.**
  DOI 10.3167/ares.2025.160109. Argues procedural justice must be integrated into CCS governance for
  legitimacy/public trust — thematically close to this paper's trust/legitimacy framing specifically
  (more so than the 09-03 note's two candidates), though its empirical focus (per the abstract metadata,
  not fully read) appears to be capture-to-conversion pathways broadly, not Louisiana/US Gulf specifically
  — would need a closer read to confirm fit before adding.

All three found via a combination of WebSearch and direct Crossref API queries; DOIs and full metadata
(title, authors, journal, volume/issue, pages, year) independently confirmed against Crossref's own
record, not just search-summary text. None cross-checked against the existing 58-entry docx list tonight
(same caveat as 09-03) — flagging as candidates only.

---

## What's still open / worth Britton's attention

- **Citation fix needed:** the project's corpus and prior notes call the Governor's moratorium order
  "Executive Order B-2025-01" — it should be **Executive Order Number JML 25-119**. "B-2025-01" belongs
  to a different document (DENR/DCE Department Guidance, Secretary Tyler Gray, not the Governor).
- **The exact "public trust" quote to use** is "to support balanced economic growth and safeguard public
  trust" — not "foster or erode public trust," which I could not verify anywhere in the primary text.
- **WV oral-argument date is unconfirmed** — the most recent source I found (May 2026) says argument
  wasn't yet scheduled; the "late October 2026" figure in the 09-03 note doesn't check out against
  anything I found and shouldn't be repeated without a fresh check.
- **New finding, not previously in project notes:** Deep South Center for Environmental Justice v. EPA,
  138 F.4th 310 (5th Cir. 2025) — a real, decided precedent where EJ groups already tried and failed to
  challenge Louisiana's own Class VI primacy grant on EJ-standing grounds. This is arguably more citable
  and more directly relevant to the paper than the WV case standing alone, since it's Louisiana-specific
  and gives the WV case its comparative point (a second attempt at the same theory, post-Louisiana-loss).
  Recommend treating these as a pair in any comparison-case writing, not WV alone.
  Primary source: https://www.ca5.uscourts.gov/opinions/pub/24/24-60084-CV0.pdf (official Fifth Circuit
  opinion PDF).
  WV brief primary source: https://cdn.climatepolicyradar.org/navigator/USA/2025/west-virginia-surface-owners-rights-organization-v-zeldin_40d11b22c2c9dc9166219a7d3c4a6d09.pdf
- Three new lit-gap candidates above — none urgent, none cross-checked against the full 58-entry list.
- Unchanged from 09-03/09-02: McCauley et al. volume-number fix, docx "51 vs 58" reconciliation, Track
  A/B/C and date-convention picks all remain Britton's.
