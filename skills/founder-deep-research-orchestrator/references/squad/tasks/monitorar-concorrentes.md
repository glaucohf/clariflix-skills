---
task: blade()
responsavel: "Blade"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de concorrentes-alvo ou setor para mapeamento + sub-questão competitiva de Orion + janela temporal de análise + tipo de sinal (produto, preço, M&A, hiring, marketing)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mapa competitivo estruturado: { competitor, signal_type, signal_date, evidence_url, strategic_implication, confidence_level }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Ranking de ameaças por urgência"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "3-5 contra-jogadas recomendadas com lógica explícita"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion roteia sub-questão classificada como 'competitive' ou 'competitor' ou 'market_moves'. Também ativado de forma proativa pelo cron de monitoramento contínuo (diário para top-3 concorrentes, seman…"
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

# Monitorar Concorrentes

**Task ID:** `blade()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Concorrentes |
| **status** | `pending` |
| **responsible_executor** | Blade (Blade — O Intel de Concorrentes) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em inteligência competitiva. Mapeia movimentos estratégicos de concorrentes: lançamentos de produto, mudanças de pricing, contratações-chave, parcerias, captações, expansões geográficas, mudanças de posicionamento. Monitora sinais fracos (job postings, mudanças em site, registros de domínio, patentes). Gera contra-jogadas táticas baseadas nos padrões identificados.

## Input

- Lista de concorrentes-alvo ou setor para mapeamento + sub-questão competitiva de Orion + janela temporal de análise + tipo de sinal (produto, preço, M&A, hiring, marketing)

## Output

- Mapa competitivo estruturado: { competitor, signal_type, signal_date, evidence_url, strategic_implication, confidence_level }
- Ranking de ameaças por urgência
- 3-5 contra-jogadas recomendadas com lógica explícita

## Trigger

Orion roteia sub-questão classificada como 'competitive' ou 'competitor' ou 'market_moves'. Também ativado de forma proativa pelo cron de monitoramento contínuo (diário para top-3 concorrentes, semanal para tier-2).

## Knowledge base (o que o executor consulta)

- CRM com dados de contas de concorrentes
- Feeds de notícias setoriais (Google Alerts, RSS)
- LinkedIn Sales Navigator para sinais de hiring
- BuiltWith / SimilarWeb para dados de tech stack e tráfego
- Histórico de análises competitivas anteriores no Vector DB
- Crunchbase / PitchBook para sinais de fundraising

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de concorrentes-alvo ou setor para mapeamento + sub-questão competitiva de Orion + janela temporal de análise + t…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mapa competitivo estruturado: { competitor, signal_type, signal_date, evidence_url, strategic_implication, confidence_l…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mapa competitivo estruturado: { competitor, signal_type, signal_date, evidence_url, strategic_implication, confidence_level }
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

- **to:** Lex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
