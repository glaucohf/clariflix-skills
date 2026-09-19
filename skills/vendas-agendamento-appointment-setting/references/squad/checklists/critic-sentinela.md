# Checklist do critic Sentinela — Agendamento

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Sentinela — Critic e Verifier de Mensagens e Compliance — Intercepta TODA mensagem externa antes do envio (confirmacoes, lembretes, reagendamentos, outreach). Valida: (1) personalizacao correta — nome, empresa e contexto do lead estao corretos e nao ha variaveis nao substituidas tipo {{nome}}; (2) tom adequado ao estagio do funil — nao agressivo em leads frios, nao generico em leads quentes; (3) compliance de horario — nao enviar fora da janela permitida; (4) limite de frequencia — lead nao esta recebendo mensagens demais; (5) dados corretos — horario, link e vendedor na mensagem batem com o evento no calendario. Bloqueia envio se qualquer check falhar e retorna para correcao com feedback especifico. Registra todas as validacoes como prova de trabalho.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Sentinela
- [ ] **C02** — Critic e Verifier de Mensagens e Compliance
- [ ] **C03** — Intercepta TODA mensagem externa antes do envio (confirmacoes, lembretes, reagendamentos, outreach)
- [ ] **C04** — Valida: (1) personalizacao correta
- [ ] **C05** — nome, empresa e contexto do lead estao corretos e nao ha variaveis nao substituidas tipo {{nome}}
- [ ] **C06** — (2) tom adequado ao estagio do funil
- [ ] **C07** — nao agressivo em leads frios, nao generico em leads quentes
- [ ] **C08** — (3) compliance de horario
- [ ] **C09** — nao enviar fora da janela permitida
- [ ] **C10** — (4) limite de frequencia
- [ ] **C11** — lead nao esta recebendo mensagens demais
- [ ] **C12** — (5) dados corretos
- [ ] **C13** — horario, link e vendedor na mensagem batem com o evento no calendario
- [ ] **C14** — Bloqueia envio se qualquer check falhar e retorna para correcao com feedback especifico
- [ ] **C15** — Registra todas as validacoes como prova de trabalho

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Aprovação humana obrigatória antes de qualquer contato com conta estratégica (deal acima de threshold configurado, ex: R$50k+) para revisar abordagem e personalização antes do envio.
- [ ] **L3** — Autorização para oferecer desconto ou condição especial durante negociação de horário/formato da reunião (ex: lead pede reunião presencial fora da política padrão).
- [ ] **L3** — Aprovação para reativar lead que foi marcado como LOST ou DISQUALIFIED pelo sistema — requer revisão humana do motivo original antes de nova tentativa.
- [ ] **L2** — Notificação ao closer/SDR quando lead muda de COLD para HOT (score sobe 30+ pontos em 24h) para decisão de abordar manualmente em vez de deixar o squad rodar sozinho.
- [ ] **L2** — Alerta ao gerente de vendas quando taxa de no-show da semana ultrapassar threshold configurado (ex: >20%) — indica problema sistêmico que requer revisão de ICP ou abordagem.
- [ ] **L1** — Revisão humana do briefing pre-reunião antes do envio ao closer, opcional mas recomendado nas primeiras 2 semanas de operação do squad para calibragem.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
