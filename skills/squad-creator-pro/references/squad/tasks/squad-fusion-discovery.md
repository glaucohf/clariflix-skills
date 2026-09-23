# Task: Squad Fusion - Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-discovery` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: squad-fusion-discovery
name: "Squad Fusion Discovery"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Faz due diligence dos squads fonte, inventariando assets, contagens e referências cruzadas antes da deduplicação."
```

## Purpose

Produzir um inventário factual dos squads fonte para que nenhuma decisão de fusão dependa de memória ou suposição.

## Workflow / Steps

### Step 1: Inventariar cada fonte

- Listar agents, tasks, workflows, templates, checklists, data, scripts e config.
- Contar linhas e metadados mínimos por arquivo.

### Step 2: Consolidar visão global

- Produzir `inventory`, `total_assets` e `cross_references`.
- Destacar dependências cruzadas que precisam sobreviver à fusão.

## Output

```yaml
output:
  schema:
    inventory: {}
    total_assets: {}
    cross_references: []
```

## Acceptance Criteria

- [ ] Todos os squads fonte entram no inventário
- [ ] O inventário cobre assets e referências cruzadas
- [ ] O output é suficiente para deduplicação e filtragem
