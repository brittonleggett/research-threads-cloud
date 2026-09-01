# 2026-09-01 — CCS_Lit_Review_Foundation.docx citation verification, continued

Continuing the citation-integrity pass on `CCS_Lit_Review_Foundation.docx` (51-source ERSS-track
literature review) that the 2026-08-31 session started (12 of ~51 checked that night — see
`2026-08-31-lit-review-citation-verification-plus-act614-followup.md`, which this session did not
have in its own branch/working tree at start but whose content was recovered from git history,
commit `b8ba5e9`, and used to avoid re-checking the same 12). No Track A/B/C or Phase 3 work
touched.

**Note on branch state:** this worktree's branch had diverged before the 08-31 commit landed on
another parallel worktree, so `CCS_Lit_Review_Foundation.docx`'s sibling verification note wasn't
present in this branch's checkout. Read its content directly via `git show b8ba5e9:...` to confirm
exactly which 12 references were already checked before picking the next batch — did not re-verify
those 12, and did not merge that commit into this branch (left for the coordinating merge process).

## Method

Same as 08-31: extracted the docx's reference list directly from `word/document.xml` (pandoc/
python-docx weren't available in this environment; unzipped the docx and pulled `<w:t>` runs with a
short Python script — no functional difference from pandoc, same underlying text). For each
reference with a DOI, queried `https://api.crossref.org/works/<doi>` directly (the DOI registry
record, independent of the docx) and compared title, full author order, journal, volume/issue, page
range, and year against the docx entry. For the two no-DOI books (Estes 2019, Gilio-Whitaker 2019)
and one uncertain-DOI entry (McCauley et al. 2013), used targeted WebSearch against publisher/
institutional-repository records instead.

Egress/WebFetch and WebSearch worked normally throughout this session.

## Batch checked tonight: 21 references (B3, B4, B12, B13, B19, B20, B26, B27, B29, B33, B38, B39,
B40, B41, B42, B43, B44, B45, B46, B47, B58 in the docx's own numbering)

Prioritized (a) the entire Indigenous-sovereignty stream, since the 08-31 note explicitly flagged it
as the highest-remaining-risk unchecked group, and (b) the core theoretical-anchor citations
(Tyler, Schlosberg, Wüstenhagen et al., Prno & Slocombe, Gehman et al., Jenkins et al., Boudet,
Krause et al., Gough et al.) that carry the manuscript's argument.

