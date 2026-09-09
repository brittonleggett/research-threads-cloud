# 2026-09-09 — Docket recheck partially blocked by new CourtListener anti-bot challenge; McNeese's own IRB policy page directly answers the CITI Basic-vs-Comprehensive question

Per the standing autonomy mandate: worked the two concrete open threads this project had
flagged (litigation docket recheck, and open question #1 on CITI training), did not touch
IRB submission itself, scale/instrument content, grad-assistant status, H3, or any Phase-3/
theme material — none of that is mine to move.

## 1. Litigation docket recheck — 2 of 4 confirmed stable, 2 blocked by a new AWS WAF challenge

Re-fetched all four CourtListener dockets via direct `curl` (same technique as 09-04
through 09-08). Two came through clean:
- **V.O.S. Selections (CAFC 26-1895):** still 24 total entries, unchanged since 09-04.
- **Axle of Dearborn (CIT 1:25-cv-00091):** still 79 total entries, unchanged since 09-04.

The other two returned **HTTP 202 with an AWS WAF JavaScript challenge page** (`awswaf.com`
challenge script, no docket content) rather than the docket HTML:
- **Section 122 / State of Oregon v. Trump (CAFC 26-1804/-1805)** — blocked.
- **Section 301 forced-labor master docket (CIT 1:26-cv-03555)** — blocked, so **tonight's
  check of the (now 5-days-overdue as of 09-09) government response could not be
  independently confirmed** via direct docket read. Retried once after a delay and with
  fuller browser headers — same WAF challenge both times. This is a new failure mode, not
  one of the two previously-logged WebSearch-synthesis fabrications — didn't attempt a
  workaround beyond a courteous retry (no CAPTCHA-solving, no header-spoofing beyond
  standard browser headers), consistent with not fighting bot-detection. **Recommend the
  next session try again fresh** (this may be a rate-limit from the volume of automated
  hits this docket has taken across nightly runs, not a permanent block) — if it's
  persistent, CourtListener's own RECAP API or PACER directly may be needed instead of
  scraping the HTML docket page.

## 2. Open question #1 (CITI Basic vs. Comprehensive) — strong primary-source answer found

`SUBMISSION_TRACKER.md` open question #1 asked whether to check with McNeese's IRB office
on whether Britton's current CITI "Stage 1 - Basic Course" (refreshed 2026-09-03, Record ID
79382211) satisfies the requirement, since McNeese's policy text names a "Comprehensive"
module. **Fetched McNeese's own published HSIRB policy page directly**
(`mcneese.edu/policy/human-subjects-institutional-review-board-hsirb-policy/`) rather than
trusting a search engine's synthesis of it (a WebSearch pass on this same question
returned a plausible-sounding synthesized answer first — treated as unverified per this
project's own standing caution on search-synthesis fabrication, and checked against the
actual page before using it). **The policy's own text, quoted directly:**

> "All researchers involved in research with human subjects must complete a CITI Program
> training module about human subjects protection, either 'Biomedical Comprehensive' or
> 'Social/Behavior/Educational Comprehensive'"

No mention of a "Basic Course" or "Refresher" option anywhere in this policy page. For a
consumer-behavior/marketing survey/experiment, the applicable track would be
**Social/Behavior/Educational Comprehensive** — which, per the tracker, is not what
Britton's current CITI record shows (Basic Course/Refresher).

**This is strong evidence, not a confirmed final answer** — it's what McNeese's own policy
page says in writing, but policy pages can lag actual practice, and there may be an
"or equivalent"/grandfathering allowance not stated here. Per the standing rule, contacting
the IRB office directly is still the right way to get a definitive answer and is an
external action — not something to do autonomously. **Recommend Britton either (a) email
the IRB office to confirm, or (b), given how directly this matches the policy's literal
text, just complete the Social/Behavior/Educational Comprehensive CITI module now rather
than waiting on a reply** — CITI modules are typically a same-day, self-paced
completion, and this would remove the ambiguity entirely rather than risk a rejected/kicked-
back IRB submission over a training-credential mismatch.

**Turnaround-time question (open question #2) — not resolved tonight.** Tried three
McNeese HSIRB sub-pages that search results pointed to for stated review-turnaround
language (`/hsirb/irb_review_procedures/`, `/hsirb/`, and the linked flowchart PDF) — all
three returned HTTP 404, site structure appears to have changed since those pages were
indexed. Didn't keep digging past three dead ends (matches the "don't rabbit-hole"
guidance) — this one likely still needs Britton to ask the IRB office directly, or check
whatever portal/SharePoint the policy page references ("detailed review process... on the
Graduate School SharePoint").

## What's still open / for Britton

- **CITI training:** strong evidence (McNeese's own policy page, quoted above) that the
  Social/Behavior/Educational Comprehensive module is required, not the Basic
  Course/Refresher currently on file. Recommend completing it directly rather than waiting
  on an IRB-office reply, given the Oct 15 deadline pressure.
- **HSIRB turnaround time:** still unknown — the pages that might state it are 404 now;
  needs a direct ask to the IRB office or the Graduate School SharePoint the policy
  references.
- **Section 301 docket:** now likely 5 days overdue on the government's response as of
  09-09, but couldn't be independently re-confirmed tonight due to the new WAF block —
  treat the 09-08 note's "4 days overdue" as the last confirmed read, not current.
- **IRB submission itself:** the 09-03 "no further action needed until the weekend" framing
  is now several days past that weekend with nothing in this repo showing submission
  happened — worth Britton confirming status directly; this is the actual critical-path
  item and not something any automated session can check for him.
- Litigation dockets, scales, H3, grad-assistant status, Phase 3: all previously resolved
  or explicitly out of scope tonight, untouched.
