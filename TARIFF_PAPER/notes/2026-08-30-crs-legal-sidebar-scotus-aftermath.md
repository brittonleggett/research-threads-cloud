# 2026-08-30 — CRS Legal Sidebar read directly; SCOTUS aftermath (refunds, CIT, de minimis) upgraded from WebSearch to primary-source confidence

Follow-up to the 2026-08-29 note's flag: "SCOTUS aftermath (refunds question, CIT follow-on
litigation, de minimis)" was sitting at WebSearch-only confidence, with the CRS Legal Sidebar named
as the next target. This pass reads that Sidebar directly (plus a second CRS product it points to,
plus — unexpectedly — the actual CIT slip opinion that resolved the de minimis question two and a
half weeks ago). All three are primary sources, read in full via the same "curl the PDF directly /
let WebFetch save the binary, then Read the saved file" workaround the 2026-08-29 note recommended.
It worked cleanly three times tonight, on three different government sites.

**Tooling note:** direct `curl` (not WebFetch) against `congress.gov/crs_external_products/.../*.pdf`
worked immediately for two of the three PDFs (no WebFetch needed at all). The third
(`cit.uscourts.gov`) blocked plain curl with a WAF rejection page, but WebFetch's own fetch got past
that WAF, choked on summarizing the binary as before, and saved it — the Read tool then parsed it
cleanly. So: try curl first for `.gov` PDFs, fall back to WebFetch-then-Read-the-saved-file when curl
is blocked. Both are now confirmed-working patterns for this project.

---

## 1. CRS Legal Sidebar LSB11398 — read in full (primary source)

**Congressional Research Service, "Supreme Court Rules Against Tariffs Imposed Under the
International Emergency Economic Powers Act (IEEPA)," dated February 23, 2026 (Version 1).**
Fetched directly: `https://www.congress.gov/crs_external_products/LSB/PDF/LSB11398/LSB11398.1.pdf`
(424KB PDF, read in full — 7 pages, author Christopher T. Zirpoli, Legislative Attorney).

Confirms everything the 2026-08-29 note already had from the slip opinion itself (case names,
Feb 20, 2026 decision date, Roberts opinion, 6-3 bottom line with a 3-3 split on major-questions
reasoning, V.O.S. Selections affirmed, Learning Resources vacated/remanded on jurisdictional
grounds) — no changes needed there. New/confirmed on the three specific aftermath questions:

**Refunds:** "The Supreme Court's opinion in Learning Resources did not address potential refunds of
tariffs the government collected pursuant to IEEPA." Justice Kavanaugh's dissent is quoted directly:
"The United States may be required to refund billions of dollars to importers who paid the IEEPA
tariffs, even though some importers may have already passed on costs to consumers or others." The
Sidebar points to a second CRS product (IF13150, below) for refund mechanics. **Confidence: A-tier,
primary source, matches what the 2026-08-29 note already inferred from the slip opinion — now
independently confirmed rather than inferred.**

**De minimis:** The Sidebar lays out the factual sequence precisely. The President's IEEPA-based
suspension of the de minimis exemption (19 U.S.C. § 1321, duty-free treatment for shipments ≤$800)
was *not* at issue in Learning Resources/V.O.S. Selections — it is a separate use of IEEPA. A
lawsuit, **Axle of Dearborn, Inc. v. Department of Commerce**, filed in the CIT in May 2025,
challenges that specific use of IEEPA. The CIT stayed that suit in July 2025 pending "final
resolution" of V.O.S. Selections. As of this Sidebar's Feb 23, 2026 publication date, the open
question was "whether the Supreme Court's holding in V.O.S. Selections and Learning Resources
forecloses the use of IEEPA to suspend de minimis importation in Axle of Dearborn or other cases."
**This question has since been answered — see Section 3 below, a genuinely new finding tonight, not
in any prior note.**

