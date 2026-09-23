---
task: Run Self Launch
responsavel: "@revenue-chief"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - target_mrr: Meta de MRR do proprio Revenue OS em 90 dias
  - launch_window_days: Janela de lancamento (ex: 14 dias)
  - available_channels: Canais disponiveis (lista + budget)
Saida: |
  - self_launch_plan: Plano operacional para vender o proprio squad
  - first_cycle_metrics: Metricas da primeira semana pos-launch
  - lessons_for_product: Aprendizados que voltam para o produto
Checklist:
  - "[ ] Oferta do Revenue OS empacotada (feature list + outcome + price)"
  - "[ ] LP com checkout ativo"
  - "[ ] Dashboard de receita e assinaturas pronto"
  - "[ ] Sequencias de email e criativos ativos"
  - "[ ] Dogfooding instrumentado (squad usa os proprios workflows)"
---

# *run-self-launch

Executa o dogfooding: usa o Revenue OS para vender o proprio Revenue OS e validar o metodo na pratica.

## Step-by-Step

1. **Empacotar oferta do Revenue OS** — Features, outcome prometido, pricing, garantias. Usar `@monetization-strategist`.
2. **Executar wf-revenue-os-self-launch** — Acionar workflow completo com DAY-1 a DAY-14.
3. **Ativar stack comercial** — LP + checkout + dashboard + email + CRM (via `*orchestrate-commercial-stack`).
4. **Medir first_cycle_metrics** — Leads, SQLs, demos, conversao, MRR novo, churn (se houver) na primeira semana.
5. **Extrair lessons_for_product** — O que o squad aprendeu usando o proprio produto? Onde o produto tem friccao? O que precisa virar feature?
6. **Registrar dogfooding feedback** — Documentar em `docs/SELF-LAUNCH-ARTIFACT-V{N}.md`.
7. **Iterar oferta baseado em objecoes** — Primeiras 5 objecoes em vendas viram refinamento de pitch/pricing/offer.

## Veto Conditions

- VETO se nao houver oferta empacotada (preco + garantia + outcome claros) → nao vende algo difuso
- VETO se squad nao estiver usando os proprios workflows internamente → dogfooding fake vira teatro
- VETO se lancar sem dashboard funcionando → nao da pra medir o que nao registra

## Output Example

```yaml
self_launch_plan:
  oferta:
    nome: "Revenue OS - Squad Comercial Completo"
    price: "R$ 3.000/mes"
    garantia: "Se nao ativar stack comercial em 14 dias, devolvemos 100%"
    outcome: "Produto pronto transformado em receita previsivel em 90 dias"

  canais_ativos:
    - canal: "Linkedin organic (posts do autor)"
      budget: "R$ 0"
      expectativa: "30-50 SQLs/mes"
    - canal: "Paid social Instagram"
      budget: "R$ 5k/mes"
      expectativa: "80-120 SQLs/mes"

  cronograma_14_dias:
    DAY-1-3: "Oferta + LP + checkout ativos"
    DAY-4-6: "Primeiros criativos e sequencia email"
    DAY-7-14: "Trafego + demos + primeiras vendas"

first_cycle_metrics:
  semana_1:
    leads: 67
    sqls: 18
    demos_agendadas: 8
    demos_realizadas: 6
    vendas: 2
    mrr_novo: "R$ 6.000"

lessons_for_product:
  - "Prospects querem ver um case real antes da demo -> criar demo-case pre-gravada"
  - "Objecao comum: 'sou solo, vou conseguir usar?' -> criar tier menor (R$ 1.5k) para solo"
  - "Setup manual de squads complementares friccionou 3 leads -> automatizar handoff via CLI"
```

## Completion Criteria

- Oferta empacotada com price + garantia + outcome
- 14 dias executados com entregas diarias documentadas
- first_cycle_metrics preenchido com numeros reais
- lessons_for_product com 3-5 aprendizados que viram backlog de produto

## Handoff

Lessons viram issues para squads relevantes (produto, onboarding, marketing). Metrics alimentam proximo `*control-weekly-metrics`.
