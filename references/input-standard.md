# Input Standard

This file governs intake precision and escalation only. Report, HTML, and sidecar output rules live elsewhere.

## Preferred Figma input

For Figma work, the preferred intake is a board or frame URL that already contains `fileKey` and `node-id`.

Examples of acceptable inputs:

- a board URL that points to one journey map or one review board
- a frame URL that points to one screen, modal, or state
- a frame URL plus PRD or supporting notes

The designer does not need to provide one URL per screen up front. A board or frame URL is enough for intake.

## Avoid when possible

- file homepage URLs with no `node-id`
- a whole page or whole file when the intended review scope is only one board
- screenshots that replace a perfectly good Figma board URL

If the user provides only a broad file URL, first locate the intended board or frame before starting critique.

## Precision expectation

`design-buff` should:

- use the intake board or frame as the root
- split large boards into screen-level review units automatically
- read each review unit with `get_design_context` and validate it with `get_screenshot`
- only claim high precision after that unit has been fully read

`design-buff` should not:

- pretend a giant board screenshot is equivalent to a precise screen read
- silently downgrade to vague critique when the board is too large
- ask the designer for a dozen separate URLs before trying automatic splitting

## Escalation and fallback

If Figma MCP is unavailable or a repeated tool boundary blocks precision:

- continue with the best visible evidence available
- mark the blocked details explicitly
- lower confidence for micro-detail findings
- ask for narrower support only after the automatic split path is exhausted
