---
task: orquestradorComercialPipeline()
responsavel: "Orquestrador Comercial"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Card de Roteamento Verificado: artefato JSON gerado por decisao de roteamento, contendo {lead_id, timestamp_entrada, timestamp_roteamento, dossie_enriquecido, score_oracle_breakdown, vendedor_designado, justificativa_roteamento, veredicto_critic, sla_aplicado, status_aceite, timestamp_primeiro_contato}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato e registrado no CRM como atividade, linkado no ClickUp como task concluida com prova de trabalho, e indexado no Langfuse para observabilidade e quality gates"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard em tempo real mostra todos os roteamentos do dia com status de SLA"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe cada novo lead ou sinal de reativação, decompose em subtarefas paralelas (enriquecimento + scoring + lookup de disponibilidade), agrega os resultados dos workers, aplica as regras de roteament…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Veredito 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro deploy; em produção, amostras aleatórias (10%) passam por revisão humana"
    - "[ ] L3: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratamento especial"
    - "[ ] L3: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente"
    - "[ ] L3: Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interface de configuração, com log de auditoria"
    - "[ ] L3: Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor designado"
---

# Orquestrar Pipeline do Roteamento Inteligente de Leads

**Task ID:** `orquestradorComercialPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Roteamento Inteligente de Leads

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Roteamento Inteligente de Leads |
| **status** | `pending` |
| **responsible_executor** | Orquestrador Comercial (Maestro (Orquestrador Comercial)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe cada novo lead ou sinal de reativação, decompose em subtarefas paralelas (enriquecimento + scoring + lookup de disponibilidade), agrega os resultados dos workers, aplica as regras de roteamento do Playbook, toma a decisão de atribuição e aciona o Worker de Notificação. Mantém o estado do lead no funil, monitora SLAs de resposta e dispara re-roteamento se SLA vencer. É o único agente que escreve diretamente no CRM a atribuição final.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Card de Roteamento Verificado: artefato JSON gerado por decisao de roteamento, contendo {lead_id, timestamp_entrada, timestamp_roteamento, dossie_enriquecido, score_oracle_breakdown, vendedor_designado, justificativa_roteamento, veredicto_critic, sla_aplicado, status_aceite, timestamp_primeiro_contato}
- Artefato e registrado no CRM como atividade, linkado no ClickUp como task concluida com prova de trabalho, e indexado no Langfuse para observabilidade e quality gates
- Dashboard em tempo real mostra todos os roteamentos do dia com status de SLA

## Trigger

Recebe cada novo lead ou sinal de reativação, decompose em subtarefas paralelas (enriquecimento + scoring + lookup de disponibilidade), agrega os resultados dos workers, aplica as regras de roteamento do Playbook, toma a decisão de atribuição e aciona o Worker de Notificação. Mantém o estado do lead no funil, monitora SLAs de resposta e dispara re-roteamento se SLA vencer. É o único agente que escreve diretamente no CRM a atribuição final.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP HubSpot disponível) ou Pipedrive/Salesforce via API
- leitura e escrita de leads, contatos, deals, atividades
- WhatsApp Business API: Gupshup ou AiSensy (crítico Brasil)
- notificação de vendedores e mensagem de apresentação ao lead
- Calendário: Google Calendar e/ou Microsoft Outlook via MCP
- consulta de disponibilidade em tempo real para Atlas
- Enriquecimento: Clay (principal) + Apollo.io (275M+ contatos)
- enriquecimento automático pelo Argos
- Comunicação interna: Slack
- alertas do Farol e notificações do Hermes para vendedores
- Gestão de tarefas/prova de trabalho: ClickUp
- cada roteamento gera task com artefato verificável (card de lead + decisão documentada)
- Observabilidade: Langfuse (OTEL)
- rastreamento de todas as decisões de roteamento, latência por agente, quality gates
- Ads/Sinais de intenção: Meta Ads + Google Ads (UTM params)
- contexto de origem do lead para scoring de intenção do Oracle
- Orquestração: LangGraph (controle fino de estado do funil) + Claude Agent SDK (Maestro como Ópus lead, workers como Sonnet)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Veredito 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Card de Roteamento Verificado: artefato JSON gerado por decisao de roteamento, contendo {lead_id, timestamp_entrada, timestamp_roteamento, dossie_enriquecido,…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Veredito 2 registrado
- [ ] Gate L3 respeitado: Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização an…
- [ ] Gate L3 respeitado: Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurtu…
- [ ] Gate L3 respeitado: Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Hermes notificando o lead com mensagem de apresentação personalizada: humano (gestor) aprova o template e as variáveis de personalização antes do primeiro depl… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Re-roteamento após 3 rejeições consecutivas do mesmo lead por diferentes vendedores: gestor decide se lead é desqualificado, entra em nurture ou recebe tratame… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Veredito retorna status REVISÃO_HUMANA: gestor comercial recebe o pacote completo e toma a decisão de roteamento manualmente | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Alterações nas regras do Playbook de Roteamento (pesos de score, limites de capacidade, territórios): somente gestor comercial pode alterar regras via interfac… | BLOQUEIA até decisão humana |
| VETO-005 | L3 — Leads com score acima de 90 (tier HOT estratégico) em contas de alto valor: notificação ao gerente de vendas para acompanhamento proativo além do vendedor desi… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão humana semanal do relatório de auditoria do Veredito para identificar vieses sistemáticos e calibrar o modelo de scoring | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Veredito 2 | BLOQUEIA entrega |

## Handoff

- **to:** Worker de Enriquecimento
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
