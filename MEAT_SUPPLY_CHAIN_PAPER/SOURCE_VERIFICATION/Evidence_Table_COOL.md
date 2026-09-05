# Evidence Table — COOL / Regulatory (fork contribution, 2026-09-03)

To be merged into the master `Evidence_Table.md` under "Country-of-origin
labeling / regulatory." Same column format.

| Claim | Source | Source type | URL | Pub. date | Page/Table | Commodity | Years covered | Geography | Verification status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2002 Farm Bill authorized mandatory COOL for beef, lamb, pork, fish, perishables, peanuts | P.L. 107-171 via National Agricultural Law Center COOL overview | Secondary, traced to primary (public law) | https://nationalaglawcenter.org/overview/cool/ | overview page, undated (describes 2002 law) | n/a | Beef, pork | 2002– | US | Verified (secondary, traced to primary) | Direct govinfo.gov PLAW text not fetched this pass |
| Final COOL rule effective March 16, 2009 | National Agricultural Law Center COOL overview | Secondary, traced to primary | https://nationalaglawcenter.org/overview/cool/ | n/a | n/a | Beef, pork | 2009 | US | Verified (secondary, traced to primary) | Corroborated by CRS RS22955 timeline (EveryCRSReport mirror) |
| WTO panel ruled against U.S. COOL Nov 18, 2011; Appellate Body upheld June 29, 2012; DSB adopted July 23, 2012 | CRS Report RS22955, "Country-of-Origin Labeling for Foods and the WTO Trade Dispute on Meat Labeling" | Secondary (CRS report), traced to WTO dispute record | https://www.everycrsreport.com/reports/RS22955.html | RS22955 (see report for version date) | n/a | Beef, pork (livestock) | 2008–2012 | US/Canada/Mexico | Verified (secondary, traced to primary) | CRS reports are considered high-reliability secondary sources; original WTO DSB documents not independently fetched this pass |
| USDA issued revised "born/raised/slaughtered" COOL rule May 23, 2013 | CRS RS22955 | Secondary, traced to primary | https://www.everycrsreport.com/reports/RS22955.html | RS22955 | n/a | Beef, pork | 2013 | US | Verified (secondary, traced to primary) | |
| WTO compliance panel ruled against revised rule Oct 20, 2014; Appellate Body upheld May 18, 2015 | CRS RS22955 | Secondary, traced to primary | https://www.everycrsreport.com/reports/RS22955.html | RS22955 | n/a | Beef, pork | 2014–2015 | US/Canada/Mexico | Verified (secondary, traced to primary) | |
| WTO arbitration authorized ~C$1.055B (Canada, ~US$781M) + ~US$228M (Mexico) retaliation, Dec 7, 2015; DSB authorization Dec 21, 2015 | CRS RS22955 | Secondary, traced to primary | https://www.everycrsreport.com/reports/RS22955.html | RS22955 | n/a | Beef, pork | 2015 | US/Canada/Mexico | Verified (secondary, traced to primary) | Combined figure (~$1.01B) matches independently-found UL Solutions news summary — cross-corroborated by two independent sources |
| Congress repealed mandatory COOL for beef and pork muscle cuts/ground product, Dec 18, 2015, via Consolidated Appropriations Act 2016, **P.L. 114-113** | Multiple: CRS RS22955; govinfo.gov PLAW-114publ113 record (title confirmed via search, not directly fetched); GAO-16-518R | Secondary + primary law citation | https://www.govinfo.gov/app/details/PLAW-114publ113 ; https://www.everycrsreport.com/reports/RS22955.html | Dec 18, 2015 | n/a | Beef, pork | 2015 | US | Verified (secondary, traced to primary — public law number cross-checked across 2 independent sources) | **Contradicted by other source**: nationalaglawcenter.org/overview/cool/ states "P.L. 114-114," which conflicts with govinfo.gov's own PLAW record title and the CRS-report-derived citation. Treating 114-113 as correct; flagging 114-114 as a likely typo on that one page. |
| USDA/AMS published conforming final rule removing beef/pork from COOL regs, March 2, 2016 | Federal Register document 2016-04609 | Primary (Federal Register), title/date confirmed via search results only | https://www.federalregister.gov/documents/2016/03/02/2016-04609/removal-of-mandatory-country-of-origin-labeling-requirements-for-beef-and-pork-muscle-cuts-ground | March 2, 2016 | n/a | Beef, pork | 2016 | US | Pending | Federal Register blocked automated WebFetch (302 to unblock.federalregister.gov interstitial); title/date only confirmed via search snippet, not read directly. Needs a follow-up fetch. |
| Mandatory COOL still applies to lamb, chicken, goat, venison, seafood, perishables, peanuts, pecans, macadamia nuts, ginseng (beef/pork repeal was commodity-specific, not a full COOL repeal) | National Agricultural Law Center COOL overview | Secondary, traced to primary (statute as amended) | https://nationalaglawcenter.org/overview/cool/ | n/a | n/a | Beef, pork, poultry (contrast) | 2015–present | US | Verified (secondary, traced to primary) | Practical enforcement/significance for poultry not verified this pass — see open item in COOL_Regulatory_Timeline.md |
| FSIS final rule "Voluntary Labeling of FSIS-Regulated Products with United States-Origin Claims," published March 18, 2024 (FR doc 2024-05479, 89 FR 19348 [table of contents/other pages give 19470 as the start page — pin down exact page before manuscript citation]); effective May 17, 2024; compliance deadline Jan 1, 2026 | Federal Register itself, via its public API/XML endpoints | **Primary — full regulatory text read directly, 2026-09-05** | Metadata: https://www.federalregister.gov/api/v1/documents/2024-05479.json ; Full text XML (this is what was actually read): https://www.federalregister.gov/documents/full_text/xml/2024/03/18/2024-05479.xml ; HTML page (still blocked, see log): https://www.federalregister.gov/documents/2024/03/18/2024-05479/voluntary-labeling-of-fsis-regulated-products-with-us-origin-claims | March 18, 2024 (pub.); May 17, 2024 (effective); Jan 1, 2026 (compliance) | n/a (full-text XML, not paginated) | Beef, pork, poultry | 2024–2026 | US | **Verified (primary — full text read directly)** | **Verification gap closed 2026-09-05.** The federalregister.gov HTML page still 302-redirects to an anti-bot interstitial (`unblock.federalregister.gov`) for both WebFetch and this pass's retry, but the site's own public `/api/v1/documents/{id}.json` metadata endpoint and `/documents/full_text/xml/...` full-text endpoint are NOT behind that block and returned complete, directly-readable content. This is the single most useful workaround from this pass — worth trying on any other federalregister.gov document that hits the same interstitial. |
| 2024 rule requires "Product of USA"/"Made in the USA" claims to mean the animal was born, raised, slaughtered, AND processed entirely in the US for single-ingredient products; for multi-ingredient products, additionally requires all non-spice/flavoring ingredients to be of domestic origin AND all preparation/processing steps to occur in the US — closing the prior loophole where FSIS's Food Standards and Labeling Policy Book allowed the claim on products "minimally processed in the United States" regardless of animal origin | Federal Register full-text XML (2024-05479), read directly | **Primary — full text read directly, 2026-09-05** | https://www.federalregister.gov/documents/full_text/xml/2024/03/18/2024-05479.xml | Rule dated March 18, 2024 | n/a | Beef, pork, poultry | 2024– | US | **Verified (primary — full text read directly)** | Supersedes the National Ag Law Center secondary summary as the citation of record for this specific claim (the summary was accurate, but this is now a direct primary-text read). Exact prior-rule language confirmed: FSIS's policy book previously had "a current 'Product of USA' entry that allows FSIS-regulated products that are minimally processed in the United States" to bear the claim — i.e., the pre-2024 loophole was specifically about *minimal* domestic processing being sufficient regardless of where the animal was born/raised/slaughtered. |

