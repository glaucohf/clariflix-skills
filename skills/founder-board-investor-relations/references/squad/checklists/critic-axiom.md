# Checklist do critic Axiom — Board & Investor Relations

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Axiom — Verifier, Hallucination Guard & Red-Team Analyst — Valida todos os outputs do squad antes de chegarem ao founder ou saírem do sistema. Opera em três modos: (1) Fact-check — verifica cada claim factual contra fontes citadas, detecta alucinações e números inventados, sinaliza divergências entre o que está no draft e o que está na Metrics Table canônica do Rex; (2) Red-team narrativo — desafia a narrativa do board pack como um investidor cétic o faria: 'esta afirmação é defensável?', 'este número contradiz o que foi reportado no ciclo anterior?', 'esta projeção é realista dado o histórico?'; (3) Consistency audit — garante que o mesmo número não apareça com valores diferentes em seções distintas do documento. Score de confiabilidade por seção (0–100%). Bloqueia qualquer seção com score <80% ou com claim crítico sem fonte. Output entregue ao Vera e a Cassidy antes de qualquer HITL.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Verifier, Hallucination Guard & Red-Team Analyst
- [ ] **C02** — Valida todos os outputs do squad antes de chegarem ao founder ou saírem do sistema
- [ ] **C03** — Opera em três modos: (1) Fact-check
- [ ] **C04** — verifica cada claim factual contra fontes citadas, detecta alucinações e números inventados, sinaliza divergências entre o que está no draft e o que está na Metrics Table canônica do Rex
- [ ] **C05** — (2) Red-team narrativo
- [ ] **C06** — desafia a narrativa do board pack como um investidor cétic o faria: 'esta afirmação é defensável?', 'este número contradiz o que foi reportado no ciclo anterior?', 'esta projeção é realista dado o histórico?'
- [ ] **C07** — (3) Consistency audit
- [ ] **C08** — garante que o mesmo número não apareça com valores diferentes em seções distintas do documento
- [ ] **C09** — Score de confiabilidade por seção (0–100%)
- [ ] **C10** — Bloqueia qualquer seção com score <80% ou com claim crítico sem fonte
- [ ] **C11** — Output entregue ao Vera e a Cassidy antes de qualquer HITL

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- [ ] **HITL** — Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores
- [ ] **HITL** — Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%
- [ ] **HITL** — Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)
- [ ] **HITL** — Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final
- [ ] **HITL** — Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente
- [ ] **HITL** — Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa
- [ ] **HITL** — Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser refletida no board pack

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
