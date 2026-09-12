# 2026-09-12 — Citation Verification Pass: DJ/PJ Correlation Meta-Analysis + Gehman et al. (2017)

**Scope:** Two bounded follow-ups from `Literature_Audit_2026-09-10.md`, not a re-run of the full
audit: (1) track down the distributive/procedural-justice correlation meta-analysis flagged at
line 65 as "found by title but not confirmed by author/journal," and (2) verify the Gehman,
Lefsrud & Fast (2017) citation flagged at line 46/128/195 as LIKELY-REAL. Method: Crossref API,
Semantic Scholar API, Unpaywall, and direct-fetch attempts (WebFetch + curl) against publisher
and repository copies. Per this project's hard rule, nothing below is asserted beyond what was
actually confirmed — verification tier is stated explicitly for every claim.

---

## 1. The distributive/procedural-justice correlation meta-analysis — FOUND AND CONFIRMED

**Citation:**
Hauenstein, N.M.A., McGonigle, T., & Flinder, S.W. (2001). "A Meta-Analysis of the Relationship
Between Procedural Justice and Distributive Justice: Implications for Justice Research."
*Employee Responsibilities and Rights Journal*, 13(1), 39–56. DOI: 10.1023/A:1014482124497.

This is unambiguously the paper the audit's P2 section was gesturing at — it is a meta-analysis
whose sole subject is the DJ/PJ correlation (not organizational justice broadly), which matches
the audit's description exactly and distinguishes it from Colquitt et al. (2001), which is a
different, already-known citation in the audit's own reading list.

**Verification tier — bibliographic: VERIFIED.** Confirmed via direct Crossref API query
(`api.crossref.org/works/10.1023/A:1014482124497`): authors Neil M. A. Hauenstein, Tim
McGonigle, Sharon W. Flinder; journal *Employee Responsibilities and Rights Journal*; volume 13,
issue 1, pages 39–56; published print March 2001; DOI as above. Every element of the citation
checks out.

**Verification tier — content/finding: NOT independently read from primary text; corroborated
only by secondary-source snippets.** Springer's own page (link.springer.com) redirects to a login
wall (303 → idp.springer.com), and Unpaywall confirms this article has **no open-access copy**
(`is_oa: false`, `oa_status: closed`) — it is fully paywalled, and no ResearchGate/PDF mirror
could be fetched (403s throughout). What I have instead is a specific finding — **ρ = .64
across all studies, with the relationship moderated by research context and substantial variability
even within context** — that appeared identically, in near-verbatim wording, across three
independent search queries, in a way consistent with it being a direct quote of the actual
abstract rather than a generated summary. That is a real signal but it is not the same as reading
the abstract or full text myself, and I want to flag that distinction explicitly rather than round
it up to VERIFIED. **Recommend Britton (or library access) pull the actual PDF/abstract before
this ρ = .64 figure goes into the manuscript as a specific number** — the citation itself
(author/journal/year/pages) is solid; the number attached to it is credible but not yet
independently confirmed by me.

**Independent triangulation — this is the strongest part of this section.** Rather than stop at
one paywalled source, I looked for corroborating meta-analytic evidence on the same question and
found it, with actual full text this time:

### Colquitt, Conlon, Wesson, Porter & Ng (2001) — upgraded from LIKELY-REAL to VERIFIED (full text read)

The audit already lists this citation (line 66, line 202) as LIKELY-REAL and cites it for "ρ
reported around .6 in the adjacent literature." I found a freely hosted educational-site copy of
the actual published PDF (*Journal of Applied Psychology*, 86(3), 425–445, "Justice at the
millennium: a meta-analytic review of 25 years of organizational justice research"), fetched it,
extracted the text with `pdftotext`, and read the actual DJ/PJ correlation section (their Table 2
and surrounding text). This is a genuine full-text read, not a search-snippet summary. Direct
findings:

- "Broadly defined procedural justice was strongly related to distributive justice (**r = .56,
  ρc = .67**)" — k = 92 studies, N = 42,576. This is the headline number.
- Using the narrower "procedural fairness perceptions" operationalization specifically: r = .48,
  ρc = .57 (k = 45, N = 13,418).
