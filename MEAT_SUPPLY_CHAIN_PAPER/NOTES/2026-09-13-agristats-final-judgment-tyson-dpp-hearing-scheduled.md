# 2026-09-13 — Agri Stats Final Judgment entered; Tyson DPP final-approval hearing now scheduled

Follow-up on the two items flagged "genuinely open" in the 2026-09-09 pass
(`NOTES/2026-09-09-doj-tyson-agristats-status-check.md`). Both resolved tonight via direct
primary-source court-record reads — not search snippets or news paraphrase. Method: CourtListener
free RECAP archive, fetched via plain `curl` with a browser User-Agent (CourtListener's own HTML
docket pages return 200 this way; its REST API still 401s without an account, and PACER itself
still requires paid credentials we don't have — same pattern as prior nights). Where a docket
entry had an attached RECAP PDF, the PDF itself was downloaded and read directly with
`pdftotext -layout`; one order (see below) was an image-only PDF with no text layer — installed
`tesseract-ocr` locally (not previously in this environment) and OCR'd it at 300dpi, which worked
cleanly. Two separate cases were involved; neither should be confused with the other or with the
already-resolved $87.5M consumer settlement.

## 1. Agri Stats — DOJ's own civil case: Final Judgment ENTERED September 10, 2026 (RESOLVED)

**Case:** *United States, et al. v. Agri Stats, Inc.*, No. 0:23-cv-03009 (JRT/JFD), D. Minnesota
(DOJ Antitrust Division + California, Minnesota, North Carolina, Tennessee, Texas, and Utah AGs —
this is DOJ's own Tunney Act civil-enforcement suit, distinct from the private consumer class
action against Agri Stats described below and in the 2026-09-09 note).

**What happened, in order, all confirmed from the actual signed court filings (not docket-entry
text alone):**
- May 7, 2026 (Doc. 742) — Plaintiffs filed a proposed Final Judgment and Stipulation and Order
  under the Antitrust Procedures and Penalties Act ("Tunney Act," 15 U.S.C. § 16). Corrected
  versions filed May 15 (Doc. 748).
- May 21, 2026 (Doc. 750) — Competitive Impact Statement filed, read in full via direct PDF fetch
  (`justice.gov/atr/media/1442401/dl`). Confirms the proposed remedy is **entirely injunctive/
  behavioral — no monetary settlement or fine.** Key terms: Agri Stats is (1) prohibited from
  sharing sales reports or non-public pricing information among competing processors; (2)
  prohibited from sharing most production/cost/labor data at the facility level between
  competitors; (3) prohibited from providing information to competing processors averaging less
  than 45 days old; (4) required to make the large majority of its reports available to *any*
  interested purchaser on reasonable, non-discriminatory terms (with a specific price-cap
  mechanism — e.g., if single-plant processors pay $1,500/month for a given report, Agri Stats
  cannot charge a non-processor more than that for the same report); (5) required to implement an
  antitrust compliance program; and (6) required to accept a court-appointed Monitor overseeing
  compliance. The Tunney Act's 60-day public-comment period ran from the June 5, 2026 Federal
  Register publication.
- **September 10, 2026 (Doc. 763) — Judge John R. Tunheim signed the Final Judgment**, downloaded
  and read in full directly (`storage.courtlistener.com/recap/gov.uscourts.mnd.210827/
  gov.uscourts.mnd.210827.763.0.pdf`, 81 pages). Section XVI, "Public Interest Determination,"
  states the parties complied with the APPA's comment/response requirements and that, based on the
  Competitive Impact Statement and any comments filed, "entry of this Final Judgment is in the
  public interest." The order concludes "LET JUDGMENT BE ENTERED ACCORDINGLY," dated and signed
  September 10, 2026, at Minneapolis.

**Bottom line:** final approval **was granted**, nine days after the September 1, 2026 hearing
this project had been tracking as unresolved. The remedy is conduct/injunctive only — there is no
settlement dollar amount to report for this specific case (that distinguishes it from the private
class-action track discussed next). I could not independently confirm from the free RECAP archive
exactly what happened *at* the September 1 hearing itself (docket entries 752–762 sit in a gap not
purchased/uploaded by any RECAP user, and the Tunney Act doesn't even require an evidentiary
hearing — 15 U.S.C. § 16(e)(2)) — but this doesn't matter for the outcome question, since the
signed Final Judgment itself is the authoritative record of what the court ultimately did and on
what terms.

**Separate but related, for anyone tracing news coverage later:** the meatingplace.com article
already flagged in the 2026-09-09 note ("Judge Approves Agri Stats Settlements in Chicken, Turkey
Antitrust Cases") was fetched again this pass (the paywall's free teaser paragraphs came through
via `curl` with a browser UA) and is now confirmed to be about the **private End-User Consumer
class action's preliminary approval** (its own text says "granted preliminary approval... if final
approval is granted, the agreement would conclude the consumer class portion of the case"), not
about DOJ's Tunney Act final judgment above. That "$203.35M" total consumer recovery figure
appearing in search results is the *cumulative* consumer-class recovery from all broiler-industry
defendants across a decade of litigation, not a settlement amount tied to DOJ's Agri Stats case
specifically. Keep these two Agri Stats tracks (DOJ's own injunctive-only suit vs. the private
consumer class's separate no-cash injunctive settlement) distinct in any manuscript reference.

## 2. Tyson $82.5M DPP settlement — final-approval hearing now scheduled for October 1, 2026 (still pending, not yet decided)

**Case:** *In re Cattle and Beef Antitrust Litigation*, No. 0:22-md-03031 (JRT/JFD), D. Minnesota
(the master beef-antitrust MDL; Direct Purchaser Plaintiffs' claims against Tyson specifically).

Confirmed via the MDL's own docket (CourtListener docket 63363039), read directly:

- May 14, 2026 (Doc. 1592) — Preliminary approval granted (already known/confirmed prior pass —
  unchanged).
- **August 10, 2026 (Docs. 1613/1614) — Direct Purchaser Plaintiffs formally filed their "Motion
  for Final Approval of Settlement with Tyson Defendants."** This had not happened as of the
  2026-09-09 check, which correctly reported no hearing scheduled yet — but the check window
  closed before this filing, and a subsequent generic web search alone would have missed it (the
  MLex headline "Direct purchasers seek US judge's final approval of Tyson antitrust settlement,"
  found again this pass, refers to this same Aug. 10 filing, corroborating the docket record —
  though the MLex article body itself is paywalled with no free teaser text, unlike meatingplace).
- **August 18, 2026 (Doc. 1621) — Judge Tunheim signed an order modifying the notice/briefing
  schedule**, read in full via OCR (see method note above; this PDF's text layer didn't extract
  with `pdftotext` despite being "Tagged: yes" in its metadata — a genuine tooling quirk, not a
  bot-block, resolved by installing `tesseract-ocr` and rasterizing the two pages at 300dpi). This
  order sets out the actual current schedule for the DPP-Tyson settlement:
  - Objection deadline: **September 14, 2026** (moved from Aug. 12)
  - Opt-out deadline: **September 14, 2026** (moved from Aug. 12)
  - Interim counsel's fee/expense/service-award motion due: September 1, 2026
  - Plaintiffs' final-approval brief and proposed order due: **September 21, 2026**
  - **Final Approval Hearing: October 1, 2026**

**Bottom line:** as of today (2026-09-13), the DPP-Tyson settlement has **not yet received final
approval** — the hearing is real and dated (October 1, 2026), roughly 2.5 weeks from today, but it
has not happened yet, and no order deciding the motion exists in the docket as of this pass. This
is genuine forward progress worth recording (a firm hearing date now exists, where none did as of
2026-09-09) without overstating it as an outcome. Worth noting for context, not as a confirmed
link: the Commercial and Institutional Indirect Purchaser Plaintiffs' own separate Tyson
settlement final-approval hearing was independently set for the same date, October 1, 2026 at
11:30 AM (Doc. 1604, entered April 28, 2026) — plausibly the court consolidating multiple pending
Tyson-settlement approvals into one hearing day, but the DPP schedule order (Doc. 1621) states only
the date, not a time, so this is not confirmed to be the literal same session. The previously-known
November 30, 2026 claims deadline is unaffected by this schedule change and still stands.

**Recommend for a future pass:** check back after October 1, 2026 for the actual ruling (should be
a short, findable order much like the Agri Stats Final Judgment above, once entered).

No design decisions touched. No external contact made. No money spent.
