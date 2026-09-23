# Task: Auto-Heal — Diagnose

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `auto-heal-diagnose` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: auto-heal-diagnose
name: "Auto-Heal — Diagnose"
category: runtime
agent: squad-chief
elicit: false
autonomous: true
description: "Classifica o erro, detecta padrão conhecido e decide se existe fix seguro."
```

## Purpose

Determinar categoria, severidade e estratégia inicial de remediação.

## Acceptance Criteria

- [ ] Erro classificado em categoria conhecida ou `UNKNOWN`
- [ ] `auto_fixable` decidido explicitamente
- [ ] Root cause resumida

## Related Documents

- `auto-heal.md`
- `auto-heal-fix.md`

---

_Task Version: 1.0.0_
