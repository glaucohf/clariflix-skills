---
task: Diagnose Revenue Gaps
responsavel: "@revenue-chief"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - product_summary: O que foi construido, para quem e estagio atual
  - current_metrics: Leads, conversao, receita atual, CAC, churn
  - channel_mix: Canais ativos e volume por canal
Saida: |
  - bottleneck_map: Gargalo principal + gargalos secundarios classificados
  - root_cause_analysis: Causa raiz de cada gargalo
  - next_14_days_plan: Plano de ataque com acoes priorizadas e owners
Checklist:
  - "[ ] Mapear ICP atual vs ICP idealizado"
  - "[ ] Identificar o gargalo principal (oferta/demanda/conversao/operacao)"
  - "[ ] Decompor causa raiz via 5 whys"
  - "[ ] Priorizar acoes de alto impacto + baixa complexidade"
---

# *diagnose-revenue-gaps

Diagnostica onde a receita esta travando: oferta, demanda, conversao ou operacao comercial.

## Step-by-Step

1. **Mapear funil atual** — Leads → MQL → SQL → Demo → Cliente. Volume + conversao entre etapas.
2. **Comparar com benchmarks** — Conversao esperada por etapa no seu segmento (ex: SaaS B2B: visita→SQL 2-5%, SQL→cliente 20-30%).
3. **Identificar gargalo principal** — Etapa onde a conversao esta mais abaixo do benchmark. Regra: so um gargalo principal por vez.
4. **Classificar gargalo em 4 categorias:**
   - Oferta: ICP errado, pricing errado, posicionamento confuso
   - Demanda: volume insuficiente no topo do funil
   - Conversao: funil perde em etapas especificas (LP, checkout, qualificacao)
   - Operacao: CRM desorganizado, follow-up lento, script inexistente
5. **Aplicar 5 whys** — Para o gargalo principal, perguntar "por que?" 5 vezes ate chegar em causa raiz.
6. **Priorizar acoes 2x2** — Impacto (alto/baixo) x Complexidade (baixa/alta). Comecar por alto impacto + baixa complexidade (quick wins).
7. **Gerar plano 14 dias** — Top 3 acoes com owner + deadline.

## Veto Conditions

- VETO se `current_metrics` nao tiver volume de leads mensurado → sem baseline, diagnostico e chute
- VETO se gargalos simultaneos em 3+ categorias → problema sistemico, escalar para `@cro-oracle-guardian` refazer macro plan
- VETO se causa raiz for "precisamos de mais trafego" sem analise de conversao → quase sempre e conversao que esta travada, nao volume

## Output Example

```yaml
bottleneck_map:
  principal:
    etapa: "SQL -> Demo"
    conversao_atual: "15%"
    benchmark: "40-50%"
    categoria: operacao
    razao: "SLA de resposta de 48h, prospect esfria antes da demo"

  secundarios:
    - etapa: "LP -> Lead"
      conversao_atual: "1.8%"
      benchmark: "3-5%"
      categoria: conversao
      razao: "CTA da LP concorrendo com 3 outros (confuso)"

root_cause_analysis:
  gargalo: "SQL -> Demo em 15% vs 40% esperado"
  5_whys:
    - "Por que baixo? SLA de resposta esta em 48h"
    - "Por que 48h? Nao tem script de primeira resposta automatizado"
    - "Por que nao automatizado? Ninguem priorizou no ultimo sprint"
    - "Por que nao priorizou? Time comercial nao media SLA antes"
    - "Por que nao media? Dashboard nao tinha essa metrica"
  causa_raiz: "Dashboard sem metrica de SLA + sem ownership = gargalo invisivel"

next_14_days_plan:
  - acao: "Criar resposta automatica de 15 min para novos leads"
    impacto: alto
    complexidade: baixa
    owner: "@sales-system-operator"
    deadline: "2026-05-07"
  - acao: "Adicionar SLA de resposta ao dashboard de receita"
    impacto: alto
    complexidade: baixa
    owner: "@revops-automation-engineer"
    deadline: "2026-05-09"
  - acao: "Simplificar LP reduzindo de 4 CTAs para 1"
    impacto: medio
    complexidade: baixa
    owner: "@funnel-conversion-engineer"
    deadline: "2026-05-12"
```

## Completion Criteria

- Bottleneck_map tem 1 principal + 0-3 secundarios (ordem de prioridade clara)
- Causa raiz do gargalo principal chega em nivel de sistema (nao pessoal)
- Plano 14 dias com top 3 acoes + owners + deadlines
- Todas as acoes tem impacto alto (sem tapar buraco com agua)

## Handoff

Acoes distribuidas para especialistas (sales-system-operator, revops-automation-engineer, funnel-conversion-engineer, etc.) via `@revenue-chief`. Resultados revisados em 14 dias na proxima rodada `*diagnose-revenue-gaps`.
