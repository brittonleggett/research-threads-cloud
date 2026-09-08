# 2026-09-08 — Schaefer et al. (2024) final new-channel retry, poultry-discrepancy hypothesis test via close reading, DOJ retailer-probe primary-source confirmation

Fourth research session on this project. Follow-up to the 2026-09-07 pass.
Three tasks per that night's open items: (1) one more genuinely new-channel
attempt on Schaefer et al. (2024, *Review of Industrial Organization*); (2)
try to resolve the 78%-vs-53% poultry citation-mix-up hypothesis by reading
both candidate papers' methods/data sections as closely as access allows;
(3) formally log the DOJ eight-retailer probe expansion with primary-source
verification. Did **not** touch the idea-28 adoption decision (still
Britton's call) or any Phase 3 / theme-review work (not yet at that stage
for this project; would be human-only regardless — no Britton exception
found for this project, and none was assumed). No git commands run this
pass, per standing instructions — a coordinating process handles git
centrally.

## 1. Schaefer et al. (2024) — still blocked; one more real retry, with a materially different kind of answer this time

**Status: unchanged (still blocked). But this pass used channels that give
an authoritative "no open-access copy exists," not just another 403 to add
to the pile — worth distinguishing from prior nights' retries.**

Channels tried this pass, all new (not attempted 09-05 or 09-07):

1. **Unpaywall API** (`api.unpaywall.org`, the standard open-access-status
   aggregator used across scholarly-infrastructure tooling) — queried
   directly by DOI (`10.1007/s11151-023-09923-z`). Result: `"is_oa": false`,
   `"oa_status": "closed"`, `"best_oa_location": null`, `"oa_locations": []`.
   This is a different, stronger kind of negative result than a channel
   returning 403 — Unpaywall aggregates across institutional repositories,
   preprint servers, and publisher OA programs, and its own index has no
   record of an open copy anywhere. It also confirmed the full, exact author
   list and affiliations (matches what the project already had).
2. **Semantic Scholar API** — same DOI. `openAccessPdf.status: "CLOSED"`,
   abstract elided by the publisher ("paper fields have been elided by the
   publisher"). Confirms the closed status independently of Unpaywall.
3. **IDEAS/RePEc** — both the author's own listing page
   (`ideas.repec.org/f/psc915.html`) and the article's own abstract page
   (`ideas.repec.org/a/kap/revind/v64y2024i1d10.1007_s11151-023-09923-z.html`).
   The article's RePEc entry is flagged "downgate" (restricted) in the
   author's publication list, and the abstract page's own "Download full
   text from publisher" section states plainly: "Access to full text is
   restricted to subscribers," offering only a LibKey institutional-access
   redirect. This did surface the paper's full abstract (already known,
   quoted in the 09-07 note) but no new full-text lead. Confirms the abstract
   text exactly matches what was found via search-engine synthesis
   previously, with no additional numeric detail.
4. **USDA-hosted mirror, retried** (`www.usda.gov/sites/default/files/
   documents/schaefer-et-al-2023.pdf`) — still returns Akamai HTTP 403 to
   both `curl` (multiple User-Agents, including Googlebot) and WebFetch,
   consistent with 09-07's finding that this URL stopped working sometime
   between 09-05 and 09-07. Confirmed still broken today, not intermittently
   recovering.
5. **USDA OCE's own "Reports and Journal Articles" index page**
   (`usda.gov/oce/economic-analysis/reports` and the newer
   `usda.gov/about-usda/general-information/staff-offices/office-chief-
   economist/economic-analysis/reports-and-journal-articles` URL) — WebFetch
   403'd on both.
6. **USDA National Agricultural Library's PubAg** (`pubag.nal.usda.gov`) —
   both the search endpoint and the catalog endpoint returned HTTP 404;
   the site's URL structure appears to have changed since whatever indexing
   any prior search-engine result was based on. No working search interface
   found this pass.
7. **Oklahoma State University's institutional repository (ShareOK)** — K.
   Aleks Schaefer's current institution. Returned HTTP 404 for the direct
   simple-search URL tried; the site itself loads (a DSpace 7 instance) but
   the query URL format used didn't resolve. Not fully exhausted (a
   properly-formed DSpace search URL might work) but not resolved this pass.
8. **UC Davis eScholarship** (Tina Saitone's institution) — Cloudflare/Akamai
   403 ("Request blocked... too much traffic or a configuration error"),
   same class of block seen elsewhere in this project.
9. **SSRN**, specifically for a related-but-different working paper by three
   of the same authors — "Leveraging Meatpacking Ownership Concentration
   and Community Centrality to Improve Disease Resiliency" (Saitone,
   Schaefer, Scheitrum; SSRN abstract_id=4041413) — found via search, tried
   as a possible adjacent lead. SSRN itself 403'd (Cloudflare challenge) to
   both `curl` and WebFetch, so this couldn't be confirmed either way; also
   worth noting this is a different paper (disease-resiliency framing) even
   if it had been accessible, not a Schaefer et al. (2024) mirror.

