# 2026-08-22 — Candidate-code relationships: co-occurrence, definitions, and example quotes (Phase 3 prep)

## What this is and isn't

The 08-21 consolidation surfaced six new candidate codes across the verification passes and
flagged, as an *observation*, that three of them "look like they could be enrichments of existing
Theme 3 rather than distinct themes." That clustering call is Phase 3 — Britton's, not made here.
What this note does instead is lay out the actual evidence underneath that observation more
rigorously: exact definitions, the quotes each code is grounded in, and which codes actually
co-occur with which other codes in which artifacts — so that when Phase 3 happens, the clustering
decision can be made against a clear picture instead of scattered single-line code labels. This is
Phase 1/2 bookkeeping (organizing existing codes), not theme review. No code is merged, dropped,
renamed, or promoted to a theme here.

Source material: `Study1_Corpus_and_Coding_DRAFT_2026-08-21.md` (all quotes/codes below are drawn
from that file, not newly fetched — no new research, just relational analysis of what's already
verified) and, for artifacts 1–7, `Study1_Corpus_and_Coding_DRAFT_2026-07-24.md`.

---

## The six candidate codes: definitions and grounding quotes

**1. `full-absorption-promise`** — Firm states or implies it will absorb the *full* cost of a
tariff itself rather than passing any of it to consumers, at least for now.
- Grounding: Chipotle CEO, NBC interview, 2025-03-02: *"It is our intent as we sit here today to
  absorb those costs."*
- Currently N=1 (Chipotle only). No other artifact in the 15-item corpus makes a full-absorption
  claim — the closest analogues (Lovesac, Birkenstock) are explicitly *partial*-absorption cases.

**2. `no-further-increase-anticipated`** — Firm states it does not expect to raise prices again
even if a specific, named future tariff action takes effect, typically citing a structural reason
(e.g., domestic sourcing) rather than a temporary one.
- Grounding: La-Z-Boy — company said it did not expect to raise prices again if the planned Jan
  2026 furniture-tariff hike (25%→30%) took effect, citing near-total domestic manufacturing. Note:
  the corpus file paraphrases this rather than quoting it verbatim — the exact sentence has not
  been pulled from a primary source yet; flagged here so a direct-fetch pass captures the precise
  wording, not just the paraphrase.
- Currently N=1 (La-Z-Boy). Distinguish from `restraint-language` (which describes *how* a price
  action is framed) — this code describes a forward-looking *non-action* commitment instead.

**3. `partial-absorption-quantified`** — Firm gives a specific ratio or multiplier showing it is
absorbing part of a tariff cost, explicitly framed as a deliberate choice not to pass the full cost
through.
- Grounding: Birkenstock CFO Ivica Krolo (WWD): the price increase "would have to be 2.5x the
  tariffs" to hold margin — implying the actual increase taken was well under that — not done "to
  our customers, being a democratic brand."
- Currently N=1 (Birkenstock).

