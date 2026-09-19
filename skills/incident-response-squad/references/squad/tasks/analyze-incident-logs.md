---
name: "Analyze Incident Logs"
description: "Análise de logs de incidente conduzida pelo LogAnalyzer: identifica fontes relevantes, agrega logs na janela de tempo, normaliza timestamps para UTC, estabelece o baseline normal, detecta anomalias (error spikes, padrões incomuns), extrai stack traces e mensagens de erro relevantes, prioriza anomalias por severidade e gera o log-analysis-report.md para o root-cause-correlator."

inputs:
  - name: incidentAlert
    type: string
    description: "Descrição do alerta — do usuário ou da task fullIncidentResponse()"
    required: true
  - name: timeWindow
    type: string
    description: "Janela de tempo para análise (ex: 30m, 1h, 6h)"
    required: true
  - name: logSources
    type: array
    description: "Fontes de log a consultar (cloudwatch, elk, splunk, datadog)"
    required: false

outputs:
  - name: logAnalysisReport
    type: file
    description: "log-analysis-report.md enviado ao root-cause-correlator"
    required: true
  - name: anomalyList
    type: array
    description: "Lista estruturada de anomalias detectadas, para root-cause-correlator e postmortem-writer"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Ao menos uma fonte de log analisada com dados relevantes"
  - blocker: true
    criteria: "Anomalias identificadas com timestamps e fonte"
  - blocker: false
    criteria: "Correlação entre múltiplas fontes de log"
---

# Analyze Incident Logs

## Flow

```
1. Receber alerta e definir janela de tempo
2. Identificar fontes de log relevantes
3. Agregar logs de cada fonte na janela de tempo
4. Normalizar timestamps entre fontes (UTC)
5. Identificar baseline de operação normal
6. Detectar anomalias (error spikes, padrões incomuns)
7. Extrair stack traces e mensagens de erro relevantes
8. Priorizar anomalias por severidade e relevância
9. Gerar log-analysis-report.md
10. Enviar relatório para @root-cause-correlator
```

## Elicitation

- "Qual o alerta ou descrição do incidente?"
- "Há quanto tempo o problema começou? (janela de tempo)"
- "Quais fontes de log devem ser consultadas? (CloudWatch, ELK, Splunk, Datadog)"
- "Há algum serviço ou componente específico suspeito?"

## Performance

- **Duração esperada:** 5-15 minutos
- **Custo estimado:** ~0 (consulta a ferramentas existentes)
- **Cacheável:** não
- **Paralelizável:** sim

## Error Handling

- **Estratégia:** retry (máx. 3 tentativas, backoff exponencial base=5s, max=30s)
- **Fallback:** se uma fonte de log estiver indisponível, usar fontes alternativas disponíveis
- **Notificação:** root-cause-correlator
