# Checklist do critic Censor Comercial — Qualificação Conversacional

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Censor Comercial — Veto — Critic/Verifier que intercepta TODA mensagem de WhatsApp antes do envio e todo scorecard antes de chegar ao closer. Para mensagens: verifica personalizacao (nome correto, contexto do anuncio refletido), tom (nao robotico, nao invasivo, sem promessas comerciais nao autorizadas), compliance LGPD (sem solicitacao de dados sensiveis sem base legal, opt-out respeitado), factualidade (nenhuma informacao sobre produto/preco que nao esteja na knowledge base do cliente). Para scorecards: verifica se todos os 4 criterios BANT foram coletados antes de classificar HOT, se o score foi calculado com os pesos corretos, se o resumo para o closer e acionavel. Bloqueia envio/promocao e retorna para reescrita se reprovar. Autonomy L1 pois nao age — apenas aprova ou bloqueia com justificativa.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Censor Comercial
- [ ] **C02** — Critic/Verifier que intercepta TODA mensagem de WhatsApp antes do envio e todo scorecard antes de chegar ao closer
- [ ] **C03** — Para mensagens: verifica personalizacao (nome correto, contexto do anuncio refletido), tom (nao robotico, nao invasivo, sem promessas comerciais nao autorizadas), compliance LGPD (sem solicitacao de dados sensiveis sem base legal, opt-out respeitado), factualidade (nenhuma informacao sobre produto/preco que nao esteja na knowledge base do cliente)
- [ ] **C04** — Para scorecards: verifica se todos os 4 criterios BANT foram coletados antes de classificar HOT, se o score foi calculado com os pesos corretos, se o resumo para o closer e acionavel
- [ ] **C05** — Bloqueia envio/promocao e retorna para reescrita se reprovar
- [ ] **C06** — Autonomy L1 pois nao age
- [ ] **C07** — apenas aprova ou bloqueia com justificativa

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comercial aprova batch antes do disparo.
- [ ] **HITL** — HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por desconto, Vera responde 'vou verificar com nosso especialista' e escala ao closer via notificação imediata.
- [ ] **HITL** — HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes de qualquer ação automática adicional. Closer decide se assume a conversa ou deixa o squad continuar.
- [ ] **HITL** — HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada.
- [ ] **HITL** — HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor responde o que fazer; resposta é adicionada ao playbook para aprendizado.
- [ ] **HITL** — HITL-6 (L1): Relatório semanal do Eco com sugestões de ajuste de prompt — gestor revisa e aprova antes de qualquer alteração ser aplicada nos prompts da Vera ou nos pesos do Magnus.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
