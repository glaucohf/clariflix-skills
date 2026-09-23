# Task: Auto-Heal — Fix

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `auto-heal-fix` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: auto-heal-fix
name: "Auto-Heal — Fix"
category: runtime
agent: squad-chief
elicit: false
autonomous: true
description: "Aplica somente correções seguras e dentro do escopo permitido pelo auto-heal."
```

## Purpose

Executar remediações seguras, sempre respeitando backups, limites e vetoes.

## Acceptance Criteria

- [ ] Fix só ocorre quando `auto_fixable=true`
- [ ] Backup exigido antes de modificação
- [ ] Resultado do fix emitido com status claro

## Related Documents

- `auto-heal.md`
- `auto-heal-escalate.md`

---

_Task Version: 1.0.0_
