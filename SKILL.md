---
name: design-buff
description: Review design drafts from business and UX angles using screenshots, docs, or Figma MCP. Prefer layered Figma reads when a Figma URL or selection is available, infer context, produce a designer-facing HTML review report plus machine sidecar in a visible project folder, and guide structural revision issue by issue.
compatibility: Best in runtimes that support MCP and the Figma MCP server. Falls back to screenshot and document review when MCP is unavailable.
metadata:
  version: "0.7"
---

# `design-buff`

Use this skill for product-minded, UX-rigorous design review. The job is to infer context, inspect evidence, judge the design, and guide revision. The job is not to hand out vague praise or taste-only commentary.

## Use This Skill For

- design self-review before formal critique
- product and UX diagnosis rather than visual polish
- reconstructing missing business or user context from the draft
- reading Figma drafts through MCP when a Figma URL or selection is available
- issue-by-issue root cause diagnosis and revision coaching
- agent workflows that need structured design review output

## Do Not Use This Skill For

- pure visual styling critique
- trend-chasing layout or color advice with no product or UX question
- full design system generation from scratch
- replacing formal user research where research evidence is required
- editing the Figma file unless the user explicitly asks for Figma changes

## Operating Model

This skill follows a strict read-review-render model.

- the `design-buff/` directory is instruction-only and should not receive runtime writes
- durable outputs live under `design-buff-reviews/<review-slug>/`
- technical scratch may live under `.design-buff/<review-slug>/`
- chat, `report.html`, and `review-state.json` must come from the same canonical review object

Detailed output, report, and scratch rules live in `references/report-contract.md`.

## Inputs And Evidence Hierarchy

Supported inputs:

- Figma board or frame URL with `node-id` and `fileKey`
- Figma URL that points to a file, frame, or node
- current Figma selection if the runtime supports selection-based MCP reads
- screenshots
- long images
- exported frames
- partial pages
- local design exports referenced by path
- PRD, feature docs, notes, research, and business materials

Prefer evidence in this order when possible:

1. user-confirmed context
2. PRD or product documents
3. Figma structural data from MCP
4. screenshots or design exports
5. explicit model inference

Always distinguish between:

- `confirmed`
- `visible`
- `inferred`
- `unknown`

Use `references/input-standard.md` for detailed Figma intake rules.
Use `scripts/parse_figma_url.py` when a Figma link needs quick normalization.

## Operating Modes

Default report mode is `self-check`.

Switch to `agent-review` only if:

- the user explicitly asks for machine-friendly output
- this skill is clearly inside an agent workflow
- the reviewed target is itself agent-generated design output

Both modes still render `report.html` and `review-state.json`.

## Runtime State Machine

### 1. Normalize Intake

Choose the narrowest lane that preserves judgment quality:

- `figma-board lane`
- `figma-structure lane`
- `draft-first lane`
- `draft + materials lane`

During intake:

- normalize the intake URL and node IDs
- identify or create the `review-slug`
- if a prior review exists, load both `report.html` and `review-state.json`
- use hidden scratch only as disposable technical recovery data

### 2. Collect Evidence

When Figma MCP is available, read in layers:

1. `get_metadata`
2. `get_screenshot`
3. `get_design_context`
4. `get_variable_defs` when token intent matters
5. `use_figma` only for exact text, icon, component, or prototype inspection

Figma discipline:

- do not edit the Figma file unless explicitly asked
- do not start with full-file deep inspection
- use the smallest node that answers the current question
- if the intake root is too large, split it into review units first

Use `scripts/pick_figma_review_units.py` on metadata output when a large board needs screen-like review units.
Use `references/figma-high-precision.md` when the board is large, exact copy or icon semantics matter, or tooling boundaries must be recorded precisely.

If only screenshots or exports are available:

- infer the background from visible evidence
- state confidence and evidence
- ask for more material only if missing context could materially change the judgment

### 3. Reconstruct Background

Before critique, determine what the design is trying to do.

- use `references/review-playbook.md` for background reconstruction, confirmation prompts, and evidence signals
- update the human report and structured sidecar from the same background read

### 4. Critique And Resolve

Review for product and UX rationality, not surface beauty.

- use `references/review-playbook.md` for critique dimensions, mandatory passes, issue anatomy, severity, confidence, stable issue identity, and resolution guidance
- when the user selects an issue, continue into revision guidance rather than stopping at critique
- use `scripts/make_issue_id.py` when you need a deterministic mixed-format stable issue ID

### 5. Synthesize The Canonical Review Object

All durable outputs must come from one canonical review object.

- use `references/review-state-schema.md` for the allowed sidecar structure
- keep the core object lean
- do not treat the human report template as the internal schema

### 6. Render Outputs

Render three outputs from the same canonical review object:

1. concise chat launch summary
2. `report.html`
3. `review-state.json`

- use `references/report-contract.md` for report language, chat order, HTML markers, section content, and hidden scratch rules
- use `scripts/detect_report_language.py` when the language signal is mixed or unclear

### 7. Persist State

Durable writes:

- update `design-buff-reviews/<review-slug>/report.html`
- update `design-buff-reviews/<review-slug>/review-state.json`

Hidden scratch may contain JSON state, run metadata, review-unit picks, read coverage, evidence manifests, and raw tool cache when genuinely useful.

Never write human-facing review prose into hidden scratch unless the user explicitly asks for extra artifacts.

## Reporting Style

### `self-check`

Audience:

- a human designer doing self-review and revision

Style:

- direct
- sharp
- concise
- coach-like
- decision-oriented

### `agent-review`

Audience:

- another agent
- a downstream automated step

Style:

- structured
- evidence-led
- priority-aware
- machine-usable

Both modes must still preserve chat and HTML parity.

## Non-Negotiables

- Do not default to aesthetic commentary unless aesthetics affect clarity, trust, or task success.
- Do not praise vague "clean and modern" work.
- Challenge the problem before endorsing the solution.
- Prefer structural correction over decorative correction.
- Distinguish what is visible from what is inferred.
- Mark uncertain conclusions as hypotheses.
- Treat structured Figma evidence as stronger than screenshot-only inference.
- If the biggest issue is strategic or contextual, say it before discussing page details.
- Cite exact frames, nodes, or visible evidence whenever possible.
- If a tool boundary blocks precision, record the exact tool, node, and missing detail instead of guessing.

## Reference Map

Read these only when the task calls for them:

- `references/input-standard.md`: detailed intake rules
- `references/figma-high-precision.md`: large-board and exactness-sensitive read path
- `references/review-playbook.md`: background reconstruction, critique, issue anatomy, and resolution logic
- `references/report-contract.md`: chat, HTML report, report language, and hidden scratch rules
- `references/review-state-schema.md`: `review-state.json` structure and field boundaries
- `references/report-style-context.md`: visual direction for the human-facing HTML report

Bundled scripts:

- `scripts/parse_figma_url.py`
- `scripts/pick_figma_review_units.py`
- `scripts/make_issue_id.py`
- `scripts/detect_report_language.py`
