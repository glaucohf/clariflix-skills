---
task: icPipeline()
responsavel: "IC"
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
    descricao: "Incident Response Package"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "artefato completo por incidente, entregue automaticamente no ClickUp e Slack: (1) Incident Cluster Report com correlacao de alertas e noise score"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Root Cause Analysis com event timeline e evidencias"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Fix Plan executado com execution log e evidencias"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(4) Post-Mortem blameless draft completo com action items criados no ClickUp"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(5) Metricas do incidente (MTTA, MTTR, blast radius, servicos afetados)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Persona: 'Orion' — o Incident Commander que nunca entra em panico. Recebe o primeiro sinal de incidente (webhook PagerDuty, alerta Datadog, trigger Sentry ou chamada manual), declara a severidade ini…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Fix Guardian antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Toda acao irreversivel ou de alto risco requer aprovacao explicita do SRE on-call antes de execucao pelo Forge: rollback de deploy em producao, failover de banco de dados primario, mudanca de configuracao de infraestrutura critica, escalonamento de recursos com impacto financeiro significativo, qualquer acao em banco de dados (DELETE, DROP, ALTER em producao)"
    - "[ ] L3: Publicacao do post-mortem final: o Chrono gera o draft, mas um humano revisa e aprova antes de publicar para o time ou para clientes"
    - "[ ] L3: Comunicacao externa para clientes afetados: o Herald gera o rascunho, o CS Manager aprova antes do envio"
    - "[ ] HITL: HITL emergencial — Se o Aegis retornar veredicto BLOCKED_ESCALATE em qualquer momento, o incidente entra em modo manual ate que um SRE sênior retome o controle via canal Slack do war room"
    - "[ ] HITL: HITL emergencial — Se o Forge encontrar falha em acao L2 ou resultado inesperado apos execucao, pausa automaticamente e notifica o SRE on-call antes de prosseguir"
---

# Orquestrar Pipeline do AI SRE

**Task ID:** `icPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do AI SRE |
| **status** | `pending` |
| **responsible_executor** | IC (Incident Commander (IC)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Persona: 'Orion' — o Incident Commander que nunca entra em panico. Recebe o primeiro sinal de incidente (webhook PagerDuty, alerta Datadog, trigger Sentry ou chamada manual), declara a severidade inicial (P1/P2/P3), abre o war room no Slack, instancia os workers especializados em paralelo, agrega as investigacoes, toma a decisao de escalonamento HITL vs autonomia e orquestra a comunicacao durante todo o ciclo de vida do incidente. Mantem o estado global do incidente em memória e no ClickUp.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Incident Response Package
- artefato completo por incidente, entregue automaticamente no ClickUp e Slack: (1) Incident Cluster Report com correlacao de alertas e noise score
- (2) Root Cause Analysis com event timeline e evidencias
- (3) Fix Plan executado com execution log e evidencias
- (4) Post-Mortem blameless draft completo com action items criados no ClickUp
- (5) Metricas do incidente (MTTA, MTTR, blast radius, servicos afetados)
- O conjunto destes artefatos e a 'prova de trabalho' verificavel que o squad gera
- o cliente pode auditar cada incidente e ver exatamente o que o squad fez, em quanto tempo e qual foi o impacto

## Trigger

Persona: 'Orion' — o Incident Commander que nunca entra em panico. Recebe o primeiro sinal de incidente (webhook PagerDuty, alerta Datadog, trigger Sentry ou chamada manual), declara a severidade inicial (P1/P2/P3), abre o war room no Slack, instancia os workers especializados em paralelo, agrega as investigacoes, toma a decisao de escalonamento HITL vs autonomia e orquestra a comunicacao durante todo o ciclo de vida do incidente. Mantem o estado global do incidente em memória e no ClickUp.

## Knowledge base (o que o executor consulta)

- PagerDuty
- recepcao de alertas via webhook, criacao e atualizacao de incidents, escalonamento on-call
- consulta de metricas, alertas, traces, service map e dashboards via API/MCP
- CloudWatch
- logs e metricas de infra AWS
- erros de aplicacao, releases e performance issues
- dashboards de metricas e alertas (Prometheus/Loki)
- GitHub Actions / ArgoCD
- historico de deploys para correlacao com root cause
- Elastic / Splunk / Loki
- consulta de logs durante investigacao
- Jaeger / Tempo
- traces distribuidos para analise de latencia e falhas
- hub de prova de trabalho: cada incidente = task com timeline, artefatos e action items
- war room automatico, notificacoes de stakeholders, canal de HITL
- Supabase / Postgres
- estado dos incidentes, historico de correlacoes, base de runbooks e post-mortems
- observabilidade OTEL do squad, tracing de chamadas de agentes, quality gates e evals de acuracia de root cause
- Terraform / AWS SSM / HashiCorp Vault
- acesso seguro a credenciais para execucao de acoes L2
- ServiceNow
- opcional: sincronizacao de incidents para empresas com ITSM legado
- Statuspage.io
- atualizacao de status page publica durante incidentes que afetam clientes

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Fix Guardian antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Incident Response Package
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Fix Guardian registrado
- [ ] Gate L3 respeitado: Toda acao irreversivel ou de alto risco requer aprovacao explicita do SRE on-call antes de execucao pelo Forge: rollback de deploy em produ…
- [ ] Gate L3 respeitado: Publicacao do post-mortem final: o Chrono gera o draft, mas um humano revisa e aprova antes de publicar para o time ou para clientes
- [ ] Gate L3 respeitado: Comunicacao externa para clientes afetados: o Herald gera o rascunho, o CS Manager aprova antes do envio

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Toda acao irreversivel ou de alto risco requer aprovacao explicita do SRE on-call antes de execucao pelo Forge: rollback de deploy em producao, failover de ban… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Publicacao do post-mortem final: o Chrono gera o draft, mas um humano revisa e aprova antes de publicar para o time ou para clientes | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Comunicacao externa para clientes afetados: o Herald gera o rascunho, o CS Manager aprova antes do envio | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL emergencial — Se o Aegis retornar veredicto BLOCKED_ESCALATE em qualquer momento, o incidente entra em modo manual ate que um SRE sênior retome o controle… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL emergencial — Se o Forge encontrar falha em acao L2 ou resultado inesperado apos execucao, pausa automaticamente e notifica o SRE on-call antes de prosseg… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — L2 confirmado — Declaracao de severidade P1 pelo Orchestrator notifica imediatamente o SRE on-call e o Engineering Lead via PagerDuty/Slack, mesmo sendo L2 (ex… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — HITL de degradacao — Se MTTR ultrapassar 2x o ETR estimado sem resolucao, o Orchestrator automaticamente escala para modo assistido e solicita intervencao huma… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Fix Guardian | BLOQUEIA entrega |

## Handoff

- **to:** Alert Correlator
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
