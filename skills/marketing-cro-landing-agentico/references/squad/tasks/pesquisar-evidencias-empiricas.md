---
task: sage()
responsavel: "Sage"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de concorrentes diretos e referências de setor (URLs das landing pages), verticais de mercado a pesquisar, hipóteses de CRO candidatas para validar com pesquisa externa, ICP Profile do squad Living ICP Profiler (se disponível) para calibrar a pesquisa de audiência"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "CRO Research Report com top-10 hipóteses de experimento evidenciadas (fonte, contexto, lift reportado), Competitive Copy Analysis (como os 5 concorrentes principais trabalham headline, proposta de valor, CTA e social proof), Persuasion Principles Map (quais princípios psicológicos são mais relevantes para o produto e audiência), biblioteca de referências para cada hipótese ativa no backlog"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Fase Discovery de cada ciclo; inclusão de nova hipótese no backlog que necessita de embasamento; Maestro solicita benchmarking de setor específico; resultado de experimento contraintuitivo que precis…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Rex 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção"
    - "[ ] HITL: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final"
    - "[ ] HITL: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)"
    - "[ ] HITL: Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)"
    - "[ ] HITL: Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)"
---

# Pesquisar Evidências Empíricas

**Task ID:** `sage()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Pesquisar Evidências Empíricas |
| **status** | `pending` |
| **responsible_executor** | Sage (Sage — CRO Research Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pesquisador especializado em CRO, copywriting e psicologia de conversão. Executa deepresearch em estudos de caso do setor, princípios de persuasão aplicados à conversão (Cialdini, Kahneman, Nielsen Norman Group), análise de copy dos concorrentes e tendências de UX. Calibra as hipóteses do squad com evidências empíricas de fora da empresa — evita que o squad repita erros já documentados pela indústria. Alias: 'Sage' — o sábio que sempre traz a evidência antes de qualquer decisão.

## Input

- Lista de concorrentes diretos e referências de setor (URLs das landing pages), verticais de mercado a pesquisar, hipóteses de CRO candidatas para validar com pesquisa externa, ICP Profile do squad Living ICP Profiler (se disponível) para calibrar a pesquisa de audiência

## Output

- CRO Research Report com top-10 hipóteses de experimento evidenciadas (fonte, contexto, lift reportado), Competitive Copy Analysis (como os 5 concorrentes principais trabalham headline, proposta de valor, CTA e social proof), Persuasion Principles Map (quais princípios psicológicos são mais relevantes para o produto e audiência), biblioteca de referências para cada hipótese ativa no backlog

## Trigger

Fase Discovery de cada ciclo; inclusão de nova hipótese no backlog que necessita de embasamento; Maestro solicita benchmarking de setor específico; resultado de experimento contraintuitivo que precisa de contexto externo para interpretação

## Knowledge base (o que o executor consulta)

- Biblioteca de estudos de caso CRO (ConversionXL, Unbounce, VWO Case Studies), princípios de psicologia de conversão documentados (Cialdini, Nielsen Norman, bayes-based copywriting), landing pages dos concorrentes (screenshots e copy extraído), relatórios de benchmark de conversão por indústria (Wordstream, Google benchmarks), pesquisas de Jobs-to-be-Done do produto

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de concorrentes diretos e referências de setor (URLs das landing pages), verticais de mercado a pesquisar, hipóte…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (CRO Research Report com top-10 hipóteses de experimento evidenciadas (fonte, contexto, lift reportado), Competitive Cop…) e persistir no artefato do squad.
4. Entregar ao critic Rex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: CRO Research Report com top-10 hipóteses de experimento evidenciadas (fonte, contexto, lift reportado), Competitive Copy Analysis (como os 5 concorrentes princ…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Rex 2 registrado
- [ ] Gate HITL respeitado: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção d…
- [ ] Gate HITL respeitado: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na pág…
- [ ] Gate HITL respeitado: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel lega…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3)… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de pro… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qu… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão es… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hi… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Rex 2 | BLOQUEIA entrega |

## Handoff

- **to:** Muse
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
