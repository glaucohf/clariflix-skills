---
task: Automate Follow-Up
responsavel: "@sales-system-operator"
responsavel_type: agent
atomic_layer: task
version: "1.1.0"
Entrada: |
  - sales_playbook: Pipeline + regras
  - communication_channels: Email, WhatsApp, CRM, SMS
  - follow_up_sequences: Sequencias definidas no setup-inbound
Saida: |
  - automation_rules: Regras de triggers + condicoes + actions
  - manual_fallback: Fallbacks manuais para casos especiais
  - automation_dashboard: Dashboard de performance das automacoes
Checklist:
  - "[ ] Definir triggers por estagio e tempo"
  - "[ ] Definir condicoes de parada (cliente respondeu, unsubscribe)"
  - "[ ] Definir fallback manual quando auto falha"
  - "[ ] Configurar dashboard de performance"
  - "[ ] Testar cada automacao antes de ativar"
---

# *automate-follow-up

Automatiza follow-up comercial sem perder controle de contexto e qualidade.

## Step-by-Step

1. **Mapear sequencias** — Listar todas as sequencias do `setup-inbound-closing-machine`.
2. **Para cada sequencia, definir triggers** — O que dispara? (form submit, demo done, deal parado X dias).
3. **Definir condicoes de parada** — O que interrompe a sequencia? (cliente respondeu, fechou, cancelou).
4. **Implementar no CRM** — Configurar workflows/automations no tool (HubSpot, Pipedrive, etc).
5. **Testar em QA** — Rodar cada automacao em ambiente de teste antes de produzir.
6. **Definir fallback manual** — Se automacao falhar, analyst recebe task.
7. **Configurar dashboard** — Visibilidade de quantos leads estao em cada sequencia + performance.

## Veto Conditions

- VETO se automacao nao tiver condicao de parada → prospect recebe email depois de ja ter fechado = ridiculo
- VETO se ativar automacao em producao sem QA → risco alto de bugs que queimam leads
- VETO se >50% dos leads estiverem em sequencia automatica sem touch humano → robotiza demais
- VETO se nao houver dashboard → automacao vira caixa preta

## Output Example

```yaml
automation_rules:
  - id: AUTO-01
    nome: "Welcome + Discovery"
    trigger: "Lead entra no CRM via form demo LP"
    condicoes:
      - "lead.origem = 'lp-demo'"
      - "lead.sla_primeira_resposta_humana < 15 min (se nao, escalar)"
    acoes_imediatas:
      - "Enviar email auto-reply (snippet_001)"
      - "Criar task 'responder em 15 min' para analyst"
      - "Notificar Slack #sales-team"
    condicoes_parada:
      - "Analyst respondeu manualmente"
      - "Lead agendou demo"
      - "Lead pediu unsubscribe"

  - id: AUTO-02
    nome: "Pre-demo reminder"
    trigger: "Demo agendada para daqui 1h"
    condicoes:
      - "demo.status = 'agendada'"
    acoes:
      - "Enviar email prep (snippet_003)"
      - "Enviar SMS lembrete (se opt-in)"
    condicoes_parada:
      - "Demo cancelada"
      - "Demo remarcada"

  - id: AUTO-03
    nome: "Pos-demo nurturing"
    trigger: "Demo realizada ha 3 dias sem proposta fechada"
    condicoes:
      - "deal.estagio = 'proposta_enviada'"
      - "deal.ultima_atividade >= 3 dias"
    acoes:
      - "Enviar email follow-up D+3 (snippet_005)"
      - "Criar task para analyst monitorar"
    condicoes_parada:
      - "Cliente respondeu"
      - "Deal fechado won/lost"

  - id: AUTO-04
    nome: "Close-loop D+14"
    trigger: "Deal em proposta_enviada ha 14 dias sem resposta"
    condicoes:
      - "deal.estagio = 'proposta_enviada'"
      - "deal.ultima_atividade >= 14 dias"
    acoes:
      - "Enviar email close-loop (snippet_007)"
      - "Enviar WhatsApp (se opt-in)"
      - "Se 3 dias sem resposta: marcar como lost + razao"

  - id: AUTO-05
    nome: "Onboarding pos-venda"
    trigger: "Payment completed"
    condicoes:
      - "customer.status = 'new'"
    acoes_sequenciais:
      - dia_0: "Welcome email + link onboarding"
      - dia_1: "Task analyst: ligar confirmando acesso"
      - dia_3: "Email 'primeiro milestone'"
      - dia_7: "Email 'primeiro resultado'"
      - dia_14: "Email NPS + call agendada"

manual_fallback:
  - cenario: "Automacao falhou ao enviar email"
    acao: "Task automatica para analyst com template"
    sla_fallback: "2h horario comercial"

  - cenario: "Cliente respondeu de forma ambigua a email automatico"
    acao: "Analyst recebe alert para responder pessoalmente"

  - cenario: "Deal tem valor > R$ 5k/mes"
    acao: "Automacoes pausadas, analyst faz touch 100% manual"
    razao: "Deals grandes exigem tratamento personalizado"

automation_dashboard:
  metricas:
    - "Leads em cada sequencia ativa"
    - "Open rate por automacao"
    - "Click rate por automacao"
    - "% leads que convertem com touch humano vs 100% auto"
    - "Tempo medio por estagio (velocity)"

  alertas:
    - "Open rate < 30% em automacao por 7 dias -> review copy"
    - "Unsubscribe rate > 5% em sequencia -> pausar"
    - "Bounce rate > 3% -> validar email list"
```

## Completion Criteria

- 5+ automacoes configuradas cobrindo todo o ciclo (welcome + nurturing + close-loop + onboarding)
- Cada automacao tem condicao de parada clara
- Fallback manual em 3+ cenarios
- Dashboard com metricas e alertas

## Handoff

`@revops-automation-engineer` implementa tecnicamente no CRM + email tool. `@commercial-senior-analyst` monitora alertas. Review semanal do dashboard.
