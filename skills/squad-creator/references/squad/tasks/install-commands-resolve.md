# Task: Resolve Conflicts & Dependencies

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `install-commands-resolve` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: install-commands-resolve
name: "Resolve Conflicts & Dependencies"
category: squad-installation
agent: squad-chief
elicit: true
autonomous: true
description: "Create per-IDE directory structures, check for existing command files, and resolve overwrite conflicts before writing."
```

## Purpose

Create the required directory structures for each detected IDE, detect existing command files that would be overwritten, and resolve conflicts via user confirmation or --force flag. This ensures the write phase has a clean, conflict-free target.

## Prerequisites

- [ ] `install-commands-discover` completed successfully
- [ ] Discovery output available (detected IDEs, squad metadata)

## Inputs

```yaml
inputs:
  discovery_output:
    type: object
    required: true
    description: "Output from install-commands-discover"
    contains:
      detected_ides: list
      squad: object
      force: boolean
```

## Workflow

### Step 1: Create Per-IDE Directory Structures

For each detected IDE, create the command directory:

```yaml
directory_creation:
  claude_code:
    directories:
      - ".claude/commands/{slashPrefix}/"
      - ".claude/commands/{slashPrefix}/agents/"
  codex:
    directories:
      - ".codex/skills/{slashPrefix}/"
      - ".codex/skills/{slashPrefix}/agents/"
  gemini:
    directories:
      - ".gemini/commands/{slashPrefix}/"
      - ".gemini/commands/{slashPrefix}/agents/"
  antigravity:
    directories:
      - ".antigravity/commands/{slashPrefix}/"
      - ".antigravity/commands/{slashPrefix}/agents/"
  cursor:
    directories:
      - ".cursor/commands/{slashPrefix}/"
      - ".cursor/commands/{slashPrefix}/agents/"
```

Execution: `mkdir -p` for each detected IDE. Skip undetected IDEs unless user chose "install for all".

### Step 2: Detect Existing Command Files

For each detected IDE, check if agent command files already exist at the target path:

```yaml
conflict_detection:
  for_each_ide:
    for_each_agent:
      target: "{ide_output_dir}/{agent-id}.md"
      check: "File exists?"
      if_exists: "Add to conflicts list"
```

### Step 3: Resolve Conflicts

```yaml
conflict_resolution:
  if_no_conflicts:
    action: "Proceed to write phase"
  if_conflicts_found:
    if_force_flag:
      action: "Mark all for overwrite, log warning"
    else:
      action: |
        Existing files found that will be overwritten:
        {list each conflicting file per IDE}
        Options:
        1. Overwrite all (equivalent to --force)
        2. Skip existing (only install new agents)
        3. Cancel installation
```

### Step 4: Report Resolution

```
RESOLUTION RESULTS

  [pass] Created directory structures for {N} IDEs:
    - Claude Code: .claude/commands/{slashPrefix}/
    - Gemini: .gemini/commands/{slashPrefix}/

  Conflicts: {count}
  Resolution: {overwrite_all | skip_existing | none}
```

## Output

```yaml
output:
  type: object
  schema:
    directories_created:
      - ".claude/commands/{slashPrefix}/agents/"
      - ".gemini/commands/{slashPrefix}/agents/"
    conflicts:
      - ide: "claude_code"
        file: ".claude/commands/{slashPrefix}/agents/agent-a.md"
        resolution: "overwrite"
    resolution_strategy: "overwrite_all | skip_existing | none"
    agents_to_install:
      - agent_id: "agent-a"
        source: "squads/{squad}/agents/agent-a.md"
        targets:
          claude_code: ".claude/commands/{slashPrefix}/agents/agent-a.md"
          gemini: ".gemini/commands/{slashPrefix}/agents/agent-a.md"
```

## Acceptance Criteria

- [ ] All required directories created via mkdir -p
- [ ] Existing files detected before any writes occur
- [ ] User prompted on conflicts (unless --force)
- [ ] Skipped IDEs logged clearly
- [ ] agents_to_install list complete with all source-to-target mappings

## Veto Conditions

```yaml
veto_conditions:
  - id: "VETO-INSTALL-001"
    condition: "Destination file exists and overwrite not authorized"
    trigger: "Conflicts found, user chose Cancel"
    block_behavior: "BLOCK write phase; abort installation"
```

## Related Documents

| Reference | File |
|-----------|------|
| Parent Task | `install-commands.md` |
| Previous Sub-Task | `install-commands-discover.md` |
| Next Sub-Task | `install-commands-write.md` |

---

_Task Version: 1.0.0 (extracted from install-commands.md v1.0)_
