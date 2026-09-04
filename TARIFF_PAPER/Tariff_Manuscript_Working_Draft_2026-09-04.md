# Tariff Messaging and Consumer Response — Working Manuscript Draft
### Assembled 2026-09-04 for Britton's weekend writing/editing session

**What this file is:** everything currently "manuscript-ready" pulled into one document,
in reading order, so you can work top to bottom instead of jumping between files. Nothing
new was written here — this is assembly of already-drafted, already-reviewed material,
plus one genuinely new piece (the Measures subsection below, written in prose for the
first time from the already-resolved scale citations in `notes/2026-08-04-full-
instrument-assembly.md`). Source files, unchanged and still the working copies if you'd
rather edit there instead: `Introduction_and_Theory_DRAFT_2026-08-12.md` and
`Study1_Methods_Section_DRAFT_2026-09-04_CONSOLIDATED.md`.

**Update 2026-09-04, later same day, walked back:** you initially said to include my
judgment on the remaining open calls (H3 direction, the three Phase 3 decisions), then
asked to hold off and review the decision sheet yourself first — right call, since
Phase 3 is this project's one explicitly researcher-only step.
**The Results paragraph and Coding Procedure section below are PROVISIONAL** — drafted
from Claude's proposed resolutions so you have something concrete to react to, but not
confirmed by you and not to be treated as final. Full reasoning for all four open
calls, still unconfirmed: `Study1_Phase3_Quick_Decisions_2026-09-04.md`.

Everything else below is either done or waiting on data that doesn't exist yet (Study
2/3 empirical results — correctly not written, per the project's own rule against
writing results before real data exists).

---

# Introduction

In 2026, tariff-driven price increases moved from a macroeconomic abstraction to a
line item on the receipt. A KPMG survey of executives that year found 55% planning
further price increases within six months, and — more tellingly — the share of firms
passing more than half of tariff-related costs directly to consumers roughly doubled
year over year, from 13% to 34%. Firms as varied as Nike, Mattel, BMW, and Williams-
Sonoma have all publicly attributed price increases to tariffs within the same
calendar year, using markedly different language to do it: Nike's "surgical price
increase," paired with a visible sourcing-shift narrative; BMW's routine-sounding
dealer bulletin that avoids the word "tariff" entirely; Chipotle's public promise to
absorb the cost rather than pass it on. This variation is not noise. It is a natural
experiment in corporate framing that consumers are exposed to, evaluate, and respond
to — and it raises a question with real theoretical and managerial stakes: **does how
a firm explains a tariff-driven price increase change how fairly consumers judge it,
independent of the price increase itself?**

This paper addresses that question in two studies. Study 1 inductively derives a
typology of real corporate tariff-messaging strategies from a corpus of public
disclosures, identifying causation attribution — whether firms explicitly name
tariffs as the cause, offer a vaguer justification, or say nothing at all — as the
messaging dimension with the clearest theoretical stakes and the most real-world
variation. Study 2 experimentally manipulates that dimension, crossed with whether the
firm frames itself as passing the full cost through or absorbing part of it, in a 3×2
between-subjects design, and traces its downstream consequences through perceived
fairness and opportunism to trust and behavioral intentions.

The contribution is threefold. First, we extend dual entitlement theory (Kahneman,
Knetsch, & Thaler, 1986) — developed to explain fairness judgments about price
increases in general — to the specific, increasingly common case of tariff-attributed
increases, where the "external shock" firms invoke as justification is itself
politically contested and unevenly understood by consumers. Second, we ground the
experimental stimuli in an inductively derived typology of *actual* firm messaging
(Study 1) rather than researcher-generated hypotheticals, addressing a common critique
of vignette-based pricing research — that manipulated scenarios don't reflect how
firms actually communicate. Third, we respond directly to this special issue's
interest in marketing's response to external, non-market forces by treating tariff
policy not as background economic context but as a communication problem with
measurable consequences for trust and purchase behavior.

# Theoretical Background and Hypothesis Development

### Dual Entitlement and the Attribution of Cost

Dual entitlement theory (Kahneman et al., 1986) holds that consumers judge a firm
entitled to pass through cost increases it did not cause, but not entitled to raise
prices simply because it can. The theory's central mechanism is *attribution*: the
same price increase is judged differently depending on whether it is understood as a
cost pass-through or a profit grab. Tariffs offer a theoretically interesting test
case precisely because the "external shock" is not a neutral, undisputed fact the way
a raw-material price spike might be — it is a policy outcome that consumers may
attribute to the firm's own strategic choices (where to source, whether to lobby
against it) as much as to circumstances beyond the firm's control. This makes the
firm's own framing of causation unusually consequential: absent a clear attribution
cue, consumers must infer intent, and inference is where perceived opportunism creeps
in (Campbell, 1999).

