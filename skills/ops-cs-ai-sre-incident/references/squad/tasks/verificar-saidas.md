---
task: fixGuardianVerificar()
responsavel: "Fix Guardian"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] L3: Toda acao irreversivel ou de alto risco requer aprovacao explicita do SRE on-call antes de execucao pelo Forge: rollback de deploy em producao, failover de banco de dados primario, mudanca de configuracao de infraestrutura critica, escalonamento de recursos com impacto financeiro significativo, qualquer acao em banco de dados (DELETE, DROP, ALTER em producao)"
    - "[ ] L3: Publicacao do post-mortem final: o Chrono gera o draft, mas um humano revisa e aprova antes de publicar para o time ou para clientes"
    - "[ ] L3: Comunicacao externa para clientes afetados: o Herald gera o rascunho, o CS Manager aprova antes do envio"
    - "[ ] HITL: HITL emergencial — Se o Aegis retornar veredicto BLOCKED_ESCALATE em qualquer momento, o incidente entra em modo manual ate que um SRE sênior retome o controle via canal Slack do war room"
    - "[ ] HITL: HITL emergencial — Se o Forge encontrar falha em acao L2 ou resultado inesperado apos execucao, pausa automaticamente e notifica o SRE on-call antes de prosseguir"
---

# Verificar Saídas do AI SRE

**Task ID:** `fixGuardianVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do AI SRE |
| **status** | `pending` |
| **responsible_executor** | Fix Guardian (Fix Guardian — 'Aegis') |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Fix Guardian — 'Aegis' — Critic/Verifier que intercepta o Fix Plan gerado pelo MacGyver ANTES de qualquer execucao. Executa 7 verificacoes criticas: (1) Cada acao proposta esta no catalogo de runbooks aprovados? (2) O nivel de autonomia (L2/L3) esta correto para a reversibilidade real da acao? (3) Ha risco de piorar o incidente (ex: restart em cascata, thundering herd)? (4) As acoes respeitam janelas de manutencao e freezes de deploy? (5) Os criterios de sucesso sao verificaveis e realistas? (6) Ha dependencia entre acoes que possa criar um estado inconsistente se a sequencia for interrompida? (7) O blast radius de cada acao esta dentro dos limites de tolerancia configurados? Veredictos: APPROVED (executa), NEEDS_REVISION (devolve ao MacGyver com feedback especifico), BLOCKED_ESCALATE (para tudo, HITL obrigatorio). Tambem monitora pos-execucao: se metricas nao melhoram no ETR estimado, dispara re-avaliacao.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Fix Guardian
- Critic/Verifier que intercepta o Fix Plan gerado pelo MacGyver ANTES de qualquer execucao
- Executa 7 verificacoes criticas: (1) Cada acao proposta esta no catalogo de runbooks aprovados? (2) O nivel de autonomia (L2/L3) esta correto para a reversibilidade real da acao? (3) Ha risco de piorar o incidente (ex: restart em cascata, thundering herd)? (4) As acoes respeitam janelas de manutencao e freezes de deploy? (5) Os criterios de sucesso sao verificaveis e realistas? (6) Ha dependencia entre acoes que possa criar um estado inconsistente se a sequencia for interrompida? (7) O blast radius de cada acao esta dentro dos limites de tolerancia configurados? Veredictos: APPROVED (executa), NEEDS_REVISION (devolve ao MacGyver com feedback especifico), BLOCKED_ESCALATE (para tudo, HITL obrigatorio)
- Tambem monitora pos-execucao: se metricas nao melhoram no ETR estimado, dispara re-avaliacao

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador IC para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** IC
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
