---
task: lex()
responsavel: "Lex"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sub-questão com dimensão regulatória identificada por Orion + setor de atuação do cliente + geografias envolvidas + tipo de operação (M&A, novo produto, expansão, parceria, captação)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mapa de riscos regulatórios: { regulation_name, applicability_score, risk_level (Alto/Médio/Baixo), key_requirement, source_url, recommended_action }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Flag explícita quando risco é Alto ou Crítico"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "requer revisão de especialista jurídico humano antes de ação"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion classifica sub-questão como 'regulatory' ou 'legal' ou 'compliance'. Ativado automaticamente quando pergunta envolve: expansão internacional, novo produto financeiro, dados de usuários, M&A ou…"
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

# Analisar Riscos Regulatórios

**Task ID:** `lex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Riscos Regulatórios |
| **status** | `pending` |
| **responsible_executor** | Lex (Lex — O Radar Regulatório) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em mapeamento de riscos regulatórios, compliance e implicações legais para decisões estratégicas. Verifica se a pergunta estratégica tem dimensão regulatória (LGPD, BACEN, ANVISA, CADE, CVM, regulações internacionais). Não dá opinião legal — entrega análise de risco com referências a textos normativos, precedentes e especialistas externos quando necessário (HITL gate).

## Input

- Sub-questão com dimensão regulatória identificada por Orion + setor de atuação do cliente + geografias envolvidas + tipo de operação (M&A, novo produto, expansão, parceria, captação)

## Output

- Mapa de riscos regulatórios: { regulation_name, applicability_score, risk_level (Alto/Médio/Baixo), key_requirement, source_url, recommended_action }
- Flag explícita quando risco é Alto ou Crítico
- requer revisão de especialista jurídico humano antes de ação

## Trigger

Orion classifica sub-questão como 'regulatory' ou 'legal' ou 'compliance'. Ativado automaticamente quando pergunta envolve: expansão internacional, novo produto financeiro, dados de usuários, M&A ou captação.

## Knowledge base (o que o executor consulta)

- Base de textos normativos relevantes ao setor do cliente (indexados no Vector DB)
- Feeds de publicações regulatórias (DOU, BACEN, ANPD, CVM)
- Histórico de análises regulatórias do cliente
- Rede de especialistas jurídicos parceiros (contatos para escalada HITL)
- Jurisprudência e precedentes administrativos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sub-questão com dimensão regulatória identificada por Orion + setor de atuação do cliente + geografias envolvidas + tip…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mapa de riscos regulatórios: { regulation_name, applicability_score, risk_level (Alto/Médio/Baixo), key_requirement, so…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mapa de riscos regulatórios: { regulation_name, applicability_score, risk_level (Alto/Médio/Baixo), key_requirement, source_url, recommended_action }
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

- **to:** Thesis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
