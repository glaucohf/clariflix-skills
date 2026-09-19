# Checklist do critic Vigia 2 — Follow-up, Nurture e Reativacao

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Vigia — Critic de Mensagens e Compliance — Verificador obrigatorio de todas as mensagens antes do envio externo. Atua como red-team em 5 dimensoes (personalizacao, tom, compliance, factualidade, eficacia). Reprova e devolve com instrucao de correcao. Se o Volta falhar 2x na correcao, escala automaticamente para HITL. Tambem faz auditoria semanal das cadencias para identificar padroes de baixa performance e recomendar ajustes ao Maestro.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Mensagens e Compliance
- [ ] **C02** — Verificador obrigatorio de todas as mensagens antes do envio externo
- [ ] **C03** — Atua como red-team em 5 dimensoes (personalizacao, tom, compliance, factualidade, eficacia)
- [ ] **C04** — Reprova e devolve com instrucao de correcao
- [ ] **C05** — Se o Volta falhar 2x na correcao, escala automaticamente para HITL
- [ ] **C06** — Tambem faz auditoria semanal das cadencias para identificar padroes de baixa performance e recomendar ajustes ao Maestro

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou edita antes do envio pelo Volta
- [ ] **L3** — Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio
- [ ] **L3** — Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar
- [ ] **L3** — Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordagem antes de qualquer novo toque
- [ ] **HITL** — Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão manual
- [ ] **HITL** — Revisão semanal de cadências — Atlas gera relatório de performance; gestor aprova ajustes de parâmetros (intervalos, canais, thresholds de score) antes de serem aplicados
- [ ] **HITL** — Opt-out recebido — Qualquer pedido de descadastro é interrompido imediatamente pelo Cronos e notificado ao responsável para confirmação de remoção do CRM

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
