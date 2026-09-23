# Task: Optimize Workflow Execution (Composed)

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow` |
| **Version** | `2.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Composed` |

## Metadata

```yaml
id: optimize-workflow
name: "Optimize Workflow Execution"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Stub composto que preserva o entrypoint *optimize-workflow e delega a análise e implementação ao workflow canônico do pack."
```

## Purpose

Preservar compatibilidade do comando `*optimize-workflow` e dos chamadores internos do pack enquanto a lógica detalhada passa a viver em tasks atômicas orquestradas por workflow dedicado.

## Canonical Owner

- `workflows/wf-optimize-workflow.yaml` é o owner canônico do fluxo de otimização de workflows no `squad-creator-pro`.

## Command Contract

```text
*optimize-workflow {target}

Flags:
--scan        Executa apenas análise
--implement   Aplica as otimizações aprovadas
--cost N      Ajusta a projeção mensal
--verbose     Amplia o relatório por fase
```

## Execution Sequence

| Sequence | Task ID | File | Type |
|----------|---------|------|------|
| 1 | `optimize-workflow-load` | `tasks/optimize-workflow-load.md` | Worker |
| 2 | `optimize-workflow-phase-necessity` | `tasks/optimize-workflow-phase-necessity.md` | Agent |
| 3 | `optimize-workflow-parallelization` | `tasks/optimize-workflow-parallelization.md` | Agent |
| 4 | `optimize-workflow-checkpoints` | `tasks/optimize-workflow-checkpoints.md` | Agent |
| 5 | `optimize-workflow-executor-distribution` | `tasks/optimize-workflow-executor-distribution.md` | Agent |
| 6 | `optimize-workflow-gap-zero` | `tasks/optimize-workflow-gap-zero.md` | Agent |
| 7 | `optimize-workflow-cost-projection` | `tasks/optimize-workflow-cost-projection.md` | Worker |
| 8 | `optimize-workflow-report` | `tasks/optimize-workflow-report.md` | Worker |
| 9 | `optimize-workflow-apply` | `tasks/optimize-workflow-apply.md` | Agent |
| 10 | `optimize-workflow-validate` | `tasks/optimize-workflow-validate.md` | Worker |

## Mode Map

```yaml
mode_map:
  scan:
    run:
      - optimize-workflow-load
      - optimize-workflow-phase-necessity
      - optimize-workflow-parallelization
      - optimize-workflow-checkpoints
      - optimize-workflow-executor-distribution
      - optimize-workflow-gap-zero
      - optimize-workflow-cost-projection
      - optimize-workflow-report
  implement:
    run:
      - optimize-workflow-load
      - optimize-workflow-phase-necessity
      - optimize-workflow-parallelization
      - optimize-workflow-checkpoints
      - optimize-workflow-executor-distribution
      - optimize-workflow-gap-zero
      - optimize-workflow-cost-projection
      - optimize-workflow-report
      - optimize-workflow-apply
      - optimize-workflow-validate
```

## Veto Conditions

- Não aplicar `--implement` sem backup
- Não aplicar `--implement` sem relatório de scan
- Não fechar a execução sem validação estrutural do YAML final

## Acceptance Criteria

- [ ] `*optimize-workflow` continua compatível para os chamadores atuais
- [ ] A lógica detalhada sai do monólito e vai para tasks atômicas
- [ ] O fluxo canônico do pack fica explicitado em `wf-optimize-workflow.yaml`

## Related Documents

- `workflows/wf-optimize-workflow.yaml`
- `tasks/optimize.md`
- `workflows/wf-optimize-squad.yaml`

_Task Version: 2.0.0_
_Role: compatibility stub for atomic workflow-optimization pipeline_
