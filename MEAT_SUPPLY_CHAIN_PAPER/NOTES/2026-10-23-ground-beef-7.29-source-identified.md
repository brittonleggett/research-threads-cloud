# 2026-10-23: The $7.29 -> $7.13 ground beef figure, source identified

**Source:** American Farm Bureau Federation, Market Intel, "Increased Beef Imports Have Not Lowered Prices For Consumers," Bernt Nelson and Faith Parum, Sept 23, 2026. https://www.fb.org/intel/markets/increased-beef-imports-have-not-lowered-prices-for-consumers. Fetched 2026-10-23; the extracted text is in `Overnight_Summaries/receipts_2026-10-23/afbf_ground_beef/`.

**What the page says (fetched text):** AFBF tracked daily prices of **80% lean ground beef** at **41 grocery stores in 22 states**, starting Sept 2 (the day after the proclamation took effect). The average went "from $7.29 a pound on Sept. 2 to $7.13 a pound on Sept. 23", a cut of 16 cents (about 2%). Prices did not change at 30 of the 41 stores.

**Why it differs from BLS.** This resolves the 10-20 discrepancy; neither number is wrong.
- AFBF: 80% lean ground beef, one 41-store convenience sample, daily, Sept 2-23.
- BLS APU0000703112: 100% beef ground beef of all lean grades, national CPI sample, monthly. Aug 6.923 -> Sep 6.792 (FRED, fetched 2026-10-20; a re-fetch on 10-23 timed out).
- They are different products and different samples, so the price levels shouldn't match. Both show a small (~2%) decline, far short of the proclamation's 25% target.

**Status:** VERIFIED (figure, sample, and dates checked against the fetched page). Use restriction: it is an advocacy-organization convenience sample, not a probability sample. Name it as AFBF's 41-store tracking. Never describe it as a national average or attribute it to BLS/USDA.

**Already correct:** `SOURCE_VERIFICATION/Evidence_Table_Imports.md` row 26 and the 09-26 note already attribute the figure to AFBF's 41-store tracking. Two places were loose and are now fixed:
- `04_DATA/watchlist.csv` row 5 called it a "BLS/USDA ... baseline". Annotated.
- `04_DATA/candidate_leads.csv` M010 said "series unidentified". Annotated.
