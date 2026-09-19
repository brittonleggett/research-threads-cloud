# 2026-09-19 — Tucker Carlson podcast claims (items 7-10), Kalshi/Arizona litigation update, Connecticut tax-statute resolution, OBBBA/idea-41 status check

This project's last dedicated pass was 09-17. That pass explicitly flagged `claims_to_verify.md` items
7-10 (the Tucker Carlson/Saagar Enjeti podcast figures) as "not part of tonight's assigned scope" and
recommended a dedicated pass — this is that pass. Also worked: the Arizona Kalshi-suit item flagged 🔶
pending verification, the Connecticut promo-deduction statute gap flagged as this project's first genuine
"the statute itself is unreachable" case, and a status check on idea 41 (OBBBA 90% gambling-loss-deduction
cap) since the 09-18 scouting log flagged it as a possible moderator tie-in worth checking, not forcing.

## 1. Podcast claims 7-10 — full detail in `claims_to_verify.md` (updated in place), summary here

**Item 7 (handle figures) — RESOLVED, both halves.** AGA's own official press release (PR Newswire,
read directly): 2025 sports betting handle was **$166.94 billion (+11.0% YoY)** — this is a different,
correctly-not-conflated metric from the $16.96B revenue figure (+22.8%) already in the literature map.
The podcast's "$166 billion wagered on sports in 2025" is accurate almost to the dollar. The "$500
billion wagered since 2018" figure traces to a specialty tracker (LegalSportsBetting.com, self-reported
methodology, not AGA) that reported crossing $500B as of **Q1 2025** — roughly 18 months before the
podcast aired in September 2026. By the podcast's air date, other tracking estimates (not AGA, not
independently reconciled to one authoritative cumulative series this session) put cumulative handle in
the $650-700B range. Bottom line: not fabricated, right order of magnitude, but stale and not AGA-sourced.

**Item 8 ($1→$2 savings claim) — the most substantive finding tonight, and it complicates rather than
resolves the original assumption.** The 09-04 note assumed this was likely a media distortion of Baker
et al.'s real, more modest figures. Getting the actual primary text changes that picture. WebFetch's
own extraction failed on the paper's PDF (same recurring failure pattern this project has hit repeatedly
— Coombs/Madonia/Nencka/Smith, Michigan's legislature site, the AGA guide, the Mullin/Vasquez FTC letter
below); downloading the PDF and running local `pdftotext -layout` on it worked cleanly both times tonight
(this paper and the FTC letter in Section 2). Direct quotes from the paper's own text (Baker, Balthrop,
Johnson, Kotter, Pisciotta, "Gambling Away Stability," Oct 21, 2024 draft, same paper as the published
JFE 2026 version):

- DiD estimate: "the estimate in Column (1) implies that net investment falls $53 per quarter, or by
  about 14% relative to the mean" (average household).
- 2SLS estimate: **"$1 of online sports betting causes net investments to fall by $0.99. This suggests
  that for the average household, sports betting entirely crowds out investment through equity
  brokerages."**
- Constrained/low-savings households: "low savings households cut net investment by about 41% relative
  to the sample mean, or about 3 times more than the overall sample average... 2SLS estimates show that
  $1 of sports betting causes low-savings households to cut net investments by $3.07 (untabulated)."

None of these match the "~20% cut in net brokerage deposits, heavy bettors >50%" figures already sitting
in `literature/literature_map.md` (sourced there from BYU News/EurekAlert press coverage) — those figures
are simply not in the primary text I read. Tracing the podcast's specific "$1→$2" framing further:
Northwestern's own Kellogg Insight (Scott Baker's home institution) states verbatim, **"For every $1 a
household spent on betting, it put $2 fewer into investment accounts"** — so the podcast is faithfully
repeating an official university research-communications article, not inventing a distortion. But that
Kellogg framing itself doesn't match the paper's own $0.99 (average) / $3.07 (constrained) coefficients
either. This is now a real, three-way discrepancy across (a) the primary paper text, (b) Kellogg's own
coverage of its own faculty member's paper, and (c) BYU/EurekAlert's coverage of the same paper — not a
fabrication anywhere, but genuinely inconsistent secondary reporting. **Updated `literature/literature_map.md`
rows 1 and 16 in place** to record the primary-text figures as authoritative and flag both press-release
figures (BYU's "20%/>50%" and Kellogg's "$1→$2") as inconsistent paraphrases that should not be cited in
a manuscript draft. One honest caveat: I read an October 2024 working-paper draft (PDF hosted via a
conference site, not the publisher); I have not independently confirmed these exact coefficients are
unchanged in the final published JFE 2026 version — flagging this as the residual uncertainty, not
re-litigating the whole paper.

