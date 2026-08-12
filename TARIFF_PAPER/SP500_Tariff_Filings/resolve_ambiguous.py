"""
Apply manual (LLM-read) resolution of the 227 "ambiguous" filings to
sp500_tariff_filings_classified.csv, write ambiguous_resolved.csv, and merge
into the TRADE / EXCLUDED_utility corpora.

Every one of the 227 was resolvable from its existing ~400-char matched_snippet
(none needed a full-document fetch) — read by hand, classified as trade or
utility_only (railroad/pipeline "public tariff" and FERC/state-PUC rate tariffs
counted as utility_only — same non-trade word sense as electric/gas utility
tariffs, even though not literally "Utilities" GICS sector: NiSource, Norfolk
Southern, Oneok, Williams Companies). No entries needed "irrelevant" or
"still_ambiguous" — all 227 cleanly resolved to one sense or the other.
"""
import csv
import pathlib

HERE = pathlib.Path(__file__).parent
IN_CSV = HERE / "sp500_tariff_filings_classified.csv"
RESOLVED_CSV = HERE / "ambiguous_resolved.csv"
TRADE_CSV = HERE / "sp500_tariff_TRADE_corpus.csv"
UTILITY_CSV = HERE / "sp500_tariff_EXCLUDED_utility.csv"

# 0-indexed positions (in filter order) of ambiguous rows resolved as utility_only.
# Everything else in range(227) resolved as trade.
UTILITY_ONLY_IDX = {
    5, 6, 8, 9, 10, 11, 26, 27, 49, 63, 64, 70, 78,
    125, 126, 127, 128, 129, 130, 131,
    132, 133, 134, 135, 136, 137,
    138, 139,
    145, 146, 147, 148, 149, 150,
    155, 156, 157,
    184,
    224, 225,
    226,
}

NOTES = {
    5: "Legal boilerplate defining 'Governmental Approval' generically (license/permit/tariff/rate) — not trade-tariff discussion.",
    6: "Same generic legal definition boilerplate as above.",
    8: "Ameren Missouri 'large primary service tariff' — MoPSC rate filing.",
    9: "AWK 'srrrs tariff' — residential rate-plan tariff filed with PUC.",
    10: "AWK 'universal affordability discount tariff' — residential rate program.",
    11: "AWK investor slide listing state rate/tariff mechanisms by state.",
    26: "CenterPoint 'special utility tariff' — bond/securitization regulatory mechanism.",
    27: "CenterPoint generic legal definition boilerplate (license/tariff/rate/permit).",
    49: "Constellation Energy 'market rules and procedures... tariff provisions' — ISO/RTO market tariff.",
    63: "DTE 'green tariff program' — utility renewable rate program for customers.",
    64: "DTE 'tariff rates... determined by the mpsc' — Michigan PSC-regulated rates.",
    70: "Entergy 'reduce tariff administrative burdens' — FERC power purchase agreement context.",
    78: "Exelon/ComEd regulatory assets 'recovered under separate tariffs' — rate recovery mechanism.",
    125: "NiSource/NIPSCO 'large load or hyperscale customer... special contract (including any tariff)' filed with IURC.",
    126: "NiSource risk factor: 'changes in... laws, regulations and tariffs... state and federal orders' — generic utility regulatory risk, no trade signal.",
    127: "Same NiSource boilerplate as above.",
    128: "NiSource/NIPSCO large-load special contract tariff, same as idx 125.",
    129: "Norfolk Southern 'public tariff' — common-carrier freight rate schedule (rail industry term of art), not a trade tariff.",
    130: "Same Norfolk Southern rail-tariff boilerplate.",
    131: "Same Norfolk Southern rail-tariff boilerplate.",
    132: "NRG generic legal definition ('applicable law, tariff or regulation').",
    133: "NRG 'market-based rate tariff' — FERC wholesale power authority.",
    134: "Same NRG FERC market-based-rate-tariff boilerplate.",
    135: "Same NRG FERC market-based-rate-tariff boilerplate.",
    136: "Same NRG FERC market-based-rate-tariff boilerplate.",
    137: "Same NRG FERC market-based-rate-tariff boilerplate.",
    138: "Oneok 'refined products tariff rates' — FERC-regulated pipeline transportation tariff, not a trade tariff.",
    139: "Oneok 'tariff-based customers' — pipeline contract structure, same non-trade sense.",
    145: "Pinnacle West XBRL tag 'ArizonaRenewableEnergyStandardAndTariff' — ACC rate program, not trade.",
    146: "Same Pinnacle West XBRL renewable-tariff tag.",
    147: "Same Pinnacle West XBRL renewable-tariff tag.",
    148: "Same Pinnacle West XBRL renewable-tariff tag.",
    149: "Same Pinnacle West XBRL renewable-tariff tag.",
    150: "Same Pinnacle West XBRL renewable-tariff tag.",
    155: "PPL 'new large load customer rate class and electric service tariff' — utility rate filing.",
    156: "PPL 'tariff or other frameworks' — cost allocation among regulated utility subsidiaries.",
    157: "PPL 'rate adjustment mechanisms or tariffs' — KPSC order.",
    184: "Southern Co XBRL tag 'MunicipalAndRuralAssociationsTariff' — Mississippi Power wholesale rate tariff.",
    224: "Williams Companies 'tariff-based customers' — FERC-regulated pipeline contract structure, not trade.",
    225: "Same Williams Companies pipeline-tariff boilerplate.",
    226: "Xcel Energy 'FERC cost sharing tariff' — NSP-Wisconsin/NSP-Minnesota interchange agreement.",
}


