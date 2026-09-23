---
task: Run 7-Day Kickoff
responsavel: "@cro-oracle-guardian"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - kickoff_goal: Meta do kickoff de 7 dias (primeira venda, primeira LP live, primeiro ciclo completo, etc.)
  - baseline_context: Contexto inicial (oferta, canal, stack atual, time disponivel)
  - macro_revenue_plan: Plano macro ja aprovado (dependencia obrigatoria)
Saida: |
  - kickoff_execution_plan: Plano detalhado dia a dia (DAY-1 a DAY-7)
  - day_by_day_owners: Donos por trilha e papel por dia
  - success_criteria: Criterios de sucesso mensuraveis por dia e ao final
  - daily_standup_template: Template de check-in diario
Checklist:
  - "[ ] Meta da semana definida e mensuravel"
  - "[ ] Metas diarias decompostas da meta semanal"
  - "[ ] Donos por papel confirmados para cada dia"
  - "[ ] Gatilhos de correcao definidos (se atrasar, o que fazer)"
  - "[ ] Workflow wf-kickoff-7-days.yaml ativado"
---

# *run-7-day-kickoff

Ativa o kickoff operacional intensivo de 7 dias com cadeia de comando completa:
CRO → CCO/CMO/CGO → Managers → Analysts → Celula especialista.

## Step-by-Step

1. **Validar macro_revenue_plan existe** — Sem plano macro, kickoff nao faz sentido. Se faltar, executar `*build-macro-revenue-plan` primeiro.
2. **Definir meta semanal unica** — Uma unica meta agressiva para 7 dias (ex: "LP live + checkout funcional + 10 demos agendadas").
3. **Decompor em 7 metas diarias** — Usar o template do `wf-kickoff-7-days`:
   - DAY-1: CRO direction + macro targets
   - DAY-2: Directors planning (CCO/CMO/CGO)
   - DAY-3: Offer, LP spec, checkout plan
   - DAY-4: Campaign + sales machine setup
   - DAY-5: Telemetry + dashboard + automations
   - DAY-6: Controlled go-live (checkpoint humano)
   - DAY-7: First metrics + next cycle (checkpoint humano)
4. **Confirmar owners por dia** — Cada dia tem 1 owner principal + 2-3 executores. Nome real, nao papel generico.
5. **Definir gatilhos de correcao** — Se DAY-3 atrasar, DAY-4 faz compensacao (ex: reduzir escopo da campanha). Definir antes, nao no meio.
6. **Ativar workflow** — Disparar `wf-kickoff-7-days.yaml` com owners preenchidos.
7. **Configurar daily standup** — 15 min, todo dia mesmo horario, template fixo (ontem/hoje/bloqueio).

## Veto Conditions

- VETO se `macro_revenue_plan` nao existir ou estiver vago → rodar `*build-macro-revenue-plan` primeiro
- VETO se meta semanal nao for mensuravel (ex: "melhorar o funil" em vez de "elevar conversao de 2% para 4%")
- VETO se nenhum humano real puder ser owner em algum dia → kickoff sem owner humano nao executa
- VETO se time disponivel <3 pessoas → kickoff intensivo exige coordenacao minima, com 1-2 pessoas melhor ir ao ritmo normal

## Output Example

```yaml
kickoff_execution_plan:
  meta_semanal: "LP live + checkout funcional + 10 demos agendadas + primeira venda registrada"
  inicio: "2026-05-05 (segunda)"
  fim: "2026-05-11 (domingo)"

  dias:
    - dia: DAY-1
      data: "2026-05-05"
      foco: "Macro direction + targets"
      owner_principal: "@cro-oracle-guardian (Rodrigo)"
      executores: ["@cco-commercial-director", "@cmo-marketing-director", "@cgo-growth-director"]
      entregas: ["Macro plan trimestral ratificado", "Targets diarios definidos"]

    - dia: DAY-2
      data: "2026-05-06"
      foco: "Directors planning"
      owner_principal: "@cco-commercial-director"
      executores: ["@cmo-marketing-director", "@cgo-growth-director"]
      entregas: ["Strategy commercial", "Masterplan marketing", "Growth system"]

    - dia: DAY-6
      data: "2026-05-10"
      foco: "Go-live"
      owner_principal: "@revenue-chief"
      executores: ["@funnel-conversion-engineer", "@revops-automation-engineer"]
      entregas: ["LP live", "Checkout testado em producao", "Dashboard live"]
      checkpoint_humano: true

success_criteria:
  final:
    - LP publicada e carregando <3s
    - Checkout processando pagamento real (teste com R$ 1)
    - 10 demos agendadas no CRM
    - Pelo menos 1 venda registrada (validacao)
    - Dashboard mostrando MRR, CAC, conversao
  por_dia:
    DAY-1: "Macro plan ratificado em reuniao de 60 min"
    DAY-6: "Checkout processa R$ 1 real sem erro"

gatilhos_correcao:
  - if: "DAY-3 atrasa checkout plan"
    then: "DAY-4 reduz escopo campanha (1 canal em vez de 2)"
  - if: "DAY-5 dashboard nao pronto"
    then: "DAY-6 go-live usa tracking manual via planilha ate DAY-10"

daily_standup:
  horario: "09:00 BRT"
  duracao_min: 15
  template: "Ontem: X | Hoje: Y | Bloqueio: Z | Ajuda: W"
  owner: "@cro-oracle-guardian"
```

## Completion Criteria

- Plano detalhado cobre 7 dias com foco + owner + entregas por dia
- Meta semanal mensuravel (numero ou marco binario)
- Success criteria final: 3-5 marcos binarios verificaveis
- Gatilhos de correcao definidos para pelo menos 2 cenarios de atraso
- Daily standup configurado com owner
- `wf-kickoff-7-days.yaml` ativado com owners preenchidos

## Handoff

Workflow `wf-kickoff-7-days` assume execucao. CRO monitora via daily standup e aciona `*control-weekly-metrics` ao final do DAY-7.

## Referencias

- `docs/KICKOFF-7-DIAS-REVENUE-OS.md`
- `data/kickoff-7-days-v1.yaml`
- `workflows/wf-kickoff-7-days.yaml`
