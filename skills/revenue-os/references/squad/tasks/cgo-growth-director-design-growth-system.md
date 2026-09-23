---
task: Design Growth System
responsavel: "@cgo-growth-director"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - commercial_strategy: Estrategia comercial (saida do CCO)
  - marketing_masterplan: Plano de marketing (saida do CMO)
  - product_metrics: Metricas atuais do produto (ativacao, retention, churn)
Saida: |
  - growth_system: Sistema integrado de crescimento com loops e metricas
  - aarrr_funnel: Funil Aquisicao-Ativacao-Retencao-Revenue-Referral mapeado
  - feedback_loops: Loops de feedback entre marketing/vendas/produto
Checklist:
  - "[ ] Mapear AARRR com owner por estagio"
  - "[ ] Integrar funil marketing -> vendas (SLA de handoff)"
  - "[ ] Definir loops de feedback (produto -> marketing, vendas -> produto)"
  - "[ ] KPI norte por estagio do funil"
---

# *design-growth-system

Integra marketing, vendas e produto em um sistema de crescimento com loops de feedback.

## Step-by-Step

1. **Mapear AARRR do negocio** — Aquisicao, Ativacao, Retencao, Revenue, Referral. Uma metrica norte por estagio.
2. **Identificar owner por estagio** — Marketing (aquisicao), produto (ativacao/retencao), CS/revenue (revenue/referral).
3. **Definir SLA de handoff marketing -> vendas** — Quanto tempo entre lead qualificado e primeira resposta.
4. **Mapear loops de feedback:**
   - Produto -> Marketing: features que viram pilares narrativos
   - Vendas -> Produto: objecoes viram backlog de melhoria
   - Clientes -> Referral: happy path leva a indicacao
5. **Definir programa de referral** — Como transformar cliente satisfeito em canal.
6. **Instrumentar tudo** — Cada estagio tem metrica visivel no dashboard.
7. **Definir cadencia de revisao** — Revisao mensal do AARRR completo.

## Veto Conditions

- VETO se algum estagio do AARRR nao tiver owner → estagio orfao = metrica morta
- VETO se handoff marketing->vendas tiver SLA >1h → lead esfria
- VETO se ativacao/retencao nao estiver instrumentada → impossivel otimizar o que nao mede

## Output Example

```yaml
growth_system:
  aarrr_funnel:
    aquisicao:
      metrica_norte: "SQLs/mes"
      target: 400
      owner: "@cmo-marketing-director"
    ativacao:
      metrica_norte: "Clientes que ativam stack comercial em 14 dias"
      target: "80% em 14 dias"
      owner: "@revenue-chief"
    retencao:
      metrica_norte: "Churn mensal"
      target: "<5%"
      owner: "@growth-senior-manager"
    revenue:
      metrica_norte: "MRR + expansion MRR"
      target: "R$ 100k em 90d"
      owner: "@monetization-strategist"
    referral:
      metrica_norte: "NPS + % clientes que indicam"
      target: "NPS 50+ / 20% indicam"
      owner: "@commercial-senior-manager"

feedback_loops:
  - loop: "Objecoes de vendas -> Backlog de produto"
    cadencia: "Semanal"
    mecanismo: "Top 3 objecoes da semana viram issues"
    owner: "@cco-commercial-director"
  - loop: "Features novas -> Pilares narrativos"
    cadencia: "Mensal"
    mecanismo: "Review produto com @cmo-marketing-director"
    owner: "@cgo-growth-director"
  - loop: "Churn reasons -> Melhorias UX"
    cadencia: "Quinzenal"
    mecanismo: "Entrevista com cada cliente que cancela"
    owner: "@growth-senior-analyst"

referral_program:
  tipo: "Credit-based"
  mecanica: "Cliente ganha 1 mes gratis por cada indicacao que converte"
  ativacao: "Automatica via CRM apos 30 dias de cliente ativo"

sla_handoff:
  marketing_to_vendas: "15 min"
  vendas_to_customer_success: "1 dia util apos venda"
```

## Completion Criteria

- AARRR completo com metrica norte + target + owner por estagio
- Pelo menos 3 feedback loops definidos com cadencia e owner
- Programa de referral com mecanica clara
- SLA de handoff marketing->vendas <1h

## Handoff

Sistema de growth integrado passa para `@growth-senior-manager` operacionalizar. Referral program ativa em `@sales-system-operator`. Revisao mensal.
