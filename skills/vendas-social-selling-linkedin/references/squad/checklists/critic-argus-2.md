# Checklist do critic Argus 2 — Social Selling e Inbound LinkedIn

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Fiscal de Mensagem (Argus) — Verificador/red-team de todas as mensagens antes do envio externo. Valida factualidade do sinal citado, genuinidade da personalização, compliance comercial, tom e proporcionalidade. Único ponto de bloqueio automático no pipeline — nenhuma mensagem chega ao lead sem passar pelo Argus. Opera em modo adversarial: assume que o Cypher tentou atalhar a personalização.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Fiscal de Mensagem (Argus)
- [ ] **C02** — Verificador/red-team de todas as mensagens antes do envio externo
- [ ] **C03** — Valida factualidade do sinal citado, genuinidade da personalização, compliance comercial, tom e proporcionalidade
- [ ] **C04** — Único ponto de bloqueio automático no pipeline
- [ ] **C05** — nenhuma mensagem chega ao lead sem passar pelo Argus
- [ ] **C06** — Opera em modo adversarial: assume que o Cypher tentou atalhar a personalização

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Mensagens para contas tier-1 (lista de contas estratégicas definida pelo cliente): humano aprova cada toque antes do envio — L3 obrigatório.
- [ ] **HITL** — Resposta HOT de lead em conta tier-1: notificação imediata ao closer/AE com contexto completo antes de qualquer resposta automatizada.
- [ ] **HITL** — Mensagem bloqueada pelo Argus após 2 iterações de revisão: escala para SDR humano com o feedback do Critic para reescrever manualmente.
- [ ] **HITL** — Qualquer menção a preço, desconto ou condição comercial detectada no rascunho do Cypher: bloqueia e encaminha para aprovação humana.
- [ ] **HITL** — Anomalia detectada pelo Nexus (ex: taxa de resposta cai >30% em 48h, sinais zerados, spike de unsubscribes): alerta para gestor de vendas revisar configuração.
- [ ] **HITL** — Primeiro envio de cadência para um novo segmento/persona não testado anteriormente: SDR revisa amostra de 5 mensagens antes de liberar automação plena.
- [ ] **HITL** — Lead responde mencionando nome de concorrente ou fazendo pergunta técnica complexa: desvia para SDR humano com contexto completo da conversa.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
