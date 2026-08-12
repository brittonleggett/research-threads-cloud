# Zotero + Claude research workflow (learned from YouTube, 2026-08-11)

Source: real transcripts pulled from 4 YouTube videos (not just titles) —
- "How I Use Claude AI Inside Zotero to Review 300+ Papers" (youtube.com/watch?v=LbBxQKgQlKY)
- "How to Connect Claude to Zotero Using MCP" (youtube.com/watch?v=RI1_b-yDTNc)
- "How to Organise Your Zotero Library" (youtube.com/watch?v=j0RJmWQIPGI)
- "Advanced Zotero + Claude AI Workflows for PhD Research" (youtube.com/watch?v=qYeZTZihXLM)

## What I already have vs. what these videos assume

The videos set up a *basic* MCP connection that can only read Zotero **metadata**
(title/author/abstract) and fetch open-access PDFs from the web — it can't read
your local PDF files. The Zotero MCP tools already available in this Claude Code
session go further: `zotero_get_item_fulltext`, `zotero_read_pdf_pages`,
`zotero_create_annotation`, `zotero_synthesize_annotations` — meaning I can
already read full PDF text and write annotations back into Zotero, which is
more than the setup these videos walk through. So the setup step is done; what's
below is the *prompting workflow* on top of it, which is the actually useful part.

**Current gap (checked live 2026-08-11): the Zotero library this MCP connection
points at has zero collections and zero items.** Either it's pointed at an empty
library, or your papers live somewhere this key doesn't see. Worth checking before
relying on any of this — none of it works until there's something in the library.

## The core skill: a per-paper structured-annotation prompt

Both videos agree the payoff comes from **one reusable prompt tailored to your
specific project's themes**, run against one paper at a time, with the output
saved back as a Zotero note. Generic "summarize this" prompts are much weaker.

Template (fill in the bracketed parts per project):

```
You are acting as a PhD-level literature reviewer specializing in [YOUR FIELD].
I am working on a paper about [ONE-LINE PROJECT DESCRIPTION].

My paper has these themes/constructs:
1. [THEME 1]
2. [THEME 2]
3. [THEME 3]
(add more as needed)

For the attached/referenced paper, give me:
- Bibliographic details
- Research overview (1-2 sentences)
- Methodology
- Key findings
- Surprising or contradictory findings
- Contribution and implications
- Domain-specific relevance: for EACH of my themes above, rate relevance
  (low/medium/high) and justify why, with specific connections to my argument
- Key quotes with page numbers I could cite
- One-paragraph summary assessment: is this essential reading for my paper,
  and why (or why not)?
```

Worked example, filled in for the **Larry Paper** (monetary incentives / goal
attainment / loyalty / dishonesty):

```
You are acting as a PhD-level literature reviewer specializing in marketing
and consumer behavior. I am working on a paper about how monetary incentive
structures affect goal attainment, brand loyalty, and dishonest behavior.

My paper has these themes/constructs:
1. Monetary incentives (design, magnitude, framing)
2. Goal attainment / goal gradient effects
3. Loyalty program engagement
4. Dishonesty / cheating behavior as a side effect of incentive structures

For the attached/referenced paper, give me: [...same list as above...]
```

## Three library-wide workflows (once the library has items)

1. **Library-wide query** — ask across the whole collection, not one paper:
   *"Find papers in my [collection] that discuss [construct]."*
   Works much better when papers are organized into collections/tags first.

2. **Cross-paper synthesis** — compare specific papers directly:
   *"Compare the findings of [Author1 Year] with [Author2 Year] on [topic].
   Do they agree, contradict, or address different aspects?"*

3. **Gap-finding** (the highest-value one for shaping a paper's contribution):
   *"Based on the papers in my [collection], what research questions remain
   unanswered about [topic]?"*
   One creator credited this prompt with pointing them toward their actual
   dissertation angle.

Practical tips from the videos, worth following:
- Organize Zotero into **collections per project/paper** (not one flat library) —
  the AI's answers get noticeably better with a scoped collection to search.
- Use **tags** for cross-cutting flags (e.g. "no-DOI", "core-cite", "needs-read")
  rather than trying to fold everything into collections.
- Be specific in prompts — "papers using difference-in-differences with a
  European sample" beats "papers about X."
- Always verify page-level citations before using them — the model is usually
  right but check before you cite.
- Don't stop at the first answer — follow up ("what about papers that disagree?").
  Treat it as a conversation, not a one-shot query.

## Meta-note: how I pulled this content

Standard transcript sites (youtubetotranscript.com, tactiq.io, youtubetranscript.com)
block automated fetches. What worked: `pip install yt-dlp` then
`yt-dlp --skip-download --write-auto-sub --sub-lang en --sub-format vtt <url>`,
then strip the VTT timing/markup down to plain text. This is a repeatable path
for pulling real transcript content from future YouTube research-skill videos,
rather than just going off titles/descriptions.
