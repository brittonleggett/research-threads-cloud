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
| Four-firm processor concentration (CR4), most-cited recent figure | ~82–85% of steer/heifer slaughter (White House CEA, Sept. 2021, using ~2021 data; USDA ERS AER-785 historical series shows steer/heifer CR4 at 80% and boxed-fed-beef CR4 at 83% already by 1997) | ~66–70% of hog slaughter (White House CEA 2021; ERS AER-785 shows hog CR4 at 54% by 1997, so continued rise since) | ~50–54% of broiler processing (White House CEA 2021: 35%→54%, 1986 to ~2021); ERS's own framing (AER-785/AER-787 series) is that poultry concentration, while it has risen, "is not particularly high relative to other manufacturing industries" compared with cattle. |
| Trajectory since 1980s | Sharpest, most dramatic rise of any of the three — described by USDA ERS itself (AER-785) as "unique," with no other 5-digit Census product class showing as dramatic an increase in any 15-year window (steer/heifer CR4: 36% in 1980 → 80% in 1997; further to ~82–85% by ~2021 per CEA). | Large rise, roughly a generation behind beef: hog slaughter CR4 rose from 34% (1980) to 54% (1997) per ERS, to ~66–70% by ~2021 per CEA. | Real but comparatively modest rise: chicken slaughter CR4 41–42% by 1987 per ERS (already risen sharply 1977–1987), then relatively stable; ~54% by ~2021 per CEA. ERS's own historical characterization: poultry concentration "is not particularly high" vs. manufacturing generally, unlike cattle. |
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
