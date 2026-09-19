---
task: maestroPipeline()
responsavel: "Maestro"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Booking Confirmation Package"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "artefato verificavel gerado para cada reuniao realizada, contendo: booking_confirmation.json (dados do evento), reminder_log.json (historico de lembretes enviados), pre_meeting_brief.md (dossie do lead para o closer), lead_priority_queue.json (snapshot do score no momento do agendamento), e validation_log.json do Sentinela (prova de que todas as mensagens passaram pelo critic)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Disponivel no CRM e no ClickUp como task concluida com todos os artefatos anexados"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe o sinal de entrada (lead qualificado, formulário submetido, intenção detectada no CRM ou WhatsApp), decompõe a jornada de agendamento em subtarefas atômicas, roteia para os workers corretos, m…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinela antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar abordagem e personalização antes do envio."
    - "[ ] L3: Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial fora da política padrão)."
    - "[ ] L3: Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nova tentativa."
    - "[ ] L2: Notificação ao closer/SDR quando lead muda de COLD para HOT (score sobe 30+ pontos em 24h) para decisão de abordar manualmente em vez de deixar o squad rodar sozinho."
    - "[ ] L2: Alerta ao gerente de vendas quando taxa de no-show da semana ultrapassar threshold configurado (ex: >20%) — indica problema sistêmico que requer revisão de ICP ou abordagem."
---

# Orquestrar Pipeline do Agendamento

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Agendamento — Appointment Setting

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Agendamento |
| **status** | `pending` |
| **responsible_executor** | Maestro (Maestro — Orquestrador de Agendamento) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o sinal de entrada (lead qualificado, formulário submetido, intenção detectada no CRM ou WhatsApp), decompõe a jornada de agendamento em subtarefas atômicas, roteia para os workers corretos, mantém o estado do lead no funil (aguardando confirmação, confirmado, lembrete enviado, no-show, reagendado), detecta stalls (lead parou de responder) e dispara sequências de recuperação. Opera como state machine: cada estado do lead tem transições definidas e o Maestro é o guardian dessas transições.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Booking Confirmation Package
- artefato verificavel gerado para cada reuniao realizada, contendo: booking_confirmation.json (dados do evento), reminder_log.json (historico de lembretes enviados), pre_meeting_brief.md (dossie do lead para o closer), lead_priority_queue.json (snapshot do score no momento do agendamento), e validation_log.json do Sentinela (prova de que todas as mensagens passaram pelo critic)
- Disponivel no CRM e no ClickUp como task concluida com todos os artefatos anexados

## Trigger

Recebe o sinal de entrada (lead qualificado, formulário submetido, intenção detectada no CRM ou WhatsApp), decompõe a jornada de agendamento em subtarefas atômicas, roteia para os workers corretos, mantém o estado do lead no funil (aguardando confirmação, confirmado, lembrete enviado, no-show, reagendado), detecta stalls (lead parou de responder) e dispara sequências de recuperação. Opera como state machine: cada estado do lead tem transições definidas e o Maestro é o guardian dessas transições.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP nativo disponível) ou Pipedrive ou Salesforce
- fonte de verdade de leads, deals e histórico
- Calendário: Google Calendar API ou Microsoft Outlook/Graph API
- leitura de disponibilidade e criação de eventos
- Agendamento: Calendly API (alternativa ao calendário direto, mais simples para B2C)
- WhatsApp Business API: Gupshup, AiSensy ou Interakt
- canal principal de comunicação no Brasil
- Email: SMTP transacional (SendGrid, Resend) ou Gmail API para lembretes e confirmações por email
- Videochamada: Google Meet API ou Zoom API
- geração de link único por reunião
- Enriquecimento: Apollo.io API (275M+ contatos) ou Clay
- dados firmográficos e de contato
- Observabilidade: Langfuse (OTEL)
- rastreamento de todas as tarefas, evals e quality gates
- Gestão de Tarefas: ClickUp
- prova de trabalho por task, artefatos verificáveis
- Notificações Internas: Slack webhook ou email
- alertas de no-show, leads quentes, aprovações L3
- Voz (opcional avançado): Vapi ou Retell AI
- ligação automática de lembrete ou confirmação por voz

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Sentinela antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Booking Confirmation Package
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinela registrado
- [ ] Gate L3 respeitado: Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar…
- [ ] Gate L3 respeitado: Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial…
- [ ] Gate L3 respeitado: Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nov…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar abordagem e persona… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial fora da política pad… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nova tentativa. | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Notificação ao closer/SDR quando lead muda de COLD para HOT (score sobe 30+ pontos em 24h) para decisão de abordar manualmente em vez de deixar o squad rodar s… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Alerta ao gerente de vendas quando taxa de no-show da semana ultrapassar threshold configurado (ex: >20%) — indica problema sistêmico que requer revisão de ICP… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão humana do briefing pre-reunião antes do envio ao closer, opcional mas recomendado nas primeiras 2 semanas de operação do squad para calibragem. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Sentinela | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
