---
task: cassandraPipeline()
responsavel: "Cassandra"
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
    descricao: "Painel de Pipeline Intelligence (atualizado a cada 4h) com: (1) lista priorizada de deals em risco com score, categoria e ação recomendada"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) forecast de 30/60/90 dias em três cenários com gap para meta"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) alertas contextualizados por deal entregues no canal preferido do closer"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) relatório mensal de aprendizado com accuracy do forecast e ROI das intervenções"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato verificável: JSON de estado do pipeline com timestamp, acessível via ClickUp e exportável para CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orchestrator central do squad. Recebe sinais do CRM (mudancas de estagio, atividade, engajamento), decompoe em subtarefas de analise, roteia para workers especializados, consolida scores e coordena e…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Nemesis antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora da empresa"
    - "[ ] L3: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM"
    - "[ ] L2: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa"
    - "[ ] L2: Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle"
    - "[ ] L1: Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal"
---

# Orquestrar Pipeline do Forecast de Pipeline e Risco de Deal

**Task ID:** `cassandraPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Forecast de Pipeline e Risco de Deal |
| **status** | `pending` |
| **responsible_executor** | Cassandra (Cassandra — Oráculo Comercial) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orchestrator central do squad. Recebe sinais do CRM (mudancas de estagio, atividade, engajamento), decompoe em subtarefas de analise, roteia para workers especializados, consolida scores e coordena emissao de alertas. Mantem estado completo do pipeline e historico de intervencoes. Nao envia alertas diretamente — valida via Critic antes de qualquer notificacao externa.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Painel de Pipeline Intelligence (atualizado a cada 4h) com: (1) lista priorizada de deals em risco com score, categoria e ação recomendada
- (2) forecast de 30/60/90 dias em três cenários com gap para meta
- (3) alertas contextualizados por deal entregues no canal preferido do closer
- (4) relatório mensal de aprendizado com accuracy do forecast e ROI das intervenções
- Artefato verificável: JSON de estado do pipeline com timestamp, acessível via ClickUp e exportável para CRM

## Trigger

Orchestrator central do squad. Recebe sinais do CRM (mudancas de estagio, atividade, engajamento), decompoe em subtarefas de analise, roteia para workers especializados, consolida scores e coordena emissao de alertas. Mantem estado completo do pipeline e historico de intervencoes. Nao envia alertas diretamente — valida via Critic antes de qualquer notificacao externa.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível), Pipedrive, Salesforce
- fonte primária de dados de deals, atividades e estágios
- gestão de tarefas de intervenção, registro de próximo passo, prova de trabalho por deal
- canal principal de alertas para closers e gestores (webhook)
- WhatsApp Business API (Gupshup / AiSensy)
- alertas urgentes para closers via WhatsApp
- Email (SMTP/SendGrid)
- digest semanal para gestores e report para board
- Langfuse (OTEL)
- observabilidade do squad, quality gates (70% dev / 85% staging / 95% prod), rastreio de accuracy do forecast
- Google Calendar / Outlook Calendar
- verificação de disponibilidade para sugestões de próximo passo do Cronos
- Clay / Apollo
- enriquecimento de dados do contato quando necessário para contexto do alerta
- Notion / Google Sheets
- export do relatório de forecast para clientes sem dashboard dedicado

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Nemesis antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Painel de Pipeline Intelligence (atualizado a cada 4h) com: (1) lista priorizada de deals em risco com score, categoria e ação recomendada
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Nemesis registrado
- [ ] Gate L3 respeitado: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem…
- [ ] Gate L3 respeitado: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM
- [ ] Gate L2 respeitado: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora d… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM | BLOQUEIA até decisão humana |
| VETO-003 | L2 — Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Nemesis | BLOQUEIA entrega |

## Handoff

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
