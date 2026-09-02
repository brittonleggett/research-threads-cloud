# Nhan & Helfers (2026) disclosure-statement access attempt

2026-09-02. Follow-up to 2026-09-01's finding that Crossref funder metadata for the Nhan & Helfers
article lists Flock Safety as a funder (award 23854). That finding was metadata-only; this session
tried to read the article's own printed disclosure/funding-statement text.

## Article identity (re-confirmed)

- DOI: `10.1177/0032258X251349633`
- Title: "Cops and hotlists: Balancing security and privacy with ALPR technology"
- Authors: Johnny Nhan (Texas Christian University), Richard C. Helfers (University of Texas at
  Tyler)
- Journal: *The Police Journal: Theory, Practice and Principles* (SAGE), Vol. 99, Issue 1, pp. 160–179
- Published online 2025-06-04; print issue March 2026 — confirms this project's "(2026)" citation is
  the print-issue year for the same online-first article.
- Re-queried the full Crossref record directly by DOI: funder metadata unchanged from 09-01 —
  `"funder": [{"name": "Flock Safety", "award": ["23854"]}]`.

## Could not access the article's own disclosure text

Every access route tried failed or confirmed no legitimate access exists:
- `journals.sagepub.com` (publisher, direct) — HTTP 403, consistent with prior sessions.
- `sage.cnpereading.com` (SAGE's China-hosted mirror) — WAF/CAPTCHA page, no content.
- ResearchGate — 403/404 on all attempts.
- DeepDyve — 403.
- CrimRxiv — 403 on search.
- **Unpaywall API** (authoritative OA check): `"is_oa": false, "oa_status": "closed",
  "has_repository_copy": false, "oa_locations": []`. **No legally open-access copy of this article
  exists anywhere Unpaywall indexes** — no preprint, no green-OA repository deposit. This confirms the
  paywall is real and universal, not an environment-specific block.
- `stopflocksafety.org` (advocacy aggregator) — only a reposted abstract/summary, no full text.

No piracy/paywall-circumvention route was attempted — outside the scope of legitimate research access,
consistent with this project's standing rules.

## Independent corroboration found instead: the author's own CV

Johnny Nhan's official TCU CV (`tcu.edu/directory/files/NhanCV2026.pdf`, updated January 2026), under
"Grants & Other External Support – Awarded," lists:

> "2024 Flock Safety evaluation of LPR technologies — sponsored research $4,000 ($8,000 total, $4,000
> per co-PI)."

This is a **self-disclosed sponsored-research grant from Flock Safety**, split between two co-PIs
(consistent with a Nhan/Helfers pairing), awarded in 2024 — plausibly the year fieldwork for this
article occurred, given June 2025 online publication. The same CV also lists Nhan and Helfers as
"consultants/editors" on a separate 2024 Flock Safety white paper ("Flock Safety technologies in law
enforcement: An initial evaluation of effectiveness in aiding police in real-world crime clearance,"
Snow & Charpentier, Flock Safety white paper), and a "Flock press release" media engagement tied to
that earlier study.

A Techdirt investigative piece (April 2024) on that earlier Flock-funded white paper reported that
Flock controlled researchers' access to police-department data and steered the study toward agencies
likely to show favorable crime-reduction statistics, and quoted Nhan expressing discomfort with data
quality and how findings were later characterized in Flock's press materials. **That reporting
concerns the earlier white-paper project, not "Cops and hotlists"** — but it documents a pattern of
Flock Safety influence over Flock-funded outputs involving this same author.

## Assessment — what this does and does not establish

- **Upgraded from metadata-only to metadata + independent author self-disclosure:** the Crossref
  funder listing (Flock Safety, award 23854) is now corroborated by an independent, author-authored
  source (Nhan's own CV) documenting a real Flock Safety sponsored-research grant to Nhan and a co-PI
  in 2024, on the same topic (LPR technology evaluation), in the plausible fieldwork timeframe.
- **Still NOT confirmed:** whether the CV's $4,000/$8,000 grant line is the *identical* funding
  instrument as Crossref's "award 23854" — this is plausible, not proven. Equally plausible: "Cops and
  hotlists" drew on a related-but-separate Flock funding line not itemized identically on the CV. The
  article's own printed Funding/Disclosure section could not be read through any legitimate route
  found.
- **Do not round this up** in the manuscript to "the article's disclosure section confirms Flock
  Safety funding" — that specific claim is unverified because the disclosure section itself was
  inaccessible. What is verified: (a) Crossref-registered funder metadata says Flock Safety/award
  23854; (b) the corresponding author's own CV independently confirms Flock Safety sponsored-research
  funding on the same topic in the relevant timeframe; (c) a previously reported pattern (Techdirt) of
  Flock Safety controlling data/methodology on this author's earlier Flock-funded work.

## For Britton

This strengthens (from metadata-only to metadata + author self-disclosure) but does not fully close
the "researcher independence" concern flagged 09-01 — still worth your own read/judgment call before
this citation is used uncritically, per that note. The article's disclosure text itself remains
unread; if you have institutional/library access to SAGE, that would be the fastest way to close this
completely. No repo files or citations were edited tonight — reporting only, per this project's
standing instruction that Phase 3/theory-chain-adjacent judgment calls on how to handle this citation
stay yours.
