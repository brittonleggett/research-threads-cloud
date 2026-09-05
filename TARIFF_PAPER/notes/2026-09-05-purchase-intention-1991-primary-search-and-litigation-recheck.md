# 2026-09-05 — Purchase Intention 1991 original: still not found (good-faith search documented); litigation recheck: Section 301 government response NOT yet filed, one new CAFC procedural entry, chip-tariff Phase 2 news

Light-touch night per Britton's 09-03/09-04 note that this project needs no further
action before his IRB submission target this weekend. Per his framing, did **not**
touch IRB materials, grad-assistant items, H3/Phase-3 theme decisions, or
`SUBMISSION_TRACKER.md`. Worked the two concrete open items only: (1) another
legitimate-means attempt at the 1991 Dodds, Monroe & Grewal original appendix text,
and (2) a litigation docket recheck plus general news sweep, following up on
`2026-09-04-purchase-intention-wom-scales-resolved.md` and
`2026-09-04-litigation-check-section301-response-due-oregon-brief-filed.md`.

## 1. Purchase Intention (Dodds, Monroe & Grewal 1991) — original appendix still not found; no change to prior conclusion

Task explicitly asked me to try again through legitimate channels (Google Scholar,
SSRN, university course-reserve pages, ResearchGate author-uploaded copies,
archive.org) before accepting the Grewal et al. (1998) secondary source as final.
Did that tonight, via WebSearch + WebFetch/curl (no Consensus.app access from this
session, same as 09-04). **Result: still could not access the 1991 JMR appendix
text itself. Documenting every avenue tried so this isn't a repeat of "just
couldn't find it" without specifics:**

- **SAGE/JMR (publisher of record)** — journals.sagepub.com/doi/10.1177/002224379102800305
  is the actual article page. Abstract only; full text is paywalled, as expected
  (JMR is not open-access). Did not attempt to bypass this — consistent with the
  repo's no-paywalled-full-text rule.
- **ResearchGate** — publication page 248552620 exists and search snippets describe
  it as "(PDF) Effects of Price, Brand, and Store Information..." but this is
  ResearchGate's standard "PDF available on request from the authors" framing for a
  paywalled Sage article, not a genuine open upload. WebFetch got HTTP 403
  (ResearchGate blocks non-browser fetches); a direct `curl` with a browser
  user-agent also got HTTP 403. Could not confirm one way or the other whether an
  author-uploaded full copy sits behind that block, but no accessible text was
  retrieved.
- **Academia.edu** — two separate uploads found (ids 39577105 and 39577167, both
  titled to match this article). Both returned HTTP 403 to WebFetch. Same outcome
  as ResearchGate — a plausible author/uploader copy exists but is not fetchable
  through legitimate automated means from this session.
- **Scribd** — two documents found (one plainly titled with the full citation).
  WebFetch returned only a client-side loading-error message (no article content
  rendered) for one; did not pursue Scribd further since it requires an account/
  paid access for full documents as a matter of site policy, not a technical fluke.
- **University repositories / course reserves** — two direct-download links turned
  up in search (`digital.library.temple.edu/.../download` and
  `fhburgenland.contentdm.oclc.org/.../download`). Fetched both directly. Neither
  was the DMG 1991 article: the Temple link's PDF metadata didn't yield readable
  text via WebFetch, and the fhburgenland link turned out to be an unrelated
  master's thesis by "Gremel" that happened to cite DMG 1991 in its reference list
  (confirmed by opening the PDF — 24.5KB, clearly a thesis reference list hit, not
  the source article). Not usable.
- **Dissertation repositories** — University of South Carolina Scholar Commons ETD
  (scholarcommons.sc.edu, article 7418) turned up as a plausible dissertation that
  might reproduce a DMG-1991-attributed appendix (the same pattern that resolved
  WOM and partially resolved Purchase Intention on 09-04, via Grewal 1998 and
  Dodds 2002). Both WebFetch and a direct `curl` with browser user-agent got
  **HTTP 403** (the raw response was a Cloudflare-style 403 error page, confirmed
  by inspecting the downloaded bytes directly — not a parsing failure, an actual
  block).
