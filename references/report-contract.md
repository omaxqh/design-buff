# Report Contract

Use this reference when rendering chat output, `report.html`, and hidden scratch for `design-buff`.

## Canonical Output Model

All outputs must come from the same canonical review object.

Durable outputs live under:

```text
design-buff-reviews/<review-slug>/
```

Each review root contains:

- `report.html`: the only formal human-facing review report
- `review-state.json`: the structured durable sidecar

Technical scratch may live under:

```text
.design-buff/<review-slug>/
```

Rules:

- `report.html` is the only human-facing source of truth
- `review-state.json` is not a second report
- chat may summarize or reorder, but may not contradict the report
- if the same draft or feature is reviewed again, update the same `review-slug` in place

## Chat Launch Summary

The chat window is a launch surface, not the long-form report.

Recommended order:

1. one-sentence overall diagnosis
2. top blockers or top priorities
3. the path to `report.html`
4. only the most urgent open questions, if any

Keep it concise. Do not paste the full report into chat.

## Report Language Rules

Choose the report language in this order:

1. explicit user override
2. dominant language across the current conversation, PRD, and supporting materials
3. fallback to `zh-CN`

Requirements:

- write the chosen language into `meta.report_language`
- write how it was chosen into `meta.language_source`
- set `<html lang="...">` in `report.html`
- keep labels, headings, and narrative in the selected report language unless the user asks for bilingual output
- preserve product names, node IDs, and quoted strings in their original form when translation would reduce precision

Use `scripts/detect_report_language.py` when the signal is mixed or when multiple materials disagree.

## Required HTML Markers

`report.html` must include:

- `<html lang="...">`
- `<meta name="design-buff-template" content="human-report-html-v1">`
- `<body data-design-buff-report="v1">`

These markers let validators confirm that the human-facing artifact follows the package contract.

## Required Sections

The final page should be self-contained and include these semantic sections:

- `#review-overview`
- `#executive-summary`
- `#changes-since-last-review` when this is not the first run
- `#highest-priority-issue`
- `#background-and-evidence`
- `#full-review`
- `#issue-list`
- `#three-flow-consistency`
- `#resolution-tracks`
- `#open-questions`
- `#next-actions`

Remove empty sections only when they are truly unnecessary.
If a section is still unknown, mark it as `unknown` rather than faking certainty.

## Section Content Map

### Review Overview

Render:

- `project_name`
- `review_slug`
- `report_mode`
- `review_date`
- `reviewer`
- `report_language`
- `source_artifacts`
- `figma_intake_url`
- `figma_file_key`
- `figma_intake_node`
- `figma_intake_node_type`
- `ingest_status`

### Executive Summary

Render:

- one-sentence overall diagnosis
- current verdict
- immediate revision priorities
- issues that block progress
- issues that need PM, research, or business clarification

### Changes Since Last Review

Use this section only when the review is continuing an existing `review-slug`.
Keep it short and place it immediately after `Executive Summary`.

Render:

- new issues
- resolved issues
- materially changed issues
- issues whose severity increased, when relevant

### Highest-Priority Issue

Render:

- `display_number`
- `stable_id`
- `title`
- `severity`
- `confidence`
- one plain-language diagnosis paragraph
- one paragraph explaining why this issue comes first
- one paragraph explaining correction paths and recommended direction
- one short `need to confirm` paragraph when recommendation quality depends on PM, business, or technical constraints

### Background and Evidence

Render as concise prose, not process logs.

Include only the parts a human reader needs in order to trust the diagnosis:

- what material was actually reviewed
- the most relevant visible evidence
- the reconstructed context and business goal
- the real review boundary or tool limit when it changes the recommendation

Do not expose unit-picking mechanics, coverage bookkeeping, or tool sequencing unless the user explicitly asks for audit-style output.

### Full Review

Render:

- top three issues in ranked order
- issue list with designer-facing prose for each issue
- summary view for issue distribution, correction path grouping, and key risk
- scenario stress test

Each issue card should include:

- `display_number`
- `stable_id`
- `title`
- `category`
- `severity`
- `confidence`
- one diagnosis paragraph that combines what is visible, why it matters, and what consequence it creates
- one correction paragraph that explains what should change and why
- one short `need to confirm` paragraph only when unresolved constraints materially affect the recommendation

### Three-Flow Consistency

Render this as a standalone major section immediately after `Full Review`.

Purpose:

- make continuity review visible instead of leaving it implied inside issue prose
- judge whether the design works as one task chain rather than as a pile of locally correct pages