Study 1's corpus illustrates the range of attribution strategies firms actually use,
from Williams-Sonoma's explicit, section-number-citing transparency ("Section 232,"
"Section 301") to BMW's dealer bulletin that frames a price increase as routine
business ("in line with past pricing communications") without naming a cause at all.
We predict that explicit attribution increases perceived fairness and decreases
perceived opportunism relative to vague or absent attribution, because it supplies the
causal information dual entitlement theory identifies as the basis for a fairness
judgment in the first place:

> **H1a.** Explicit tariff attribution leads to higher perceived price fairness than
> vague or silent attribution.
> **H1b.** Explicit tariff attribution leads to lower perceived opportunism than vague
> or silent attribution.

### Psychological Reactance and the Cost of Silence

Where dual entitlement explains *why* attribution matters, psychological reactance
theory (Brehm, 1966) explains why its absence is not merely uninformative but
actively counterproductive. A price increase presented without explanation removes
the consumer's ability to evaluate whether it is justified, which reactance theory
predicts will be experienced as a constraint on the consumer's freedom to make an
informed choice — provoking resistance disproportionate to the economic magnitude of
the increase itself. This motivates treating silence not as a neutral baseline but as
the condition most likely to provoke the sharpest fairness penalty, consistent with
Study 1's finding that BMW's silent-attribution artifact was also its most
routine-normalizing one — a combination that, per reactance logic, may minimize
apparent imposition in the moment while still measuring worse on trust downstream
because consumers were denied the information to judge for themselves.

### Cost-Response and the Signal of Restraint

The second manipulated factor — whether the firm frames the price increase as a full
pass-through or a shared-burden absorption of part of the cost — maps onto dual
entitlement's other core prediction: firms that visibly absorb part of a cost increase
signal restraint, and restraint is itself evidence against an opportunistic motive.
Study 1's Theme 1 (restraint signaling) and Theme 3 (mitigation-effort narrative) are
both, at root, firms trying to claim this signal — Nike's "surgical" framing, Lovesac's
disclosed four-part mitigation strategy that cost the firm over $22 million in absorbed
margin. We predict:

> **H2a.** Shared-burden cost absorption leads to higher perceived price fairness than
> full pass-through.
> **H2b.** Shared-burden cost absorption leads to lower perceived opportunism than full
> pass-through.

### The Interaction: Attribution and Response Together

Dual entitlement theory implies these two factors should not simply add — a firm that
explains its reasoning *and* visibly shares the burden should be judged disproportionately
more fairly than either cue alone would predict, because together they supply both halves
of what the theory says a fair pass-through requires: a legitimate cause, and evidence the
firm isn't exploiting it. Conversely, a firm that stays silent about cause *and* passes
the full cost through supplies neither — the condition dual entitlement theory would
predict as least defensible, and the condition Study 1's corpus suggests is rarest in
practice, perhaps because firms themselves anticipate this penalty.

> **H3.** Attribution Frame and Cost-Response interact such that the fairness benefit of
> explicit attribution is amplified when paired with shared-burden absorption, and
> attenuated when paired with full pass-through.

**[OPEN — your call]** Is this the direction you'd actually predict for H3? See item 2
in the source file's checklist.

### From Fairness Judgments to Trust and Behavior

The chain from perceived fairness and opportunism to downstream brand outcomes follows
an established path in the pricing-fairness literature: fairness judgments and
attributed motive both shape trust (Chaudhuri & Holbrook, 2001), and trust in turn
predicts the two behavioral intentions most relevant to a firm managing a tariff-driven
price increase — whether the consumer still buys, and whether they say anything about
it to others.

> **H4a.** Perceived price fairness is positively associated with trust in the company.
> **H4b.** Perceived opportunism is negatively associated with trust in the company.
> **H5a.** Trust in the company is positively associated with purchase intention.
> **H5b.** Trust in the company is positively associated with word-of-mouth intention.

---

# Study 1: Method

### Purpose and Theoretical Framing

