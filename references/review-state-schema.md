# Review State Schema

Use this reference when writing or updating:

```text
design-buff-reviews/<review-slug>/review-state.json
```

This file governs the machine sidecar only. Human-facing report structure and chat rules live in `report-contract.md`.

## Purpose

`review-state.json` stores structured durable state so the system can:

- recover prior review state without reparsing the full HTML report
- compare runs
- track issue identity over time
- render `Changes Since Last Review`

It is not a second human-facing report.

## v1 Top-Level Shape

```json
{
  "schema_version": "v1",
  "meta": {},
  "intake": {},
  "coverage": {},
  "background": {},
  "evidence": [],
  "issues": [],
  "priorities": {},
  "history": {}
}
```

## v1 Field Specification

### `schema_version`

- required: yes
- type: `string`
- value in v1: `"v1"`

### `meta`

Run identity and compatibility metadata.

- `project_name`: `string`, optional
- `review_slug`: `string`, required
- `report_mode`: `string`, required, allowed `self-check | agent-review`
- `review_date`: `string`, required, format `YYYY-MM-DD`
- `reviewer`: `string`, required
- `report_language`: `string`, required
- `language_source`: `string`, required, allowed `explicit_override | intake_inference | default_zh_cn`
- `run_id`: `string`, required
- `input_hash`: `string | null`, optional
- `template_version`: `string`, required
- `renderer_version`: `string`, required
- `created_at`: `string`, required, ISO 8601 timestamp
- `updated_at`: `string`, required, ISO 8601 timestamp

### `intake`

Normalized intake state and selected review scope.

- `source_artifacts`: `array<string>`, required
- `figma_intake_url`: `string | null`, optional
- `figma_file_key`: `string | null`, optional
- `figma_intake_node`: `string | null`, optional
- `figma_intake_node_type`: `string | null`, optional
- `ingest_status`: `string`, required
- `selected_unit_ids`: `array<string>`, required
- `high_precision_unit_ids`: `array<string>`, required
- `structural_only_unit_ids`: `array<string>`, required
- `deferred_unit_ids`: `array<string>`, required
- `tool_limits`: `array<string>`, required

### `coverage`

Read coverage and validation coverage.

- `fully_read_unit_ids`: `array<string>`, required
- `partially_read_unit_ids`: `array<string>`, required
- `screenshot_validated_unit_ids`: `array<string>`, required
- `open_tooling_gaps`: `array<string>`, required

### `background`

Structured background state only. Keep human-facing narrative out of this object.

- `page_type`: `string | null`, optional
- `product_type`: `string | null`, optional
- `industry`: `string | null`, optional
- `target_user`: `string | null`, optional
- `core_scenario`: `string | null`, optional
- `business_goal`: `string | null`, optional
- `workflow_position`: `string | null`, optional
- `summary`: `string | null`, optional, short structured summary only
- `assumptions`: `array<string>`, required
- `unknowns`: `array<string>`, required
- `confidence`: `string | null`, optional

### `evidence`

Evidence ledger. Every item must be machine-usable.

Each item includes:

- `evidence_id`: `string`, required
- `source_type`: `string`, required
- `node_ref`: `string | null`, optional
- `artifact_ref`: `string | null`, optional
- `read_method`: `string`, required
- `confidence`: `string`, required
- `raw_ref`: `string | null`, optional
- `tags`: `array<string>`, required

### `issues`

Structured issue state. Stable issue identity behavior is defined in `review-playbook.md`; this file only defines the machine fields.

Each item includes:

- `stable_id`: `string`, required
- `display_number`: `string`, required, example `ISSUE-001`
- `title`: `string`, required
- `category`: `string`, required
- `severity`: `string`, required
- `confidence`: `string`, required
- `status`: `string`, required, recommended `active | resolved | changed | deferred`
- `evidence_ids`: `array<string>`, required
- `problem_summary`: `string | null`, optional, short machine summary only
- `impact_summary`: `string | null`, optional, short machine summary only
- `recommendation_summary`: `string | null`, optional, short machine summary only
- `discussion_prompts`: `array<string>`, required

### `priorities`

Structured priority state.

- `highest_priority_issue_id`: `string | null`, optional
- `top_issue_ids`: `array<string>`, required
- `open_questions`: `array<object>`, required
- `next_actions`: `array<object>`, required

Each `open_questions` item includes:

- `question_id`: `string`
- `title`: `string`
- `status`: `string`
- `related_issue_ids`: `array<string>`

Each `next_actions` item includes:

- `action_id`: `string`
- `title`: `string`
- `status`: `string`
- `related_issue_ids`: `array<string>`

