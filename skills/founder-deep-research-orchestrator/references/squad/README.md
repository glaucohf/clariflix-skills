# Deep Research Estratégico — Founder Intelligence Squad

> Transforma qualquer pergunta estratégica em um brief 100% citado em minutos — sem fragmentação, sem alucinação, com rastreabilidade total de fontes.

**Área:** Founder Office · **TopSquad:** F4 Foresight, Risco & Research Estratégico · **Prioridade:** must‑have · **Agentes:** 10 (8 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Perguntas estratégicas críticas (movimentos de mercado, análise competitiva, due diligence de parceiros, teses de expansão) exigem hoje 2-5 dias de pesquisa manual fragmentada, sem rastreabilidade de fontes e com alto risco de alucinação. O founder toma decisões de alto impacto baseado em memória, feeling ou resumos superficiais. Mensurável por: tempo de geração do brief estratégico (48h → 25 min), cobertura de fontes por brief (média 3-5 → 30-60 fontes verificadas), taxa de claims com citação rastreável (< 30% → 100%), e custo de hora do founder poupada por decisão (8h × R$1.500/h = R$12.000 por brief substituído).

## Impacto esperado

ROI direto estimado: R$12.000 por brief substituído (8h de founder a R$1.500/h). Com 4 briefs/mês: R$48.000/mês em alavancagem de tempo do founder. Indireto: decisões mais rápidas e embasadas aceleram ciclos de M&A, parcerias e pivôs estratégicos. Para a consultoria Lendar[IA]: este squad é o produto âncora do pilar Dados & Tecnologia — serve como prova de valor imediata no Diagnóstico (encontro 4, Blueprint), justifica ticket de implementação R$40-120k e gera recorrência mensal de R$8-15k como serviço gerenciado de inteligência estratégica. NPS esperado > 90 por ser o squad que o founder usa pessoalmente toda semana.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — O Estrategista Sistêmico | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `nexus` · Nexus | Nexus — O Analista de Mercado | L2 · orquestra / decide | `analisar-tendencias-setoriais.md` |
| `blade` · Blade | Blade — O Intel de Concorrentes | L2 · orquestra / decide | `monitorar-concorrentes.md` |
| `lex` · Lex | Lex — O Radar Regulatório | L1 · worker autônomo | `analisar-riscos-regulatorios.md` |
| `thesis` · Thesis | Thesis — O Analista de Teses | L2 · orquestra / decide | `analisar-teses-investimento.md` |
| `prism` · Prism | Prism — O Scanner de Tecnologia | L2 · orquestra / decide | `analisar-tecnologiasemergentes.md` |
| `parallax` · Parallax | Parallax — O Guardião de Citações | L0 · worker determinístico | `verificar-credibilidade-fonte.md` |
| `vera` · Vera | Vera — O Crítico Adversarial | L1 · worker autônomo | `verificar-contradicoes-claims.md` |
| `sage` · Sage | Sage — O Clone do Founder | L2 · orquestra / decide | `humanizar-briefs.md` |
| `vera-2` · Vera 2 | Vera — O Crítico Adversarial | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-deep-research-orchestrator:orion` (ou instale via `npx squads add ./founder-deep-research-orchestrator`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-deep-research-orchestrator-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicação financeira direta — Orion apresenta o Research Brief ao founder para aprovação antes de disparar workers. Custo estimado de tokens também é apresentado.
- REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciência do risco e confirmar se deseja prosseguir antes de receber recomendações estratégicas naquele domínio. Recomendação de consultor jurídico parceiro é incluída.
- CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief é retido e o founder recebe notificação com lista dos claims não verificados, podendo aprovar release com ressalvas ou solicitar re-pesquisa.
- COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado como 'obtained via unclear method' é automaticamente removido e o founder é notificado. Toda coleta passa por whitelist de fontes permitidas.
- FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder deve revisar e aprovar. Sage pode enviar internamente (Notion, Slack privado) sem aprovação, mas envio externo é sempre L3.
- COST THRESHOLD (L3): Se estimativa de custo de tokens de uma pesquisa superar limite configurado (default: U$5 por brief) — Orion pausa e solicita aprovação explícita do founder antes de continuar.

## KPIs

- Tempo médio de geração de brief completo (target < 25 min vs. baseline 48h manual)
- Taxa de claims com citação verificada no brief final (target 100%)
- Número médio de fontes únicas por brief (target >= 30)
- Taxa de claims classificados como High confidence por Vera (target >= 70%)
- NPS do founder com o brief (pesquisa pós-entrega — target >= 9/10)
- Custo médio por brief em tokens (target < U$3 por pesquisa padrão)
- Taxa de briefs aprovados sem re-pesquisa solicitada pelo founder (target >= 80%)
- Número de briefs gerados por mês (proxy de utilização e alavancagem)
- Tempo poupado do founder por mês em horas (target >= 32h/mês = 4 briefs × 8h)
- Taxa de decisões estratégicas do founder com brief como input documentado (proxy de impacto real)

## Integrações

- Slack (intake de perguntas via canal #founder-intel + entrega de briefs + alertas de Blade sobre movimentos competitivos)
- Notion (Knowledge Base central — armazenamento permanente de briefs, corpus do founder, histórico de pesquisas)
- ClickUp (criação automática de tasks de follow-up pelo Echo após cada brief — prova de trabalho e rastreabilidade)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia paralelismo dos workers e estado da sessão)
- Langfuse (observabilidade OTEL — tracing de custo por agente/token, evals de qualidade por brief, dashboard de KPIs do squad)
- Brave Search API ou Perplexity API (web search dos workers — principal fonte de dados em tempo real)
- Vector DB — Pinecone ou Qdrant (armazenamento e busca semântica do corpus do founder, briefs históricos e base de conhecimento)
- Gmail (ingestão de newsletters, relatórios e sinais estratégicos para alimentar workers via Echo/Chief of Staff)
- LinkedIn Sales Navigator (Blade usa para sinais de hiring e movimentos de concorrentes)
- Crunchbase / PitchBook API pública (Thesis usa para sinais de fundraising e múltiplos)
- MCP Servers (camada de integração universal — cada ferramenta exposta como tool para os agents via protocolo MCP)

## Entregável (prova de trabalho)

Brief Estratégico Verificado — documento estruturado entregue em Notion e Slack contendo: (1) Executive Summary de 300 palavras, (2) Findings por dimensão pesquisada (Mercado, Competição, Regulação, Tese, Tech — cada claim com âncora [Fonte N]), (3) Implicações Estratégicas com 3-5 recomendações acionáveis rankeadas por impacto/esforço/urgência, (4) Red Team Summary (principais contra-argumentos identificados por Vera), (5) Appendix de Fontes completo (30-60 fontes com URL, data, credibilidade score), (6) Audit Trail (log de quais workers foram ativados, quais queries foram executadas, timestamp de cada etapa), (7) Next Steps automáticos criados no ClickUp pelo Echo. Formato disponível em três densidades: 1-pager executivo (Sage), brief completo técnico (Orion), e versão no tom do founder (Sage clone).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base mais próxima do squad: arquitetura de pesquisa multi-source com síntese, pode ser fork para os workers Nexus/Blade/Thesis com adaptação de prompts para contexto founder
- Skeptic Protocol (5 agentes, red-team/QA) — mapeia diretamente para o papel do Vera (Critic): protocolo de verificação adversarial, detecção de fraquezas lógicas e claims sem evidência — integrar como camada de verificação
- Genius Athena Strange (5 agentes, decisão sob incerteza) — complementa o squad na fase Framework: raciocínio bayesiano e decisão sob ambiguidade, útil para a seção de Implicações Estratégicas quando dados são incompletos

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F4 · TopSquad de Foresight, Risco & Research Estratégico** — Visão de futuro: cenários, riscos e pesquisa profunda para as apostas de alto risco.

- **Missão:** O squad que pensa o futuro: faz pesquisa estratégica profunda, simula cenários e wargaming de decisões grandes, e monitora riscos com alertas precoces. A munição analítica para as apostas de alto risco do founder.
- **Por que consolidar:** Os três alimentam a mesma decisão de alto risco: a pesquisa profunda dá o insumo, o wargaming simula os cenários e o risk sentinel vigia o que pode dar errado. É um pipeline único — pesquisar → simular → monitorar. Separados, a pesquisa não conversava com os cenários; unidos, viram um motor de decisão estratégica.
- **Squads irmãos:** Deep Research Estratégico, Strategic Foresight & Wargaming, Risk & Scenario Sentinel

## Estrutura

```
founder-deep-research-orchestrator/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