Study 1 addressed an inductive research question — how do firms discursively frame
tariff-driven price increases to consumers and investors, and what typology of
messaging strategies emerges from actual market practice — with the explicit goal of
grounding the experimental stimuli for Study 2 in real-world messaging patterns rather
than researcher-generated hypotheticals. The analysis was informed by three
theoretical lenses: dual entitlement theory (Kahneman, Knetsch, & Thaler, 1986), which
holds that firms are perceived as entitled to pass through unavoidable cost increases
but not to raise prices opportunistically; prospect theory's framing effects
(Kahneman & Tversky, 1979; Tversky & Kahneman, 1981); and psychological reactance
theory (Brehm, 1966), which predicts resistance to price changes perceived as
unexplained or non-consensual.

### Data

The corpus consisted of publicly available corporate communications — earnings-call
transcripts, official press statements, and price bulletins — addressing tariff-driven
pricing decisions, drawn from **15** firms spanning apparel/footwear, toys, automotive,
HVAC, building materials, home goods, furniture, general merchandise, steel/industrial,
and food service. As of the final verification pass (2026-08-29), **14 of the 15
artifacts are Tier A** (primary-fetched — an official transcript, press release, or
investor-relations page directly read, or an on-the-record statement to a named outlet
cross-corroborated across independent sources). The remaining Home Depot artifact is
Tier B for two of its three messaging beats; its central beat is itself Tier A. One
artifact (Chipotle) is Tier C — its quote is confirmed accurate, but it is dated
roughly a year earlier than the rest of the corpus, raising a scope question addressed
under Coding Procedure below. Because the corpus consists exclusively of publicly
available corporate disclosures with no interaction with or data collection from human
subjects, Study 1 was determined exempt from IRB review under 45 CFR 46.102(e).

### Analytic Approach

Consistent with a growing body of methodological guidance on AI-assisted qualitative
analysis (Braun & Clarke, 2006, 2019; Xu, 2026; Naeem, Smith, & Thomas, 2025), Study 1
employed a **small-q, coding-reliability thematic analysis** — distinct from Braun and
Clarke's "Big Q" reflexive tradition, which treats researcher subjectivity as the
locus of quality and explicitly rejects reliability statistics as a validity marker.
Because Study 1's themes were intended to ground a confirmatory quantitative program
(Study 2's experimental manipulation, Study 3's structural model), a coding-reliability
framing — in which agreement between coders is reported as evidence of trustworthiness
— was the methodologically consistent choice.

Coding was conducted through a human–AI collaborative workflow using Claude (Anthropic),
following an established six-phase procedure adapted from Naeem et al. (2025) and
consistent with the practice documented in Xu (2026) and Goyanes, Lopezosa, and Jordá
(2025): (0) optional quantitative triage of the corpus, (0.5) briefing the model on the
research question, data source, and theoretical frame, (1) deductive and inductive
coding of individual artifacts, (2) clustering of codes into candidate themes, (3)
review and refinement of candidate themes, (4) definition and naming of finalized
themes, and (5) write-up. **[PENDING — Phase 3 (theme review) not yet completed by the
researcher.]** Claude has proposed candidate resolutions for each open clustering/scope
decision, with supporting evidence summarized for each, in
`Study1_Phase3_Quick_Decisions_2026-09-04.md` — Britton's independent review of those
proposals is still outstanding. Consistent with the precedent established in Xu
(2026), the project's standing intent is for Phase 3 to be conducted by the
researcher, not generated by AI; the exact final language here (researcher-only vs.
recommend-and-confirm) depends on how that review actually goes and should be set
once it's done, not before.

### Reliability and Validity

