---
task: pulseAnalyst()
responsavel: "Pulse Analyst"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Respostas de email via webhook do ESP (SendGrid/Instantly)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Mensagens de WhatsApp incoming via WhatsApp Business API"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Transcrições de calls geradas pelo Vapi com Deepgram STT"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Histórico de outreach do lead (qual mensagem gerou a resposta"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "contexto crítico para análise)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Score e dossiê do lead para contexto"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Análise de resposta estruturada por lead: { sentiment (positive / neutral / negative / objection / not_now / wrong_person / unsubscribe), intent_score (0-100), objections_detected: [lista com categoria e texto exato], next_best_action (schedule_meeting / send_followup / escalate_to_human / close_sequence), coaching_note: 'texto para o SDR', reply_suggested: true/false }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Se reply_suggested = true: draft de resposta para objeção gerado pelo Cyrano e submetido ao Sentinel antes de chegar ao SDR"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Atualização automática do CRM com activity e intent score"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Se intent = confirmed_interest: trigger de notificação IMEDIATA ao SDR humano para assumir a conversa"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Relatório semanal para o Maestro e SDR humano: top 5 objeções do período, taxa de resposta por canal e variação A/B, mensagens vencedoras identificadas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook em tempo real para qualquer mensagem incoming (email, WhatsApp, LinkedIn). Processamento em batch a cada 4 horas para transcrições de calls. Trigger semanal automático para relatório de patte…"
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

# Analisar Respostas Recebidas

**Task ID:** `pulseAnalyst()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Respostas Recebidas |
| **status** | `pending` |
| **responsible_executor** | Pulse Analyst (Pulse Analyst — O Intérprete de Respostas) |
| **execution_type** | `Worker` |
| **input** | 6 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analisa em tempo real todas as respostas recebidas (email replies, mensagens de WhatsApp, transcrições de calls de voz) e extrai sinais estruturados: sentimento, intenção, objeções levantadas e próximo passo ideal. Alimenta o CRM com insights para o SDR humano agir com contexto total. Sugere o script de resposta ideal para cada objeção detectada. Em calls gravadas via Vapi, identifica momentos de hesitação, melhores ângulos e padrões de objeções para coaching do SDR. Fecha o loop de aprendizado: toda mensagem vencedora (reply rate real) retroalimenta a biblioteca do Cyrano; todo pattern de objeção retroalimenta o ICP Cartografo.

## Input

- Respostas de email via webhook do ESP (SendGrid/Instantly)
- Mensagens de WhatsApp incoming via WhatsApp Business API
- Transcrições de calls geradas pelo Vapi com Deepgram STT
- Histórico de outreach do lead (qual mensagem gerou a resposta
- contexto crítico para análise)
- Score e dossiê do lead para contexto

## Output

- Análise de resposta estruturada por lead: { sentiment (positive / neutral / negative / objection / not_now / wrong_person / unsubscribe), intent_score (0-100), objections_detected: [lista com categoria e texto exato], next_best_action (schedule_meeting / send_followup / escalate_to_human / close_sequence), coaching_note: 'texto para o SDR', reply_suggested: true/false }
- Se reply_suggested = true: draft de resposta para objeção gerado pelo Cyrano e submetido ao Sentinel antes de chegar ao SDR
- Atualização automática do CRM com activity e intent score
- Se intent = confirmed_interest: trigger de notificação IMEDIATA ao SDR humano para assumir a conversa
- Relatório semanal para o Maestro e SDR humano: top 5 objeções do período, taxa de resposta por canal e variação A/B, mensagens vencedoras identificadas

## Trigger

Webhook em tempo real para qualquer mensagem incoming (email, WhatsApp, LinkedIn). Processamento em batch a cada 4 horas para transcrições de calls. Trigger semanal automático para relatório de patterns e retroalimentação do ICP Cartografo e biblioteca do Cyrano. Trigger imediato se sentimento = VERY_POSITIVE ou intenção = CONFIRMED_INTEREST (notificação urgente ao SDR).

## Knowledge base (o que o executor consulta)

- Mapeamento de objecoes frequentes por segmento e scripts de resposta validados (nao e o momento / ja tenho solucao / preco / preciso de aprovacao / etc)
- Frameworks de qualificacao BANT e MEDDIC para classificar nivel de interesse
- Criterios de handoff para o closer humano: quais sinais indicam que o lead esta pronto para negociacao
- Biblioteca de transcricoes de calls vencedoras anonimizadas para fine-tuning do modelo de analise
- Matriz de sentiment x intent x next_action para decisao automatica de proximo passo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Respostas de email via webhook do ESP (SendGrid/Instantly)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Análise de resposta estruturada por lead: { sentiment (positive / neutral / negative / objection / not_now / wrong_pers…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Análise de resposta estruturada por lead: { sentiment (positive / neutral / negative / objection / not_now / wrong_person / unsubscribe), intent_score (0-100),…
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

- **to:** Sentinel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