**Item 9 (25-30% claim) — RESOLVED.** This maps cleanly to Hollenbeck, Larsen & Proserpio (Management
Science, 2026), already a core anchor citation in the literature map: their finding is a **25-30%
increase in bankruptcy filings** following online/mobile legalization — not a 25-30% increase in
"gambling" itself, which is how the podcast phrased it. Real number, mischaracterized outcome variable.

**Item 10 (DeWine statement) — partially advanced, not resolved as originally framed.** No source (primary
or secondary) was found containing the specific claimed statement (Ohio's ~$200M gambling revenue
"roughly offset" by equivalent social costs). What is real and directly quotable: DeWine said publicly in
February 2026 (per 13abc, read directly), **"I signed the bill to allow sports betting. I think that was
a mistake. If I had to do it over again, I wouldn't do it,"** and "I think all the leagues are walking on
pretty thin ice with this betting." This is a genuine, on-record, quotable gubernatorial statement critical
of legalization — usable as elite-discourse context (same weak evidentiary tier as always intended for this
item), just not the specific revenue/cost framing originally attributed to him. Do not conflate the two.

## 2. Kalshi/prediction-market litigation — Arizona corrected, a new Ninth Circuit ruling found, FTC letter now fully read

The 09-17 note flagged Arizona's Kalshi action as "sued... per secondary reporting — not independently
confirmed... flag as 🔶 pending direct verification." Verified directly against azag.gov (Arizona
Attorney General's own site) this pass, and the finding is more specific than "sued":

