---
task: Define Pricing and Packaging
responsavel: "@monetization-strategist"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - offer_stack: Arquitetura de oferta com tiers
  - unit_economics: Custos de entrega + margem alvo minima
  - willingness_to_pay: Evidencia de disposicao a pagar (entrevistas, pricing tests, concorrencia)
Saida: |
  - pricing_ladder: Estrutura de precos por pacote com logica de valor
  - upgrade_triggers: Criterios que levam cliente a subir de tier
  - margin_model: Modelo de margem por tier
Checklist:
  - "[ ] Definir ticket por pacote com logica (value-based, cost-plus, competitive)"
  - "[ ] Definir criterio/trigger de upgrade entre tiers"
  - "[ ] Validar margem minima por tier (gross > 60%)"
  - "[ ] Testar pricing com 5-10 prospects antes de fechar"
---

# *define-pricing-and-packaging

Define precificacao e empacotamento com logica de valor e sustentabilidade de margem.

## Step-by-Step

1. **Validar input** — Offer stack + unit economics + willingness to pay devem existir. Sem willingness, pricing e chute.
2. **Escolher logica de pricing** — Value-based (baseado em outcome), cost-plus (custo + margem), competitive (vs concorrentes). Preferir value-based.
3. **Definir ticket por tier** — Usar ancoragem: premium primeiro, depois standard, depois starter.
4. **Calcular margem por tier** — Receita - custo_entrega (horas squad + infra + suporte) = margem bruta. Target: >60%.
5. **Definir upgrade triggers** — O que faz starter virar standard? Standard virar pro? Volume, features, outcome?
6. **Testar pricing** — Rodar pricing test com 5-10 prospects antes de publicar. Medir reacao a cada tier.
7. **Publicar** — Atualizar LP, CRM, checkout com nova estrutura.

## Veto Conditions

- VETO se margem bruta estimada for <60% em qualquer tier → negocio nao sustenta
- VETO se pricing baseado em cost-plus sem considerar valor percebido → deixa dinheiro na mesa
- VETO se nao houver upgrade path claro → clientes ficam no tier mais baixo para sempre
- VETO se preco premium for <3x o preco starter → ancoragem fraca

## Output Example

```yaml
pricing_ladder:
  logica: "Value-based com ancoragem tier a tier"

  tiers:
    - tier: starter
      price: "R$ 1.500/mes"
      annual_price: "R$ 15.000 (2 meses gratis)"
      positioning: "Para founders solo validando primeira venda"

    - tier: standard
      price: "R$ 3.000/mes"
      annual_price: "R$ 30.000 (2 meses gratis)"
      most_popular: true
      positioning: "Para founders com trafego operando em escala"

    - tier: pro
      price: "R$ 8.000/mes"
      annual_price: "R$ 80.000 (2 meses gratis)"
      positioning: "Para agencias e multi-produto"

upgrade_triggers:
  starter_para_standard:
    - "MRR do cliente atinge R$ 10k (ficou volume)"
    - "Cliente precisa de checkout assistido (features do Standard)"
    - "Cliente comeca a rodar 2+ canais pagos"

  standard_para_pro:
    - "Cliente opera 2+ produtos"
    - "Cliente quer white-label"
    - "MRR do cliente atinge R$ 50k"

margin_model:
  starter:
    receita_mensal: 1500
    custo_entrega:
      horas_squad: "4h/mes x R$ 150/h = R$ 600"
      infra: "R$ 100"
      suporte: "R$ 150"
    custo_total: 850
    margem_bruta: "R$ 650 (43.3%)"
    status: "PROBLEMA - abaixo de 60%"

  standard:
    receita_mensal: 3000
    custo_entrega:
      horas_squad: "6h/mes x R$ 150/h = R$ 900"
      infra: "R$ 100"
      suporte: "R$ 300"
    custo_total: 1300
    margem_bruta: "R$ 1.700 (56.7%)"
    status: "PROBLEMA - ajustar custo ou preco"

  pro:
    receita_mensal: 8000
    custo_entrega:
      horas_squad: "10h/mes x R$ 150/h = R$ 1.500"
      infra: "R$ 200"
      suporte: "R$ 500"
    custo_total: 2200
    margem_bruta: "R$ 5.800 (72.5%)"
    status: "OK"

  recomendacao: "Starter precisa subir para R$ 2k/mes ou reduzir horas squad para 3h/mes para bater margem"
```

## Completion Criteria

- Tiers com pricing mensal + anual (desconto para anual)
- Upgrade triggers claros por tier
- Margem bruta calculada por tier (flags se <60%)
- Pricing testado com pelo menos 5 prospects antes de fechar

## Handoff

Pricing passa para `@revops-automation-engineer` implementar em checkout/billing. Upgrade triggers viram automacao. Guarantees implementadas junto.
