---
task: Spec Sales LP and Checkout Flow
responsavel: "@funnel-conversion-engineer"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - offer_stack: Oferta com tiers + pricing
  - icp_profile: Segmentos alvo com dor e jobs-to-be-done
  - value_proposition: Mensagem central por segmento
Saida: |
  - lp_spec: Especificacao funcional completa da landing page
  - checkout_flow_spec: Fluxo de checkout (one-time + assinatura)
  - tracking_spec: Events de tracking com UTM e conversion points
Checklist:
  - "[ ] Estrutura LP: Hero, proof, oferta, FAQ, CTA definida"
  - "[ ] Fluxo de checkout minimal (max 2 paginas)"
  - "[ ] Eventos de tracking mapeados em cada interacao"
  - "[ ] Copy por secao com tom e comprimento"
  - "[ ] Requisitos tecnicos (performance, acessibilidade)"
---

# *spec-sales-lp-and-checkout-flow

Especifica LP comercial e fluxo de checkout para handoff ao squad de design e implementacao.

## Step-by-Step

1. **Absorver oferta** — Ler offer_stack + value_proposition. Entender transformacao prometida.
2. **Estruturar LP** — Template comprovado: Hero -> Proof social -> Problema -> Solucao -> Features -> Prova -> Oferta -> Garantia -> FAQ -> CTA final.
3. **Escrever copy por secao** — Tom, comprimento, conteudo-chave por secao. Nao e copy final, e brief de copy.
4. **Desenhar fluxo de checkout** — Max 2 paginas: (1) resumo + pagamento, (2) confirmacao. Minimizar campos.
5. **Mapear eventos de tracking** — Click no CTA, scroll em X%, form start, form complete, checkout initiated, payment completed.
6. **Definir requisitos tecnicos** — Lighthouse >90, accessibility AA, mobile-first, carregamento <3s.
7. **Empacotar spec para handoff** — Arquivo estruturado que design + dev conseguem executar.

## Veto Conditions

- VETO se LP tiver >1 CTA principal → dispersao mata conversao
- VETO se checkout tiver >2 paginas → cada pagina adicional perde 10-20%
- VETO se nao houver tracking em cada secao da LP → impossivel otimizar depois
- VETO se LP nao for mobile-first → 60%+ do trafego e mobile

## Output Example

```yaml
lp_spec:
  url_temporaria: "/lp/revenue-os-case-14-dias"
  url_final: "/revenue-os" (apos testes)

  estrutura:
    hero:
      headline: "De produto AIOS pronto para R$ 20k+ MRR em 90 dias"
      subhead: "Squad completo CRO/CCO/CMO/CGO que transforma produto em receita previsivel"
      cta_principal: "Agendar demo de 30 min"
      visual: "Video loop de dashboard com MRR subindo"
      proof_badge: "Usado por founders AIOS"

    proof_social:
      tipo: "Logos + numeros"
      conteudo:
        - "R$ 40k+ MRR gerado no dogfooding"
        - "17 agents operando"
        - "14 dias ate primeira venda"

    problema:
      headline: "Voce sabe construir. Mas vender e outro bicho."
      subhead: "80% dos founders AIOS chegam ao produto pronto sem saber ativar receita"
      visual: "Diagrama: construcao OK (verde) / vendas NAO OK (vermelho)"

    solucao:
      headline: "Revenue OS = departamento comercial em formato de squad"
      subhead: "Cadeia de comando CRO -> C-level -> managers -> analysts"
      visual: "Diagrama da hierarquia com 17 agents"

    features:
      layout: "3 colunas x 2 linhas (6 features)"
      features:
        - "Kickoff 7 dias (plano -> operacao)"
        - "LP + checkout + CRM integrados"
        - "Dashboard de receita automatico"
        - "Experimentos de growth em sprints"
        - "Governanca semanal + mensal"
        - "Ecossistema AIOS integrado"

    oferta_principal:
      headline: "Escolha seu tier"
      cards:
        - tier: "Starter"
          price: "R$ 1.500/mes"
          features: ["Squad completo", "5 workflows", "Suporte async"]
          cta: "Comecar com Starter"

        - tier: "Standard"
          price: "R$ 3.000/mes"
          most_popular: true
          features: ["Tudo do Starter", "LP + checkout assistidos", "2 sync/mes"]
          cta: "Comecar com Standard"

        - tier: "Pro"
          price: "R$ 8.000/mes"
          features: ["Tudo do Standard", "White-label", "Multi-produto"]
          cta: "Falar com vendas"

    garantia:
      tipo: "Performance"
      texto: "Se em 14 dias sua LP + checkout + CRM nao estiverem ativos, devolvemos 100%. Sem perguntas."

    faq:
      perguntas:
        - "Nao tenho tempo, vou conseguir usar?"
        - "Como funciona a ativacao de 14 dias?"
        - "E se eu nao souber o que pedir pro squad?"
        - "Preciso ter produto pronto?"
        - "Posso cancelar quando quiser?"

    cta_final:
      headline: "Pronto para transformar produto em receita?"
      cta: "Agendar demo de 30 min"

checkout_flow_spec:
  pagina_1_resumo_pagamento:
    elementos:
      - "Resumo da oferta selecionada (tier + price + features)"
      - "Form: nome, email, empresa (3 campos max)"
      - "Payment: Stripe checkout ou Pix"
      - "Trust badges: SSL, Stripe, garantia"
      - "CTA: 'Confirmar pagamento'"

  pagina_2_confirmacao:
    elementos:
      - "Mensagem de sucesso + boas-vindas"
      - "Proximos passos: checar email + agendar call"
      - "CTA: 'Agendar call de onboarding'"
      - "Info sobre acesso ao squad"

tracking_spec:
  events_lp:
    - event: "lp_viewed"
      trigger: "Page load"
    - event: "scroll_50"
      trigger: "Scroll 50%"
    - event: "scroll_100"
      trigger: "Scroll 100%"
    - event: "cta_hero_clicked"
      trigger: "Click CTA principal"
    - event: "pricing_card_clicked"
      trigger: "Click em card de tier"

  events_checkout:
    - event: "checkout_initiated"
      trigger: "Entrou na pagina 1"
    - event: "payment_info_added"
      trigger: "Adicionou dados de pagamento"
    - event: "payment_completed"
      trigger: "Pagamento confirmado"

  events_fail:
    - event: "checkout_abandoned"
      trigger: "Saiu da pagina 1 sem completar"

requisitos_tecnicos:
  performance:
    lighthouse_score: ">90"
    lcp: "<2.5s"
    fid: "<100ms"
    cls: "<0.1"
  accessibility:
    wcag_level: "AA"
  mobile_first: true
  browsers: ["Chrome", "Safari", "Firefox", "Edge"]
```

## Completion Criteria

- LP spec com 9 secoes estruturadas + copy brief por secao
- Checkout com max 2 paginas e form de 3 campos
- Tracking em cada interacao principal (views, clicks, form)
- Requisitos tecnicos com metrics quantitativas

## Handoff

Spec passa para squad `design` (layout visual + prototipacao). Copy final passa para `content-os` ou `content-engine`. Implementacao tecnica passa para `n8n-builder` (automacoes) + dev contratado. Tracking implementado por `@revops-automation-engineer`.