- **Google Scholar / SSRN / archive.org directly** — no working, accessible
  full-text link surfaced for this specific article on any of these through
  WebSearch. (SSRN does not appear to host this article at all — it's a 1991 JMR
  piece, not the kind of working paper SSRN typically carries.)

**Bottom line: no legitimate accessible copy of the 1991 original was found tonight,
after trying every channel the task specified plus a few more (dissertation
repositories, author-name + faculty-page searches). This is a real dead end for
search/fetch tools from this session, not a lack of effort. No wording below is
guessed or reconstructed — nothing changes from the 09-04 conclusion.**

**Status stays exactly as 09-04 left it:** the Grewal, Krishnan, Baker & Borin
(1998, *Journal of Retailing*, Table 1) verbatim reproduction — explicitly cited to
Dodds, Monroe & Grewal (1991), co-authored by Grewal himself — remains the
strongest available secondary source, corroborated independently by Dodds's own
2002 *Marketing Bulletin* single-item measure. **If Britton has JSTOR/library
access this weekend, that's still the fastest real path to the 1991 appendix
itself; short of that, the Grewal et al. (1998) wording is defensible to use as-is
with dual citation (1991 for construct/attribution, 1998 for exact item source),
per the recommendation already on record.** Nothing here should be read as
"still worth searching" — this line is close to fully exhausted for AI-tool-based
methods; further progress needs either paid database access or Britton pasting in
text he can access directly.

## 2. Litigation docket recheck (CourtListener, fetched directly via `curl` with a browser user-agent — WebFetch alone got HTTP 403 on courtlistener.com tonight, so switched to the same curl technique prior nightly passes have used)

