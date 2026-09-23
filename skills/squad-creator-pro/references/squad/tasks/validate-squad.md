# Task: Validate Squad (Composed)

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad` |
| **Version** | `4.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Composed` |

## Metadata

```yaml
id: validate-squad
name: "Validate Squad"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Task composta que orquestra 9 subtasks atômicas de validação para squads pro e permanece local como override legítimo do pack."
```

## Purpose

Executar a validação completa de um squad pro em nove etapas atômicas, preservando retrocompatibilidade do comando `*validate-squad` e separando claramente gates deterministas, análise semântica, vetos e emissão de relatório.

Ao contrário de outros shadows redundantes do pack, este arquivo **deve permanecer local**: o `squad-creator-pro` usa uma sequência de 9 subtasks e um workflow próprio (`workflows/validate-squad.yaml`) que não equivale ao modelo de 7 etapas do base.

## Execution Sequence

```text
INPUT (squad_name)
  |
[1] validate-squad-type-detect
  |
[2] validate-squad-structure
  |
[3] validate-squad-security
  |
[4] validate-squad-coverage
  |
[5] validate-squad-cross-references
  |
[6] validate-squad-quality
  |
[7] validate-squad-contextual
  |
[8] validate-squad-veto
  |
[9] validate-squad-report
  |
OUTPUT: Validation report + final score
```

## Sub-Task References

| Sequence | Task ID | File | Type |
|----------|---------|------|------|
| 1 | `validate-squad-type-detect` | `tasks/validate-squad-type-detect.md` | Worker |
| 2 | `validate-squad-structure` | `tasks/validate-squad-structure.md` | Worker |
| 3 | `validate-squad-security` | `tasks/validate-squad-security.md` | Worker |
| 4 | `validate-squad-coverage` | `tasks/validate-squad-coverage.md` | Worker |
| 5 | `validate-squad-cross-references` | `tasks/validate-squad-cross-references.md` | Worker |
| 6 | `validate-squad-quality` | `tasks/validate-squad-quality.md` | Agent |
| 7 | `validate-squad-contextual` | `tasks/validate-squad-contextual.md` | Agent |
| 8 | `validate-squad-veto` | `tasks/validate-squad-veto.md` | Worker |
| 9 | `validate-squad-report` | `tasks/validate-squad-report.md` | Worker |

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `squad_name` | string | Yes | Name of squad to validate |
| `squad_path` | string | No | Override default path |
| `type_override` | string | No | Force detected type |
| `mode` | string | No | `deep` or `quick` |

## Outputs

| Output | Location |
|--------|----------|
| Validation Report | `{squad_path}/docs/validation-report-{date}.md` |
| JSON Report | `{squad_path}/docs/validation-report-{date}.json` |
| Console Summary | stdout |

## Notes

- Este arquivo agora funciona como stub composto de retrocompatibilidade.
- A lógica detalhada foi movida para subtasks atômicas.
- O workflow `workflows/validate-squad.yaml` deve referenciar estas subtasks explicitamente.
- Este é um override legítimo do pack, não uma cópia acidental do base.

## Related Documents

| Reference | File |
|-----------|------|
| Workflow | `workflows/validate-squad.yaml` |
| Checklist | `checklists/squad-checklist.md` |
| Type Definitions | `squads/squad-creator/data/squad-type-definitions.yaml` |
| Quality Framework | `data/quality-dimensions-framework.md` |

## Acceptance Criteria

- [ ] Output artifact produced: Location
- [ ] Task output validated against quality standards
