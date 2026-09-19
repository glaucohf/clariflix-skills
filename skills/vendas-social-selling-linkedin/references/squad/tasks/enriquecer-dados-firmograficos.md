---
task: sherlock()
responsavel: "Sherlock"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Signal Event do Sentinela com lead_id e tipo_sinal"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "acesso a CRM para histórico de interações"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead Dossiê JSON: perfil_linkedin_completo, histórico_cargo (3 últimas posições), empresa (tamanho, setor, stack, notícias_recentes), conexões_em_comum, conteúdo_recente_publicado (3 últimos posts), interações_crm_anteriores, talking_points_recomendados (3-5 baseados no sinal), pain_signals_detectados"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Signal Event recebido do Orquestrador com score >= 5; solicitação manual de enriquecimento de SDR via ClickUp."
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

# Enriquecer Dados Firmográficos

**Task ID:** `sherlock()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Social Selling e Inbound LinkedIn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dados Firmográficos |
| **status** | `pending` |
| **responsible_executor** | Sherlock (Detetive de Conta (Sherlock)) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Enriquecimento profundo de conta e lead no momento do sinal. Monta dossiê contextual: histórico de cargo, stack tecnológica da empresa, notícias recentes, conexões em comum, conteúdo publicado pelo lead, interações anteriores no CRM. Objetivo: entregar ao Worker de Outreach o contexto necessário para uma mensagem cirúrgica.

## Input

- Signal Event do Sentinela com lead_id e tipo_sinal
- acesso a CRM para histórico de interações

## Output

- Lead Dossiê JSON: perfil_linkedin_completo, histórico_cargo (3 últimas posições), empresa (tamanho, setor, stack, notícias_recentes), conexões_em_comum, conteúdo_recente_publicado (3 últimos posts), interações_crm_anteriores, talking_points_recomendados (3-5 baseados no sinal), pain_signals_detectados

## Trigger

Signal Event recebido do Orquestrador com score >= 5; solicitação manual de enriquecimento de SDR via ClickUp.

## Knowledge base (o que o executor consulta)

- Credenciais Apollo/Clay para enriquecimento, acesso read ao CRM, base de dados de stack tecnológica por setor (Clearbit/BuiltWith), templates de talking points por tipo de sinal e segmento, histórico de dossiês anteriores para evitar re-pesquisa

## Action Items

1. Confirmar o gatilho e carregar a entrada (Signal Event do Sentinela com lead_id e tipo_sinal).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead Dossiê JSON: perfil_linkedin_completo, histórico_cargo (3 últimas posições), empresa (tamanho, setor, stack, notíc…) e persistir no artefato do squad.
4. Entregar ao critic Argus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead Dossiê JSON: perfil_linkedin_completo, histórico_cargo (3 últimas posições), empresa (tamanho, setor, stack, notícias_recentes), conexões_em_comum, conteú…
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

- **to:** Cypher
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
