---
task: atlas()
responsavel: "Atlas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Target Profile v0 + URL do produto + repositórios públicos (GitHub se open source) + reviews de app stores"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sub-relatório Tech/Produto: stack tecnológico identificado, estimativa de divida técnica (Low/Medium/High/Critical), tamanho do time de engenharia, NPS/rating público do produto, red flags de produto (churn de reviews negativas, bugs críticos reportados), diferencial tecnológico (patentes, algoritmos proprietários), score tech 0-10"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Nexus em paralelo com outros workers após aprovacao do Target Profile v0."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Columbo 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complementa com dados adicionais (especialmente se completude < 60). Criticidade: ALTA — avançar com dados incompletos invalida todo o pipeline."
    - "[ ] HITL: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFIED/DISPUTED para decisão: aceitar o risco e prosseguir, solicitar pesquisa adicional (re-ativa workers específicos), ou cancelar a triagem do target."
    - "[ ] HITL: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20% do valuation estimado, irregularidade fiscal grave) pausa o pipeline e exige confirmação do founder antes de prosseguir. Pode levar ao cancelamento imediato da triagem."
    - "[ ] HITL: HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilhamento com advisors, bancos, co-investidores ou o próprio target. Ações irreversíveis (envio externo) sempre requerem aprovação humana explícita."
    - "[ ] HITL: HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados pontos. Eco re-executa com instruções específicas. Não é irreversível, mas é um checkpoint de qualidade importante."
---

# Analisar Maturidade Tecnológica

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Due Diligence / M&A Screening

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Maturidade Tecnológica |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — O Analista de Tech e Produto) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em trilha Tecnologia/Produto/Engineering. Avalia a maturidade tecnológica do target, divida técnica estimada, stack tecnológico, qualidade do produto (reviews de usuários, NPS público), capacidade de engenharia (tamanho do time via LinkedIn, reviews no Glassdoor/Blind), roadmap público e diferenciais de produto. Detecta riscos de lock-in tecnológico ou obsolescência.

## Input

- Target Profile v0 + URL do produto + repositórios públicos (GitHub se open source) + reviews de app stores

## Output

- Sub-relatório Tech/Produto: stack tecnológico identificado, estimativa de divida técnica (Low/Medium/High/Critical), tamanho do time de engenharia, NPS/rating público do produto, red flags de produto (churn de reviews negativas, bugs críticos reportados), diferencial tecnológico (patentes, algoritmos proprietários), score tech 0-10

## Trigger

Ativado pelo Nexus em paralelo com outros workers após aprovacao do Target Profile v0.

## Knowledge base (o que o executor consulta)

- BuiltWith (stack tecnologico), Wappalyzer, GitHub API (repos publicos), App Store/Play Store reviews, Glassdoor/Blind (reviews de engenheiros), LinkedIn (headcount de engenharia), G2/Capterra/Trustpilot (reviews de produto), CVEs publicas (vulnerabilidades), SimilarTech, Stackshare

## Action Items

1. Confirmar o gatilho e carregar a entrada (Target Profile v0 + URL do produto + repositórios públicos (GitHub se open source) + reviews de app stores).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sub-relatório Tech/Produto: stack tecnológico identificado, estimativa de divida técnica (Low/Medium/High/Critical), ta…) e persistir no artefato do squad.
4. Entregar ao critic Columbo 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sub-relatório Tech/Produto: stack tecnológico identificado, estimativa de divida técnica (Low/Medium/High/Critical), tamanho do time de engenharia, NPS/rating…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Columbo 2 registrado
- [ ] Gate HITL respeitado: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude…
- [ ] Gate HITL respeitado: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a list…
- [ ] Gate HITL respeitado: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passiv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complem… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFI… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20%… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilham… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados po… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL Gate L1 — Configuração Inicial do Target: O founder define a intenção estratégica (por que este target, qual a tese inicial, quais setores/mercados são re… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Columbo 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
