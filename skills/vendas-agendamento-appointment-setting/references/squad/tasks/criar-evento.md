---
task: slot()
responsavel: "Slot"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead qualificado (qualification_score >= threshold configurado), slot_preference do Radar, acesso ao calendário do vendedor via API (Google Calendar / Outlook / Calendly), link de videochamada configurado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Evento criado no calendário com: título, participantes, link de vídeo, descrição com contexto do lead"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "CRM atualizado com deal stage = 'Reunião Agendada', campo meeting_date preenchido"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Mensagem de confirmação enviada ao lead pelo canal preferido"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato: booking_confirmation.json com todos os dados do agendamento"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro roteia lead com status BOOK_NOW vindo do Radar. Lead responde positivamente a uma mensagem de outreach com intenção de agendar. HITL aprova agendamento em conta estratégica (L3 bypass)."
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

# Criar Evento

**Task ID:** `slot()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Agendamento — Appointment Setting

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Criar Evento |
| **status** | `pending` |
| **responsible_executor** | Slot (Slot — Worker de Agendamento e Booking) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Condutor direto do lead ao booking. Acessa o calendário do closer/vendedor em tempo real, apresenta 2-3 opções de horários (nunca mais que 3 para não gerar paralisia), captura a escolha do lead, cria o evento no calendário, envia convite com link de videochamada (Meet/Zoom/Teams) e registra o agendamento no CRM. Trata conflitos de timezone automaticamente. Nunca empurra horários fora da janela de disponibilidade configurada.

## Input

- Lead qualificado (qualification_score >= threshold configurado), slot_preference do Radar, acesso ao calendário do vendedor via API (Google Calendar / Outlook / Calendly), link de videochamada configurado

## Output

- Evento criado no calendário com: título, participantes, link de vídeo, descrição com contexto do lead
- CRM atualizado com deal stage = 'Reunião Agendada', campo meeting_date preenchido
- Mensagem de confirmação enviada ao lead pelo canal preferido
- Artefato: booking_confirmation.json com todos os dados do agendamento

## Trigger

Maestro roteia lead com status BOOK_NOW vindo do Radar. Lead responde positivamente a uma mensagem de outreach com intenção de agendar. HITL aprova agendamento em conta estratégica (L3 bypass).

## Knowledge base (o que o executor consulta)

- Regras de disponibilidade do closer/vendedor (horários bloqueados, capacidade máxima de reuniões/dia, buffer entre reuniões), templates de mensagem de confirmação por canal (WhatsApp, email), mapeamento de timezones por região do cliente, política de duração de reuniões por tipo (demo = 30min, discovery = 45min, closing = 60min)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead qualificado (qualification_score >= threshold configurado), slot_preference do Radar, acesso ao calendário do vend…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Evento criado no calendário com: título, participantes, link de vídeo, descrição com contexto do lead) e persistir no artefato do squad.
4. Entregar ao critic Sentinela; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Evento criado no calendário com: título, participantes, link de vídeo, descrição com contexto do lead
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

- **to:** Vigil
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