The growing empirical literature on LLM-assisted thematic and qualitative coding
provides a basis for confidence in this approach while also indicating its limits.
In a blinded comparison against human analysts, Hill et al. (2026) found Claude 4
Sonnet achieved deductive-coding agreement (93.5%; Gwet's AC1 = .93) statistically
indistinguishable from, and numerically exceeding, trained human coders (92.7%;
AC1 = .92) on a comparable corpus. AlGhamdi (2026), evaluating Claude Code
specifically against a human/NVivo baseline, reported a pattern of **hierarchical
convergence**: agreement at the level of individual codes was more variable than
agreement at the level of higher-order themes, and structured, multi-phase prompting
produced more stable alignment than single-shot prompting — the prompting approach
adopted here. Both studies, along with Misra et al. (2026) and prior work in this
literature, converge on a consistent pattern: agreement is highest for
descriptive/semantic coding and lower for latent, interpretive coding.

**[PENDING]** A validation pilot has not yet been conducted for this corpus — confirm
with the grad assistant whether the blind-coding worksheet has been completed.

### Coding Procedure and Themes

**[PROVISIONAL — Phase 3 not yet confirmed by Britton.]** The seven-theme structure
below is Claude's proposed resolution, not a completed researcher review — see
`Study1_Phase3_Quick_Decisions_2026-09-04.md` for the open decisions this depends on.
If your own review lands differently, this section (and the Results paragraph below
it) needs to change with it. Proposed themes, pending confirmation: (1) restraint signaling, (2) causation attribution, (3) mitigation-effort
narrative (encompassing three quantified variants surfaced during verification:
partial pass-through, partial absorption, and quantified cost-absorption), (4)
normalization through relabeling, (5) asymmetric disclosure (single-case, reported as
an exploratory observation rather than a stable pattern), (6) full-absorption promise
(single-case, Chipotle, scoped as a bounded earlier-wave observation — see Results),
and (7) reversal narrative (Home Depot), a temporal pattern distinct from the other six
static framing strategies. La-Z-Boy is treated as a boundary/counter-example case
(limited tariff exposure via domestic manufacturing) rather than a pass-through
exemplar; `section-232-specific` is retained as a legal-basis metadata tag, not a
thematic code.

### Results

**[PROVISIONAL — written from the unconfirmed theme structure above; treat as a
draft to react to, not a finished section.]**

Across the 15-artifact corpus, causation attribution (Theme 2) was the most
consistently present dimension, ranging from Williams-Sonoma's section-number-citing
transparency ("Section 232," "Section 301") to BMW's dealer bulletin, which frames a
price increase as routine business without naming a cause at all — the clearest
real-world instantiation of the silent-attribution condition manipulated in Study 2.
Firms rarely stopped at naming tariffs as a cause; explicit attribution was typically
paired with a restraint or mitigation signal (Themes 1 and 3), consistent with the
theoretical logic that firms seek to be judged not only as truthful but as
non-opportunistic. Nike's "surgical price increase," framed alongside a visible
sourcing-shift narrative, and Lovesac's disclosed four-part mitigation strategy — which
the company quantified at over $22 million in absorbed gross margin — represent the
clearest cases: both name tariffs explicitly and visibly bear part of the cost, the
joint condition H3 predicts should draw the strongest fairness response. Theme 3 also
captured three more granular variants once the corpus was verified against primary
sources: IKEA's explicit partial pass-through (raising Uppland sofa pricing from $849
to $899 while stating it "can't stay immune to absorb all the costs" itself),
Birkenstock's quantified partial-absorption logic (a price increase held to roughly 2.5
times the tariff cost rather than passed through in full, explicitly framed against the
company's identity as "a democratic brand"), and Lovesac's own quantified absorption
figure above — together suggesting that when firms do share the burden, they
increasingly attach a number to the claim rather than asserting restraint in the
abstract, a pattern not anticipated at the design stage and worth noting as a
descriptive finding independent of the experimental hypotheses.

A smaller set of firms took the opposite approach, framing price changes as routine
rather than exceptional (Theme 4: normalization through relabeling) — Dormakaba's
press language recast a tariff-driven increase as part of an ongoing growth strategy
rather than a one-off response to policy. GMS's surcharge notice, which explained a
price *increase* by citing tariffs but left a subsequent price *decrease*
unexplained, is the corpus's clearest instance of asymmetric disclosure (Theme 5) —
retained as a single-case, exploratory observation rather than a generalizable
pattern, since no other artifact in the corpus exhibited the same pairing.

Two artifacts illustrate boundary conditions the typology above does not fully
capture. La-Z-Boy raised prices in 2025 but explicitly attributed its expectation of
*no further* increases to near-total domestic manufacturing — a statement about
limited tariff exposure rather than a fairness-messaging strategy, and a useful
counter-example showing the corpus captures variation in firms' actual cost exposure,
not just in how exposed firms choose to communicate. Chipotle offered the corpus's
only clean full-absorption promise ("It is our intent... to absorb those costs") but
the statement is dated March 2025 — roughly a year before the rest of the corpus and
before the February 2026 SCOTUS ruling that reshaped the legal basis for tariff
authority (see `notes/2026-08-14-scotus-ieepa-legal-sequence-confirmed.md`). It is
retained here as illustrative of the theoretical possibility of full absorption, with
its earlier dating reported transparently rather than treated as contemporaneous with
the rest of the sample. Finally, Home Depot's messaging shifted across three dated
statements from an initial no-broad-increases position (May 2025) to acknowledging
"modest price movement in some categories" (Aug 2025) to citing accelerating cost
pressure (May 2026) — a reversal narrative (Theme 7) that, unlike the other six themes,
describes a change in position over time under sustained pressure rather than a fixed
framing choice, and is reported separately for that reason.

