# Squad Programmatic SEO + GEO/AEO

> Sua marca indexada em todos os motores — de busca e de IA — antes que o concorrente perceba que o jogo mudou.

**Área:** Marketing · **TopSquad:** M3 Conteúdo & Criativo · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Trafego orgânico estagna porque equipes de conteúdo não conseguem produzir em escala suficiente para competir por milhares de termos de cauda longa, E a marca fica invisível nas respostas de IA (ChatGPT, Perplexity, Google AI Overviews) porque o conteúdo existente não foi estruturado para ser citado por LLMs. Resultado: demanda que migra para search generativo simplesmente some do radar — não aparece no Google Analytics, não tem atribuição, não é monitorada. Mensurável por: páginas indexadas e ranqueando, volume de citações da marca em motores de IA (GEO Score), tráfego orgânico total e tráfego assistido por IA (dark traffic que vira atribuível).

## Impacto esperado

Produção programática com IA permite publicar 200-2.000 páginas SEO otimizadas por mês vs 10-30 páginas de uma equipe editorial humana — 20-100x de alavancagem de volume sem adição de headcount editorial. Cada página ranqueando na primeira página do Google gera em média 500-2.000 visitas orgânicas/mês (benchmark SemRush 2024 para conteúdo B2B de nicho). GEO/AEO aumenta probabilidade de citação em AI Overviews e ChatGPT em 3-5x quando o conteúdo é estruturado com dados, fontes e entidades verificáveis. Para um negócio B2B com ticket médio de R$15k e taxa de conversão orgânico-para-lead de 2%: cada 10.000 visitas orgânicas/mês adicionais = 200 leads = 40-60 reuniões qualificadas ao mês. ROI estimado: stack de conteúdo programático com SEO + GEO paga-se em 90-180 dias; após isso, tráfego e citações são ativos permanentes que valorizam com o tempo (ao contrário de tráfego pago que zera no momento que você para de pagar). Redução de 70% do custo de produção de conteúdo vs agência editorial tradicional.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `argo` · Argo | Argo — O Cartógrafo de Visibilidade | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `lexus` · Lexus | Lexus — O Estrategista de Palavras | L1 · worker autônomo | `mapear-palavras-chave.md` |
| `orion` · Orion | Órion — O Minerador de Dados | L1 · worker autônomo | `minerar-dados-brutos.md` |
| `scribe` · Scribe | Scribe — O Motor de Conteúdo | L2 · orquestra / decide | `otimizar-estrutura-h1.md` |
| `beacon` · Beacon | Beacon — O Otimizador de IA Search | L1 · worker autônomo | `otimizar-conteudo-para-ia.md` |
| `atlas` · Atlas | Atlas — O Publicador Inteligente | L3 · aprovação humana | `publicar-conteudo-tecnico.md` |
| `sonar` · Sonar | Sonar — O Vigia de Visibilidade | L1 · worker autônomo | `monitorar-posicoes-keywords.md` |
| `lumen` · Lumen | Lumen — O Guardião da Qualidade Editorial | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-programmatic-seo-geo:argo` (ou instale via `npx squads add ./marketing-programmatic-seo-geo`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-programmatic-seo-geo-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, paginas de alta competicao definidas no onboarding) bloqueia e notifica o gestor de conteudo com preview completo para aprovacao antes de publicar um caracter.
- Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamente) e escalado para o editor humano com o checklist completo de reprovações e sugestões específicas de correção.
- Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bloqueado e sinalizado para o time de conteúdo verificar manualmente antes de qualquer publicação — zero tolerância para afirmação sem rastreabilidade.
- Batch de publicação programática acima de 50 páginas: qualquer batch acima do threshold configurado (default: 50 páginas/batch) requer aprovação do gestor de SEO antes do Atlas iniciar a publicação — para proteger o crawl budget e a reputação do domínio.
- Queda abrupta de visibilidade detectada pelo Sonar: queda de >30% em tráfego orgânico em 7 dias ou desaparecimento de cluster inteiro das SERPs = alerta imediato ao time de SEO para investigação manual antes de qualquer ação automática do squad — pode ser update algorítmico que requer análise humana.
- Novos templates programáticos: sempre que Lexus ou Argo identificam um novo tipo de página programática não mapeada anteriormente, o template precisa de aprovação humana antes de entrar em produção em escala — para garantir alinhamento estratégico e qualidade do formato.
- Decisões de redirects e exclusão de conteúdo: qualquer ação que envolva deletar, redirecionar ou desindexar páginas existentes (especialmente com tráfego ou backlinks) é sempre humana — reversibilidade zero para ações de remoção de conteúdo já indexado.

## KPIs

- Páginas indexadas e ranqueando: total de páginas publicadas pelo squad que estão indexadas no Google, com breakdown por posição (top 3, top 10, top 100) — meta crescimento de 20-30% ao mês no primeiro trimestre
- GEO Score mensal: % dos 50 termos prioritários do cliente em que a marca é citada em pelo menos 1 motor de IA (ChatGPT, Perplexity, Google AI Overviews) — baseline no onboarding, meta +5 pontos percentuais por mês
- Tráfego orgânico total (sessões/mês): crescimento mês-a-mês de tráfego via busca orgânica com atribuição por cluster temático — meta +15-25% ao mês nos primeiros 6 meses
- Tráfego assistido por IA (dark traffic atribuível): visitas diretas ou de referência que aumentam em correlação com o aumento do GEO Score — indicador indireto de visibilidade em search generativo
- Volume de produção verificada: páginas publicadas/mês com score Lumen >= threshold — meta de produção: 50-200 páginas programáticas + 8-16 artigos editoriais por mês dependendo do tier
- Taxa de aprovação do Lumen no primeiro ciclo: meta >65% para produção programática, >75% para artigos editoriais — indica qualidade dos templates e calibragem dos agentes de produção
- Tempo de ciclo de produção: da aprovação do backlog item pelo Argo ao conteúdo publicado e submetido ao GSC — meta <4 horas para páginas programáticas, <24 horas para artigos editoriais
- Taxa de indexação pós-publicação: % das páginas publicadas pelo Atlas que são indexadas pelo Google em 7 dias — meta >80%; abaixo disso aciona investigação de crawl budget ou qualidade de conteúdo
- Taxa de task success por agente no Langfuse: gate produção = 95%; qualquer agente abaixo do threshold aciona alerta automático para revisão
- CPL orgânico (Custo por Lead orgânico): leads gerados por tráfego orgânico / custo mensal do squad — meta: custo de aquisição via orgânico 70% menor que via tráfego pago equivalente após 6 meses de operação
- Featured Snippets e AI Overviews conquistados: número de posições zero e citações em AI Overviews ganhas no período — indicador direto da eficácia do Beacon e da estratégia GEO

## Integrações

- CMS: WordPress via REST API (principal para clientes brasileiros B2B), Webflow CMS API, Contentful API, Ghost API — Atlas conecta diretamente via MCP ou REST
- SEO e pesquisa de keywords: SemRush Enterprise AIO (posições, volume, dificuldade, backlinks, AI Growth Agent nativo), Frase.io (SEO scoring e briefing de conteúdo com NLP), Ahrefs API (backlinks e historical rank tracking)
- Google Search Console API: monitoramento de indexação, impressões, cliques, CTR, posição média por URL e query — fonte primária de dados de performance
- Google PageSpeed Insights API e CrUX API: monitoramento de Core Web Vitals em batch para todo o portfólio publicado
- Monitoramento de citações em IA: ChatGPT API (queries sistemáticas para rastrear citações), Perplexity API (monitoramento de menções), Google AI Overviews via Search Console e monitoramento manual estruturado
- Enriquecimento de dados programáticos: Clay (waterfall de dados de empresas, pessoas e localizações para páginas programáticas B2B), APIs de dados abertos (IBGE, dados.gov.br), APIs setoriais específicas do segmento do cliente
- Gestão de tarefas e prova de trabalho: ClickUp (artefatos verificáveis por batch — keyword map, dataset, conteúdo aprovado, log de publicação, relatório de indexação e performance) conectado ao Argo via MCP ou webhook
- Orquestração multi-agente: LangGraph (controle de estado do pipeline de conteúdo, grafos de decisão por batch) ou Claude Agent SDK
- Observabilidade e evals: Langfuse (traces OTEL por agente, quality gates dev 70% / staging 85% / prod 95% task success, dashboard de performance do squad com métricas específicas de conteúdo)
- No-code complementar: n8n para automações de integração (conecta webhooks do GSC, triggers do CMS, notificações de HITL, relatórios automáticos) sem código custom — pilar comum de agências agênticas 2026
- Similarity e plagiarism check: Copyscape API ou Originality.ai para verificacao de unicidade de conteudo antes da publicacao
- Notificações internas: Slack ou email do gestor de conteúdo para alertas de HITL, oportunidades críticas detectadas pelo Sonar e relatórios semanais do squad

## Entregável (prova de trabalho)

Portfolio de conteúdo SEO+GEO verificado, publicado e monitorado de forma contínua: (1) Universo de keywords e entidade map (Lexus) — documento vivo no ClickUp com backlog priorizado, atualizado mensalmente; (2) Datasets programáticos estruturados (Orion) — base de dados verificada com score de qualidade por registro e log de fontes, rastreável no ClickUp; (3) Conteúdo aprovado por página (Scribe + Beacon) — Markdown completo com SEO score, GEO score, checklist do Lumen aprovado e versionamento no ClickUp; (4) Log de publicação imutável por batch (Atlas) — URL publicada, timestamp, internal links inseridos, schema markup aplicado, status de indexação no GSC, screenshot do preview; (5) Dashboard de visibilidade semanal (Sonar) — posições por keyword, GEO Score por motor de IA, oportunidades detectadas, alertas de queda, backlinks novos/perdidos, Core Web Vitals; (6) Relatório mensal de ROI — crescimento de tráfego orgânico, evolução do GEO Score, páginas ranqueando em top 10, leads atribuídos ao orgânico vs baseline pré-implantação. Todo o pipeline e auditável por design: cada página publicada tem agente responsável em cada etapa, timestamp, veredicto do Lumen, trace no Langfuse e artefato verificável no ClickUp. O gestor de conteúdo opera os gates L3 e vê o status completo de cada batch em um único painel.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athênaeum (11 agentes, inteligência estratégica) — base direta para o Lexus e o Orion: os agentes de pesquisa de mercado, síntese de inteligência e análise de dados públicos do Athênaeum podem ser adaptados para o ciclo de keyword research avançado, construção do entidade map e coleta de dados programáticos — economizando semanas de desenvolvimento da camada de inteligência do squad.
- Skeptic Protocol (5 agentes, red-team/QA) — base para o Lumen: o protocolo de crítica adversarial com checklist multi-ponto pode ser reutilizado como framework de validação das 10 dimensões do crític de conteúdo, especialmente o verificador de factualidade e o detector de conteúdo thin — o coração da confiabilidade editorial do squad.
- Data Quality Guardian (5 agentes, qualidade de dados) — base para o Orion: a estrutura de validação, scor­ing de completude e detecção de anomalias em datasets pode ser diretamente adaptada para o sistema de qualida­de dos datasets programáticos do Orion, garantindo que cada registro tem os campos obriga­tórios, fontes verificá­veis e unicidade antes de alimentar o Scribe.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M3 · TopSquad de Conteúdo & Criativo (UGC + SEO/GEO)** — Fábrica de criativos e conteúdo que ranqueia em buscadores e em LLMs.

- **Missão:** A máquina de produção de ativos: gera criativos UGC em escala para mídia paga/social e conteúdo programático otimizado para SEO tradicional e para GEO/AEO (ser citado por LLMs e respostas de IA). Um só motor de conteúdo, dois canais de distribuição.
- **Por que consolidar:** UGC e SEO programático são a mesma capacidade — gerar conteúdo de marca em escala — apontada a destinos diferentes (feed pago vs. busca/LLM). Compartilham a voz de marca, o briefing e o critic de qualidade. Um único motor evita duplicar a governança de conteúdo.
- **Squads irmãos:** Creative UGC Factory, Programmatic SEO + GEO/AEO

## Estrutura

```
marketing-programmatic-seo-geo/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
