---
task: rex()
responsavel: "Rex"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ticket novo + índice de tickets abertos nas últimas 24h (embedding de similaridade) + threshold de surto configurado (ex: 3+ tickets similares em 30min)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Flag de deduplicação: UNIQUE (segue fluxo normal) | DUPLICATE (vincula ao pai, fecha o novo) | SURGE (agrega em incidente, roteia para fila de incidentes)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Em caso de SURGE, cria ticket-mestre com lista de afetados e notifica canal Slack de incidentes"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Triador-Mor após classificação da Lara, antes do Enzo executar o roteamento final. Execução paralela com Dante."
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

# Detectar E Agrupar Duplicatas

**Task ID:** `rex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Triagem, Roteamento e Priorização de Tickets

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar E Agrupar Duplicatas |
| **status** | `pending` |
| **responsible_executor** | Rex (Rex — Detector de Duplicatas e Agrupamento) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Antes de criar um novo ticket na fila, verifica se já existe um ticket aberto para o mesmo problema/cliente e se há um surto de tickets similares (ex: 5 clientes reportando o mesmo bug em 10 minutos = incident, não tickets individuais). Em caso de duplicata, vincula ao ticket-pai e notifica. Em caso de surto, cria um ticket de incidente agregado e roteia para fila de incidentes, evitando que a equipe processe N tickets do mesmo problema.

## Input

- Ticket novo + índice de tickets abertos nas últimas 24h (embedding de similaridade) + threshold de surto configurado (ex: 3+ tickets similares em 30min)

## Output

- Flag de deduplicação: UNIQUE (segue fluxo normal) | DUPLICATE (vincula ao pai, fecha o novo) | SURGE (agrega em incidente, roteia para fila de incidentes)
- Em caso de SURGE, cria ticket-mestre com lista de afetados e notifica canal Slack de incidentes

## Trigger

Disparado pelo Triador-Mor após classificação da Lara, antes do Enzo executar o roteamento final. Execução paralela com Dante.

## Knowledge base (o que o executor consulta)

- Índice vetorial de tickets abertos (últimas 24-48h), embeddings de intenções similares, threshold de surto por categoria (configurável), mapeamento de problemas conhecidos e incidentes ativos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ticket novo + índice de tickets abertos nas últimas 24h (embedding de similaridade) + threshold de surto configurado (e…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Flag de deduplicação: UNIQUE (segue fluxo normal) | DUPLICATE (vincula ao pai, fecha o novo) | SURGE (agrega em inciden…) e persistir no artefato do squad.
4. Entregar ao critic Auditor de Roteamento; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Flag de deduplicação: UNIQUE (segue fluxo normal) | DUPLICATE (vincula ao pai, fecha o novo) | SURGE (agrega em incidente, roteia para fila de incidentes)
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

- **to:** FAQ/L0
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
