# Design Buff Portable Instructions

Use this workflow when the user asks for a design review, self-check, flow diagnosis, or UX critique from Figma, screenshots, exported frames, PRDs, or product notes.

## What This Is For

- product- and UX-led design review, not taste-only commentary
- reconstructing missing context before judging the draft
- diagnosing structural, cognitive, trust, and continuity problems
- producing a human-readable review plus machine-friendly structured state when file output is available

## Do Not Use It For

- pure visual styling commentary with no product or UX question
- trend-chasing advice with no task or business context
- replacing formal user research when research evidence is required

## Core Working Model

- review the design as a real user path, not as isolated pages
- reconstruct the scenario, target user, business goal, and chain position before critique
- judge the decisions the design forces the user to make
- prefer structural correction over decorative correction
- keep machine state and human-facing output aligned if both are produced

## Evidence Order

Prefer evidence in this order whenever possible:

1. confirmed user context
2. product documents or business materials
3. Figma structure and screenshots from the runtime's design tooling or MCP integration
4. screenshots, exports, or long images
5. explicit inference

Always distinguish:

- `confirmed`
- `visible`
- `inferred`
- `unknown`

Do not present guesses as conclusions.

## Review Workflow

### 1. Normalize Intake

- identify the design target and the narrowest review lane that preserves judgment quality
- if a prior review exists, load it before starting a fresh pass
- prefer the smallest review unit that answers the current question

### Report Mode

- default to `self-check`
- switch to `agent-review` only when the user explicitly wants machine-first handoff or the primary audience is another agent / automation step
- being inside an agent runtime, IDE, or CLI is not enough to justify `agent-review`
- reviewing an AI-generated draft is also not enough by itself; if human designers are still the main readers, stay in `self-check`

### 2. Collect Evidence

- if the runtime supports Figma or MCP, read structure first and screenshots second
- do not start with full-board deep inspection when a smaller node can answer the question
- if only screenshots or exports are available, reconstruct context from visible evidence and mark confidence clearly

### 3. Reconstruct Background

Before critique, determine:

- what the design is trying to help the user do
- who the user is and what they likely already know
- what business target this flow is serving
- where this screen or step sits in the larger journey
- which details are known versus inferred

### 4. Critique

Review from business and UX rationality, not surface beauty.

At minimum, inspect:

- scenario fit
- cognition and operation cost
- user expectation, trust, and mental model
- value carry-through
- baseline experience quality

Mandatory passes:

- cognitive and copy load check
- three-flow continuity review
- scenario stress test on the most important pressure or failure path

### 5. Synthesize One Canonical Review

- keep one canonical review object behind every output
- do not let the human HTML report become the internal schema
- keep issue IDs stable enough for reruns and comparison
- the HTML report and structured sidecar must come from the same review object, not two separately improvised summaries

### 6. Render Outputs

If file output is allowed, write:

- `design-buff-reviews/<review-slug>/report.html`
- `design-buff-reviews/<review-slug>/review-state.json`

Optional technical scratch can live under:

- `.design-buff/<review-slug>/`

If file output is not available, keep the same review logic in chat and state the persistence limit explicitly.

Rendering guardrails:

- keep the fixed report section ids: `review-overview`, `executive-summary`, `highest-priority-issue`, `background-and-evidence`, `full-review`, `issue-list`, `three-flow-consistency`, `resolution-tracks`, `open-questions`, `next-actions`
- if the report language is Chinese, keep section titles, labels, chips, and helper text in Chinese too; do not leave English scaffolding such as `Executive Summary`, `Issue List`, `Resolution Tracks`, `Project`, or `Review Slug`
- show stable issue identifiers in the human report as well as display numbers
- if the full repository or validator script is available, run the contract validator after writing and repair until it passes

## Three-Flow Continuity Review

This is the signature check in Design Buff.

For at least one key task path, explicitly inspect whether these three flows stay aligned:

- `旅程流`: whether the macro path still holds from entry to outcome
- `操作流`: whether each concrete action and response stays clear and continuous
- `心智流`: whether user certainty and trust move forward instead of collapsing mid-path

This check exists to catch a common failure mode: pages may look locally correct one by one, while the full task chain is still broken.

Focus on:

- whether the design only looks right at page level but fails as one connected path
- whether the large journey, concrete actions, and user confidence support each other
- exactly where the break happens and what kind of break it is

## Human Report Rules

- when the user writes in Chinese, the human report should read like natural Chinese design review, not translated schema output
- do not expose rigid labels such as `what i see`, `likely consequence`, or `discussion prompt` unless the user explicitly asks for audit framing
- compress repeated micro-fields into clear causal paragraphs
- keep the machine identity in structured fields, not in awkward human titles
- the human-facing artifact should be `report.html`, not a long raw chat dump

## Non-Negotiables

- do not default to aesthetic commentary unless aesthetics affect clarity, trust, or task success
- do not hand out vague praise
- challenge the problem before endorsing the solution
- distinguish what is visible from what is inferred
- mark uncertain conclusions as hypotheses
- if the biggest issue is strategic or contextual, say it before page-level details
- if tooling limits block precision, record the limit instead of guessing

## Canonical Source Files

If the full Design Buff repository is available, these files remain the source of truth:

- `SKILL.md`
- `references/input-standard.md`
- `references/figma-high-precision.md`
- `references/review-playbook.md`
- `references/report-contract.md`
- `references/review-state-schema.md`
- `references/report-style-context.md`
- `templates/report-shell.html`
