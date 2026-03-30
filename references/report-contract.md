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
- `#read-coverage`
- `#full-review`
- `#issue-list`
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
- `why_this_is_first`
- `severity`
- `confidence`
- `evidence_basis`
- `figma_nodes`
- `screenshot_refs`
- `precision_limit`
- `what_i_see`
- `why_it_is_a_problem`
- `recommended_direction`
- `correction_paths_summary`
- `adopted_or_recommended_path`

### Background and Evidence

Render these groups:

- Figma intake summary
- selected review units
- high-precision units
- structural-only units
- deferred units
- tooling boundaries
- initial hypothesis
- visible evidence
- user confirmation
- supporting materials
- confirmed background
- review boundaries

### Read Coverage

Render:

- review units fully read
- review units partially read
- screens validated by screenshot
- open tooling gaps

### Full Review

Render:

- top three issues in ranked order
- issue list with designer-facing prose for each issue
- category view
- structural revision summary
- continuity review
- scenario stress test

Each issue card should include:

- `display_number`
- `stable_id`
- `title`
- `category`
- `severity`
- `confidence`
- `evidence_basis`
- `figma_nodes`
- `screenshot_refs`
- `precision_limit`
- `what_i_see`
- `why_it_is_a_problem`
- `what_misunderstanding_it_reveals`
- `who_it_hurts`
- `likely_consequence`
- `recommended_direction`
- `discussion_prompts`

### Resolution Tracks

For each selected issue, render:

- problem restatement
- root cause hypothesis
- correction path A
- correction path B
- correction path C
- recommended direction
- revised structural proposal
- what to validate next

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