| Docx citation (short form) | Verdict | Notes |
|---|---|---|
| Wolsink (2006), *Transactions of the Institute of British Geographers* 31(1), 85–91 | **Exact match** | |
| Whyte (2018), *Environment and Society* 9(1), 125–144 | **Exact match** | |
| Whyte (2020), *WIREs Climate Change* 11(1), e603 | **Exact match** | Online-first Oct 2019, print Jan 2020 — docx correctly uses the print year here. |
| Spice (2018), *Environment and Society* 9(1), 40–56 | **Exact match** | |
| Schilling-Vacaflor (2017), *Third World Quarterly* 38(5), 1058–1074 | **Exact match** | Online-first 2016, print 2017 — docx correctly uses print year. |
| Temper (2019), *Local Environment* 24(2), 94–112 | **Exact match** | |
| Awāsis (2020), *Canadian Geographies* 65(1), 8–23 | **Discrepancy (minor, same family as 08-31's)** | Crossref: online-first April 2020, print issue **March 2021**. Docx cites "(2020)" — the online-first year, opposite of the print-year convention the docx used for Whyte 2020, Schilling-Vacaflor 2017, and Alexander & Stanley 2022 below. Not an error, but a third instance of the online-first-vs-print-year question, and evidence the docx isn't even internally consistent about which convention it follows — worth folding into whatever house rule Britton picks. |
| Alexander & Stanley (2022), *Environment and Planning E* 5(4), 2112–2131 | **Exact match** | Online-first Dec 2021, print Dec 2022 — docx uses print year; author order (Alexander first) confirmed. |
| Tyler (2003), *Crime and Justice* 30, 283–357 | **Exact match** | |
| Wüstenhagen, Wolsink, & Bürer (2007), *Energy Policy* 35(5), 2683–2691 | **Exact match** | Author order confirmed. |
| Prno & Slocombe (2012), *Resources Policy* 37(3), 346–357 | **Exact match** | |
| Gehman, Lefsrud, & Fast (2017), *Canadian Public Administration* 60(2), 293–317 | **Exact match** | |
| Krause, Carley, Warren, Rupp, & Graham (2014), *Risk Analysis* 34(3), 529–540 | **Exact match** | Online-first Oct 2013, print March 2014 — docx uses print year. |
| Jenkins, McCauley, Heffron, Stephan, & Rehner (2016), *ERSS* 11, 174–182 | **Exact match** | Author order confirmed. |
| Boudet (2019), *Nature Energy* 4(6), 446–455 | **Exact match** | |
| Gough, Cunningham, & Mander (2018), *IJGGC* 68, 16–25 | **Exact match** | |
| Schlosberg (2007), *Defining Environmental Justice*, Oxford University Press | **Exact match** | Book DOI resolves; sole-author confirmed. |
| Coulthard (2014), *Red Skin, White Masks*, University of Minnesota Press | **Exact match** | Crossref's DOI record listed a second contributor (Taiaiake Alfred) alongside Coulthard, which needed a second look — confirmed via independent sources (SAGE book review, Amazon listing) that Alfred wrote the **foreword only**, not a co-author. Docx correctly lists Coulthard as sole author. |
| Estes (2019), *Our History Is the Future*, Verso, ISBN 9781786636737 | **Exact match** | Hardback ISBN circulating in most citations is 9781786636720; docx's ISBN (9781786636737) is confirmed as the real ebook/VitalSource-edition ISBN for the same title, not an invented number. |
| Gilio-Whitaker (2019), *As Long as Grass Grows*, Beacon Press, ISBN 9780807073780 | **Exact match** | |
| McCauley, Heffron, Stephan, & Jenkins (2013), *International Energy Law Review* **3(3)**, 107–**111** | **DISCREPANCY — real citation error** | Two independent institutional repository records (University of Stirling: "vol. 32 (3), pp. 107-110"; University of St Andrews: "vol. 32, no. 3, pp. 107-116") agree the actual volume is **32**, not 3 — docx's "3(3)" is very likely a dropped digit. The two repositories disagree with each other on the exact end page (110 vs. 116), but neither says 111, so the docx's end page is also off by at least a few. First page (107) and the core citation (title/authors/journal/year) are all correct. This is the first genuine reference error found across 33 references checked so far (this session's 21 plus 08-31's 12) — not a fabrication (the article, authors, and journal are all real), but the docx's own volume/page numbers need correcting before manuscript-final. The docx itself already flagged this entry as "DOI UNCERTAIN," which is why it got extra scrutiny — but the flag was about missing DOI, not about the volume/page numbers being wrong, so this is a genuinely new finding, not something the docx's own caveat already covered. |

**Bottom line: 20 of 21 checked tonight are clean exact matches; 1 has a real (non-fabrication)
citation error (McCauley et al. 2013 volume/page numbers), and 1 has the same online-first/print-
year ambiguity already flagged twice before (Awāsis 2020).**

## Running total

- Checked across both sessions: **33 of 51** references (08-31: 12; tonight: 21 additional, no
  overlap).
- Zero fabricated citations found in either session.
- One real, correctable citation error found (McCauley et al. 2013 — see above); recommend fixing
  the volume ("32" not "3") and end page (closest independently-sourced figure is 110, per the
  Stirling repository) before manuscript-final.
- Three references now carry the online-first-vs-print-year ambiguity (Cox et al. 2021/2022,
  Bergquist 2024/2025 from 08-31; Awāsis 2020/2021 from tonight) — still not errors, but Britton
  needs to pick one dating convention and apply it consistently; the docx currently mixes both.
- **18 of 51 remain unverified**: B5, B6, B7, B11, B14, B15, B16, B17, B18, B21, B22, B23, B24, B25,
  B32, B34, B35, B37, B48, B50, B51, B52, B53, B54, B56 in the docx's numbering (this list has more
  than 18 raw slots because a few B-numbers are cross-stream duplicates the docx itself already
  excludes from its "51 unique" count — see the docx's own note at the end of Part B). These are
  mostly the remaining governance-framing/vignette-experiment stream (Whitmarsh et al., Pianta et
  al., Demski et al., Liebe et al. x2, Walker et al., Chewinski et al.) and a handful of siting/
  justice-theory entries (Devine-Wright x2, Batel, Bergquist et al. 2020, Cha, Sovacool & Dworkin,
  Sovacool et al., Jenkins et al. 2018, McCauley et al. 2019, Walker & Day, Hall et al., Boutilier,
  Horowitz et al., Mabon et al., Hansson et al., Thomas et al., Atkinson et al., Ó Maonaigh et al.).
  Still explicitly unverified, not assumed clean.

## Routine standing checks

**1. legis.la.gov codification lag (R.S. 30:1109, `Law.aspx?d=670795`):** re-fetched tonight —
**still stale**, same as every prior check back through 08-30/08-31. Subsection (B) still shows the
pre-Act-614 $250,000/$500,000/$1,000,000 caps, subsection (G) is still present and unrepealed, and
the acts-history line still stops at "Acts 2025, No. 458." Not a concern for the manuscript (the
enrolled Act 614 text is the controlling primary source, already verified). Just don't cite this
page for "current" R.S. 30:1109 text yet.

**2. New legal challenge to HB79/Act 614/HB804:** re-ran the search tonight — **still nothing new**.
Results are the same known items: the pre-existing Save My Louisiana eminent-domain suit (filed Nov
2025, unrelated to HB79/Act 614/HB804 specifically, already correctly set aside in prior notes) and
routine 2026 legislative-session coverage (The Lens, Talk 107.3FM, Liskow & Lewis). One new item
worth flagging for awareness, though it is *not* a lawsuit: an April 2026 student note in the *LSU
Journal of Energy Law & Resources*, "You Shall Not Pass; or Should You? Examining the
Constitutionality of Granting Expropriation Authority for Carbon Capture and Storage Pipelines" —
an academic legal analysis of CCS pipeline expropriation authority, potentially useful as a legal-
context literature source later, but not itself a challenge/suit and not verified as a citation
tonight (out of scope for this session — flagging only that it exists).

## What's still open

- Track A/B/C reframing and Phase 3 theme review: untouched, per standing instruction, reserved for
  Britton.
- 18 of 51 `CCS_Lit_Review_Foundation.docx` citations remain unverified (list above) — next
  candidate for a third verification pass if this paper stays in rotation.
- **Britton judgment call needed:** the McCauley et al. (2013) volume/page numbers should be
  corrected in the docx before manuscript-final (recommend "32(3), 107–110" per the Stirling
  repository, the more specific/authoritative of the two independent sources found) — flagging
  rather than editing the docx myself, since this is the kind of correction Britton should see and
  confirm rather than have silently changed underneath him.
- The online-first-vs-print-year citation-year convention question (now three instances: Cox et al.,
  Bergquist, Awāsis) still needs a house-style decision before manuscript-final — not urgent now.
- `Law.aspx?d=670795` codification lag: still stale, re-check periodically; not a blocker.
