# Review Playbook

Use this reference when reconstructing background, judging the design, writing issues, or turning diagnosis into correction paths.

## Goal

Figure out what the design is trying to do before judging how well it does it, then push the critique toward structural correction rather than decorative advice.

## Background Reconstruction

Infer and then validate:

- page or flow type
- product type
- likely industry
- target user
- core scenario
- business goal
- workflow or funnel position
- assumptions
- unknowns

## Evidence Sources

Prefer stronger evidence first:

1. user-confirmed context
2. PRD, product docs, or research
3. Figma structural data
4. screenshots or exports
5. model inference

Useful signals:

- page titles and visible copy
- CTA wording
- field labels and table columns
- navigation structure
- trust or risk cues
- status labels
- component hierarchy
- prototype links
- variable naming and token usage

When the evidence is screenshot-only or partial:

- lower confidence instead of faking precision
- record the exact boundary
- keep the critique focused on what is actually visible

## Confirmation Pass

After the first reconstruction pass, confirm or correct:

- who this is for
- what task the user is trying to complete
- what business outcome the design is meant to drive
- what constraints or domain rules are not visible in the draft

## Critique Dimensions

Review the draft across these dimensions:

1. `problem and value`
2. `users and insight`
3. `scenario and fit`
4. `user mental models and habits`
5. `cognitive and operational cost`
6. `industry baseline and alternatives`
7. `foundational experience checks`

## Mandatory Passes

Always run these passes on the most important path:

- `cognitive and copy load check`
- `three-flow continuity review` across journey flow, operation flow, and mental flow
- `scenario stress test` against the most relevant failure or pressure cases
- `micro-detail pass` when wording, icon semantics, or state coverage matters

### Three-Flow Continuity Review

For at least one key task path, explicitly inspect whether these three flows stay aligned:

- `journey flow`: whether the macro task path still holds from entry to outcome
- `operation flow`: whether each concrete action and system response stays clear and continuous
- `mental flow`: whether user understanding, certainty, and trust keep moving forward instead of collapsing mid-path

This pass exists to catch continuity failures that do not show up when pages are judged one by one.

Check:

- whether the design is locally correct page by page but broken as one complete task chain
- whether the macro path holds, the concrete actions stay smooth, and the user feels more certain rather than less certain
- whether the three flows support each other or work against each other
- exactly where the break happens and what kind of break it is

For complex flows, review 2-3 key paths. Do not map every page exhaustively unless the user asks for that level of audit.

In the human HTML report, prefer one stage-aligned vertical timeline over three long abstract flow cards. Each node should write only the real issue blocks that matter, and each block should say `problem + fix` in plain language.

## Human Issue Anatomy

Each issue should be strong enough to support designer-facing review and machine-side tracking.

Keep both:

- a `stable_id` for tracking and diff
- a display label such as `ISSUE-001` for human reading

Each issue should at minimum cover:

- `title`
- `category`
- `severity`
- `confidence`
- `evidence_ids` or equivalent evidence basis
- `what_i_see`
- `why_it_is_a_problem`
- `what_misunderstanding_it_reveals`
- `who_it_hurts`
- `likely_consequence`
- `recommended_direction`
- `discussion_prompts`

## Human Writing Rules

The machine object may stay structured. The HTML report must not read like the schema.

### Title Rules

Issue titles are for human reading first and tracking second.

- write the title so a designer can understand it on first read
- prefer concrete subject + concrete problem + visible consequence
- in Chinese, prefer natural subject-verb-object phrasing over compressed abstract nouns
- if a title needs explanation before it becomes understandable, rewrite it
- keep `stable_id` responsible for machine precision; do not force the title to do machine work

Avoid titles like:

- `首步路径选择依赖用户自诊断账号状态`
- `分流策略与用户心智存在错位`
- `认知负担过重`

Prefer titles like:

- `用户可能不知道自己是否注册过万豪，却必须先选开通还是绑定`
- `页面把业务分流直接丢给用户判断，选错后要到失败页才发现`
- `协议页把必选授权和营销偏好混在一起，用户很难一眼分清`

### Paragraph Rules

For the human report:

- do not expose `what_i_see`, `who_it_hurts`, `likely_consequence`, `discussion_prompts` as rigid field labels by default
- combine them into one causal paragraph that explains what is happening, why it matters, and who is affected
- follow with one paragraph that explains the correction direction in plain language
- merge discussion prompts into a short `需要确认` paragraph when they materially affect the recommendation
- keep evidence visible, but do not let node IDs and tool steps dominate the reading flow

### Chinese Writing Rules

When the report language is `zh-CN`:

- write like a strong Chinese-speaking design lead, not like translated English analysis
- prefer short complete sentences over stacked modifier phrases
- prefer user-known facts over internal product taxonomy
- explain abstract UX terms through visible behavior
- use terminology only when it helps, not as a substitute for explanation
- do not use PM jargon such as `结构包` or `整改包` in the human-facing report

Examples:

- instead of `用户自诊断账号状态`, write `用户要先自己判断自己到底算未注册还是已注册`
- instead of `路径分流`, write `先选开通还是绑定`
- instead of `认知负担`, write `用户得自己多想一步，而且很容易想错`

## Severity Guidance

- `critical`: blocks task success, creates serious trust risk, or reveals a strategic misread
- `high`: causes likely failure, confusion, abandonment, or expensive rework
- `medium`: weakens understanding, efficiency, or confidence but does not fully block the task
- `low`: noticeable but not central to the outcome

## Confidence Guidance

- `high`: exact copy or node evidence plus screenshot confirmation
- `medium`: visible and structurally implied, but not backed by exact node-level evidence
- `low`: inferred from partial visuals, sparse reads, or a tooling boundary

## Stable Issue Identity

- internal logic must use `stable_id`, not display labels
- stable IDs should be mixed-format: readable semantic fragment plus stable suffix
- display labels may reorder between runs
- stable IDs must not change merely because display order changed
- continuing issues, resolved issues, and materially changed issues should all be tracked through `stable_id`

## Resolution Sequence

For the selected issue:

1. restate the true problem
2. identify the likely root cause
3. propose 2-3 correction paths
4. explain tradeoffs
5. recommend one direction
6. define what should be validated next

## Root Cause Prompts

Ask which layer is actually broken:

- wrong problem framing
- wrong user assumption
- wrong scenario assumption
- wrong information hierarchy
- wrong sequencing
- wrong interaction contract
- missing state or recovery path
- copy or terminology drift

## Review Posture

- default to product and UX rationality, not style commentary
- challenge the problem before endorsing the solution
- prefer structural correction over decorative correction
- distinguish what is visible from what is inferred
- if the biggest issue is strategic, say it before discussing page details
