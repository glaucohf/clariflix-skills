# Checklist do critic Aegis — ABM Signal Orchestrator

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Aegis — Verificador de Qualidade e Compliance — Gate obrigatorio antes de qualquer envio externo (email, ad publish, LinkedIn message, WhatsApp). Verifica: (1) aderencia ao brand voice e tom da empresa, (2) personalizacao real (rejeita copy generico sem mencao a sinal especifico da conta), (3) compliance legal (CAN-SPAM, LGPD, politica anti-spam do canal), (4) coerencia entre canais (mesma conta nao recebe mensagens contraditórias), (5) score de qualidade de copy (clareza, CTA, relevancia). Inspirado no Skeptic Protocol (squad gratuito de red-team/QA).

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Verificador de Qualidade e Compliance
- [ ] **C02** — Gate obrigatorio antes de qualquer envio externo (email, ad publish, LinkedIn message, WhatsApp)
- [ ] **C03** — Verifica: (1) aderencia ao brand voice e tom da empresa, (2) personalizacao real (rejeita copy generico sem mencao a sinal especifico da conta), (3) compliance legal (CAN-SPAM, LGPD, politica anti-spam do canal), (4) coerencia entre canais (mesma conta nao recebe mensagens contraditórias), (5) score de qualidade de copy (clareza, CTA, relevancia)
- [ ] **C04** — Inspirado no Skeptic Protocol (squad gratuito de red-team/QA)

## Gates humanos (bloqueiam até decisão)

- [ ] **L3** — Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plataformas de ads
- [ ] **L3** — Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad
- [ ] **L3** — Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio
- [ ] **L2** — Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha completa
- [ ] **L2** — Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana sobre próximos passos
- [ ] **L1** — Curadoria do Account Universe Map: adicionar/remover contas do universo ABM e ajustar Tiers requer input estratégico humano (revisão quinzenal)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
