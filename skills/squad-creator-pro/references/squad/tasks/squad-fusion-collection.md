# Task: Squad Fusion - Collection

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-collection` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: squad-fusion-collection
name: "Squad Fusion Collection"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Executa o ETL extract: copia componentes selecionados para o workspace temporário e registra provenance."
```

## Purpose

Montar o workspace de fusão sem tocar ainda no target final, preservando rastreabilidade completa do que foi coletado.

## Workflow / Steps

### Step 1: Copiar componentes aprovados

- Copiar assets de `final_components` para o workspace.
- Resolver conflitos físicos de nome e path.

### Step 2: Registrar provenance

- Produzir `workspace_contents`, `conflicts_resolved` e `provenance_map`.
- Garantir que cada asset do workspace aponte para sua origem.

## Output

```yaml
output:
  schema:
    workspace_contents: []
    conflicts_resolved: []
    provenance_map: {}
```

## Acceptance Criteria

- [ ] Só componentes aprovados entram no workspace
- [ ] Todo conflito resolvido fica registrado
- [ ] A provenance do merge fica preservada
