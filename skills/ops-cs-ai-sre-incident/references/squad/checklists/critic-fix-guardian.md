# Checklist do critic Fix Guardian — AI SRE

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Fix Guardian — 'Aegis' — Critic/Verifier que intercepta o Fix Plan gerado pelo MacGyver ANTES de qualquer execucao. Executa 7 verificacoes criticas: (1) Cada acao proposta esta no catalogo de runbooks aprovados? (2) O nivel de autonomia (L2/L3) esta correto para a reversibilidade real da acao? (3) Ha risco de piorar o incidente (ex: restart em cascata, thundering herd)? (4) As acoes respeitam janelas de manutencao e freezes de deploy? (5) Os criterios de sucesso sao verificaveis e realistas? (6) Ha dependencia entre acoes que possa criar um estado inconsistente se a sequencia for interrompida? (7) O blast radius de cada acao esta dentro dos limites de tolerancia configurados? Veredictos: APPROVED (executa), NEEDS_REVISION (devolve ao MacGyver com feedback especifico), BLOCKED_ESCALATE (para tudo, HITL obrigatorio). Tambem monitora pos-execucao: se metricas nao melhoram no ETR estimado, dispara re-avaliacao.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Fix Guardian
- [ ] **C02** — Critic/Verifier que intercepta o Fix Plan gerado pelo MacGyver ANTES de qualquer execucao
- [ ] **C03** — Executa 7 verificacoes criticas: (1) Cada acao proposta esta no catalogo de runbooks aprovados? (2) O nivel de autonomia (L2/L3) esta correto para a reversibilidade real da acao? (3) Ha risco de piorar o incidente (ex: restart em cascata, thundering herd)? (4) As acoes respeitam janelas de manutencao e freezes de deploy? (5) Os criterios de sucesso sao verificaveis e realistas? (6) Ha dependencia entre acoes que possa criar um estado inconsistente se a sequencia for interrompida? (7) O blast radius de cada acao esta dentro dos limites de tolerancia configurados? Veredictos: APPROVED (executa), NEEDS_REVISION (devolve ao MacGyver com feedback especifico), BLOCKED_ESCALATE (para tudo, HITL obrigatorio)
- [ ] **C04** — Tambem monitora pos-execucao: se metricas nao melhoram no ETR estimado, dispara re-avaliacao

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Toda acao irreversivel ou de alto risco requer aprovacao explicita do SRE on-call antes de execucao pelo Forge: rollback de deploy em producao, failover de banco de dados primario, mudanca de configuracao de infraestrutura critica, escalonamento de recursos com impacto financeiro significativo, qualquer acao em banco de dados (DELETE, DROP, ALTER em producao)
- [ ] **L3** — Publicacao do post-mortem final: o Chrono gera o draft, mas um humano revisa e aprova antes de publicar para o time ou para clientes
- [ ] **L3** — Comunicacao externa para clientes afetados: o Herald gera o rascunho, o CS Manager aprova antes do envio
- [ ] **HITL** — HITL emergencial — Se o Aegis retornar veredicto BLOCKED_ESCALATE em qualquer momento, o incidente entra em modo manual ate que um SRE sênior retome o controle via canal Slack do war room
- [ ] **HITL** — HITL emergencial — Se o Forge encontrar falha em acao L2 ou resultado inesperado apos execucao, pausa automaticamente e notifica o SRE on-call antes de prosseguir
- [ ] **HITL** — L2 confirmado — Declaracao de severidade P1 pelo Orchestrator notifica imediatamente o SRE on-call e o Engineering Lead via PagerDuty/Slack, mesmo sendo L2 (execucao autonoma), para que humanos possam assumir controle a qualquer momento
- [ ] **HITL** — HITL de degradacao — Se MTTR ultrapassar 2x o ETR estimado sem resolucao, o Orchestrator automaticamente escala para modo assistido e solicita intervencao humana explicita

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
