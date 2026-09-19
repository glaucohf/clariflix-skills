---
task: faqL0()
responsavel: "FAQ/L0"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ticket classificado como FAQ/L0 pela Lara + base de conhecimento (artigos, FAQs, runbooks) + histórico de respostas aprovadas para intenção similar"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta ao cliente (se auto-resolução confirmada, confidence >= 0.90) OU sumário de tentativa de resolução (para o agente humano, se confidence < 0.90)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Ticket atualizado com campo 'auto_resolution_attempted' e confidence score"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparada pelo Triador-Mor apenas para tickets classificados como intent_l1=FAQ ou status_query com confidence >= 0.85 na classificação da Lara. NUNCA disparada para P1 ou intenções de churn/cancelam…"
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

# Autoresponder Consultas

**Task ID:** `faqL0()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Triagem, Roteamento e Priorização de Tickets

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Autoresponder Consultas |
| **status** | `pending` |
| **responsible_executor** | FAQ/L0 (Nina — Respondente de Auto-Resolução (FAQ/L0)) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Para tickets de intenção de baixa complexidade (FAQ, status de pedido, reset de senha, links de documentação), Nina tenta resolver automaticamente consultando a base de conhecimento antes de criar trabalho humano. Se conseguir resolver com confiança >= 0.90, responde ao cliente diretamente e fecha o ticket como 'auto-resolvido'. Se não, passa o contexto de tentativa para o agente humano (evitando que o agente repita a pesquisa).

## Input

- Ticket classificado como FAQ/L0 pela Lara + base de conhecimento (artigos, FAQs, runbooks) + histórico de respostas aprovadas para intenção similar

## Output

- Resposta ao cliente (se auto-resolução confirmada, confidence >= 0.90) OU sumário de tentativa de resolução (para o agente humano, se confidence < 0.90)
- Ticket atualizado com campo 'auto_resolution_attempted' e confidence score

## Trigger

Disparada pelo Triador-Mor apenas para tickets classificados como intent_l1=FAQ ou status_query com confidence >= 0.85 na classificação da Lara. NUNCA disparada para P1 ou intenções de churn/cancelamento.

## Knowledge base (o que o executor consulta)

- Base de conhecimento do produto (artigos de ajuda, FAQs, runbooks), histórico de respostas aprovadas por agentes humanos (few-shot de alta qualidade), políticas de atendimento (o que pode ser auto-respondido e o que não pode), status operacional do produto (para responder queries de status)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ticket classificado como FAQ/L0 pela Lara + base de conhecimento (artigos, FAQs, runbooks) + histórico de respostas apr…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resposta ao cliente (se auto-resolução confirmada, confidence >= 0.90) OU sumário de tentativa de resolução (para o age…) e persistir no artefato do squad.
4. Entregar ao critic Auditor de Roteamento; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta ao cliente (se auto-resolução confirmada, confidence >= 0.90) OU sumário de tentativa de resolução (para o agente humano, se confidence < 0.90)
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

- **to:** Auditor de Roteamento
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
