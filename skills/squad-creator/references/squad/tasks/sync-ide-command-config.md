# Task: Sync IDE Command — Config

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `sync-ide-command-config` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: sync-ide-command-config
name: "Sync IDE Command — Config"
category: utility
agent: squad-chief
elicit: false
autonomous: true
description: "Carrega .aiox-sync.yaml, resolve IDEs ativas e aliases necessários para o sync."
```

## Purpose

Produzir a configuração efetiva da sincronização sem misturar isso com descoberta
de arquivos ou execução.

## Acceptance Criteria

- [ ] Configuração carregada
- [ ] IDEs ativas resolvidas
- [ ] Aliases e comportamento de log definidos

## Related Documents

- `sync-ide-command.md`
- `sync-ide-command-discover.md`

---

_Task Version: 1.0.0_
