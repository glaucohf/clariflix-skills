---
task: orionPipeline()
responsavel: "Orion"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Brief Estratégico Verificado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "documento estruturado entregue em Notion e Slack contendo: (1) Executive Summary de 300 palavras, (2) Findings por dimensão pesquisada (Mercado, Competição, Regulação, Tese, Tech"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "cada claim com âncora [Fonte N]), (3) Implicações Estratégicas com 3-5 recomendações acionáveis rankeadas por impacto/esforço/urgência, (4) Red Team Summary (principais contra-argumentos identificados por Vera), (5) Appendix de Fontes completo (30-60 fontes com URL, data, credibilidade score), (6) Audit Trail (log de quais workers foram ativados, quais queries foram executadas, timestamp de cada etapa), (7) Next Steps automáticos criados no ClickUp pelo Echo"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Formato disponível em três densidades: 1-pager executivo (Sage), brief completo técnico (Orion), e versão no tom do founder (Sage clone)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion é o orquestrador principal do squad. Recebe a pergunta estratégica bruta do founder, executa o protocolo de intake (classificação, decomposição breadth-first em sub-questões, estimativa de comp…"
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

# Orquestrar Pipeline do Deep Research Estratégico

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Deep Research Estratégico |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — O Estrategista Sistêmico) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orion é o orquestrador principal do squad. Recebe a pergunta estratégica bruta do founder, executa o protocolo de intake (classificação, decomposição breadth-first em sub-questões, estimativa de complexidade 1-5 e custo de tokens), roteia sub-questões para workers especializados em paralelo, monitora progresso e cobertura, recebe chunks verificados e sintetiza o Brief Estratégico final. Opera em modo workflow-engine: nunca responde diretamente ao founder sem passar pelo ciclo completo Discovery → Deep Dive → Framework. Responsável pela qualidade estrutural do output e pelo cumprimento do contrato de 100% de claims citados.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Brief Estratégico Verificado
- documento estruturado entregue em Notion e Slack contendo: (1) Executive Summary de 300 palavras, (2) Findings por dimensão pesquisada (Mercado, Competição, Regulação, Tese, Tech
- cada claim com âncora [Fonte N]), (3) Implicações Estratégicas com 3-5 recomendações acionáveis rankeadas por impacto/esforço/urgência, (4) Red Team Summary (principais contra-argumentos identificados por Vera), (5) Appendix de Fontes completo (30-60 fontes com URL, data, credibilidade score), (6) Audit Trail (log de quais workers foram ativados, quais queries foram executadas, timestamp de cada etapa), (7) Next Steps automáticos criados no ClickUp pelo Echo
- Formato disponível em três densidades: 1-pager executivo (Sage), brief completo técnico (Orion), e versão no tom do founder (Sage clone)

## Trigger

Orion é o orquestrador principal do squad. Recebe a pergunta estratégica bruta do founder, executa o protocolo de intake (classificação, decomposição breadth-first em sub-questões, estimativa de complexidade 1-5 e custo de tokens), roteia sub-questões para workers especializados em paralelo, monitora progresso e cobertura, recebe chunks verificados e sintetiza o Brief Estratégico final. Opera em modo workflow-engine: nunca responde diretamente ao founder sem passar pelo ciclo completo Discovery → Deep Dive → Framework. Responsável pela qualidade estrutural do output e pelo cumprimento do contrato de 100% de claims citados.

## Knowledge base (o que o executor consulta)

- Slack (intake de perguntas via canal #founder-intel + entrega de briefs + alertas de Blade sobre movimentos competitivos)
- Notion (Knowledge Base central
- armazenamento permanente de briefs, corpus do founder, histórico de pesquisas)
- ClickUp (criação automática de tasks de follow-up pelo Echo após cada brief
- prova de trabalho e rastreabilidade)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente
- gerencia paralelismo dos workers e estado da sessão)
- Langfuse (observabilidade OTEL
- tracing de custo por agente/token, evals de qualidade por brief, dashboard de KPIs do squad)
- Brave Search API ou Perplexity API (web search dos workers
- principal fonte de dados em tempo real)
- Vector DB
- Pinecone ou Qdrant (armazenamento e busca semântica do corpus do founder, briefs históricos e base de conhecimento)
- Gmail (ingestão de newsletters, relatórios e sinais estratégicos para alimentar workers via Echo/Chief of Staff)
- LinkedIn Sales Navigator (Blade usa para sinais de hiring e movimentos de concorrentes)
- Crunchbase / PitchBook API pública (Thesis usa para sinais de fundraising e múltiplos)
- MCP Servers (camada de integração universal
- cada ferramenta exposta como tool para os agents via protocolo MCP)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Vera 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Brief Estratégico Verificado
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