**CIT follow-on litigation generally:** The Sidebar's framing is that the Supreme Court's ruling
established CIT exclusive jurisdiction over IEEPA tariff challenges (28 U.S.C. § 1581(i)), which
"will shape future litigation procedures in that specialized tribunal" — deliberately general,
since the Sidebar is dated three days after the ruling and predates most of the actual follow-on
litigation.

**Important dating caveat:** LSB11398 is Version 1, dated Feb 23, 2026, three days after the ruling.
It is *not* updated for anything that happened after that date (the March/April CIT liquidation
orders, the August CIT de minimis ruling — see below). Treat it as a primary source for the ruling
itself and the state of play as of Feb 23, not as current status.

## 2. CRS In Focus IF13150 — read in full (primary source, refund mechanics)

**"Potential Refunds of Tariffs Imposed Under the International Emergency Economic Powers Act
(IEEPA)," dated January 13, 2026 (Version 4) — Christopher T. Zirpoli and Christopher A. Casey.**
Fetched directly: `https://www.congress.gov/crs_external_products/IF/PDF/IF13150/IF13150.4.pdf`
(note: version numbering on this URL pattern is inconsistent — v1/v2/v5/v6 at this path 404-redirect
to the congress.gov homepage as HTML, only v3 and v4 are real PDFs; v4 used as the latest).

**This document predates the Feb 20, 2026 ruling** (it's written prospectively — "in the event that
the Supreme Court holds that some or all of these tariffs are unlawful") so it is a mechanics
reference, not a report of what actually happened. Key mechanics it lays out, useful background for
the refund-wave corpus context already in prior notes:
- **Liquidated vs. unliquidated entries:** as of Dec 10, 2025, ~19.2M of ~34M IEEPA-tariffed entries
  were still unliquidated (~$129B in estimated duty deposits paid by then). Unliquidated entries can
  get refunds automatically on liquidation; liquidated entries need a protest or lawsuit.
- **Protest path:** 19 U.S.C. § 1514(c)(3), 180-day window from liquidation — but the CRS analysis
  flags real uncertainty whether CBP's collection of IEEPA tariffs is even a "protestable decision"
  under that section, since CBP was just following presidential executive orders.
- **CIT lawsuit path:** residual jurisdiction under 28 U.S.C. § 1581(i), two-year statute of
  limitations from when the tariff was paid.
- **Class actions / nationwide relief:** genuinely uncertain per this CRS analysis — one class-action
  IEEPA-refund suit had already been filed and voluntarily dismissed as of this writing; *Trump v.
  CASA, Inc.* (June 2025) limits nationwide injunctions to what's needed for complete relief to
  parties, and CRS flags this as an open question for whether CIT can order refunds for
  non-parties.
- **Congressional options noted:** streamline the refund process, or alternatively legislate to
  expressly approve the IEEPA tariffs and foreclose refunds.

**Confidence: A-tier, primary source, but explicitly pre-ruling — a mechanics primer, not a status
report.** Nothing here should be cited as "what happened," only as "what the legal mechanism is."

## 3. De minimis question — now definitively resolved, found via primary CIT slip opinion (genuinely new)

This is the most significant finding tonight and **was not flagged as resolved in any prior note.**
A WebSearch pass surfaced that the CIT ruled on *Axle of Dearborn* on **August 13, 2026** — only
two and a half weeks before this note. Rather than take that on WebSearch confidence, I found and
read the actual slip opinion directly.

**Primary source: Slip Op. 26-94, *Axle of Dearborn, Inc. d/b/a Detroit Axle v. Department of
Commerce*, Court No. 25-00091, U.S. Court of International Trade, decided August 13, 2026.** Fetched
via WebFetch (which choked summarizing the binary as expected) then read directly from the saved
PDF file — full ~30-page opinion read.

- **Panel:** Three-judge panel — Gary S. Katzmann, Timothy M. Reif, Jane A. Restani. Per curiam.
- **Holding:** IEEPA's authority to "nullify, void, prevent or prohibit ... exercising any right,
  power, or privilege" (50 U.S.C. § 1702(a)(1)(B)) **does authorize** the President's rescission of
  the de minimis exemption, because the exemption is explicitly a "privilege" under its own statutory
  text (19 U.S.C. § 1321(a)(2), (c)) — a different, narrower delegation than the tariff-imposition
  power struck down in Learning Resources. The court explicitly distinguished this from Learning
  Resources: rescinding an exemption "imposes no new duties," doesn't touch "the core congressional
  power of the purse," and isn't equivalent to the line-item veto struck down in *Clinton v. City of
  New York* — it just makes already-dutiable goods (dutiable under rates Congress set) actually
  subject to those existing duties.
- **APA claim also rejected:** agency implementation of the President's directive (Commerce,
  Treasury, CBP) was "ministerial" and not reviewable under the APA, per *Franklin v. Massachusetts*.