**4. `partial-pass-through-explicit`** — Firm explicitly states that a price increase reflects only
part of a cost increase, with the remainder implicitly or explicitly absorbed.
- Grounding: IKEA (Ingka Group's Tolga Öncü, to WSJ): prices passed on "part of the cost increase"
  because the company "can't stay immune to absorb all the costs" itself.
- Currently N=1 (IKEA).

**5. `quantified-cost-absorption`** — Firm reports a specific dollar or percentage figure showing
costs it absorbed rather than passed on, typically tied to a visible profitability impact.
- Grounding: Lovesac official IR release: $22M+ in tariff costs absorbed into gross profit (margin
  held at 56.4%); net income fell from $11.6M to $4.1M.
- Currently N=1 (Lovesac). Note this is the only one of the six grounded in a quantified figure
  rather than a quote — worth keeping in mind for Phase 3, since it's evidentially a different kind
  of artifact than the other five (numbers in an official release vs. a spoken/quoted claim).

**6. `reversal-narrative`** — A firm's own public position on whether it will raise prices changes
across two or more dated statements, in response to continued cost pressure.
- Grounding: Home Depot, three-beat sequence — (1) May 2025: publicly said it would *not* raise
  prices broadly; (2) Aug 2025, CFO Richard McPhail: "some modest price movement for some
  categories," "not on a broad scale"; (3) May 2026: further update citing fuel/commodity pressure
  plus new tariffs, "the environment is changing almost every day."
- Currently N=1 (Home Depot) — but see the companion note filed tonight
  (`2026-08-22-webfetch-and-new-developments.md`) for a possible second, much larger instance of a
  *different kind* of reversal (Walmart's Aug 2026 tariff-refund-funded price cuts) that is not
  folded into this code's definition here, since it runs in the opposite direction (price relief,
  not increase) — flagged there as a distinct candidate, not asserted as the same code.

`section-232-specific` (Insteel) is excluded from the tables below — per the 08-21 note it's a
legal-basis metadata tag, not a thematic code, so it doesn't behave like the other five for
co-occurrence purposes.

---

## Co-occurrence: which codes actually appear together, in which artifact

Read literally off each artifact's code list in the 08-21 corpus draft — every code that shares an
artifact with one of the five thematic candidate codes above.

| Candidate code | Artifact | Existing/legacy codes it co-occurs with in that same artifact |
|---|---|---|
| `full-absorption-promise` | Chipotle | `causation-explicit`, `restraint-language`, `hedged-commitment` |
| `no-further-increase-anticipated` | La-Z-Boy | `causation-explicit` (2025 increases only) |
| `partial-absorption-quantified` | Birkenstock | `causation-explicit`, `mitigation-narrative`, `selective/style-by-style-framing` |
| `partial-pass-through-explicit` | IKEA | `causation-explicit`, `numeric-transparency` |
| `quantified-cost-absorption` | Lovesac | `causation-explicit`, `mitigation-narrative`, `restraint-language` |
| `reversal-narrative` | Home Depot | `causation-explicit` (Aug 2025 on), `hedged-commitment` |

Two observations this makes concrete rather than impressionistic:

1. **`causation-explicit` is the one code every single new candidate co-occurs with** — unsurprising
   (it's the most common code in the whole corpus) but worth stating so it isn't mistaken for a
   meaningful pairing.
2. **On the specific "these three might be one enriched Theme 3" question flagged 08-21:**
   `partial-absorption-quantified` (Birkenstock) and `quantified-cost-absorption` (Lovesac) both
   co-occur directly with `mitigation-narrative` in their own artifact. `partial-pass-through-explicit`
   (IKEA) does **not** — IKEA's own code list has no `mitigation-narrative` tag alongside it, only
   `numeric-transparency`. So the three candidates aren't evidentially uniform even under the
   "enrichment of Theme 3" reading: two have a direct same-artifact link to Theme 3's existing code,
   one doesn't. That's a concrete fact for Phase 3 to weigh, not a recommendation either way.

**None of the six new candidate codes co-occur with each other** — each is currently attested in
exactly one artifact, and no artifact carries two of the six. That means every one of these
candidates is currently an **N=1 code**: a single supporting artifact, no internal replication yet.
This is a saturation gap worth naming plainly before Phase 3, separate from the clustering
question — a theme built on N=1 evidence per sub-code is thinner than one where multiple artifacts
independently support the same code, regardless of how the clustering call goes.

---

## Cross-corpus resemblance candidates for a future re-read (not asserted, flagged only)

Checking the six new codes against the **original 7 artifacts'** codes (which predate the
verification passes and haven't been re-read against this new code set) turned up some conceptual
echoes worth a deliberate re-read pass, not asserted as matches here since exact quotes for 1–7
would need re-pulling from the 07-24 draft's sourcing to code with confidence:

- **Lennox's `cost-diffusion`** ("price is one lever among several, not the headline," tariff
  impact $125M "blended into a broader cost-management story") reads similarly in spirit to
  `partial-pass-through-explicit` — both describe a firm treating the tariff cost as one piece of a
  larger picture rather than the sole driver of a price action. Not the same code as currently
  worded (Lennox's is about narrative emphasis, IKEA's is about a quantified split), but close
  enough to be worth a side-by-side re-read.
- **Williams-Sonoma's `high-technical-transparency`** (names specific tariff sections 232/301/122,
  walks through timing/uncertainty) and **Mattel's `numeric-transparency`** ($270M quantified cost)
  both share the "specific-number-as-legitimation" logic underlying `quantified-cost-absorption`,
  though neither is framed around *absorption* specifically — Williams-Sonoma and Mattel both
  disclose numbers about cost, not numbers about how much was *not* passed through. Worth checking
  whether either artifact's primary source actually contains an absorption framing that just wasn't
  captured in the original one-line 07-24 coding.
- **Dormakaba's `reframing-temporary-to-permanent`** is worth noting as a near-opposite of La-Z-Boy's
  `no-further-increase-anticipated` — one firm converts a temporary surcharge into a permanent
  price increase, the other commits to no further increase despite a live tariff threat. If Phase 3
  ends up wanting a "temporal commitment" axis (how firms frame the durability of a price action),
  these two are a natural contrasting pair to anchor it.

These three are flagged as *candidates for a re-read*, not as findings — none of the original 7
artifacts have had their primary sources re-examined against this new code vocabulary, and doing
that re-read is itself more Phase-1/2 groundwork than a Phase 3 decision, so it's a reasonable
next non-blocked task for a future session if Britton wants it done before Phase 3, rather than
during it.

---

## What this buys Phase 3

When Britton sits down to do Phase 3 on the six new codes, this note means he can see, without
re-deriving it: (a) each code's exact grounding quote and its one supporting artifact, (b) that
none of the six have internal replication yet, (c) precisely which existing codes each one already
travels with, and (d) that the "three of six are Theme 3 enrichment" read from 08-21 is only
partially uniform once you check same-artifact evidence directly. None of that decides the
clustering — it just means the clustering call, whenever he makes it, is made against the actual
evidence layout rather than a one-line impression carried over from the verification passes.
