# Instructions for Holden: Coding the Study 1 Tariff-Messaging Corpus

**From:** Britton Leggett
**What this is:** You're going to be one of two independent human coders on a qualitative
coding task for the Tariff Messaging paper's Study 1 — the other coder is Britton himself. This
document teaches you the method and walks you through exactly what to do. Budget **2–3 hours**
for the actual coding — it's 15 short artifacts, but read them slowly.

---

## 1. The one-paragraph version

Study 1 asks: *when companies raise prices and blame it on tariffs, how do they talk about it?*
We collected 15 real examples of companies explaining tariff-driven price increases (earnings
calls, press statements, price bulletins) and are analyzing the *rhetorical strategies* they use
— do they name tariffs explicitly or stay vague? Do they emphasize restraint ("we're absorbing
most of the cost")? Do they pair the increase with a mitigation story (sourcing changes, supplier
negotiations)? **Your job is to independently code the same 15 artifacts by hand. Britton is
doing his own independent pass at the same time, without seeing your codes and without you
seeing his.** Once you're both done, we compare the two sets and measure how much you agree.
That agreement number (and where you diverge) is itself a piece of the paper's methods section —
it's not a test of you, and there's no "correct" answer key you're being scored against.

---

## 2. The method: thematic analysis, in plain terms

This project uses **thematic analysis (TA)** — a standard qualitative method for finding
patterns of meaning across a set of texts. It comes from Braun & Clarke's foundational work, and
it happens in six phases. One thing worth knowing up front, because it'll look odd if you go
read the original Braun & Clarke papers: they describe two different flavors of TA —

- **"Reflexive" TA** — fully interpretive, one researcher's evolving judgment, explicitly
  *rejects* the idea of measuring agreement between coders as a quality marker.
- **"Coding-reliability" TA** (sometimes called "small-q" TA) — uses a shared coding approach
  across multiple coders and *does* report agreement statistics, closer to traditional content
  analysis.

This project deliberately uses the second variant, because we're about to report a reliability
statistic (Gwet's AC1, similar in spirit to Cohen's Kappa) comparing your codes to Britton's. If
you read Braun & Clarke and get confused about why we're computing agreement stats at all — that's
why. We're not doing "Braun & Clarke reflexive TA"; we're doing the six-phase TA process in its
coding-reliability form. This is also just standard practice for multi-coder qualitative work
generally (Neuendorf, Lombard, and the broader content-analysis tradition) — two independent
coders comparing notes on the same material.

**The six phases:**

1. **Familiarization** — read everything once, all the way through, before coding anything.
2. **Generating initial codes** — label short, meaningful chunks of text with a brief tag
   describing what's happening in that chunk.
3. **Searching for themes** — step back and look for patterns across your codes; group related
   codes into candidate themes.
4. **Reviewing themes** — check candidate themes against the full dataset; do they hold up, or
   need splitting/merging/dropping?
5. **Defining and naming themes** — write a one-line definition of each theme and give it a
   clear name.
6. **Write-up** — report themes with supporting quotes/evidence.

**You are only doing Phases 1 and 2, informally through Phase 3** (initial noticing of patterns
— not a final theme map; that's Britton's call). You are not writing the paper's actual theme
section. You're producing one independent, blind pass of coding that gets compared to Britton's
independent pass.

**A note on where the corpus came from:** the 15 artifacts you're coding were gathered and
fact-verified with AI assistance (finding the source documents, extracting neutral facts,
primary-sourcing quotes against original transcripts/press releases). That's a data-collection
step, not coding — no AI has coded this corpus. The actual thematic coding, the part you and
Britton are doing, is entirely human.

---

## 3. Semantic vs. latent coding — the part that actually matters here

Every code you write will fall into one of two types:

- **Semantic codes** capture what's said on the surface. If a company says "tariffs added $50M
  in costs," a semantic code might be something like `cites-dollar-figure` or
  `explicit-cause-named`.
- **Latent codes** capture what's implied, assumed, or notably *absent* — tone, hedging, who's
  being addressed, what's conspicuously not said. If a company carefully avoids the word
  "tariff" entirely while raising prices, that absence is itself a latent code — something like
  `avoids-naming-cause`.

