# 2026-08-16 — Fleshing out the 2026-08-04 corpus-supplement candidates (WebSearch only)

## Tooling caveat up front
`WebFetch` tested against `www.dce.louisiana.gov` and returned `EGRESS_BLOCKED` again tonight
— fourth consecutive session with this exact failure (2026-08-13, 08-14, 08-15, now 08-16).
Also tested a direct `curl` from the Bash shell tonight as a fallback: `CONNECT tunnel failed,
response 403` — so this isn't a WebFetch-tool-specific limitation, it's the whole session's
network egress. **Practical consequence for this project specifically:** unlike
DATA_CENTER_PAPER (whose "corpus" is a markdown file of summarized artifacts, which WebSearch
summaries can populate directly), `CCS_PAPER/Corpus_1/` is a folder of actual downloaded PDF
files feeding a Python text-extraction pipeline. I cannot add real files to it without fetch
access — doing so by paraphrasing WebSearch summaries into fake "PDF" content would violate the
no-fabrication rule. So tonight's work is **research/prep, not corpus population**: fleshing
out the substance of the 6 candidates the 2026-08-04 note only named, plus the systematic
40+-bill sweep that note flagged as unfinished, so that whoever does the actual fetch pass
(human or a future WebFetch-working session) has a scoped, prioritized list instead of starting
from six bare names.

## The 6 original candidates, fleshed out

**1. DCE public rebuttal (Feb 2026)** — responds directly to the EIP report below. Secretary
Dustin Davidson's core counter-claims (per American Press/KALB coverage, not the primary DCE
text): EIP's list of 65 projects "includes many that have been cancelled, contain incorrect
information, are counted twice, or have not yet begun any formal regulatory process." This is a
specific, checkable claim — if Track A's coding ever needs to adjudicate "how many CCS projects
are actually live" as a factual question, DCE's rebuttal and EIP's list are the two documents to
reconcile against each other, not just cite in isolation.

**2. EIP report (Feb 11, 2026)**, now with real numbers beyond the 08-04 note's headline count:
65 projects, most of any state; concentrated in Cameron Parish (11 projects, tied to the LNG
export buildout — direct thematic link to the LNG scouting stream, see below) and Ascension
Parish (10 projects); 30 of the 65 are direct-air-capture, 35 are underground-injection; combined
33M metric tons CO2/year, at least 135M tons cumulative injectable. [EIP report](https://environmentalintegrity.org/reports/65-carbon-capture-projects-proposed-in-louisiana-most-in-u-s/)

**3. Legislative bills — corrected and expanded from the 08-04 note's partial list.** The 08-04
note had HB6/HB7/HB820 as "not yet reviewed." Now confirmed, with outcomes (session appears to
have adjourned sine die):
   - **HB5** (Johnson) — parish-by-parish referendum authority on Class VI wells/sequestration/
     CO2 pipelines. **Failed 7-9** in House Natural Resources Committee.
   - **HB6** (Johnson) — same referendum mechanism, Rapides Parish only (its police jury had
     passed a supporting resolution Dec 8, 2025). Part of a package of **six** parish-specific
     local-option bills (Allen, Beauregard, Rapides, Sabine, Vernon parishes) that **all failed**
     in the same committee session, in a series of 7-8/7-9 votes — this was one committee
     hearing killing the entire local-option strategy at once, not six separate outcomes.
   - **HB7** (Johnson, "Louisiana Landowners Protection Act") — repeal CCS unitization statute +
     remove CO2-pipeline expropriation/eminent-domain authority (reversing a 2020 law). **Failed
     12-7** in House Natural Resources Committee, March 31, after ~5 hours of testimony.
   - **HB820** (Farnum) — CO2 pipeline tracking: manifests from capture through injection,
     10-year retention, inspection rights, permit-revocation exposure if end-use diverges from
     what was approved. **This one appears to have passed** — coverage describes it as enacted,
     unlike HB5/6/7. Worth confirming against the primary bill-status page once fetch access is
     back, since this is a real substantive difference (a passed accountability/tracking measure
     survived while the property-rights and local-control bills all died) that's directly
     relevant to a signaling-theory reading of the legislative session.
   - **Two bills the 08-04 note missed entirely, surfaced tonight:**
     - **HB840** — notice and public-hearing requirements before DCE issues sequestration
       orders/permits/certificates. Procedural-transparency angle, thematically adjacent to
       DATA_CENTER_PAPER's procedural-exclusion theme — worth flagging for Britton as a possible
       cross-paper comparison point (does the CCS corpus show the same procedural-exclusion
       grammar DATA_CENTER_PAPER is finding, just legislated instead of litigated/regulated?).
     - **HB507** (McCormick, Owen, Schamerhorn co-sponsors) — would eliminate the current
       liability caps on CCS storage-facility/pipeline operators and CO2 generators ($250K
       noneconomic-damages cap per person, $500K for wrongful death/permanent injury). Status at
       last check: pending in House Civil Law and Procedure, not yet resolved in what search
       surfaced. If it failed like HB5-7, that's four consecutive industry-skeptical bills dying
       in committee — a pattern worth naming explicitly if it holds.
   - **Session-wide framing, confirmed:** "more than 40 bills" directly concerning or materially
     touching CCS were filed this session — search puts this at roughly double the 2025 count.
     The 5 named above (HB5/6/7/820/840/507 — six, correcting the 08-04 note's "HB6/HB7/HB820"
     framing as "the new ones") are a sample. A systematic pull of the full 40+ list from
     legis.la.gov (filtering by CCS-relevant subject/keyword) is still the right next WebFetch-
     dependent task — tonight's search-based sweep surfaced 3 more named bills than the 08-04
     note had, but that's still nowhere near 40.

**4. Two Class VI permits — status update, both now resolved further than the 08-04 note knew:**
   - **Hackberry Carbon Sequestration** (Cameron Parish, CO2 sourced from Cameron LNG) —
     the 08-04 note said "first draft permit issued since primacy." Correction: that draft was
     April 3, 2025; search tonight indicates HCS **received its final permit in late 2025** —
     Louisiana's first fully-issued Class VI permit, not still in draft. ~2M metric tons CO2/year
     capacity.
   - **Strategic Biofuels / Louisiana Green Fuels** (Caldwell Parish) — draft permit Feb/March
     2026, public hearing held April 9, 2026 as the 08-04 note anticipated (21 of 24 speakers
     supported it, 3 opposed — lopsided public comment, worth noting if public-comment-record
     material becomes a corpus source), and **the final Class VI permit was subsequently
     granted** (per Strategic Biofuels' own June 30, 2026 release plus DCE coverage) — combined
     100MW wood-fired power plant + carbon storage, >1M tons CO2/year target.

## Bottom line for whoever picks this up next
Nothing added to `Corpus_1/` tonight — that still needs a working WebFetch/browsing pass to
pull the actual PDFs/HTML (DCE rebuttal page, EIP report PDF, the 6+ bill texts and digests,
the 2 permit documents) the way every other file in that folder was acquired. What's ready now:
a prioritized, fact-checked target list (6 originally-flagged items now substantively described,
2 additional bills found, all bill outcomes resolved where available) plus one open thread —
whether HB507 passed, failed, or is still pending — to close out on the next fetch-capable pass.
