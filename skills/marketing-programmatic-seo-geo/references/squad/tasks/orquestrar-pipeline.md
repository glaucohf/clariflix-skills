---
task: argoPipeline()
responsavel: "Argo"
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
    descricao: "Portfolio de conteúdo SEO+GEO verificado, publicado e monitorado de forma contínua: (1) Universo de keywords e entidade map (Lexus)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "documento vivo no ClickUp com backlog priorizado, atualizado mensalmente"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Datasets programáticos estruturados (Orion)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "base de dados verificada com score de qualidade por registro e log de fontes, rastreável no ClickUp"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Conteúdo aprovado por página (Scribe + Beacon)"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Markdown completo com SEO score, GEO score, checklist do Lumen aprovado e versionamento no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Decompõe a meta de visibilidade orgânica e em IA (ex: X novas páginas indexadas/mês, Y citações em motores de IA) em batches de produção distribuídos aos workers na sequência correta: Lexus mapeia ke…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Lumen antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, paginas de alta competicao definidas no onboarding) bloqueia e notifica o gestor de conteudo com preview completo para aprovacao antes de publicar um caracter."
    - "[ ] HITL: Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamente) e escalado para o editor humano com o checklist completo de reprovações e sugestões específicas de correção."
    - "[ ] HITL: Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bloqueado e sinalizado para o time de conteúdo verificar manualmente antes de qualquer publicação — zero tolerância para afirmação sem rastreabilidade."
    - "[ ] HITL: Batch de publicação programática acima de 50 páginas: qualquer batch acima do threshold configurado (default: 50 páginas/batch) requer aprovação do gestor de SEO antes do Atlas iniciar a publicação — para proteger o crawl budget e a reputação do domínio."
    - "[ ] HITL: Queda abrupta de visibilidade detectada pelo Sonar: queda de >30% em tráfego orgânico em 7 dias ou desaparecimento de cluster inteiro das SERPs = alerta imediato ao time de SEO para investigação manual antes de qualquer ação automática do squad — pode ser update algorítmico que requer análise humana."
---

# Orquestrar Pipeline do Programmatic SEO + GEO/AEO

