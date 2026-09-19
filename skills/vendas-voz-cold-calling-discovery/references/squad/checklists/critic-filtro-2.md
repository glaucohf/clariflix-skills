# Checklist do critic Filtro 2 — Voz para Cold Calling e Discovery

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Filtro (Critic/Verifier de Qualificação e Compliance) — Verificador crítico que audita cada call antes de avançar no funil: valida preenchimento genuíno de BANT/MEDDIC, detecta promessas comerciais não autorizadas, checa compliance LGPD (opt-out, horários), avalia tom e aderência ao roteiro. Bloqueia leads mal qualificados e sinaliza anomalias para revisão humana. Opera como red-team interno do squad, prevenindo que leads de baixa qualidade contaminem o pipeline do closer.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Filtro (Critic/Verifier de Qualificação e Compliance)
- [ ] **C02** — Verificador crítico que audita cada call antes de avançar no funil: valida preenchimento genuíno de BANT/MEDDIC, detecta promessas comerciais não autorizadas, checa compliance LGPD (opt-out, horários), avalia tom e aderência ao roteiro
- [ ] **C03** — Bloqueia leads mal qualificados e sinaliza anomalias para revisão humana
- [ ] **C04** — Opera como red-team interno do squad, prevenindo que leads de baixa qualidade contaminem o pipeline do closer

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3).
- [ ] **HITL** — Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3).
- [ ] **HITL** — Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3).
- [ ] **HITL** — Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3).
- [ ] **HITL** — Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation).
- [ ] **HITL** — Confirmação de reagendamento quando prospect cancela reunião pela segunda vez consecutiva (decisão humana sobre continuar ou desqualificar — L3).
- [ ] **HITL** — Calibragem quinzenal de voz e persona do Vox Agent com gestor de vendas (revisão humana de amostras de áudio — L1).

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