**Latent codes are the most valuable thing you can contribute.** This is the layer where genuine
interpretive judgment shows up, and where two independent readers are most likely to notice
different things — which is exactly the point of having two coders. Don't rush past the
"Notes/latent reads" field on the worksheet — it's arguably more important than the codes field.

### A worked example (not from the real corpus — just to show the mechanics)

Imagine a fictional airline says, in an earnings call:

> "As you know, we've had to make some adjustments to bag fees this quarter. This is consistent
> with the kind of periodic pricing review we do every year."

- **Semantic codes:** `price-increase-announced`, `framed-as-routine`
- **Latent read:** The word "adjustments" is a euphemism for an increase — softer language than
  a direct statement would use. "As you know" presumes the increase is already expected/accepted,
  which pre-empts pushback. No cause is named at all — contrast this with a statement that
  explicitly blames a cost driver.

That's the level of granularity we want. You don't need special vocabulary or a fixed code list —
short, plain-language labels are exactly right. Braun & Clarke's own guidance: code as much as
feels meaningful, don't force a target number, and don't worry about "getting it right" relative
to some hidden answer key.

---

## 4. What to actually do, step by step

1. Open **`Study1_Validation_Pilot_BLIND_CODING_WORKSHEET_2026-08-27_FULL_CORPUS.md`** (same
   folder as this file). That has the 15 artifacts, each with a short set of neutral facts and a
   source link.

   You may also see a file called `Study1_Validation_Pilot_AI_CODES_SEALED_2026-08-27_
   FULL_CORPUS.md` in the same folder — **ignore it.** It was built for an earlier version of
   this design and isn't part of what you're doing. Don't open it.

2. **Don't compare notes with Britton, or look at anything he's written, until you're both
   completely finished.** Talking through it partway — even casually — turns a blind comparison
   into an anchored one, and we lose the whole point of having two independent coders.

3. For each of the 15 artifacts:
   - Read the neutral facts. Click the source link if you want fuller context (optional, but
     often helpful — the facts summary is deliberately compressed).
   - Fill in **"Your codes"** — as many short labels as feel meaningful. No minimum or maximum.
   - Fill in **"Notes/latent reads"** — anything interpretive: tone, hedging, what's *not* said,
     who the statement seems really aimed at, anything that reads as strategic rather than
     incidental.
   - Move to the next artifact. Don't go back and revise earlier ones to "match" later ones —
     your first read is the data point we want.

4. After all 15 are coded, fill in the **"After coding all 15: your candidate theme(s)"** section
   at the bottom — this is your own Phase 3-ish step. Look across your 15 sets of codes and ask:
   what patterns keep showing up? Do any artifacts feel like they don't fit any pattern? A useful
   check (Naeem et al.'s "4 Rs"): does a candidate theme feel **r**ecognizable (someone else could
   spot it too), **r**esponsive (it actually answers "how do firms talk about tariff pricing?"),
   and not just a repeat of another theme in different words?

5. Save the file (don't overwrite the blank original — save as
   `Study1_Validation_Pilot_BLIND_CODING_WORKSHEET_2026-08-27_FULL_CORPUS_[yourname].md` or
   similar) and tell Britton you're done.

---

## 5. Ground rules

- There is no answer key. Divergence between you and Britton is expected and useful, not a
  mistake on your part.
- Don't force your codes to a particular count or to match any pattern you assume we're looking
  for. Independent means independent.
- If an artifact seems ambiguous or you're torn between two readings, write both — don't pick one
  to look decisive.
- This is about the 15 artifacts as given. Don't go research additional outside context beyond
  what the source link gives you; we want your read of *this* material, not a deeper investigative
  pass.
- Questions about the task itself (not about "what's the right answer") — ask Britton directly
  rather than guessing.

---

## 6. Why this matters for the paper (context, not something you need to act on)

Once you're both done, Britton lines your codes up against his own, computes Gwet's AC1 at both
the code level and the theme level, spot-checks a sample of quotes against their original
sources, and writes up a reviewer-facing Validation Report plus a plain-language brief for
coauthors. Two independent human coders with a reported agreement statistic is standard practice
for this kind of qualitative work — your pass is what makes that possible.
