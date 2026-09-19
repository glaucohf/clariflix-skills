---
task: postMortemWriter()
responsavel: "Post-Mortem Writer"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Todos os artefatos do incidente (Incident Cluster Report, Root Cause Analysis, Fix Plan, Execution Log, communication timeline), historico de post-mortems anteriores para deteccao de padroes, templates de post-mortem da empresa, lista de action items abertos de incidentes anteriores relacionados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Post-Mortem draft completo em Markdown com: (1) Resumo executivo (impacto, duracao, servicos)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Timeline detalhada com evidencias"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Root Cause Analysis (5 Whys completo)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Contributing Factors"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(5) O que funcionou bem"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(6) O que pode melhorar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Incidente marcado como 'resolved' pelo Orchestrator; tambem pode ser chamado em modo 'interim report' para incidentes de duracao > 4h para fornecer update parcial"
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

# Analisar Incidentes

**Task ID:** `postMortemWriter()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Incidentes |
| **status** | `pending` |
| **responsible_executor** | Post-Mortem Writer (Post-Mortem Writer — 'Chrono') |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 10 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Ao resolucao do incidente, consome todos os artefatos gerados durante o ciclo (Incident Cluster, Root Cause Analysis, Fix Plan, Execution Log, communication timeline) e produz automaticamente um post-mortem completo no padrao da industria (5 Whys, Timeline, Contributing Factors, Action Items). Identifica padroes recorrentes comparando com post-mortems anteriores. Sugere melhorias de runbook baseadas no que funcionou/nao funcionou. Cria os action items no ClickUp com assignees sugeridos e due dates. O post-mortem e gerado como rascunho para revisao humana (L3 para publicacao final).

## Input

- Todos os artefatos do incidente (Incident Cluster Report, Root Cause Analysis, Fix Plan, Execution Log, communication timeline), historico de post-mortems anteriores para deteccao de padroes, templates de post-mortem da empresa, lista de action items abertos de incidentes anteriores relacionados

## Output

- Post-Mortem draft completo em Markdown com: (1) Resumo executivo (impacto, duracao, servicos)
- (2) Timeline detalhada com evidencias
- (3) Root Cause Analysis (5 Whys completo)
- (4) Contributing Factors
- (5) O que funcionou bem
- (6) O que pode melhorar
- (7) Action Items com owner sugerido, prioridade e due date
- (8) Runbook updates recomendados
- (9) Deteccao de padroes (se este incidente se repete)
- Task ClickUp criada automaticamente com o draft para revisao

## Trigger

Incidente marcado como 'resolved' pelo Orchestrator; tambem pode ser chamado em modo 'interim report' para incidentes de duracao > 4h para fornecer update parcial

## Knowledge base (o que o executor consulta)

- Historico completo de post-mortems dos ultimos 24 meses
- base de action items e seu status de resolucao
- templates de post-mortem (formato blameless, Five Whys, SRE Google style)
- catalogo de runbooks para identificar onde atualizar
- metricas de MTTR historico para benchmarking no relatorio

## Action Items

1. Confirmar o gatilho e carregar a entrada (Todos os artefatos do incidente (Incident Cluster Report, Root Cause Analysis, Fix Plan, Execution Log, communication t…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Post-Mortem draft completo em Markdown com: (1) Resumo executivo (impacto, duracao, servicos)) e persistir no artefato do squad.
4. Entregar ao critic Fix Guardian; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Post-Mortem draft completo em Markdown com: (1) Resumo executivo (impacto, duracao, servicos)
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

- **to:** Fix Guardian
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
