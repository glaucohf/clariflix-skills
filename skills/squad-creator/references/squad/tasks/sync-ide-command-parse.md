# Task: Sync IDE Command — Parse

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `sync-ide-command-parse` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: sync-ide-command-parse
name: "Sync IDE Command — Parse"
category: utility
agent: squad-chief
elicit: false
autonomous: true
description: "Valida argumentos, flags e tipo de componente para a operação de sync."
```

## Purpose

Normalizar a chamada do comando antes de tocar configuração ou filesystem.

## Acceptance Criteria

- [ ] Tipo validado (`agent|task|workflow|squad`)
- [ ] Flags normalizadas
- [ ] Pedido de sync serializado

## Related Documents

- `sync-ide-command.md`
- `sync-ide-command-config.md`

---

_Task Version: 1.0.0_
