---
task: alertCorrelator()
responsavel: "Alert Correlator"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stream de alertas raw de multiplas ferramentas de monitoramento (JSON normalizado via MCP/webhook), service dependency graph carregado do CMDB ou mapa de infra, historico de co-ocorrencias dos ultimos 90 dias"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Incident Cluster Report: alertas agrupados por root cause hipotetico, Alert Noise Score (ex: '47 alertas -> 3 clusters'), ranking de prioridade dos clusters, lista de servicos afetados e servicos downstream suprimidos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de novo alerta recebido no pipeline de ingestion; chamada direta pelo Orchestrator ao declarar incidente; modo batch a cada 2 min durante incidente ativo para re-avaliar correlacoes com novos…"
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

# Correlacionar Alertas

**Task ID:** `alertCorrelator()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Correlacionar Alertas |
| **status** | `pending` |
| **responsible_executor** | Alert Correlator (Alert Correlator — 'Nexus') |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Consome o flood de alertas das multiplas fontes (Datadog, PagerDuty, CloudWatch, Grafana, Sentry, custom webhooks) dentro de uma janela de tempo configuravel (padrao: 5 min). Aplica algoritmos de correlacao baseados em: timestamp proximity, shared labels/tags (servico, regiao, pod, host), topologia de dependencia de servicos e padroes historicos de co-ocorrencia de alertas. Agrupa alertas em 'incident clusters' e calcula um Alert Noise Score (quantos alertas sao sintomas do mesmo root cause). Elimina duplicatas e suprime alertas de servicos downstream sabidamente impactados pelo upstream ja identificado.

## Input

- Stream de alertas raw de multiplas ferramentas de monitoramento (JSON normalizado via MCP/webhook), service dependency graph carregado do CMDB ou mapa de infra, historico de co-ocorrencias dos ultimos 90 dias

## Output

- Incident Cluster Report: alertas agrupados por root cause hipotetico, Alert Noise Score (ex: '47 alertas -> 3 clusters'), ranking de prioridade dos clusters, lista de servicos afetados e servicos downstream suprimidos

## Trigger

Webhook de novo alerta recebido no pipeline de ingestion; chamada direta pelo Orchestrator ao declarar incidente; modo batch a cada 2 min durante incidente ativo para re-avaliar correlacoes com novos alertas chegando

## Knowledge base (o que o executor consulta)

- Service dependency graph (CMDB / Datadog Service Map / mapa manual)
- historico de incidentes dos ultimos 90 dias com suas correlacoes reais
- topologia de infraestrutura (regions, AZs, clusters K8s, microservicos)
- regras de supressao configuradas pelo time
- thresholds de severidade por servico

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stream de alertas raw de multiplas ferramentas de monitoramento (JSON normalizado via MCP/webhook), service dependency…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Incident Cluster Report: alertas agrupados por root cause hipotetico, Alert Noise Score (ex: '47 alertas -> 3 clusters'…) e persistir no artefato do squad.
4. Entregar ao critic Fix Guardian; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Incident Cluster Report: alertas agrupados por root cause hipotetico, Alert Noise Score (ex: '47 alertas -> 3 clusters'), ranking de prioridade dos clusters, l…
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

- **to:** Root Cause Investigator
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
