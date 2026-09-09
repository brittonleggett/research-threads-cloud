# Social Cost of Gambling — Theoretical Constraints on This Project

_Compiled 2026-09-04, from Walker & Barnett (foundational critique), the classic "Methodological Issues in the Social Cost of Gambling Studies" (Journal of Gambling Studies), and a 2025 scoping review of social-cost-of-gambling methodologies (ScienceDirect). See `literature_map.md` Section E for full citations._

## The core methodological problem

Gambling social-cost research borrowed its framework from cost-of-illness (COI) studies of alcohol and drugs — direct costs (healthcare, treatment) plus indirect costs (productivity loss). Walker & Barnett's central critique, which the field still has not resolved as of the 2025 scoping review: most published estimates use an **ad hoc, "common sense" definition of what counts as a social cost**, rather than starting from the economic definition of an externality (a cost imposed on a third party who did not consent to bear it, not internalized in the transaction).

The 2025 scoping review confirms this is still live: existing social-cost-of-gambling estimates vary enormously depending on (1) which cost categories are included, (2) how each is monetized, (3) what level of "problem gambling" is assumed to generate costs, and (4) how causality is handled (attribution vs. correlation). There is no consensus formula this project can adopt off the shelf.

## What this means for our brief's proposed quantities

Section 3 of the kickoff brief proposes two illustrative quantities: Net Public Benefit (fiscal benefits − monetized external costs) and a Social Cost Ratio (external costs ÷ state revenue). Walker & Barnett's framework says: **these are only defensible if every cost term in them is a true externality, not a transfer.**

### Categories to EXCLUDE from any cost estimate (per Walker/Barnett + the classic methodological-issues paper)

- **Gambling losses themselves.** A bettor who loses $500 to a sportsbook has not created a social cost — that $500 is a transfer from bettor to firm (and via tax, partly to the state). Counting it as a "cost" double-counts the same dollar the revenue side already claims as a benefit.
- **Private debt with no external effect.** If someone borrows against their own future income to keep gambling and repays it without affecting anyone else, that is a private welfare loss (potentially large), not a social cost in the externality sense — unless it produces a downstream cost someone else bears (see below).
- **Voluntary consumption expenditure** by a non-problem gambler who enjoys betting as entertainment. Textbook consumer-surplus reasoning says this is a benefit to the bettor, not a cost to society, however uncomfortable that feels normatively.

### Categories that MAY qualify as genuine external/public costs — subject to the 6-part test the brief requires (Section 11) for each one

For every candidate below, the brief requires answering: (1) why it's external, (2) who bears it, (3) how measured, (4) how monetized, (5) double-counting risk, (6) causal attribution realism.

| Candidate cost | External? Who bears it | Measurement path | Double-counting risk | Causal attribution difficulty |
|---|---|---|---|---|
| Publicly funded gambling-treatment programs | Yes — taxpayers fund it regardless of whether the bettor consents | State health department treatment-admission counts + program budgets | Low, if kept separate from private treatment spending | Moderate — need treatment admissions specifically coded as gambling-related, and a plausible link to legalization timing |
| Bankruptcy administrative costs (court system costs, not the debt itself) | Yes — court system, other creditors in a bankruptcy pool | US Courts bankruptcy filing data; administrative cost estimates from bankruptcy-system research | Low, if separated from the debt discharge amount itself (which is a private/transfer loss to creditors, arguably a private cost not a public one) | High — Hollenbeck et al. show a correlational bankruptcy increase tied to state-level legalization timing, not individual gambling-caused bankruptcy |
| Uncompensated healthcare / crisis-care utilization tied to gambling disorder or associated mental-health crises | Yes, when uncompensated (hospital absorbs cost, or Medicaid/public insurance pays) | CDC/BRFSS, SAMHSA treatment admissions, state Medicaid claims where accessible | Moderate — must avoid double-counting with treatment-program line above | High — very few datasets code "gambling-caused" as a specific admission reason |
| Domestic/intimate-partner-violence response costs (policing, courts, shelters) — motivated by Matsuzawa & Arnesen's finding | Yes — third party (the abused partner, and public safety systems) bears the cost, not the bettor | NIBRS incident counts (as in Matsuzawa & Arnesen) × average public cost-per-IPV-incident estimates from criminal-justice research | Moderate — need a defensible per-incident public cost figure from a source outside this project's own literature | High — Matsuzawa & Arnesen identify an amplification effect (interaction with emotional cues), not a simple average causal effect size easy to multiply into a dollar figure |
| Public assistance (SNAP/TANF) drawn by gambling-related financial distress | Potentially — if legalization causally increases enrollment | SNAP/TANF administrative data by state/year | Low | Very high — no study located this session establishes this causal link for sports betting specifically; would be a genuinely novel (and speculative) claim |
| Productivity losses (missed work, reduced performance) | Contested — Walker & Barnett are explicit that "lost productivity" is one of the most commonly *misused* categories in this literature, often assumed rather than measured | Would require employer-side or BLS data on absenteeism tied to gambling — none identified this session | High — classic double-counting trap (the literature review flags this explicitly) | Very high — recommend **excluding this category** unless a much stronger data source is found; it is the single most-criticized line item in the social-cost literature |

## Bottom line for the project

A **full, defensible dollar-for-dollar Net Public Benefit or Social Cost Ratio calculation is not currently supportable** with publicly available data and current causal evidence — several of the categories above have plausible mechanisms but no dataset that cleanly isolates the "external, gambling-caused, non-transfer" portion of the cost. This directly shapes the GO/MODIFY/STOP call in `PROJECT_STATUS.md`: Design A (the literal net-benefit calculation) is the most theoretically ambitious version of this project and the hardest to execute credibly; the brief's own Section 11 instruction — "if full monetization cannot be defended, recommend a different design rather than forcing a dubious aggregate dollar estimate" — points toward one of the non-monetized designs (B, C, or D in `candidate_designs.md`) as more executable without violating the "don't force significance / don't force a dubious dollar estimate" ground rules.
