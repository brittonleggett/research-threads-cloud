# 2026-08-27 (second pass) — WebFetch retry on Nhan & Helfers via a working session, Study 2 vignette face-validity review

## What this is

Follow-up to the same-day `2026-08-27-nhan-helfers-retry-and-study2-instrument-assembly.md` note,
run from a session where WebFetch is confirmed working (unlike the cloud routine's, which has been
`EGRESS_BLOCKED` for 17+ consecutive nights — that infrastructure issue was diagnosed and fixed
today, but hasn't had its first nightly run yet). Two things done: (1) one real direct-fetch
attempt at the Nhan & Helfers disclosure question, the one avenue every prior session flagged as
untried; (2) a literature-grounded face-validity review of the newly drafted Study 2 vignette
(`Study2_Instrument_DRAFT_2026-08-27.md`, Section 4), which that document itself flags as the
single highest-priority thing needing review before fielding anything.

No locked theme, hypothesis, or design element touched. No Britton-reserved design call decided.

## 1. Nhan & Helfers: direct WebFetch attempt — a different failure mode than before, still unresolved

Fetched `https://doi.org/10.1177/0032258X251349633` directly. This is a genuinely different result
than every prior session's `EGRESS_BLOCKED`:

- The DOI resolved and redirected cleanly to `https://journals.sagepub.com/doi/10.1177/0032258X251349633`
  — the network path itself is NOT blocked in this session (consistent with today's fix to the
  routine's environment network-access setting, though this session isn't the routine).
- The SAGE page itself then returned a clean **HTTP 403 Forbidden** — not a network-egress failure,
  but SAGE's own server actively rejecting the request (near-certainly bot/non-browser-agent
  detection on their end, standard for paywalled academic publishers).

**Why this matters going forward:** this is a more precise diagnosis than "WebFetch is blocked."
Even with full network egress working, this specific source is very unlikely to ever be
WebFetch-reachable — it needs an authenticated browser session (library proxy/institutional login),
not a fixed network policy. Recommend not retrying this specific URL via WebFetch again regardless
of future egress-policy changes; the real path to resolving the funding-disclosure question is
still what every prior session has said — an institutional library pull or a manual check by
Britton, not another automated fetch attempt.

**Bottom line, unchanged:** the underlying question (does this article disclose a Flock Safety
funding/research relationship) remains unresolved. Five sessions, ~25 search queries, and now one
direct-fetch attempt have all failed to surface a disclosure statement. Treating this as closed to
further automated attempts, per the 08-27 note's own recommendation — not re-opening it again
without a genuinely new access method (e.g., if Britton pulls the PDF via Ole Miss library access,
the way several Tariff Paper literature gaps were closed).

## 2. Study 2 vignette face-validity review (Section 4 of `Study2_Instrument_DRAFT_2026-08-27.md`)

This is a close textual read plus general, well-established experimental-vignette-methodology
principles (matched stimulus length, single-manipulation purity, reading-level consistency with
the rest of the instrument) — not a substitute for an actual human pilot, which the instrument
document itself correctly flags as still needed. Four concrete findings:

**(a) The document's own "three sentences of condition-specific content" claim is wrong — both
conditions are actually two sentences.** Not a substantive problem, just an inline inaccuracy
worth fixing before this goes to Britton, so the delivery-notes description matches the actual
text.