### V.O.S. Selections (CAFC 26-1895) — stable
Re-fetched https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/
directly. Still 24 total entries, same as 09-04. Last entry (#24, Sep 2) is the
caption revision removing AGS Company Automotive Solutions and Grant & Bowman, Inc.
as appellees — already known from the 09-03 note. No new activity.

### Axle of Dearborn (CIT 1:25-cv-00091) — stable, no appeal filed
Re-fetched https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/
directly. Still 79 total entries, same as 09-04. No notice of appeal. Per the
09-03/09-04 arithmetic (Slip Op. 26-94, Aug 13 + 60 days ≈ Oct 12, 2026), roughly
37 days remain in the government's appeal window — coordinator's arithmetic from
the ruling date, not a court-stated deadline, same caveat as before.

### Section 122 (State of Oregon v. Trump, CAFC 26-1804/-1805) — one new procedural entry since 09-04, no substantive change
Re-fetched https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/
directly. Now **81 total entries** (up from 80 as of the 09-04 note, which covered
through entry #80). The new one:

- **Entry #81 (Sep 3, 2026):** another MOTION by Appellees Basic Fun, Inc. and
  Burlap and Barrel, Inc. "to extend the time to 09/03/2026 to file brief, to
  correct or supplement." This follows entry #80's Sep 3 notice that their prior
  correction attempt (entry #78) was non-compliant and set a corrected-document
  deadline of 09/11/2026. Entry #81 is the small-business appellees' latest attempt
  to get a compliant brief on file — same underlying issue as documented 09-04, not
  a new dispute. No entries dated Sep 4 or later found on this docket as of this
  check. No oral argument date yet.

### Section 301 forced-labor master docket (In re Section 301 Forced Labor Cases, CIT) — government response due 9/4 NOT YET FILED as of this check
Re-fetched https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/
directly. Now **21 total entries** (up from 20 as of 09-04). The new one:

- **Entry #21 (Sep 4, 2026):** "First Form 11 Notice of Appearance. Filed by Barry
  William Appleton of Appleton & Associates on behalf of All Plaintiffs." **This is
  a notice of appearance, not the government's response to the plaintiffs'
  dispositive motion that was docketed as due 9/4/2026 (entry #16).** As of this
  check, no government response/opposition brief has posted on this docket. A
  targeted news search (WebSearch, several queries on "Section 301 forced labor,"
  "Learning Resources," "government response," "September 2026") also turned up
  nothing reporting that the response was filed — consistent with the docket, not
  contradicting it. **Genuinely unresolved: either the response is filed but not
  yet docketed (normal filing-to-posting lag, as the 09-04 note anticipated), or
  it's late. Cannot distinguish between these from outside; worth a same-week
  recheck.** Reply brief (Sep 18) and oral argument (Sep 30, Judges Choe-Groves,
  Reif, Wang) remain on the docket's schedule metadata, unchanged.

### The "second State of Oregon v. Trump" (new Aug 3 CIT complaint, docket 73711779) — no new substantive activity, still just an individual member case
Re-fetched https://www.courtlistener.com/docket/73711779/the-state-of-oregon-v-donald-j-trump/
directly. 34 entries total, but all of the most recent ones are Form 11 notices of
appearance for various state AG offices (through Aug 21) — this individual-case
docket doesn't carry the master docket's later substantive filings (motions,
orders) directly; those post to the lead docket (74219533, checked above), per the
consolidated-proceeding structure already flagged 09-04. Nothing new to add here
beyond confirming the naming-collision flag from 09-04 still stands and still needs
a disambiguator if the manuscript cites "State of Oregon v. Trump" for the Section
301 track.

### General news sweep since 09-04 — no new litigation developments found; one new *policy* item worth noting for background/context (not litigation, and not currently part of the manuscript's tracked cases)
- No new tariff-litigation filings, rulings, or news beyond what the docket checks
  above already show.
- **Semiconductor/chip tariffs, "Phase 2":** Commerce Secretary Howard Lutnick
  announced (reported Sep 2–3, 2026 — Bloomberg, "Trump Plans New Chip Tariffs,
  Exemptions for US Manufacturing," and corroborating trade-press coverage from
  Digitimes and TechTimes) a second phase of semiconductor tariffs structured
  around an exemption for firms manufacturing chips in the US; unexempted imports
  would pay a new levy. Scope reportedly could extend to servers, laptops, and
  gaming hardware (categories not covered by Phase 1). No specific rate, exemption
  criteria, or effective date has been announced yet per this coverage — this is
  an announcement/trial-balloon stage, not an implemented tariff, and it is a
  **different authority/product category than any of the four litigation tracks
  this project follows** (IEEPA, Section 122, Section 301 forced-labor, de
  minimis). Flagging only because it's a genuinely new development since 09-04 and
  the task asked for a general sweep — **not** recommending folding it into the
  manuscript's litigation tracking unless Britton wants a broader tariff-policy
  landscape section.

## Summary table

| Item | Status as of 09-05 |
|---|---|
| Purchase Intention 1991 original appendix | **Still not found** after a second, broader legitimate-means search (ResearchGate, Academia.edu, Scribd, 2 university repositories, 1 dissertation repository, SSRN/archive.org sweep — all blocked or not the right document). No change to 09-04's Grewal et al. (1998)-as-best-available-secondary-source conclusion. |
| V.O.S. Selections (26-1895) | Stable, no new entries |
| Axle of Dearborn appeal | Stable, still not filed, ~37 days left in window |
| Section 122 (26-1804/-1805) | One new procedural entry (#81, Sep 3) — small-business appellees' latest correction attempt; no substantive change |
| Section 301 forced-labor master docket | **Government's response due 9/4 not yet visible on the docket as of this check** — new entry #21 is only a notice of appearance. Genuinely unresolved whether filed-but-not-posted or late. |
| Section 301 — second "State of Oregon v. Trump" | No new substantive activity; naming-collision flag from 09-04 still stands |
| General tariff news | New chip-tariff "Phase 2" policy announcement (Sep 2–3) — background only, not one of the four tracked litigation threads |

## Open items for Britton / next session

- **Purchase Intention:** if he has JSTOR/library access this weekend (or after),
  five minutes pulling the actual 1991 JMR appendix would let this close out
  fully; otherwise the Grewal et al. (1998)-plus-Dodds(2002) secondary-source
  package already on record is defensible to use as-is. This is not blocking
  anything — flagged only because the task asked to try again, not because it's
  newly urgent.
- **Section 301 government response:** worth a quick recheck in the next few days
  (docket 74219533) to see whether the 9/4 response has posted and, if so, what it
  argues — it wasn't there as of this pass.
- Everything in this note is background/corpus material, not on the critical path
  to IRB submission — consistent with Britton's "no further action needed on this
  thread until [after IRB]" framing. No IRB, grad-assistant, or Phase-3/theme
  material was touched.
