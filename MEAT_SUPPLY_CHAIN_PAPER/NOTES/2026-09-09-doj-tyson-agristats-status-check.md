# 2026-09-09 — DOJ retailer probe, Tyson $82.5M DPP settlement, Agri Stats hearing: status check

Three remaining items from `PROJECT_STATUS.md`'s "Next actions" list. Mixed results — one
reconfirmed, one clarified-but-not-fully-resolved, one genuinely still open.

## 1. DOJ eight-retailer probe — no new primary document (reconfirms 2026-09-08 finding)

Re-searched for a DOJ.gov document (not the social-media post already verified 2026-09-08).
Found nothing new — same result as before: no dedicated DOJ Office of Public Affairs press
release exists for the eight-retailer letters specifically, only the DOJ's own official
X/Twitter post (already primary-source-confirmed) and trade-press coverage of it. Treat this as
closed for now; a formal DOJ.gov release may still follow later, but no further automated-search
time is likely to find one that doesn't exist yet.

## 2. Tyson $82.5M DPP (grocer/distributor) settlement — clarified, not identical to the already-tracked $87.5M settlement, final-approval date unconfirmed

**Important disambiguation the search results kept blurring:** there are two separate 2026 Tyson
beef-antitrust settlements in play, and generic search queries return a mix of both:

1. The **$87.5M indirect-purchaser/consumer settlement** (Tyson + Cargill) — already tracked in
   this project (`NOTES/2026-09-07-schaefer-pozo-idea28-followup.md`), final-approval order
   **signed May 27, 2026** per that prior pass's direct verification (not May 29, a date that
   appears in some press headlines/coverage timing rather than the signing date itself).
2. The **$82.5M direct-purchaser (grocers/distributors) Tyson-only settlement** — this project's
   actual open item — reached in principle December 2025, **preliminary approval granted May 14,
   2026** by Judge John Tunheim (D. Minn.), covering direct beef purchases Jan 1, 2015 - Feb 29,
   2020, claims deadline Nov 30, 2026. This is corroborated consistently across multiple
   independent trade-press outlets (Feedstuffs, MEAT+POULTRY, Supply Chain Dive, Food Dive), so
   the preliminary-approval fact and date are solid.

**What I could NOT confirm:** whether a distinct *final* approval order has since been entered
for the $82.5M DPP settlement specifically. Several search results state a "final approval" date
of May 27 or May 29, 2026 — but on closer reading these appear to describe the *other* ($87.5M)
settlement's final approval, not this one, and at least one source's own preliminary-approval
timeline (May 14) makes a final hearing only 12-13 days later implausible for a class settlement
of this size (final hearings are typically set months out to allow the objection/opt-out period,
consistent with the $87.5M settlement's own timeline). Attempted direct primary verification:
CourtListener's docket page (403-blocked to automated fetch, consistent with tonight's pattern
elsewhere in this project) and its REST API (401, requires an authenticated account I don't
have); Tyson's own FY2026 Q3 10-K filing (confirmed via SEC.gov to contain a
`tsn:BeefAntitrustCivilLitigationMember` XBRL tag, meaning Tyson does disclose this, but the
automated fetch could not extract the narrative footnote text — the filing is large and the tool
returned only the index structure).

**Recommendation:** do not state a final-approval date for the $82.5M DPP settlement in the
manuscript without either (a) a direct read of Tyson's 10-Q legal-proceedings footnote (may need
a targeted fetch of just that section, or a manual PDF/HTML pull), or (b) a PACER/CourtListener
docket check with real credentials. This is exactly the kind of specific-date confusion this
project has already been burned by twice (the Missouri and California fabricated-case-number
incidents, 2026-09-05/09-07) — better to leave it as "preliminarily approved May 14, 2026, final
approval status unconfirmed" than to guess.

## 3. Agri Stats Sept 1, 2026 final approval hearing — genuinely unresolved, real open item

Confirmed via DOJ's own Federal Register notice (federalregister.gov/documents/2026/06/05/2026-11329)
and the Minnesota AG's own press release that: the proposed Final Judgment was filed May 7, 2026;
the public-comment/objection period closed July 13, 2026; a final approval hearing was set for
September 1, 2026. **No source found — DOJ.gov, Federal Register, or reputable trade press —
confirms what happened at or after that hearing.** One meatingplace.com headline surfaced in
search ("Judge Approves Agri Stats Settlements in Chicken, Turkey Antitrust Cases") looked
promising but the article itself 403-blocked automated fetch and I could not confirm its publish
date or content directly — do not treat the headline alone as confirmation, it could equally be
about an earlier procedural approval (e.g., the May 7 proposed-judgment filing) rather than the
September hearing's outcome. **Genuinely open, worth a follow-up pass** (try `justice.gov/atr`
case docket page directly with a different URL pattern, or check for a post-Sept-1 DOJ press
release) — not resolved tonight.

No design decisions touched. No external contact made. No money spent.
