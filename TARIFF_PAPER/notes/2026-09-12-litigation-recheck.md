# 2026-09-12 — Litigation recheck: Section 301 docket exploded with a 7-amicus wave (22→45 entries); Section 122 government asks to push its brief deadline to Nov 12; V.O.S. Selections gets a new extension motion; Axle of Dearborn unchanged

## What this is

Re-ran the same four-docket litigation check per the 09-10 note
(`2026-09-10-litigation-recheck-section301-government-response-was-filed-on-time-not-actually-overdue.md`),
using the same four CourtListener docket URLs that note and its predecessors used.
All four fetched directly via `curl` with a browser user-agent (HTTP 200, real
docket HTML each time — no WAF block tonight, no WebFetch/search-summary
substitution needed). Parsed each docket's raw HTML with BeautifulSoup (installed
fresh this session) rather than eyeballing grep output, to read every new entry's
actual text rather than inferring from an entry-count delta.

## 1. Section 301 forced-labor master docket — big new development: a 7-filer amicus wave, 22→45 entries

`https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`

Stable at 22 entries as of 09-10 (entry #22 being the government's Sep 4 response,
confirmed on-time that night). **Now at 45 entries** — 23 new entries, almost all
dated Sep 10-11. Read each new entry directly:

- **#23-24 (Sep 10):** Motion for leave to file an amicus brief by **"Former Senior
  U.S. Trade Officials"** — named as Carla A. Hills, Alan Wm. Wolff, and Warren H.
  Maruyama — with a proposed brief attached, plus their corporate disclosure
  statement.
- **#25-28 (Sep 10):** Barry Appleton's motion to appear as amicus curiae (his own,
  separate from the trade-officials group), then a motion for leave to file an
  amicus brief by the **Goldwater Institute** "in Support of Plaintiffs" (counsel
  Timothy Sandefur), with brief attached, corporate disclosure, and notice of
  appearance.
- **#29-34 (Sep 11):** Motion for leave to file an amicus brief by **Ed Gresser /
  Progressive Policy Institute** (with brief attached), followed by a motion to
  appear as amicus by trade-law professors **Timothy Meyer and Gregory Shaffer**
  (brief attached) — both with corrected/amended corporate disclosure statements
  superseding an initial non-compliant filing.
- **#35-39 (Sep 11):** **Consumer Watchdog** — unopposed motion for leave, notice of
  appearance (counsel Rudi Planert of Taft Stettinius & Hollister, plus Alan
  Morrison), corporate disclosure, and the actual **brief in support of plaintiffs'
  motion for judgment on the agency record** filed (conditionally, per the Sep 2
  procedural order at entry #19 that lets amicus briefs be conditionally filed
  alongside the motion for leave).
- **#40-43 (Sep 11):** **Cato Institute** (Michael W. McConnell and Ilya Somin,
  counsel from Crowell & Moring) — notice of appearance, then a motion to appear as
  amicus curiae with brief attached, plus corrected corporate disclosure statements
  (an initial one was superseded).
- **#44-45 (Sep 11):** **Burlap and Barrel, Inc. and Collective Horology, LLC**
  (counsel Jeffrey Schwab, Liberty Justice Center) — motion to appear as amicus
  curiae with brief and proposed order attached, plus corporate disclosure. Worth
  flagging: Burlap and Barrel is a named *appellee/plaintiff* in the separate
  Section 122 appeal (item 2 below) — here it is seeking amicus status in this
  different case, which is a genuine cross-case connection, not a duplicate entry.

None of these motions for leave have been ruled on yet as of this fetch (no grant
order appears after entry #45) — they are pending, with responses generally due
10/1 or 10/2/2026 per each entry's own "Responses due by" language.

**Read for the paper:** this is a much larger and more ideologically diverse amicus
wave than the two-filer bump Section 122 saw around the same dates (09-08/09) —
seven distinct amici/movants (a bipartisan-leaning former-USTR-officials group, a
libertarian think tank, a center-left trade-policy institute, two international
trade law professors, a consumer-advocacy nonprofit, and another libertarian legal
group representing small-business plaintiffs from the other case) all weighing in
within roughly 48 hours. That is a real signal of the case's visibility, not
routine housekeeping — background color for the paper's litigation-context
framing, no design/theory implication.

**Entry #22 (the government's Sep 4 response, replies due 9/18/2026) reread and
unchanged** from the 09-10 account — still says "Modified on 9/8/2026," still shows
"Entered: 09/04/2026." Sep 18 reply deadline confirmed still standing, unaffected by
the amicus wave above (amicus filings target the plaintiffs' underlying motion, not
the government's response specifically).

## 2. Section 122 (State of Oregon v. Trump / Burlap and Barrel, CAFC 26-1804/-1805) — government asks to push its brief deadline to Nov 12; a corrected states' brief filed

`https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`

90 entries as of 09-10; **now 96.** Read entries #91-96 directly:

- **#91-92 (Sep 9):** Order granting Allison Johnson leave to appear as counsel for
  Cross-Appellant State of New Mexico, plus her entry of appearance.
- **#93 (Sep 9):** **Appellants (the government — DHS, EOP, USTR, Trump, CBP, et
  al.) moved to extend the time to file their brief to 11/12/2026.** This is a
  large extension request — roughly two months out — for what is presumably their
  combined reply/response-to-cross-appeal brief (they already filed their opening
  brief on 7/21; the states' cross-appeal response brief was filed 8/31 and
  corrected 9/10, see below).
- **#94 (Sep 10):** The Cross-Appellant states (Arizona, Illinois, California, New
  Mexico, North Carolina, Rhode Island, Colorado, Connecticut, Delaware, Maine,
  Maryland, Michigan, Minnesota, Nevada, New Jersey, New York, Oregon, Vermont,
  Wisconsin, Massachusetts, Virginia, Kentucky (ex rel. Beshear), Pennsylvania (ex
  rel. Shapiro)) and Appellee State of Washington filed a **corrected response
  brief** — this resolves the non-compliance notice against their original 8/31
  response brief that was flagged at entry #82 on 9/4 (i.e., separate from and
  earlier than the small-business appellees' own corrected-brief saga at entries
  #78-86 already covered in the 09-10 note).
