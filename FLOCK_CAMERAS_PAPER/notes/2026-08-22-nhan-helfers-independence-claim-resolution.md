# 2026-08-22 — Nhan & Helfers "contractually stipulated researcher independence" claim: resolution attempt

## Status: **still genuinely unresolvable by search tonight** — not confirmed, not confirmed-false.
Softened replacement language drafted below for Britton to drop into the Introduction draft
himself (not applied directly, per the "new files, not overwrites" convention).

## What this pass tried, beyond 2026-08-21's first flag

**WebFetch tested directly, as instructed.** Attempted six fetches across five distinct domains:
`journals.sagepub.com` (the article's own publisher page), `stopflocksafety.org` (an activist
site with an article specifically summarizing this study — the most promising secondary-source
lead found tonight), `www.techdirt.com` (the 2024 reporting on the researchers' earlier
Flock-funded work), `www.researchgate.net` (hosting the earlier white paper), and `www.tcu.edu`
(Nhan's CV, to check for grant/contract language). **Every single fetch failed with
`EGRESS_BLOCKED`** — same result as every prior session. This is the 11th straight session
WebFetch has been unavailable; tonight's test was broader than prior sessions' (five different
domains, not just the target article) specifically to rule out a domain-specific block rather
than a blanket one, and the result is the same across all five: **WebFetch remains fully
non-functional in this environment**, not selectively blocked.

**WebSearch: eight distinct targeted queries tonight**, beyond the single pass 2026-08-21 ran,
specifically hunting for the actual disclosure/funding statement or any secondary source quoting
it directly:
1. General query combining the article title, "funding disclosure," and "Flock Safety"
2. Direct query for "funding," "disclosure," or "conflict of interest" language attached to the
   authors/journal
3. Query on the article's DOI directly
4. Targeted query at the `stopflocksafety.org` summary page specifically (a site whose whole
   purpose is critical coverage of Flock — if anyone would have surfaced and highlighted a weak
   or absent independence clause, it would likely be them, and even their summary apparently
   doesn't quote one)
5. Query for the exact kind of sentence a disclosure statement would use ("this research was
   funded," "declared no conflict," "declared the following")
6. Query combining Nhan's name with "researcher independence," "editorial control," "final say"
7. Query combining the article title with "no role," "independent," "sole discretion" (typical
   disclosure-statement phrasing)
8. Query for Nhan's CV/grant history directly, to see if a contract or grant terms were listed
   institutionally

**None surfaced the article's actual funding/disclosure statement, any contract term, or any
secondary source quoting one.** Search summaries consistently describe the study's *substantive
findings* (interviews with law enforcement, policymakers, and Flock representatives; concerns
about unclear policy/misuse potential) but never its funding-disclosure section. One search did
surface Nhan's own reported explanation for the *2024* controversy (from a 2024 Slashdot/404
Media piece, "Researcher Who Oversaw Flock Surveillance Study Now Questions How It Was Done")
that he later found police-department data "too varied and incomplete for us to do any type of
meaningful statistical analysis" — consistent with the 2026 *Police Journal* piece's pivot to an
interview-based, qualitative method, but this is a methodological explanation, not an
independence/funding-terms confirmation, and it's still about the *earlier* project, not
directly about the 2026 article's own disclosure section.

## Bottom line

Nothing found tonight changes 2026-08-21's assessment: the specific clause "with contractually
stipulated researcher independence on topic, methodology, and findings" is **not sourced to
anything found by search**, and the only real reporting on this same author pair's relationship
with Flock funding (the 2024 Techdirt piece on their earlier white paper) describes Flock
steering which departments the researchers could interview and one author's own internal email
wanting to see a "big swing" in the results — the opposite of clean independence, albeit on a
different, earlier work product. This is not proof the 2026 study lacks independence. It is also
not confirmation that it has it. The claim as currently worded in the draft asserts a specific
contractual fact that no source found so far actually states.

**This is a genuinely primary-source-gated question** — the only way to actually confirm or
refute it is a direct read of the 2026 *Police Journal* article's own funding/disclosure section
(via Ole Miss library access, the way the four scale-source citations were verified on
2026-08-16) or a working WebFetch, neither available tonight.

## Drafted replacement language (for Britton to review and drop into
`Introduction_and_Theory_DRAFT_2026-08-16.md`, lines 76-81, if he agrees — not applied here)

Current text (unverified clause bolded for reference):
> "It is also worth noting plainly, in the interest of an even-handed comparison, that Nhan and
> Helfers's study was conducted under a research grant from Flock Safety itself **(with
> contractually stipulated researcher independence on topic, methodology, and findings)** and
> relied on Flock as a gatekeeper for agency access; the present study uses no vendor funding or
> vendor-facilitated access, drawing instead on public news coverage, court filings, and
> government records."

Suggested softened replacement:

> "It is also worth noting plainly, in the interest of an even-handed comparison, that Nhan and
> Helfers's (2026) study was conducted under a research relationship with Flock Safety and
> relied on Flock as a gatekeeper for agency access — Flock representatives were themselves among
> the interviewees, and Flock's cooperation was necessary to reach the law-enforcement users and
> policymakers in the sample. The published article's own funding and disclosure statement has
> not been independently verified for this paper as of this draft; the present study uses no
> vendor funding or vendor-facilitated access of any kind, drawing instead on public news
> coverage, court filings, and government records — a methodological contrast that holds
> regardless of how the 2026 study's specific disclosure statement reads once confirmed."

This keeps the genuinely useful and defensible comparison (funded/gatekept vs. unfunded/public-
record) while dropping the specific unverified contractual claim, and it flags plainly, in-text,
that the disclosure statement itself hasn't been read yet — consistent with how this project has
handled every other WebSearch-only confidence flag. An alternative, more conservative option is
to cut the parenthetical entirely rather than replace it, if Britton would rather not raise the
independence question in-text at all until it's confirmed either way; both options are left for
his call, since this is language he'll want to have final say on before it goes further.

## What would resolve this for real

1. A direct read of the 2026 *Police Journal* article itself (Ole Miss library access, the same
   route that verified the four scale-source citations) — highest-value next step, cheap once
   library access or a working WebFetch is available.
2. Failing that, a request to Britton (not done here, since contacting anyone externally is out
   of scope) is not needed — this is a read-only verification task he or a future session with
   working WebFetch/library access can complete without contacting the authors or journal.

Not editing `Introduction_and_Theory_DRAFT_2026-08-16.md` — per the project's convention, this is
a flag-and-propose note, not a silent correction.
