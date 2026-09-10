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

**Update 2026-09-04, Phase 3 finalized by Britton:** after reviewing the decision
sheet independently, Britton confirmed 3 of Claude's 4 proposed resolutions and
overrode the fourth — declining to elevate Home Depot's single-artifact
`reversal-narrative` code to a seventh theme, on the grounds that a single case
doesn't support a new theme, and reporting it as a deviant case instead. **Final: six
themes, not seven.** Full record of the decisions and reasoning:
`Study1_Phase3_Quick_Decisions_2026-09-04.md`. The Coding Procedure, Results, and
AI-Use Disclosure sections below reflect this final state. H3 remains open — Britton
hasn't yet confirmed a direction independently.

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
margin. Cost absorption works as a signal in the formal sense used in signaling theory:
it is costly to fake (Kirmani & Rao, 2000; Connelly, Certo, Ireland, & Reutzel, 2011) —
a firm gains nothing from claiming restraint while still passing the full increase
through, while forgoing real margin is a cost only a firm confident it can absorb would
accept. Verbal attribution, by contrast, costs a firm nothing to state; this asymmetry
matters directly for H3 below. We predict:

> **H2a.** Shared-burden cost absorption leads to higher perceived price fairness than
> full pass-through.
> **H2b.** Shared-burden cost absorption leads to lower perceived opportunism than full
> pass-through.

### The Interaction: Attribution and Response Together

Attribution theory offers a more specific prediction for how these two cues combine
than a simple additive logic would suggest. Kelley's (1972) discounting principle holds
that the causal weight assigned to any one available cue is discounted to the degree
that another plausible cause for the same effect is already present — and Kelley
specifically describes a *compensatory* causal schema for cases where two such causes
are treated as continuous and substitutable rather than independent, each capable on
its own of producing the effect. Cost absorption and explicit attribution both point to
the same underlying inference this paper cares about — that the firm is not acting
opportunistically — which makes them compensatory causes in exactly Kelley's sense
rather than complementary ones. A firm that visibly absorbs cost has already supplied
costly, hard-to-fake behavioral evidence of restraint (see above); once that evidence is
in hand, a stated cause for the price increase has comparatively little left to add,
because consumers already have independent grounds for the fair-intent inference dual
entitlement theory says attribution exists to supply. Full pass-through withholds that
behavioral evidence entirely — which is precisely the condition under which attribution
is doing its full share of the inferential work, since cheap-talk explanation is the
only cue available at all (Campbell, 1999).

This predicts a *compensatory*, cue-substitution interaction rather than a "two good
things amplify each other" one: attribution's fairness benefit should be *larger*, not
smaller, under full pass-through, where it is the only available evidence of fair
intent, and *smaller* under shared-burden absorption, where a costlier behavioral cue
has already done most of that inferential work.

> **H3.** Attribution frame and cost-response strategy interact such that the positive
> effect of explicit tariff attribution on perceived price fairness is stronger when the
> firm fully passes the cost increase through to consumers than when the firm partially
> absorbs the cost.

The discounting principle and its compensatory-schema case are Kelley's own and
well-established in the general attribution literature; applying a costly/cheap
distinction to firm signals is similarly established in signaling theory (Kirmani &
Rao, 2000; Connelly et al., 2011). What is new here is the specific combination: the
field's own standard price-fairness review (Xia, Monroe, & Cox, 2004), read in full
alongside its extensive citation of Bolton, Warlop, and Alba (2003), addresses cost
salience, attribution of responsibility, and controllability individually but neither
tests nor discusses attribution and cost-response as substitutable cues for the same
inferred-motive judgment. So while the discounting logic behind H3 is borrowed, not
invented, the hypothesis itself is this paper's extension of that logic to the
tariff-messaging context, not a replication of a prior finding.