- **#95 (Sep 10):** Notice of correction to the government's own extension motion
  (#93).
- **#96 (Sep 10):** The government **re-filed a corrected version of the same
  extension motion**, again requesting 11/12/2026 to file their brief.

**As of this fetch, neither extension motion (#93/#96) has been ruled on** — no
grant or denial order appears after entry #96. If granted, this pushes the next
substantive filing in this appeal roughly ten weeks out from now, a meaningfully
longer gap than anything else logged in this case's briefing schedule to date
(compare: the government's own opening-brief extension in June/July was ~4 weeks,
entries #63-64).

## 3. V.O.S. Selections (CAFC 26-1895) — one new entry: appellee also seeks a brief-deadline extension

`https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`

24 entries as of 09-10; **now 25.** New entry:

- **#25 (Sep 11):** **Appellee V.O.S. Selections, Inc. moved to extend the time to
  10/05/2026 to file [its] brief**, filed by counsel Colleen Roh Sinzdak.

Not yet ruled on as of this fetch. Otherwise unchanged — entries #1-24 reread and
match the 09-10 account.

## 4. Axle of Dearborn (CIT 1:25-cv-00091) — unchanged

`https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

**Still 79 entries.** Entries #74-79 reread directly — same content as the 09-10
note: the Cape Phase 3 participation motion (#74, Jul 28), the Aug 13 Slip Op.
26-94 ruling and partial judgment (#75-76), the Aug 17 judge reassignment (#77),
and the Aug 25 stay/reliquidation order pair (#78-79). No notice of appeal, no new
activity of any kind.

## For Britton

- **Section 301 case is suddenly a magnet for amicus filers** — seven different
  amici/movants (former senior U.S. trade officials including Carla Hills; the
  Goldwater Institute; Ed Gresser/Progressive Policy Institute; law professors
  Timothy Meyer and Gregory Shaffer; Consumer Watchdog; the Cato Institute via
  Ilya Somin; and Burlap and Barrel/Collective Horology, who are also plaintiffs
  in the *other* tracked case) all filed within about 48 hours (Sep 10-11). None
  of their motions for leave have been ruled on yet. Background color for the
  paper — worth a mention if the litigation-context section wants an example of
  how visible this issue has become, but nothing here requires action from you.
  The Sep 18 government-reply deadline on this same docket is unaffected and still
  stands.
- **Section 122 (Oregon v. Trump/Burlap and Barrel): the government has asked
  (twice, after a correction) to push its next brief deadline out to November 12,
  2026** — not yet granted. If it goes through, that's a real schedule shift worth
  knowing about if you're watching this case for the paper's timeline, but it's
  still just a pending motion, not an order. Also: the states' corrected response
  brief (separate issue from the small-business appellees' one already noted
  09-10) is now filed and appears compliant.
- **V.O.S. Selections: one new item** — the appellee itself asked for a brief
  extension to Oct 5, 2026. Not yet ruled on. Nothing to do.
- **Axle of Dearborn: no change**, nothing to do.
- All four docket URLs, entry counts, and every quoted docket-entry text above were
  read directly from the live CourtListener HTML tonight (Sep 12), not from a
  search summary or from AI-mediated fetch — same standard as every prior night's
  notes. No tooling blockers tonight (no WAF challenge, no failed installs); the
  only new tool used was a fresh `beautifulsoup4` pip install to parse the raw
  HTML entry-by-entry rather than relying on grep context windows, which made it
  easier to catch the full amicus wave text-by-text.
- Everything else in this project (IRB submission status, CITI Comprehensive-module
  question, grad-assistant blind-coding worksheet, H3 direction, Purchase Intention
  item-count choice) was untouched tonight — this was a verification-only pass on
  the four litigation dockets, no other project files were read or edited, and
  nothing was committed to git.
