# Task: Migrate Workflows to YAML (Stub)

**Task ID:** `migrate-workflows-to-yaml`
**Pattern:** HO-TP-001 (Task Anatomy Standard)
**Execution Type:** Hybrid (parsing/validation scripts + Agent for semantic conversion)
**Model:** `Sonnet` (requires understanding workflow semantics for proper conversion)
**Haiku Eligible:** NO

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Migrate Workflows to YAML |
| **status** | `active` |
| **responsible_executor** | @squad-chief |
| **execution_type** | `Hybrid` |
| **input** | Workflow .md files in any squad's workflows/ folder |
| **output** | Migrated .yaml files + archived .md files |
| **action_items** | 3 sub-tasks |
| **acceptance_criteria** | 3 criteria |

**Estimated Time:** 30min per workflow

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-MWY-001 | Dry-run output must be reviewed before conversion | Generate YAML preview and validate syntax before writing | VETO - BLOCK |
| VETO-MWY-002 | Original .md files must be archived before deletion | Verify _archive/ directory exists and originals are copied | VETO - BLOCK |
| VETO-MWY-003 | All cross-references must be identified before archiving | Grep for references to source .md filenames across tasks, workflows, config | VETO - BLOCK |

---

## Overview

Migrar workflows em formato `.md` (legacy/narrativo) para o formato `.yaml` padrao do AIOX.

**Motivacao:**

- Consistencia no ecossistema (todos workflows em .yaml)
- Parsing automatico por scripts de validacao
- Suporte a tooling (templates, linters, geradores)
- Validacao por schema

---

## Sub-Tasks (Atomic Execution)

| # | Sub-Task | File | Responsibility |
|---|----------|------|----------------|
| 1 | Analyze | `migrate-workflows-analyze.md` | Read .md workflows, extract structure, identify gaps vs YAML template |
| 2 | Convert + Validate | `migrate-workflows-convert.md` | Convert to YAML format, validate syntax and required fields |
| 3 | Archive + Cleanup | `migrate-workflows-archive.md` | Archive originals, update references, verify no broken links |

---

## Execution Flow

```
Step 1: migrate-workflows-analyze
  Input: .md workflow files + workflow-tmpl.yaml
  Output: structure map per workflow (fields, phases, gaps)

Step 2: migrate-workflows-convert
  Input: structure maps + workflow-tmpl.yaml
  Output: .yaml workflow files + validation results

Step 3: migrate-workflows-archive
  Input: validated .yaml files + original .md files
  Output: archived .md files + updated references
```

---

## Acceptance Criteria

- [ ] **AC1:** All workflows converted to .yaml with valid structure
- [ ] **AC2:** `workflows/` contains only .yaml files (except _archive/)
- [ ] **AC3:** Original files preserved in `workflows/_archive/`

---

## Quality Gate

```yaml
quality_gate:
  id: "QG_WF_MIGRATE_001"
  name: "Workflow Migration Quality Gate"
  placement: "exit"
  type: "automated"
  severity: "blocking"
  criteria:
    - check: "YAML syntax valid"
      weight: 3
    - check: "Required fields present"
      value: ["workflow-id", "name", "version", "phases"]
      weight: 3
    - check: "Each phase has checkpoint"
      weight: 2
  thresholds:
    pass: 8
    review: 6
    fail: 5
```

---

## Handoff

| Attribute | Value |
|-----------|-------|
| **Next Task** | `refresh-registry` |
| **Trigger** | Migration complete |
| **Executor** | @squad-chief |

---

_Task Version: 2.0.0_
_Atomized: 2026-03-26_
_Sub-tasks: migrate-workflows-analyze, migrate-workflows-convert, migrate-workflows-archive_
