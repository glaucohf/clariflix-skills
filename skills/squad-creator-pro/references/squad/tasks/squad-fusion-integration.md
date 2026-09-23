# Task: Squad Fusion - Integration

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-integration` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: squad-fusion-integration
name: "Squad Fusion Integration"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Executa smoke tests e valida se o squad fusionado está operacional antes da sincronização de comandos e cleanup."
```

## Purpose

Confirmar que o squad recém-criado é realmente utilizável antes de qualquer etapa irreversível.

## Workflow / Steps

### Step 1: Testar operação do squad

- Rodar checks mínimos de estrutura, entrada, comandos e rotas internas.
- Identificar regressões causadas pela fusão.

### Step 2: Emitir relatório de integração

- Produzir `test_status` e `test_report`.
- Bloquear cleanup quando houver falha crítica.

## Output

```yaml
output:
  schema:
    test_status: "pass | warn | fail"
    test_report: markdown
```

## Acceptance Criteria

- [ ] O squad fusionado é testado antes do cleanup
- [ ] Falhas críticas impedem avanço
- [ ] O report de integração é legível e acionável
