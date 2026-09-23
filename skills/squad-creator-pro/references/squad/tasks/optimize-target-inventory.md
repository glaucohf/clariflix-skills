# Task: Optimize - Target Inventory

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-target-inventory` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: optimize-target-inventory
name: "Optimize Target Inventory"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Carrega o framework de decisao, resolve o target e produz o inventario factual que abastece toda a otimizacao."
```

## Purpose

Resolver `target`, `mode` e `focus` em um inventário determinístico. Esta task existe para impedir que a otimização comece por intuição ou por nome de arquivo.

## Inputs

```yaml
inputs:
  target:
    type: string
    required: true
  mode:
    type: string
    required: false
    default: scan
  focus:
    type: string
    required: false
    default: tasks
```

## Workflow / Steps

### Step 1: Carregar dependências obrigatórias

- Ler `squads/squad-creator/data/executor-decision-tree.md` por completo.
- Confirmar que o operador sabe aplicar Q1-Q6 literalmente.

### Step 2: Resolver o target

- Se `target` for arquivo, operar em uma task específica.
- Se `target` for nome de squad, listar `tasks/*.md` do squad.
- Se `target = all`, listar tasks de todos os squads elegíveis e excluir o meta-squad.

### Step 3: Inventariar artefatos e restrições

- Registrar arquivos alvo, tamanho, tipo e execution_type atual.
- Marcar se o modo exige backup prévio (`implement` ou `hybrid`).
- Emitir inventário reutilizável pelas phases seguintes.

## Output

```yaml
output:
  schema:
    resolved_scope: "single-task | squad | all"
    target_files: []
    current_execution_types: []
    decision_tree_loaded: true
    backups_required: true
```

## Acceptance Criteria

- [ ] O target é resolvido sem ambiguidade
- [ ] O decision tree foi carregado antes de qualquer classificação
- [ ] O inventário lista arquivos, escopo e pré-condições do modo

## Related Documents

- `optimize.md`
- `optimize-determinism-analysis.md`
- `squads/squad-creator/data/executor-decision-tree.md`
