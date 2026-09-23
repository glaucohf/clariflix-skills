# Task: Squad Fusion - Cleanup

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-cleanup` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Human` |

## Metadata

```yaml
id: squad-fusion-cleanup
name: "Squad Fusion Cleanup"
category: fusion
agent: squad-chief
elicit: true
autonomous: false
description: "Executa a limpeza final opcional da fusão, respeitando quality gates, rollback path e confirmação humana para ações destrutivas."
```

## Purpose

Executar cleanup apenas quando a fusão estiver estável e houver confirmação apropriada para ações irreversíveis.

## Workflow / Steps

### Step 1: Verificar pré-condições

- Confirmar quality gates aprovados.
- Confirmar rollback path pronto.
- Respeitar `keep_sources`.

### Step 2: Executar cleanup opcional

- Arquivar ou remover squads fonte somente quando aprovado.
- Limpar workspace temporário e fechar o audit log.

## Output

```yaml
output:
  schema:
    sources_removed: []
    final_status: "completed | completed_with_sources_kept"
```

## Acceptance Criteria

- [ ] Cleanup nunca ocorre sem aprovação compatível com o modo
- [ ] Sources são preservados quando `keep_sources=true`
- [ ] O fechamento final mantém trilha de rollback
