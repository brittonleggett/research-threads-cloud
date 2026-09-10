# 2026-09-10 — LPSC U-37882 order PDF: finally read, plus a real tooling fix and one important correction

## Tooling note first (relevant beyond this one file)

Two prior forks today couldn't extract this PDF's text: one hit broken `poppler-utils`/`pypdf`
in the sandboxed environment, the next hit a "media removed: request limit" wall from an
unrelated prior task in that same session. This session installed `poppler` fresh via `winget`
(`oschwartz10612.Poppler`, confirmed working: `pdftoppm`/`pdfinfo` etc. now present on this
machine at `%LOCALAPPDATA%\Microsoft\WinGet\Packages\oschwartz10612.Poppler_...\poppler-25.07.0\Library\bin`),
then rendered pages to PNG directly with `pdftoppm.exe` (bypassing Claude Code's own Read-tool
PDF path, which still fails because its internal `pdftoppm` lookup doesn't see a PATH change
made after the harness process started) and read the PNGs with the Read tool's normal image
support. **This works and is repeatable**: `pdftoppm -png -r 150 -f <start> -l <end> input.pdf
out_prefix`, then `Read` each `out_prefix-0NN.png`. Worth knowing for any future court/agency
PDF this project needs to read directly, on this machine specifically (not the cloud nightly-
routine sandbox, which has its own separate, still-broken tooling).

## What the PDF actually is — an important correction to how this docket's been characterized

`pdfinfo` shows this is a real **103-page** document, not the "1 page" a naive `file` check
reported earlier today. Read the first 5 pages directly (not OCR'd via any lossy process —
direct page-image reads of the actual filed document).

**Pages 1-4** are the Chief ALJ's (Melanie Verzwyvelt) July 31, 2026 *"Referral of
Interlocutory Ruling to Commissioners for Review"* — a cover memo, not the Commission's own
order. **Page 5 onward (86 pages) are the attached exhibits** — starting with the ALJ's own
underlying *"Ruling on Motion for Subpoena for the Production of Documents,"* i.e., the
actual merits ruling being referred up.

**This refines, not just confirms, what this docket is about.** It is not simply "a PSC
secrecy vote" in the abstract — it's a **discovery/subpoena fight**: the Alliance for
Affordable Energy and Union of Concerned Scientists (intervenors, "NPOs") subpoenaed Meta
Platforms (a non-party) for documents. The ALJ's Subpoena Ruling (July 10, 2026) **granted**
two categories and **denied** three:

- **Granted**: (1) documents substantiating the Richland Data Center's claimed investment
  and permanent job creation; (2) documents substantiating the data center's electricity
  load.
- **Denied**: (3) load-factor/variability data; (4) Meta-ELL communications about the
  "Sustainability Agreement"; (5) information on Meta's assets sufficient to cover its
  guaranty obligations to ELL, plus Meta's other utility guaranties.

Meta then fought even the two *granted* categories: filed a Motion for Stay (granted,
still in effect as of this referral), a Motion for Immediate [Commission] Review, and a
Motion to Quash the subpoena entirely. The ALJ declined to reconsider her own ruling and
referred the quash question up to the full Commission — which is presumably the origin of
the Commissioners' vote (Coussan/Francis/Skrmetta reversing, Lewis dissenting) a prior
fork already confirmed from a separate source.

**Important limitation — the vote's own reasoning is NOT in this file.** This 103-page PDF
is the ALJ's referral package (cover memo + the underlying merits filings/exhibits), dated
July 31, 2026. It predates the Commission's actual vote and does not contain the
Commissioners' own stated reasoning for reversing, or Lewis's dissent reasoning — those
would be in the Commission's own subsequent order or open-meeting minutes/transcript from
whatever business meeting the vote happened at, which is a **separate document not yet
located**. Do not attribute the majority/dissent reasoning to this file; it isn't here.

## Relevance to the corpus's framing

This is a stronger secrecy/transparency angle for the manuscript than "the PSC voted to
reverse an ALJ order" alone conveys: the actual dispute is public-interest intervenors
trying to verify Meta's own public job-creation and investment claims (the "10,000 jobs"-
type claim-specificity theme this project already tracks elsewhere, e.g. SpaceX) against
Meta's internal documents, and Meta successfully blocking even the ALJ's already-narrowed,
partial disclosure via a stay pending Commission review — with the Commission (per the
already-confirmed vote) apparently upholding Meta's position over the intervenors' and the
ALJ's own ruling. Worth folding this specific framing (claim-verification-via-subpoena
blocked by the beneficiary company) into the corpus write-up rather than the more generic
"secrecy vote" language currently used, once Britton does the actual Phase 3 coding pass —
not changing the theme/coding myself, just flagging the sharper framing available.

## What's still open

- Locate the actual Commission order/meeting record with the majority's stated reasoning
  and Lewis's dissent — separate document, not this PDF.
- Pages 6-90 of this PDF (the remaining exhibits: NPOs' opposition brief, Staff's
  memorandum, Meta's reply) weren't read this pass — time-boxed to the referral cover memo
  and the ALJ's own ruling (pages 1-5), which was enough to correct the docket's framing.
  A future pass could pull specific quotes from the NPOs' or Meta's own briefs if the
  manuscript needs direct argument language.

No Phase 3/theme decisions made — this is primary-source content extraction and a
factual correction to the corpus's existing characterization of the docket, per Britton's
standing rule that Phase 3 stays his.
