# Task: Verify Commands Installed Correctly

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `install-commands-verify` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: install-commands-verify
name: "Verify Installation"
category: squad-installation
agent: squad-chief
elicit: false
autonomous: true
description: "Run per-IDE validation checks, cross-IDE consistency checks, and confirm installation integrity."
```

## Purpose

Validate that all agents were correctly converted and written to each detected IDE's command directory. Verify file counts match, YAML syntax is valid, no non-agent artifacts leaked, and all IDEs have consistent agent coverage.

## Prerequisites

- [ ] `install-commands-write` completed successfully
- [ ] Write output available (files_written, failures)

## Inputs

```yaml
inputs:
  write_output:
    type: object
    required: true
    description: "Output from install-commands-write"
    contains:
      files_written: list
      failures: list
      total_files: number
  discovery_output:
    type: object
    required: true
    description: "Original discovery output"
    contains:
      squad: object
      detected_ides: list
```

## Workflow

### Step 1: Per-IDE Validation

For each detected IDE, run three checks:

```yaml
per_ide_validation:
  checks:
    - id: "V-IDE-001"
      check: "All agents converted"
      action: |
        Count source: ls squads/{squad_name}/agents/*.md | wc -l
        Count target: ls {ide_command_dir}/{slashPrefix}/agents/*.md | wc -l
        Compare: source_count == target_count
      on_fail: "Report which agents failed for {ide_name}"

    - id: "V-IDE-002"
      check: "YAML syntax valid in converted files"
      action: "Basic check for ```yaml blocks in each converted agent file"
      on_fail: "Report which files have YAML issues"

    - id: "V-IDE-003"
      check: "No tasks/checklists/templates leaked to commands"
      action: |
        For each IDE command dir:
          Verify NO tasks/, checklists/, templates/, workflows/ directories exist
      on_fail: "Report leaked directories -- these belong in squads/ only"
```

### Step 2: Cross-IDE Consistency Check

```yaml
consistency_check:
  check: "Same agents installed across all IDEs"
  action: |
    For each IDE pair:
      Compare agent file lists
      Report any discrepancies
  on_discrepancy: "Warning: {ide_a} has {agent} but {ide_b} does not"
```

### Step 3: Report Verification Results

```
VERIFICATION RESULTS

  V-IDE-001: Agent count match
    [pass] Claude Code: 5/5 agents
    [pass] Gemini: 5/5 agents

  V-IDE-002: YAML syntax valid
    [pass] All files valid

  V-IDE-003: No leaked artifacts
    [pass] Clean command directories

  Cross-IDE Consistency: [pass] All IDEs match
```

## Output

```yaml
output:
  type: object
  schema:
    verification_passed: true | false
    checks:
      - id: "V-IDE-001"
        status: "pass | fail"
        details: "5/5 agents for all IDEs"
      - id: "V-IDE-002"
        status: "pass | fail"
        details: "All YAML blocks valid"
      - id: "V-IDE-003"
        status: "pass | fail"
        details: "No leaked directories"
    consistency:
      status: "pass | warning"
      discrepancies: []
    failed_agents: []
```

## Acceptance Criteria

- [ ] Source agent count matches target count per IDE
- [ ] All converted files contain valid YAML blocks
- [ ] No tasks/, checklists/, templates/, workflows/ directories in command dirs
- [ ] Cross-IDE agent lists are identical
- [ ] Clear report produced with pass/fail per check

## Veto Conditions

```yaml
veto_conditions: []
# Verification reports but does not block -- failures are informational.
# The report sub-task will surface any issues.
```

## Related Documents

| Reference | File |
|-----------|------|
| Parent Task | `install-commands.md` |
| Previous Sub-Task | `install-commands-write.md` |
| Next Sub-Task | `install-commands-sync.md` |

---

_Task Version: 1.0.0 (extracted from install-commands.md v1.0)_
