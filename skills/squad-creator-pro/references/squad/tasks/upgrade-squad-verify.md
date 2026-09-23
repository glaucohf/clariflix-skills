# Task: Upgrade Squad - Verify

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `upgrade-squad-verify` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: upgrade-squad-verify
name: "Upgrade Squad Verify"
category: upgrade
agent: squad-chief
elicit: false
autonomous: true
description: "Reusa a verificação estrutural do base e separa claramente o que ficou pendente por decisão qualitativa do overlay."
```

## Purpose

Executar a verificação final sem misturar as camadas:
- score e integridade estrutural continuam vindo do base
- pendências qualitativas ficam visíveis como follow-up, não como regressão silenciosa

## Workflow / Steps

### Step 1: Rodar a verificação estrutural herdada

- Ler `squads/squad-creator/tasks/upgrade-squad-verify.md`.
- Recalcular after-score e report estrutural no formato canônico.

### Step 2: Anexar o residual qualitativo

- Separar `remaining_todos.structural` de `remaining_todos.qualitative`.
- Reforçar os handoffs recomendados (`extract-voice-dna`, `extract-thinking-dna`, etc.).

## Output

```yaml
output:
  schema:
    structural_report: {}
    qualitative_followups:
      remaining_todos: []
      handoffs: []
```

## Acceptance Criteria

- [ ] A verificação estrutural continua ancorada no task canônico do base
- [ ] Pendências qualitativas não são escondidas nem tratadas como “resolvidas”
- [ ] O report final deixa claro o próximo handoff por item

## Related Documents

- `squads/squad-creator/tasks/upgrade-squad-verify.md`
- `upgrade-squad.md`