### AI-Use Disclosure

**[Exact final language depends on how Phase 3 review actually goes — left unresolved
on purpose rather than pre-written.]** Consistent with emerging disclosure norms in
this literature (Xu, 2026; Naeem et al., 2025), the authors disclose that AI assistance
(Claude, Anthropic) was used in corpus coding (Phases 1–2) and theme-naming support
(Phase 4). Whether Phase 3 (theme review) was conducted by the researcher alone or
involved reviewing AI-proposed candidate resolutions is not yet settled — see
`Study1_Phase3_Quick_Decisions_2026-09-04.md` — and this disclosure should be written
to match whichever actually happens, not the other way around.

---

# Study 2 & Study 3: Measures
### (New prose, written 2026-09-04 from resolved scale citations — first time this exists as manuscript text rather than a working note)

Five scales were used across Studies 2 and 3, adapted from the vignette-based ("the
message"/"Meridian Home") framing for Study 2 to the recalled-experience framing
("the retailer"/"this experience") for Study 3. All items used 7-point Likert
response formats unless otherwise noted.

**Perceived price fairness** was measured with two items from Campbell (1999, Study 2):
a bipolar item ("very fair" to "very unfair") and a reverse-scored agreement item ("This
price is not fair," "strongly agree" to "strongly disagree"), averaged after reverse-
scoring. The original study reports r = .84 (p < .0001).

**Perceived opportunism** was measured with two items adapted from Campbell's (2007)
extension of the same inferred-motive construct: a motive rating ("bad" to "good") and
an agreement item ("The intent in this situation was to take advantage of you [the
customer]," "agree" to "disagree" — reverse-coded relative to the instrument's other
items).

**Trust in the company** was measured with four items from Chaudhuri and Holbrook
(2001): "I trust this company," "I rely on this company," "This is an honest company,"
and "This company is safe."

**Purchase intention** was measured with a three-item scale attributed to Dodds,
Monroe, and Grewal (1991), following the verbatim reproduction in Grewal, Krishnan,
Baker, and Borin (1998, *Journal of Retailing*, 74(3), 331–352, Table 1): "I would
purchase this [product]," "I would consider buying at this price," and "The
probability that I would consider buying [this product] is [high]" (original item
reliabilities .92, .90, and .94 respectively; composite reliability = .92).

**Word-of-mouth intention** was measured with the three-item Favorable WOM scale from
Maxham and Netemeyer (2002, *Journal of Marketing*, 66[4], 57–71, Appendix A),
genericized from the original banking-services context: "How likely are you to spread
positive word-of-mouth about [company]?," "I would recommend [company]'s [products/
services] to my friends," and "If my friends were looking for [a product/service like
this], I would tell them to try [company]" (original coefficient alpha range .83–.97
across measures and time periods).

**[NOTE for Britton: Purchase Intention above uses the Grewal et al. (1998) secondary
source, not the 1991 original — see the confirm-or-override flag in
`notes/2026-08-04-full-instrument-assembly.md` item 9. If you pull the actual 1991
appendix this weekend, this paragraph is a 2-minute edit, not a rewrite.]**

---

# What's not written yet (correctly)

- **Study 2 Results, Study 3 Results** — no data collected; IRB not yet submitted.
- **Discussion, Implications, Limitations, Conclusion** — depend on the above.
- **Full reference list** — every citation above traces to a real source found and
  read directly in this project's own research (Campbell 1999/2007, Chaudhuri &
  Holbrook 2001, Grewal et al. 1998, Dodds et al. 1991, Maxham & Netemeyer 2002, Hill
  et al. 2026, AlGhamdi 2026, Braun & Clarke 2006/2019, Xu 2026, Naeem et al. 2025,
  Goyanes et al. 2025, Misra et al. 2026, KPMG 2026 survey), with full bibliographic
  detail available in the notes cited inline above. The theoretical-foundation
  citations (Kahneman, Knetsch, & Thaler 1986; Kahneman & Tversky 1979; Tversky &
  Kahneman 1981; Brehm 1966) are classic, well-known citations that predate this
  project's own verification pipeline — worth one quick check of exact journal/
  volume/page details before the reference list is finalized, same as everything else
  got checked.
