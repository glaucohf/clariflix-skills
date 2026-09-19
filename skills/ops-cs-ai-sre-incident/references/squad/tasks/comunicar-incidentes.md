---
task: incidentCommunicator()
responsavel: "Incident Communicator"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Estado atual do incidente do Orchestrator (severidade, servicos, status, acoes em andamento), templates de comunicacao configurados por severidade e fase (detected/investigating/mitigating/resolved), lista de stakeholders por severidade, canal Slack target, historico de updates ja enviados no incidente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens de Slack postadas no war room e canais de stakeholders"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "ticket ClickUp atualizado com timeline de comunicacao"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "status page entry (se integrado)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "rascunhos de comunicado externo para aprovacao do CS (L3 para envio externo)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "summary executivo ao fechar o incidente"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Inicio de incidente declarado pelo Orchestrator; atualizacoes de estado (nova hipotese confirmada, acao executada, mitigacao aplicada, incidente resolvido); intervalo de tempo (heartbeat de status du…"
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

# Comunicar Incidentes

**Task ID:** `incidentCommunicator()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI SRE — Incident Management Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Comunicar Incidentes |
| **status** | `pending` |
| **responsible_executor** | Incident Communicator (Incident Communicator — 'Herald') |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia toda a comunicacao durante o ciclo de vida do incidente. Ao inicio: cria o canal de war room no Slack, envia notificacao inicial com severidade, servicos afetados, impacto estimado e link para o ClickUp task. Durante o incidente: posta atualizacoes de status a cada intervalo configuravel (padrao: 10 min para P1, 30 min para P2) com o que esta sendo investigado/executado. Ao escalon: notifica stakeholders corretos por severidade (P1: CTO + eng leads; P2: tech lead; P3: SRE on-call). Ao resolver: posta o all-clear com resumo executivo. Mantém uma status page interna atualizada. Para clientes externos afetados (quando configurado): gera comunicados em linguagem nao-tecnica para o time de CS.

## Input

- Estado atual do incidente do Orchestrator (severidade, servicos, status, acoes em andamento), templates de comunicacao configurados por severidade e fase (detected/investigating/mitigating/resolved), lista de stakeholders por severidade, canal Slack target, historico de updates ja enviados no incidente

## Output

- Mensagens de Slack postadas no war room e canais de stakeholders
- ticket ClickUp atualizado com timeline de comunicacao
- status page entry (se integrado)
- rascunhos de comunicado externo para aprovacao do CS (L3 para envio externo)
- summary executivo ao fechar o incidente

## Trigger

Inicio de incidente declarado pelo Orchestrator; atualizacoes de estado (nova hipotese confirmada, acao executada, mitigacao aplicada, incidente resolvido); intervalo de tempo (heartbeat de status durante incidente ativo); escalacao HITL; resolucao final

## Knowledge base (o que o executor consulta)

- Templates de comunicacao por severidade e fase (mantidos pelo time)
- lista de stakeholders com contatos e condicoes de notificacao (horario, severidade minima)
- historico de comunicacoes de incidentes anteriores
- runbook de comunicacao externa (para clientes)
- convencoes de nomenclatura de canais Slack
- SLAs de comunicacao exigidos por contrato

## Action Items

1. Confirmar o gatilho e carregar a entrada (Estado atual do incidente do Orchestrator (severidade, servicos, status, acoes em andamento), templates de comunicacao…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens de Slack postadas no war room e canais de stakeholders) e persistir no artefato do squad.
4. Entregar ao critic Fix Guardian; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens de Slack postadas no war room e canais de stakeholders
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

- **to:** Post-Mortem Writer
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
