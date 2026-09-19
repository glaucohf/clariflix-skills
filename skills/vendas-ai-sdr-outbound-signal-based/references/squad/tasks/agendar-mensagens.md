---
task: vox()
responsavel: "Vox"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft aprovado pelo Critic (com canal, destinatário, timing recomendado)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Score e tier do lead (Magnus)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Regras de gate L3 configuradas pelo cliente (ex: contas acima de R$X, segmentos estratégicos, mensagens com desconto)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Disponibilidade do calendário (Calendly/Cal.com API)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Log de envio verificável no ClickUp: { message_id, lead_id, channel, sent_at, status (sent/queued/blocked_for_hitl), tracking_url }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Atualização do CRM com activity de outreach"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para respostas positivas: link de booking enviado e slot reservado no calendário"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Notificação ao SDR humano para follow-up de alta prioridade"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Nexus imediatamente apos aprovacao do Critic. Re-trigger nos dias D+2, D+4, D+7 para follow-up automatico se nao houver resposta. Trigger especial se lead abrir email ou clicar em link (…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo."
    - "[ ] HITL: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial."
    - "[ ] HITL: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual."
    - "[ ] HITL: Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo."
    - "[ ] HITL: Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach."
---

# Agendar Mensagens

**Task ID:** `vox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Agendar Mensagens |
| **status** | `pending` |
| **responsible_executor** | Vox (Vox — Dispatchêr e Agendador) |
| **execution_type** | `Hybrid` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável pelo envio efetivo das mensagens aprovadas pelo Critic e pelo fluxo de agendamento. Conecta com as APIs dos canais (email via SMTP/SendGrid, LinkedIn via automação, WhatsApp Business API, Vapi para voz). Controla timing de envio (horários de melhor abertura por canal/segmento), sequência de follow-up automático e booking de reuniões quando o lead responde positivamente. Para leads HOT em contas estratégicas ou mensagens com desconto/promessa comercial: bloqueia e escala para HITL antes de enviar.

## Input

- Draft aprovado pelo Critic (com canal, destinatário, timing recomendado)
- Score e tier do lead (Magnus)
- Regras de gate L3 configuradas pelo cliente (ex: contas acima de R$X, segmentos estratégicos, mensagens com desconto)
- Disponibilidade do calendário (Calendly/Cal.com API)

## Output

- Log de envio verificável no ClickUp: { message_id, lead_id, channel, sent_at, status (sent/queued/blocked_for_hitl), tracking_url }
- Atualização do CRM com activity de outreach
- Para respostas positivas: link de booking enviado e slot reservado no calendário
- Notificação ao SDR humano para follow-up de alta prioridade

## Trigger

Ativado pelo Nexus imediatamente apos aprovacao do Critic. Re-trigger nos dias D+2, D+4, D+7 para follow-up automatico se nao houver resposta. Trigger especial se lead abrir email ou clicar em link (sinal de engajamento = prioridade imediata para proximo toque).

## Knowledge base (o que o executor consulta)

- Regras de timing por canal (email: Ter-Qui 9h-11h / 14h-16h
- WhatsApp: horário comercial + sem finais de semana para B2B
- LinkedIn: dias úteis manhã)
- Limites de volume diário por conta de envio (para evitar blacklist de email)
- Regras de gate L3 configuradas no onboarding
- Templates de mensagem de agendamento e confirmação
- Política de unsubscribe e opt-out LGPD

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft aprovado pelo Critic (com canal, destinatário, timing recomendado)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Log de envio verificável no ClickUp: { message_id, lead_id, channel, sent_at, status (sent/queued/blocked_for_hitl), tr…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Log de envio verificável no ClickUp: { message_id, lead_id, channel, sent_at, status (sent/queued/blocked_for_hitl), tracking_url }
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossi…
- [ ] Gate HITL respeitado: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do…
- [ ] Gate HITL respeitado: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação ant… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Unsubscribe ou resposta negativa agressiva: processado pelo Lumen, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Lumen
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
