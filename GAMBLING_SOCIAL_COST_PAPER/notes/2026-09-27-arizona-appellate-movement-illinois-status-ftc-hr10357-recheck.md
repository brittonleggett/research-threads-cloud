# 2026-09-27 — Arizona/Kalshi Ninth Circuit appellate docket has real new movement (no mandate yet); Illinois HB 5143 appears stalled in House Rules Committee; FTC and H.R. 10357 rechecked, no change

This pass works the four open items from the 09-24 note in the same order, using direct docket/
primary-source reads wherever the tooling allowed it this session. No design or scope decisions
made — everything below is information for Britton, consistent with every prior pass. The
fiscal-dependence-vs-net-benefit framing question (open_questions.md #1 / PROJECT_STATUS.md's
GO/MODIFY/STOP section) was not touched and is not resolved here — that stays Britton's call.

## 1. Arizona/Kalshi — real appellate movement since 09-24, but still no mandate; the district case itself remains untouched

The 09-24 note's read of the **district court** docket (*KalshiEX LLC v. Johnson*, 2:26-cv-01715-MTL,
D. Ariz.) is still accurate as far as it went — re-fetched directly via CourtListener/RECAP this pass
(`curl`, not WebFetch, which still 403s on courtlistener.com; same workaround as 09-24) and confirmed
the district docket's last known filing is still Sept. 23, 2026, and it is still just the two
administrative "mail returned as undeliverable" notices (docket #109–110) the 09-24 note already
found. **No motion to lift the May 18, 2026 stay has been filed in the district case itself.**

But the 09-24 note did not check the **separate Ninth Circuit appellate dockets** that the district
stay is actually keyed to, and there has been real, primary-source-confirmed activity there since
Aug 28:

**(a) Arizona's own interlocutory appeal of the May 5 preliminary injunction** — *Commodity Futures
Trading Commission, et al. v. Johnson, et al.*, 9th Cir. No. **26-4281** (CourtListener docket ID
73585802, fetched directly, ~29 docket entries read in full):
- Jul 21, 2026: the panel granted a joint motion staying this appeal pending the decision in the
  consolidated cases (25-7516 Assad, 25-7187 NADEX, 25-7831 Dreitzer), and ordered that **within 7
  days after that decision issues, appellants must file a status report or motion for relief.**
- Aug 28, 2026: the consolidated decision issued (see below).
- **Sep 4, 2026** (docket #20): Arizona (Kris Mayes et al., as Appellants) filed a **Status Report** —
  exactly 7 days after Aug 28, matching the July 21 order's deadline.
- **Sep 14, 2026** (docket #25): Arizona filed a **Motion for Summary Disposition or to Dismiss** —
  this is what the Sept 25 local press (Arizona Mirror / Tucson Sentinel, "Mayes pushes to revive her
  gambling case against Kalshi") is describing; the motion itself asks the Ninth Circuit to summarily
  vacate the May 5 preliminary injunction, per the news coverage — the motion's own text was not
  independently readable this pass (the individual-document page 403'd; only the docket-entry
  description was confirmed directly).
- **Sep 24, 2026** (docket #29): the CFTC, as Appellee, filed a **Response** to Arizona's motion. Its
  content/position (support or opposition) was not independently confirmed this pass — flagging this
  as a gap, not a fact, rather than assuming it opposes.

**(b) The underlying consolidated cases themselves** — *KalshiEX, LLC v. Assad, et al.*, 9th Cir. No.
**25-7516** (CourtListener docket ID 72237443, ~224 docket entries, fetched directly across all 3
pages):
- Aug 28, 2026: panel opinion issued (Nelson, Bade, Lee), ruling against Kalshi/for Nevada — matches
  what the 09-24 note and secondary reporting already had.
- Aug 28, 2026 (docket #201): a **corrected opinion** was issued the same day (one typo fix, page 35)
  — not a substantive change, but worth knowing the "final" opinion text is the corrected version.
- **Sep 9, 2026** (docket #206): KalshiEX filed a **Petition for Panel Rehearing and Petition for
  Rehearing En Banc**, docketed across all three consolidated case numbers (25-7516/25-7187/25-7831).
  **This is the key fact for the paper's purposes: under FRAP 41, a timely rehearing petition
  automatically stays issuance of the mandate.** As of this pass, no mandate has issued in the
  consolidated cases — contrary to what one might assume from "the Ninth Circuit ruled Aug 28" alone.
- Sep 17–21, 2026: several amicus briefs were filed on the rehearing petition (Paradigm Operations LP,
  a "Coalition for Prediction Markets," and an individual amicus, Colin Skow) — this is a live,
  contested rehearing fight, not a formality.
- **Sep 25, 2026** (docket #224, two days before this note): KalshiEX filed another **Status Report**
  in the consolidated docket. What triggered it or what it says was not independently confirmed this
  pass (docket entry description only; the document itself 403'd) — flagging as open, not guessing.

**Bottom line, stated precisely rather than rounded off:** the Ninth Circuit's Aug 28 ruling is not
yet final — Kalshi's en banc/panel rehearing petition (filed Sept 9) is still pending and pauses the
mandate under FRAP 41. Separately, and somewhat asynchronously, Arizona has already asked the Ninth
Circuit (in its own appeal, No. 26-4281) to act on the Aug 28 opinion now regardless of the pending
rehearing petition, via a Sept 14 motion for summary disposition that the CFTC responded to Sept 24.
The **district court case remains formally stayed** (per its own May 18 order's "after the Ninth
Circuit issues a decision... parties will confer" language) and no one has yet gone back to Judge
Liburdi to argue the stay should lift or continue. **Next natural check-in point: whichever comes
first — a ruling on Arizona's Sept 14 motion for summary disposition (No. 26-4281), or a ruling on
Kalshi's Sept 9 rehearing petition (No. 25-7516) and the mandate that would follow it.**

Sourcing note: all of the above is read directly from CourtListener's RECAP docket entries (case
names, docket numbers, dates, and the docket's own one-line descriptions), fetched via `curl` with
the environment's CA bundle after WebFetch continued to 403 on courtlistener.com — same working
pattern as 09-24. Where a docket entry's underlying PDF was not independently readable (individual
document pages 403'd this pass, unlike 09-24 when they were sometimes reachable), that is stated
explicitly above rather than inferred from the entry title alone.

## 2. FTC non-response — rechecked, still no response found

Checked ftc.gov's press-release listing directly (nothing on prediction markets, Kalshi, Polymarket,
or a response to the Mullin/Vasquez letter in the 20 most recent releases, Aug 21–Sept 24, 2026) and
searched for any follow-up statement from Reps. Mullin or Vasquez. Found nothing indicating a
response was ever received. Same status as every prior pass since 09-19: genuinely unresolved, not
a new finding. Now roughly three months past the June 29, 2026 requested-response deadline.

## 3. Illinois HB 5143 (Rep. Didech, per-wager tax repeal) — appears procedurally stalled in House Rules Committee, not "unresolved" so much as currently going nowhere

The 09-24 note left this as "final passage/signature status unresolved." This pass could not get a
clean direct fetch of the bill's own ilga.gov status page — every attempt (WebFetch and `curl`, several
URL variants, including the printable `Print=1` form) returned either a 503 or, via `curl`, a TLS
handshake failure specific to that host (Google and other sites fetched fine through the same proxy/CA
bundle in the same session, so this looks like an ilga.gov-side or edge-case block, not a general
tooling failure). That is a real limitation of this pass, not glossed over.

What could be confirmed, from two independent Google-indexed snippets of the ilga.gov bill-status page
itself (not secondary news commentary) surfaced via WebSearch: **on 3/27/2026, HB 5143 was subject to
House Rule 19(a) and re-referred to the Rules Committee**, and a separate snippet independently
describes the bill as "currently pending in the House Rules Committee" with "25% progression." House
Rule 19(a) re-referral is what happens automatically when a bill misses its chamber's own procedural
deadline (here, a third-reading deadline preceding the April 17, 2026 crossover deadline already noted
in this project's files) — in ordinary Illinois legislative practice this typically means a bill is
shelved for the session unless House leadership actively pulls it back out of Rules, not that it was
voted down. **Caveat, stated plainly: this is based on search-engine-indexed snippets of the primary
source, not a page this session was able to render and read directly** — the specific fact type (a
named procedural rule and a specific date) is a good sign it is accurately quoting the ilga.gov page
rather than a generative summary, but it is not the same confidence tier as the direct primary-source
reads elsewhere in this note, and a future session should retry ilga.gov directly to confirm and to
check for any later action past March 27. No news coverage found (searched again this pass) reports
the bill advancing further, being voted on, or being withdrawn — consistent with, but not proof of,
the re-referral finding.

**Net effect for the project's still-open design question** (does this per-wager excise tax belong in
the coded policy table, and if so as what kind of variable — flagged 09-24, not decided here): if the
re-referral finding holds up, the practical policy fact for the study period is that Illinois' per-wager
tax has been in effect since July 1, 2025 and remains in effect today, with a repeal effort that has
stalled rather than succeeded. That is a firmer basis for coding it as a stable (not time-varying)
policy feature during the study period than the 09-24 note had, if Britton decides to add it — still
his call whether/how to add it.

## 4. H.R. 10357 — rechecked, no material change since 09-24

congress.gov and govtrack.us both blocked direct fetches this pass (Cloudflare challenge page on
congress.gov; 403 on govtrack.us) — a real tooling limitation, not a finding. Secondary-source search
(multiple independent outlets: Legal Sports Report, Las Vegas Sun, Covers, Yogonet, Horse Racing
Nation) is unanimous and consistent with the 09-24 note: passed House Ways & Means 38-5 on Sept 16,
2026 as part of the broader Digital Asset Tax Certainty Act package, now awaiting a House floor vote
not expected before the November 2026 midterms. No new figures beyond the previously-logged JCT
~$2B/2027–2036 revenue-cost estimate. Per the task's own instruction this item is low priority; treated
as reconfirmed at the same (secondary-source) sourcing tier as before, not escalated further this pass.

## What's still open / unresolved after tonight

- **FTC non-response** — recheck again in a few weeks; now roughly three months past the requested
  response deadline.
- **Arizona/Kalshi** — genuinely more complex than "stayed, waiting for a mandate": two separate
  Ninth Circuit dockets (26-4281 Arizona's own appeal, 25-7516 the consolidated Assad case) both have
  live, unresolved motion practice as of this week, while the district case itself has had zero
  substantive activity since the May 18 stay order. Next check-in: a ruling on either Arizona's Sept 14
  motion for summary disposition or Kalshi's Sept 9 rehearing petition, whichever comes first.
- **Illinois HB 5143** — likely stalled in House Rules Committee since March 27, 2026 per re-referral
  under Rule 19(a), based on search-indexed primary-source snippets rather than a direct page read this
  session; needs a direct ilga.gov confirmation next time the site is reachable. Still an open design
  question for Britton whether/how this tax mechanism should be coded at all.
- **H.R. 10357** — no floor vote expected before the November midterms; next natural check-in point is
  after the midterms, per the task's own low-priority framing.
- The fiscal-dependence/consumer-protection-policy (C+D) framing question and every other item in
  `PROJECT_STATUS.md`, `DECISION_LOG.md`, and `notes/open_questions.md` remains exactly as it was —
  this pass was scoped to the four recurring litigation/legislative-tracking items, not a full project
  review, and nothing here should be read as advancing or resolving that framing question.

No fabricated citations, docket numbers, case names, dates, or figures were introduced this pass.
Where a route was genuinely blocked (ilga.gov, congress.gov, govtrack.us, and individual CourtListener
document pages all 403'd or failed TLS at various points this session), that is stated plainly above
next to the specific claim it affects, rather than smoothed over or worked around with an unverified
guess.
