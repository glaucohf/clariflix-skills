# Task: Auto-Heal — Verify

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `auto-heal-verify` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: auto-heal-verify
name: "Auto-Heal — Verify"
category: runtime
agent: squad-chief
elicit: false
autonomous: true
description: "Reexecuta checks pós-fix, decide rollback quando necessário e fecha o veredito do auto-heal."
```

## Purpose

Garantir que o auto-heal não deixa correções parciais ou regressões em aberto.

## Acceptance Criteria

- [ ] Retry ou validação pós-fix executado
- [ ] Política de rollback aplicada quando necessário
- [ ] Veredito final emitido

## Related Documents

- `auto-heal.md`
- `templates/auto-heal-task-tmpl.md`

---

_Task Version: 1.0.0_