**(b) Word counts are well-matched (67 vs. 65 words), but sentence *complexity* is not.**
Condition A (transparent/disclosed) splits its content into two medium sentences (41 words, then
26 words). Condition B (secret/broad-access) front-loads nearly all its content into one 46-word
sentence containing two em-dash-set-off parenthetical clauses ("— one the city council was not
told about when it approved the contract —"), followed by a short 19-word second sentence. Raw
word count is matched; syntactic complexity is not — Condition B's single long, multiply-embedded
sentence is harder to parse than Condition A's two more evenly-split ones. This is exactly the
kind of confound the instrument's own "This description was easy to understand" confound-check
item is designed to catch downstream, but it's better to reduce the risk at the design stage than
to only measure and hope it doesn't show up — recommend splitting Condition B's first sentence
into two shorter ones before piloting, to bring sentence-level complexity closer to Condition A's.

**(c) Both conditions likely sit above the instrument's own stated ~8th-grade reading-level
target for consent language** (per `Study2_Instrument_DRAFT_2026-08-27.md` Section 1's own stated
target) — sentence lengths in the 26-46 word range, plus passive-voice constructions throughout
("would be accessible," "was presented," "were able to review," "were not told," "was not told"),
push well past an 8th-grade Flesch-Kincaid level on sentence-length alone, independent of
vocabulary difficulty. Worth an actual readability-formula check once wording is finalized, not
just a stated intent — flagging the likely gap now rather than assuming the same reading-level
target that governs the consent language was also applied to the vignette text, since nothing in
the drafting notes suggests it was checked.

**(d) The more substantive concern: Condition B may confound "broad access" with "government
incompetence/being caught off guard," which Condition A has no equivalent for.** Condition A is
framed entirely around what the city did procedurally right (published a policy, presented it
publicly, let residents review it in advance) — a pure disclosure-process narrative. Condition B
is framed not just as "broader access exists" but as a *discovery* narrative: "a local news
investigation found... one the city council was not told about... City officials said they had
not known this setting existed until the news investigation brought it to their attention." That
adds a second dimension — the city government being unaware and caught off guard by its own
system, revealed by an outside investigator — that isn't present or mirrored in Condition A at
all. This risks the manipulation actually testing (at least in part) *perceived government
competence/awareness* rather than cleanly isolating disclosed-vs-undisclosed access as intended.
The existing manipulation-check items (Section 5) test recall of *who can access the data*, which
would look clean either way — they wouldn't catch this confound, because the confound isn't about
what respondents remember, it's about what else the story implies. **Recommend Britton's attention
specifically here**, since it's a design question (does the undisclosed condition need to be
rewritten to remove the "found out via investigation, officials didn't know" framing, replacing it
with a more neutral statement of broader default access that's still undisclosed but doesn't imply
incompetence) rather than something a wording tweak alone fixes.

## What this pass did NOT do

- Did not touch the locked thematic map, hypotheses, or any design element.
- Did not decide either item still reserved for Britton (Moderator 1 Path A/B; single-manipulation
  vs. factorial; PLS-SEM vs. PROCESS).
- Did not rewrite the vignette text itself — flagged concerns for Britton's review rather than
  silently editing newly-drafted stimulus material.
- Did not run an actual readability-formula calculation (no tool access to one tonight) or a real
  human pilot — this review supplements, but does not replace, the actual face-validity pilot the
  instrument document already flags as needed.

## Open items for Britton

1. Everything already open in prior notes remains open (archival-moderator feasibility,
   single-manipulation vs. factorial, PLS-SEM vs. PROCESS, CITI certificate number, power analysis,
   Theme 3 promotion gut-check, the consent risk-language sentence).
2. New: consider revising Condition B's vignette text to remove the "discovered via news
   investigation, city didn't know" framing before piloting — as written, it likely confounds
   disclosure/secrecy with perceived government incompetence (finding 2d above).
3. New: Condition B's first sentence (46 words, two embedded parenthetical clauses) is
   syntactically more complex than anything in Condition A — recommend splitting it before
   piloting (finding 2b above).
4. New: a real readability-formula check on both vignette conditions, since both likely exceed the
   instrument's own stated ~8th-grade target (finding 2c above).
5. Nhan & Helfers: now confirmed genuinely inaccessible to any automated fetch method (SAGE's own
   bot-blocking, not a network-policy issue) — closing this to further automated attempts; only a
   manual/library pull can resolve it.