**[RESOLVED 2026-09-10]** Britton reversed the direction and supplied the underlying
logic (compensatory/cue-substitution, not amplification) — see the source file
(`Introduction_and_Theory_DRAFT_2026-08-12.md`) and
`notes/2026-09-10-h3-reversal-literature-check.md` for the literature check.

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
themes, and (5) write-up. Consistent with the precedent established in Xu (2026),
**Phase 3 (theme review) was conducted by the researcher.** Claude surfaced candidate
resolutions for each open clustering/scope decision with supporting evidence
summarized for each (`Study1_Phase3_Quick_Decisions_2026-09-04.md`); the researcher
independently reviewed these, adopted three as proposed, and overrode a fourth —
declining to elevate a single-artifact deviant case (Home Depot's `reversal-narrative`)
to a seventh theme on the grounds that doing so would overstate what one case supports,
finalizing six themes instead of the seven Claude had proposed.

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

**Phase 3 (theme review) completed by the researcher, 2026-09-04** — final decisions
and reasoning in `Study1_Phase3_Quick_Decisions_2026-09-04.md`. Six themes were
finalized: (1) restraint signaling, (2) causation attribution, (3) mitigation-effort
narrative (encompassing three quantified variants surfaced during verification:
partial pass-through, partial absorption, and quantified cost-absorption), (4)
normalization through relabeling, (5) asymmetric disclosure (single-case, reported as
an exploratory observation rather than a stable pattern), and (6) full-absorption
promise (single-case, Chipotle, scoped as a bounded earlier-wave observation — see
Results). La-Z-Boy is treated as a boundary/counter-example case (limited tariff
exposure via domestic manufacturing) rather than a pass-through exemplar;
`section-232-specific` is retained as a legal-basis metadata tag, not a thematic code.
Home Depot's `reversal-narrative` code — a stated position changing over time under
sustained pressure — was deliberately **not** elevated to a seventh theme: with a
single supporting artifact, doing so would overstate what the evidence bears, so it is
reported in Results as an exploratory deviant case instead, the methodologically more
conservative choice.

### Results

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
the rest of the sample.

Home Depot's messaging is reported as a single deviant case rather than folded into
the six-theme typology above. Across three dated statements, its position shifted from
an initial no-broad-increases stance (May 2025) to acknowledging "modest price
movement in some categories" (Aug 2025) to citing accelerating cost pressure (May
2026) — a change in position over time under sustained pressure, which is a
qualitatively different kind of pattern than the other six themes' fixed framing
choices. With only one artifact exhibiting it, elevating it to a seventh theme would
overstate what a single case supports; reported as a deviant case instead, it stays
available as a substantively interesting observation — and a candidate for its own
theme should a larger corpus surface more examples — without inflating the typology
beyond what the evidence bears.

### AI-Use Disclosure

Consistent with emerging disclosure norms in this literature (Xu, 2026; Naeem et al.,
2025), the authors disclose that AI assistance (Claude, Anthropic) was used in corpus
coding (Phases 1–2) and theme-naming support (Phase 4). For Phase 3, Claude surfaced
candidate resolutions with supporting evidence for each open clustering/scope decision;
the researcher independently reviewed these and made the final determination for each,
including overriding one AI-surfaced recommendation (declining to elevate a
single-artifact deviant case to a full theme). All final interpretive judgments were
the researcher's.

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

# References

**Compiled 2026-09-04 from bibliographic detail already established in this project's
own files** (`Overnight_Citation_Verification_2026-07-08.md`,
`notes/2026-08-04-scale-sourcing.md`, `notes/2026-08-04-AI-methodology-justification.md`,
`notes/2026-09-04-purchase-intention-wom-scales-resolved.md`, and
`Claude Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md`, whose citation
list was Crossref-verified 2026-07-08) — not re-researched here, just assembled into
one alphabetical list for the first time. Five entries carry an explicit gap, flagged
inline rather than papered over; everything else below has a confirmed journal,
volume, and page range from this project's own prior verification work.

