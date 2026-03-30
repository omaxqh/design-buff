# design-buff

`design-buff` is a Codex skill for product-minded, UX-rigorous design review. It reads screenshots, docs, or Figma evidence, reconstructs missing context, identifies structural UX issues, and produces:

- a human-facing `report.html`
- a machine-facing `review-state.json`

This repository README is only a GitHub entry point for humans. The runtime contract lives in `SKILL.md` and the files under `references/`.

## What This Skill Does

- reviews flows from business and UX angles instead of surface-only visual critique
- prefers layered Figma reads when a precise Figma URL or selection is available
- reconstructs background, goals, target users, and unknowns before critique
- runs an explicit three-flow continuity check across journey flow, operation flow, and mental flow
- outputs a durable HTML review artifact plus structured sidecar state
- keeps runtime output outside the skill package

## Source Of Truth

When you update or distribute this skill, use these files as the active contract:

- `SKILL.md`
- `agents/openai.yaml`
- `references/input-standard.md`
- `references/figma-high-precision.md`
- `references/review-playbook.md`
- `references/report-contract.md`
- `references/review-state-schema.md`

## Repository Layout

```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── agents/
├── references/
├── scripts/
└── templates/
```

## Install

1. Copy this folder into your Codex skills directory as `design-buff`.
2. Keep the skill package read-only at runtime.
3. Run reviews from the target project root, not from inside the skill package.

## Runtime Outputs

The skill does not write into its own repository during normal use.

- visible outputs: `design-buff-reviews/<review-slug>/`
- scratch data: `.design-buff/<review-slug>/`

Those folders belong in the reviewed project, not in this repository.

## Requirements

- Codex runtime with skill loading support
- Figma MCP for the highest-fidelity review path
- Python 3.9+ for bundled helper scripts

The skill still works without Figma MCP, but falls back to screenshot and document review.

## License

MIT. See `LICENSE`.
