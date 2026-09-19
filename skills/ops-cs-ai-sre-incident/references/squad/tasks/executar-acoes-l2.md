---
task: fixExecutor()
responsavel: "Fix Executor"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Fix Plan aprovado pelo Critic com acoes L2 sinalizadas, credenciais de acesso via secrets manager (nunca em texto), contexto do ambiente (prod/staging, regiao, cluster), estado atual dos servicos-alvo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Execution Log em tempo real com: (1) Acao executada com timestamp"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) Comando exato executado"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) Output/response capturado"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) Status (success/failure/partial)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(5) Metricas observadas antes e depois"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(6) Status de resolucao por acao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orchestrator somente apos Critic aprovar o Fix Plan; ativado apenas para acoes marcadas como L2 no plano; triggers tambem inclui 'mitigation mode' para acoes de estabilizacao enquanto ro…"
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

# Executar Ações L2

**Task ID:** `fixExecutor()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Executar Ações L2 |
| **status** | `pending` |
| **responsible_executor** | Fix Executor (Fix Executor — 'Forge') |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 7 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa as acoes classificadas como L2 (autonomia direta, sem aprovacao humana) do Fix Plan aprovado pelo Critic. Opera com acesso restrito: apenas acoes pre-aprovadas no catalogo de runbooks, em ambientes e servicos explicitamente autorizados no onboarding. Executa cada acao, captura o output exato (stdout/stderr, exit codes, API responses), monitora as metricas de sucesso por ate 5 min apos cada acao, e reporta o resultado ao Orchestrator em tempo real. Se uma acao L2 falhar ou gerar resultado inesperado, pausa imediatamente e escala para HITL antes de continuar. Nunca executa acoes irreversiveis sem aprovacao explicita, mesmo que classificadas erroneamente como L2.

## Input

- Fix Plan aprovado pelo Critic com acoes L2 sinalizadas, credenciais de acesso via secrets manager (nunca em texto), contexto do ambiente (prod/staging, regiao, cluster), estado atual dos servicos-alvo

## Output

- Execution Log em tempo real com: (1) Acao executada com timestamp
- (2) Comando exato executado
- (3) Output/response capturado
- (4) Status (success/failure/partial)
- (5) Metricas observadas antes e depois
- (6) Status de resolucao por acao
- (7) Evidencia de execucao para o post-mortem

## Trigger

Chamado pelo Orchestrator somente apos Critic aprovar o Fix Plan; ativado apenas para acoes marcadas como L2 no plano; triggers tambem inclui 'mitigation mode' para acoes de estabilizacao enquanto root cause ainda e investigado

## Knowledge base (o que o executor consulta)

- Catalogo de acoes L2 aprovadas por ambiente e servico
- secrets references (nao os secrets em si) via Vault/AWS SSM
- limites de rate de execucao para evitar loop de restart
- historico de execucoes anteriores para detectar loops
- criterios de abort (se metrica piorar X% apos acao, abortar e escalar)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Fix Plan aprovado pelo Critic com acoes L2 sinalizadas, credenciais de acesso via secrets manager (nunca em texto), con…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Execution Log em tempo real com: (1) Acao executada com timestamp) e persistir no artefato do squad.
4. Entregar ao critic Fix Guardian; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Execution Log em tempo real com: (1) Acao executada com timestamp
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

- **to:** Incident Communicator
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