- The relationship is significantly moderated by how procedural justice is operationalized (the
  paper's own point) — the strongest relationship (r = .63) came from "indirect combination
  measures" — but under every operationalization tested, the corrected correlation is
  moderate-to-strong and positive, never near zero.
- The paper itself frames this as reopening "perhaps the oldest debate in the justice literature
  concerning the independence of procedural and distributive justice," citing prior single-study
  correlations of .72 (Sweeney & McFarlin, 1997) and .74 (Welbourne et al., 1995), and explicitly
  engages Cropanzano & Ambrose's (2001) "monistic perspective" argument that the DJ/PJ distinction
  "may sometimes be overemphasized."

### Cohen-Charash & Spector (2001) — a third independent meta-analysis, scope confirmed

Also found: Cohen-Charash, Y., & Spector, P.E. (2001). "The Role of Justice in Organizations: A
Meta-Analysis." *Organizational Behavior and Human Decision Processes*, 86(2), 278–321. DOI:
10.1006/obhd.2001.2958. Confirmed via Crossref (bibliographic: VERIFIED) and via the authors' own
USF DigitalCommons repository page, which gave a real abstract excerpt: correlates of
distributive, procedural, and interactional justice examined across "190 studies samples,
totaling 64,757 participants." I could not get its specific DJ-PJ correlation coefficient (the
correlation table itself was not accessible — ScienceDirect 403'd, no OA copy located this
session), so this one stays at **abstract-level confirmation only** — its exact number is
UNVERIFIED, but its existence, scope, and general subject matter (justice-dimension
intercorrelations across the same literature) independently corroborate that this is a
well-studied, converging empirical question, not a single fluke result.

**Net finding for Task 1:** Three separate meta-analyses of the organizational-justice literature
(Hauenstein, McGonigle & Flinder 2001; Colquitt, Conlon, Wesson, Porter & Ng 2001; Cohen-Charash &
Spector 2001) all treat the distributive/procedural-justice correlation as a live, well-documented
question, and the two I could pull actual numbers for both land in the moderate-to-strong positive
range (ρ ≈ .64 per Hauenstein et al., self-reported per search corroboration only; ρc = .57–.67
per Colquitt et al., confirmed via full-text read). This is materially stronger evidence than the
audit had when it flagged this as an unconfirmed lead — it is no longer "a title-only lead that
might complicate P2," it is now a confirmed, converging empirical pattern across the adjacent
literature that DJ and PJ perceptions are substantially correlated, not independent.

---

## 2. Gehman, Lefsrud & Fast (2017) — citation CONFIRMED, content confirmed at abstract level only

**Citation as audited:** Gehman, J., Lefsrud, L.M., & Fast, S. (2017). "Social license to
operate: legitimacy by another name?" *Canadian Public Administration*, 60(2), 293–317.

**Verification tier — bibliographic: VERIFIED**, from two independent sources:
1. Crossref API (`api.crossref.org/works/10.1111/capa.12218`): authors Joel Gehman, Lianne M.
   Lefsrud, Stewart Fast; short-container-title "Can Public Adm" (= *Canadian Public
   Administration*); volume 60, issue 2, pages 293–317; published online 2017-06-15; open-access
   under CC BY 4.0. Every element of the audit's citation matches exactly, including the exact
   page range.
2. Independent cross-check against **Lianne Lefsrud's own faculty publications page**
   (liannelefsrud.com/publications-and-honours), which lists: "Gehman, J., Lefsrud, L.M. & Fast,
   S. 2017. Social License to Operate: Legitimacy by Another Name? ... Canadian Public
   Administration, 60(2): 293–317" and separately notes it was "the most cited paper for
   2015–2019 in *Canadian Public Administration*." A co-author's own CV independently confirming
   the identical citation is about as solid as bibliographic confirmation gets without opening
   the article itself.

**Verification tier — content: abstract confirmed (real text, not summarized); full body text NOT
obtained this session.** Semantic Scholar's API returned this genuine abstract for the DOI
(not editorialized — this is the actual publisher abstract, which Semantic Scholar carries under
a text-and-data-mining agreement):

> "Social license to operate is an increasingly used but seldom defined concept. In this article,
> we draw from academic, popular, and industry literature to identify and synthesize three models
> of social license to operate. Building on our review, we investigate the linkages between social
> license to operate and legitimacy and consider how the two concepts differ from and interrelate
> with one another. Then, we review the various methods that have been used to measure social
> license to operate. We conclude by discussing the implications for stakeholder engagement,
> evolving models of regulation, and potential avenues for future research."

This directly confirms the audit's characterization (Section 6, Section 8, Master Reading List
#6): the paper's actual, stated project is exactly "investigate the linkages between social
license to operate and legitimacy and consider how the two concepts differ from and interrelate
with one another" — i.e., it does engage the "is SLO just legitimacy by another name?" question
as its central contribution, not as a rhetorical title only. This is enough to justify citing it
in the Theoretical Foundations section wherever SLO/legitimacy is defined, as the audit
recommends.