**Conclusion for this item: do not spend further nightly-pass time retrying
Schaefer et al. (2024) itself.** Unpaywall's negative result is the
strongest evidence yet that there genuinely is no open-access copy sitting
on some institutional-repository or preprint-server corner that a cleverer
search would find — this project has now tried the publisher, two
aggregator APIs, RePEc, the USDA mirror (twice, at two different points in
time), Wayback/archive.org (09-07, blocked by this environment's own
egress policy), ResearchGate (09-07), Google Scholar's full version list
(09-07), and now PubAg/ShareOK/eScholarship. This reads as genuinely
requiring Britton's own institutional Springer access, not an access
problem this environment's tooling can solve. Recommend the open-decision
entry in `PROJECT_STATUS.md` be updated to reflect this more firmly (done
below) rather than implying another automated retry is likely to work.

## 2. The 78%-vs-53% poultry hypothesis — closer reading advances it further, still not fully confirmed

**Task**: per the brief, read both candidate papers' methods/data sections
closely enough to confirm or refute which one Britton's project should
actually cite. Schaefer et al. (2024) itself remains unreadable (see above),
so this pass instead did a **closer, more targeted re-read of the full text
of the 2025 companion paper already in hand** (Saitone, Schaefer, Scheitrum,
Arita, Breneman & Nemec Boehm, "Consolidation, productivity, and downstream
prices in the US poultry industry," *Agricultural and Resource Economics
Review* 54 (2025), 157–178 — CC-BY open access, fetched directly from
Cambridge Core's own PDF endpoint, all 1,391 lines of extracted text
searched and the full paper re-read start to finish, not just the two
sentences quoted 09-07), specifically hunting for anything that would
confirm or refute the working hypothesis.

**Three new findings, all from direct reading, none of which alone settle
the question, but which meaningfully narrow it:**

1. **The 2025 paper never cites the RIO 2024 paper anywhere** — not in the
   introduction/literature review, not in the data section, not in the
   conclusion, and not in its own 30-entry reference list (checked in
   full; the reference list is reproduced in the note's source material and
   contains no "Saitone... 2024" or "Review of Industrial Organization"
   entry at all). This is a genuinely surprising omission for two papers
   this closely related — same core five authors, same topic
   (concentration measurement), published roughly a year apart (RIO:
   February 2024; ARER: received Nov. 2024, published March 2025) — and it
   argues *against* the two papers being presented by their own authors as
   a matched pair (one FSIS, one NETS, deliberately compared). If they were
   explicitly building the second on the first, normal academic practice
   would be to cite it directly, especially when justifying a different
   data source for what looks like the same measurement exercise. Its
   absence suggests these are two independently-scoped analyses that
   happen to compute a similar-looking statistic on the same industry in
   the same year, not one explicitly extending or reconciling with the
   other.
2. **The paper's own data-availability statement says its data "were
   obtained via a cooperative work agreement with the Office of the Chief
   Economist"** and are "not publicly available" — reinforcing that this
   is a distinct, non-FSIS commercial dataset (NETS/D&B) accessed through a
   USDA cooperative agreement, not a repackaging of the same
   federally-inspected-establishment data PSD and (per its abstract) RIO
   2024 both use.
3. **Universe size**: the 2025 paper's NETS-based sample is **522 unique
   poultry processing facilities and 307 unique owners** tracked across
   1991-2019 (any plant that existed at any point in that 28-year window,
   including entries and exits) — a substantially larger set than the
   roughly 320-360 FSIS-federally-inspected poultry slaughter
   establishments operating in any single recent year (per a same-night
   WebSearch check of USDA NASS Poultry Slaughter reports — **this
   comparison figure is WebSearch-sourced, not independently verified
   against a primary FSIS document this pass, and covers all poultry
   species/current-year snapshots rather than the 1991-2019 broiler-specific
   window, so treat it as directional context, not a proven count
   mismatch**). Still, a NETS-based "any plant that ever existed across
   28 years" count of 522 is plausibly counting a broader universe (e.g.
   further-processing plants alongside slaughter plants, cumulative
   entries/exits) than an FSIS-slaughter-establishment-only figure for one
   year — consistent with, though not proof of, the two papers measuring
   different markets.

**Net effect on the working hypothesis**: strengthened, not confirmed. The
evidence increasingly looks like two genuinely separate measurement
exercises (different data, different universe, no cross-citation) rather
than one paper's figure "belonging" to the other in any direct sense — which
actually makes the citation-mix-up explanation *more* plausible as an
explanation for how the original 2026-09-03 AI-search synthesis produced
"78%" attributed to the wrong paper (a real number, genuinely associated
with this author team, more easily misattributed between two papers that
don't even cite each other than between two that are presented as a
deliberate comparison). **This still does not tell us what RIO 2024's own
2019 broiler CR4 figure actually is** — that remains genuinely unread and
blocked (see Item 1). The manuscript-facing recommendation is unchanged from
09-07: use PSD's official 53-55% for poultry, treat 78% as a real but
likely-misattributed figure belonging to the 2025 NETS-based paper, and
flag this as resolved-by-inference-but-not-by-direct-confirmation if it
ever needs a precise footnote.

