# Study 2 — Qualtrics Post-Import Checklist (2026-09-11)

Companion to **`Study2_Qualtrics_IMPORT_2026-09-11.txt`**. The import file carries all 11 blocks,
6 vignette blocks, 32 questions, choices, and export tags. Qualtrics' Advanced Format **cannot**
carry Survey Flow, randomization, branch logic, timers, or embedded-data assignment — those are the
steps below. Budget ~20 minutes.

## Step 0 — Import
Qualtrics → **Create new project** → Survey → **"Import a survey file"** → select
`Study2_Qualtrics_IMPORT_2026-09-11.txt`. You should land on 16 blocks / 32 questions.

## Step 1 — Paste the two long texts (2 min)
Advanced Format can't safely carry multi-paragraph legal text, so two placeholders are in the file.
Both are marked `<PASTE THE FULL TEXT OF …>`:
- `consent_text` (Consent block) ← `Informed_Consent_Tariffs.docx`
- `debrief` (Debriefing block) ← `notes/2026-08-04-debriefing-statement.md`

## Step 2 — Survey Flow (the main job)
Build this exact structure in **Survey → Survey Flow**:

```
1.  Block: Consent
2.  Branch If: consent = "I do not agree to participate"  ->  End of Survey (ineligible message)
3.  Block: Screener
4.  Branch If: age_screen < 18                             ->  End of Survey (ineligible message)
5.  Branch If: us_resident = "No"                          ->  End of Survey (ineligible message)
6.  Randomizer  —  "Evenly Present Elements", 1 of 6:
        Group A: Set Embedded Data {AttributionFrame=explicit, CostResponse=pass-through} + Block: Vignette 1
        Group B: Set Embedded Data {AttributionFrame=explicit, CostResponse=absorption}   + Block: Vignette 2
        Group C: Set Embedded Data {AttributionFrame=vague,    CostResponse=pass-through} + Block: Vignette 3
        Group D: Set Embedded Data {AttributionFrame=vague,    CostResponse=absorption}   + Block: Vignette 4
        Group E: Set Embedded Data {AttributionFrame=silent,   CostResponse=pass-through} + Block: Vignette 5
        Group F: Set Embedded Data {AttributionFrame=silent,   CostResponse=absorption}   + Block: Vignette 6
7.  Block: Manipulation Checks
8.  Block: Perceived Price Fairness
9.  Block: Perceived Opportunism
10. Block: Trust in the Company
11. Block: Purchase Intention
12. Block: Word-of-Mouth Intention
13. Block: Demographics
14. Block: Debriefing
```

**Critical:** the Set-Embedded-Data element must sit *inside* each randomizer group, above its
vignette block. This is what logs condition assignment in the export — do not rely on
reconstructing condition from block order afterward.

Also tick **"Evenly Present Elements"** on the Randomizer, and set elements to present = **1**.

## Step 3 — Vignette timer
On each of the 6 vignette blocks: add a **Timing** question → set **"Enable submit after"
= 10 seconds**. (Per spec: discourages skimming.) Six separate additions, one per block.

## Step 4 — Auto-score the two derived fields
In Survey Flow, *after* the Manipulation Checks block, add two **Set Embedded Data** elements:
- `ManipCheck1Correct` = 1 if `mc_reason` matches the condition's correct answer
  (Tariffs for conditions A/B; General rising costs for C/D; No reason given for E/F), else 0
- `AttentionCheckPass` = 1 if `attn_check` statement 2 = "Somewhat agree", else 0

Simplest build: one Branch-If per condition setting the value. Or leave both blank and score in
analysis from the raw columns — the raw responses export either way, so this step is optional
convenience, not a data-integrity requirement.

## Step 5 — Survey Options
- Progress bar: on
- Back button: **off** (prevents re-reading the vignette after seeing the DVs)
- Force response: on for all scale items; **off** for the open "Prefer to self-describe" text
- Prevent ballot-box stuffing: on
- Anonymize responses per IRB — **confirm against the approved protocol before fielding**

## Step 6 — Preview and pilot
Preview all 6 paths (Tools → Preview, run 6+ times, confirm you see each vignette and that
`AttributionFrame`/`CostResponse` populate). Then the **N=150–180 pretest** per
`2026-08-04-pretest-design.md` before the main study.

---

## ⚠ Two decisions still yours — both built AS SPECIFIED, neither decided for you

1. **`opp_2` reverse polarity.** The Opportunism item 2 ("The intent in this situation was to take
   advantage of you") is the only item in the instrument running Agree→Disagree while everything
   else runs Disagree→Agree. It is built **as originally specified (unflipped)**. The standing
   recommendation in the spec is to flip the displayed anchors so respondents never hit an
   inconsistent scale direction mid-survey. If you want that, flip the choice order on `opp_2`
   after import — and then do **not** reverse-score it in analysis.
2. **Attention-check failure handling.** Built as **flag-only** (no hard terminate), per the spec's
   recommended default. If you want hard-terminate instead, add a Branch-If after the Screener block.

## ⚠ Standing blockers, unchanged by this build
- **HSIRB approval** — submitted 2026-09-08, still pending. Do not field before approval.
- **Vignettes are v1 drafts, not yet face-validity reviewed by you and not pretested.** The import
  file uses them verbatim from `notes/2026-08-04-vignette-drafts-v1.md`. Your sign-off on the
  Silent-condition design tension (documented at the end of that note — "keep as drafted" vs. "make
  Silent truly silent") is still outstanding, and option 2 would change the vignette text.

Building the survey now is still worth doing — it's reusable regardless of which way that call goes,
and only the 2 Silent blocks would need editing.
