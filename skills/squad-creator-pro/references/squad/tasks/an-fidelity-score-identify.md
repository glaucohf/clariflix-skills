---
task-id: an-fidelity-score-identify
name: "Identify Clone Files & Run Script"
version: 1.0.0
execution_type: Worker
model: Haiku
model_rationale: "File identification and script execution are deterministic."
haiku_eligible: true
estimated-time: 5 min
complexity: low

inputs:
  required:
    - clone_path: "Path to the clone agent file"

outputs:
  primary:
    - clone_files: "Map of all clone-related files"
    - preflight_scores: "Scores from worker script"

worker_script: "scripts/fidelity-score.sh"
elicit: false
---

# Task: Identify Clone Files & Run Script

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-fidelity-score-identify` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

- **Parent Task:** `an-fidelity-score` (orchestrator stub)
- **Sequence:** Phase 1 of 3
- **Previous Task:** None
- **Next Task:** `an-fidelity-score-layers`

## Purpose

Locate all clone-related files and execute the worker script to generate deterministic preflight scores.

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-FS-001 | Preflight script must succeed | BLOCK - Do NOT proceed manually |

## Workflow / Steps

### Step 1: Locate Clone Files

1. Find the agent file (e.g., `.claude/agents/{clone}.md` or `squads/*/agents/{clone}.md`)
2. Identify supporting files:
   - `voice_dna` section
   - `thinking_dna` section
   - `heuristics` files
   - `artifacts` files

```yaml
clone_files:
  agent_file: "{path}"
  voice_dna_section: true|false
  thinking_dna_section: true|false
  heuristics_files: []
  artifacts_files: []
```

### Step 2: Run Worker Script (MANDATORY)

```bash
bash squads/squad-creator-pro/scripts/fidelity-score.sh <clone-path> > /tmp/preflight-fidelity-score.yaml
```

**IF command fails:** FIX the script error. Do NOT proceed manually.
**IF command succeeds:** READ `/tmp/preflight-fidelity-score.yaml`. Use ONLY these scores.

### Step 3: Validate Script Output

Confirm output file exists and contains valid YAML with scores for all 8 layers.

## Output

```yaml
clone_files: { file map }
preflight_scores: { parsed YAML from script }
```

## Acceptance Criteria

- [ ] Clone agent file located
- [ ] Supporting files identified
- [ ] Worker script executed successfully
- [ ] Preflight scores file exists and is valid YAML
- [ ] All 8 layers have scores in preflight output

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-fidelity-score.md` | Parent orchestrator |
| `an-fidelity-score-layers.md` | Next phase |
