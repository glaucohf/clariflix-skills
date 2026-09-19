# Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

> Nenhuma aposta grande sai sem estressar premissas contra futuros plausíveis e adversários autônomos — o founder decide com o mapa completo, não com o feeling.

**Área:** Founder Office · **TopSquad:** F4 Foresight, Risco & Research Estratégico · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Decisões de alta aposta (alocação de capital, entrada em mercado, parceria estratégica, pivô de produto) são tomadas sem simular como concorrentes vão reagir, sem mapear cenários de futuro alternativos e sem estressar as premissas que sustentam a tese. O resultado: surpresas evitáveis corroem ROI, capital é alocado em apostas que não sobreviveriam a um red-team básico, e o founder descobre os furos da tese após comprometer recursos. Mensurável por: número de cenários plausíveis simulados por decisão (baseline 0 → target >= 3), % de premissas críticas estressadas antes da alocação de capital (baseline < 20% → target 100%), tempo de ciclo de wargaming (baseline 2 semanas com consultor externo → target 4 horas com squad), e custo por simulação (baseline R$15.000-50.000 em consultoria → target R$300-800 por rodada).

## Impacto esperado

ROI direto: uma única aposta de R$500k protegida por wargaming que evita erro estratégico retorna 625x o custo mensal do squad. Estimativa conservadora: 2 decisões/mês de R$50k+ cada — prevenir retrabalho em 30% delas gera R$30.000/mês em capital protegido. Para a consultoria Lendar[IA]: este squad é o produto premium do pilar Estratégia da Founder Office — diferencial competitivo máximo pois simula adversários autônomos (não apenas SWOT estático). Serve como âncora de ticket alto (R$25-60k implementação) e recorrência mensal de R$12-25k. Posicionamento: 'o único sistema que joga contra você antes do mercado jogar'.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `atlas` · Atlas | Atlas — O Estrategista de Decisões | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `cassandra` · Cassandra | Cassandra — A Arquiteta de Futuros | L2 · orquestra / decide | `mapear-espaco-de-futuros.md` |
| `brutus` · Brutus | Brutus — O Adversário Autônomo | L2 · orquestra / decide | `simular-reacoes-adversarias.md` |
| `chisel` · Chisel | Chisel — O Destruidor de Premissas | L1 · worker autônomo | `destruir-premissas.md` |
| `pythia` · Pythia | Pythia — A Analista de Sinais Fracos | L2 · orquestra / decide | `coletar-sinais-fracos.md` |
| `memo` · Memo | Memo — O Redator de Board Packs | L3 · aprovação humana | `sintetizar-wargaming-report.md` |
| `tripwire` · Tripwire | Tripwire — O Guardião de Alertas | L2 · orquestra / decide | `monitorar-indicadores-de-alerta.md` |
| `ajax` · Ajax | Ajax — O Crítico de Guerra | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-strategic-foresight-wargaming:atlas` (ou instale via `npx squads add ./founder-strategic-foresight-wargaming`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-strategic-foresight-wargaming-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificação de stakes, estimativa de custo de tokens). Para decisões classificadas como Alto (R$100k-500k) ou Crítico (R$500k+), aprovação explícita do founder é obrigatória antes de disparar workers. Inclui confirmação do escopo, dos concorrentes a simular e do nível de profundidade desejado.
- PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e founder recebe notificação urgente com evidências contrárias. O founder deve decidir: (a) revisar a tese antes de prosseguir, (b) validar a premissa com dado adicional, ou (c) aceitar o risco explicitamente e autorizar o prosseguimento. Sem aprovação explícita, Atlas não gera recomendação de GO.
- PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloqueia automaticamente a recomendação de GO e escalona para o founder. O relatório apresenta: narrativa do caminho de falha, premissas que o geram e opções de mitigação. O founder deve responder com ação concreta (mitigar, aceitar, desistir) antes de qualquer recomendação final.
- BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento gerado vai primeiro para Notion como draft. Somente após founder marcar como aprovado o envio é permitido. Este gate é inviolável e não pode ser desabilitado.
- WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades financeiras ou decisões internas), o output é marcado como confidencial e apresentado ao founder antes de ser incluído em qualquer documento compartilhável. Dados de origem não-verificada são explicitamente rotulados.
- DECISÃO DE MONITORAMENTO CONTÍNUO (L2): Após wargaming concluído, Atlas apresenta lista de tripwires sugeridos para aprovação do founder antes de ativar Tripwire. O founder pode ajustar thresholds, remover indicadores ou adicionar novos. Apenas após aprovação o monitoramento é ativado para evitar notificações não-desejadas.

## KPIs

- Número de cenários plausíveis simulados por decisão (target >= 3, baseline 0)
- % de premissas críticas estressadas antes da alocação de capital (target 100%, baseline < 20%)
- Tempo de ciclo de wargaming completo — intake até Wargaming Report entregue (target < 4 horas vs. baseline 2 semanas com consultor)
- % de Pre-Mortems com caminho de falha identificado (proxy de qualidade do red-team — target >= 60% de wargamings encontram pelo menos 1 risco não-mapeado previamente)
- Taxa de premissas classificadas como Frágil ou Inválida que o founder não havia considerado (proxy de valor gerado — target >= 2 por decisão)
- Acurácia de cenários: % de cenários materializados dentro do range previsto após 6 meses (meta de calibração bayesiana — target >= 65% para cenário Base)
- Número de wargamings por mês (proxy de utilização e embedding no processo decisório — target >= 4/mês)
- Custo por wargaming em tokens (target < R$800 por rodada completa)
- NPS do founder com o Wargaming Report (pesquisa pós-entrega — target >= 9/10)
- Número de decisões com tripwires ativos em monitoramento (proxy de valor acumulado — meta: 80% das decisões estratégicas do founder com tripwire configurado)

## Integrações

- Slack (intake de decisões via canal #founder-strategy + entrega do Wargaming Report + alertas urgentes do Tripwire + notificações de HITL gates)
- Notion (Knowledge Base central — armazenamento permanente de Wargaming Reports, Árvores de Premissas, Scenario Matrices, histórico de decisões com outcomes documentados)
- ClickUp (criação automática de tasks de tripwire e follow-up pós-decisão — prova de trabalho e rastreabilidade de cada aposta tomada)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia paralelismo de Cassandra/Brutus/Chisel e estado do wargaming entre sessões)
- Langfuse (observabilidade OTEL — tracing de custo por agente/token, evals de qualidade de cenários, dashboard de KPIs do squad, latência por fase do pipeline)
- Brave Search API ou Perplexity API (web search de Pythia e Chisel — sinais de mercado, evidências contrárias a premissas, dados de concorrentes em tempo real)
- Vector DB — Pinecone ou Qdrant (armazenamento e busca semântica de wargamings históricos, perfis de concorrentes, premissas e seus outcomes, corpus do founder)
- LinkedIn Sales Navigator (Pythia usa para sinais de hiring e movimentos estratégicos de concorrentes)
- Crunchbase / PitchBook API pública (Brutus e Pythia usam para sinais de fundraising, aquisições e capacidades financeiras de adversários)
- Google Alerts / RSS Feeds setoriais (Pythia usa para monitoramento contínuo de sinais fracos do setor e de concorrentes específicos)
- MCP Servers (camada de integração universal — cada ferramenta exposta como tool para os agents via protocolo MCP)
- APIs financeiras e de métricas do cliente (Tripwire usa para monitoramento de indicadores de early-warning pós-decisão — integração com dashboards internos via MCP)

## Entregável (prova de trabalho)

Wargaming Report Completo — documento estratégico entregue em Notion e Slack contendo: (1) Decision Brief com contexto, stakes, Árvore de Premissas completa e classificação de cada premissa (Sólida/Frágil/Inválida); (2) Scenario Matrix com 3+ cenários estruturados — narrativa, driving forces, early-warning indicators, probabilidades bayesianas e impacto quantificado por cenário; (3) Adversarial Playbook por concorrente — reações simuladas em 30/90/180 dias, probabilidades, vulnerabilidades exploradas e contra-jogadas do founder; (4) Pre-Mortem Report — narrativa causal da falha mais plausível em 12 meses com probabilidade estimada; (5) Decision Recommendation — GO/NO-GO/PIVOT com condições explícitas, premissas a monitorar e ações de mitigação para riscos identificados; (6) Tripwire Configuration — lista de early-warning indicators configurados para monitoramento pós-decisão com thresholds de alerta; (7) Audit Trail completo (qual worker gerou cada insight, fontes utilizadas, timestamp de cada fase, custo de tokens). Disponível em três formatos: Wargaming Report completo técnico (Atlas), Executive One-Pager para decisão rápida, e Board Memo formatado (Memo — após aprovação L3).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Genius Athena Strange (5 agentes, decisão sob incerteza) — alinhamento direto: raciocínio bayesiano e decisão sob ambiguidade mapeiam para Cassandra (cenários com probabilidades) e Chisel (stress-testing de premissas). Pode ser usado como base para os prompts de construção de cenários e análise de sensibilidade
- Skeptic Protocol (5 agentes, red-team/QA) — mapeia diretamente para Ajax (Crítico): protocolo de verificação adversarial e red-team estruturado pode ser integrado como camada de Pre-Mortem e consistência cruzada dos outputs dos workers
- Athenaeum (11 agentes, inteligência estratégica) — complementa o squad na fase de Deep Dive: a arquitetura de pesquisa multi-source com síntese do Athenaeum pode alimentar Cassandra com dados de mercado verificados e Pythia com fontes de sinais setoriais

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F4 · TopSquad de Foresight, Risco & Research Estratégico** — Visão de futuro: cenários, riscos e pesquisa profunda para as apostas de alto risco.

- **Missão:** O squad que pensa o futuro: faz pesquisa estratégica profunda, simula cenários e wargaming de decisões grandes, e monitora riscos com alertas precoces. A munição analítica para as apostas de alto risco do founder.
- **Por que consolidar:** Os três alimentam a mesma decisão de alto risco: a pesquisa profunda dá o insumo, o wargaming simula os cenários e o risk sentinel vigia o que pode dar errado. É um pipeline único — pesquisar → simular → monitorar. Separados, a pesquisa não conversava com os cenários; unidos, viram um motor de decisão estratégica.
- **Squads irmãos:** Deep Research Estratégico, Strategic Foresight & Wargaming, Risk & Scenario Sentinel

## Estrutura

```
founder-strategic-foresight-wargaming/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
