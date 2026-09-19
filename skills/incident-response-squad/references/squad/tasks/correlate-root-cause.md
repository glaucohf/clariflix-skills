---
name: "Correlate Root Cause"
description: "Correlação de causa raiz conduzida pelo Correlator: recebe o relatório de análise de logs, coleta métricas de monitoramento, constrói o grafo de dependências, correlaciona anomalias de log com métricas temporalmente, identifica o ponto de origem da cascata de falhas, mapeia o blast radius (direto, first-order, second-order), calcula o confidence score e gera o root-cause-report.md com remediação sugerida para o runbook-executor."

inputs:
  - name: logAnalysisReport
    type: file
    description: "Relatório de análise de logs — do log-analyzer (analyzeIncidentLogs())"
    required: true
  - name: monitoringMetrics
    type: json
    description: "Métricas de monitoramento (Datadog, Prometheus, Grafana)"
    required: false
  - name: dependencyMap
    type: file
    description: "Mapa de dependências — documentação de arquitetura ou discovery automática"
    required: false

outputs:
  - name: rootCauseReport
    type: file
    description: "root-cause-report.md enviado a runbook-executor e postmortem-writer"
    required: true
  - name: blastRadiusAssessment
    type: json
    description: "Mapeamento de serviços afetados, para status-page-updater e postmortem-writer"
    required: true
  - name: confidenceScore
    type: number
    description: "Nível de confiança da hipótese de causa raiz, registrado no root-cause-report.md"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Causa raiz identificada com confidence score >= 50%"
  - blocker: true
    criteria: "Blast radius mapeado com serviços afetados listados"
  - blocker: false
    criteria: "Remediação sugerida vinculada a runbook existente"
---

# Correlate Root Cause

## Flow

```
1. Receber relatório de análise de logs do @log-analyzer
2. Coletar métricas de monitoramento relevantes
3. Construir/atualizar grafo de dependências
4. Correlacionar anomalias de log com métricas
5. Identificar ponto de origem da cascata de falhas
6. Mapear blast radius (direto, first-order, second-order)
7. Calcular confidence score baseado em evidências
8. Propor causa raiz e remediação sugerida
9. Gerar root-cause-report.md
10. Enviar relatório para @runbook-executor
```

## Correlação Multi-Ferramenta

### Fontes de Sinal

| Categoria | Ferramentas | Sinais |
|---|---|---|
| Métricas | Datadog, Prometheus, CloudWatch | CPU, memória, latência, error rate |
| Traces | Jaeger, X-Ray, Datadog APM | Distributed traces, latência por serviço |
| Logs | ELK, Splunk, CloudWatch Logs | Erros, exceções, padrões |
| Alertas | PagerDuty, OpsGenie | Timeline de alertas |
| Infra | Kubernetes, AWS, GCP | Events, health checks |

## Performance

- **Duração esperada:** 10-30 minutos
- **Custo estimado:** ~0 (consulta a ferramentas existentes)
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** escalate (retry máx. 2 tentativas, backoff exponencial base=10s, max=60s)
- **Fallback:** se a correlação for inconclusiva, escalar para engenharia sênior com os dados coletados
- **Notificação:** status-page-updater
