# CCS Paper — Louisiana Carbon Capture & Storage Research

Private research repo for a study on Louisiana carbon capture and storage (CCS)
governance, discourse, and consumer/marketing framing. Britton R. Leggett, McNeese
State University.

## Contents

- **`Corpus_1/`** — 18 Louisiana CCS legislative/regulatory documents (bills, digests,
  fiscal notes, agency orders, a Federal Register notice, a public comment, and a
  Tunica Tribe document), plus the MAXQDA project file (`Corpus_1_MAX.mqda`).
- **`Analysis/`** — Python pipeline that extracts text from the corpus and runs word
  frequency, VADER sentiment, and signaling-theory-relevant keyword-frequency analysis.
  See `Government_Document_Analysis_Summary.docx` for the readable writeup. Caveat:
  VADER underperforms on this formal legal register — see the summary doc for why.
- **`CCS_Lit_Review_Foundation.docx`** — a 51-source literature review targeting
  *Energy Research & Social Science*, built around procedural justice / energy justice
  / social license theory and a governance-frame vignette experiment design. This is a
  separate methodological track from the Study 1 work below — see notes.

## Study tracks (don't conflate these)

1. **Government document analysis** (this repo's `Analysis/` folder) — descriptive,
   institutional-signal context, not consumer data.
2. **ERSS-track lit review** (`CCS_Lit_Review_Foundation.docx`) — a governance-frame
   survey experiment design, different theory, different target journal.
3. **JCM Study 1 (planned)** — AI-assisted netnography of public/consumer social media
   discourse about CCS, informed by signaling theory and greenwashing/green-skepticism
   constructs, feeding a Study 2 PLS-SEM survey. Shared methodology (also used by a
   companion tariff-messaging paper) documented at
   `Desktop\Claude global\Claude Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md`.

## Status (as of 2026-07-08)

Elementary phase — lit review and government-document analysis done; Study 1 data
platform not yet chosen; Study 2 constructs not yet finalized.
