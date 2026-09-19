# Checklist do critic Rex 2 — CRO & Landing Page Agêntico

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Rex — Critic & Brand Voice Verifier — Implementa o padrao Skeptic Protocol para o squad de CRO: desafia cada variacao antes de publicacao, verifica alinhamento de brand voice e tom, valida message match entre ad e landing page, detecta claims sem substantiation e urgencia falsa, audita compliance legal do copy, e garante que nenhum experimento publico contradiga o posicionamento da marca. Gate L3 obrigatorio e nao-bypassavel — nenhuma variacao vai ao ar sem aprovacao de Rex. Em caso de BLOCKED, escala imediatamente para HITL humano antes de qualquer acao.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — Critic & Brand Voice Verifier
- [ ] **C02** — Implementa o padrao Skeptic Protocol para o squad de CRO: desafia cada variacao antes de publicacao, verifica alinhamento de brand voice e tom, valida message match entre ad e landing page, detecta claims sem substantiation e urgencia falsa, audita compliance legal do copy, e garante que nenhum experimento publico contradiga o posicionamento da marca
- [ ] **C03** — Gate L3 obrigatorio e nao-bypassavel
- [ ] **C04** — nenhuma variacao vai ao ar sem aprovacao de Rex
- [ ] **C05** — Em caso de BLOCKED, escala imediatamente para HITL humano antes de qualquer acao

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção
- [ ] **HITL** — Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final
- [ ] **HITL** — Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)
- [ ] **HITL** — Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)
- [ ] **HITL** — Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)
- [ ] **HITL** — Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): implica realocação de budget
- [ ] **HITL** — Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hipoteses devem ser arquivadas (L1)

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
