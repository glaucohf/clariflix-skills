# Task: Upgrade Squad - Apply

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `upgrade-squad-apply` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: upgrade-squad-apply
name: "Upgrade Squad Apply"
category: upgrade
agent: squad-chief
elicit: false
autonomous: true
description: "Executa primeiro o apply estrutural herdado do base e depois incorpora apenas os patches qualitativos aprovados ou placeholders explícitos."
```

## Purpose

Aplicar o plano aprovado sem duplicar a lógica do base:
- estrutural -> usar o baseline de `squads/squad-creator/tasks/upgrade-squad-apply.md`
- qualitativo -> aplicar somente o que veio em `apply_now` ou inserir TODO/handoff explícito

## Workflow / Steps

### Step 1: Rodar o apply estrutural herdado

- Ler `squads/squad-creator/tasks/upgrade-squad-apply.md`.
- Preservar `backup`, `dry-run`, validação por arquivo e `upgrade_log`.

### Step 2: Mesclar a trilha qualitativa aprovada

- Aplicar apenas patches marcados como `apply_now`.
- Inserir TODOs/handoffs onde o plano qualitativo mandou adiar.
- Nunca eliminar o backup/restore do baseline estrutural.

## Output

```yaml
output:
  schema:
    upgrade_log: {}
    qualitative_applied: []
    qualitative_deferred: []
```

## Acceptance Criteria

- [ ] O apply estrutural do base continua intacto
- [ ] Todo patch qualitativo aplicado veio de plano aprovado
- [ ] TODOs e handoffs diferidos ficam registrados no log final

## Related Documents

- `squads/squad-creator/tasks/upgrade-squad-apply.md`
- `upgrade-squad-verify.md`
