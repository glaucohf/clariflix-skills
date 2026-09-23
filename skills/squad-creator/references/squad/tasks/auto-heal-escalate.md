# Task: Auto-Heal — Escalate

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `auto-heal-escalate` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: auto-heal-escalate
name: "Auto-Heal — Escalate"
category: runtime
agent: squad-chief
elicit: false
autonomous: true
description: "Prepara a escalada quando o fix automático não é seguro, não é suficiente ou já falhou repetidamente."
```

## Purpose

Produzir um handoff claro para ação humana ou investigação manual.

## Acceptance Criteria

- [ ] Escalada emitida quando fix não resolve ou é vetado
- [ ] Próximo passo fica claro
- [ ] Nível de escalada explicitado

## Related Documents

- `auto-heal.md`
- `auto-heal-persist.md`

---

_Task Version: 1.0.0_
