# Checklist do critic Nemesis — Forecast de Pipeline e Risco de Deal

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Nemesis — Verificador de Alertas — Critic/Verifier que intercepta TODOS os alertas antes do envio externo. Verifica: (1) o score de risco está matematicamente coerente com os dados do deal? (2) o alerta não é duplicado ou dentro da janela de silêncio? (3) o tom da mensagem é apropriado para o canal e stakeholder? (4) a ação recomendada é factível no contexto atual do deal? (5) o alerta pode criar constrangimento ou comprometer negociação em andamento? Bloqueia ou solicita revisão antes de qualquer notificação sair.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Verificador de Alertas
- [ ] **C02** — Critic/Verifier que intercepta TODOS os alertas antes do envio externo
- [ ] **C03** — Verifica: (1) o score de risco está matematicamente coerente com os dados do deal? (2) o alerta não é duplicado ou dentro da janela de silêncio? (3) o tom da mensagem é apropriado para o canal e stakeholder? (4) a ação recomendada é factível no contexto atual do deal? (5) o alerta pode criar constrangimento ou comprometer negociação em andamento? Bloqueia ou solicita revisão antes de qualquer notificação sair

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora da empresa
- [ ] **L3** — Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM
- [ ] **L2** — Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa
- [ ] **L2** — Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle
- [ ] **L1** — Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
