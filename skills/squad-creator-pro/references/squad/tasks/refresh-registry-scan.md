---
task-id: refresh-registry-scan
name: "Run Script & Collect Data"
version: 1.0.0
execution_type: Worker
model: Haiku
model_rationale: "Deterministic script execution. No LLM judgment needed."
haiku_eligible: true
estimated-time: 5 min
complexity: low

inputs:
  required: []
  optional:
    - squads_path: "Base path to scan (default: squads/)"

outputs:
  primary:
    - script_output: "Structured JSON with counts, config metadata, agent names"

worker_script: "scripts/refresh-registry.py"
elicit: false
---

# Task: Run Script & Collect Data

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `refresh-registry-scan` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

- **Parent Task:** `refresh-registry` (orchestrator stub)
- **Sequence:** Phase 1 of 3
- **Previous Task:** None
- **Next Task:** `refresh-registry-enrich`

## Purpose

Execute the deterministic Python script to scan all squads and collect factual data: counts, config metadata, agent names, executor profiles.

## Workflow / Steps

### Step 1: Run Python Script

```bash
python3 squads/squad-creator-pro/scripts/refresh-registry.py --output json --registry-format
```

### Step 2: Validate Script Output

Confirm output contains:

```json
{
  "metadata": {
    "scan_date": "ISO-8601",
    "total_squads": 0
  },
  "squads": {
    "{squad-name}": {
      "path": "squads/{squad-name}/",
      "version": "X.Y.Z",
      "description": "...",
      "counts": {
        "agents": 0,
        "tasks": 0,
        "workflows": 0,
        "templates": 0,
        "checklists": 0,
        "data_files": 0
      },
      "agent_names": [],
      "domain": "_TO_BE_INFERRED_",
      "keywords": [],
      "highlights": [],
      "example_use": ""
    }
  },
  "summary": {
    "total_agents": 0,
    "total_tasks": 0,
    "total_workflows": 0
  }
}
```

**What script does (deterministic):**
- Scans `squads/` directory
- Reads each `config.yaml`
- Counts files in each subdirectory
- Lists agent names
- Checks for README.md, CHANGELOG.md
- Validates YAML syntax
- Extracts `executor_profile` from each agent
- Builds `executor_capable_agents` and `executor_reviewers` lists
- Aggregates `work_contexts` keywords per squad
- Emits WARNING for squads without executor_profile

**What script does NOT do:**
- Infer domain category
- Extract keywords
- Generate highlights
- Generate example_use

## Output

```yaml
script_output: { JSON as above }
```

## Acceptance Criteria

- [ ] Script executes without errors
- [ ] JSON output is valid and parseable
- [ ] All squads in squads/ are represented
- [ ] Counts match actual file system state

## Related Documents

| Document | Relationship |
|----------|-------------|
| `refresh-registry.md` | Parent orchestrator |
| `refresh-registry-enrich.md` | Next phase |
