# Living ICP Profiler

> Seu ICP nunca mais vai envelhecer: perfil vivo, versionado e alimentado por 100+ fontes para o time sempre saber para quem vender.

**Área:** Marketing · **TopSquad:** M4 Inteligência de Mercado, ICP & Concorrência · **Prioridade:** must‑have · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

ICPs estáticos em slides se tornam obsoletos em semanas. O time de vendas atira em listas genéricas, queima budget com leads fora de fit e não sabe identificar os sinais de compra que diferenciam um prospect quente de um curioso. Resultado mensurável: % de leads dentro do ICP abaixo de 40%, fit score médio inconsistente entre SDRs e taxa de conversão por segmento invisível. O squad mantém um perfil de cliente ideal vivo e versionado via gateways de dados e enriquecimento em cascata de 100+ fontes, gerando um ICP Score dinâmico que atualiza automaticamente conforme novos dados entram.

## Impacto esperado

Empresas que operam com ICP dinâmico reportam aumento de 35-60% no % de leads dentro do fit, redução de 40% no CAC por segmento e aumento de 2-3x na taxa de conversão Leads -> Oportunidades qualificadas. Para uma empresa com R$50k/mês em budget de aquisição, reduzir desperdício de 30% para 10% libera R$10k/mês — ROI do squad em 2-4 meses. KPI primário: ICP Fit Score médio da pipeline acima de 7.5/10 em 90 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `maestro` · Maestro | Maestro — Orquestrador de ICP | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `atlas` · Atlas | Atlas — ICP Research Agent | L2 · orquestra / decide | `construir-personas-calibradas.md` |
| `iris` · Iris | Íris — Enrichment Cascade Agent | L2 · orquestra / decide | `enriquecer-dados-lead.md` |
| `zara` · Zara | Zara — Signal & Intent Sensor | L2 · orquestra / decide | `monitorar-sinais-de-compra.md` |
| `nox` · Nox | Nóx — PMF Deep Research Agent | L2 · orquestra / decide | `calibrar-icp-com-dados-de-mercado.md` |
| `rex` · Rex | Rex — ICP Scoring & Versioning Agent | L1 · worker autônomo | `calcular-icp-score.md` |
| `vera` · Vera | Vera — Critic & Data Quality Verifier | L3 · aprovação humana | `verificar-qualidade-de-dados.md` |
| `vera-2` · Vera 2 | Vera — Critic & Data Quality Verifier | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-living-icp-profiler:maestro` (ou instale via `npx squads add ./marketing-living-icp-profiler`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-living-icp-profiler-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3)
- Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3)
- Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)
- Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3)
- Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1)
- Aprovação de integração com nova fonte de dados de enriquecimento que implica custo adicional — qualquer nova ferramenta paga requer validação financeira (L3)

## KPIs

- ICP Fit Score medio da pipeline: meta > 7.5/10 em 90 dias (baseline atual a medir no Discovery)
- % de leads dentro do ICP: meta > 65% em 90 dias (de baseline típico de ~35-40%)
- Cobertura de enriquecimento: >= 85% dos campos prioritários preenchidos para leads tier 1
- Taxa de conversão por segmento de fit: rastreada por quartil de score (Q1-Q4) para validar poder preditivo do modelo
- Tempo de detecção de sinal até alerta no CRM: meta < 24h para Hot Accounts
- Freshness do ICP: versão do ICP com < 30 dias de idade (nunca mais um ICP de slide com 6 meses)
- Data Quality Score (Vera): >= 85/100 em cada publicação de nova versão
- Redução de CAC por segmento ICP: meta de 20% em 6 meses via melhora de targeting

## Integrações

- HubSpot CRM — campo customizado ICP Fit Score por lead/empresa, propriedades de segmento e sinais, webhook de novo lead para trigger de enriquecimento
- Clay — waterfall enrichment primary engine, ICP custom tables, intent signals agregados de 100+ fontes
- Apollo.io — prospecting consolidado, enriquecimento de contatos, dados de seniority e titulo
- Cognism — enriquecimento complementar com foco em compliance GDPR para mercados internacionais
- ClickUp — prova de trabalho: task automática por ciclo de enriquecimento, dashboard de ICP Score médio da pipeline, alertas de desvio de ICP
- LinkedIn Sales Navigator — sinais de atividade de contatos, mudanças de emprego, company updates
- Bombora / 6sense — intent data B2B por tópico e segmento
- n8n — orquestração de workflows de enriquecimento e notificações (complemento no-code)
- Langfuse — observabilidade OTEL de todos os agents, quality gates (dev 70% / staging 85% / prod 95% task success)
- Slack / Email — alertas de Hot Accounts (intent score > 70) e notificações de nova versão de ICP publicada

## Entregável (prova de trabalho)

ICP Profile vivo e versionado publicado no CRM (HubSpot/Salesforce) com: (1) ICP Fit Score automático por lead (0-10 com breakdown por dimensão), (2) Segmentos priorizados com PMF Score e TAM estimado, (3) Mapa de 40+ atributos por segmento com confidence score, (4) Signal Feed diário de Hot Accounts com intent score, (5) Dashboard de fit score médio da pipeline no ClickUp, (6) Changelog de versões do ICP com rastreabilidade completa, (7) Relatório mensal de desvio de ICP (quando o perfil real dos leads está divergindo do ideal).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base para o módulo de deepresearch de Atlas e Nox: estrutura de coleta e síntese de inteligência de mercado reutilizável diretamente no ciclo de Discovery e PMF research
- Data Quality Guardian (5 agentes, qualidade de dados) — acelera a construção de Vera (Critic): lógica de validação, detecção de inconsistências e scoring de qualidade já implementados, basta customizar as regras para atributos de ICP
- Synthetic Intelligence Factory (fábrica de agentes especializados) — acelera a criação das synthetic personas no Atlas: estrutura de geração e calibração de personas já existe, customizar para o contexto de ICP B2B

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M4 · TopSquad de Inteligência de Mercado, ICP & Concorrência** — Para quem falar, contra quem competir e onde está o fit — atualizado continuamente.

- **Missão:** O squad que define a direção: espia anúncios e movimentos da concorrência, pesquisa o mercado e o product-market fit, e mantém um ICP vivo que se atualiza com os dados reais de quem converte. A inteligência que abastece os squads de execução de marketing.
- **Por que consolidar:** Os três respondem à mesma pergunta — "qual é o terreno?" — por lentes complementares: concorrência, mercado e cliente ideal. O ICP vivo se nutre da pesquisa de mercado e do que a concorrência mira. Separados, repetiam coleta; juntos, formam um único radar estratégico de marketing.
- **Squads irmãos:** Competitive Intelligence & Ad-Spy, PMF & Market Deep Research, Living ICP Profiler

## Estrutura

```
marketing-living-icp-profiler/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
