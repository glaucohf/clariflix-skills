---
task: lumen()
responsavel: "Lumen"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Respostas de email (via webhook do ESP), mensagens de WhatsApp incoming (via WhatsApp Business API), transcrições de calls (Vapi/Retell com Deepgram STT)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Histórico de outreach do lead (qual mensagem gerou a resposta)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Analise de resposta estruturada: { sentiment (positive/neutral/negative/objection), intent (interested/not_now/wrong_person/unsubscribe), objections_detected: [], suggested_reply_angle, coaching_note_for_sdr }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Atualizacao do CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Se interest = confirmed: trigger de agendamento para o Vox"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Se objection detectada: draft de resposta para objecao gerado pelo Penna e submetido ao Critic"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Relatorio semanal de top objecoes e win/loss patterns para o SDR humano"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook em tempo real para qualquer resposta incoming. Processamento em batch diário de transcrições de calls das 24h anteriores. Trigger semanal para relatório de patterns."
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

# Analisar Respostas Recebidas

**Task ID:** `lumen()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Respostas Recebidas |
| **status** | `pending` |
| **responsible_executor** | Lumen (Lumen — Analista de Conversação e Coaching) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analisa as respostas recebidas (email replies, mensagens de WhatsApp, transcrições de calls via Vapi) e extrai: sentimento, objeções levantadas, nível de interesse, próximo passo ideal. Alimenta o CRM com insights estruturados e sugere ao SDR humano como responder a cada objeção. Em calls gravadas, identifica momentos de hesitação e melhores práticas para coaching. Fecha o loop de aprendizado atualizando a biblioteca de mensagens vencedoras do Penna.

## Input

- Respostas de email (via webhook do ESP), mensagens de WhatsApp incoming (via WhatsApp Business API), transcrições de calls (Vapi/Retell com Deepgram STT)
- Histórico de outreach do lead (qual mensagem gerou a resposta)

## Output

- Analise de resposta estruturada: { sentiment (positive/neutral/negative/objection), intent (interested/not_now/wrong_person/unsubscribe), objections_detected: [], suggested_reply_angle, coaching_note_for_sdr }
- Atualizacao do CRM
- Se interest = confirmed: trigger de agendamento para o Vox
- Se objection detectada: draft de resposta para objecao gerado pelo Penna e submetido ao Critic
- Relatorio semanal de top objecoes e win/loss patterns para o SDR humano

## Trigger

Webhook em tempo real para qualquer resposta incoming. Processamento em batch diário de transcrições de calls das 24h anteriores. Trigger semanal para relatório de patterns.

## Knowledge base (o que o executor consulta)

- Mapeamento de objeções frequentes por segmento e script de resposta validado
- Frameworks de qualificação BANT e MEDDIC para classificar o nível de interesse
- Biblioteca de calls vencedoras (transcrições anonimizadas)
- Criterios de handoff para o closer humano (quais sinais indicam que o lead está pronto para a conversa de venda)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Respostas de email (via webhook do ESP), mensagens de WhatsApp incoming (via WhatsApp Business API), transcrições de ca…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Analise de resposta estruturada: { sentiment (positive/neutral/negative/objection), intent (interested/not_now/wrong_pe…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Analise de resposta estruturada: { sentiment (positive/neutral/negative/objection), intent (interested/not_now/wrong_person/unsubscribe), objections_detected:…
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

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
