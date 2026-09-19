---
name: "Full Data Quality Audit"
description: "Auditoria completa de qualidade de dados orquestrada pelo data-quality-reporter, do profiling à remediação em 5 fases: profiling (data-profiler), detecção de anomalias (anomaly-detector), validação de schema (schema-validator), relatório de qualidade com score composto (data-quality-reporter) e sugestão de remediação (remediation-suggester). A profundidade (quick, standard, deep) ajusta o rigor de cada fase."

inputs:
  - name: dataset
    type: string
    description: "Dataset para auditoria — do usuário"
    required: true
  - name: depth
    type: string
    description: "Profundidade da auditoria (quick, standard, deep)"
    required: false

outputs:
  - name: auditResult
    type: json
    description: "Resultado completo e consolidado da auditoria entregue ao usuário"
    required: true
  - name: profilingReport
    type: file
    description: "profiling-report.md gerado na fase de profiling"
    required: true
  - name: anomalyReport
    type: file
    description: "anomaly-report.md gerado na fase de detecção de anomalias"
    required: false
  - name: schemaReport
    type: file
    description: "schema-validation-report.md gerado na fase de validação de schema"
    required: false
  - name: qualityReport
    type: file
    description: "quality-report.md com o score composto por 6 dimensões"
    required: true
  - name: remediationPlan
    type: file
    description: "remediation-plan.md com correções priorizadas e scripts"
    required: false

acceptance_criteria:
  - blocker: true
    criteria: "Pipeline completo do profiling à remediação executado"
  - blocker: true
    criteria: "Score de qualidade calculado com 6 dimensões"
  - blocker: false
    criteria: "Scripts de correção prontos para execução"
---

# Full Data Quality Audit

## Pipeline

```
Fase 1: Profiling         → @data-profiler         → profileDataset()
Fase 2: Anomalias         → @anomaly-detector      → detectAnomalies()
Fase 3: Schema            → @schema-validator       → validateSchema()
Fase 4: Relatório         → @data-quality-reporter  → generateQualityReport()
Fase 5: Remediação        → @remediation-suggester  → suggestRemediation()
```

## Elicitation

### Fase 1 — Dataset
- "Qual o dataset ou tabela para auditar?"
- "Qual o formato dos dados? (CSV, Parquet, JSON, SQL table)"
- "Qual a profundidade desejada? (quick, standard, deep)"

### Fase 2 — Contexto
- "Há um schema esperado documentado?"
- "Existem regras de negócio específicas para validar?"
- "Há um baseline anterior para comparação?"

### Fase 3 — Remediação
- "Deseja gerar scripts de correção automatizados?"
- "Qual a linguagem preferida para scripts? (Python, SQL, dbt)"
- "Há restrições de janela de execução?"

## Profundidade da Auditoria

| Profundidade | Profiling | Anomalias | Schema | Relatório | Remediação |
|---|---|---|---|---|---|
| quick | Básico (nulls, types) | Rule-based only | Tipos e nulls | Standard | Críticos apenas |
| standard | Completo | Statistical + rules | Full + constraints | Detailed | Todos priorizados |
| deep | Deep (distribuições, correlações) | Statistical + ML | Full + referential | Executive + detailed | Todos + prevenção |

## Performance

- **Duração esperada:** 30-60 minutos
- **Custo estimado:** variável conforme o tamanho do dataset
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** escalate (retry máx. 2 tentativas, backoff exponencial base=10s, max=60s)
- **Fallback:** se qualquer fase falhar, continuar com as fases seguintes e reportar os gaps no relatório final
- **Notificação:** data-quality-reporter

## Dependencies

- profileDataset()
- detectAnomalies()
- validateSchema()
- generateQualityReport()
- suggestRemediation()
