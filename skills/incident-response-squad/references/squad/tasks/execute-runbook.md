---
name: "Execute Runbook"
description: "Execução de runbook de remediação conduzida pelo RunbookExec: recebe o root cause report, seleciona o runbook apropriado da biblioteca, valida pré-condições (permissões, acesso, estado do sistema), prepara o plano de rollback, executa os passos sequencialmente com logging, valida pós-condições e monitora métricas; em falha executa rollback e tenta alternativa, registrando tudo no execution-log.md e comunicando o status ao status-page-updater."

inputs:
  - name: rootCauseReport
    type: file
    description: "Root cause report com remediação sugerida — do root-cause-correlator (correlateRootCause())"
    required: true
  - name: runbookLibrary
    type: file
    description: "Biblioteca de runbooks do squad"
    required: false
  - name: environmentContext
    type: json
    description: "Configuração do ambiente (staging, production, região)"
    required: true

outputs:
  - name: executionLog
    type: file
    description: "execution-log.md com todas as ações executadas, para postmortem-writer"
    required: true
  - name: remediationStatus
    type: string
    description: "Status da remediação (resolved, partially_resolved, failed), para status-page-updater e postmortem-writer"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Runbook executado com todos os passos logados"
  - blocker: true
    criteria: "Status de remediação definido (resolved, partially_resolved, failed)"
  - blocker: false
    criteria: "Métricas de saúde confirmam melhoria"
---

# Execute Runbook

## Flow

```
1. Receber root cause report com remediação sugerida
2. Selecionar runbook apropriado da biblioteca
3. Validar pré-condições (permissões, acesso, estado do sistema)
4. Preparar plano de rollback
5. Executar passos do runbook sequencialmente
6. Validar pós-condição de cada passo
7. Monitorar métricas após execução
8. Se falhar, executar rollback e tentar alternativa
9. Registrar todas as ações no execution-log.md
10. Comunicar status para @status-page-updater
```

## Runbooks Disponíveis

| Runbook | Categoria | Tempo | Risco |
|---|---|---|---|
| `rollback_deploy` | Deploy | 5-15 min | Médio |
| `canary_rollback` | Deploy | 2-5 min | Baixo |
| `feature_flag_disable` | Deploy | 1-2 min | Baixo |
| `horizontal_scale_up` | Scaling | 5-10 min | Baixo |
| `restart_service` | Infra | 2-5 min | Médio |
| `restart_pod` | Infra | 1-3 min | Baixo |
| `failover_db` | Infra | 5-15 min | Alto |
| `clear_cache` | Infra | 1-2 min | Baixo |
| `dns_failover` | Network | 5-10 min | Alto |
| `circuit_breaker_open` | Network | 1 min | Médio |

## Performance

- **Duração esperada:** 5-30 minutos
- **Custo estimado:** variável conforme a ação (scaling pode ter custo de infra)
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** retry (máx. 2 tentativas, backoff exponencial base=10s, max=60s)
- **Fallback:** se a remediação falhar após 2 tentativas, escalar para engenharia e abrir circuit breaker
- **Notificação:** root-cause-correlator, status-page-updater
