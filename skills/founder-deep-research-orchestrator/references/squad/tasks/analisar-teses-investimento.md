---
task: thesis()
responsavel: "Thesis"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sub-questão de tese ou análise financeira de Orion + empresa ou setor-alvo + tipo de análise (valuation, múltiplos, narrativa de VC, benchmarks de crescimento, unit economics)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Síntese de teses: { thesis_source, investor_name_or_fund, thesis_summary, key_metrics_cited, bull_case, bear_case, source_url, publication_date }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Benchmarks setoriais comparáveis"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Narrativa de consenso vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "visão contrária"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion roteia sub-questão classificada como 'investment_thesis' ou 'valuation' ou 'fundraising' ou 'due_diligence'. Também ativado quando founder prepara board pack ou reunião com investidores."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vera 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicação financeira direta — Orion apresenta o Research Brief ao founder para aprovação antes de disparar workers. Custo estimado de tokens também é apresentado."
    - "[ ] HITL: REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciência do risco e confirmar se deseja prosseguir antes de receber recomendações estratégicas naquele domínio. Recomendação de consultor jurídico parceiro é incluída."
    - "[ ] HITL: CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief é retido e o founder recebe notificação com lista dos claims não verificados, podendo aprovar release com ressalvas ou solicitar re-pesquisa."
    - "[ ] HITL: COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado como 'obtained via unclear method' é automaticamente removido e o founder é notificado. Toda coleta passa por whitelist de fontes permitidas."
    - "[ ] HITL: FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder deve revisar e aprovar. Sage pode enviar internamente (Notion, Slack privado) sem aprovação, mas envio externo é sempre L3."
---

# Analisar Teses Investimento

**Task ID:** `thesis()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Teses Investimento |
| **status** | `pending` |
| **responsible_executor** | Thesis (Thesis — O Analista de Teses) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em síntese de teses de investimento, análise de fundamentos, sinais de capital e narrativas de venture/growth. Pesquisa como investidores e analistas qualificados enxergam o mercado, setor ou empresa-alvo. Útil para preparação de pitch, due diligence reversa, análise de múltiplos e benchmarks financeiros.

## Input

- Sub-questão de tese ou análise financeira de Orion + empresa ou setor-alvo + tipo de análise (valuation, múltiplos, narrativa de VC, benchmarks de crescimento, unit economics)

## Output

- Síntese de teses: { thesis_source, investor_name_or_fund, thesis_summary, key_metrics_cited, bull_case, bear_case, source_url, publication_date }
- Benchmarks setoriais comparáveis
- Narrativa de consenso vs
- visão contrária

## Trigger

Orion roteia sub-questão classificada como 'investment_thesis' ou 'valuation' ou 'fundraising' ou 'due_diligence'. Também ativado quando founder prepara board pack ou reunião com investidores.

## Knowledge base (o que o executor consulta)

- Memos públicos de VCs (a16z, Sequoia, Bessemer, Kaszek, Monashees)
- Relatórios de equity research públicos
- Transcrições de earnings calls
- PitchBook/Crunchbase (dados públicos)
- Vector DB com teses e análises anteriores
- Benchmarks SaaS/Fintech/Marketplace por estágio

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sub-questão de tese ou análise financeira de Orion + empresa ou setor-alvo + tipo de análise (valuation, múltiplos, nar…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Síntese de teses: { thesis_source, investor_name_or_fund, thesis_summary, key_metrics_cited, bull_case, bear_case, sour…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Síntese de teses: { thesis_source, investor_name_or_fund, thesis_summary, key_metrics_cited, bull_case, bear_case, source_url, publication_date }
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vera 2 registrado
- [ ] Gate HITL respeitado: INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer op…
- [ ] Gate HITL respeitado: REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder…
- [ ] Gate HITL respeitado: CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicaçã… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciên… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — COST THRESHOLD (L3): Se estimativa de custo de tokens de uma pesquisa superar limite configurado (default: U$5 por brief) — Orion pausa e solicita aprovação ex… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Vera 2 | BLOQUEIA entrega |

## Handoff

- **to:** Prism
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
