---
task: Setup Subscription Analytics
responsavel: "@revops-automation-engineer"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - telemetry_spec: Eventos de receita
  - billing_events: Eventos do provedor de pagamento (Stripe webhooks)
  - historical_subscription_data: Dados historicos de assinaturas (se houver)
Saida: |
  - subscription_kpi_model: Modelo de KPIs de assinaturas
  - dashboard_subscription_views: Views para MRR, churn, cohorts
  - anomaly_alerts: Alertas automaticos para anomalias
Checklist:
  - "[ ] MRR, churn, expansion, contraction definidos"
  - "[ ] Cohort analysis configurada"
  - "[ ] Eventos de assinatura reconciliados com Stripe"
  - "[ ] Alertas de anomalia configurados"
---

# *setup-subscription-analytics

Estrutura analise de assinaturas para decisao de crescimento e retencao.

## Step-by-Step

1. **Definir formulas canonicas** — MRR, ARR, Churn rate, Expansion MRR, Contraction MRR, Net Revenue Retention.
2. **Reconciliar com Stripe** — Dashboard deve bater 100% com relatorio oficial do Stripe.
3. **Configurar cohort analysis** — Agrupar clientes por mes de cadastro + tier. Analisar retencao N.
4. **Segmentar por tier e canal** — MRR por tier (Starter/Standard/Pro) + por canal de aquisicao.
5. **Calcular NRR (Net Revenue Retention)** — (MRR inicio + expansion - contraction - churn) / MRR inicio. Target: >100%.
6. **Configurar alertas** — Churn spike, MRR drop, expansion stagnation.
7. **Montar views** — Visualizacoes para uso diario do `@cro-oracle-guardian` e semanal do time.

## Veto Conditions

- VETO se MRR calculado divergir do Stripe >2% → dado sem confianca destroi decisao
- VETO se cohort analysis nao tiver base historica minima de 3 meses → dados prematuros
- VETO se nao houver segmentacao por tier → media esconde informacao por tier
- VETO se alertas dispararem >5/dia → ruido, time ignora

## Output Example

```yaml
subscription_kpi_model:
  kpis_primarios:
    - kpi: "MRR"
      formula: "Soma(subscription.amount_monthly) de todos os clientes ativos"
      atualizacao: "Tempo real via webhook"
      target: "R$ 100k em 90d"

    - kpi: "Churn rate mensal"
      formula: "Clientes que cancelaram no mes / Total clientes inicio do mes"
      target: "<5%"
      alerta: ">7%"

    - kpi: "Net Revenue Retention (NRR)"
      formula: "(MRR inicio + expansion - contraction - churn) / MRR inicio"
      target: ">100% (idealmente 110-130%)"

    - kpi: "Expansion MRR"
      formula: "Soma dos upgrades e add-ons de clientes existentes"
      target: "15% do MRR total"

    - kpi: "CAC Payback"
      formula: "CAC / MRR medio por cliente"
      target: "<6 meses"

  kpis_secundarios:
    - "ARR (MRR x 12)"
    - "LTV estimado"
    - "LTV:CAC ratio"
    - "Quick Ratio"
    - "Churn por tier"
    - "Churn por canal de aquisicao"

cohort_analysis:
  dimensoes:
    - "Mes de cadastro (cohort_month)"
    - "Tier de entrada"
    - "Canal de aquisicao"

  metricas_por_cohort:
    - "Retencao M+1, M+3, M+6, M+12"
    - "MRR medio por cohort"
    - "Expansion rate por cohort"

  visualizacao: "Heatmap com retencao por mes"

dashboard_subscription_views:
  view_executiva:
    kpis: ["MRR atual", "MRR novo mes", "Churn rate", "NRR"]
    comparacao: "vs mes anterior + vs meta"
    audiencia: "@cro-oracle-guardian"

  view_operacional:
    kpis: ["Churn diario", "Upgrades semana", "Proximos renewals", "Cartoes expirando"]
    audiencia: "@revenue-chief, @commercial-senior-manager"

  view_cohort:
    visualizacao: "Heatmap retencao"
    filtros: ["Tier", "Canal", "Mes cadastro"]
    audiencia: "@cgo-growth-director, @growth-senior-manager"

anomaly_alerts:
  - alerta: "Churn spike"
    trigger: "Churn diario >2x media ultimas 4 semanas"
    canal: "Slack #revenue-ops + email @cro-oracle-guardian"

  - alerta: "MRR drop"
    trigger: "MRR cai >5% semana a semana"
    canal: "Slack + email executivo"

  - alerta: "Expansion stagnation"
    trigger: "0 upgrades em 14 dias consecutivos"
    canal: "Slack #revenue-ops"

  - alerta: "Cartoes expirando"
    trigger: "5+ cartoes expirando nos proximos 7 dias"
    canal: "Task no CRM para @sales-system-operator contatar"
```

## Completion Criteria

- MRR reconciliado com Stripe (100% match)
- Cohort analysis com base minima de 3 meses
- 3 views no dashboard (executiva + operacional + cohort)
- 4 alertas de anomalia configurados

## Handoff

Dashboard alimenta `*control-weekly-metrics`. Alertas enviados via Slack. `@growth-senior-manager` usa cohorts para priorizar retention experiments.
