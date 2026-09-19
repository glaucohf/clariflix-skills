---
task: fixProposer()
responsavel: "Fix Proposer"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Root Cause Analysis Report do Sherlock, catalogo de runbooks disponíveis, risk matrix de acoes configurada no onboarding, estado atual da infraestrutura (replicas, versoes de deploy, configs), restricoes de janela de manutencao"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Fix Plan estruturado com: (1) Lista de acoes em sequencia com prioridade"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Para cada acao: comando exato / API call / steps, nivel de autonomia (L2 auto-execute / L3 requires approval), justificativa, reversibilidade e rollback procedure"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Criterios de sucesso verificaveis (metricas a observar, thresholds esperados)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Estimated Time to Recovery (ETR) estimado"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(5) Acoes de mitigacao temporaria vs fix definitivo claramente separadas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orchestrator apos Sherlock entregar o Root Cause Analysis com pelo menos uma hipotese de probabilidade > 60%; tambem chamado em modo 'mitigation-only' quando root cause ainda nao esta cl…"
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

# Gerar Propostas De Fix

**Task ID:** `fixProposer()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Propostas De Fix |
| **status** | `pending` |
| **responsible_executor** | Fix Proposer (Fix Proposer — 'MacGyver') |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o Root Cause Analysis do Sherlock e gera propostas de fix concretas e executaveis. Para cada hipotese de root cause, mapeia o runbook correspondente (ou cria um novo se nao existe). Classifica cada acao proposta por: (a) reversibilidade (reversivel/irreversivel), (b) impacto potencial (baixo/medio/alto), (c) complexidade de execucao. Determina o nivel de autonomia adequado para cada acao: L2 para acoes reversiveis de baixo risco (scale up, restart de pod, flush de cache, toggle de feature flag), L3 para acoes de risco medio/alto (rollback de deploy, mudanca de configuracao critica, failover de banco de dados). Gera o Fix Plan com sequencia de acoes, comandos exatos e criterios de sucesso verificaveis.

## Input

- Root Cause Analysis Report do Sherlock, catalogo de runbooks disponíveis, risk matrix de acoes configurada no onboarding, estado atual da infraestrutura (replicas, versoes de deploy, configs), restricoes de janela de manutencao

## Output

- Fix Plan estruturado com: (1) Lista de acoes em sequencia com prioridade
- (2) Para cada acao: comando exato / API call / steps, nivel de autonomia (L2 auto-execute / L3 requires approval), justificativa, reversibilidade e rollback procedure
- (3) Criterios de sucesso verificaveis (metricas a observar, thresholds esperados)
- (4) Estimated Time to Recovery (ETR) estimado
- (5) Acoes de mitigacao temporaria vs fix definitivo claramente separadas

## Trigger

Chamado pelo Orchestrator apos Sherlock entregar o Root Cause Analysis com pelo menos uma hipotese de probabilidade > 60%; tambem chamado em modo 'mitigation-only' quando root cause ainda nao esta claro mas servico precisa ser estabilizado

## Knowledge base (o que o executor consulta)

- Catalogo de runbooks por tipo de incidente e componente
- historico de fixes que funcionaram vs que falharam
- catalogo de comandos kubectl / terraform / aws-cli / db queries aprovados
- risk matrix de acoes por ambiente (staging vs producao)
- constraints de SLA e janelas de manutencao
- documentacao de feature flags disponíveis
- playbooks de rollback por servico

## Action Items

1. Confirmar o gatilho e carregar a entrada (Root Cause Analysis Report do Sherlock, catalogo de runbooks disponíveis, risk matrix de acoes configurada no onboardin…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Fix Plan estruturado com: (1) Lista de acoes em sequencia com prioridade) e persistir no artefato do squad.
4. Entregar ao critic Fix Guardian; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Fix Plan estruturado com: (1) Lista de acoes em sequencia com prioridade
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

- **to:** Fix Executor
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
