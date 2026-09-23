# Task: Installation Report with Before/After Diff

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `install-commands-report` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: install-commands-report
name: "Installation Report"
category: squad-installation
agent: squad-chief
elicit: false
autonomous: true
description: "Generate a comprehensive installation report with before/after diff, usage examples, and next steps."
```

## Purpose

Produce a final summary report showing what was installed, where, for which IDEs, with a before/after file count diff, usage examples, and actionable next steps for the user.

## Prerequisites

- [ ] All previous sub-tasks completed
- [ ] Verification and sync outputs available

## Inputs

```yaml
inputs:
  discovery_output:
    type: object
    required: true
    description: "Output from install-commands-discover"
  write_output:
    type: object
    required: true
    description: "Output from install-commands-write"
  verify_output:
    type: object
    required: true
    description: "Output from install-commands-verify"
  sync_output:
    type: object
    required: true
    description: "Output from install-commands-sync"
```

## Workflow

### Step 1: Generate Cross-IDE Summary Table

```
INSTALLATION COMPLETE

Squad: {squad_name} v{version}

| IDE | Agents | Status |
|-----|--------|--------|
| Claude Code | {N} | [pass] |
| Gemini | {N} | [pass] |
| Codex | -- | [skip] not detected |
| Antigravity | -- | [skip] not detected |
| Cursor | -- | [skip] not detected |

Total files created: {total}
```

### Step 2: Before/After Diff

```
BEFORE / AFTER

  Before:
    .claude/commands/{slashPrefix}/: {0 | N existing files}
    .gemini/commands/{slashPrefix}/: {0 | N existing files}

  After:
    .claude/commands/{slashPrefix}/: {N files} (+{delta})
    .gemini/commands/{slashPrefix}/: {N files} (+{delta})

  New files: {count}
  Overwritten: {count}
  Skipped: {count}
```

### Step 3: Available Commands

```
Commands available (Claude Code):

  /{slashPrefix}:{agent-id-1} - {description}
  /{slashPrefix}:{agent-id-2} - {description}
  ...

Tasks/checklists/templates stay in squads/{squad_name}/ (loaded on-demand).
```

### Step 4: Next Steps

```
NEXT STEPS

  1. Test the installation:
     /{slashPrefix}:{first-agent}
     *help

  2. Read the documentation:
     squads/{squad_name}/README.md

  3. Share with team:
     Commit IDE command directories to git if team-shared
     Or keep in .gitignore if personal installation

  4. Install for additional IDEs:
     python3 scripts/sync-ide-command.py squad {name} --ide=cursor
```

### Step 5: Error Summary (if any)

If verification found issues, surface them:

```
WARNINGS

  - {agent-id} failed conversion for {ide}: {reason}
  - Cross-IDE discrepancy: {details}

  Suggest: Review and rerun with --force if needed.
```

## Output

```yaml
output:
  type: object
  schema:
    report: string  # Full formatted report text
    summary:
      squad: "{squad_name}"
      version: "{version}"
      ides_installed: N
      agents_per_ide: N
      total_files_created: N
      files_overwritten: N
      warnings: N
    success: true | false
```

## Acceptance Criteria

- [ ] Cross-IDE summary table with pass/fail/skip per IDE
- [ ] Before/after file count diff
- [ ] Full list of available activation commands
- [ ] Actionable next steps with copy-paste examples
- [ ] Warnings surfaced if verification found issues
- [ ] Report is human-readable, under 50 lines of output

## Veto Conditions

```yaml
veto_conditions: []
# Report is the final step -- informational only, never blocks.
```

## Related Documents

| Reference | File |
|-----------|------|
| Parent Task | `install-commands.md` |
| Previous Sub-Task | `install-commands-sync.md` |
| Worker Script | `scripts/sync-ide-command.py` |

---

_Task Version: 1.0.0 (extracted from install-commands.md v1.0)_
