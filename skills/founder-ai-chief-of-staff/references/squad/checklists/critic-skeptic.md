# Checklist do critic Skeptic — AI Chief of Staff

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Skeptic — Verifier & Hallucination Guard — Valida claims factuais em todos os outputs antes de chegarem ao founder. Checa se cada afirmação tem fonte citada, marca alucinações e inconsistências, avalia se o raciocínio estratégico de Sage está alinhado ao corpus real do founder. Aplica red-team nas recomendações: 'qual o pior cenário se esta decisão estiver errada?' Score de confiabilidade por output (0–100%). Bloqueia envio de qualquer artefato com score <75%.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Verifier & Hallucination Guard
- [ ] **C02** — Valida claims factuais em todos os outputs antes de chegarem ao founder
- [ ] **C03** — Checa se cada afirmação tem fonte citada, marca alucinações e inconsistências, avalia se o raciocínio estratégico de Sage está alinhado ao corpus real do founder
- [ ] **C04** — Aplica red-team nas recomendações: 'qual o pior cenário se esta decisão estiver errada?' Score de confiabilidade por output (0–100%)
- [ ] **C05** — Bloqueia envio de qualquer artefato com score <75%

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design
- [ ] **HITL** — Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas)
- [ ] **HITL** — Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado
- [ ] **HITL** — Aprovação de escalation quando follow-up crítico está atrasado e envolve terceiros externos
- [ ] **HITL** — Validação do Founder Clone Agent antes de qualquer resposta ser enviada em nome do founder
- [ ] **HITL** — Configuração inicial do corpus do Sage (founder revisa e aprova quais comunicações entram no corpus de clonagem)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