**What I could not get, despite real effort:** the actual argument/conclusion — i.e., does the
paper conclude SLO *is* essentially legitimacy, *is not*, or (most likely, per the abstract's
"differ from and interrelate with") stakes out some third position distinguishing them along
specific lines? That level of detail requires the full text, and I could not retrieve it this
session despite the article being genuinely open access (CC BY 4.0, confirmed via both Crossref
and Unpaywall license metadata, `oa_status: hybrid`, `is_oa: true`). I tried, in order: Wiley's
full-text page (403), Wiley's direct-PDF endpoint (403), SSRN's hosted copy (403), two different
ResearchGate-hosted PDF mirrors (403 both), Gehman's personal academic site (404/503,
inconsistent between tools), and the Wayback Machine (blocked entirely in this session's
tooling). Every host blocked automated fetching even though the content itself is legally open —
this looks like anti-bot blocking on the publisher/repository side, not an access-rights problem.

**Recommendation:** Treat the citation itself (author/year/title/journal/volume/issue/pages) as
solid and citable as-is. Before the manuscript quotes or paraphrases *specific claims from the
body* of this article (e.g., what exactly the "three models of SLO" are, or the precise wording
of its conclusion on the legitimacy question), get one more direct-access attempt from an
actual browser or institutional library login — the open-access PDF is real and should be
gettable that way even though this session's automated tools couldn't get past the bot-blocking.

---

## What's still open

1. **Hauenstein et al. (2001)'s ρ = .64 figure** — citation confirmed, number not independently
   read from primary source. Get institutional/library access to the actual PDF or abstract
   before citing the specific coefficient.
2. **Cohen-Charash & Spector (2001)'s exact DJ-PJ correlation** — citation and scope confirmed,
   specific number not retrieved. Lower priority than #1 since Colquitt et al.'s full-text-verified
   number already anchors the point.
3. **Gehman et al. (2017)'s actual argument/conclusion** (not just abstract) — needs a real
   browser/library-access pull, not another automated-tool attempt; every host blocked bots this
   session despite the article being open access.
4. This was a bounded, two-item follow-up — it does not touch any other LIKELY-REAL item still
   sitting in the audit (Moffat & Zhang 2014, Walters & Bolger 2019 confirmation status unchanged,
   the CSREM DOIs still needing full-text checks, etc.). Those remain exactly as the 2026-09-10
   audit left them.

---

## For Britton

Both things you asked about check out as real citations — I'm confident putting both in a
reference list as-is (author/year/title/journal/volume/issue/pages all confirmed independently,
Gehman et al. from two separate sources including a co-author's own CV).

**On the meta-analysis, though — this is a real threat to the model, and it's now better-documented
than a "maybe" flag.** I found the exact paper the audit was chasing (Hauenstein, McGonigle &
Flinder 2001, ρ ≈ .64), but couldn't get past its paywall to read the number myself — so I went
looking for a second angle and actually read the full text of Colquitt et al. (2001), which the
audit already had on the list. It reports a corrected distributive-procedural justice correlation
of **.57 to .67 depending on how procedural justice is measured**, based on 45–92 studies and
13,000–42,000+ participants. That's a real, well-powered, moderate-to-strong positive
correlation between the two constructs your model (P1–P4) treats as independently-caused
mediators of BBA.

Practically: this doesn't kill P1–P4, but it does mean the "two independent mediators" framing
needs to be defended explicitly rather than assumed, exactly as the audit already recommended
(soften P2 to a scrutiny-heightening mechanism, or model DJ/PJ as correlated co-outcomes rather
than fully separate paths, and cite this correlation literature directly when you do it). Now you
have the actual numbers to engage with instead of a hunch that they exist — a CSREM reviewer with
an organizational-justice background could reasonably ask "if DJ and PJ correlate .6+, why are
they modeled as parallel, independently-caused arms rather than a single higher-order justice
perception with two facets?" Worth deciding before the propositions get locked, not after a
reviewer asks.

One honesty note: I could not get inside the actual paywalled/blocked full texts of either the
Hauenstein meta-analysis or the Gehman et al. article this session — every automated tool I had
got 403'd by Wiley, SSRN, ResearchGate, and Springer's login wall, even where the content is
legitimately open access. If it's easy for you to pull either one through your library login, that
would upgrade both from "solid citation, abstract/secondary-confirmed content" to "fully read,"
which is worth doing before final manuscript drafting — but it's not blocking anything right now.
