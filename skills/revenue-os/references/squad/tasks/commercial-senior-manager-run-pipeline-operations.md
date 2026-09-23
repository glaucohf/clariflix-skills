---
task: Run Pipeline Operations
responsavel: "@commercial-senior-manager"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - sales_target_tree: Metas comerciais (saida do CCO)
  - weekly_quotas: Quotas semanais por executor
  - crm_state: Estado atual do pipeline CRM
Saida: |
  - pipeline_ops_plan: Plano operacional com rotinas diarias e semanais
  - daily_standup_agenda: Agenda de standup diario
  - escalation_rules: Regras de escalacao para deals travados
Checklist:
  - "[ ] Distribuir metas por estagio do pipeline"
  - "[ ] Definir rotina diaria (standup, prospeccao, demos, follow-up)"
  - "[ ] Definir regras de escalacao"
  - "[ ] Sync semanal com @cco-commercial-director"
---

# *run-pipeline-operations

Transforma estrategia comercial em operacao diaria de pipeline executada pelos analysts.

## Step-by-Step

1. **Absorver metas e quotas** — Ler `sales_target_tree` + `weekly_quotas`.
2. **Mapear pipeline CRM atual** — Quantos deals em cada estagio. Volume por owner.
3. **Definir volume alvo por estagio** — Para bater meta de vendas, quanto precisa ter em cada estagio do pipeline (3-4x cobertura).
4. **Montar rotina diaria:**
   - 09:00 Standup 15 min
   - 09:15-12:00 Prospeccao + primeiro contato
   - 13:00-17:00 Demos + follow-up
   - 17:00-17:30 Atualizacao CRM
5. **Definir rotina semanal** — Sync segunda (planejamento) + sexta (retro).
6. **Criar regras de escalacao** — Deal sem movimento por X dias -> manager intervem.
7. **Instrumentar** — Pipeline view no dashboard com alertas automaticos.

## Veto Conditions

- VETO se cobertura do pipeline for <2x da meta → historicamente deals morrem, precisa de 3x+
- VETO se rotina diaria nao tiver block para prospeccao → pipeline nao se alimenta sozinho
- VETO se regras de escalacao permitirem deals >21 dias parados sem acao

## Output Example

```yaml
pipeline_ops_plan:
  meta_mensal: "R$ 48k MRR novo = 11 vendas"
  cobertura_necessaria: "33-44 deals em pipeline ativo"

  pipeline_por_estagio:
    lead_qualificado: { target: 200, atual: 180 }
    demo_agendada: { target: 44, atual: 35 }
    demo_realizada: { target: 33, atual: 28 }
    proposta_enviada: { target: 22, atual: 18 }
    fechamento: { target: 11, atual: 8 }

  rotina_diaria:
    - horario: "09:00"
      atividade: "Standup 15 min"
      owner: "@commercial-senior-manager"
    - horario: "09:15-12:00"
      atividade: "Prospeccao + primeiro contato novos leads"
      owner: "@commercial-senior-analyst"
    - horario: "13:00-17:00"
      atividade: "Demos + follow-up + propostas"
      owner: "@commercial-senior-analyst"
    - horario: "17:00-17:30"
      atividade: "Atualizacao CRM (obrigatorio)"
      owner: "Todos"

  rotina_semanal:
    segunda_manha: "Planejamento semanal (60 min)"
    sexta_tarde: "Retro semanal (30 min)"
    quinta_tarde: "1:1 com @cco-commercial-director (30 min)"

escalation_rules:
  - trigger: "Deal sem movimento por 7 dias"
    acao: "Analyst revisa e adiciona nota de status"
  - trigger: "Deal sem movimento por 14 dias"
    acao: "Manager intervem, call com prospect"
  - trigger: "Deal sem movimento por 21 dias"
    acao: "Marcar como stalled, mover para nurturing"

daily_standup_agenda:
  template: "Ontem: X deals | Hoje: Y deals | Bloqueio: Z"
  duracao_min: 15
  participantes: ["@commercial-senior-manager", "@commercial-senior-analyst"]
```

## Completion Criteria

- Pipeline com cobertura ≥3x da meta
- Rotina diaria com blocos de prospeccao + demos + follow-up
- Regras de escalacao com triggers de 7/14/21 dias
- Sync semanal com CCO agendado

## Handoff

Rotina ativada. Metricas sobem no dashboard. Reporta para `@cco-commercial-director` semanalmente.
