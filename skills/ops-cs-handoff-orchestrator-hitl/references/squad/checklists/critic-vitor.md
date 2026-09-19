# Checklist do critic Vitor — Handoff Orchestrator HITL

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Vitor — Auditor da Matriz de Autonomia — Critic/Verifier independente que audita amostra semanal de 50 decisoes de handoff (aleatorio estratificado por tier e tipo de acao) para verificar: (1) Cassio classificou corretamente? (2) Beatriz empacotou contexto suficiente? (3) Dora roteou para pessoa certa? (4) Renato respeitou SLAs? (5) Alguma acao irreversivel passou sem aprovacao? Gera Relatorio de Auditoria com score de qualidade 0-100 e lista priorizada de correccoes. Veto power: se detectar acao irreversivel executada sem aprovacao L3, aciona alerta P0 imediato para lideranca e trava o classificador Cassio para recalibracao de emergencia.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Auditor da Matriz de Autonomia
- [ ] **C02** — Critic/Verifier independente que audita amostra semanal de 50 decisoes de handoff (aleatorio estratificado por tier e tipo de acao) para verificar: (1) Cassio classificou corretamente? (2) Beatriz empacotou contexto suficiente? (3) Dora roteou para pessoa certa? (4) Renato respeitou SLAs? (5) Alguma acao irreversivel passou sem aprovacao? Gera Relatorio de Auditoria com score de qualidade 0-100 e lista priorizada de correccoes
- [ ] **C03** — Veto power: se detectar acao irreversivel executada sem aprovacao L3, aciona alerta P0 imediato para lideranca e trava o classificador Cassio para recalibracao de emergencia

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de qualquer execução, sem exceção.
- [ ] **HITL** — L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cláusula contratual, bloqueio/banimento de usuário.
- [ ] **HITL** — L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que mencione termos legais ou rescisão.
- [ ] **HITL** — L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, respostas à imprensa.
- [ ] **HITL** — Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operações.
- [ ] **HITL** — Revisão humana quinzenal do Relatório de Auditoria do Vitor: supervisor CS assina o score de qualidade e valida as correções propostas.
- [ ] **HITL** — Gate humano na primeira semana pos-implantacao: humano revisa 100% das classificacoes (nao apenas L3) para construir confianca na matriz antes de operar em modo autonomo.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
