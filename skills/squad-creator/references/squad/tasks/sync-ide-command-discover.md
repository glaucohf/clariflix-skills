# Task: Sync IDE Command — Discover

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `sync-ide-command-discover` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: sync-ide-command-discover
name: "Sync IDE Command — Discover"
category: utility
agent: squad-chief
elicit: false
autonomous: true
description: "Localiza arquivos-fonte, calcula destinos e detecta conflitos antes da sincronização."
```

## Purpose

Gerar um plano explícito de sync, incluindo arquivos, IDEs e possíveis
sobrescritas.

## Acceptance Criteria

- [ ] Arquivos-fonte resolvidos
- [ ] Destinos calculados por IDE
- [ ] Conflitos e necessidade de `--force` explicitados

## Related Documents

- `sync-ide-command.md`
- `sync-ide-command-execute.md`

---

_Task Version: 1.0.0_