## Log of unsuccessful/inconclusive searches

**Resolved 2026-09-05** (for the 2024-05479 voluntary-labeling rule
specifically — see updated rows above; full method in
`NOTES/2026-09-05-primary-source-retry-pass.md`):
- The federalregister.gov HTML document page still 302-redirects to the
  `unblock.federalregister.gov` anti-automation interstitial — that part of
  the original blocker is NOT fixed. What worked instead: federalregister.gov
  publishes the same content at two other endpoints that are not behind the
  interstitial — `/api/v1/documents/{doc-number}.json` (metadata: title,
  dates, PDF/HTML/XML URLs) and `/documents/full_text/xml/{yyyy}/{mm}/{dd}/
  {doc-number}.xml` (the complete regulatory text). Both were fetched
  successfully via WebFetch directly.
- The govinfo.gov PDF mirror (`FR-2024-03-18/pdf/2024-05479.pdf`) was also
  re-fetched this pass and again came back as an unreadable binary stream to
  WebFetch's own reader — but per the GAO-02-246 resolution in
  `Evidence_Table_PriceTransmission.md`, this class of problem is now fixable
  by installing `poppler-utils` locally and running `pdftotext` on the saved
  binary file. Not actually needed here since the XML endpoint gave complete
  text directly, but worth knowing for other federalregister.gov/govinfo.gov
  PDFs that lack an XML full-text mirror.
- fsis.usda.gov was not retried this pass (not needed once the FR XML
  endpoint worked) — still presumptively blocked (403 on 2026-09-03),
  unconfirmed either way as of this pass.

**Still open:**
- The **2016 conforming rule** (Federal Register doc 2016-04609, removing
  beef/pork from mandatory COOL regs) was NOT retried this pass — only the
  2024 voluntary-labeling rule was targeted. The same API/XML workaround
  should work for it too; flagged as a quick follow-up for a future pass
  rather than attempted here.
- Prior to 2026-09-05, this fork's COOL timeline relied on convergent
  secondary sourcing (CRS report + National Agricultural Law Center +
  independently-found news/law-firm summaries). The 2024 rule specifically
  is now primary-text-verified; the rest of the timeline (2002 Farm Bill,
  2009 rule, WTO rulings, 2015 repeal, 2016 conforming rule) still rests on
  secondary sourcing and was not re-verified this pass.
