# Task: Optimize - Bias Test

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-bias-test` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-bias-test
name: "Optimize Bias Test"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Executa o teste bidirecional de viés para detectar se a task otimizada passou a favorecer alvos, contextos ou outputs específicos."
```

## Purpose

Evitar que a otimização introduza um viés operacional invisível. Esta task isola a parte 7b do monólito original.

## Inputs

```yaml
inputs:
  empirical_results:
    type: object
    required: true
  target_files:
    type: array
    required: true
```

## Workflow / Steps

### Step 1: Rodar alvos contrastantes

- Reexecutar a task otimizada em variações controladas.
- Coletar saídas comparáveis.

### Step 2: Detectar e registrar viés

- Marcar diferença sistemática indevida.
- Salvar bias report para revisão posterior.

## Output

```yaml
output:
  schema:
    bias_findings: []
    bias_report_paths: []
```

## Acceptance Criteria

- [ ] O teste usa ao menos dois alvos contrastantes quando aplicável
- [ ] Bias findings ficam serializados e reutilizáveis

## Related Documents

- `optimize.md`
- `optimize-empirical-validation.md`
