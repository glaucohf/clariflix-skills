# Task: Sync IDE Command — Verify

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `sync-ide-command-verify` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: sync-ide-command-verify
name: "Sync IDE Command — Verify"
category: utility
agent: squad-chief
elicit: false
autonomous: true
description: "Valida os arquivos sincronizados e emite o resumo final por IDE."
```

## Purpose

Fechar a operação de sync com verificação de saída e resumo útil para o usuário.

## Acceptance Criteria

- [ ] Arquivos criados/atualizados validados
- [ ] Resumo final emitido
- [ ] Falhas por IDE ficaram explícitas

## Related Documents

- `sync-ide-command.md`
- `scripts/sync-ide-command.py`

---

_Task Version: 1.0.0_
