---
task: cadenceDispatcher()
responsavel: "Cadence Dispatcher"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft aprovado pelo Sentinel com metadados (canal, destinatário, timing recomendado, variação A ou B)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Score e tier do lead (Calibre Scorer)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Regras de gate L3 configuradas no onboarding (deal size threshold, segmentos estratégicos, tipos de mensagem que requerem aprovação)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Disponibilidade do calendário via API (Calendly ou Cal.com)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Limites de volume configurados por conta de envio"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Log de envio verificável e imutável no ClickUp por cada mensagem: { message_id, lead_id, channel, variação_ab, sent_at, status (sent / queued / blocked_for_hitl), open_tracked, click_tracked }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Atualização do CRM com activity de outreach (canal, data, mensagem enviada resumida)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para respostas positivas detectadas via webhook: link de booking enviado automaticamente e notificação ao SDR humano para assumir a conversa"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Para gates L3 ativados: notificação ao SDR com draft completo, dossiê e score para aprovação com 1 clique"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Maestro imediatamente após Sentinel aprovar o draft. Triggers de follow-up automático nos dias configurados (D2, D5, D10) se nenhuma resposta detectada. Trigger de oportunidade: lead abr…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR humano com draft completo, dossiê e score para aprovação ou rejeição com 1 clique antes de qualquer disparo."
    - "[ ] HITL: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o feedback detalhado do critic para reescritura manual."
    - "[ ] HITL: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente não envia com informação não verificada."
    - "[ ] HITL: Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para assumir a conversa — o squad nao conduz negociacao, apenas entrega o contexto completo e recua."
    - "[ ] HITL: Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do gestor comercial antes de qualquer envio."
---

# Enviar Mensagens Multicanal

**Task ID:** `cadenceDispatcher()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagens Multicanal |
| **status** | `pending` |
| **responsible_executor** | Cadence Dispatcher (Cadence Dispatcher — O Maestro de Envio) |
| **execution_type** | `Hybrid` |
| **input** | 5 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável pelo envio efetivo das mensagens aprovadas pelo Sentinel e pelo controle de toda a cadência multicanal. Conecta com as APIs dos canais (email via SendGrid/Instantly, LinkedIn via automação controlada, WhatsApp Business API, Vapi para voz). Controla timing de envio por canal e segmento (horários de melhor abertura), volume diário por conta de envio (para não queimar reputação de domínio), sequência de follow-up e booking de reuniões quando lead responde positivamente. Para qualquer envio que atinja os gates L3 configurados (contas estratégicas, mensagens com condição comercial, leads FIRE acima de threshold de deal size): BLOQUEIA completamente e notifica SDR humano com contexto completo antes de enviar um caracter.

## Input

- Draft aprovado pelo Sentinel com metadados (canal, destinatário, timing recomendado, variação A ou B)
- Score e tier do lead (Calibre Scorer)
- Regras de gate L3 configuradas no onboarding (deal size threshold, segmentos estratégicos, tipos de mensagem que requerem aprovação)
- Disponibilidade do calendário via API (Calendly ou Cal.com)
- Limites de volume configurados por conta de envio

## Output

- Log de envio verificável e imutável no ClickUp por cada mensagem: { message_id, lead_id, channel, variação_ab, sent_at, status (sent / queued / blocked_for_hitl), open_tracked, click_tracked }
- Atualização do CRM com activity de outreach (canal, data, mensagem enviada resumida)
- Para respostas positivas detectadas via webhook: link de booking enviado automaticamente e notificação ao SDR humano para assumir a conversa
- Para gates L3 ativados: notificação ao SDR com draft completo, dossiê e score para aprovação com 1 clique

## Trigger

Ativado pelo Maestro imediatamente após Sentinel aprovar o draft. Triggers de follow-up automático nos dias configurados (D2, D5, D10) se nenhuma resposta detectada. Trigger de oportunidade: lead abre email ou clica em link = prioridade imediata para próximo toque na sequência. Trigger de cancelamento: lead responde com opt-out = cancela toda a sequência e atualiza CRM.

## Knowledge base (o que o executor consulta)

- Regras de timing por canal: email (Ter-Qui 9h-11h / 14h-16h melhor abertura para B2B), WhatsApp (horário comercial, sem domingos para B2B), LinkedIn (dias úteis manhã), voz (Ter-Qui 11h-12h / 16h-17h)
- Limites de volume diário: email (max 50/dia por conta nova, 200/dia por conta aquecida), LinkedIn (max 20 connection requests/dia, max 10 InMails/dia)
- Regras de gate L3 configuradas no onboarding
- Política de unsubscribe e opt-out LGPD com registro de consentimento
- Logs de deliverability por domínio para rotação de contas de envio

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft aprovado pelo Sentinel com metadados (canal, destinatário, timing recomendado, variação A ou B)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Log de envio verificável e imutável no ClickUp por cada mensagem: { message_id, lead_id, channel, variação_ab, sent_at,…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Log de envio verificável e imutável no ClickUp por cada mensagem: { message_id, lead_id, channel, variação_ab, sent_at, status (sent / queued / blocked_for_hit…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloquei…
- [ ] Gate HITL respeitado: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para…
- [ ] Gate HITL respeitado: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR h… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o f… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente nã… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para a… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ICP Cartografo detecta shift significativo de mercado (nova objecao emergindo em >30% das respostas, queda de >20% no reply rate em 2 semanas consecutivas): al… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out ou resposta negativa agressiva: processado pelo Pulse Analyst, sequência cancelada automaticamente, CRM atualizado, notificação ao SDR para decisão sob… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Pulse Analyst
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