Render it as one vertical timeline aligned to the main journey, not as three large flow essays.

Render:

- a left-side vertical timeline with 4-8 journey nodes
- one right-side card per node
- optional stage summary when it helps the reader place the node in the journey
- up to three issue blocks inside the card: `journey flow`, `operation flow`, `mental flow`
- one short synthesis paragraph on whether the three flows support each other or fight each other

Each node should:

- use a concrete stage title tied to the real journey, not an abstract checkpoint label
- show only the flow blocks that actually have a meaningful problem
- avoid filler such as `normal`, `pass`, or neutral prose when no issue exists

The renderer may build a transient `timeline_nodes[]` view model for HTML output. It may contain stage titles, optional stage summaries, and optional `journey_issue`, `operation_issue`, and `mental_issue` blocks. This helper model is render-only and must not be written back into `review-state.json`.

Each issue block should explain only:

- a short human-readable title such as `旅程流断裂` or `操作流不清`
- the problem
- the fix

### Resolution Tracks

Do not render this as a second issue list.

Render it as a compact summary module grouped with other full-review synthesis panels.

Use it to answer:

- which issues should be fixed together as one structural batch
- what the recommended path is at a structural level
- what the user loses if the team keeps the current design shape

Keep it shorter than the issue cards and the three-flow section.

### Open Questions

Render the open questions in clear ranked order.

### Next Actions

Render:

- what the designer can revise immediately
- what should be confirmed with PM or business
- what should be re-read from Figma before implementation

## Visual System

This HTML report is the scoped design subsystem embedded inside `design-buff`.

Design intent:

- editorial hierarchy over dashboard chrome
- deliberate typography over default web stacks
- varied spacing rhythm over repetitive card grids
- evidence-led structure over decorative noise
- strong visual identity without sacrificing readability

Required components:

- `hero masthead`: project, verdict, language, intake status, and top metadata
- `diagnosis rail`: one-sentence diagnosis plus immediate priorities
- `issue spotlight`: the highest-priority issue rendered as a dominant feature block
- `issue cards`: repeatable structured blocks for each issue
- `evidence chips`: compact tokens for nodes, screenshots, confidence, and tooling gaps
- `action columns`: open questions and next actions rendered side by side on wide screens

Visual constraints:

- use a warm light palette with tinted neutrals
- combine a distinctive display face with a practical body face and a mono metadata accent
- create visual rhythm with varied spacing and strong dividers
- let the highest-priority issue dominate the first viewport
- use motion only for subtle reveal polish and respect reduced-motion preferences
- do not make it look like a metrics dashboard
- do not rely on generic gradients, glass cards, or glows
- do not stack identical cards for every section
- do not bury the diagnosis below oversized decorative hero content

## Accessibility

- keep contrast strong enough for long-form reading
- preserve readable line lengths
- use semantic headings and list structure
- support keyboard navigation without hidden controls
- include responsive behavior that keeps the page readable on laptop and mobile

## Human Writing Rules

The human report must read like an editorial design review, not like exported form fields.

Required:

- write issue titles and paragraphs in plain language first
- prefer one or two strong paragraphs over six labeled micro-fields
- keep machine identity in `stable_id`, not in unnatural title wording
- use Chinese that sounds native to a product or design team when `report_language` is `zh-CN`
- translate headings, subheadings, and UI labels into the selected report language

Avoid:

- schema-like labels such as `what i see`, `likely consequence`, `discussion prompt` in the final HTML unless the user explicitly asks for audit framing
- direct translation of English analytical nouns when a natural Chinese sentence would be clearer
- Chinese PM or process jargon such as `结构包` or `整改包` in the human-facing report
- compressed phrases that hide the actor, action, or consequence

Good title pattern in Chinese:

- `谁在什么地方不知道什么，却被要求先做什么`
- `页面让用户做关键决定，但没有告诉他会发生什么`
- `成功页宣布结果了，但没有把下一步价值接住`

If a line sounds like it came from a spreadsheet, schema, or machine translation, rewrite it before persisting.

## Hidden Scratch Rules

Hidden scratch lives under `.design-buff/<review-slug>/`.

Allowed:

- JSON state
- raw tool cache
- run metadata

Not allowed:

- Markdown review documents
- human-facing issue prose
- executive summary prose
- recommendation prose

If a hidden file could be mistaken for the formal review, it does not belong there.

## Template Basis

Use `templates/report-shell.html` as the structural and stylistic basis.
Use `references/report-style-context.md` as the embedded design context for the report artifact.
The final result must still look like it came from the same design system.
