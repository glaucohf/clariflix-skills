---
task: enzo()
responsavel: "Enzo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Output da Lara + output do Dante + estado atual das filas (carga, disponibilidade dos agentes, tickets em aberto por fila) + matriz de roteamento configurada"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ticket atualizado no ClickUp com: tags aplicadas (intent_l1, intent_l2, priority_tier, canal, produto, cliente_tier), assignee/fila de destino definidos, sla_deadline setado, campo 'routing_justification' preenchido com texto legível"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Notificação Slack para supervisor se P1"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Triador-Mor após outputs de Lara e Dante consolidados. Re-disparado pelo Triador-Mor se Auditor retornar veredito REROUTE."
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

# Selecionar Fila Destino

**Task ID:** `enzo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Triagem, Roteamento e Priorização de Tickets

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Selecionar Fila Destino |
| **status** | `pending` |
| **responsible_executor** | Enzo (Enzo — Despachante de Fila) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Com base na intenção (Lara) e prioridade (Dante), executa o roteamento: seleciona a fila/agente de destino correto aplicando a matriz de roteamento configurada. Verifica disponibilidade e carga atual das filas antes de despachar — se fila sobrecarregada, aciona lógica de overflow (fila alternativa ou notificação de supervisor). Aplica todas as tags no ClickUp via API e registra justificativa de roteamento no campo interno do ticket.

## Input

- Output da Lara + output do Dante + estado atual das filas (carga, disponibilidade dos agentes, tickets em aberto por fila) + matriz de roteamento configurada

## Output

- Ticket atualizado no ClickUp com: tags aplicadas (intent_l1, intent_l2, priority_tier, canal, produto, cliente_tier), assignee/fila de destino definidos, sla_deadline setado, campo 'routing_justification' preenchido com texto legível
- Notificação Slack para supervisor se P1

## Trigger

Disparado pelo Triador-Mor após outputs de Lara e Dante consolidados. Re-disparado pelo Triador-Mor se Auditor retornar veredito REROUTE.

## Knowledge base (o que o executor consulta)

- Matriz de roteamento viva (intenção × prioridade × tier → fila/agente), perfis e especialidades de cada agente humano, regras de overflow e escalonamento, histórico de roteamentos corretos e incorretos por categoria

## Action Items

1. Confirmar o gatilho e carregar a entrada (Output da Lara + output do Dante + estado atual das filas (carga, disponibilidade dos agentes, tickets em aberto por fi…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ticket atualizado no ClickUp com: tags aplicadas (intent_l1, intent_l2, priority_tier, canal, produto, cliente_tier), a…) e persistir no artefato do squad.
4. Entregar ao critic Auditor de Roteamento; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ticket atualizado no ClickUp com: tags aplicadas (intent_l1, intent_l2, priority_tier, canal, produto, cliente_tier), assignee/fila de destino definidos, sla_d…
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

- **to:** Bela
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
