# Task: Optimize Squad/Task Execution (Composed)

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize` |
| **Version** | `5.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Composed` |

## Metadata

```yaml
id: optimize
name: "Optimize Squad/Task Execution"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Stub composto que preserva o entrypoint *optimize e orquestra as subtasks atomicas de analise, conversao, validacao e economia."
```

## Purpose

Preservar retrocompatibilidade do comando `*optimize` enquanto a lógica real passa a viver em subtasks especializadas. Este arquivo continua sendo o owner do entrypoint, mas não volta a concentrar a implementação inteira.

## Command Contract

```text
*optimize {target}

Flags:
--scan        Executa apenas análise e relatório inicial
--implement   Executa análise + conversões estruturais
--hybrid      Executa o pipeline completo até validação empírica
--post        Recalcula economia a partir de artefatos já gerados
--exec N      Ajusta projeção de economia
```

## Mode Map

```yaml
mode_map:
  scan:
    run:
      - optimize-target-inventory
      - optimize-determinism-analysis
      - optimize-scope-clarification
      - optimize-gatekeeper-detection
      - optimize-roi-report
  implement:
    run:
      - optimize-target-inventory
      - optimize-determinism-analysis
      - optimize-scope-clarification
      - optimize-gatekeeper-detection
      - optimize-roi-report
      - optimize-binary-checkpoints
      - optimize-hybrid-executor
      - optimize-gap-zero
  hybrid:
    run:
      - optimize-target-inventory
      - optimize-determinism-analysis
      - optimize-scope-clarification
      - optimize-gatekeeper-detection
      - optimize-roi-report
      - optimize-binary-checkpoints
      - optimize-hybrid-executor
      - optimize-gap-zero
      - optimize-empirical-validation
      - optimize-bias-test
      - optimize-post-economy
  post:
    run:
      - optimize-post-economy
```

## Execution Sequence

| Sequence | Task ID | File | Type |
|----------|---------|------|------|
| 1 | `optimize-target-inventory` | `tasks/optimize-target-inventory.md` | Worker |
| 2 | `optimize-determinism-analysis` | `tasks/optimize-determinism-analysis.md` | Agent |
| 3 | `optimize-scope-clarification` | `tasks/optimize-scope-clarification.md` | Agent |
| 4 | `optimize-gatekeeper-detection` | `tasks/optimize-gatekeeper-detection.md` | Agent |
| 5 | `optimize-roi-report` | `tasks/optimize-roi-report.md` | Worker |
| 6 | `optimize-binary-checkpoints` | `tasks/optimize-binary-checkpoints.md` | Agent |
| 7 | `optimize-hybrid-executor` | `tasks/optimize-hybrid-executor.md` | Agent |
| 8 | `optimize-gap-zero` | `tasks/optimize-gap-zero.md` | Agent |
| 9 | `optimize-empirical-validation` | `tasks/optimize-empirical-validation.md` | Worker |
| 10 | `optimize-bias-test` | `tasks/optimize-bias-test.md` | Worker |
| 11 | `optimize-post-economy` | `tasks/optimize-post-economy.md` | Worker |

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `target` | string | Yes | Task file, squad name ou `all` |
| `mode` | string | No | `scan`, `implement`, `hybrid` ou `post` |
| `exec` | number | No | Volume de execuções para projeção |

## Outputs

| Output | Description |
|--------|-------------|
| Determinism Analysis | Análise Q1-Q6 por task e por ação |
| ROI Report | Matriz de prioridade e economia projetada |
| Patch Plans | Conversões binárias, hybrid e GAP ZERO |
| Final Economy Report | Before/after consolidado |

## Veto Conditions

- Não iniciar classificação sem ler `squads/squad-creator/data/executor-decision-tree.md`
- Não propor mudança destrutiva em `--implement` ou `--hybrid` sem backup requirement explícito
- Não fechar `--hybrid` sem validação empírica e bias test

## Notes

- `wf-optimize-squad.yaml` passa a compor estas subtasks com `task_ref`.
- `wf-optimize-yolo.yaml` continua owner do ciclo autônomo de alto nível e pode reutilizar estas mesmas subtasks por referência.
- Este arquivo substitui o monólito anterior por contrato de composição.

## Acceptance Criteria

- [ ] `*optimize` continua compatível para chamadores atuais
- [ ] O modo de execução escolhe o subconjunto correto de subtasks
- [ ] A implementação detalhada foi movida para tasks atômicas

## Related Documents

- `workflows/wf-optimize-squad.yaml`
- `workflows/wf-optimize-yolo.yaml`
- `checklists/quality-gate-checklist.md`

_Task Version: 5.0.0_
_Role: compatibility stub for atomic optimization pipeline_
