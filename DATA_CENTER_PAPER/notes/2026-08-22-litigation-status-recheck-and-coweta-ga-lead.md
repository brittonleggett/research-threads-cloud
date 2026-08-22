# 2026-08-22 — Litigation status re-check (Sabey, MS/TN xAI) + new Coweta County, GA lead + WebFetch re-test

## WebFetch status — still blocked, tested against two real queued targets (not just the control)
Per 08-21's note, two specific pulls were queued for "when WebFetch returns": the Kent, OH signed
ordinance PDF and the JAPA/Kollar article's abstract page. Tested both directly tonight instead of
just the Wikipedia control:
- `https://www.kentohio.gov/media/yrhjyjrn/2026-31-data-center-moratorium_signed.pdf` → `EGRESS_BLOCKED`
- `https://www.tandfonline.com/doi/full/10.1080/01944363.2026.2618221` → `EGRESS_BLOCKED`

Same failure mode both times (network egress proxy blocking the domain), consistent with 10+ prior
sessions. **11th+ consecutive session WebFetch is down.** Both pulls stay queued. Everything below
is WebSearch-summarized only, same confidence tier as every prior note.

## 1. Sabey Corp / Decatur Township judicial review — still no ruling, nothing changed since 08-21
Ran several targeted searches (hearing outcome, "dismissed OR denied OR granted", Mirror Indy's
own coverage archive, day-after-hearing queries). **No coverage of the Aug 20, 2026 motion-to-
dismiss hearing's outcome has surfaced.** This is a real "still pending" — not a gap in search
technique; the most recent dated Sabey coverage found tonight is the same tax-abatement/aquatic-
center piece already cited in 08-21's note. The Sept. 16, 2026 Metropolitan Development Commission
vote on the ~$242M incentive package is still a future date (confirmed still scheduled, nothing
moved up). **Recommend one more re-check in a few days** — motion-to-dismiss rulings often issue
as a written order some time after the hearing, so this may just need more elapsed time, same as
08-21 flagged.

## 2. MS/TN xAI/Colossus DOJ intervention — no ruling on the intervention motion, but found a concrete near-term date
Also still no ruling on DOJ's June 15 motion to intervene/dismiss. New and useful: found the case
number and a scheduled hearing not in prior notes.
- **Case:** *NAACP v. xAI Corp. et al.*, No. 3:26-cv-00074-DMB-JMV, U.S. District Court for the
  Northern District of Mississippi, Oxford Division.
