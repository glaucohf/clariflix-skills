# Task: Squad Smoke Test — Operational Verification

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `create-squad-smoke-test` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: create-squad-smoke-test
name: "Squad Smoke Test"
category: squad-creation
agent: squad-chief
elicit: false
autonomous: true
description: "Run a quick operational smoke test: activate squad, verify greeting, run *help, test 1 command."
```

## Purpose

Verify that the newly created squad is operationally functional by performing a minimal end-to-end activation test. This confirms the squad can be activated, responds with the correct greeting, lists its commands, and executes at least one command successfully.

## Prerequisites

- [ ] Squad validation passed (or fix cycle succeeded)
- [ ] Entry agent file exists at `squads/{squad_slug}/agents/{entry_agent}.md`
- [ ] `config.yaml` defines `entry_agent` and `activation.shortcuts`
- [ ] Command files installed (if applicable)

## Inputs

```yaml
inputs:
  squad_slug:
    type: string
    required: true
    description: "Slug of the squad to smoke test"
  entry_agent:
    type: string
    required: true
    description: "ID of the entry agent to activate"
  config_path:
    type: file
    required: true
    path: "squads/{squad_slug}/config.yaml"
    description: "Squad configuration file"
```

## Workflow / Steps

### Step 1: Activate Entry Agent

- Load the entry agent file from `squads/{squad_slug}/agents/{entry_agent}.md`
- Parse the agent definition (YAML block + markdown sections)
- Verify the agent file is well-formed (has `agent.id`, `persona`, `commands`)
- Confirm the agent responds with a greeting matching `greeting_levels`
- **Pass criteria:** Agent file loads without parse errors, greeting text present

### Step 2: Verify *help Command

- Simulate `*help` command against the entry agent definition
- Verify the agent has a `commands` section with at least 1 command defined
- Confirm each command has: `name`, `description`, `visibility`
- **Pass criteria:** Commands list is non-empty and well-structured

### Step 3: Test One Command

- Select the first non-help command from the agent's command list
- Verify the command has a corresponding task or handler:
  - Check `dependencies.tasks` for a matching task file
  - Or check if command maps to a known workflow
- Verify the referenced task file exists on disk
- **Pass criteria:** At least one command resolves to an existing task file

### Step 4: Generate Smoke Test Report

- Produce `smoke-test-report.md` with:
  - Test date and squad slug
  - Results for each test scenario (PASS/FAIL)
  - Overall verdict: PASS (3/3) or FAIL (with details)
  - Entry agent activation command for documentation

## Output

```yaml
outputs:
  smoke_test_report:
    path: ".aiox/squad-runtime/create-squad/{squad_slug}/validation/smoke-test-report.md"
    description: "Smoke test results with per-scenario verdicts"
  verdict:
    type: enum
    values: [PASS, FAIL]
    description: "Overall smoke test result"
```

## Acceptance Criteria

- [ ] Entry agent file loads and parses without errors
- [ ] Greeting text is present and matches agent persona
- [ ] *help lists at least 1 command with name and description
- [ ] At least 1 command resolves to an existing task file
- [ ] Smoke test report generated with 3 scenario results
- [ ] Overall verdict is PASS only when all 3 scenarios pass

## Veto Conditions

- **VETO if** entry agent file does not exist or fails to parse
- **VETO if** config.yaml does not define an entry_agent
- **VETO if** smoke test passes but no report is generated

## Related Documents

- `squads/squad-creator/workflows/create-squad.yaml` (smoke_test phase)
- `squads/squad-creator/workflows/wf-create-squad.yaml` (phase-8 OPERATIONAL TEST)
- `squads/squad-creator/tasks/create-squad-validate.md` (upstream validation)
- `squads/squad-creator/tasks/qa-check-structure.md` (structural checks reference)
