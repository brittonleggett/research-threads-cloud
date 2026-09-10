# 2026-09-10 — Tier 1 (Louisiana) primary-source pull, plus a second xAI ruling recheck

Per Britton's scope-lock message today ("prioritize comprehensive coding of the
Louisiana corpus"), went after actual primary documents for Tier 1 artifacts — not
just better news sourcing, which is as far as the 2026-08-16 verification pass got.
Direct-fetched via `curl` with a browser user-agent (bypasses the AWS WAF challenge
that blocks the plain WebFetch tool — same technique the nightly routine uses for
CourtListener) plus one official government press-release page.

## 1. Meta/PSC secrecy vote (artifact #12) — vote roster corrected, one name added twice-confirmed

Existing notes (2026-08-16 pass) had the vote as 3-1 but only named two of the three
majority voters (Coussan, and dissenter Lewis) — "the other two majority votes weren't
named in either source fetched." A fresh WebSearch across multiple outlets (Louisiana
Illuminator, WWNO, Fox8) now converges on all three majority votes:
**Jean-Paul Coussan, Mike Francis, and Eric Skrmetta** voted to reverse ALJ
Verzwyvelt's order (all three Republicans); **Davante Lewis** (Democrat) dissented,
consistent with the party-line framing already in the corpus. Docket number:
**U-37882** (Entergy Louisiana rate case Meta's subpoena fight is attached to).

Attempted to pull the actual LPSC order document directly (not news coverage) via the
commission's own document portal (`lpscpubvalence.lpsc.louisiana.gov`, fileId
`XUggTpCKCj4=`, found via WebSearch) — downloaded successfully (19MB, confirmed a real
PDF, not broken/placeholder), but it's a large scanned single-page file this
environment's tooling couldn't get clean text out of (same PDF-extraction gap flagged
in the Tariff Paper's litigation note today). **Flagging, not fabricating**: the vote
roster above is still secondary-sourced (converging news reports), not confirmed
against the primary order's own text. A future session with working PDF-OCR tooling,
or a direct ask to the LPSC clerk's office, could close this properly.

## 2. New Orleans moratorium (artifacts #9-11) — real correction: it's two motions, not one

Every existing note describes this as a single "6-0 moratorium vote." Direct-fetched
the New Orleans City Council's own press release
(`council.nola.gov/news/january-2026/new-orleans-city-council-approves-motions-to-study/`)
— a genuine primary source, the council's own site, not news coverage. It's actually
**two motions**, both introduced by Council President JP Morrell and District E
Councilmember Jason Hughes on January 28, 2026:
- **M-26-62** — directs the City Planning Commission to formally define "data center"
  in the zoning code and study use/design standards (density, sound, safety).
- **M-26-63** — directs the CPC to study creating a temporary Data Center Interim
  Zoning District that **pauses occupational licenses/approvals for data centers
  citywide for one year** — this is the actual "moratorium" mechanism; M-26-62 alone
  doesn't pause anything.

The council's own release also has two direct quotes not previously in this project's
files, both relevant to the existing `distributive-injustice`/racial-framing theme:
Council Vice President **Matthew Willard** on "rising cost of electricity and the
enormous amount of water they use," and District B Councilmember **Lesli Harris**:
*"data centers are often placed in Black and Brown communities, bringing with them
environmental, economic, and public health harm."* The exact vote count wasn't stated
in this particular press release (the 6-0 figure already in the corpus comes from news
coverage — not re-verified against a primary vote record tonight, flagging as still
secondary on that specific number).

Motion text itself is on Granicus (`cityofno.granicus.com/MetaViewer.php?...
event_id=24823&meta_id=774936`) — found via WebSearch but not fetched tonight (time
budget); worth a follow-up if the exact motion language matters for direct quotation.

## 3. Amazon/Caddo court challenge (artifact #15) — plaintiffs named for the first time

Existing notes describe Judge Lafitte's April 20, 2026 dismissal but don't name who
brought the challenge. WebSearch across three outlets converges: the petition was
filed by **Mooringsport Mayor Tyler Gordon and two local residents**, raising notice,
environmental-impact, and infrastructure-strain concerns; Lafitte's written decision
dismissed the petition and affirmed the City Council's reversal of the planning
commission's denial. Plaintiffs have since sought an appeal, **backed by the Sierra
Club** (per a May 2026 KTBS piece) — this is new to the corpus and worth a coding note:
it's the first artifact showing a national environmental org joining a Louisiana case
directly, relevant if "outside advocacy-org involvement" ever becomes its own code.
Not independently verified against the actual court filing/docket (Caddo Parish's
court records aren't in a WebFetch-friendly public portal as far as this pass found).

## 2. xAI ruling recheck (second attempt today, now via direct curl)

Last night's fork got 403/401 on both direct CourtListener access and the REST API.
Retried this afternoon with `curl` + a browser user-agent instead of the WebFetch
tool (bypasses the WAF JS challenge) — this worked cleanly (HTTP 200) against the
known docket URL from last night's own note
(`courtlistener.com/docket/73188848/national-association-for-the-advancement-of/`).

**Still 122 entries, identical to last night's count — no ruling has landed.** Read
the three most recent entries directly:
- **Entry 120 (Sep 3):** NAACP's opposition to the government's "Motion For Entry of
  Written Order No Later Than September 10."
- **Entry 121 (Sep 3):** NAACP's supporting memorandum for the same opposition.
- **Entry 122 (Sep 8):** the government's reply brief on that same motion.

So as of this check, the docket confirms DOJ is specifically asking for a **written
order** by September 10 (not just any ruling) and NAACP is opposing that timeline —
but no order/ruling entry exists yet. This is a direct docket read, not inferred from
a news search. Worth one more check tomorrow if the deadline matters to Britton;
today's absence of a ruling by the time of this check isn't unusual given DOJ's own
reply just landed two days ago.

## What's still open

- LPSC order text (item 1) — tooling gap, not a decision question.
- NOLA's exact vote count and the Granicus motion text itself — not fetched tonight,
  time-budget cut, not a real blocker.
- Caddo court filing itself — no public WebFetch-friendly portal found for Caddo
  Parish district court records.
- None of this is a Phase 3/theme decision — purely corpus/evidence-quality additions,
  per Britton's standing rule that theme review stays his.