### `history`

Structured review diff state.

- `previous_run_id`: `string | null`, optional
- `previous_review_date`: `string | null`, optional
- `new_issue_ids`: `array<string>`, required
- `resolved_issue_ids`: `array<string>`, required
- `changed_issue_ids`: `array<string>`, required
- `severity_changed_issue_ids`: `array<string>`, required
- `recommendation_changed_issue_ids`: `array<string>`, required

## Forbidden Content

Do not store:

- executive summary prose
- full issue prose
- `why_it_is_a_problem` long-form text
- complete human-facing recommendation paragraphs
- any text block that could be mistaken for the formal review report

Rule of thumb:

- if a field helps the system resume, compare, or track, it belongs here
- if a field mainly exists to persuade or explain to a human reader, it belongs in `report.html`

## Minimal Example

```json
{
  "schema_version": "v1",
  "meta": {
    "project_name": "Example Review",
    "review_slug": "example-review",
    "report_mode": "self-check",
    "review_date": "2026-03-27",
    "reviewer": "Codex design-buff",
    "report_language": "zh-CN",
    "language_source": "intake_inference",
    "run_id": "run_001",
    "input_hash": "abc123",
    "template_version": "human-report-html-v1",
    "renderer_version": "design-buff-v0.7",
    "created_at": "2026-03-27T10:00:00Z",
    "updated_at": "2026-03-27T10:15:00Z"
  },
  "intake": {
    "source_artifacts": ["figma:get_metadata", "figma:get_design_context"],
    "figma_intake_url": "https://www.figma.com/design/FILE123/Test?node-id=1-2",
    "figma_file_key": "FILE123",
    "figma_intake_node": "1:2",
    "figma_intake_node_type": "frame",
    "ingest_status": "success",
    "selected_unit_ids": ["1:2", "1:3"],
    "high_precision_unit_ids": ["1:2"],
    "structural_only_unit_ids": ["1:3"],
    "deferred_unit_ids": [],
    "tool_limits": []
  },
  "coverage": {
    "fully_read_unit_ids": ["1:2"],
    "partially_read_unit_ids": ["1:3"],
    "screenshot_validated_unit_ids": ["1:2"],
    "open_tooling_gaps": []
  },
  "background": {
    "page_type": "mobile modal flow",
    "product_type": "membership binding flow",
    "industry": "travel",
    "target_user": "high-intent loyalty users",
    "core_scenario": "choose the correct path and complete account linking",
    "business_goal": "increase successful account binding",
    "workflow_position": "late-stage conversion",
    "summary": "membership opening and linking flow",
    "assumptions": ["user may not know account status"],
    "unknowns": ["real callback behavior"],
    "confidence": "medium-high"
  },
  "evidence": [
    {
      "evidence_id": "ev_001",
      "source_type": "figma",
      "node_ref": "1:2",
      "artifact_ref": "intake-board",
      "read_method": "get_design_context",
      "confidence": "high",
      "raw_ref": ".design-buff/example-review/tool-cache/context-1-2.json",
      "tags": ["copy", "cta", "hierarchy"]
    }
  ],
  "issues": [
    {
      "stable_id": "routing-self-diagnosis__90f948",
      "display_number": "ISSUE-001",
      "title": "Routing depends on self-diagnosis",
      "category": "scenario and fit",
      "severity": "high",
      "confidence": "high",
      "status": "active",
      "evidence_ids": ["ev_001"],
      "problem_summary": "entry routing asks users to infer backend state",
      "impact_summary": "causes wrong-path failure and trust loss",
      "recommendation_summary": "prefer system routing or a clear uncertainty path",
      "discussion_prompts": ["Can the system pre-check account status?"]
    }
  ],
  "priorities": {
    "highest_priority_issue_id": "routing-self-diagnosis__90f948",
    "top_issue_ids": ["routing-self-diagnosis__90f948"],
    "open_questions": [
      {
        "question_id": "q_001",
        "title": "Can the system pre-check account status?",
        "status": "open",
        "related_issue_ids": ["routing-self-diagnosis__90f948"]
      }
    ],
    "next_actions": [
      {
        "action_id": "a_001",
        "title": "Add a clearer routing decision path",
        "status": "pending",
        "related_issue_ids": ["routing-self-diagnosis__90f948"]
      }
    ]
  },
  "history": {
    "previous_run_id": null,
    "previous_review_date": null,
    "new_issue_ids": ["routing-self-diagnosis__90f948"],
    "resolved_issue_ids": [],
    "changed_issue_ids": [],
    "severity_changed_issue_ids": [],
    "recommendation_changed_issue_ids": []
  }
}
```
