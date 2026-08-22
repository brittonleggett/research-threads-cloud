# 2026-08-22 — WebFetch retest, and new developments since 08-14/08-21

## 1. WebFetch status: still blocked (11th consecutive session)

Tested against `https://www.cfodive.com/news/home-depot-warns-tariff-impact-modest-price-hikes/758202/`
— one of the corpus's own Tier-B sources (Home Depot), chosen specifically so a working fetch
would double as progress on the standing Tier-B re-verification task. Result: **`EGRESS_BLOCKED`**,
same failure mode as every prior session back to ~08-13. No change. Not retesting again tomorrow
night on the assumption it's still broken is reasonable, same logic prior sessions used — but
flagging plainly rather than silently: this is now a real, sustained tooling gap, not a one-off.
All research below is WebSearch-summarized only, same confidence caveat as the 08-14 legal-sequence
note (cross-corroborated across independent outlets, but not read from the primary document
myself).

## 2. SCOTUS/IEEPA: refund process has advanced concretely since 08-14 (new info, not a re-flag of the framing question)

The 08-13/08-14 notes pinned down the *legal sequence* (IEEPA struck down Feb 20/terminated Feb 24
→ Section 122 → Section 301) and flagged the framing question for Britton — that question is
unchanged and not reargued here. What's new is the **refund mechanics**, which weren't covered
in either prior note and are now concrete enough to matter for the corpus:

- The government collected roughly **$166 billion** in IEEPA duties from an estimated 330,000
  importers across 53+ million entries.
- CBP built a dedicated system, **CAPE** (Consolidated Administration and Processing of Entries),
  inside the ACE Portal to process refunds at scale rather than entry-by-entry. Phase 1 opened
  April 20, 2026.