AlGhamdi, R. (2026). From code variability to theme convergence: AI–human alignment in
thematic analysis with Claude Code. *International Journal of Qualitative Methods*.
https://doi.org/10.1177/16094069261462093

Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative
Research in Psychology, 3*(2), 77–101. **[Not independently verified in this
project's own pipeline — canonical, extremely well-established citation; worth one
quick confirm before submission, same standard applied to everything else here.]**

Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis.
*Qualitative Research in Sport, Exercise and Health, 11*(4), 589–597. **[Same flag as
above — not independently verified in this project's pipeline.]**

Brehm, J. W. (1966). *A theory of psychological reactance*. Academic Press. **[Same
flag — confirmed as a real, foundational citation in the 2026-07-08 verification pass,
but exact publisher detail not independently re-checked since.]**

Campbell, M. C. (1999). Perceptions of price unfairness: Antecedents and consequences.
*Journal of Marketing Research, 36*(2), 187–199.

Campbell, M. C. (2007). Says who?!: How the source of price information and the
direction of price change influence perceptions of price fairness. *Journal of
Marketing Research, 44*(2), 261–271. **[Bibliographic detail now resolved 2026-09-10 —
verified directly against Campbell's own CV (UCR faculty page), not a search summary.
Note: several secondary/citing sources (search engines, a citing paper's own reference
list) give a different subtitle — "...and Affect Influence Perceived Price
(Un)fairness" — for what appears to be the same paper (identical journal/volume/issue/
pages, 44(2) 261–271, across sources); the CV is treated as authoritative since Campbell
is the paper's own author. Still open: the specific scale items attributed to this
paper in the Measures section below (a "bad"/"good" motive rating and a "took advantage
of you" agreement item) have NOT been independently verified against the paper's actual
text — only the bibliographic citation itself was confirmed this pass. Pull the full
text before submission if those exact items matter.]**

Connelly, B. L., Certo, S. T., Ireland, R. D., & Reutzel, C. R. (2011). Signaling
theory: A review and assessment. *Journal of Management, 37*(1), 39–67. **[Added
2026-09-10 for the reversed H3 — citation verified via WebSearch (SAGE/Journal of
Management record); general signal-cost mechanism confirmed, full-text not pulled.]**

Chaudhuri, A., & Holbrook, M. B. (2001). The chain of effects from brand trust and
brand affect to brand performance: The role of brand loyalty. *Journal of Marketing,
65*(2), 81–93. **[CONFIRMED 2026-09-10 — independently re-verified via WebSearch
(SAGE DOI jmkg.65.2.81.18255), exact match.]**

Dodds, W. B. (2002). The effects of perceived and objective market cues on consumers'
product evaluations. *Marketing Bulletin, 13*, Article 2.

Dodds, W. B., Monroe, K. B., & Grewal, D. (1991). Effects of price, brand, and store
information on buyers' product evaluations. *Journal of Marketing Research, 28*(3),
307–319. **[Construct/attribution source for Purchase Intention — exact 1991 item
wording still not directly verified; see the Measures section note above.]**

Goyanes, M., Lopezosa, C., & Jordá, B. (2025). Thematic analysis of interview data
with ChatGPT: Designing and testing a reliable research protocol. *Quality &
Quantity, 59*(6), 5491–5510. **[RESOLVED 2026-09-10 — independently confirmed via
WebSearch; note the manuscript's own draft had a typo on the start page, 5493, off by
2 from the real 5491.]** https://doi.org/10.1007/s11135-025-02199-3

Grewal, D., Krishnan, R., Baker, J., & Borin, N. (1998). The effect of store name,
brand name and price discounts on consumers' evaluations and purchase intentions.
*Journal of Retailing, 74*(3), 331–352.

Hill, C., Dahil, A., Simpson, G., Hardisty, D., Keast, J., Pinn, C. K., &
Dambha-Miller, H. (2026). Large language models for thematic analysis in healthcare
research: A blinded mixed-methods comparison with human analysts. *PLOS Digital
Health, 5*(4), e0001189. https://doi.org/10.1371/journal.pdig.0001189

Kahneman, D., Knetsch, J. L., & Thaler, R. (1986). Fairness as a constraint on profit
seeking: Entitlements in the market. *American Economic Review, 76*(4), 728–741.

Kelley, H. H. (1972). Causal schemata and the attribution process. In E. E. Jones, D.
E. Kanouse, H. H. Kelley, R. E. Nisbett, S. Valins, & B. Weiner (Eds.), *Attribution:
Perceiving the causes of behavior* (pp. 151–174). General Learning Press. **[Added
2026-09-10 for the reversed H3 — the discounting principle and its compensatory
causal-schema case, verified via WebSearch across multiple independent secondary
sources describing the chapter's actual content; the original 1972 chapter text itself
was not directly pulled.]**

Kirmani, A., & Rao, A. R. (2000). No pain, no gain: A critical review of the
literature on signaling unobservable product quality. *Journal of Marketing, 64*(2),
66–79. **[Added 2026-09-10 for the reversed H3 — citation verified via WebSearch
(SAGE/Journal of Marketing DOI record); a direct PDF pull was attempted but this
environment's PDF text-extraction tooling is currently broken (same poppler-utils/
pypdf gap flagged elsewhere in this project), so the costly-vs-cheap-signal mechanism
is confirmed from the abstract/secondary description, not the full text.]**

Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under
risk. *Econometrica, 47*(2), 263–291. **[CONFIRMED 2026-09-10 — independently
re-verified via WebSearch (Econometric Society + RePEc/IDEAS bibliographic record),
exact match.]**

