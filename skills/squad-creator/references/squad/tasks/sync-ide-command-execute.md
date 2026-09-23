# Task: Sync IDE Command — Execute

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `sync-ide-command-execute` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: sync-ide-command-execute
name: "Sync IDE Command — Execute"
category: utility
agent: squad-chief
elicit: false
autonomous: true
description: "Executa o worker script de sync ou produz preview determinístico em modo dry-run."
worker_script: scripts/sync-ide-command.py
```

## Purpose

Executar o sync de forma determinística, sem embutir lógica de negócio extra fora
do worker.

## Acceptance Criteria

- [ ] Dry-run respeitado quando solicitado
- [ ] Worker script utilizado como executor canônico
- [ ] Resultado bruto de sync emitido

## Related Documents

- `sync-ide-command.md`
- `sync-ide-command-verify.md`

---

_Task Version: 1.0.0_