- As of early August 2026, roughly **$100 billion (~60%) had been refunded**, per CNBC (2026-08-05:
  [Trump admin refunds $100 billion in 'liberation day' tariffs](https://www.cnbc.com/2026/08/05/trump-tariffs-refunds-ieepa-lawsuit.html)).
  A separate Fox News item references a judge ordering refunds framed around a $130B figure — the
  two numbers weren't reconciled by search (different reporting dates/scopes, most likely), noted
  here as a discrepancy to resolve before citing either figure precisely, not smoothed over.
- Multiple corroborating sources: [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/02/supreme-court-strikes-down-ieepa-tariffs),
  [Penn Wharton Budget Model](https://budgetmodel.wharton.upenn.edu/p/2026-02-20-supreme-court-tariff-ruling/),
  [Norton Rose Fulbright (refunds)](https://www.nortonrosefulbright.com/en/knowledge/publications/20f2de87/potential-refunds-us-supreme-court-overturns-ieepa-tariffs),
  [CBP.gov IEEPA duty refunds page](https://www.cbp.gov/trade/programs-administration/trade-remedies/ieepa-duty-refunds).

**Why this belongs in the paper's orbit, not just the legal-background note:** the refund process
is no longer an abstract legal footnote — it's now generating its own corporate messaging distinct
from the original "we're raising/absorbing prices because of tariffs" framing the whole Study 1
corpus was built to capture. See the Walmart item below, which is exactly that: a corpus company
making a public statement about what it's doing *with a tariff refund*, not about a tariff cost.
This doesn't change the SCOTUS/IEEPA framing call itself (still Britton's, still not decided here)
but it does mean the "two-wave corpus" framing question flagged for Chipotle on 08-21 may actually
need to become a **three-wave** question (pre-IEEPA-ruling / post-ruling-tariff-cost / post-refund)
if any refund-driven statements get added to the corpus. Flagging, not deciding.

## 3. New corporate statements found — one concrete addition, one weak lead, several null results

Checked all named corpus companies (La-Z-Boy, Chipotle, IKEA, Birkenstock, Walmart, Insteel, Home
Depot) for anything published after the 08-21 consolidation. Results:

**Concrete and citable — Walmart, Aug 20, 2026 (Q2 FY2027 earnings call):**
CFO John David Rainey said Walmart received "substantially all" of a **$2.9 billion** IEEPA tariff
refund and is directing it toward price cuts on **11,000 items**, concentrated in grocery and
general merchandise: *"We've taken a disciplined approach to investing these funds back into
customer experience and price leadership, prioritizing investment in grocery and general
merchandise categories."* This is a **different quarter** than either Walmart artifact already in
the corpus (Q1 FY26 and Q2 FY26/2026, both already Tier A) — Q2 FY2027 falls roughly a year later
and is about a refund funding price *decreases*, not a cost driving price *increases*, so it isn't
just an update to the existing entries, it's a structurally different kind of artifact for the same
company. Sources: [CNBC](https://www.cnbc.com/2026/08/20/walmart-wmt-q2-2027-earnings.html),
[CBS News](https://www.cbsnews.com/news/walmart-tariff-refunds-lower-prices/),
[Fortune](https://fortune.com/2026/08/20/walmart-tariff-refunds-prices/),
[CNN](https://www.cnn.com/2026/08/20/business/walmart-tariff-refund).
**Not added to the corpus master file here** — that's a corpus-composition decision (new artifact
count, new code needed for "refund-funded price reduction," interacts with the three-wave question
above) that belongs with the rest of the corpus edits, not slipped in via a side note. Flagging it
as a strong, ready-to-add candidate for whoever next touches the corpus file.

**Also concrete, smaller — La-Z-Boy FY2026 10-K:** per search of La-Z-Boy's own FY2026 10-K
filing, the company states it **became eligible for a refund of tariffs previously paid** on
imported goods following the February 2026 SCOTUS/IEEPA ruling. This directly ties an existing
corpus company (artifact #9, currently Tier B) to the SCOTUS/IEEPA sequence in a way the current
coding doesn't capture — La-Z-Boy's existing codes (`causation-explicit`,
`no-further-increase-anticipated`) are both about the 2025/Jan-2026 cost side, not this refund
side. Not independently verified beyond the search summary (10-K not directly fetched — WebFetch
still blocked); flagged as a lead for the next direct-fetch pass, alongside the four already-queued
Tier-B artifacts.

**Weak, not verified — Chipotle:** found a Q4 2025 earnings call (reported February 2026) in which
CFO Adam Rymer discussed 2026 margin pressure and a planned 1–2% price increase. Some secondary
coverage (Yahoo/Tasting Table) attributes this partly to tariffs, but the CFO quote actually
findable in search (*"margins in 2026 will be under pressure, and it's mostly due to our investment
of taking less price compared to the inflation that we're experiencing"*) doesn't itself name
tariffs as the cause — the tariff attribution is journalistic framing, not a direct Rymer quote in
what search surfaced. This predates the 08-21 consolidation's stated corpus scope in one sense
(Feb 2026 call, before the already-checked Q1 2026 call that "does not mention tariffs at all")
but wasn't previously surfaced in any note. **Not coded, not added anywhere** — flagged only as a
lead that needs a direct primary-source read (or a WebSearch with a more targeted quote-finding
pass) before it's usable, since the current evidence doesn't clearly support a tariff-causation
code.

**Null results (checked, nothing new found):** IKEA, Birkenstock, Home Depot, and Insteel — no
statements found beyond what's already coded in the 08-21 corpus draft. Home Depot's May 2026
"environment is changing almost every day" statement (already coded as the third beat of
`reversal-narrative`) remains the most recent dated statement found for that company. Stated
plainly as a null result, not padded.

## What's open for Britton

- Reconcile the $100B vs. $130B refund-figure discrepancy before either gets cited with precision
  (not urgent, corpus-adjacent only).
- Decide whether to add the Walmart Aug 20, 2026 refund-driven artifact (and possibly a
  corresponding new candidate code) to the corpus — ready to add, not added here since it's a
  corpus-composition call.
- La-Z-Boy's refund eligibility (10-K) is a lead for the next direct-fetch pass, bundled with the
  existing four Tier-B artifacts once WebFetch is restored.
- Chipotle Q4 2025/Feb 2026 call: needs a direct primary-source check before it's usable; not
  action-required otherwise.
- SCOTUS/IEEPA legal-framing call itself: unchanged, not re-argued here, still Britton's.