- **Disposition:** Denied Axle's motion for summary judgment on Counts I (IEEPA authority) and II
  (APA), granted summary judgment for the government on those counts. **Deferred** judgment on Count
  III (whether the President could impose the underlying tariffs at all) as effectively moot, since
  Learning Resources had already resolved that question and the tariffs were already ended.
- **This is a merits ruling upholding the de minimis suspension**, not merely a procedural stay
  lifted — it forecloses (at the CIT level, subject to appeal) the Axle theory that the Learning
  Resources ruling extends to invalidate the de minimis rescission too.

**Confidence: A-tier, primary source (actual slip opinion, not a secondary summary).** This directly
answers the exact question the 2026-08-14/08-18/08-29 notes had all flagged as open.

**One important nuance surfaced by this same document, worth flagging honestly rather than
smoothing over:** the slip opinion's footnote 12 describes a separate, already-existing CIT order
directing CBP to liquidate/reliquidate IEEPA-duty entries (unliquidated, non-final-liquidated, and
even finally-liquidated entries — all without regard to the IEEPA duties). The opinion cites this
order as issued in ***V.O.S. Selections, Inc. v. United States*, No. 25-cv-00066, dated April 17,
2026 (ECF No. 82)** — with the government's appeal "pending at the Federal Circuit" as *V.O.S.
Selections, Inc. v. Trump*, No. 26-1895, filed June 3, 2026, **consolidating four appeals of
identical Orders Directing Liquidation.**

This is a different case name and a later date than a body of law-firm secondary sources found via
WebSearch tonight (Greenberg Traurig, Forvis Mazars, Tax Notes, Snell & Wilmer, Buchalter, Stinson,
Thompson Hine, Kaplan Gore, HNRK), which describe a materially similar liquidation/reliquidation
order in a case styled ***Atmus Filtration, Inc. v. United States*, CIT Court No. 26-01259, Judge
Richard K. Eaton**, with an original order and amendments dated **March 20 and March 27, 2026** —
about a month earlier than the April 17 date the Axle opinion cites for the V.O.S. order. The
"consolidating four appeals of identical Orders Directing Liquidation" language in the Axle opinion
is consistent with there having been multiple, separately docketed CIT liquidation orders across
several cases (Atmus Filtration plausibly being one of the four) that were substantively identical
and got consolidated on appeal — which would mean both sets of facts are correct and just describe
different cases in the same consolidated family. **I could not independently confirm this reconciles
cleanly — I did not get a working direct fetch of the CIT's own docket or PACER for either case
(CourtListener returned a CloudFront 403 on every query attempted; a direct docket-number guess on
cit.uscourts.gov also failed).** Flagging this as an open loose end rather than papering over it:
the Atmus Filtration narrative is B-tier (multiple independent law-firm write-ups, one direct-fetched
— GT Law — but no primary docket confirmation), and the V.O.S. Selections order is A-tier (named
directly, with docket number and date, inside a primary CIT opinion I read in full) but is one node
in a four-case consolidated appeal whose other three members I haven't identified. Both can be true;
neither is fully pinned down at citation-grade precision. If this level of detail ever needs to go
into the manuscript, it's worth a follow-up pass specifically to identify all four consolidated cases
by docket number.

