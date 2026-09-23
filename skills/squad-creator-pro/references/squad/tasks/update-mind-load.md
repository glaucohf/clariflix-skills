---
task-id: update-mind-load
name: "Load Existing DNA & Create Snapshot"
version: 1.0.0
execution_type: Hybrid
model: Sonnet
haiku_eligible: false
estimated-time: 5 min
complexity: low

inputs:
  required:
    - squad_name: "Nome do squad (ex: copy, legal)"
    - agent_slug: "Slug do agent existente (snake_case)"
  optional:
    - focus: "voice|thinking|both (default: both)"

outputs:
  primary:
    - existing_dna: "Parsed DNA sections from current agent file"
    - snapshot_before: "Quantitative snapshot of current DNA"
    - backup_path: "Path to backup file created"

elicit: false
---

# Task: Load Existing DNA & Create Snapshot

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `update-mind-load` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

- **Parent Task:** `update-mind` (orchestrator stub)
- **Sequence:** Phase 1 of 4
- **Previous Task:** None
- **Next Task:** `update-mind-extract`

## Purpose

Localizar arquivos existentes do agent, criar backup de seguranca, e gerar snapshot quantitativo do DNA atual para comparacao posterior no diff report.

## Prerequisites

- Agent existente em `squads/{squad_name}/agents/{agent_slug}.md`

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-UPM-001 | Backup must be created before any modification | BLOCK - Create backup first |
| VETO-UPM-002 | Agent file must exist and be parseable | BLOCK - Fix path or structure |

## Workflow / Steps

### Step 1: Locate Existing Files

```yaml
existing_files:
  agent_file: "squads/{squad_name}/agents/{agent_slug}.md"
  sources_dir: "squads/{squad_name}/minds/{agent_slug}/sources/"
  metadata: "squads/{squad_name}/minds/{agent_slug}/metadata.yaml"
```

Validate agent_file exists (REQUIRED). sources_dir and metadata are optional.

### Step 2: Create Backup

Copy current agent file to backup location:

```yaml
backup:
  path: "squads/{squad_name}/.backup/{agent_slug}.{timestamp}.md"
```

### Step 3: Generate Snapshot Before

Parse agent file and count elements:

```yaml
snapshot_before:
  voice_dna:
    power_words_count: 0
    signature_phrases_count: 0
    stories_count: 0
    anti_patterns_count: 0
  thinking_dna:
    frameworks_count: 0
    heuristics_count: 0
    recognition_patterns_count: 0
  sources:
    total: 0
    tier_1: 0
  quality_scores:
    voice: "X/10"
    thinking: "X/9"
    fidelity_estimate: "X%"
```

## Output

```yaml
existing_dna: { parsed YAML blocks from agent file }
snapshot_before: { counts as above }
backup_path: "squads/{squad_name}/.backup/{agent_slug}.{timestamp}.md"
```

## Acceptance Criteria

- [ ] Agent file located and validated as parseable
- [ ] Backup created at `.backup/` before any modification
- [ ] Snapshot counts are accurate (verified against file content)
- [ ] All existing file paths mapped

## Related Documents

| Document | Relationship |
|----------|-------------|
| `update-mind.md` | Parent orchestrator |
| `update-mind-extract.md` | Next phase |
