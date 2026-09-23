# Task: Register Workflow in Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-workflow-register` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: create-workflow-register
name: Register Workflow in Squad
category: workflow-creation
agent: squad-chief
elicit: false
autonomous: true
description: >
  Register the created workflow in squad config.yaml,
  update the squad README, and present a handoff summary
  with structure and quality metrics.
```

## Purpose

Complete the workflow creation pipeline by registering the new workflow in the squad's configuration, updating documentation, and presenting a summary to the user. This is a deterministic registration step -- no creative decisions, only file updates and reporting.

## Prerequisites

- [ ] Workflow file exists and passed validation (create-workflow-generate output)
- [ ] SC_WFL_001 quality gate passed
- [ ] workflow-validator.js passed in strict mode

## Inputs

```yaml
inputs:
  - name: workflow_file
    type: object
    required: true
    source: previous_task
    description: "Validated workflow file from create-workflow-generate"

  - name: phase_0_classification
    type: object
    required: true
    source: previous_task
    description: "Workflow identity (name, id, squad)"

  - name: squad_name
    type: string
    required: true
    source: previous_task
    description: "Target squad identifier"
```

## Workflow / Steps

### Step 1: Update config.yaml

Add the workflow to the squad's configuration:

```yaml
update_config:
  file: "squads/{squad_name}/config.yaml"
  section: "workflows"
  add:
    - id: "wf-{workflow_id}"
      name: "{workflow_name}"
      file: "workflows/wf-{workflow_id}.yaml"
      phases: "{phase_count}"
      agents: "{agent_count}"
```

### Step 2: Update README

Add the workflow to the squad's README:

```yaml
update_readme:
  file: "squads/{squad_name}/README.md"
  section: "Workflows"
  add:
    entry: "- **{workflow_name}** (`wf-{workflow_id}.yaml`) -- {description}"
```

### Step 3: Present Handoff Summary

```yaml
present_summary:
  workflow_created:
    name: "{workflow_name}"
    id: "wf-{workflow_id}"
    file: "squads/{squad_name}/workflows/wf-{workflow_id}.yaml"
    lines: "{line_count}"

  structure:
    phases: "{phase_count}"
    total_tasks: "{task_count}"
    checkpoints: "{checkpoint_count}"
    agents_involved: "{agent_count}"

  quality:
    score: "{SC_WFL_001_score}/10"
    contract: "PASS"
    status: "PASS"

  next_actions:
    - "Review workflow file for domain accuracy"
    - "Create any placeholder tasks marked as TODO"
    - "Test workflow execution with a sample run"
```

## Output

```yaml
output:
  name: registration_complete
  format: yaml
  structure:
    config_updated: true
    readme_updated: true
    summary_presented: true
    workflow_path: "squads/{squad_name}/workflows/wf-{workflow_id}.yaml"
```

## Acceptance Criteria

- [ ] Workflow added to config.yaml workflows section
- [ ] README updated with workflow entry
- [ ] Handoff summary presented with structure and quality metrics
- [ ] All file paths are correct and files exist

## Veto Conditions

- config.yaml update fails or corrupts existing content
- Workflow file does not exist at expected path
- Registration attempted before validation passes

## Related Documents

- `create-workflow-generate.md` -- Preceding task (YAML generation)
- `create-workflow.md` -- Parent composed task
- `squads/{squad_name}/config.yaml` -- Target configuration file
- `squads/{squad_name}/README.md` -- Target documentation file

---

_Task Version: 1.0.0_
_Extracted from: create-workflow.md PHASE 5 (Handoff)_