**Refund mechanics status, tied together:** the CIT liquidation/reliquidation order (whichever case
is the lead one) is exactly the mechanism IF13150 predicted in January — reliquidation of
already-liquidated entries "without regard to" the invalidated duties — now actually ordered by the
court, not just a Section 1514/1515 protest process running its course. That order is under appeal
at the Federal Circuit as of June 3, 2026 and, per the multiple law-firm sources, was "suspended ...
as to immediate compliance" pending CBP building out a refund-processing system (referred to in one
source as "CAPE"). **This detail (the CAPE system name and the compliance stay) is B-tier,
WebSearch/law-firm-sourced only — not independently confirmed against a primary document tonight.**

## 4. What's now confirmed vs. still open, summary

**Newly confirmed at primary-source (A-tier) confidence tonight:**
- The Learning Resources/V.O.S. Selections opinion did not address refunds (confirmed twice now:
  once from the slip opinion itself on 08-29, again from the CRS Sidebar tonight, both primary).
- The de minimis question is **resolved** at the CIT level: IEEPA's rescission of the de minimis
  exemption was **upheld** on August 13, 2026 (Axle of Dearborn), on the theory that the exemption is
  a "privilege" IEEPA lets the President void, distinct from a tariff. This is a merits win for the
  government, not a procedural non-event — worth updating any framing that treated de minimis status
  as still an open question post-ruling.
- Refund mechanics generally (protest process, CIT residual jurisdiction, liquidation/reliquidation,
  class-action/nationwide-injunction uncertainty) are confirmed against CRS's own analysis, though
  that analysis itself predates the ruling and is a mechanics primer, not a report of outcomes.
- A CIT order exists directing CBP to liquidate/reliquidate IEEPA-tariffed entries broadly (even
  finally-liquidated ones), and it's on appeal at the Federal Circuit — confirmed via a primary
  document, though the precise case name/docket at the head of that consolidated appeal is not fully
  pinned down (see the Atmus Filtration/V.O.S. Selections nuance above).

**Still open / not independently verified:**
- The exact roster of the four consolidated Federal Circuit appeals (Atmus Filtration vs. V.O.S.
  Selections vs. two others) — B-tier at best right now.
- Whether/how the CAPE refund-processing system and the "suspended pending compliance" detail are
  accurately characterized — WebSearch/law-firm sourced only, not primary-confirmed tonight.
- Whether Axle of Dearborn has been or will be appealed (the slip opinion is dated Aug 13, 2026,
  three and a half weeks before this note — too recent to expect appellate activity yet, and I did
  not find any).
- The "$175 billion" refund-exposure figure that surfaced in one WebSearch snippet (Norton Rose
  Fulbright headline) was not chased down or verified tonight — noting it exists as an industry
  estimate circulating in secondary coverage, not confirming or using it.

## 5. Untouched per standing instructions

Did not touch the refund-wave corpus-scope decision (still Britton's call) or the Insteel
"freight"/"profit" quote discrepancy (still needs Britton's own eyes on the transcript). Neither was
in scope for tonight's task and neither was approached.

---

## For Britton

1. **The de minimis exemption suspension has been upheld by the CIT (Aug 13, 2026, Axle of
   Dearborn)** — if the manuscript's discussion section treats de minimis status as unresolved
   post-ruling, that should be updated. This is a primary-source-confirmed merits decision, not a
   procedural stay.
2. There's a genuine, unresolved discrepancy between a primary CIT document (naming the liquidation
   order's home case as *V.O.S. Selections v. United States*, April 17, 2026) and a cluster of
   law-firm secondary sources (naming it *Atmus Filtration v. United States*, March 2026) for what
   may be the same family of consolidated orders. Not citation-ready at the docket level; flagged
   above, not resolved.
3. Both CRS documents (LSB11398 and IF13150) are public-domain U.S. government works and were saved
   only to the local scratchpad during this session, not copied into the repo — consistent with the
   project's IRB/sensitivity conventions and the instruction not to store paywalled material (these
   aren't paywalled, but nothing was added to the repo beyond this note either way).
