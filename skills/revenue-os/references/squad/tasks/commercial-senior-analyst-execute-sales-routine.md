---
task: Execute Sales Routine
responsavel: "@commercial-senior-analyst"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - pipeline_ops_plan: Plano operacional do manager
  - daily_quota: Quotas do dia (prospeccao, demos, follow-up)
  - crm_access: Acesso ao CRM com leads do dia
Saida: |
  - sales_execution_log: Log diario de execucao com numeros
  - updated_crm: CRM atualizado com status de cada deal
  - objections_log: Objecoes encontradas no dia
Checklist:
  - "[ ] Executar blocos de prospeccao, demos e follow-up conforme rotina"
  - "[ ] Atualizar CRM apos cada interacao"
  - "[ ] Registrar objecoes para virarem material de treino"
  - "[ ] Reportar no standup diario"
---

# *execute-sales-routine

Executa a rotina comercial do dia seguindo o plano operacional.

## Step-by-Step

1. **Preparar o dia (08:45-09:00)** — Revisar CRM, identificar deals que precisam acao hoje.
2. **Standup 09:00 (15 min)** — Reportar ontem/hoje/bloqueio.
3. **Bloco prospeccao (09:15-12:00)** — Contato com leads novos + qualificacao. Meta: X leads/dia.
4. **Bloco demos (13:00-15:00)** — Agendadas previamente. Seguir playbook de demo.
5. **Bloco follow-up (15:00-17:00)** — Deals em negociacao, responder objecoes, enviar propostas.
6. **Atualizacao CRM (17:00-17:30)** — Obrigatorio. Todo deal tocado no dia deve ter update.
7. **Log objecoes + async report** — Objecoes novas no documento compartilhado + update no canal.

## Veto Conditions

- VETO se CRM nao for atualizado no mesmo dia → dados desatualizados destroem dashboard
- VETO se pular bloco de prospeccao por "nao ter tempo" → pipeline morre
- VETO se demo sair do playbook sem motivo documentado → inconsistencia mata conversao

## Output Example

```yaml
sales_execution_log:
  data: "2026-05-06"
  owner: "@commercial-senior-analyst"

  prospeccao:
    leads_contactados: 28
    qualificados: 11
    nao_qualificados: 17
    quota_dia: 25
    atingida: "Sim (112%)"

  demos:
    agendadas: 3
    realizadas: 2
    no_show: 1
    follow_up_pos_demo_enviado: 2

  follow_up:
    deals_movidos: 5
    propostas_enviadas: 2
    fechamentos: 1
    mrr_novo: "R$ 3.000"

  tempo_resposta:
    sla_target: "<15 min"
    sla_atingido_dia: "12 min (mediana)"

objections_log:
  - objecao: "Nao tenho time para rodar o squad"
    frequencia_dia: 3
    resposta_usada: "Nossa proposta e guiada: voce executa com o squad te dizendo o proximo passo"
    convertida: "1 de 3"

  - objecao: "Preco alto pra minha fase"
    frequencia_dia: 2
    resposta_usada: "Desconto de 30% nos 3 primeiros meses com commit de 6 meses"
    convertida: "0 de 2"

updated_crm:
  deals_atualizados: 19
  novos_deals: 11
  movidos_para_proximo_estagio: 5
  marcados_stalled: 2
```

## Completion Criteria

- Quota diaria atingida (>=90%)
- CRM 100% atualizado no mesmo dia
- Objecoes logadas com frequencia e taxa de conversao
- Log entregue no canal ate 17:30

## Handoff

Log alimenta dashboard que `@commercial-senior-manager` revisa na retro semanal. Objecoes viram material para treino e backlog de produto.
