# Checklist do critic Columbo 2 — Due Diligence / M&A Screening

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Columbo — O Cético Verificador — Verifica rastreabilidade de 100% dos claims dos workers, detecta alucinações, marca claims sem fonte como UNVERIFIED, simula contra-argumentos do vendedor por red flag, e bloqueia o pipeline se confiança geral < 75. Garante que nenhum Investment Memo entregue ao founder contenha afirmações não verificadas. Opera como gate obrigatório entre Deep Dive e Framework (síntese final).

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Cético Verificador
- [ ] **C02** — Verifica rastreabilidade de 100% dos claims dos workers, detecta alucinações, marca claims sem fonte como UNVERIFIED, simula contra-argumentos do vendedor por red flag, e bloqueia o pipeline se confiança geral < 75
- [ ] **C03** — Garante que nenhum Investment Memo entregue ao founder contenha afirmações não verificadas
- [ ] **C04** — Opera como gate obrigatório entre Deep Dive e Framework (síntese final)

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complementa com dados adicionais (especialmente se completude < 60). Criticidade: ALTA — avançar com dados incompletos invalida todo o pipeline.
- [ ] **HITL** — HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFIED/DISPUTED para decisão: aceitar o risco e prosseguir, solicitar pesquisa adicional (re-ativa workers específicos), ou cancelar a triagem do target.
- [ ] **HITL** — HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20% do valuation estimado, irregularidade fiscal grave) pausa o pipeline e exige confirmação do founder antes de prosseguir. Pode levar ao cancelamento imediato da triagem.
- [ ] **HITL** — HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilhamento com advisors, bancos, co-investidores ou o próprio target. Ações irreversíveis (envio externo) sempre requerem aprovação humana explícita.
- [ ] **HITL** — HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados pontos. Eco re-executa com instruções específicas. Não é irreversível, mas é um checkpoint de qualidade importante.
- [ ] **HITL** — HITL Gate L1 — Configuração Inicial do Target: O founder define a intenção estratégica (por que este target, qual a tese inicial, quais setores/mercados são relevantes) antes do início do pipeline. Isso calibra os pesos do Scorecard e o foco dos workers.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