- **Arizona filed 20 CRIMINAL charges against Kalshi (KalshiEx LLC and Kalshi Trading LLC) on March 17,
  2026** — not a civil lawsuit as the word "sued" implied. Charges include wagers on Arizona college
  basketball, Super Bowl props, and four election-wagering counts (2028 presidential race, 2026 AZ
  governor's race and GOP primary, 2026 AZ Secretary of State race). AG Mayes, quoted directly: "Kalshi
  may brand itself as a 'prediction market,' but what it's actually doing is running an illegal gambling
  operation and taking bets on Arizona elections... No company gets to decide for itself which laws to
  follow."
- **New since 09-17: a Ninth Circuit ruling, *KalshiEX, LLC v. Assad*, referenced in an AZ AG press
  release dated August 28, 2026** — the court held the Commodity Exchange Act does **not** preempt state
  authority to regulate Kalshi's sports event contracts as sports betting ("Calling a sports bet a 'swap'
  doesn't make it one," per Mayes). This is a real, dated, primary-sourced appellate win for the states'
  side of the core legal question this project's Kalshi angle turns on. Mayes's own release notes Arizona
  has a **separate, ongoing civil case against Kalshi** beyond the criminal charges — a detail not
  previously in this project's notes; the civil case itself was not independently located/read this pass,
  flagged as a loose end for a future pass if it becomes relevant to the panel-construction question.
  The ruling does not address election contracts specifically (Arizona's criminal charges do include
  election-wagering counts) — that piece remains open per the release's own wording.
- **The Mullin/Vasquez FTC letter (previously unreadable, flagged 🔶 in the 09-17 note) was fully read
  this pass.** Same PDF-extraction fix as Section 1 (WebFetch failed, local `pdftotext` on the downloaded
  PDF worked cleanly). Dated **June 3, 2026**, addressed to FTC Chairman Andrew Ferguson, signed by **9**
  members exactly as previously reported secondhand: Kevin Mullin, Gabe Vasquez, Jared Huffman, Raul Ruiz,
  Salud Carbajal, Mike Levin, Dina Titus, Paul Tonko, Valerie Foushee. The letter's core argument, quoted
  directly: Kalshi and Polymarket "advertise themselves to consumers as a way to attract those interested
  in gambling" while arguing in litigation that their contracts are financial instruments ("offers
  consumers the chance to invest," "financial tools used to mitigate risk") — the same doublespeak
  argument this project's design already treats as central to the channeling mechanism. It cites two March
  2026 polls: 61% of Americans (AIBM/Ipsos) see prediction-market event contracts as closer to gambling
  than investing; 81% (Morning Consult) believe sports betting on prediction markets is gambling — both
  potentially useful, real, dated public-opinion data points for a motivation section. Response was
  requested by June 29, 2026; **a search this pass found no evidence the FTC ever responded**, publicly or
  otherwise — treat as still unanswered as of tonight, not confirmed closed either way.

## 3. Connecticut promo-deduction statute — upgraded from 🔶 to a materially stronger (but not fully closed) status

The 09-17 pass hit a genuine hard wall: Justia 403'd on §12-850, cga.ct.gov 503'd on the whole chapter.
This pass re-tried both exact same routes first (both failed identically — confirmed as a repeat, not a
one-off) before trying a mirror this project already treats as acceptable when a .gov/Justia route fails:
**codes.findlaw.com**, which had not been tried against Connecticut specifically before. It returned clean
text for **§12-867** (the actual sports-wagering tax section, not just the general definitions section
§12-850 that the 09-17 pass had been trying): the 13.75%-of-"gross gaming revenue from online or retail
sports wagering" tax includes a promotional-coupon/credit exclusion phased **25% of monthly gross revenue
(Year 1) → 20% (Year 2) → 15% (Year 3+)**. This is the same 25/20/15 figure the 09-17 pass had confirmed
only for online casino gaming — on this reading, it appears to be written directly into the sports-wagering
tax section itself, not conflated in from the casino section. **Honest caveat, stated plainly**: this rests
on one mirror site's rendering, not an independent second primary read — cga.ct.gov and Justia both
remain genuinely blocked to this session's tools (a real, repeat hard wall, not a retry-harder problem).
Updated `policy/state_policy_variables.md`'s Connecticut row to reflect this as materially more confirmed
than 09-17's 🔶 status but flagged short of Kansas's tier (read directly on the state's own official site).
**A single Westlaw/Lexis query or a working direct .gov fetch by Britton would fully close this out.**

## 4. OBBBA / idea 41 status check (informational only — no design call made)

The 09-18 scouting log's idea 41 flagged the House Ways & Means 38-5 vote (Sept 16) to restore the 100%
gambling-loss deduction as a possible moderator worth Britton's read, not a standalone commitment. Quick
status check, not a design decision: **H.R. 10357 cleared committee Sept 16 as reported, and per fresh
coverage (Covers.com, Yogonet, Las Vegas Sun, all dated Sept 16-17) now heads to the House floor, but
lawmakers are not expected to hold a floor vote until after the November 2026 midterms** — i.e., this is
still live and unresolved, not something that flipped to "passed" or "died" since the 09-18 note. Nothing
else to add here; whether/how this ties into `GAMBLING_SOCIAL_COST_PAPER`'s design (as a moderator or not
at all) stays Britton's call per the standing rule, same as `open_questions.md` items 1-5.

## What's still open / unresolved after tonight

- **Baker et al.'s exact figures need one more check**: I read the Oct 2024 working-paper draft, not the
  final JFE 2026 published version — if Britton has journal access, a two-minute check of whether the
  published version's Table 6/7 coefficients match ($0.99, $53/quarter, $3.07, 41%) would fully close this.
- **Connecticut §12-850/§12-867 still hasn't been read on a primary .gov source or via Justia** — the
  findlaw mirror is a reasonable stand-in per this project's own established sourcing convention, but it's
  one source, not two. Flag for Britton's Westlaw/Lexis if he wants full certainty before citing.
- **Arizona's separate civil case against Kalshi** (mentioned in passing in the AG's Ninth Circuit press
  release) was not independently located or read this pass — a loose end, not a blocker.
- **FTC's non-response to the June 29, 2026 deadline** — genuinely unresolved; worth a quick recheck in a
  future pass since if the FTC does eventually respond (or continues not to), either outcome is a citable,
  dated fact for a regulatory-landscape paragraph.
- **The "$500B since 2018" and "~$650-700B by late 2026" cumulative-handle figures** were not reconciled
  to one single authoritative source (AGA doesn't appear to publish a cumulative running total in its own
  press materials, only annual figures) — if a precise cumulative figure is ever needed for the manuscript,
  it would need to be hand-summed from AGA's own annual figures rather than quoted from a tracker site.

No fabricated citations, figures, or quotes were introduced this pass. One real correction made to
existing project files: the Baker et al. row in `literature/literature_map.md` had been carrying press-
release paraphrase figures as if they were the paper's own findings; that's now corrected to the actual
primary-text coefficients, with the press figures explicitly flagged as inconsistent rather than deleted
(per this project's convention of appending/correcting rather than silently overwriting history).
