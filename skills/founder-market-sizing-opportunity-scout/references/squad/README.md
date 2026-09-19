# Market Sizing & Opportunity Scout — Founder Strategy Squad

> De hunch para tese fundamentada: TAM/SAM/SOM com fontes rastreáveis e oportunidades de expansão dimensionadas em menos de 45 minutos — sem consultoria, sem planilha manual, sem alucinação.

**Área:** Founder Office · **TopSquad:** F3 Inteligência Competitiva & de Mercado · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Avaliar tamanho de mercado e identificar novas oportunidades de expansão é hoje um processo que consome 3-7 dias de trabalho analítico, produz outputs inconsistentes entre rounds e raramente cita fontes verificáveis — resultando em teses frágeis que não resistem ao escrutínio de investidores ou do próprio board. O founder faz sizing no feeling ou paga consultoria R$30-80k para um slide de TAM que fica desatualizado em 6 meses. Mensurável por: tempo de geração de tese de sizing (72h → 45 min), número de oportunidades dimensionadas com fontes por trimestre (2-3 → 12-15), taxa de claims de mercado com citação verificável (< 20% → 100%), e custo por tese (R$15.000 consultoria → R$200 squad).

## Impacto esperado

ROI direto: substituição de 1 projeto de sizing de consultoria/trimestre poupa R$30-80k. Com utilização de 4 teses/mês: R$60k-120k/ano em economia direta, além de velocidade 96x maior para capturar janelas de oportunidade antes de concorrentes. Para a consultoria Lendar[IA]: este squad ancora o pilar Dados & Tecnologia do Diagnóstico — é o 'aha moment' do encontro 4 (Blueprint) quando o founder vê em tempo real o sizing do próprio mercado sendo feito ao vivo. Justifica ticket de implementação R$35-90k e gera recorrência mensal de R$6-12k como serviço de inteligência de mercado contínua. NPS esperado > 92 por resolver dor real com prova imediata no próprio Diagnóstico.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `atlas` · Atlas | Atlas — O Cartógrafo Estratégico | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `cosmos` · Cosmos | Cosmos — O Analista Top-Down | L2 · orquestra / decide | `analisar-dados-macro.md` |
| `praxis` · Praxis | Praxis — O Engenheiro Bottom-Up | L2 · orquestra / decide | `contar-unidades-economicas.md` |
| `radar` · Radar | Radar — O Leitor de Concorrentes | L2 · orquestra / decide | `estimar-mercado-competitivo.md` |
| `scout` · Scout | Scout — O Caçador de Oportunidades | L2 · orquestra / decide | `cacar-oportunidadesadjacentes.md` |
| `faro` · Faro | Faro — O Guardião de Barreiras | L1 · worker autônomo | `mapear-barreiras-regulatorias.md` |
| `citadel` · Citadel | Citadel — O Arquivista de Fontes | L0 · worker determinístico | `classificar-credibilidade-fontes.md` |
| `axiom` · Axiom | Axiom — O Verificador de Sizing | L1 · worker autônomo | `verificar-convergencia-e-sanity-check.md` |
| `axiom-2` · Axiom 2 | Axiom — O Verificador de Sizing | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-market-sizing-opportunity-scout:atlas` (ou instale via `npx squads add ./founder-market-sizing-opportunity-scout`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-market-sizing-opportunity-scout-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado de tokens é apresentado ao founder para aprovação explícita. Perguntas que envolvam sizing de mercados para M&A, captação ou due diligence de parceiros têm este gate obrigatório e não podem ser puladas.
- REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, autorização CADE) — o Market Opportunity Report é retido e o founder recebe alerta com a barreira descrita. O SOM do relatório final é ajustado para refletir a barreira e marcado como 'pendente de validação jurídica' até que especialista humano confirme a análise. Inclui recomendação de consultor jurídico parceiro.
- CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolverem o gap — o relatório é enviado ao founder com flag explícita de 'sizing com alta incerteza metodológica'. O founder decide se aceita o intervalo de incerteza ou solicita pesquisa adicional paga (escopo ampliado).
- INVESTMENT MEMO / PITCH USE (L3): Quando o founder sinaliza que vai usar o Market Opportunity Report em pitch a investidores, board pack ou material de captação — Axiom executa uma rodada adicional de verificação adversarial de nível máximo (100% de claims quantitativos devem ter fonte credibilidade >= 4) e o founder deve revisar e assinar o relatório antes do envio externo. Nexar (Founder Clone) não escreve versão de pitch sem este gate.
- COST THRESHOLD (L3): Se a estimativa de custo de tokens de uma pesquisa superar o limite configurado (default: U$8 por análise de sizing completo) — Atlas pausa, apresenta o breakdown de custo por worker e solicita aprovação explícita antes de continuar.
- NEW MARKET ENTRY RECOMMENDATION (L3): Quando Scout ranquear uma oportunidade com recomendação de ação imediata (ex: janela de entrada fechando em < 3 meses, sinal de concorrente se posicionando) — o alerta é escalado para o founder com nível de urgência explícito antes de qualquer automação de follow-up no ClickUp.

## KPIs

- Tempo médio de geração de Market Opportunity Report completo (target < 45 min vs. baseline 72h manual)
- Taxa de convergência entre métodos no relatório final — % de relatórios onde desvio entre top-down e bottom-up < 40% (target >= 80%)
- Taxa de claims quantitativos com citação verificada credibilidade >= 3 (target 100%)
- Número médio de fontes únicas por relatório de sizing (target >= 20 fontes)
- Número de oportunidades de expansão dimensionadas com fontes por trimestre (target 12-15 vs. baseline 2-3)
- NPS do founder com o relatório — pesquisa pós-entrega (target >= 9/10)
- Taxa de relatórios aprovados sem solicitação de re-pesquisa (target >= 75%)
- Custo médio por relatório em tokens (target < U$6 por sizing completo com triangulação)
- Taxa de teses de sizing usadas em decisão real pelo founder (proxy de impacto — documentado no ClickUp)
- Economia estimada vs. consultoria externa por trimestre (target R$30k-80k substituídos)

## Integrações

- Slack (intake de perguntas via canal #market-sizing + entrega de relatórios + alertas de Scout sobre oportunidades emergentes + notificações de gate HITL)
- Notion (Knowledge Base central — armazenamento permanente de Market Opportunity Reports, histórico de sizings, corpus de benchmarks e teses de expansão do cliente)
- ClickUp (criação automática de tasks de validação e follow-up após cada relatório — prova de trabalho rastreável, conectado a story de estratégia)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente — gerencia paralelismo dos workers e estado do pipeline de sizing)
- Langfuse (observabilidade OTEL — tracing de custo por worker/token, evals de qualidade por relatório, dashboard de KPIs do squad, alerta de desvio de convergência)
- Brave Search API / EXA API (web search dos workers — fonte primária de dados em tempo real para Cosmos, Praxis, Radar e Scout)
- Vector DB — Pinecone ou Qdrant (armazenamento semântico de benchmarks setoriais, sizings históricos, corpus de teses e relatórios de mercado do cliente)
- Google Trends API (Scout usa para sinais de demanda crescente e identificação de timing de oportunidades)
- Crunchbase / PitchBook API pública (Radar e Scout usam para proxy de revenue de concorrentes e sinais de funding por setor)
- SimilarWeb / SEMrush API (Radar usa para proxy de receita de concorrentes digitais via tráfego e keywords)
- IBGE API / Dados Abertos Receita Federal (Praxis usa para contagem de CNPJs por CNAE como base do bottom-up)
- MCP Servers (camada de integração universal — cada fonte de dados exposta como tool para os agents via protocolo MCP)

## Entregável (prova de trabalho)

Market Opportunity Report — documento estruturado entregue em Notion e Slack contendo: (1) Executive Summary com TAM/SAM/SOM finais em reais/dólares com intervalo de confiança, (2) Sizing Waterfall top-down com cada etapa do cálculo e fonte inline [Fonte N], (3) Sizing bottom-up com tabela de sensibilidade (3 cenários), (4) Competitive Sizing com receitas dos principais players e TAM implícito, (5) Triangulação dos três métodos com análise de convergência ou divergência explicada, (6) Mapa de Oportunidades de Expansão rankeadas por potencial x esforço x timing com sizing individual de cada oportunidade, (7) Tese de Entrada recomendada com lógica explícita e 3 hipóteses de execução, (8) Barrier Map com SOM adjustment justificado, (9) Appendix de Fontes completo (20+ fontes com URL, data, credibilidade score), (10) Audit Trail (metodologia, queries, workers ativados, timestamp). Disponível em duas densidades: 1-pager executivo para board/investidores e relatório analítico completo. Tasks de follow-up criadas automaticamente no ClickUp com responsáveis e prazos.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — arquitetura de pesquisa multi-source com síntese e rastreabilidade de fontes mapeia diretamente para os workers Cosmos, Radar e Scout; fork dos prompts de pesquisa com adaptação para metodologia de sizing (top-down, bottom-up, triangulação) acelera em 60% o desenvolvimento dos workers
- Skeptic Protocol (5 agentes, red-team/QA) — protocolo de verificação adversarial e detecção de fraquezas lógicas mapeia diretamente para o papel do Axiom: integrar como camada de red-team de SOM e convergência metodológica, especialmente a lógica de 'tenta refutar o claim principal antes de liberar'
- Genius Athena Strange (5 agentes, decisão sob incerteza) — raciocínio bayesiano e estruturação de decisão sob ambiguidade complementa o squad na síntese final: útil para o Mapa de Oportunidades quando dados são incompletos e o founder precisa rankear oportunidades com informação parcial, especialmente para novos mercados sem dados históricos

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F3 · TopSquad de Inteligência Competitiva & de Mercado** — Onde estão as oportunidades, os concorrentes e as tecnologias que importam.

- **Missão:** O radar externo do founder: monitora concorrentes continuamente, dimensiona mercados e detecta oportunidades, e mantém um tech radar com decisões de build-vs-buy. A inteligência de "onde jogar" e "com o quê".
- **Por que consolidar:** Os três escaneiam o ambiente externo por lentes que se cruzam: concorrente, mercado e tecnologia. O tech radar informa o build-vs-buy que depende do tamanho do mercado que depende do que o concorrente faz. Separados, repetiam a varredura externa; juntos, um radar estratégico único.
- **Squads irmãos:** Inteligência Competitiva Contínua, Market Sizing & Opportunity Scout, Tech Radar & Build-vs-Buy

## Estrutura

```
founder-market-sizing-opportunity-scout/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
