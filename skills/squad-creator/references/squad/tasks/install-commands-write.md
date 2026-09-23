# Task: Write Command Files to Destination

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `install-commands-write` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: install-commands-write
name: "Write Command Files"
category: squad-installation
agent: squad-chief
elicit: false
autonomous: true
description: "Convert squad agents to IDE-specific formats and write command files to each detected IDE's directory."
```

## Purpose

Read source agent files from `squads/{squad_name}/agents/`, convert each agent to the IDE-specific format using per-IDE templates, and write the converted files to their destination directories. Only agents are synced -- tasks, checklists, templates, and workflows stay in squads/ and are loaded on-demand via IDE-FILE-RESOLUTION.

## Prerequisites

- [ ] `install-commands-resolve` completed successfully
- [ ] Resolution output available (agents_to_install, directories created)
- [ ] All target directories exist

## Inputs

```yaml
inputs:
  resolve_output:
    type: object
    required: true
    description: "Output from install-commands-resolve"
    contains:
      agents_to_install: list
      resolution_strategy: string
      directories_created: list
  squad:
    type: object
    required: true
    description: "Squad metadata from discovery"
```

## Workflow

### Step 1: Read Source Agent Files

For each file in `squads/{squad_name}/agents/*.md`:
- Parse agent metadata (name, role, id from header lines)
- Parse sections: Persona, Commands, Tasks, Templates, Activation
- Extract: core_principles, dependencies, integration_points

### Step 2: Convert to IDE Format

Each IDE has a specific output format. Apply the appropriate template per IDE.

**Supported Formats:**

| IDE | Format | Key Difference |
|-----|--------|----------------|
| Claude Code | `.md` with YAML activation block | Full IDE-FILE-RESOLUTION, REQUEST-RESOLUTION, activation-instructions |
| Codex | `SKILL.md` simplified | Skill-oriented, no YAML activation block |
| Gemini | `.md` with YAML block | Similar to Claude Code, simplified activation |
| Antigravity | `.md` with YAML block | Same structure as Gemini |
| Cursor | `.md` with `.cursorrules` ref | References .cursorrules for project-level rules |

### Step 3: Conversion Rules

```yaml
conversion_rules:
  agent_id:
    rule: "Convert filename to kebab-case"
    example: "process-mapper.md -> process-mapper"
  commands:
    rule: "Extract all *command-name from ## Commands section"
  task_references:
    rule: "Convert relative paths to absolute"
    example: "tasks/{task}.md -> squads/{squad_name}/tasks/{task}.md"
  preserve:
    - "All persona details"
    - "Expertise information"
    - "Style and focus"
    - "Core principles"
```

### Step 4: Write Converted Commands

For each agent, for each detected IDE:

```yaml
write_commands:
  for_each_agent:
    for_each_detected_ide:
      - step: "Generate IDE-specific content from template"
      - step: "Write to {ide_output_dir}/{agent-id}.md"
      - step: "Confirm: [pass] {ide}: Converted {agent-id}"
  on_failure:
    - "Log which agent failed for which IDE"
    - "Continue with next agent (do not abort)"
    - "Report failures at end"
```

### Step 5: Generate Per-IDE README

For each detected IDE, create a README in the command directory:

```yaml
readme_target: "{ide_command_dir}/{slashPrefix}/README.md"
readme_content:
  - Squad name, version, install timestamp, IDE name
  - Available agents list with activation syntax
  - Usage examples
  - Documentation links (squad README, agent source, tasks)
  - Uninstall instructions
```

## Output

```yaml
output:
  type: object
  schema:
    files_written:
      - path: ".claude/commands/{slashPrefix}/agents/agent-a.md"
        ide: "claude_code"
        agent_id: "agent-a"
        status: "success | failed"
    readmes_written:
      - ".claude/commands/{slashPrefix}/README.md"
    total_files: N
    failures: []
```

## Acceptance Criteria

- [ ] Every agent converted for every detected IDE
- [ ] Claude Code format includes full YAML activation block with IDE-FILE-RESOLUTION
- [ ] Codex format uses simplified SKILL.md structure
- [ ] Cursor format references .cursorrules
- [ ] Per-IDE README generated with correct activation syntax
- [ ] Failures logged but do not abort remaining agents
- [ ] NO tasks/checklists/templates leaked to command directories

## Veto Conditions

```yaml
veto_conditions: []
# Write phase has no veto -- conflicts were resolved in previous step.
# Failures are logged and reported, not blocked.
```

## Related Documents

| Reference | File |
|-----------|------|
| Parent Task | `install-commands.md` |
| Previous Sub-Task | `install-commands-resolve.md` |
| Next Sub-Task | `install-commands-verify.md` |
| Agent Template | `templates/agent-tmpl.md` |
| Format Details | See parent task IDE Format Reference section |

---

_Task Version: 1.0.0 (extracted from install-commands.md v1.0)_
