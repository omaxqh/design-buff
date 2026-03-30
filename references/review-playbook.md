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
- `continuity review` across journey, interaction, and mental flow
- `scenario stress test` against the most relevant failure or pressure cases
- `micro-detail pass` when wording, icon semantics, or state coverage matters

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
