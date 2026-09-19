---
task: nexus()
responsavel: "Nexus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Execution Log do Pulso, Lead Classification do Radar, Signal Events do Scout, Lead Dossies do Sherlock"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "CRM Update Confirmation: contatos_atualizados, deals_criados, tarefas_criadas_no_clickup, métricas_diárias (sinais_detectados, mensagens_enviadas, respostas_recebidas, HOTs_gerados, reuniões_agendadas), alert_de_anomalia (queda brusca de sinais, taxa de resposta abaixo do threshold), relatório_semanal_squad"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento de conclusão de qualquer worker (batch a cada 15 min); cron diário para relatório consolidado; trigger semanal para relatório executivo."
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

# Sincronizar Dados Crm

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sincronizar Dados Crm |
| **status** | `pending` |
| **responsible_executor** | Nexus (Guardião do Pipeline (Nexus)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de higiene e sincronização de CRM. Garante que cada lead abordado, cada sinal detectado, cada mensagem enviada e cada resposta recebida seja registrado no CRM com dados completos. Faz dedup de contatos, atualiza cargos desatualizados, cria deals quando lead classifica como HOT, e gera o dashboard de métricas do squad no ClickUp. E a prova de trabalho verificável do squad.

## Input

- Execution Log do Pulso, Lead Classification do Radar, Signal Events do Scout, Lead Dossies do Sherlock

## Output

- CRM Update Confirmation: contatos_atualizados, deals_criados, tarefas_criadas_no_clickup, métricas_diárias (sinais_detectados, mensagens_enviadas, respostas_recebidas, HOTs_gerados, reuniões_agendadas), alert_de_anomalia (queda brusca de sinais, taxa de resposta abaixo do threshold), relatório_semanal_squad

## Trigger

Evento de conclusão de qualquer worker (batch a cada 15 min); cron diário para relatório consolidado; trigger semanal para relatório executivo.

## Knowledge base (o que o executor consulta)

- Schema do CRM do cliente (campos obrigatórios, owners, estágios do funil), regras de dedup por email/LinkedIn URL, mapeamento de estágios CRM para status de cadência do squad, thresholds de anomalia (baseline de métricas da semana 1), template de relatório executivo semanal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Execution Log do Pulso, Lead Classification do Radar, Signal Events do Scout, Lead Dossies do Sherlock).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (CRM Update Confirmation: contatos_atualizados, deals_criados, tarefas_criadas_no_clickup, métricas_diárias (sinais_dete…) e persistir no artefato do squad.
4. Entregar ao critic Argus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: CRM Update Confirmation: contatos_atualizados, deals_criados, tarefas_criadas_no_clickup, métricas_diárias (sinais_detectados, mensagens_enviadas, respostas_re…
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

- **to:** Argus 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
