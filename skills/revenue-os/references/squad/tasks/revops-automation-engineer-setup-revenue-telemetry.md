---
task: Setup Revenue Telemetry
responsavel: "@revops-automation-engineer"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - funnel_map: Etapas e eventos do funil
  - crm_fields: Campos do pipeline
  - channel_portfolio: Canais ativos para atribuicao
Saida: |
  - telemetry_spec: Spec de eventos + propriedades + taxonomia
  - attribution_minimum_setup: Modelo de atribuicao (first-touch, last-touch, linear)
  - data_warehouse_schema: Schema basico de data warehouse
Checklist:
  - "[ ] Definir taxonomia de eventos padronizada"
  - "[ ] Mapear cada evento para KPI especifico"
  - "[ ] Implementar UTM tagging em todos os links"
  - "[ ] Validar consistencia de dados cross-tool (LP, CRM, Checkout)"
  - "[ ] Configurar atribuicao minima multi-touch"
---

# *setup-revenue-telemetry

Implementa telemetria minima para enxergar o funil de receita de ponta a ponta.

## Step-by-Step

1. **Definir taxonomia de eventos** — Nomenclatura padrao: `object_action` (ex: `demo_scheduled`, `payment_completed`).
2. **Listar eventos necessarios** — Baseado no funnel_map, todos os touchpoints que importam.
3. **Mapear evento -> KPI** — Cada evento alimenta pelo menos 1 KPI.
4. **Implementar UTM tagging** — Todos os links saindo tem utm_source, utm_medium, utm_campaign.
5. **Configurar tracking** — Google Analytics 4 + PostHog (ou Amplitude) + CRM events.
6. **Validar consistencia cross-tool** — Dados no GA batem com dados no CRM batem com dados no Stripe.
7. **Implementar atribuicao** — Minimo first-touch + last-touch. Ideal: linear multi-touch.

## Veto Conditions

- VETO se taxonomia de eventos for inconsistente (camelCase vs snake_case misturados) → dashboard quebrado
- VETO se algum evento nao tiver UTM tagging → atribuicao impossivel
- VETO se dados diferirem >10% entre tools sem razao documentada → perda de confianca nos dados
- VETO se so houver last-touch attribution → canais de topo de funil ficam invisiveis

## Output Example

```yaml
telemetry_spec:
  taxonomia:
    padrao: "snake_case, object_action"
    examples_ok:
      - "lead_captured"
      - "demo_scheduled"
      - "payment_completed"
    examples_nao:
      - "capturedLead" (camelCase errado)
      - "capturaLead" (portugues misturado)

  eventos_mapeados:
    - event: "page_viewed"
      properties: ["page_url", "referrer", "utm_source", "utm_medium", "utm_campaign"]
      kpi: ["Traffic", "CTR canal"]

    - event: "lead_captured"
      properties: ["lead_id", "source", "campaign", "landing_page"]
      kpi: ["Lead volume", "CPL"]

    - event: "demo_scheduled"
      properties: ["lead_id", "booking_time", "source"]
      kpi: ["SQL conversion", "Velocity"]

    - event: "demo_completed"
      properties: ["lead_id", "demo_duration", "demo_outcome"]
      kpi: ["Demo show rate", "Demo-to-proposal conversion"]

    - event: "checkout_initiated"
      properties: ["lead_id", "tier", "price", "currency"]
      kpi: ["Checkout conversion"]

    - event: "payment_completed"
      properties: ["customer_id", "tier", "mrr_amount", "annual_or_monthly"]
      kpi: ["MRR novo", "CAC", "LTV inicio"]

    - event: "subscription_cancelled"
      properties: ["customer_id", "reason", "tenure_days"]
      kpi: ["Churn rate", "Razoes churn"]

attribution_minimum_setup:
  modelo_principal: "Linear multi-touch (4 touchpoints)"
  fallback: "Last-touch para analise rapida"

  regras:
    first_touch: "Primeiro evento de qualquer canal nos 90 dias anteriores a conversao"
    last_touch: "Ultimo evento antes da conversao"
    linear: "Credito igual distribuido entre todos os touchpoints no path"

  implementacao:
    tool: "GA4 + custom attribution via PostHog"
    lookback_window: "90 dias"

data_warehouse_schema:
  tool: "BigQuery (ou Supabase como alternativa simples)"

  tabelas:
    - nome: "events"
      colunas: ["event_id", "event_name", "user_id", "timestamp", "properties (JSON)"]

    - nome: "users"
      colunas: ["user_id", "email", "first_seen", "last_seen", "source", "stage"]

    - nome: "attribution_paths"
      colunas: ["path_id", "user_id", "touchpoints (JSON array)", "conversion_event", "conversion_value"]

  etl:
    frequencia: "Diaria (batch 3am)"
    source: "PostHog + CRM + Stripe"
    destino: "BigQuery"

validacao_consistencia:
  checks_diarios:
    - "Leads no GA = leads no CRM (+/- 2%)"
    - "MRR no Stripe = MRR no dashboard (+/- 0%)"
    - "Eventos duplicados < 1%"

  acao_se_inconsistente:
    - ">10% diferenca: alerta Slack + investigacao em 24h"
    - "<10% diferenca: log para review semanal"
```

## Completion Criteria

- Taxonomia de eventos padronizada (snake_case)
- Todos os eventos do funil mapeados para KPI
- UTM tagging em 100% dos links saindo
- Atribuicao multi-touch minimo (first + last + linear)
- Consistencia cross-tool validada (GA vs CRM vs Stripe)

## Handoff

Dados fluem para `*build-revenue-dashboard`. Schema alimentado por ETL diaria. `@marketing-senior-analyst` e `@commercial-senior-analyst` usam tagging nos links.
