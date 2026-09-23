---
task: Build Revenue Dashboard
responsavel: "@revops-automation-engineer"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - telemetry_spec: Eventos e fontes de dados
  - subscription_kpi_model: KPIs de assinatura
  - revenue_goal: Meta de receita com metas por mes/sprint
Saida: |
  - dashboard_spec: Spec completo do dashboard (views + queries + alerts)
  - owner_matrix: Responsavel por cada indicador
  - refresh_schedule: Cadencia de atualizacao de dados
Checklist:
  - "[ ] Definir KPIs leading e lagging"
  - "[ ] Configurar views por audiencia (exec, operacional, analytics)"
  - "[ ] Definir alertas operacionais"
  - "[ ] Definir rotina de revisao (daily/weekly/monthly)"
  - "[ ] Validar que dados fazem match com fonte da verdade"
---

# *build-revenue-dashboard

Cria dashboard operacional de receita para decisao semanal e correcoes rapidas.

## Step-by-Step

1. **Definir fonte da verdade** — Stripe para revenue, CRM para pipeline, GA4 para aquisicao.
2. **Mapear KPIs por audiencia** — Executiva (CRO), operacional (managers), analytics (analysts).
3. **Configurar queries** — SQL ou dashboard tool queries que puxam dados consolidados.
4. **Montar views** — Tres views principais: Executive, Operational, Deep-dive Analytics.
5. **Configurar alertas** — Anomalias + thresholds + destinatarios.
6. **Definir refresh schedule** — Real-time para revenue events, daily para cohorts, weekly para LTV.
7. **Validar dados** — Comparar dashboard vs fontes (Stripe, CRM). Se divergir >2%, investigar.

## Veto Conditions

- VETO se dashboard misturar dados de tools diferentes sem reconciliacao → desconfianca nos numeros
- VETO se audiencia executiva receber >8 KPIs → overload, ninguem olha
- VETO se refresh de KPIs criticos for >daily → operacao cega para movimentos do dia
- VETO se alertas dispararem >3x/semana sem acao real → fadiga de alerta

## Output Example

```yaml
dashboard_spec:
  tool: "Metabase (ou Retool, Grafana, Looker Studio)"

  fontes_dados:
    - tool: "Stripe"
      tipos: ["MRR", "payments", "subscriptions", "churn"]
      refresh: "Real-time via webhook"
    - tool: "CRM (HubSpot/Pipedrive)"
      tipos: ["leads", "deals", "pipeline stages", "SLA"]
      refresh: "15 min"
    - tool: "GA4 + PostHog"
      tipos: ["traffic", "conversions", "user journey"]
      refresh: "1h"

  views:
    view_executiva:
      audiencia: "@cro-oracle-guardian + diretores"
      kpis:
        - "MRR atual + meta"
        - "MRR novo (mes)"
        - "Churn rate (mes)"
        - "NRR"
        - "CAC payback"
        - "Leads/semana"
        - "Demos realizadas/semana"
        - "Top 3 gargalos do funil"
      layout: "Single page, scroll vertical, mobile-first"
      cadencia_revisao: "Diaria (CRO) + semanal (reuniao)"

    view_operacional:
      audiencia: "@revenue-chief + senior managers"
      kpis:
        - "Pipeline por estagio"
        - "SLA de resposta (atual vs target)"
        - "Velocidade media por estagio"
        - "Deals em escalacao (>14 dias)"
        - "Cartoes expirando (7 dias)"
        - "Falhas de pagamento ativas"
        - "Campanhas ativas + performance"
      cadencia_revisao: "2x/dia (manha + tarde)"

    view_analytics:
      audiencia: "@growth-senior-analyst + experimentation"
      kpis:
        - "Funil de conversao por canal"
        - "Cohort retention heatmap"
        - "Attribution multi-touch"
        - "A/B test results"
        - "Churn reasons breakdown"
        - "LTV por segmento"
      cadencia_revisao: "Semanal (sexta)"

  alertas:
    - alerta: "MRR drop >5% week-over-week"
      destinatario: "CRO + revenue-chief"
      canal: "Slack + email"

    - alerta: "Churn spike (>2x media 4 semanas)"
      destinatario: "CGO + growth manager"
      canal: "Slack"

    - alerta: "SLA primeira resposta >30 min"
      destinatario: "Sales manager"
      canal: "Slack real-time"

    - alerta: "Pagamento falhado"
      destinatario: "Sales system operator"
      canal: "Task automatica no CRM"

owner_matrix:
  "MRR": "@cro-oracle-guardian (accountable), @revops-automation-engineer (responsible)"
  "Churn rate": "@cgo-growth-director (accountable)"
  "Pipeline velocity": "@cco-commercial-director (accountable)"
  "Lead volume": "@cmo-marketing-director (accountable)"
  "SLA resposta": "@commercial-senior-manager (accountable)"

refresh_schedule:
  real_time: ["Revenue events", "Pipeline movements"]
  hourly: ["GA4 traffic", "Campaign metrics"]
  daily: ["Cohort analysis", "Attribution"]
  weekly: ["LTV calculations", "Retention curves"]
```

## Completion Criteria

- 3 views (executive + operacional + analytics) com audiencia definida
- KPIs de cada view limitados (<8 para exec, <15 para ops)
- Alertas configurados com destinatario e canal
- Owner matrix com accountable/responsible por KPI
- Dados reconciliados com fonte da verdade (2% tolerancia max)

## Handoff

Dashboard vira source of truth para `*control-weekly-metrics`. Owners recebem alertas e atuam conforme. Review mensal do proprio dashboard (KPIs ainda relevantes?).
