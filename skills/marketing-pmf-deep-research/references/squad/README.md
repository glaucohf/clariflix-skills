# PMF & Market Deep Research Squad

> Pare de adivinhar o mercado: valide dor, tamanho e ângulo antes de gastar um real em mídia.

**Área:** Marketing · **TopSquad:** M4 Inteligência de Mercado, ICP & Concorrência · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Decisões de posicionamento e oferta são tomadas no achismo, sem evidência de dor real ou tamanho de mercado mensurável, resultando em campanhas que não convertem e verba desperdiçada. O squad produz evidências quantitativas e qualitativas de PMF — hipóteses validadas/refutadas, mapa de concorrentes, personas sintéticas testadas e PMF score — antes que qualquer real de mídia seja investido.

## Impacto esperado

Redução de 40-60% no custo de validação vs. rodadas de mídia exploratória (benchmark: R$15-80k em média queimada por posicionamento errado). Meta: >= 3 hipóteses validadas por ciclo de 10 dias, PMF score >= 7/10 antes de escalar budget, redução de CPA em 25-35% nas primeiras campanhas pós-validação.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Estrategista de Mercado | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `marco` · Marco | Marco — Research Lead | L2 · orquestra / decide | `pesquisar-tendencias-industriais.md` |
| `iris` · Iris | Íris — ICP Profiler | L1 · worker autônomo | `gerar-scoring-de-fit.md` |
| `vesper` · Vesper | Vesper — Signal Sensor | L2 · orquestra / decide | `monitorar-sinais-de-dor.md` |
| `nyx` · Nyx | Nyx — Synthetic Persona Engine | L2 · orquestra / decide | `simular-entrevistas-sinteticas.md` |
| `atlas` · Atlas | Atlas — Competitive Intelligence Analyst | L2 · orquestra / decide | `analisar-concorrentes-diretos-indiretos.md` |
| `brutus` · Brutus | Brutus — Research Crític & Réd-Team | L1 · worker autônomo | `questionar-premissas.md` |
| `vega` · Vega | Vega — PMF Synthesizer & Storyteller | L2 · orquestra / decide | `sintetizar-pmf-documento.md` |
| `brutus-2` · Brutus 2 | Brutus — Research Crític & Réd-Team | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-pmf-deep-research:orion` (ou instale via `npx squads add ./marketing-pmf-deep-research`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-pmf-deep-research-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias de pesquisa na direção errada
- Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx simular entrevistas
- Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva documentada
- Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução (Copywriter, Media Buying) — gate L3 porque decisões de mídia são financeiramente irreversíveis
- Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser incluído no documento final

## KPIs

- Número de hipóteses validadas ou refutadas por ciclo de pesquisa (meta: >= 3 por ciclo de 10 dias)
- PMF Score final (escala 1-10, meta: >= 7 antes de escalar budget de mídia)
- Custo de validação por hipótese vs. custo equivalente de mídia exploratória (meta: redução de 40-60%)
- Taxa de aprovação do Brutus por artefato (meta: >= 70% claims com evidência Alta/Média sem retrabalho)
- Tempo médio ciclo completo Discovery -> Framework (meta: <= 10 dias úteis)
- Taxa de adoção de ângulos de posicionamento pelo squad de Copywriter/Media Buying (meta: >= 80% dos ângulos entregues testados)
- Redução de CPA nas campanhas pós-validação vs. campanhas pré-squad (meta: -25-35% em 60 dias)
- NPS do cliente sobre qualidade do PMF Framework Document (meta: >= 8/10)

## Integrações

- HubSpot / Salesforce — leitura de dados de CRM para ICP profiling (Iris)
- Clay — waterfall enrichment de 100+ fontes para enriquecimento de ICP e sinais de intent
- Apollo.io — prospecting e enriquecimento de contatos para validacao de ICP
- SEMrush / SimilarWeb — share of voice, keywords e tráfego de concorrentes (Marco, Atlas)
- Meta Ad Library / Google Ads Transparency — análise de criativos e copy de concorrentes (Atlas)
- G2 / Capterra / Trustpilot — reviews públicos para signal sensing e competitive intel (Vesper, Atlas)
- LinkedIn — sinais de hiring, conteúdo e movimentos estratégicos de concorrentes (Vesper, Atlas)
- Reddit / forums do nicho — captura de linguagem de dor organica (Vesper)
- Notion / Google Docs — entrega do PMF Framework Document e Persona Cards ao cliente
- ClickUp — registro de tasks, prova de trabalho e rastreamento de artefatos entregues por ciclo
- Langfuse — observabilidade OTEL, evals e quality gates dos agentes (dev 70% / staging 85% / prod 95%)
- Slack / WhatsApp Business — notificações de HITL ao cliente/board para aprovações críticas

## Entregável (prova de trabalho)

PMF Framework Document (PDF/Notion, 10-15 páginas executivas) contendo: PMF Score (1-10) com breakdown, ICP Master Profile com 3-5 clusters rankeados, top-3 ângulos de posicionamento com justificativa de evidência, Persona Cards (3-5), Competitive Matrix, Angle Test Kit (3-5 headlines/hooks prontos por canal) e Roadmap de Validação (30 dias). Artefato registrado e versionado no ClickUp como prova de trabalho auditável.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 ag, inteligência estratégica) — base para a camada de síntese e framework de pesquisa multi-fonte do Marco e Vega
- Genius Athena Strange (5 ag, decisão sob incerteza) — base para o protocolo de red-team do Brutus e para o processo de scoring de hipóteses sob incerteza do Orion
- deep-research (harness de pesquisa multi-fonte com fan-out, verificação adversarial e relatório citado) — acelera a trilha de pesquisa do Marco com busca paralela e verificação de claims automatizada

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M4 · TopSquad de Inteligência de Mercado, ICP & Concorrência** — Para quem falar, contra quem competir e onde está o fit — atualizado continuamente.

- **Missão:** O squad que define a direção: espia anúncios e movimentos da concorrência, pesquisa o mercado e o product-market fit, e mantém um ICP vivo que se atualiza com os dados reais de quem converte. A inteligência que abastece os squads de execução de marketing.
- **Por que consolidar:** Os três respondem à mesma pergunta — "qual é o terreno?" — por lentes complementares: concorrência, mercado e cliente ideal. O ICP vivo se nutre da pesquisa de mercado e do que a concorrência mira. Separados, repetiam coleta; juntos, formam um único radar estratégico de marketing.
- **Squads irmãos:** Competitive Intelligence & Ad-Spy, PMF & Market Deep Research, Living ICP Profiler

## Estrutura

```
marketing-pmf-deep-research/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
