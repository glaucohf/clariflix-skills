---
task: vigil()
responsavel: "Vigil"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "booking_confirmation.json do Slot"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Preferência de canal do lead (WhatsApp prioritário no Brasil)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Janela de horários da reunião"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Registro de cada lembrete enviado com timestamp, canal e status de entrega/leitura"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "CRM atualizado com confirmation_status (CONFIRMED | PENDING | AT_RISK)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alerta para Maestro se lead não confirmou até T-4h (alto risco de no-show)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato: reminder_log.json"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Agendamento criado pelo Slot (disparo imediato). Scheduler interno: 24h antes, 2h antes, no horário. CRM webhook: reunião próxima sem confirmação."
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

# Enviar Lembretes Agendados

**Task ID:** `vigil()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Agendamento — Appointment Setting

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Lembretes Agendados |
| **status** | `pending` |
| **responsible_executor** | Vigil (Vigil — Worker de Confirmação e Lembrete) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Guardian anti-no-show. Executa sequência automática de lembretes após o agendamento: confirmação imediata (T+0), lembrete D-1 (24h antes), lembrete H-2 (2h antes) e mensagem de 'estamos te esperando' H-0 (no horário). Detecta ausência de confirmação e escala para reagendamento proativo. Monitora se o lead abriu o convite do calendário. Registra status de confirmação no CRM.

## Input

- booking_confirmation.json do Slot
- Preferência de canal do lead (WhatsApp prioritário no Brasil)
- Janela de horários da reunião

## Output

- Registro de cada lembrete enviado com timestamp, canal e status de entrega/leitura
- CRM atualizado com confirmation_status (CONFIRMED | PENDING | AT_RISK)
- Alerta para Maestro se lead não confirmou até T-4h (alto risco de no-show)
- Artefato: reminder_log.json

## Trigger

Agendamento criado pelo Slot (disparo imediato). Scheduler interno: 24h antes, 2h antes, no horário. CRM webhook: reunião próxima sem confirmação.

## Knowledge base (o que o executor consulta)

- Templates de lembrete por canal e tom (urgente vs amigável), política de frequência (max X mensagens para não spam), horários de silêncio (não enviar entre 22h-8h), histórico de preferência de comunicação do lead, link do calendário e da videochamada para incluir nos lembretes

## Action Items

1. Confirmar o gatilho e carregar a entrada (booking_confirmation.json do Slot).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Registro de cada lembrete enviado com timestamp, canal e status de entrega/leitura) e persistir no artefato do squad.
4. Entregar ao critic Sentinela; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Registro de cada lembrete enviado com timestamp, canal e status de entrega/leitura
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

- **to:** Bounce
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
