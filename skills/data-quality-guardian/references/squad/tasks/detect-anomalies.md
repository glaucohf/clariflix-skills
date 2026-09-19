---
name: "Detect Anomalies"
description: "Detecção de anomalias conduzida pelo anomaly-detector: aplica detecção estatística (Z-score, IQR, MAD), verifica regras de negócio e domínio, compara distribuições com baseline, identifica data drift temporal, classifica cada anomalia por severidade (critical, warning, info) com evidência e localização, e gera o anomaly-report.md."

inputs:
  - name: dataset
    type: string
    description: "Dataset para análise — do usuário ou da task fullDataQualityAudit()"
    required: true
  - name: profilingReport
    type: file
    description: "profiling-report.md vindo da task profileDataset()"
    required: false
  - name: sensitivity
    type: string
    description: "Sensibilidade da detecção (low, medium, high)"
    required: false

outputs:
  - name: anomalyReport
    type: file
    description: "anomaly-report.md com evidências e classificação, enviado a data-quality-reporter e remediation-suggester"
    required: true
  - name: anomalyList
    type: array
    description: "Lista estruturada de anomalias detectadas (anomaly-list.json)"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Anomalias classificadas por severidade (critical, warning, info)"
  - blocker: true
    criteria: "Cada anomalia documentada com evidência e localização"
  - blocker: false
    criteria: "Taxa de falso positivo estimada"
---

# Detect Anomalies

## Flow

```
1. Receber dataset e relatório de profiling
2. Aplicar detecção estatística (Z-score, IQR, MAD)
3. Verificar regras de negócio e domínio
4. Comparar distribuições com baseline
5. Identificar data drift temporal
6. Classificar anomalias por severidade (critical, warning, info)
7. Documentar evidências para cada anomalia
8. Gerar anomaly-report.md
9. Enviar para @data-quality-reporter
```

## Elicitation

- "Qual o dataset para análise de anomalias?"
- "Qual a sensibilidade desejada? (low, medium, high)"
- "Há regras de negócio específicas para validar?"
- "Existe um baseline de referência para comparação?"

## Performance

- **Duração esperada:** 10-20 minutos
- **Custo estimado:** ~0 (análise local de dados)
- **Cacheável:** não
- **Paralelizável:** sim

## Error Handling

- **Estratégia:** retry (máx. 3 tentativas, backoff exponencial base=5s, max=30s)
- **Fallback:** se o profiling não estiver disponível, executar a detecção apenas com métodos rule-based
- **Notificação:** data-quality-reporter

## Dependencies

- profileDataset()
