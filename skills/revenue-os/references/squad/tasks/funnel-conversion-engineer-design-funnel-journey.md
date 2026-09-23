---
task: Design Funnel Journey
responsavel: "@funnel-conversion-engineer"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - channel_plan: Canais e fontes de trafego
  - offer_stack: Estrutura de oferta com tiers
  - icp_profile: Perfil do ICP com jobs-to-be-done
Saida: |
  - funnel_map: Mapa completo do funil com etapas e transicoes
  - friction_log: Pontos de friccao identificados por etapa
  - passage_criteria: Criterios de passagem de uma etapa para outra
Checklist:
  - "[ ] Definir etapas do funil (visita -> lead -> SQL -> demo -> cliente)"
  - "[ ] Definir CTA unico por etapa"
  - "[ ] Definir eventos de tracking por etapa"
  - "[ ] Identificar e documentar friccoes"
---

# *design-funnel-journey

Desenha a jornada completa do funil para reduzir queda entre etapas e aumentar previsibilidade.

## Step-by-Step

1. **Mapear estado atual** — Se funil ja existe, inventariar etapas e conversoes atuais.
2. **Desenhar estado ideal** — Jornada completa: visita -> lead capture -> qualificacao -> demo -> proposta -> fechamento -> ativacao.
3. **Definir CTA unico por etapa** — Cada etapa tem 1 acao esperada. Multiplos CTAs confundem.
4. **Identificar friccoes** — Em cada etapa, listar o que pode fazer o usuario abandonar.
5. **Definir eventos de tracking** — Events que confirmam progressao (lead_captured, demo_scheduled, etc).
6. **Mapear ferramentas** — Que tool executa cada etapa (LP tool, email tool, CRM, checkout).
7. **Definir criterios de passagem** — O que torna um lead um SQL? Um SQL em demo-ready?

## Veto Conditions

- VETO se etapa nao tiver CTA unico → abandono garantido
- VETO se alguma etapa nao for instrumentada (sem event) → funil cego
- VETO se funil tiver >7 etapas → complexidade mata conversao
- VETO se criterio de passagem for subjetivo ("lead engajado") → objetividade exige definicao

## Output Example

```yaml
funnel_map:
  etapa_1_awareness:
    fonte: ["Paid IG", "Linkedin organic", "Content SEO"]
    destino: "LP de lead magnet OU sales LP"
    cta_unico: "Clicar anuncio / post"
    event: "click_ad"

  etapa_2_lead_capture:
    pagina: "LP lead magnet"
    cta_unico: "Baixar playbook" OR "Agendar demo"
    event: "lead_captured"
    campos_form: ["email", "empresa"]
    conversao_target: "3% visita -> lead"

  etapa_3_qualificacao:
    canal: "Email sequencia aquecimento"
    cta_unico: "Agendar demo via link no email"
    event: "demo_scheduled"
    conversao_target: "20% lead -> SQL"

  etapa_4_demo:
    canal: "Call 30 min (zoom/meet)"
    cta_unico: "Assinar proposta ao final"
    event: "demo_completed"
    conversao_target: "40% SQL -> demo realizada"

  etapa_5_proposta:
    canal: "Email pos-demo com link checkout"
    cta_unico: "Fechar no checkout"
    event: "checkout_initiated"
    conversao_target: "40% demo -> proposta enviada"

  etapa_6_fechamento:
    canal: "Checkout Stripe"
    cta_unico: "Confirmar pagamento"
    event: "payment_completed"
    conversao_target: "70% proposta -> fechamento"

  etapa_7_ativacao:
    canal: "Onboarding 14 dias"
    cta_unico: "Ativar LP + checkout do cliente"
    event: "customer_activated"
    conversao_target: "75% fechamento -> ativado"

friction_log:
  etapa_2_lead_capture:
    - "Formulario com >3 campos derruba 20% de conversao"
    - "LP sem proof social reduz confianca"
    - "CTA acima da dobra ausente"

  etapa_5_proposta:
    - "Checkout com >2 paginas aumenta abandono"
    - "Falta de garantia visivel gera hesitacao"
    - "Ausencia de multiple payment methods"

passage_criteria:
  lead_to_sql: "Respondeu 2+ emails de aquecimento + clicou CTA agendar"
  sql_to_demo_realizada: "Demo completa > 20 min + perguntou sobre pricing"
  demo_to_proposta: "Confirmou fit + pediu proposta por escrito"
  proposta_to_fechamento: "Link de checkout aberto + nao cancelado em 48h"
```

## Completion Criteria

- Funil com 5-7 etapas (nao mais)
- Cada etapa com CTA unico + event + conversao target
- Friccoes documentadas por etapa com impacto estimado
- Criterios de passagem objetivos (sem "lead engajado" vago)

## Handoff

Funil passa para `@revops-automation-engineer` implementar tracking. Friccoes viram backlog de `*improve-conversion-rates`. LP design passa para `@funnel-conversion-engineer *spec-sales-lp-and-checkout-flow`.
