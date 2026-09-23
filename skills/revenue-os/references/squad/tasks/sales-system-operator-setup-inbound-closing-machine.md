---
task: Setup Inbound Closing Machine
responsavel: "@sales-system-operator"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - crm_pipeline: Estagios e definicoes do CRM (saida do playbook)
  - offer_objections: Objection matrix (saida do monetization)
  - sales_playbook: Playbook completo com scripts
Saida: |
  - inbound_closing_system: Sistema de fechamento inbound com scripts e automacoes
  - sla_and_escalation: SLA de resposta + regras de escalacao
  - follow_up_sequences: Sequencias de follow-up por estagio
Checklist:
  - "[ ] Script de discovery e fechamento integrados ao CRM"
  - "[ ] Rotina de follow-up por janela definida (3, 7, 14 dias)"
  - "[ ] Escalacao para casos criticos (deal travado >14d)"
  - "[ ] Automatizacao de lembretes + tarefas no CRM"
  - "[ ] Integracao com email + chat + telefone"
---

# *setup-inbound-closing-machine

Configura operacao de fechamento inbound com previsibilidade de resposta e conversao alta.

## Step-by-Step

1. **Mapear touchpoints inbound** — Formularios, chat, demo request, email de interesse.
2. **Configurar resposta imediata** — Primeira resposta automatica em <2 min + resposta humana em <15 min.
3. **Integrar scripts ao CRM** — Discovery + demo + fechamento como snippets/templates.
4. **Criar sequencias de follow-up** — 3 dias, 7 dias, 14 dias com conteudo especifico por janela.
5. **Definir escalacao** — Deal parado >14 dias escala para manager. >21 dias revisao executiva.
6. **Automatizar lembretes** — Tasks automaticas no CRM (ligar dia X, enviar email dia Y).
7. **Instrumentar tudo** — Dashboard com SLA, velocity, conversion por estagio.

## Veto Conditions

- VETO se SLA de primeira resposta >15 min → prospect esfria, conversao cai drasticamente
- VETO se automatizacao disparar >3 touchpoints em mesmo dia → percepcao de spam
- VETO se escalacao para manager for subjetiva → precisa trigger automatico
- VETO se scripts nao estiverem acessiveis durante call → analyst improvisa

## Output Example

```yaml
inbound_closing_system:
  touchpoints_ativos:
    - tipo: "Form demo LP"
      sla_primeira_resposta: "15 min humana + auto-reply imediato"
      fluxo: "form -> CRM -> Slack alert -> analyst responde"

    - tipo: "Chat widget LP"
      sla_primeira_resposta: "2 min (horario comercial)"
      fallback: "Fora horario: auto-reply + contato na manha seguinte"

    - tipo: "Email direto inbound"
      sla_primeira_resposta: "2h horario comercial"

  scripts_no_crm:
    snippet_id_001: "Primeira resposta demo request"
    snippet_id_002: "Discovery questions (7 perguntas BANT)"
    snippet_id_003: "Demo prep email (envio 1h antes)"
    snippet_id_004: "Proposta template personalizavel"
    snippet_id_005: "Close follow-up D+3"
    snippet_id_006: "Close follow-up D+7"
    snippet_id_007: "Close follow-up D+14 + close-loop"

follow_up_sequences:
  pos_demo_nao_fechado:
    - dia: 3
      canal: email
      objetivo: "Recap da demo + proposta enviada, duvidas?"
      template: "snippet_id_005"

    - dia: 7
      canal: email
      objetivo: "Tratar objecao comum + urgencia soft"
      template: "snippet_id_006"

    - dia: 14
      canal: email + whatsapp
      objetivo: "Close-loop - ultima chamada"
      template: "snippet_id_007"
      se_nao_responder: "Marcar como lost com razao"

  pos_proposta_sem_checkout:
    - dia: 1
      canal: email
      objetivo: "Confirmar recebimento proposta + oferecer call de duvidas"

    - dia: 3
      canal: email
      objetivo: "Tratar objecoes esperadas"

    - dia: 7
      canal: email + whatsapp
      objetivo: "Urgencia + bonus (se aplicavel)"

sla_and_escalation:
  slas:
    primeira_resposta: "15 min (horario comercial)"
    envio_proposta_pos_demo: "24h"
    resposta_duvidas_prospect: "2h horario comercial"

  escalacao:
    trigger_1:
      condicao: "Deal sem movimento por 7 dias"
      acao: "Analyst adiciona nota + tenta novo contato"
      owner: "@commercial-senior-analyst"

    trigger_2:
      condicao: "Deal sem movimento por 14 dias"
      acao: "Manager intervem, call pessoal"
      owner: "@commercial-senior-manager"

    trigger_3:
      condicao: "Deal sem movimento por 21 dias"
      acao: "Review executivo, decide revive ou lost"
      owner: "@cco-commercial-director"

    trigger_4:
      condicao: "Objecao de preco em >3 deals/semana"
      acao: "Review pricing com @monetization-strategist"
      owner: "@commercial-senior-manager"

automacoes:
  - trigger: "Novo lead via form"
    acoes: ["Criar deal CRM", "Notificar analyst Slack", "Auto-reply email"]

  - trigger: "Demo agendada"
    acoes: ["Prep email 1h antes", "Task no CRM para analyst", "Block no calendario"]

  - trigger: "Demo realizada"
    acoes: ["Task envio proposta 24h", "Atualizar estagio CRM", "Tag 'demo-done'"]

  - trigger: "Proposta sem abertura por 3 dias"
    acoes: ["Task follow-up", "Notificar analyst"]
```

## Completion Criteria

- SLA primeira resposta <15 min configurado
- Scripts disponiveis como snippets no CRM
- Sequencias de follow-up (3 janelas) configuradas
- Escalacao automatica em 3 triggers (7, 14, 21 dias)
- Dashboard com SLA + velocity + conversion

## Handoff

`@commercial-senior-analyst` opera o sistema. `@revops-automation-engineer` implementa automacoes no CRM. Review semanal em `*run-pipeline-operations`.
