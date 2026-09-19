---
task: prism()
responsavel: "Prism"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sub-questão tecnológica de Orion + domínio técnico de interesse + contexto de uso (qual problema de negócio a tecnologia deve resolver) + critérios de avaliação (custo, maturidade, integração, vendor lock-in)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tech landscape report: { technology_name, maturity_level, top_vendors, open_source_alternatives, use_case_examples, integration_complexity, cost_estimate_range, recommendation (Build/Buy/Partner/Wait), source_urls }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Matriz comparativa de soluções"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion classifica sub-questão como 'technology' ou 'build_vs_buy' ou 'tech_stack' ou 'ai_tools'. Também ativado quando founder avalia adoção de nova ferramenta de IA ou parceria com empresa de tecnolo…"
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

# Analisar TecnologiasEmergentes

**Task ID:** `prism()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar TecnologiasEmergentes |
| **status** | `pending` |
| **responsible_executor** | Prism (Prism — O Scanner de Tecnologia) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em análise de landscape tecnológico, soluções emergentes e avaliação de build vs. buy vs. partner. Mapeia o estado da arte de uma tecnologia específica, principais players, maturidade (TRL), casos de uso reais e implicações para o roadmap do cliente. Alimenta decisões de arquitetura técnica e parcerias estratégicas de tecnologia.

## Input

- Sub-questão tecnológica de Orion + domínio técnico de interesse + contexto de uso (qual problema de negócio a tecnologia deve resolver) + critérios de avaliação (custo, maturidade, integração, vendor lock-in)

## Output

- Tech landscape report: { technology_name, maturity_level, top_vendors, open_source_alternatives, use_case_examples, integration_complexity, cost_estimate_range, recommendation (Build/Buy/Partner/Wait), source_urls }
- Matriz comparativa de soluções

## Trigger

Orion classifica sub-questão como 'technology' ou 'build_vs_buy' ou 'tech_stack' ou 'ai_tools'. Também ativado quando founder avalia adoção de nova ferramenta de IA ou parceria com empresa de tecnologia.

## Knowledge base (o que o executor consulta)

- Repositórios de tech intelligence (Product Hunt, GitHub trending, Hacker News, arxiv para AI/ML)
- G2/Capterra para comparativos de ferramentas
- Documentação técnica de APIs e SDKs relevantes
- Histórico de avaliações de tecnologia do cliente
- Stack atual do cliente (para análise de compatibilidade)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sub-questão tecnológica de Orion + domínio técnico de interesse + contexto de uso (qual problema de negócio a tecnologi…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tech landscape report: { technology_name, maturity_level, top_vendors, open_source_alternatives, use_case_examples, int…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tech landscape report: { technology_name, maturity_level, top_vendors, open_source_alternatives, use_case_examples, integration_complexity, cost_estimate_range…
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

- **to:** Parallax
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
