# Task: Discover Commands — IDE Detection & Squad Validation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `install-commands-discover` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: install-commands-discover
name: "Discover Commands"
category: squad-installation
agent: squad-chief
elicit: true
autonomous: true
description: "Detect installed IDEs, validate squad structure, and collect inputs for command installation."
```

## Purpose

Scan the project root for supported IDE configuration directories, validate that the target squad exists with proper structure (config.yaml + agents/), and build the discovery context needed by downstream sub-tasks.

## Prerequisites

- [ ] squad-chief agent is active
- [ ] Write permissions for project root directory
- [ ] At least one IDE configuration directory exists (or user accepts fallback)

## Inputs

```yaml
inputs:
  squad_name:
    type: string
    required: true
    description: "Name of the squad to install"
    source: "user input or discovery via `ls squads/`"
  force:
    type: boolean
    required: false
    default: false
    description: "Skip overwrite confirmations"
```

## Workflow

### Step 1: Detect Installed IDEs

Scan the project root for IDE configuration directories.

```yaml
ide_detection:
  checks:
    claude_code:
      detect: "Directory .claude/ exists at project root"
      config_file: ".claude/settings.json OR .claude/settings.local.json"
      command_dir: ".claude/commands/"
      status: "detected | not_found"
    codex:
      detect: "Directory .codex/ exists at project root"
      config_file: ".codex/config.yaml OR .codex/settings.json"
      command_dir: ".codex/skills/"
      status: "detected | not_found"
    gemini:
      detect: "Directory .gemini/ exists at project root"
      config_file: ".gemini/settings.json"
      command_dir: ".gemini/commands/"
      status: "detected | not_found"
    antigravity:
      detect: "Directory .antigravity/ exists at project root"
      config_file: ".antigravity/config.yaml"
      command_dir: ".antigravity/commands/"
      status: "detected | not_found"
    cursor:
      detect: "Directory .cursor/ exists at project root OR .cursorrules file exists"
      config_file: ".cursorrules"
      command_dir: ".cursor/commands/"
      status: "detected | not_found"
```

### Step 2: IDE Detection Fallback

```yaml
detection_fallback:
  if_no_ides_detected:
    action: |
      No IDE configuration directories found. Options:
      1. Install for Claude Code (create .claude/commands/)
      2. Install for specific IDE (specify which)
      3. Install for all IDEs (create all directories)
      4. Cancel
  if_only_one_detected:
    action: "Proceed with detected IDE only"
  always_include:
    - "claude_code"  # Always install for Claude Code as baseline
```

### Step 3: Validate Squad Structure

If squad name not provided, ask user:

```
Which squad would you like to install?
Available squads: [list directories in squads/]
```

Validate:
- `squads/{squad_name}/config.yaml` exists
- `squads/{squad_name}/agents/` directory exists
- Load config.yaml to extract: `name`, `slashPrefix`, `version`

### Step 4: Report Discovery

```
IDE DETECTION RESULTS

  [detected] Claude Code  - .claude/commands/
  [not_found] Codex       - .codex/skills/
  [detected] Gemini       - .gemini/commands/
  ...

IDEs detected: {N} of 5
Primary IDE: {first detected}

SQUAD VALIDATION
  [pass] Found squad: {name} v{version}
  Slash prefix: @{slashPrefix}:
  Agents found: {count}
```

## Output

```yaml
output:
  type: object
  schema:
    detected_ides: ["claude_code", "gemini"]
    total_detected: 2
    primary_ide: "claude_code"
    squad:
      name: "{squad_name}"
      path: "squads/{squad_name}/"
      slash_prefix: "{slashPrefix}"
      version: "{version}"
      agent_count: N
      agent_files: ["agent-a.md", "agent-b.md"]
    force: false
```

## Acceptance Criteria

- [ ] All 5 IDE directories are checked
- [ ] Fallback offered when no IDEs detected
- [ ] Squad config.yaml parsed successfully
- [ ] Agent count matches files in agents/ directory
- [ ] Output schema is complete for downstream tasks

## Veto Conditions

```yaml
veto_conditions:
  - id: "VETO-INSTALL-002"
    condition: "Squad source structure validation failed"
    trigger: "config.yaml missing OR agents/ directory missing"
    block_behavior: "BLOCK install; suggest *create-squad"
```

## Related Documents

| Reference | File |
|-----------|------|
| Parent Task | `install-commands.md` |
| Config Schema | `data/config-schema.yaml` |
| Worker Script | `scripts/sync-ide-command.py` |

---

_Task Version: 1.0.0 (extracted from install-commands.md v1.0)_
