---
task: agenda()
responsavel: "Agenda"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de no-show ou cancelamento do calendario"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "disponibilidade do calendário do closer"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "preferencias de horario do lead (se conhecidas)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem de re-agendamento enviada com link de booking direto ou 3 opções de horário"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Reunião re-agendada confirmada no CRM e no calendário"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Série de reminders criada para o novo horário"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato no ClickUp: 'Agenda-NoShow-{lead_id}-{timestamp}' com status (reagendado, sem resposta, recusou)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de no-show do calendário (reunião não iniciada 10min após horário); evento de cancelamento; 24h e 1h antes de reunião confirmada (trigger de reminder)"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vigia 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou edita antes do envio pelo Volta"
    - "[ ] L3: Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio"
    - "[ ] L3: Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar"
    - "[ ] L3: Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordagem antes de qualquer novo toque"
    - "[ ] HITL: Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão manual"
---

# Reagendar Reuniões

**Task ID:** `agenda()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reagendar Reuniões |
| **status** | `pending` |
| **responsible_executor** | Agenda (Agenda — Worker de Re-agendamento e Booking) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em no-shows e re-agendamento. Quando um lead não comparece a uma reunião ou cancela com antecedência, Agenda entra em ação imediatamente com uma sequência específica de re-agendamento: WhatsApp nos primeiros 5 minutos, email em 2h, segunda tentativa de WhatsApp em 24h com 3 opções de horário diretas. Integra com Google Calendar/Outlook/Calendly para checar disponibilidade em tempo real e oferecer slots diretamente na mensagem. Também envia reminders pré-reunião (24h + 1h antes) para reduzir no-shows futuros.

## Input

- Evento de no-show ou cancelamento do calendario
- disponibilidade do calendário do closer
- preferencias de horario do lead (se conhecidas)

## Output

- Mensagem de re-agendamento enviada com link de booking direto ou 3 opções de horário
- Reunião re-agendada confirmada no CRM e no calendário
- Série de reminders criada para o novo horário
- Artefato no ClickUp: 'Agenda-NoShow-{lead_id}-{timestamp}' com status (reagendado, sem resposta, recusou)

## Trigger

Webhook de no-show do calendário (reunião não iniciada 10min após horário); evento de cancelamento; 24h e 1h antes de reunião confirmada (trigger de reminder)

## Knowledge base (o que o executor consulta)

- Regras de re-agendamento por urgência (lead quente = até 3 tentativas em 48h
- lead morno = 2 tentativas em 5 dias)
- scripts de re-agendamento por motivo (esqueceu, conflito, não viu o link)
- integração com calendário do time de vendas
- horários de pico de resposta por perfil de lead

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de no-show ou cancelamento do calendario).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagem de re-agendamento enviada com link de booking direto ou 3 opções de horário) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagem de re-agendamento enviada com link de booking direto ou 3 opções de horário
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vigia 2 registrado
- [ ] Gate L3 respeitado: Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico;…
- [ ] Gate L3 respeitado: Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio
- [ ] Gate L3 respeitado: Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualifi…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou ed… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordag… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão semanal de cadências — Atlas gera relatório de performance; gestor aprova ajustes de parâmetros (intervalos, canais, thresholds de score) antes de sere… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out recebido — Qualquer pedido de descadastro é interrompido imediatamente pelo Cronos e notificado ao responsável para confirmação de remoção do CRM | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Vigia 2 | BLOQUEIA entrega |

## Handoff

- **to:** Memento
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
