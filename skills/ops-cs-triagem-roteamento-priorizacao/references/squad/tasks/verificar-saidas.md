---
task: auditorDeRoteamentoVerificar()
responsavel: "Auditor de Roteamento"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Confiança de classificação < 0.75 (Lara sinalizou ambiguidade): humano revisa intenção antes do roteamento prosseguir"
    - "[ ] HITL: Ticket P1 criado: notificação imediata para supervisor via Slack com justificativa do score, supervisor confirma ou rebaixa prioridade em até 5min"
    - "[ ] HITL: Intenção de churn/cancelamento detectada (intent_l1=churn): roteamento bloqueado automaticamente até CS Manager aprovar estratégia de resposta (L3 por risco de perda de receita)"
    - "[ ] HITL: Rex detecta surto (SURGE): incident manager humano é notificado e confirma se é incidente real antes de agrupar tickets — evita falso positivo que agruparia tickets distintos"
    - "[ ] HITL: Nina tentou auto-resolução mas confidence < 0.90: agente humano recebe ticket com contexto da tentativa e decide a resposta final"
---

# Verificar Saídas do Triagem, Roteamento e Priorização de Tickets

**Task ID:** `auditorDeRoteamentoVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Triagem, Roteamento e Priorização de Tickets

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Triagem, Roteamento e Priorização de Tickets |
| **status** | `pending` |
| **responsible_executor** | Auditor de Roteamento (Auditor de Roteamento — Sócrates) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Auditor de Roteamento — Sócrates — Critic/Verifier que atua em duas camadas: (1) Verificação pré-despacho: após Lara e Dante gerarem outputs e antes de Enzo executar o roteamento, Sócrates revisa a consistência — a intenção bate com os dados do ticket? O score de prioridade faz sentido dado o tier do cliente? A fila de destino é a correta para essa combinação? (2) Auditoria pós-ciclo: diariamente, amostra 10% dos tickets roteados automaticamente, compara destino atribuído vs. destino real (se houve reassignment posterior), calcula drift de qualidade e alerta se acurácia cair abaixo de 85%. Sócrates questiona, não executa — seus outputs são flags e justificativas, nunca ações diretas.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Auditor de Roteamento
- Critic/Verifier que atua em duas camadas: (1) Verificação pré-despacho: após Lara e Dante gerarem outputs e antes de Enzo executar o roteamento, Sócrates revisa a consistência
- a intenção bate com os dados do ticket? O score de prioridade faz sentido dado o tier do cliente? A fila de destino é a correta para essa combinação? (2) Auditoria pós-ciclo: diariamente, amostra 10% dos tickets roteados automaticamente, compara destino atribuído vs
- destino real (se houve reassignment posterior), calcula drift de qualidade e alerta se acurácia cair abaixo de 85%
- Sócrates questiona, não executa
- seus outputs são flags e justificativas, nunca ações diretas

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Triador-Mor para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Triador-Mor
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
