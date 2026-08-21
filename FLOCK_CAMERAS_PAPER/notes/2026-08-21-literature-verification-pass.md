# 2026-08-21 — Literature-grounding verification pass (WebSearch only — WebFetch confirmed egress-blocked again tonight, 10th straight session)

Checks the theory-chain citations in `Introduction_and_Theory_DRAFT_2026-08-16.md` that hadn't
already gone through a library-access verification pass the way the four scale-source citations
did (Reisig, Bratton, & Gertz 2007; Miethe et al. 2025; van Zomeren et al. 2004 — all verified via
Ole Miss full-text pulls per `2026-08-16-scale-sourcing.md`). **WebSearch-summary confidence only
for everything below** — WebFetch attempts failed with the same egress-blocked result reported in
every prior session; no full text was independently read, only search-result summaries. Flagging
per the project's own standard (`CLAUDE.md`: "flag anything WebSearch-summarized-only vs. directly
fetched").

---

## Citations confirmed real (author/year/journal/publisher check out)

- **Sunshine, J., & Tyler, T. R. (2003).** "The Role of Procedural Justice and Legitimacy in
  Shaping Public Support for Policing." *Law & Society Review*, 37(3), 513-547. Confirmed via
  Wiley/Cambridge Core listings.
- **Nissenbaum, H. (2010).** *Privacy in Context: Technology, Policy, and the Integrity of Social
  Life.* Stanford University Press. Confirmed via publisher/Amazon/Internet Archive listings;
  contextual-integrity framing in the draft matches the book's actual thesis (information flows
  judged by context-specific norms, not a public/private binary).
- **Tyler, T. R. (1990).** *Why People Obey the Law.* Yale University Press. Confirmed (note:
  Princeton University Press published a later paperback edition — cite the original 1990 Yale
  edition as the draft does, or flag which edition/page numbers if quoting directly later).
- **Tyler, T. R., & Huo, Y. J. (2002).** *Trust in the Law: Encouraging Public Cooperation with
  the Police and Courts.* Russell Sage Foundation. Confirmed via publisher/Russell Sage listing.
- **Reisig, M. D., & Lloyd, C. (2009).** "Procedural Justice, Police Legitimacy, and Helping the
  Police Fight Crime: Results from a Survey of Jamaican Adolescents." *Police Quarterly*, 12(1),
  42-62. Confirmed via SAGE Journals listing (N=289 Jamaican high school students, matches how the
  draft cites it).
- **Bradford, B., Yesberg, J. A., Jackson, J., & Dawson, P. (2020).** "Live Facial Recognition:
  Trust and Legitimacy as Predictors of Public Support for Police Use of New Technology." *British
  Journal of Criminology*, 60(6), 1502-1522. DOI 10.1093/bjc/azaa032. Confirmed via Oxford
  Academic listing. **The draft's specific claim — that trust/legitimacy "alleviated" privacy
  concern rather than just coexisting with it — is directly supported** by the search summary
  ("trust and, particularly, legitimacy seem to serve to alleviate privacy concerns about police
  use of this technology"), so H6's framing of this as a close precedent, not just an adjacent
  one, holds up.
- **Li, L. (2024).** "Institutional trustworthiness on public attitudes toward facial recognition
  technology: Evidence from U.S. policing." *Government Information Quarterly*. Confirmed real
  (ScienceDirect listing, June 2024, N=4,679 nationally representative 2021 U.S. survey, integrity
  and ability as the two trustworthiness dimensions tested) — matches the draft's citation.
  **One specific sub-claim not independently confirmed by the search summary:** the draft states
  the trust effect was "largest in the highest-privacy-concern scenario tested (public
  protests)" — the search result confirms five scenarios were tested (including public protests)
  and that integrity/ability both matter, but did not surface the specific "largest effect in the
  protests scenario" detail. Not contradicted either — just not independently confirmed at this
  pass. Low-priority flag (a plausible, specific-sounding detail, not implausible), but worth a
  direct-fetch check before it's stated as confirmed fact in a submitted manuscript.
- **Nhan, J., & Helfers, R. C. (2026).** "Cops and hotlists: Balancing security and privacy with
  ALPR technology." *The Police Journal*. DOI 10.1177/0032258X251349633, published 2026-04-01.
  Confirmed real — matches the draft's description (interviews with law-enforcement users,
  policymakers, and Flock Safety representatives).

## One claim in the draft that needs Britton's attention before it goes further — not confirmed, and there's a real reason for caution

The Introduction draft states, about Nhan & Helfers (2026): *"conducted under a research grant
from Flock Safety itself (with contractually stipulated researcher independence on topic,
methodology, and findings)."*

**The "contractually stipulated researcher independence" clause could not be confirmed by this
pass.** No search result surfaced a funding-disclosure statement, contract term, or independence
clause for the specific 2026 *Police Journal* article. What the search **did** surface is a 2024
Techdirt piece describing a *different, earlier* Flock-funded project involving the same two
authors (Nhan and Helfers) — a white paper titled "Flock Safety Technologies in Law Enforcement:
An Initial Evaluation of Effectiveness in Aiding Police in Real-World Crime Clearance" — in which
internal communications reportedly showed Flock recommending which police departments the
researchers should talk to, and Nhan himself reportedly emailing that he wanted to see data
showing a "big swing" pre/post-adoption. The same search summarized this as researchers being
"compromised by Flock's insistence [that] the research it's funding deliver the results it's
seeking," while also noting Nhan's own stated response that he and Helfers were "brought into the
study late," had concerns about how it was framed, and were separately working on more independent
qualitative/case-study research with Flock going forward — which may be a reference to the 2026
*Police Journal* piece itself, or may not be; the search results don't resolve which.

**This doesn't mean the 2026 study lacked genuine independence** — the Techdirt reporting concerns
an earlier, different work product, and Nhan's own account (per the same reporting) pushes back on
how that earlier project was framed. But it means **the specific "contractually stipulated
researcher independence" claim in the current draft is an assertion this pass could not verify**,
and there is at least suggestive, real reporting that the same research team's relationship with
Flock funding has been publicly questioned before. Recommend one of:
(a) a direct-fetch read of the actual 2026 *Police Journal* article's funding/disclosure statement
(needs library access or a working WebFetch — neither available this session),
(b) softening the draft's language to something verifiable without the article in hand (e.g.,
noting the funding relationship and that the article's own disclosure section states X, once read,
rather than asserting a specific contractual term), or
(c) flagging this explicitly to Britton as a claim to verify or cut before submission — the
comparison itself (this study's independence vs. Nhan & Helfers's funded position) is a real and
useful point for the paper to make, it just needs to rest on something actually confirmed rather
than an unverified specific clause.

**Not editing `Introduction_and_Theory_DRAFT_2026-08-16.md` directly** — per this project's
"prefer new dated files over overwriting" convention, and because this is a factual-accuracy flag
for Britton's read-through rather than a locked correction, same posture as Tariff Paper's own
citation-verification passes (`TARIFF_PAPER/notes/2026-08-14-primary-source-verification-pass3-websearch-only.md`
is the precedent for this kind of flag-don't-silently-edit note).

## What this pass did not check

Did not re-verify the four scale-source citations (Reisig et al. 2007, Miethe et al. 2025, van
Zomeren et al. 2004) — those already went through a stronger verification method (direct full-text
pull via Ole Miss library access, not WebSearch) on 2026-08-16, a higher confidence bar than
anything in this pass could add. Did not attempt to re-verify any of the 22 Study 1 corpus
artifacts' news-source citations — see `2026-08-21-corpus-addendum-new-evidence.md` for that
(separate, corpus-focused pass done the same night).
