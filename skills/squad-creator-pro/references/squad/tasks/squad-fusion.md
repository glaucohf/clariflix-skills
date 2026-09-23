# Task: Squad Fusion (Composed)

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion` |
| **Version** | `2.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Composed` |

## Metadata

```yaml
id: squad-fusion
name: "Squad Fusion"
category: fusion
agent: squad-chief
elicit: true
autonomous: false
description: "Stub composto que preserva o entrypoint *squad-fusion e delega a execução real para o workflow canônico de fusão do pack pro."
```

## Purpose

Preservar o comando `*squad-fusion` sem manter o monólito anterior. A lógica real passa a viver em tasks atômicas ligadas ao `wf-squad-fusion.yaml`, que continua sendo o owner canônico do processo de fusão.

## Canonical Owner

- `workflows/wf-squad-fusion.yaml` é o owner canônico de `*squad-fusion`.

## Command Contract

```text
*squad-fusion

Flags:
--sources a,b,c
--target target-name
--mode yolo|quality
--dry-run
--keep-sources
--verbose
```

## Execution Sequence

| Seq | Task ID | File | Type | Phase |
|-----|---------|------|------|-------|
| 1 | `squad-fusion-initialize` | `tasks/squad-fusion-initialize.md` | Worker | Setup |
| 2 | `squad-fusion-discovery` | `tasks/squad-fusion-discovery.md` | Worker | Discovery |
| 3 | `squad-fusion-deduplication` | `tasks/squad-fusion-deduplication.md` | Agent | Dedup |
| 4 | `squad-fusion-scope` | `tasks/squad-fusion-scope.md` | Agent | Scope |
| 5 | `squad-fusion-collection` | `tasks/squad-fusion-collection.md` | Worker | Collection |
| 6 | `squad-fusion-validation` | `tasks/squad-fusion-validation.md` | Hybrid | Validation |
| 7 | `squad-fusion-structure` | `tasks/squad-fusion-structure.md` | Worker | Structure |
| 8 | `squad-fusion-integration` | `tasks/squad-fusion-integration.md` | Hybrid | Integration |
| 9 | `squad-fusion-command-sync` | `tasks/squad-fusion-command-sync.md` | Worker | Cmd Sync |
| 10 | `squad-fusion-cleanup` | `tasks/squad-fusion-cleanup.md` | Human | Cleanup |

## Mode Map

```yaml
mode_map:
  dry_run:
    run: [seq 1-4]  # Stops after scope -- no writes
  yolo:
    run: [seq 1-10] # Automatic checkpoints
  quality:
    run: [seq 1-10] # Human checkpoints at hybrid/human phases
```

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-SFU-001 | Fewer than 2 valid source squads | BLOCK |
| VETO-SFU-002 | No dry-run analysis before destructive merge | BLOCK |
| VETO-SFU-003 | No rollback path before writing | BLOCK |
| VETO-SFU-004 | Cleanup without quality gates pass | BLOCK |

## Quality Gates

| Gate ID | Name | Type |
|---------|------|------|
| SC_FUS_001 | Fusion Completeness | Blocking |
| SC_FUS_002 | Config Validity | Blocking |
| SC_FUS_003 | Documentation Quality | Recommended |

## Related Documents

- `workflows/wf-squad-fusion.yaml`
- `data/fusion-decision-points-analysis.md`
- `data/fusion-executor-analysis.md`
- `checklists/executor-matrix-checklist.md`
- `templates/config-tmpl.yaml`
- `templates/readme-tmpl.md`

_Task Version: 2.0.0_
_Role: composed stub orchestrating 10 atomic fusion sub-tasks_

## Acceptance Criteria

- [ ] All veto conditions checked and none triggered
- [ ] Output artifact produced: Completed squad-fusion output artifact
- [ ] Task output validated against quality standards
