---
task: scout()
responsavel: "Scout"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de contas-alvo (ICP), palavras-chave de sinais, perfis de decisores monitorados, feed do Sales Navigator, alertas do Apollo/Clay, webhooks de mencoes"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Signal Events JSON com: lead_id, tipo_sinal, urgência_score (1-10), contexto_sinal (texto do post ou evento), janela_timing_estimada (horas), dados_enriquecidos_lead, flag_HITL se conta tier-1"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron a cada 30 minutos para verificação de feed LinkedIn; webhook imediato para alertas de mudança de cargo via Apollo; evento de engajamento em post próprio da empresa."
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

# Monitorar Sinais De Intencao

**Task ID:** `scout()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais De Intencao |
| **status** | `pending` |
| **responsible_executor** | Scout (Sentinela de Sinais (Scout)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitor contínuo de sinais de intenção no LinkedIn e fontes externas. Detecta eventos de timing: mudança de cargo, post de decisor sobre dor relevante, engajamento em conteúdo da empresa, menção a concorrente, anúncio de funding, contratação de cargos indicativos de expansão. Prioriza sinais por score de urgência e relevância de ICP.

## Input

- Lista de contas-alvo (ICP), palavras-chave de sinais, perfis de decisores monitorados, feed do Sales Navigator, alertas do Apollo/Clay, webhooks de mencoes

## Output

- Signal Events JSON com: lead_id, tipo_sinal, urgência_score (1-10), contexto_sinal (texto do post ou evento), janela_timing_estimada (horas), dados_enriquecidos_lead, flag_HITL se conta tier-1

## Trigger

Cron a cada 30 minutos para verificação de feed LinkedIn; webhook imediato para alertas de mudança de cargo via Apollo; evento de engajamento em post próprio da empresa.

## Knowledge base (o que o executor consulta)

- ICP Canvas do cliente, lista de contas-alvo tier-1/tier-2/tier-3, taxonomia de sinais com scores de valor, histórico de sinais que geraram reunião (para calibrar scoring), perfis de decisores monitorados, glossário de dores do segmento-alvo

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de contas-alvo (ICP), palavras-chave de sinais, perfis de decisores monitorados, feed do Sales Navigator, alertas…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Signal Events JSON com: lead_id, tipo_sinal, urgência_score (1-10), contexto_sinal (texto do post ou evento), janela_ti…) e persistir no artefato do squad.
4. Entregar ao critic Argus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Signal Events JSON com: lead_id, tipo_sinal, urgência_score (1-10), contexto_sinal (texto do post ou evento), janela_timing_estimada (horas), dados_enriquecido…
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

- **to:** Sherlock
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
