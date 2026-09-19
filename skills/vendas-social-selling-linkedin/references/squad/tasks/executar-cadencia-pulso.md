---
task: pulso()
responsavel: "Pulso"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem aprovada pelo Argus, sequência de cadência definida no playbook, limites de envio configurados, status de resposta do lead"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Execution Log por lead: timestamp_cada_toque, canal_utilizado, status_entrega, resposta_recebida (sim/não), tipo_resposta (positiva/negativa/neutra), próxima_acao_recomendada, atualização_CRM_confirmada, alert_HITL se resposta recebida em conta tier-1"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Mensagem aprovada pelo Argus; cron diário para verificar follow-ups pendentes na fila; webhook de resposta LinkedIn/email; evento de resposta detectado pelo monitor de inbox."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório."
    - "[ ] HITL: Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada."
    - "[ ] HITL: Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente."
    - "[ ] HITL: Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana."
    - "[ ] HITL: Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração."
---

# Executar Cadencia Pulso

**Task ID:** `pulso()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Executar Cadencia Pulso |
| **status** | `pending` |
| **responsible_executor** | Pulso (Executor de Cadência (Pulso)) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia a execução da cadência multicanal após aprovação do Argus. Controla timing de envios (respeitando limites do LinkedIn para não gerar restrição de conta), sequência de toques (D0: connection request, D2: DM, D5: follow-up, D10: nurture de conteúdo), registra cada interação no CRM, detecta resposta do lead e notifica Orquestrador para reclassificação. Para contas tier-1: enfileira para HITL antes de cada toque.

## Input

- Mensagem aprovada pelo Argus, sequência de cadência definida no playbook, limites de envio configurados, status de resposta do lead

## Output

- Execution Log por lead: timestamp_cada_toque, canal_utilizado, status_entrega, resposta_recebida (sim/não), tipo_resposta (positiva/negativa/neutra), próxima_acao_recomendada, atualização_CRM_confirmada, alert_HITL se resposta recebida em conta tier-1

## Trigger

Mensagem aprovada pelo Argus; cron diário para verificar follow-ups pendentes na fila; webhook de resposta LinkedIn/email; evento de resposta detectado pelo monitor de inbox.

## Knowledge base (o que o executor consulta)

- Playbook de cadência por tipo de sinal e tier de conta (sequência de toques, intervalos, canais), limites de segurança do LinkedIn (max conexões/dia, max DMs/dia), CRM com status atualizado de cada lead, histórico de respostas para detectar padrões de melhor timing

## Action Items

1. Confirmar o gatilho e carregar a entrada (Mensagem aprovada pelo Argus, sequência de cadência definida no playbook, limites de envio configurados, status de resp…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Execution Log por lead: timestamp_cada_toque, canal_utilizado, status_entrega, resposta_recebida (sim/não), tipo_respos…) e persistir no artefato do squad.
4. Entregar ao critic Argus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Execution Log por lead: timestamp_cada_toque, canal_utilizado, status_entrega, resposta_recebida (sim/não), tipo_resposta (positiva/negativa/neutra), próxima_a…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus 2 registrado
- [ ] Gate HITL respeitado: Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório.
- [ ] Gate HITL respeitado: Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada.
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório. | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana. | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Primeiro envio de cadência para um novo segmento/persona não testado anteriormente: SDR revisa amostra de 5 mensagens antes de liberar automação plena. | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Lead responde mencionando nome de concorrente ou fazendo pergunta técnica complexa: desvia para SDR humano com contexto completo da conversa. | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Argus 2 | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
