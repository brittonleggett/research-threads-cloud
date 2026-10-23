# 2026-10-23: Kyle TX (F008) correction applied

Fetched both pages tonight (they returned 403 on 10-18):
- Community Impact, Oct 7: https://communityimpact.com/san-marcos-buda-kyle/government/kyle-to-suspend-use-of-flock-cameras/
- KUT, Oct 8: https://www.kut.org/crime-justice/2026-10-08/the-city-of-kyle-will-suspend-use-of-flock-cameras-until-a-referendum-next-year

**Both agree:**
- On **Oct 5** the council voted **4-3 to suspend / temporarily disable** the Flock ALPR cameras until a **non-binding May referendum**. KUT's headline says "next year", i.e. May 2027.
- Yes votes: Flores-Cale, Medina, Goza, Zapata. No votes: Harris, McKinney, Tobias (names from Community Impact).
- While suspended, the cameras collect no plate data.
- The referendum covers both the ALPR and drone (DFR) contracts.
- The mayor voted to keep the cameras earlier in the year and switched, citing public opposition (KUT).

**Not confirmed by either fetched page:**
- **The earlier 6-1 vote to continue the contract** (search results put it in early September). Community Impact says only that a budget amendment to cancel two contracts got no second.
- Camera/drone counts and cost (F033's "47 cameras + 2 drones, >$420k/yr" is search-level).
- Texas Scorecard/KXAN's "cover" wording. The fetched outlets say suspend/disable.

**Applied:** F008 in `04_DATA/candidate_leads.csv` was rewritten as a 4-3 suspension (status CORRECTED; original wording kept in the title for the record). F033 is marked CORRECTION_APPLIED_TO_F008. Both Kyle watchlist rows are resolved, and one recheck is set for the May ballot language.

**Britton's call:** Kyle is now a split-then-suspend case, not a clean counter-case. How to code it (or whether it enters the corpus) is a Phase 3 / coding decision.