KPMG. (2026). *2026 tariff survey*.
https://kpmg.com/us/en/media/news/kpmg-2026-tariff-survey.html

Maxham, J. G., III, & Netemeyer, R. G. (2002). A longitudinal study of complaining
customers' evaluations of multiple service failures and recovery efforts. *Journal of
Marketing, 66*(4), 57–71.

Misra, R., Dahal, R., Kirk, B., Khan, R., Dogan, G., Chataut, R., & Gyawali, P. (2026).
Large language models in qualitative analysis: Comparing traditional and
researcher-interpreted approaches. *International Journal of Qualitative Methods*.
https://doi.org/10.1177/16094069261426100 **[RESOLVED 2026-09-10 — full author list was
already on record in `Claude_Knowledge/AI_Thematic_Analysis_Reading_List.csv`, just not
yet carried into this reference list; not re-verified against the paper itself this
pass, only cross-referenced against the project's own prior work.]**

Naeem, M., Smith, T., & Thomas, L. (2025). Thematic analysis and artificial
intelligence: A step-by-step process for using ChatGPT in thematic analysis.
*International Journal of Qualitative Methods, 24*, 1–18.
https://doi.org/10.1177/16094069251333886

Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of
choice. *Science, 211*(4481), 453–458. **[CONFIRMED 2026-09-10 — independently
re-verified via WebSearch (Science/AAAS DOI record), exact match.]**

Xia, L., Monroe, K. B., & Cox, J. L. (2004). The price is unfair! A conceptual
framework of price fairness perceptions. *Journal of Marketing, 68*(4), 1–15.
**[Added 2026-09-10 for the reversed H3 — full text pulled and read directly (a real
PDF, not a search summary) to check whether the field's standard price-fairness
review tests or discusses an attribution × cost-response substitution interaction; it
does not, and its own extensive citation of Bolton, Warlop, and Alba (2003) doesn't
either — see `notes/2026-09-10-h3-reversal-literature-check.md`. Bolton, Warlop, and
Alba (2003) itself remains paywalled to this session (JSTOR/Oxford Academic,
ResearchGate, and SciSpace all inaccessible); verified here only through Xia et al.'s
treatment of it, not its own full text.]**

Xu, W. (2026). Doing thematic analysis in the age of generative AI: Practices, ethics
and reflexivity. *International Journal of Qualitative Methods, 25*, 1–14.
https://doi.org/10.1177/16094069261425173

---

# What's not written yet (correctly)

- **Study 2 Results, Study 3 Results** — no data collected; IRB not yet submitted.
- **Discussion, Implications, Limitations, Conclusion** — depend on the above.
- **Reference list gaps — mostly closed 2026-09-10** (see
  `notes/2026-09-10-citation-accuracy-pass.md` for the full verification pass): Campbell
  (2007)'s bibliographic citation, Goyanes et al. (2025)'s page range, and Misra et al.
  (2026)'s full author list are all resolved. Kahneman & Tversky (1979), Tversky &
  Kahneman (1981), and Chaudhuri & Holbrook (2001) were independently re-verified and
  confirmed exact. **One real gap remains**: Campbell (2007)'s specific scale-item
  wording (the "bad"/"good" motive rating and the "took advantage of you" item used for
  H1b/H2b's opportunism measure) has NOT been independently verified against the
  paper's actual text — only its bibliographic citation was confirmed. Braun & Clarke
  (2006, 2019) and Brehm (1966) remain un-re-verified this pass (canonical,
  low-fabrication-risk citations, confirmed real in the 2026-07-08 pass) — still worth
  a final spot-check before submission, same as before.
