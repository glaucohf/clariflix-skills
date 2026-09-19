---
task: bela()
responsavel: "Bela"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "ID do cliente extraído do ticket + integração com CRM (HubSpot/Salesforce), plataforma de CS (ChurnZero/Custify) e histórico de tickets"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Bloco de contexto padronizado (max 300 palavras) anexado ao ticket no ClickUp: resumo da conta (tier, ARR, data de início), últimos 3 tickets (status, resolução), eventos recentes (renovação, onboarding, incidente), health score atual, flag de VIP ou risco especial"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparada em paralelo com Dante (não bloqueia o roteamento, enriquece o ticket antes do agente humano abrir). Disparada apenas para P1/P2 ou clientes Enterprise por padrão (configurável)."
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

# Enriquecer Contexto Cliente

**Task ID:** `bela()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Triagem, Roteamento e Priorização de Tickets

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Contexto Cliente |
| **status** | `pending` |
| **responsible_executor** | Bela (Bela — Contextualista de Conta) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em enriquecimento de contexto: antes do roteamento final, busca no CRM e nas plataformas de CS dados relevantes sobre o cliente — últimas interações, tickets recentes, status de onboarding, uso do produto, faturas em aberto, NPS mais recente. Monta um 'briefing de conta' compacto que acompanha o ticket para o agente de destino, eliminando a necessidade de o agente buscar contexto manualmente.

## Input

- ID do cliente extraído do ticket + integração com CRM (HubSpot/Salesforce), plataforma de CS (ChurnZero/Custify) e histórico de tickets

## Output

- Bloco de contexto padronizado (max 300 palavras) anexado ao ticket no ClickUp: resumo da conta (tier, ARR, data de início), últimos 3 tickets (status, resolução), eventos recentes (renovação, onboarding, incidente), health score atual, flag de VIP ou risco especial

## Trigger

Disparada em paralelo com Dante (não bloqueia o roteamento, enriquece o ticket antes do agente humano abrir). Disparada apenas para P1/P2 ou clientes Enterprise por padrão (configurável).

## Knowledge base (o que o executor consulta)

- Acesso ao CRM (HubSpot/Salesforce), plataforma de CS (ChurnZero/Custify/Chargebee), histórico de tickets dos últimos 180 dias, catálogo de produtos e módulos contratados por conta

## Action Items

1. Confirmar o gatilho e carregar a entrada (ID do cliente extraído do ticket + integração com CRM (HubSpot/Salesforce), plataforma de CS (ChurnZero/Custify) e hist…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Bloco de contexto padronizado (max 300 palavras) anexado ao ticket no ClickUp: resumo da conta (tier, ARR, data de iníc…) e persistir no artefato do squad.
4. Entregar ao critic Auditor de Roteamento; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Bloco de contexto padronizado (max 300 palavras) anexado ao ticket no ClickUp: resumo da conta (tier, ARR, data de início), últimos 3 tickets (status, resoluçã…
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

- **to:** Rex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
