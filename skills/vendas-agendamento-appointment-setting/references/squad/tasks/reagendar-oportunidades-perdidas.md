---
task: bounce()
responsavel: "Bounce"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de no-show ou cancelamento do calendário (webhook)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Status de confirmation_status = NO_SHOW do Vigil"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Histórico de tentativas anteriores de reagendamento para o mesmo lead"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Nova opcao de horarios enviada ao lead com mensagem personalizada (tom empatico, nao chato)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "CRM atualizado com noshow_reason (se capturado), reschedule_attempt_count"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Se limite de tentativas atingido: lead movido para status NURTURE e notificacao ao vendedor"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato: reschedule_attempt.json"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook do calendário: evento marcado como no-show ou cancelado. Vigil envia alerta de AT_RISK sem confirmação T-4h. Maestro detecta lead em stall pós-agendamento."
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

# Reagendar Oportunidades Perdidas

**Task ID:** `bounce()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Agendamento — Appointment Setting

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reagendar Oportunidades Perdidas |
| **status** | `pending` |
| **responsible_executor** | Bounce (Bounce – Worker de Reagendamento e Recuperação) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em recuperar oportunidades perdidas. Atua em dois cenários: (1) Lead cancela ou não comparece — inicia sequência de reagendamento com janela de opções em até 2h após o no-show; (2) Lead não responde aos lembretes — inicia cadência de reativação com nova proposta de horário. Limita tentativas conforme política (padrão: 3 tentativas de reagendamento antes de mover para nurture). Registra motivo do no-show quando capturado.

## Input

- Evento de no-show ou cancelamento do calendário (webhook)
- Status de confirmation_status = NO_SHOW do Vigil
- Histórico de tentativas anteriores de reagendamento para o mesmo lead

## Output

- Nova opcao de horarios enviada ao lead com mensagem personalizada (tom empatico, nao chato)
- CRM atualizado com noshow_reason (se capturado), reschedule_attempt_count
- Se limite de tentativas atingido: lead movido para status NURTURE e notificacao ao vendedor
- Artefato: reschedule_attempt.json

## Trigger

Webhook do calendário: evento marcado como no-show ou cancelado. Vigil envia alerta de AT_RISK sem confirmação T-4h. Maestro detecta lead em stall pós-agendamento.

## Knowledge base (o que o executor consulta)

- Templates de mensagem de reagendamento por contexto (no-show vs cancelamento antecipado vs sem resposta), política de tentativas e intervalos (ex: tentativa 1 em 2h, tentativa 2 em D+1, tentativa 3 em D+3), scripts de abordagem empática para não queimar o lead, regras de quando desistir e mover para nurture

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de no-show ou cancelamento do calendário (webhook)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Nova opcao de horarios enviada ao lead com mensagem personalizada (tom empatico, nao chato)) e persistir no artefato do squad.
4. Entregar ao critic Sentinela; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Nova opcao de horarios enviada ao lead com mensagem personalizada (tom empatico, nao chato)
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

- **to:** Intell
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