- **NAACP/Earthjustice/SELC filed for a preliminary injunction** (their own emergency motion,
  separate from DOJ's motion to intervene) seeking to halt the unpermitted turbines — filed brief
  visible at [earthjustice.org (PI brief PDF link, not fetched)](https://earthjustice.org/wp-content/uploads/2026/05/file-stamped-xai-pi-brief.pdf).
- **An evidentiary hearing on that preliminary-injunction motion is scheduled for Aug. 24, 2026** —
  two days from tonight. [Yahoo/AP syndication](https://www.yahoo.com/news/us/articles/spacexai-hearing-decide-future-southaven-100436668.html)
- Also newly surfaced: NAACP's notice-of-violation history predates the suit — notified xAI/MZX
  Tech in February 2026 that the original 27 turbines violated the Clean Air Act; instead of
  addressing it, the companies added 6 more turbines (33 total) before suit was filed in April.
  [NAACP.org](https://naacp.org/articles/naacp-asks-court-emergency-action-stop-illegal-air-pollution-xais-data-center-power-plant), [SELC](https://www.selc.org/press-release/naacp-asks-court-for-emergency-action-to-stop-illegal-air-pollution-from-xais-data-center-power-plant/)
- DOJ's motion to intervene notably **does not dispute that the turbines lack required permits** —
  its argument is entirely that national/economic/energy-security stakes outweigh enforcement,
  per a secondary summary (Mondaq legal-analysis piece), worth noting as it sharpens the
  "national-security override" framing for the `federal-national-security-override` candidate code.
- **Net status:** both DOJ's motion to intervene and NAACP's preliminary-injunction motion are
  still pending. **Aug. 24, 2026 is a concrete date worth a same-question re-check right after** —
  a ruling or at least hearing coverage is plausible within days of that date, unlike Sabey where
  there's no similarly dated next event on record.

## 3. New, well-sourced corpus lead: Coweta County, GA — "Project Sail" ($17B, 829 acres)
Found while re-verifying GA material; **not the same site as existing Tier 2 rows #18/#19**
(Stanton Springs/Newton Co. and Covington) — this is a third, distinct GA county case, and it's
unusually well-documented (AJC, WSB-TV, FOX5 Atlanta, CBS Atlanta, Times-Herald, GovTech, DeSmog
all independently covering it). Timeline:
- **May 2025:** Coweta County Board of Commissioners adopted a 180-day moratorium to revise data-
  center zoning/ordinance rules, prompted by the proposed Project Sail campus. [Times-Herald](https://www.times-herald.com/news/commissioners-approve-180-day-data-center-moratorium/article_29dd50b8-88fb-4424-98d9-9d87abfb4588.html), [GovTech](https://www.govtech.com/products/second-atlanta-area-government-hits-pause-on-data-centers)
- **April 2026:** moratorium having lapsed/been revised, commissioners voted **3-2 to approve**
  Project Sail — Atlas Development LLC's 829-acre, $17B, nine-building (4.34M sq ft) campus on
  rural land. [AJC](https://www.ajc.com/business/2026/04/coweta-votes-to-turn-this-800-acre-forest-into-17b-data-center-campus/), [FOX5 Atlanta](https://www.fox5atlanta.com/news/coweta-county-approves-massive-project-sail-data-center)
- **May 5, 2026:** 17 residents/farmers/landowners sued in Coweta County Superior Court, seeking
  to void the rezoning — arguing the 3-2 vote was an abuse of power/due-process violation for the
  1,200+ homes within 1.25 miles of the site. Notable framing hook: the site sits in the Middle
  Chattahoochee River basin, state-designated a "Most Significant Groundwater Recharge Area" —
  a resource-scarcity/environmental angle distinct from Stanton Springs' EJ/racial-disparity
  framing, giving Coweta a different grievance profile within the same state. [CBS Atlanta](https://www.cbsnews.com/atlanta/news/coweta-county-residents-file-appeal-to-stop-massive-data-center-on-protected-rural-land/), [The Citizen](https://thecitizen.com/2026/05/11/coweta-residents-sue-to-block-project-sail-data-center/)
- Also notable: a 1,750-signature opposition petition, and a Coweta County farmer's viral video
  testimony opposing use of eminent domain for the project (AtlantaFi.com coverage, not
  independently corroborated elsewhere — treat that specific detail as lower confidence than the
  rest).
- **Litigation outcome:** not established by this search pass — same "pending" status as the two
  threads above; not chased further tonight given time budget.

**Why this is worth flagging rather than adding as a formal corpus row:** it strengthens the
existing GA leg of the multi-state design (a second, structurally different GA case — litigation
over an *already-approved* project versus Stanton Springs' Congressional-hearing/EJ angle) and
adds a genuinely new grievance vocabulary (groundwater recharge area protection, eminent domain)
worth Britton's eye for the moderator/theme map. **Not added as a numbered corpus row** — that's
still gated on the open corpus-size call, and this item hasn't been WebFetch-verified, same
Tier-3-equivalent standard as everything else pending direct-source confirmation.

## Also noted, not chased further: Clinton County, IN corroboration strengthened
While re-checking, Clinton County's 3-0 rezoning denial (Jan. 20, 2026) turned up independently in
seven-plus local outlets (Clinton County Daily News, Inside INdiana Business, ftimes.com, WTHR,
Clinton County Today, Carroll County Daily News, Fox59, WISH-TV) — the same fact pattern already
in the corpus draft as Tier 3's "one of the only outright opposition wins," now corroborated well
beyond a single-source level. Not promoting its tier myself — flagging that it's about as solid as
WebSearch-only verification gets, same evidentiary bar the 08-21 note applied to the DOJ/xAI fact
pattern.

## What's still open / blocked on Britton
- **Corpus-size call (exemplar vs. comprehensive)** — untouched tonight, unchanged.
- **Sabey/Decatur Township ruling** — still unknown; no new information since 08-21; re-check in a
  few more days.
- **MS/TN DOJ intervention + NAACP preliminary-injunction ruling** — still unknown; but now has a
  concrete near-term date (Aug. 24, 2026 evidentiary hearing) worth a targeted re-check right after.
- **Coweta County, GA (Project Sail)** — new, well-sourced lead; not yet WebFetch-verified or
  added as a formal corpus row; litigation outcome also unresolved.
- **Kent, OH ordinance PDF + JAPA/Kollar abstract page** — still blocked on WebFetch specifically,
  unchanged; both re-tested directly tonight (not just the Wikipedia control) and both still fail.

## WebFetch status (for the running tally)
11th+ consecutive session `EGRESS_BLOCKED`. Tonight tested two real queued targets directly (Kent
OH ordinance PDF, JAPA/tandfonline abstract page) instead of only the neutral Wikipedia control —
same error both times. If it comes back working in a future session, flag prominently at the top
of that session's note per standing instruction; several primary-source pulls are queued (Kent OH
ordinance, JAPA abstract, CCS Paper's legis.la.gov HB79 page, the DOJ.gov filing PDF, and now the
NAACP/Earthjustice preliminary-injunction brief PDF).
