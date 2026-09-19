---
task: radar()
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Resposta do lead (texto da DM LinkedIn ou email), contexto do lead (dossiê, histórico de cadência), histórico de respostas similares classificadas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead Classification: classificação (HOT/WARM/COLD/UNSUBSCRIBE), confidence_score (0-100), resumo_intenção (2-3 linhas), ação_recomendada, rascunho_resposta_sugerida (para HOT/WARM), urgência (IMEDIATO/HOJE/SEMANA), trigger_agendamento (se HOT), atualização_score_crm"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de nova resposta no inbox LinkedIn ou email; revisão manual solicitada pelo SDR via ClickUp."
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

# Classificar Intencao

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Intencao |
| **status** | `pending` |
| **responsible_executor** | Radar (Qualificador de Resposta (Radar)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analisa respostas recebidas de leads e classifica intenção: HOT (quer reunião, pede proposta), WARM (interesse mas sem urgência, nurture), COLD (sem interesse agora, reativar em 60-90 dias), UNSUBSCRIBE (remover imediatamente). Para HOTs: aciona agendamento e notifica SDR/closer em tempo real. Para WARMs: define próxima ação de nurture. Opera 24/7 sem demora de resposta.

## Input

- Resposta do lead (texto da DM LinkedIn ou email), contexto do lead (dossiê, histórico de cadência), histórico de respostas similares classificadas

## Output

- Lead Classification: classificação (HOT/WARM/COLD/UNSUBSCRIBE), confidence_score (0-100), resumo_intenção (2-3 linhas), ação_recomendada, rascunho_resposta_sugerida (para HOT/WARM), urgência (IMEDIATO/HOJE/SEMANA), trigger_agendamento (se HOT), atualização_score_crm

## Trigger

Webhook de nova resposta no inbox LinkedIn ou email; revisão manual solicitada pelo SDR via ClickUp.

## Knowledge base (o que o executor consulta)

- Exemplos de respostas classificadas por intenção (base de treinamento), contexto do lead e histórico de interações, critérios de qualificação BANT/MEDDIC simplificados para LinkedIn, scripts de resposta para cada classificação, SLA de resposta por tier de conta (tier-1: 5 min, tier-2: 30 min, tier-3: 2h)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Resposta do lead (texto da DM LinkedIn ou email), contexto do lead (dossiê, histórico de cadência), histórico de respos…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead Classification: classificação (HOT/WARM/COLD/UNSUBSCRIBE), confidence_score (0-100), resumo_intenção (2-3 linhas),…) e persistir no artefato do squad.
4. Entregar ao critic Argus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead Classification: classificação (HOT/WARM/COLD/UNSUBSCRIBE), confidence_score (0-100), resumo_intenção (2-3 linhas), ação_recomendada, rascunho_resposta_sug…
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
