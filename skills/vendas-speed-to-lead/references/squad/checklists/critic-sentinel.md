# Checklist do critic Sentinel — Speed-to-Lead

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Sentinel — Critic de Mensagem e Compliance — Intercepta toda mensagem ANTES do envio externo para validar: (1) personalizacao correta (nome, empresa, produto correto); (2) tom adequado ao canal e estagio do funil; (3) compliance com LGPD e politicas de spam (sem envio para contatos que optaram por nao receber); (4) factualidade — sem promessas comerciais nao autorizadas, precos incorretos ou claims inventados; (5) ausencia de dados sensiveis expostos indevidamente. Retorna APROVADO ou BLOQUEADO com raiz do problema. Maximo 2 iteracoes de corrececao automatica — na 3a, escala para HITL.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic de Mensagem e Compliance
- [ ] **C02** — Intercepta toda mensagem ANTES do envio externo para validar: (1) personalizacao correta (nome, empresa, produto correto)
- [ ] **C03** — (2) tom adequado ao canal e estagio do funil
- [ ] **C04** — (3) compliance com LGPD e politicas de spam (sem envio para contatos que optaram por nao receber)
- [ ] **C05** — (4) factualidade
- [ ] **C06** — sem promessas comerciais nao autorizadas, precos incorretos ou claims inventados
- [ ] **C07** — (5) ausencia de dados sensiveis expostos indevidamente
- [ ] **C08** — Retorna APROVADO ou BLOQUEADO com raiz do problema
- [ ] **C09** — Maximo 2 iteracoes de corrececao automatica
- [ ] **C10** — na 3a, escala para HITL

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead
- [ ] **HITL** — Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto
- [ ] **HITL** — Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio
- [ ] **HITL** — Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel
- [ ] **HITL** — Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano
- [ ] **HITL** — Reagendamento apos segundo no-show — Atlas escala para closer decidir se continua ou descarta lead
- [ ] **HITL** — Lead demonstra sinal negativo forte (reclamacao de contato excessivo, solicitacao de opt-out) — intervencao humana obrigatoria e imediata

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
