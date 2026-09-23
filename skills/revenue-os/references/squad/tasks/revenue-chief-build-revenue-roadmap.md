---
task: Build 90-Day Revenue Roadmap
responsavel: "@revenue-chief"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - business_goal: Meta de receita em 90 dias
  - constraints: Time, budget, canais disponiveis
  - diagnosed_bottleneck: Gargalo principal do *diagnose-revenue-gaps
Saida: |
  - roadmap_90_days: Plano por sprint (6 sprints de 2 semanas)
  - owners_and_kpis: Donos e KPIs por sprint
  - dependency_map: Dependencias entre sprints
Checklist:
  - "[ ] Meta total decomposta por mes (M1/M2/M3)"
  - "[ ] Meta mensal decomposta por sprint (2 sprints/mes)"
  - "[ ] Owners por frente de receita"
  - "[ ] KPI leading e lagging por sprint"
  - "[ ] Dependencias mapeadas (sprint X depende de sprint Y)"
---

# *build-revenue-roadmap

Monta roadmap de 90 dias com entregas por sprint e donos claros por frente de receita.

## Step-by-Step

1. **Validar entrada** — Meta numerica + prazo. Se faltar, retornar para `*build-macro-revenue-plan`.
2. **Decompor meta por mes** — M1: 20%, M2: 35%, M3: 45% (ajustar conforme contexto).
3. **Decompor meta mensal em 2 sprints de 2 semanas** — Cada sprint tem 1 objetivo unico e mensuravel.
4. **Mapear frentes de receita ativas** — Aquisicao, conversao, retention, monetizacao (nova oferta).
5. **Atribuir frentes a sprints** — Sprint 1 foca em desbloqueio do gargalo (output do diagnose). Sprints seguintes ampliam.
6. **Definir KPIs por sprint** — 1 leading (acao) + 1 lagging (resultado) por frente.
7. **Mapear dependencias** — Sprint B depende de Sprint A? Registrar para nao paralelizar o que nao pode.

## Veto Conditions

- VETO se soma das metas mensais nao bater 100% da meta trimestral
- VETO se algum sprint tiver >3 frentes simultaneas → diluicao, reduzir escopo
- VETO se sprint 1 nao atacar o gargalo diagnosticado → roadmap desalinhado da realidade
- VETO se alguma frente nao tiver owner humano nomeado

## Output Example

```yaml
roadmap_90_days:
  meta_trimestral: "R$ 100k MRR em 90 dias"

  sprints:
    - sprint: S1 (semanas 1-2)
      foco: "Desbloquear SLA de resposta <15min (gargalo diagnosticado)"
      frentes: [conversao_sql_cliente]
      meta: "SLA medio < 15 min + 25% conversao SQL->cliente"
      owner: "@sales-system-operator"

    - sprint: S2 (semanas 3-4)
      foco: "Ativar paid social canal secundario"
      frentes: [aquisicao_paid]
      meta: "200 SQLs/mes via paid com CAC payback < 4 meses"
      owner: "@demand-gen-architect"
      depende_de: [S1]

    - sprint: S6 (semanas 11-12)
      foco: "Lancar upsell para retencao"
      frentes: [monetization, retention]
      meta: "15% dos clientes M1 em upsell"
      owner: "@monetization-strategist"
      depende_de: [S3, S4]

owners_and_kpis:
  "@demand-gen-architect":
    kpi_leading: "SQLs/semana via paid"
    kpi_lagging: "CAC payback por canal"
  "@sales-system-operator":
    kpi_leading: "SLA medio primeira resposta"
    kpi_lagging: "Conversao SQL->cliente"

dependency_map:
  S2_depende_de: [S1]  # Precisa SLA ok antes de escalar volume
  S4_depende_de: [S2]  # Precisa canal estabilizado
  S6_depende_de: [S3, S4]  # Precisa clientes ativos para upsell
```

## Completion Criteria

- 6 sprints (90 dias / 2 semanas) com objetivo unico por sprint
- Cada sprint tem owner humano + KPIs leading e lagging
- Dependencias entre sprints mapeadas
- Meta total = soma das metas mensais = 100% da meta trimestral

## Handoff

Roadmap distribuido para diretores (CCO/CMO/CGO) via `@cro-oracle-guardian`. Sprint 1 inicia imediatamente.
