---
name: "Profile Dataset"
description: "Profiling de dataset conduzido pelo data-profiler: identifica o formato, infere ou carrega o schema, calcula estatísticas descritivas por coluna (count, nulls, unique, min/max/mean/median/std, percentis), analisa distribuições, identifica tipos inconsistentes, estabelece o baseline de qualidade e gera o profiling-report.md para 100% das colunas."

inputs:
  - name: dataset
    type: string
    description: "Caminho ou referência do dataset — do usuário ou da task fullDataQualityAudit()"
    required: true
  - name: format
    type: string
    description: "Formato dos dados (csv, parquet, json, sql); detectado se omitido"
    required: false
  - name: depth
    type: string
    description: "Profundidade do profiling (quick, standard, deep)"
    required: false

outputs:
  - name: profilingReport
    type: file
    description: "profiling-report.md com estatísticas por coluna, enviado a anomaly-detector, schema-validator e data-quality-reporter"
    required: true
  - name: columnStats
    type: json
    description: "Estatísticas estruturadas por coluna enviadas a anomaly-detector e data-quality-reporter"
    required: true
  - name: baselineProfile
    type: json
    description: "Baseline de qualidade persistido para comparações futuras (baseline-profile.json)"
    required: false

acceptance_criteria:
  - blocker: true
    criteria: "100% das colunas profiladas com tipo, nulls e distribuição"
  - blocker: true
    criteria: "Estatísticas descritivas para colunas numéricas (min, max, mean, median, std)"
  - blocker: false
    criteria: "Comparação com baseline anterior quando disponível"
---

# Profile Dataset

## Flow

```
1. Receber dataset e identificar formato
2. Inferir ou carregar schema existente
3. Calcular estatísticas por coluna (count, nulls, unique)
4. Analisar distribuições para colunas numéricas
5. Calcular taxas de nulos e unicidade
6. Identificar tipos de dados inconsistentes
7. Estabelecer baseline de qualidade
8. Gerar profiling-report.md
9. Enviar para @anomaly-detector
```

## Elicitation

- "Qual o dataset ou caminho para profilar?"
- "Qual o formato dos dados? (CSV, Parquet, JSON, SQL table)"
- "Qual a profundidade desejada? (quick, standard, deep)"
- "Há um baseline anterior para comparação?"

## Performance

- **Duração esperada:** 5-15 minutos
- **Custo estimado:** ~0 (análise local de dados)
- **Cacheável:** sim
- **Paralelizável:** sim

## Error Handling

- **Estratégia:** retry (máx. 3 tentativas, backoff exponencial base=5s, max=30s)
- **Fallback:** se o dataset estiver inacessível, solicitar caminho alternativo ou formato diferente
- **Notificação:** data-quality-reporter
