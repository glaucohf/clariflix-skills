# Task: Optimize - Determinism Analysis

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-determinism-analysis` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-determinism-analysis
name: "Optimize Determinism Analysis"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Decompoe cada task em acoes atomicas e aplica o decision tree Q1-Q6 para recomendar Worker, Agent, Hybrid ou Human."
```

## Purpose

Executar a parte semanticamente crítica da otimização. Esta task transforma o conteúdo real das tasks em uma análise tabular auditável, sem classificar pelo nome do arquivo.

## Inputs

```yaml
inputs:
  inventory:
    type: object
    required: true
  decision_tree_loaded:
    type: boolean
    required: true
```

## Workflow / Steps

### Step 1: Decompor a task em ações

- Ler cada task alvo por completo.
- Extrair cada ação executável como linha separada.

### Step 2: Aplicar Q1-Q6 por ação

- Responder o fluxo completo do decision tree para cada ação.
- Classificar cada linha como `Worker`, `Agent`, `Hybrid` ou `Human`.

### Step 3: Agregar por task

- Calcular distribuição por executor.
- Sugerir classificação final da task.
- Listar justificativa e risco de erro de classificação.

## Output

```yaml
output:
  schema:
    analysis_table: []
    task_recommendations: []
    high_roi_targets: []
```

## Acceptance Criteria

- [ ] Nenhuma task é classificada só pelo filename
- [ ] Cada ação recebe resposta explícita para Q1-Q6
- [ ] O output identifica as melhores candidatas a Worker/Hybrid

## Related Documents

- `optimize.md`
- `optimize-scope-clarification.md`
- `squads/squad-creator/data/executor-decision-tree.md`