def main():
    with open(IN_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())

    ambiguous_positions = [i for i, r in enumerate(rows) if r["classification"] == "ambiguous"]
    assert len(ambiguous_positions) == 227, f"expected 227 ambiguous rows, found {len(ambiguous_positions)}"

    resolved_fields = fields + ["resolved_classification", "resolution_note"]
    with open(RESOLVED_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=resolved_fields)
        w.writeheader()
        for local_idx, row_idx in enumerate(ambiguous_positions):
            r = rows[row_idx]
            if local_idx in UTILITY_ONLY_IDX:
                resolved = "utility_only"
                note = NOTES.get(local_idx, "Utility/regulatory rate-tariff sense, not trade tariff.")
            else:
                resolved = "trade"
                note = "Genuine trade-tariff discussion (cost impact, pricing, trade policy, or macro risk factor framed as trade tariffs)."
            out = {k: r.get(k, "") for k in fields}
            out["resolved_classification"] = resolved
            out["resolution_note"] = note
            w.writerow(out)
            rows[row_idx]["classification"] = resolved  # update in-memory for merge below

    n_trade_new = sum(1 for i in range(227) if i not in UTILITY_ONLY_IDX)
    n_util_new = len(UTILITY_ONLY_IDX)
    print(f"Resolved: {n_trade_new} -> trade, {n_util_new} -> utility_only, 0 irrelevant/still_ambiguous.")

    # Merge into TRADE and EXCLUDED_utility corpora
    with open(TRADE_CSV, encoding="utf-8") as f:
        trade_rows = list(csv.DictReader(f))
        trade_fields = trade_rows[0].keys() if trade_rows else fields
    with open(UTILITY_CSV, encoding="utf-8") as f:
        util_rows = list(csv.DictReader(f))
        util_fields = util_rows[0].keys() if util_rows else fields

    new_trade = [rows[row_idx] for local_idx, row_idx in enumerate(ambiguous_positions) if local_idx not in UTILITY_ONLY_IDX]
    new_util = [rows[row_idx] for local_idx, row_idx in enumerate(ambiguous_positions) if local_idx in UTILITY_ONLY_IDX]

    with open(TRADE_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(trade_fields))
        for r in new_trade:
            w.writerow({k: r.get(k, "") for k in trade_fields})
    with open(UTILITY_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(util_fields))
        for r in new_util:
            w.writerow({k: r.get(k, "") for k in util_fields})

    print(f"Merged {len(new_trade)} rows into {TRADE_CSV.name}, {len(new_util)} rows into {UTILITY_CSV.name}.")

    # Final counts
    with open(TRADE_CSV, encoding="utf-8") as f:
        final_trade = list(csv.DictReader(f))
    companies = set((r["cik"], r["company"]) for r in final_trade)
    print(f"FINAL trade corpus: {len(final_trade)} filings, {len(companies)} unique companies.")


if __name__ == "__main__":
    main()
