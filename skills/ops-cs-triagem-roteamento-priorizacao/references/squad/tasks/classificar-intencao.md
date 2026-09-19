---
task: lara()
responsavel: "Lara"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ticket bruto (texto livre, transcrição de áudio, campos de formulário) + histórico dos últimos 3 tickets do mesmo cliente (contexto)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON com campos: intent_l1, intent_l2, entities{produto, modulo, erro, data}, confidence_score (0-1), ambiguity_flag (boolean)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Se confidence < 0.75, sinaliza para HITL"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparada pelo Triador-Mor para todo ticket novo recebido. Re-disparada se Auditor de Roteamento retornar flag de inconsistência."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Auditor de Roteamento antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Confiança de classificação < 0.75 (Lara sinalizou ambiguidade): humano revisa intenção antes do roteamento prosseguir"
    - "[ ] HITL: Ticket P1 criado: notificação imediata para supervisor via Slack com justificativa do score, supervisor confirma ou rebaixa prioridade em até 5min"
    - "[ ] HITL: Intenção de churn/cancelamento detectada (intent_l1=churn): roteamento bloqueado automaticamente até CS Manager aprovar estratégia de resposta (L3 por risco de perda de receita)"
    - "[ ] HITL: Rex detecta surto (SURGE): incident manager humano é notificado e confirma se é incidente real antes de agrupar tickets — evita falso positivo que agruparia tickets distintos"
    - "[ ] HITL: Nina tentou auto-resolução mas confidence < 0.90: agente humano recebe ticket com contexto da tentativa e decide a resposta final"
---

# Classificar Intenção

**Task ID:** `lara()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Triagem, Roteamento e Priorização de Tickets

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Intenção |
| **status** | `pending` |
| **responsible_executor** | Lara (Lara — Classificadora de Intenção) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Lê o conteúdo bruto do ticket (texto, áudio transcrito, formulário) e classifica a intenção em dois níveis: L1 (macro: Suporte Técnico, Financeiro/Billing, Onboarding, Churn/Cancelamento, Feedback, Entrega/Status, Outro) e L2 (micro: ex. Suporte Técnico → Bug Crítico / Dúvida de Uso / Solicitação de Feature). Extrai entidades-chave: produto mencionado, módulo, mensagem de erro, data de referência.

## Input

- Ticket bruto (texto livre, transcrição de áudio, campos de formulário) + histórico dos últimos 3 tickets do mesmo cliente (contexto)

## Output

- JSON com campos: intent_l1, intent_l2, entities{produto, modulo, erro, data}, confidence_score (0-1), ambiguity_flag (boolean)
- Se confidence < 0.75, sinaliza para HITL

## Trigger

Disparada pelo Triador-Mor para todo ticket novo recebido. Re-disparada se Auditor de Roteamento retornar flag de inconsistência.

## Knowledge base (o que o executor consulta)

- Taxonomia de intenções do cliente (documento vivo no ClickUp), glossário de produtos/módulos, histórico de tickets classificados corretamente (few-shot examples), padrões de linguagem do canal (WhatsApp usa informal, formulários são mais estruturados)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ticket bruto (texto livre, transcrição de áudio, campos de formulário) + histórico dos últimos 3 tickets do mesmo clien…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON com campos: intent_l1, intent_l2, entities{produto, modulo, erro, data}, confidence_score (0-1), ambiguity_flag (b…) e persistir no artefato do squad.
4. Entregar ao critic Auditor de Roteamento; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON com campos: intent_l1, intent_l2, entities{produto, modulo, erro, data}, confidence_score (0-1), ambiguity_flag (boolean)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Auditor de Roteamento registrado
- [ ] Gate HITL respeitado: Confiança de classificação < 0.75 (Lara sinalizou ambiguidade): humano revisa intenção antes do roteamento prosseguir
- [ ] Gate HITL respeitado: Ticket P1 criado: notificação imediata para supervisor via Slack com justificativa do score, supervisor confirma ou rebaixa prioridade em a…
- [ ] Gate HITL respeitado: Intenção de churn/cancelamento detectada (intent_l1=churn): roteamento bloqueado automaticamente até CS Manager aprovar estratégia de respo…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Confiança de classificação < 0.75 (Lara sinalizou ambiguidade): humano revisa intenção antes do roteamento prosseguir | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Ticket P1 criado: notificação imediata para supervisor via Slack com justificativa do score, supervisor confirma ou rebaixa prioridade em até 5min | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Intenção de churn/cancelamento detectada (intent_l1=churn): roteamento bloqueado automaticamente até CS Manager aprovar estratégia de resposta (L3 por risco de… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Rex detecta surto (SURGE): incident manager humano é notificado e confirma se é incidente real antes de agrupar tickets — evita falso positivo que agruparia ti… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Nina tentou auto-resolução mas confidence < 0.90: agente humano recebe ticket com contexto da tentativa e decide a resposta final | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Novo tipo de intenção detectado (não mapeado na taxonomia): Triador-Mor para o fluxo e aciona ops lead para expandir a taxonomia antes de processar o lote | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Auditoria do Sócrates aponta drift de acurácia < 85%: revisão semanal obrigatória com ops lead para recalibrar pesos da matriz de roteamento | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Auditor de Roteamento | BLOQUEIA entrega |

## Handoff

- **to:** Dante
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