**Task ID:** `argoPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Programmatic SEO + GEO/AEO

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Programmatic SEO + GEO/AEO |
| **status** | `pending` |
| **responsible_executor** | Argo (Argo — O Cartógrafo de Visibilidade) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Decompõe a meta de visibilidade orgânica e em IA (ex: X novas páginas indexadas/mês, Y citações em motores de IA) em batches de produção distribuídos aos workers na sequência correta: Lexus mapeia keywords -> Orion coleta dados -> Scribe produz conteúdo -> Beacon otimiza para IA -> Lumen valida -> Atlas publica -> Sonar monitora e retroalimenta. Mantém o estado de cada batch de conteúdo no pipeline — da ideia ao published+indexado. Prioriza produção com base em volume x competitividade da keyword, potencial de citação em IA e urgência de oportunidades detectadas pelo Sonar. Consolida todos os artefatos em pacotes de conteúdo rastreados no ClickUp. Monitora os quality gates no Langfuse e escalona para HITL sempre que um gate falha ou uma decisão de publicação de alto impacto está pendente. Opera em L2: executa o ciclo completo de orquestração autonomamente, mas gates L3 bloqueiam o fluxo para aprovação humana antes de publicação de páginas estratégicas ou ações com impacto em SEO técnico do domínio.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Portfolio de conteúdo SEO+GEO verificado, publicado e monitorado de forma contínua: (1) Universo de keywords e entidade map (Lexus)
- documento vivo no ClickUp com backlog priorizado, atualizado mensalmente
- (2) Datasets programáticos estruturados (Orion)
- base de dados verificada com score de qualidade por registro e log de fontes, rastreável no ClickUp
- (3) Conteúdo aprovado por página (Scribe + Beacon)
- Markdown completo com SEO score, GEO score, checklist do Lumen aprovado e versionamento no ClickUp
- (4) Log de publicação imutável por batch (Atlas)
- URL publicada, timestamp, internal links inseridos, schema markup aplicado, status de indexação no GSC, screenshot do preview
- (5) Dashboard de visibilidade semanal (Sonar)
- posições por keyword, GEO Score por motor de IA, oportunidades detectadas, alertas de queda, backlinks novos/perdidos, Core Web Vitals
- (6) Relatório mensal de ROI
- crescimento de tráfego orgânico, evolução do GEO Score, páginas ranqueando em top 10, leads atribuídos ao orgânico vs baseline pré-implantação
- Todo o pipeline e auditável por design: cada página publicada tem agente responsável em cada etapa, timestamp, veredicto do Lumen, trace no Langfuse e artefato verificável no ClickUp
- O gestor de conteúdo opera os gates L3 e vê o status completo de cada batch em um único painel

## Trigger

Decompõe a meta de visibilidade orgânica e em IA (ex: X novas páginas indexadas/mês, Y citações em motores de IA) em batches de produção distribuídos aos workers na sequência correta: Lexus mapeia keywords -> Orion coleta dados -> Scribe produz conteúdo -> Beacon otimiza para IA -> Lumen valida -> Atlas publica -> Sonar monitora e retroalimenta. Mantém o estado de cada batch de conteúdo no pipeline — da ideia ao published+indexado. Prioriza produção com base em volume x competitividade da keyword, potencial de citação em IA e urgência de oportunidades detectadas pelo Sonar. Consolida todos os artefatos em pacotes de conteúdo rastreados no ClickUp. Monitora os quality gates no Langfuse e escalona para HITL sempre que um gate falha ou uma decisão de publicação de alto impacto está pendente. Opera em L2: executa o ciclo completo de orquestração autonomamente, mas gates L3 bloqueiam o fluxo para aprovação humana antes de publicação de páginas estratégicas ou ações com impacto em SEO técnico do domínio.

## Knowledge base (o que o executor consulta)

- CMS: WordPress via REST API (principal para clientes brasileiros B2B), Webflow CMS API, Contentful API, Ghost API
- Atlas conecta diretamente via MCP ou REST
- SEO e pesquisa de keywords: SemRush Enterprise AIO (posições, volume, dificuldade, backlinks, AI Growth Agent nativo), Frase.io (SEO scoring e briefing de conteúdo com NLP), Ahrefs API (backlinks e historical rank tracking)
- Google Search Console API: monitoramento de indexação, impressões, cliques, CTR, posição média por URL e query
- fonte primária de dados de performance
- Google PageSpeed Insights API e CrUX API: monitoramento de Core Web Vitals em batch para todo o portfólio publicado
- Monitoramento de citações em IA: ChatGPT API (queries sistemáticas para rastrear citações), Perplexity API (monitoramento de menções), Google AI Overviews via Search Console e monitoramento manual estruturado
- Enriquecimento de dados programáticos: Clay (waterfall de dados de empresas, pessoas e localizações para páginas programáticas B2B), APIs de dados abertos (IBGE, dados.gov.br), APIs setoriais específicas do segmento do cliente
- Gestão de tarefas e prova de trabalho: ClickUp (artefatos verificáveis por batch
- keyword map, dataset, conteúdo aprovado, log de publicação, relatório de indexação e performance) conectado ao Argo via MCP ou webhook
- Orquestração multi-agente: LangGraph (controle de estado do pipeline de conteúdo, grafos de decisão por batch) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (traces OTEL por agente, quality gates dev 70% / staging 85% / prod 95% task success, dashboard de performance do squad com métricas específicas de conteúdo)
- No-code complementar: n8n para automações de integração (conecta webhooks do GSC, triggers do CMS, notificações de HITL, relatórios automáticos) sem código custom
- pilar comum de agências agênticas 2026
- Similarity e plagiarism check: Copyscape API ou Originality.ai para verificacao de unicidade de conteudo antes da publicacao
- Notificações internas: Slack ou email do gestor de conteúdo para alertas de HITL, oportunidades críticas detectadas pelo Sonar e relatórios semanais do squad

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Lumen antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Portfolio de conteúdo SEO+GEO verificado, publicado e monitorado de forma contínua: (1) Universo de keywords e entidade map (Lexus)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Lumen registrado
- [ ] Gate HITL respeitado: Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, pag…
- [ ] Gate HITL respeitado: Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamen…
- [ ] Gate HITL respeitado: Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bl…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, paginas de alta competi… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamente) e escalado para… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bloqueado e sinalizado… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Batch de publicação programática acima de 50 páginas: qualquer batch acima do threshold configurado (default: 50 páginas/batch) requer aprovação do gestor de S… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Queda abrupta de visibilidade detectada pelo Sonar: queda de >30% em tráfego orgânico em 7 dias ou desaparecimento de cluster inteiro das SERPs = alerta imedia… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Novos templates programáticos: sempre que Lexus ou Argo identificam um novo tipo de página programática não mapeada anteriormente, o template precisa de aprova… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Decisões de redirects e exclusão de conteúdo: qualquer ação que envolva deletar, redirecionar ou desindexar páginas existentes (especialmente com tráfego ou ba… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Lumen | BLOQUEIA entrega |

## Handoff

- **to:** Lexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
