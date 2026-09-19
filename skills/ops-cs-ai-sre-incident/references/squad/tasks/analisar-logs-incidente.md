---
task: rootCauseInvestigator()
responsavel: "Root Cause Investigator"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Incident Cluster Report do Nexus, acesso a logs via MCP (Elastic/CloudWatch/Splunk), metricas (Datadog/Prometheus via API), traces distribuidos (Jaeger/Tempo), historico de deploys (GitHub API / ArgoCD API), historico de mudancas de infra (Terraform / K8s audit logs), lista de runbooks relevantes"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Root Cause Analysis Report com: (1) Event Timeline ordenado com evidencias"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Top 3 hipoteses de root cause com score de probabilidade e evidencias citadas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Servicos e componentes impactados com blast radius estimado"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Anomalias detectadas em metricas/logs com timestamps"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(5) Contexto de mudancas recentes relevantes"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orchestrator apos Nexus entregar o Incident Cluster; pode ser re-chamado com novos dados durante incidente ativo se hipoteses iniciais nao confirmarem"
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

# Analisar Logs Incidente

**Task ID:** `rootCauseInvestigator()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Logs Incidente |
| **status** | `pending` |
| **responsible_executor** | Root Cause Investigator (Root Cause Investigator — 'Sherlock') |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Dado o Incident Cluster gerado pelo Nexus, executa investigacao profunda de root cause. Consulta logs (CloudWatch, Splunk, Elastic, Loki) para o periodo do incidente e janela pre-incidente (configuravel, padrao 30 min antes). Correlaciona com eventos recentes: deploys (GitHub Actions / ArgoCD), mudancas de configuracao (Terraform state, Kubernetes ConfigMaps), escalas de infra, migracao de banco de dados, picos de trafego. Constroi um Event Timeline ordenado. Aplica tecnicas de analise: anomaly detection em metricas, diff de configuracao pre/pos incidente, analise de traces distribuidos (Jaeger/Tempo). Produz hipoteses de root cause rankeadas por probabilidade com evidencias.

## Input

- Incident Cluster Report do Nexus, acesso a logs via MCP (Elastic/CloudWatch/Splunk), metricas (Datadog/Prometheus via API), traces distribuidos (Jaeger/Tempo), historico de deploys (GitHub API / ArgoCD API), historico de mudancas de infra (Terraform / K8s audit logs), lista de runbooks relevantes

## Output

- Root Cause Analysis Report com: (1) Event Timeline ordenado com evidencias
- (2) Top 3 hipoteses de root cause com score de probabilidade e evidencias citadas
- (3) Servicos e componentes impactados com blast radius estimado
- (4) Anomalias detectadas em metricas/logs com timestamps
- (5) Contexto de mudancas recentes relevantes

## Trigger

Chamado pelo Orchestrator apos Nexus entregar o Incident Cluster; pode ser re-chamado com novos dados durante incidente ativo se hipoteses iniciais nao confirmarem

## Knowledge base (o que o executor consulta)

- Runbooks de incidentes anteriores (base de conhecimento interna)
- padroes de falha conhecidos por servico/componente
- historico de root causes dos ultimos 12 meses
- documentacao de arquitetura dos servicos
- thresholds de anomalia por metrica e servico
- playbooks de diagnostico por tipo de incidente (memoria, CPU, latencia, erro 5xx, timeout de DB)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Incident Cluster Report do Nexus, acesso a logs via MCP (Elastic/CloudWatch/Splunk), metricas (Datadog/Prometheus via A…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Root Cause Analysis Report com: (1) Event Timeline ordenado com evidencias) e persistir no artefato do squad.
4. Entregar ao critic Fix Guardian; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Root Cause Analysis Report com: (1) Event Timeline ordenado com evidencias
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

- **to:** Fix Proposer
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
