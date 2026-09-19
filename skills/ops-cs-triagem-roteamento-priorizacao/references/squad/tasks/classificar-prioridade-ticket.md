---
task: dante()
responsavel: "Dante"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Output da Lara (intent + entities) + perfil do cliente do CRM (tier, ARR, health score, data de renovação, tickets abertos) + regras de SLA configuradas pelo cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON com campos: priority_tier (P1/P2/P3/P4), sla_deadline (timestamp), priority_score (0-100), priority_rationale (texto de 1-2 frases explicando o score), churn_risk_flag (boolean)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Triador-Mor após output da Lara. Também re-executado se cliente atualiza o ticket com informação nova de impacto."
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

# Classificar Prioridade Ticket

**Task ID:** `dante()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Triagem, Roteamento e Priorização de Tickets

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Prioridade Ticket |
| **status** | `pending` |
| **responsible_executor** | Dante (Dante — Árbitro de Prioridade) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Calcula o score de prioridade do ticket combinando 4 dimensões: (1) Urgência declarada pelo cliente (tom, palavras-chave como 'urgente', 'paralisado'), (2) Tier do cliente (Enterprise/Mid/SMB buscado no CRM), (3) Impacto operacional estimado (bug que afeta N usuários > dúvida individual), (4) Risco de churn (cliente com health score baixo ou em período de renovação). Output: tier de prioridade P1-P4 com prazo de SLA associado.

## Input

- Output da Lara (intent + entities) + perfil do cliente do CRM (tier, ARR, health score, data de renovação, tickets abertos) + regras de SLA configuradas pelo cliente

## Output

- JSON com campos: priority_tier (P1/P2/P3/P4), sla_deadline (timestamp), priority_score (0-100), priority_rationale (texto de 1-2 frases explicando o score), churn_risk_flag (boolean)

## Trigger

Disparado pelo Triador-Mor após output da Lara. Também re-executado se cliente atualiza o ticket com informação nova de impacto.

## Knowledge base (o que o executor consulta)

- Matriz de SLA do cliente (tier × tipo de intenção), health scores do CRM/ChurnZero, regras de negócio especiais (clientes VIP, contratos enterprise com SLA customizado), histórico de tickets P1 anteriores para calibrar score

## Action Items

1. Confirmar o gatilho e carregar a entrada (Output da Lara (intent + entities) + perfil do cliente do CRM (tier, ARR, health score, data de renovação, tickets aber…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON com campos: priority_tier (P1/P2/P3/P4), sla_deadline (timestamp), priority_score (0-100), priority_rationale (tex…) e persistir no artefato do squad.
4. Entregar ao critic Auditor de Roteamento; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON com campos: priority_tier (P1/P2/P3/P4), sla_deadline (timestamp), priority_score (0-100), priority_rationale (texto de 1-2 frases explicando o score), ch…
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

- **to:** Enzo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
