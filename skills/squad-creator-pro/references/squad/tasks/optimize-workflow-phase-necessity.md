# Task: Optimize Workflow - Phase Necessity

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-phase-necessity` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-workflow-phase-necessity
name: "Optimize Workflow Phase Necessity"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Classifica fases como essential, redundant ou merge_candidate com base em output único, impacto de remoção e consumo downstream."
```

## Purpose

Executar a dimensão D1. Esta task mede quanto do workflow é realmente necessário antes de qualquer paralelização ou refactor.

## Inputs

```yaml
inputs:
  workflow_files:
    type: array
    required: true
```

## Workflow / Steps

### Step 1: Decompor fases

- Extrair nome, propósito, inputs, outputs, dependências e agente por fase.

### Step 2: Classificar contribuição

- `ESSENTIAL`: output único e necessário.
- `REDUNDANT`: não produz output útil nem quebra o fluxo.
- `MERGE_CANDIDATE`: agrega pouco e pode ser absorvida por outra fase.

## Output

```yaml
output:
  schema:
    phase_necessity_table: []
    redundant_candidates: []
    merge_candidates: []
```

## Acceptance Criteria

- [ ] Cada fase recebe classificação objetiva
- [ ] O output diferencia remoção de merge

## Related Documents

- `optimize-workflow.md`
- `optimize-workflow-parallelization.md`
