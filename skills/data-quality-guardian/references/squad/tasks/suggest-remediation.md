---
name: "Suggest Remediation"
description: "Sugestão de remediação conduzida pelo remediation-suggester: analisa os problemas do relatório de qualidade por categoria (dados, schema, pipeline, governança), prioriza por impacto x esforço, gera scripts de limpeza automatizados (Python, SQL, dbt), define correções manuais quando necessário, recomenda políticas de governança e prevenção de causa raiz, e gera o remediation-plan.md."

inputs:
  - name: qualityReport
    type: file
    description: "quality-report.md vindo da task generateQualityReport()"
    required: true
  - name: priority
    type: string
    description: "Foco de remediação (critical-only, all, preventive)"
    required: false

outputs:
  - name: remediationPlan
    type: file
    description: "remediation-plan.md priorizado, enviado à equipe de dados"
    required: true
  - name: cleaningScripts
    type: array
    description: "Scripts de limpeza prontos para execução"
    required: false
  - name: governanceRecommendations
    type: array
    description: "Políticas de governança recomendadas para o time de governança"
    required: false

acceptance_criteria:
  - blocker: true
    criteria: "Remediações priorizadas por impacto x esforço"
  - blocker: true
    criteria: "Scripts automatizáveis incluídos quando possível"
  - blocker: false
    criteria: "Recomendações de prevenção para causa raiz"
---

# Suggest Remediation

## Flow

```
1. Receber relatório de qualidade com problemas
2. Analisar problemas por categoria (dados, schema, pipeline, governança)
3. Priorizar por impacto (dados afetados) x esforço (complexidade)
4. Gerar scripts de limpeza automatizados (Python, SQL, dbt)
5. Definir correções manuais quando necessário
6. Recomendar políticas de governança e prevenção
7. Estimar impacto da remediação (% de dados corrigidos)
8. Gerar remediation-plan.md
9. Enviar para equipe de dados
```

## Elicitation

- "Qual o foco de remediação? (critical-only, all, preventive)"
- "Qual a linguagem preferida para scripts? (Python, SQL, dbt)"
- "Há restrições de janela de execução para correções?"
- "Deseja incluir recomendações de governança?"

## Performance

- **Duração esperada:** 10-20 minutos
- **Custo estimado:** ~0 (geração de recomendações)
- **Cacheável:** não
- **Paralelizável:** não

## Error Handling

- **Estratégia:** retry (máx. 2 tentativas, backoff exponencial base=5s, max=30s)
- **Fallback:** se o relatório estiver incompleto, gerar remediações para os problemas com dados suficientes
- **Notificação:** data-quality-reporter

## Dependencies

- generateQualityReport()
