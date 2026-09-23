# Task: Sync with Claude Code Skills Index

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `install-commands-sync` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: install-commands-sync
name: "Sync Skills Index"
category: squad-installation
agent: squad-chief
elicit: false
autonomous: true
description: "Sync installed commands with Claude Code's skill discovery index and verify activation syntax works."
```

## Purpose

Ensure that installed commands are discoverable by Claude Code's skill system. Verify that the `/{slashPrefix}:{agent-id}` activation syntax resolves correctly, and that the skills index recognizes the new commands.

## Prerequisites

- [ ] `install-commands-verify` completed successfully
- [ ] Verification passed (or passed with warnings only)

## Inputs

```yaml
inputs:
  verify_output:
    type: object
    required: true
    description: "Output from install-commands-verify"
  discovery_output:
    type: object
    required: true
    description: "Original discovery output with squad metadata"
```

## Workflow

### Step 1: Verify Skill Resolution

For each agent installed to Claude Code:
- Confirm the file exists at `.claude/commands/{slashPrefix}/agents/{agent-id}.md`
- Verify the file starts with `# /{slashPrefix}:{agent-id} Command`
- Confirm the YAML activation block is present and parseable

### Step 2: Check Skill Discoverability

```yaml
discoverability_check:
  claude_code:
    method: "Verify .claude/commands/{slashPrefix}/ directory is indexed"
    validation: "Files in .claude/commands/ are auto-discovered by Claude Code"
  other_ides:
    method: "IDE-specific discovery varies; file presence is sufficient"
```

### Step 3: Validate Activation Syntax

For each installed agent, confirm the activation path:

```yaml
activation_validation:
  claude_code: "/{slashPrefix}:{agent-id}"
  codex: "Skill: {Agent Name}"
  gemini: "/{slashPrefix}:{agent-id}"
  antigravity: "/{slashPrefix}:{agent-id}"
  cursor: "/{slashPrefix}:{agent-id}"
```

### Step 4: Report Sync Status

```
SYNC STATUS

  Claude Code Skills Index:
    [pass] {slashPrefix} directory indexed
    [pass] {N} agents discoverable
    Activation: /{slashPrefix}:{agent-id}

  Other IDEs:
    [pass] Gemini: files in place
    [skip] Codex: not detected
```

## Output

```yaml
output:
  type: object
  schema:
    sync_status: "synced | partial | failed"
    discoverable_agents:
      - ide: "claude_code"
        agent_id: "agent-a"
        activation: "/{slashPrefix}:agent-a"
        discoverable: true
    activation_commands:
      - "/{slashPrefix}:agent-a"
      - "/{slashPrefix}:agent-b"
```

## Acceptance Criteria

- [ ] All Claude Code command files are in the correct directory structure
- [ ] Activation syntax follows `/{slashPrefix}:{agent-id}` pattern
- [ ] Files auto-discoverable by Claude Code's skill system
- [ ] Activation commands list generated for user reference

## Veto Conditions

```yaml
veto_conditions: []
# Sync is informational -- does not block installation.
```

## Related Documents

| Reference | File |
|-----------|------|
| Parent Task | `install-commands.md` |
| Previous Sub-Task | `install-commands-verify.md` |
| Next Sub-Task | `install-commands-report.md` |
| Sync Script | `scripts/sync-ide-command.py` |

---

_Task Version: 1.0.0 (extracted from install-commands.md v1.0)_
