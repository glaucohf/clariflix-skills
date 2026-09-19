---
task: agenda()
responsavel: "Agenda"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead qualificado com BANT validado pelo Filtro Agent, disponibilidade do calendário do closer (Google Calendar/Outlook), template de convite por vertical"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Evento criado no calendário com todos os participantes, confirmação enviada por WhatsApp/SMS/email, registro de agendamento no CRM com link do evento, status atualizado para 'Reunião Agendada' no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Filtro Agent emite veredicto VÁLIDO para lead qualificado. Leads que não compareceram à reunião anterior (reagendamento automático). Lembrete D-1 e H-1 da reunião."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Filtro 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3)."
    - "[ ] HITL: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3)."
    - "[ ] HITL: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3)."
    - "[ ] HITL: Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3)."
    - "[ ] HITL: Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation)."
---

# Agendar Reunião

**Task ID:** `agenda()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Agendar Reunião |
| **status** | `pending` |
| **responsible_executor** | Agenda (Agenda (Worker de Agendamento e Booking)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Conduz o fechamento do agendamento da reunião de discovery/demo com o closer humano. Acessa disponibilidade real do calendário, oferece 2-3 opções de horário, envia convite com link de videoconferência, dispara confirmação via WhatsApp/SMS e executa sequência de lembrete (D-1 e H-1). Se prospect não confirmar, reagenda automaticamente até 2x antes de escalar.

## Input

- Lead qualificado com BANT validado pelo Filtro Agent, disponibilidade do calendário do closer (Google Calendar/Outlook), template de convite por vertical

## Output

- Evento criado no calendário com todos os participantes, confirmação enviada por WhatsApp/SMS/email, registro de agendamento no CRM com link do evento, status atualizado para 'Reunião Agendada' no ClickUp

## Trigger

Filtro Agent emite veredicto VÁLIDO para lead qualificado. Leads que não compareceram à reunião anterior (reagendamento automático). Lembrete D-1 e H-1 da reunião.

## Knowledge base (o que o executor consulta)

- Regras de disponibilidade do closer (horários bloqueados, carga máxima de reuniões por dia), templates de mensagem de confirmação por vertical, histórico de no-shows para ajustar cadência de lembrete, integração com Google Calendar/Outlook via MCP

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead qualificado com BANT validado pelo Filtro Agent, disponibilidade do calendário do closer (Google Calendar/Outlook)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Evento criado no calendário com todos os participantes, confirmação enviada por WhatsApp/SMS/email, registro de agendam…) e persistir no artefato do squad.
4. Entregar ao critic Filtro 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Evento criado no calendário com todos os participantes, confirmação enviada por WhatsApp/SMS/email, registro de agendamento no CRM com link do evento, status a…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Filtro 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3).
- [ ] Gate HITL respeitado: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3).
- [ ] Gate HITL respeitado: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3).

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3). | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3). | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3). | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3). | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation). | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Confirmação de reagendamento quando prospect cancela reunião pela segunda vez consecutiva (decisão humana sobre continuar ou desqualificar — L3). | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibragem quinzenal de voz e persona do Vox Agent com gestor de vendas (revisão humana de amostras de áudio — L1). | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Filtro 2 | BLOQUEIA entrega |

## Handoff

- **to:** Eco
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
