# Checklist do critic Argus — AI SDR Outbound Signal-Based

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Argus — Verificador de Mensagens e Compliance — Valida cada draft gerado pelo Penna ANTES de qualquer envio. Checklist de 8 pontos: (1) Personalizacao real — a mensagem usa pelo menos 2 elementos especificos do dossie do Sherlock (nao frases genericas)? (2) Factualidade — todas as afirmacoes sobre a empresa/lead sao verificaveis no dossie? (3) Tom adequado ao canal e cargo? (4) CTA claro e unico? (5) Compliance LGPD — tem mecanismo de opt-out, nao promete resultados garantidos, nao usa dados sensiveis? (6) Ausencia de red flags — sem pressao excessiva, sem promessas comerciais nao autorizadas, sem desconto nao aprovado? (7) Comprimento adequado ao canal (email: max 150 palavras no cold; WhatsApp: max 3 blocos curtos)? (8) Subject line tem menos de 50 caracteres e nao parece spam? Veredicto: APROVADO / REESCREVER (com instrucoes especificas) / BLOQUEAR_HITL (para casos que exigem revisao humana). Maximo 2 ciclos de reescritura automatica antes de escalar.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Verificador de Mensagens e Compliance
- [ ] **C02** — Valida cada draft gerado pelo Penna ANTES de qualquer envio
- [ ] **C03** — Checklist de 8 pontos: (1) Personalizacao real
- [ ] **C04** — a mensagem usa pelo menos 2 elementos especificos do dossie do Sherlock (nao frases genericas)? (2) Factualidade
- [ ] **C05** — todas as afirmacoes sobre a empresa/lead sao verificaveis no dossie? (3) Tom adequado ao canal e cargo? (4) CTA claro e unico? (5) Compliance LGPD
- [ ] **C06** — tem mecanismo de opt-out, nao promete resultados garantidos, nao usa dados sensiveis? (6) Ausencia de red flags
- [ ] **C07** — sem pressao excessiva, sem promessas comerciais nao autorizadas, sem desconto nao aprovado? (7) Comprimento adequado ao canal (email: max 150 palavras no cold
- [ ] **C08** — WhatsApp: max 3 blocos curtos)? (8) Subject line tem menos de 50 caracteres e nao parece spam? Veredicto: APROVADO / REESCREVER (com instrucoes especificas) / BLOQUEAR_HITL (para casos que exigem revisao humana)
- [ ] **C09** — Maximo 2 ciclos de reescritura automatica antes de escalar

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo.
- [ ] **HITL** — Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial.
- [ ] **HITL** — Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual.
- [ ] **HITL** — Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo.
- [ ] **HITL** — Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach.
- [ ] **HITL** — Unsubscribe ou resposta negativa agressiva: processado pelo Lumen, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
