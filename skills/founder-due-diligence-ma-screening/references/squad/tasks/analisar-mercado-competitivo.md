---
task: sigma()
responsavel: "Sigma"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Target Profile v0 + tese de aquisição do founder + mapa de concorrentes do setor"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sub-relatório de Mercado: TAM/SAM/SOM estimados com fontes, posicionamento vs top 3 concorrentes, share de mercado estimado, moat assessment (network effects, switching cost, brand, cost), tendências favoráveis/desfavoráveis, sinergias quantificadas (receita cruzada, redução de CAC, expansão geográfica), score de mercado 0-10"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Nexus em paralelo com outros workers apos aprovação do Target Profile v0."
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

# Analisar Mercado Competitivo

**Task ID:** `sigma()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Due Diligence / M&A Screening

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Mercado Competitivo |
| **status** | `pending` |
| **responsible_executor** | Sigma (Sigma — O Analista de Mercado) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em trilha Mercado/Posicionamento/Competitivo. Mapeia o mercado addressable do target, posicionamento competitivo, dinamica de concorrencia, share estimado, tendencias de setor, barreiras de entrada e sinergias potenciais com o adquirente. Usa frameworks de analise competitiva (Porter, Jobs-to-be-Done, moat analysis).

## Input

- Target Profile v0 + tese de aquisição do founder + mapa de concorrentes do setor

## Output

- Sub-relatório de Mercado: TAM/SAM/SOM estimados com fontes, posicionamento vs top 3 concorrentes, share de mercado estimado, moat assessment (network effects, switching cost, brand, cost), tendências favoráveis/desfavoráveis, sinergias quantificadas (receita cruzada, redução de CAC, expansão geográfica), score de mercado 0-10

## Trigger

Ativado pelo Nexus em paralelo com outros workers apos aprovação do Target Profile v0.

## Knowledge base (o que o executor consulta)

- Relatórios de mercado públicos (IBISWorld resumos gratuitos, Statista previews, consultorias), cobertura de imprensa especializada, LinkedIn para estimativa de headcount e crescimento, SimilarWeb (tráfego estimado), dados de App Store/Play Store se aplicável, comparáveis setoriais do Nexus knowledge base

## Action Items

1. Confirmar o gatilho e carregar a entrada (Target Profile v0 + tese de aquisição do founder + mapa de concorrentes do setor).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sub-relatório de Mercado: TAM/SAM/SOM estimados com fontes, posicionamento vs top 3 concorrentes, share de mercado esti…) e persistir no artefato do squad.
4. Entregar ao critic Columbo 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sub-relatório de Mercado: TAM/SAM/SOM estimados com fontes, posicionamento vs top 3 concorrentes, share de mercado estimado, moat assessment (network effects,…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
