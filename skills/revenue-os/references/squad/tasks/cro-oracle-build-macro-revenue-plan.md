---
task: Build Macro Revenue Plan
responsavel: "@cro-oracle-guardian"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - executive_brief: Brief executivo (saida de *intake-and-route)
  - revenue_target: Meta numerica com prazo (ex: R$ 100k MRR em 90 dias)
  - command_chain_route: Diretores selecionados (CCO/CMO/CGO)
Saida: |
  - macro_revenue_plan: Plano trimestral com metas mensais, owners e KPIs
  - leading_indicators: KPIs leading (acoes) por frente
  - lagging_indicators: KPIs lagging (resultados) por frente
  - weekly_cadence: Ritmo de revisao semanal definido
Checklist:
  - "[ ] Meta macro decomposta por mes (M1, M2, M3)"
  - "[ ] Cada diretor tem meta propria derivada da macro"
  - "[ ] KPI leading e lagging definidos por frente"
  - "[ ] Cadencia semanal definida (dia, hora, participantes, output)"
  - "[ ] Plano aprovado pelo usuario antes de distribuir"
---

# *build-macro-revenue-plan

Define o plano macro de receita com metas mensais, owners claros e cadencia de revisao.

## Step-by-Step

1. **Validar entrada** — Confirmar que `executive_brief` tem meta numerica e diretores definidos. Se nao, VETO.
2. **Decompor meta macro em metas mensais** — Regra padrao (ajustar conforme contexto):
   - M1: 20% da meta (ramp-up, setup, primeiros experimentos)
   - M2: 35% da meta (aceleracao, canais estabilizados)
   - M3: 45% da meta (escala)
3. **Derivar metas por diretor** — Cada diretor recebe fatia da meta coerente com seu escopo:
   - CMO: meta de leads qualificados (SQL) e CAC por canal
   - CCO: meta de conversao pipeline→receita e tempo de ciclo
   - CGO: meta de uplift em conversao e retention
4. **Definir KPIs leading e lagging por frente** — Leading (acao) + Lagging (resultado). Ex: leads/semana (leading) + MRR novo (lagging).
5. **Definir cadencia semanal** — Reuniao semanal de 30-45 min com: dia fixo, participantes fixos, output fixo (update em dashboard).
6. **Consolidar plano** — Output YAML com todas as informacoes acima.
7. **Aprovar com usuario** — Apresentar plano, coletar ajustes, registrar aprovacao.

## Veto Conditions

- VETO se meta mensal somar menos ou mais que 100% da meta trimestral → recalcular decomposicao
- VETO se algum diretor ficar sem meta propria → redistribuir ou escalar
- VETO se nenhum KPI leading for definido (so lagging) → replanejar, pois squad nao conseguira ajustar no meio do caminho
- VETO se cadencia semanal nao tiver owner de facilitacao → sem owner, reuniao morre

## Output Example

```yaml
macro_revenue_plan:
  meta_trimestral: "R$ 100k MRR em 90 dias"
  decomposicao_mensal:
    M1: { meta: "R$ 20k MRR novo", foco: "setup + primeiros experimentos" }
    M2: { meta: "R$ 35k MRR novo", foco: "aceleracao canais pagos" }
    M3: { meta: "R$ 45k MRR novo", foco: "escala + retention" }

  metas_por_diretor:
    cmo-marketing-director:
      meta: "400 SQLs/mes ate M3 com CAC payback < 4 meses"
      owner: "@cmo-marketing-director"
    cco-commercial-director:
      meta: "Conversao SQL→cliente = 25% + ciclo medio < 14 dias"
      owner: "@cco-commercial-director"
    cgo-growth-director:
      meta: "Uplift +15% conversao LP + churn < 5%/mes"
      owner: "@cgo-growth-director"

  leading_indicators:
    - { kpi: "SQLs/semana", owner: "@cmo-marketing-director", target: 100 }
    - { kpi: "Demos/semana", owner: "@cco-commercial-director", target: 25 }
    - { kpi: "Experimentos/mes", owner: "@cgo-growth-director", target: 4 }

  lagging_indicators:
    - { kpi: "MRR novo", target: "R$ 100k em 90d" }
    - { kpi: "CAC payback", target: "< 4 meses" }
    - { kpi: "Churn mensal", target: "< 5%" }

  weekly_cadence:
    dia: "Terca-feira"
    hora: "09:00 BRT"
    duracao_min: 30
    participantes: [cro-oracle-guardian, cmo-marketing-director, cco-commercial-director, cgo-growth-director]
    facilitador: "@cro-oracle-guardian"
    output: "Update em revenue-dashboard + decisoes registradas"
```

## Completion Criteria

- Plano completo cobre M1, M2, M3 com metas somando 100% da meta trimestral
- Cada diretor selecionado tem meta propria, owner e KPIs (leading + lagging)
- Cadencia semanal definida e aceita por todos os owners
- Plano aprovado pelo usuario (registro em log de decisao)

## Handoff

Apos aprovacao, o plano e distribuido via `command_chain_route` para cada diretor. Primeiro ciclo de `*control-weekly-metrics` agendado para 1 semana apos.
