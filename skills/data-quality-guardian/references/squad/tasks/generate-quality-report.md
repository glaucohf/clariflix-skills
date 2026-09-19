---
name: "Generate Quality Report"
description: "Geração de relatório de qualidade conduzida pelo data-quality-reporter: recebe dados de profiling, anomalias e schema, calcula o score por dimensão e o score composto ponderado nas 6 dimensões (completude, acurácia, consistência, timeliness, unicidade, validade), compara com SLAs alertando violações, identifica tendências temporais, prioriza issues por impacto e gera o quality-report.md com sumário executivo."

inputs:
  - name: profilingData
    type: file
    description: "Dados de profiling vindos da task profileDataset()"
    required: true
  - name: anomalyData
    type: file
    description: "Dados de anomalias vindos da task detectAnomalies()"
    required: false
  - name: schemaData
    type: file
    description: "Dados de validação de schema vindos da task validateSchema()"
    required: false
  - name: format
    type: string
    description: "Formato do relatório (standard, executive, detailed)"
    required: false

outputs:
  - name: qualityReport
    type: file
    description: "quality-report.md com scores por dimensão, enviado a remediation-suggester e stakeholders"
    required: true
  - name: qualityScore
    type: json
    description: "Score composto e por dimensão (quality-score.json)"
    required: true

acceptance_criteria:
  - blocker: true
    criteria: "Score de qualidade calculado com 6 dimensões (completude, acurácia, consistência, timeliness, unicidade, validade)"
  - blocker: true
    criteria: "Violações de SLA identificadas e alertadas"
  - blocker: false
    criteria: "Tendência temporal incluída quando dados históricos disponíveis"
---

# Generate Quality Report

## Flow

```
1. Receber dados de profiling, anomalias e schema
2. Calcular score por dimensão de qualidade (6 dimensões)
3. Calcular score composto ponderado
4. Comparar com SLAs definidos
5. Identificar tendências temporais
6. Priorizar issues por impacto
7. Gerar sumário executivo
8. Formatar relatório final
9. Enviar para @remediation-suggester
```

## Elicitation

- "Qual o formato desejado do relatório? (standard, executive, detailed)"
- "Há SLAs de qualidade definidos para este dataset?"
- "Deseja incluir comparação com períodos anteriores?"
- "Quem são os stakeholders destinatários do relatório?"

## Performance

- **Duração esperada:** 5-15 minutos
- **Custo estimado:** ~0 (geração de relatório)
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** retry (máx. 2 tentativas, backoff exponencial base=5s, max=30s)
- **Fallback:** se os dados forem parciais, gerar o relatório com as dimensões disponíveis e marcar os gaps
- **Notificação:** remediation-suggester

## Dependencies

- profileDataset()
