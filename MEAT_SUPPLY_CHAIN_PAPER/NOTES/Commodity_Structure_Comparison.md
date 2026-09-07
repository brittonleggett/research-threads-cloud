# Commodity Structure Comparison — Beef, Pork, Poultry

Status: first pass, 2026-09-03. Covers Section 3 of the project brief. Sources
verified primary (USDA ERS) except where noted; see
`SOURCE_VERIFICATION/Evidence_Table_Concentration.md` for the full ledger.

## Why this matters
The brief's instruction to treat beef, pork, and poultry as "related but
distinct supply chains" is well supported by the structural evidence below.
The three commodities differ sharply on (a) how the live animal/bird gets
from grower to processor (open market vs. contract vs. full vertical
ownership) and (b) who bears price risk. Findings should not be pooled across
commodities without checking whether the mechanism under study (e.g., price
transmission, market power) plausibly operates the same way in a fragmented,
open-market structure (cattle) as in a fully-integrated, contract structure
(broilers).

## Summary table

| Dimension | Beef / Cattle | Pork / Hogs | Poultry / Broilers |
|---|---|---|---|
| Dominant procurement model | Still substantially open/cash market at the feedlot-to-packer stage, but a large and contested share moves on formula/contract pricing tied to negotiated cash prices ("captive supply") — the subject of the Cattle Price Discovery and Transparency Act debate. Cow-calf and feedlot stages are mostly independent operations, not owned by packers. | Sharply shifted from open-market to contract: hogs sold under contract/marketing-agreement arrangements rose from ~2% (1980) to ~11% (1993) to ~69% (2004); an additional share is packer-owned. (USDA ERS, AER-777B / related ERS vertical-coordination series.) | Essentially fully contracted: 99.5% of broiler production (by value) raised under production contracts in 2020 (USDA ERS Chart of Note, citing NASS/ARMS data). Integrator owns the birds, feed, and (often) inputs throughout; grower supplies land, labor, housing. |
| Grower compensation mechanism | Cash sale or formula pricing tied to negotiated/cash cattle prices; no tournament system. | Base price plus contract-specific premiums/formulas; less uniform "tournament" structure than broilers, but heavily contract-formula-based since the 1990s–2000s shift. | "Tournament" system: growers are ranked against cohorts raising birds of similar age/breed under similar conditions and paid relative to that cohort's average performance, not a flat per-bird fee — a structure USDA/GIPSA has received two decades of grower complaints about (Federal Register 2023 "Transparency in Poultry Grower Contracting and Tournaments" rule; 2025 "Poultry Grower Payment Systems and Capital Improvement Systems" rule). |
| Vertical integration | Low-to-moderate. Packers do not typically own cattle from birth; captive-supply arrangements (packer-owned or formula-priced cattle scheduled for delivery) are a *partial* integration mechanism and a specific point of controversy, not full ownership of the herd. | High. Large processors (e.g., Smithfield/WH Group) own significant hog production directly in addition to contracting; pork industry structure has followed the broiler model with a lag. | Very high / near-total. Integrators (Tyson, Pilgrim's Pride/JBS, Perdue, Sanderson Farms–Cargill/Continental Grain joint venture, Mountaire, etc.) own the birds and most inputs from hatchery through processing; growers own only land/housing/labor. |
| Four-firm processor concentration (CR4), most-cited recent figure | **85% of steer/heifer slaughter (2019) — matches BOTH the Schaefer-et-al.-attributed Consensus.app synthesis AND USDA AMS PSD's own official Annual Report to Congress figure (read directly 2026-09-05) exactly.** Supersedes the earlier 82% White House CEA estimate. USDA ERS AER-785 historical series shows steer/heifer CR4 at 80% and boxed-fed-beef CR4 at 83% already by 1997 | **67% of hog slaughter (2019) — also matches PSD's official figure exactly.** ERS AER-785 shows hog CR4 at 54% by 1997, so continued rise since | **DISPUTED, see caveat: use 53-55% (USDA AMS PSD's own official 2019-2021 broiler figures, read directly 2026-09-05), not 78%.** A "78% (2019)" figure was adopted 2026-09-03 via an unread AI-search synthesis attributed to Schaefer et al. (2024); PSD's official figure for the same year is 53% — a 25-point gap. As of 2026-09-07, 78% has been independently confirmed as a real figure reported by an overlapping author team, but in a *different*, NETS-data-based 2025 companion paper, not (as best can be determined without a direct read) the FSIS-data-based Schaefer et al. (2024) paper actually cited — plausible citation mix-up, not yet confirmed. See `PROJECT_STATUS.md` Open Decision #6. Poultry is being treated as the least-concentrated of the three commodities on a national-CR4 basis again, per AER-785's original framing, pending resolution. |
| Trajectory since 1980s | Sharpest, most dramatic rise of any of the three — described by USDA ERS itself (AER-785) as "unique," with no other 5-digit Census product class showing as dramatic an increase in any 15-year window (steer/heifer CR4: 36% in 1980 → 80% in 1997 → 85% by 2019, confirmed both by the Schaefer-attributed synthesis and PSD's own official figures). | Large rise, roughly a generation behind beef: hog slaughter CR4 rose from 34% (1980) to 54% (1997) per ERS, to 67% by 2019 (also PSD-confirmed). | **Unresolved, see caveat above — do not cite "78% by 2019" without qualification.** Chicken slaughter CR4 was 41-42% by 1987 per ERS; PSD's own official current-period figure is 53% (2019) → 55% (2021), i.e. a continued but comparatively modest rise, consistent with AER-785's original "not particularly high" framing. A disputed "78% (2019)" figure exists in the literature (see above) but is not yet independently confirmed against the paper it was originally attributed to. |
| Farm-level unit of analysis | Individual cow-calf producers/ranchers (numerous, small, geographically dispersed) plus separate feedlot operators. | Individual hog farms, increasingly consolidated themselves and often contract growers for integrators. | Individual contract growers, structurally analogous to hog contract growers but under the tournament pay system specifically. |
| Where market power concerns concentrate | Packer buyer-side power over numerous independent cattle sellers (monopsony-type concern); captive supply's effect on cash/negotiated price discovery. | Packer buyer-side power plus direct ownership; contract terms and formula pricing. | Integrator power over growers via tournament ranking and contract terms (a *labor/contract-fairness* concern more than a price-discovery concern, since integrators own the birds outright) — this is a structurally different kind of "farmer squeeze" than in beef/pork. |

## Implication for the paper
The "farmer squeezed by processor / consumer squeezed by high prices"
narrative, if it holds at all, likely operates through **different
mechanisms** in each commodity:
- **Beef**: a price-discovery / monopsony story (independent ranchers selling
  into a concentrated, partly captive-supply buyer market).
- **Pork**: a hybrid — moving toward the poultry model (direct ownership +
  contract) but retaining more independent-farm elements than poultry.
- **Poultry**: not really a "price the farmer receives for a commodity" story
  at all, because growers rarely own the birds — it's a **contract-fairness /
  tournament-pay** story. Framing poultry growers as "receiving a low farm
  price for chicken" would misdescribe the actual economic relationship.

This has direct implications for Study 1 corpus design (Section 10) and for
which theoretical lens fits which commodity (`THEORY_CANDIDATES.md`) — e.g.,
distributive/procedural justice and dependence theory may fit poultry grower
contracts better than a classic price-transmission framing does.

## Open items for a follow-up pass
- Need current (2022–2024) CR4/HHI figures directly from USDA AMS Packers &
  Stockyards Division annual reports or the peer-reviewed Schaefer et al.
  (2024, *Review of Industrial Organization*) update — see
  `LITERATURE/Market_Concentration_Evidence.md` for verification status; the
  2023 USDA working-paper PDF returned HTTP 403 on direct fetch and the
  published journal version is paywalled. Britton may have journal access
  worth using to pull exact current figures.
- Have not yet verified current ownership share of hog production held
  directly by Smithfield/WH Group vs. contract growers — flagged as
  "Pending" in the evidence table, not yet a verified figure in this memo.
- Cattle captive-supply share and the Cattle Price Discovery and
  Transparency Act's current status not yet researched in depth — belongs
  with Section 8 (price transmission) as much as Section 3.
