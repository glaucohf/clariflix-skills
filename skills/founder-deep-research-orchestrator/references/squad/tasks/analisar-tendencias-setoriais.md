---
task: nexus()
responsavel: "Nexus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sub-questão de mercado extraída por Orion + critérios de suficiência (mínimo de fontes, janela temporal, geografias-alvo) + query plan com termos de busca priorizados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Array de chunks estruturados: { claim, source_url, source_date, source_credibility_score (1-5), excerpt, relevance_score }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Mínimo 8-12 fontes por sub-questão"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Relatório de gaps identificados"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion roteia sub-questão classificada como 'market' ou 'demand' ou 'tam' ou 'trends'. Também ativado por Sage quando founder clone precisa de dados de mercado atualizados para responder pergunta espe…"
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

# Analisar Tendências Setoriais

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Tendências Setoriais |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — O Analista de Mercado) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em pesquisa de mercado, tendências setoriais, tamanho de mercado (TAM/SAM/SOM), crescimento e dinâmicas de demanda. Executa web searches estruturados em fontes primárias (relatórios de consultorias, bases de dados setoriais, publicações acadêmicas, filings públicos). Retorna chunks padronizados com metadata completa de fonte.

## Input

- Sub-questão de mercado extraída por Orion + critérios de suficiência (mínimo de fontes, janela temporal, geografias-alvo) + query plan com termos de busca priorizados

## Output

- Array de chunks estruturados: { claim, source_url, source_date, source_credibility_score (1-5), excerpt, relevance_score }
- Mínimo 8-12 fontes por sub-questão
- Relatório de gaps identificados

## Trigger

Orion roteia sub-questão classificada como 'market' ou 'demand' ou 'tam' ou 'trends'. Também ativado por Sage quando founder clone precisa de dados de mercado atualizados para responder pergunta específica.

## Knowledge base (o que o executor consulta)

- Relatórios de mercado ingeridos (Gartner, McKinsey, CB Insights, Statista, IBGE, relatórios setoriais do setor do cliente)
- Vector DB com corpus histórico de pesquisas anteriores do founder
- Acesso a web search via MCP (Brave Search / Perplexity API)
- Cache de fontes validadas de alta credibilidade por setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sub-questão de mercado extraída por Orion + critérios de suficiência (mínimo de fontes, janela temporal, geografias-alv…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Array de chunks estruturados: { claim, source_url, source_date, source_credibility_score (1-5), excerpt, relevance_scor…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Array de chunks estruturados: { claim, source_url, source_date, source_credibility_score (1-5), excerpt, relevance_score }
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

- **to:** Blade
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
