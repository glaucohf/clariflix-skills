---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead identificado com nome, canal de entrada, histórico de mensagens (se houver) e fonte de aquisição"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Contexto do ICP (Ideal Customer Profile) do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON com: qualification_score (0-100), bant_summary {budget, authority, need, timing}, lead_profile {cargo, empresa, dor_principal, urgência}, recommendation (BOOK_NOW | NURTURE | DISQUALIFY), suggested_slot_preference (período do dia, dia da semana)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo lead entra no CRM com status 'novo' ou 'a qualificar'. Formulário de landing page submetido. Lead reativado do nurture com engajamento detectado."
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

# Qualificar Lead Conversacionalmente

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Agendamento — Appointment Setting

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Qualificar Lead Conversacionalmente |
| **status** | `pending` |
| **responsible_executor** | Radar (Rádar — Worker de Qualificação Conversacional) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Conduz a qualificacao do lead via conversa natural (WhatsApp, chat ou email) usando framework BANT/SPIN adaptado ao contexto do cliente. Determina se o lead tem Budget, Authority, Need e Timing suficientes para ir direto ao agendamento ou se precisa de nurture. Produz um score de qualificacao e um resumo do perfil do lead para o Maestro e para o Worker de Agendamento.

## Input

- Lead identificado com nome, canal de entrada, histórico de mensagens (se houver) e fonte de aquisição
- Contexto do ICP (Ideal Customer Profile) do cliente

## Output

- JSON com: qualification_score (0-100), bant_summary {budget, authority, need, timing}, lead_profile {cargo, empresa, dor_principal, urgência}, recommendation (BOOK_NOW | NURTURE | DISQUALIFY), suggested_slot_preference (período do dia, dia da semana)

## Trigger

Novo lead entra no CRM com status 'novo' ou 'a qualificar'. Formulário de landing page submetido. Lead reativado do nurture com engajamento detectado.

## Knowledge base (o que o executor consulta)

- ICP do cliente (criterios de qualificação), scripts de qualificação BANT/SPIN personalizados, histórico de conversas anteriores do lead (CRM), FAQs do produto/serviço para responder objeções iniciais, regras de disqualificação imediata (ex: concorrente, fora do território)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead identificado com nome, canal de entrada, histórico de mensagens (se houver) e fonte de aquisição).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON com: qualification_score (0-100), bant_summary {budget, authority, need, timing}, lead_profile {cargo, empresa, do…) e persistir no artefato do squad.
4. Entregar ao critic Sentinela; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON com: qualification_score (0-100), bant_summary {budget, authority, need, timing}, lead_profile {cargo, empresa, dor_principal, urgência}, recommendation (…
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

- **to:** Slot
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
