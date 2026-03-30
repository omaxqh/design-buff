# Figma High-Precision Read

Use this playbook when a board or frame URL is available and the review requires exact text, icon semantics, or state-level judgment.

## Goal

Turn one board or frame URL into a set of reviewable screen units that are small enough to read precisely and broad enough to support product judgment.

## Intake flow

1. Normalize the intake URL.
2. Call `get_metadata` on the intake root.
3. Call `get_screenshot` on the intake root.
4. Try `get_design_context` on the intake root.
5. If the node is too large or the response is sparse metadata, split into review units.

## Review-unit heuristics

Prefer child nodes that are:

- `frame` nodes with screen-like dimensions
- one state, one step, or one branch of the journey
- rich in visible copy, CTA copy, form fields, or state messaging

Usually exclude from primary units:

- decorative vectors
- connector arrows
- slices
- giant collage wrappers
- standalone labels that only title another screen

## Recursive split rule

If a unit still returns a sparse or oversized contextual read:

- go one level deeper
- choose the smallest child frames that still preserve one coherent task or state
- stop only when the unit produces a useful contextual read or when no meaningful UI grouping remains

## Evidence ladder for micro-detail work

- `high`: exact text, named instance, named component, or direct contextual read plus screenshot match
- `medium`: screenshot-visible and structurally implied, but not backed by exact node naming
- `low`: inferred from dense visuals or blocked by a tool boundary

## Tool mismatch rule

If `get_metadata` and `get_design_context` can read a node but `use_figma` cannot locate it:

- treat `get_metadata + get_design_context + get_screenshot` as the primary evidence set
- use `use_figma` only on nodes it can actually resolve
- record the mismatch in the review instead of guessing

## Code Connect blocker

If `get_design_context` is interrupted by a Code Connect prompt:

- follow the tool instruction exactly
- do not treat that as proof the design cannot be read
- continue the main read path after the prompt is resolved
