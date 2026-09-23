# Task: Squad Scaffold — Directory Structure & Initial Files

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-scaffold` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: create-squad-scaffold
name: "Squad Scaffold"
category: squad-creation
agent: squad-chief
elicit: false
autonomous: true
description: "Create the squad directory structure and initial files (config.yaml, README.md) using templates."
```

## Purpose

Create the physical directory structure for the new squad and generate initial files from templates. This is a deterministic, non-creative step that prepares the filesystem for component creation.

## Prerequisites

- [ ] `create-squad-architecture` completed successfully (PHASE 2 output available)
- [ ] Squad name, entry agent, and tier structure defined
- [ ] Write permissions for `squads/` directory
- [ ] Templates available: `templates/config-tmpl.yaml`

## Inputs

```yaml
inputs:
  phase_2_output:
    type: object
    required: true
    description: "Output from create-squad-architecture"
    fields: [tier_structure, quality_gates, handoffs, architecture_score]
  squad_name:
    type: string
    required: true
  pack_title:
    type: string
    required: true
  entry_agent:
    type: string
    required: true
  version:
    type: string
    required: true
    default: "1.0.0"
  author:
    type: string
    required: true
```

## Workflow / Steps

### Step 3.0: Verify No Existing Directory

```yaml
verify_no_collision:
  check: "squads/{squad_name}/ does NOT exist"
  on_exists:
    action: "HALT — trigger VETO-SQD-001"
    prompt: "Squad directory already exists. Overwrite? (yes/no)"
    on_confirm: "Remove existing and proceed"
    on_deny: "Abort scaffold"
```

### Step 3.1: Create Directory Structure

```yaml
create_directories:
  base: "squads/{squad_name}/"
  subdirectories:
    - agents/
    - tasks/
    - workflows/
    - templates/
    - checklists/
    - data/
    - docs/
```

### Step 3.2: Create Initial Files

```yaml
create_initial_files:
  config_yaml:
    source: "templates/config-tmpl.yaml"
    target: "squads/{squad_name}/config.yaml"
    interpolate:
      - pack.name: "{squad_name}"
      - pack.version: "{version}"
      - pack.description: "{purpose}"
      - pack.icon: "determined from domain"
      - entry_agent: "{entry_agent}"
      - agents: "from tier_structure"
      - capabilities: "from use_cases"
      - activation.shortcuts: "/{squad_name}:{entry_agent}"

  readme_md:
    target: "squads/{squad_name}/README.md"
    content: "Placeholder — will be completed in create-squad-integrate"
    sections:
      - "# {pack_title}"
      - "## Overview"
      - "## Agents"
      - "## Workflows"
      - "## Tasks"
      - "## Usage"
```

### Step 3.3: Initialize Runtime State

```yaml
init_runtime:
  state_file: ".aiox/squad-runtime/create-squad/{squad_name}/state.json"
  initial_state:
    squad_name: "{squad_name}"
    phase: "scaffold_complete"
    created_at: "{timestamp}"
    mode: "{mode}"
    phases_completed: ["discover", "select-type", "architecture", "scaffold"]
    phases_remaining: ["components", "integrate", "validate"]
```

## Output

```yaml
scaffold_output:
  base_path: "squads/{squad_name}/"
  directories_created: 7
  files_created:
    - "squads/{squad_name}/config.yaml"
    - "squads/{squad_name}/README.md"
  runtime_state: ".aiox/squad-runtime/create-squad/{squad_name}/state.json"
  status: "PASS"
```

## Acceptance Criteria

- [ ] Directory `squads/{squad_name}/` exists with all 7 subdirectories
- [ ] `config.yaml` is valid YAML with `entry_agent` field populated
- [ ] `config.yaml` defines `workspace_integration.level` (VETO-SQD-004)
- [ ] `README.md` placeholder created
- [ ] Runtime state file initialized
- [ ] No pre-existing directory was overwritten without confirmation

## Veto Conditions

- **VETO-SQD-001:** Squad directory already exists without user confirmation to overwrite
- **VETO-SQD-004:** `config.yaml` missing `workspace_integration.level` field

## Related Documents

- `create-squad.md` (parent composed task)
- `create-squad-architecture.md` (previous step)
- `create-squad-components.md` (next step)
- `templates/config-tmpl.yaml`

---

_Task Version: 1.0.0_
_Extracted from: create-squad.md PHASE 3 (Steps 3.0-3.1)_