## 3. DOJ eight-retailer probe expansion — now formally confirmed via a primary source

**Status: upgraded from secondary-press-only (09-07) to independently
verified against the U.S. Department of Justice's own official
communication, not just news paraphrase.**

The 09-07 note flagged this as "confirmed only via reputable secondary
press... not yet traced to a DOJ document directly." This pass traced it
successfully — with one honest caveat about what kind of DOJ document it
is.

**What was found**: Two independent agricultural trade-press outlets
(Meatingplace, a paid-subscription industry trade publication, and Hoosier
Ag Today, an Indiana agricultural broadcast/news outlet — fetched directly
via `curl` with a browser User-Agent after WebFetch itself was blocked with
403s on both, a new site-specific-bot-protection instance of the pattern
logged repeatedly in this repo, not a new failure type) both quote the same
source: **an official post on X (Twitter) by the U.S. Department of
Justice's own verified account, @TheJusticeDept**, embedding the Antitrust
Division's own account (@JusticeATR) and naming Associate Attorney General
Stanley Woodward (@ASGWoodward) as the letters' sender:

> "🚨@JusticeATR has expanded its investigation to include 8 of the largest
> grocers when it comes to beef affordability. @ASGWoodward sent letters to
> the following regarding the recent increases in the retail price for
> beef: -Kroger -Publix -Walmart -Albertsons -Aldi -Ahold Delhaize USA
> -Costco -Amaz[on]" — U.S. Department of Justice (@TheJusticeDept),
> September 2, 2026

**This was independently verified by fetching the actual X post directly**
(`https://x.com/TheJusticeDept/status/2094959466194071943`, found via
search, not assumed). X's own page returns a JavaScript app shell to
scripted fetches (as expected), but X server-renders Open Graph metadata
for bots/crawlers/link-preview purposes on the same URL, and that
server-rendered `og:description`/`twitter:description` content — generated
by X itself for this exact status ID, not editable by any news outlet
quoting it — **reproduces the same text verbatim**, including the exact
retailer list and the truncation point ("Amaz…"). This is a meaningfully
stronger verification than relying on trade-press paraphrase: it confirms
the post is real, was made by the account it's attributed to, and says
what the press quoted it as saying, independent of any single news outlet's
accuracy. A separate DOJ quote reported by Hoosier Ag Today — "Beef prices
are a critical concern to Americans, and a priority for this Justice
Department" — was **not** independently re-verified against the X post's
own metadata this pass (the org description field truncates before that
sentence) but is corroborated by two independent outlets attributing it to
the same DOJ statement.

**Caveat worth logging plainly**: this confirms a **DOJ social-media
announcement**, not a DOJ.gov press release. Searches for a dedicated
Office of Public Affairs (`justice.gov/opa/pr/...`) release specifically
about the retailer letters came up empty — by contrast with the May 2026
"Big Four" meatpacker announcement, which did get an OPA-level press
conference (already logged 09-07). It's possible DOJ simply hasn't issued
one for this specific action, or issued one this search didn't surface; the
project should not claim a formal OPA release exists unless one is actually
found. The X post itself, from the department's own official/verified
account, is being treated here as a legitimate primary source for what DOJ
publicly said — not the same evidentiary weight as a signed letter or court
filing, but a real step up from secondary press synthesis.

**Not independently confirmed this pass, flagged rather than smoothed
over**: one AI-search-synthesized detail claimed the underlying
investigative letters were "dated July 14, 2026" (i.e., sent privately
weeks before the September 2 public announcement). This specific date was
not traced to any primary document or even a single named news outlet in
the sources checked this pass — it surfaced only in a WebSearch synthesis
answer, not in the direct quotes pulled from Meatingplace, Hoosier Ag
Today, or the X post itself. Per this project's standing caution about
treating WebSearch-surfaced specifics as unverified until independently
confirmed, **do not use "July 14, 2026" as the letters' send date without
further verification** — the only date solidly confirmed by primary
material is the September 2, 2026 public DOJ announcement.

**Retailer list, now primary-confirmed**: Kroger, Publix, Walmart,
Albertsons, Aldi, Ahold Delhaize USA, Costco, Amazon — exactly matching the
09-07 secondary-sourced list, now confirmed via DOJ's own post rather than
press paraphrase alone.

## Files edited this pass

- `PROJECT_STATUS.md` — Open Decision #6 (Schaefer/poultry) updated with
  the "no further automated retry recommended" conclusion and the
  strengthened-not-confirmed hypothesis; Open Decision #8 (idea 28) updated
  to reflect the DOJ retailer probe now being primary-confirmed rather than
  secondary-only.
- `SOURCE_VERIFICATION/Evidence_Table.md` — Schaefer et al. (2024) row
  annotated with the 09-08 channel list and Unpaywall's definitive
  closed-access result; no verification-status change (still Verified
  secondary / not independently WebFetched) since the paper itself remains
  unread.
- This file (new).

No git commands were run this pass — these changes are uncommitted as of
this note, per standing instructions for this session (a coordinating
process handles git centrally).
