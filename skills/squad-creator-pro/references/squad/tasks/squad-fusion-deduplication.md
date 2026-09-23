# Task: Squad Fusion - Deduplication

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-deduplication` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: squad-fusion-deduplication
name: "Squad Fusion Deduplication"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Resolve entidades duplicadas e decide registros canônicos com base em função real, qualidade e provenance."
```

## Purpose

Identificar duplicatas semânticas e criar uma visão canônica do que deve permanecer, ser fundido ou ser excluído.

## Workflow / Steps

### Step 1: Detectar colisões reais

- Comparar nomes, função, outputs e dependências dos assets.
- Diferenciar duplicata real de variante complementar.

### Step 2: Definir golden records

- Escolher versão canônica por qualidade, completude e aderência ao target.
- Produzir listas `agents_to_keep` e `agents_to_exclude`.

## Output

```yaml
output:
  schema:
    duplicates_found: []
    duplicates_resolved: []
    assets_to_keep: []
    assets_to_exclude: []
```

## Acceptance Criteria

- [ ] Duplicatas são resolvidas por semântica, não só por nome
- [ ] Toda exclusão tem provenance
- [ ] O output pode ser consumido pela fase de escopo
