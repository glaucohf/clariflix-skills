# Competitive Intelligence & Ad-Spy

> Enquanto seus concorrentes testam ângulos, você já sabe quais funcionaram — inteligência competitiva continua que converte swipe files em vantagem de aquisição antes do mercado reagir.

**Área:** Marketing · **TopSquad:** M4 Inteligência de Mercado, ICP & Concorrência · **Prioridade:** avançado · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Movimentos de concorrentes — novos angulos de copy, criativos virais, mudancas de preco, lanamentos de oferta — sao descobertos tarde demais para reagir. O time de marketing fica refem de alertas manuais, prints esporadicos de ads e gut feeling. Nao existe processo sistematico de monitoramento de bibliotecas de anuncios (Meta Ad Library, Google Ads Transparency), analise de posicionamento competitivo, ou construcao de swipe files reutilizaveis. Resultado mensuravel: (1) angulos de copy testados pelos concorrentes chegam ao time semanas depois que o mercado ja saturou, (2) mudancas de preco ou oferta de concorrentes sao detectadas pelo proprio cliente reclamando, nao pelo time, (3) budget de criativos e gasto em testes que a concorrencia ja fez e descartou. O squad monitora continuamente ads ativos, rastreia mudancas de posicionamento e preco, identifica angulos vencedores antes que se tornem commodity, e entrega swipe files prontos para reutilizacao como base de briefings de criativo — transformando inteligencia competitiva em vantagem de aquisicao mensuravel.

## Impacto esperado

Times que operam com inteligencia competitiva estruturada reduzem em 40-60% o tempo de producao de criativos (briefings baseados em angulos validados pelo mercado, nao em suposicao), elevam o CTR medio de ads em 25-35% (angulos ja provados na categoria sao mais eficientes que testes a partir do zero), e detectam ameacas competitivas em media 3-5 semanas antes do impacto em pipeline. Para uma empresa com R$50k/mes de budget em paid media, reduzir em 30% o CAC via angulos mais precisos representa R$15k/mes de eficiencia. Adicione a isso a reducao de ciclo de criativo de 3 semanas para 5 dias usando swipe files estruturados — ROI positivo em 45-60 dias de operacao. KPI primario: tempo medio de deteccao de mudanca competitiva abaixo de 48h e pelo menos 10 angulos swipe reutilizados por mes nos briefings de criativo.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Orquestrador de Inteligência Competitiva | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `falcon` · Falcon | Falcon — Scout & Competitive Mapper | L2 · orquestra / decide | `monitorar-anuncios-concorrentes.md` |
| `cipher` · Cipher | Cipher — Ad Intelligence Analyst | L2 · orquestra / decide | `classificar-angulos-narrativos.md` |
| `prism` · Prism | Prism — Positioning & Pricing Intelligence | L2 · orquestra / decide | `monitorar-mudancas-concorrenciais.md` |
| `echo` · Echo | Écho — Swipe File Curator | L1 · worker autônomo | `curar-swipe-file.md` |
| `volta` · Volta | Volta — Trend Synthesizer & Market Intelligence | L2 · orquestra / decide | `sintetizar-tendencias-mercado.md` |
| `nexus` · Nexus | Nexus — Alert Dispatcher & Briefing Generator | L3 · aprovação humana | `gerar-briefings-acionaveis.md` |
| `sigma` · Sigma | Sigma — Critic & Intelligence Verifier | L3 · aprovação humana | `verificar-inteligencia-competitiva.md` |
| `sigma-2` · Sigma 2 | Sigma — Crític & Intelligence Verifier | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-competitive-adspy:orion` (ou instale via `npx squads add ./marketing-competitive-adspy`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-competitive-adspy-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente e critérios de alerta antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação)
- Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fazem sentido para o contexto do setor antes do squad entrar em produção completa (L3, calibração crítica de taxonomia)
- Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e decidir sobre reação antes de qualquer briefing ser disparado ao time (L3, irreversível — reação de preço e decisão estratégica)
- Aprovação de Category Trend Alert — quando Volta detecta convergência de 3+ concorrentes, o CMO deve validar a hipótese estratégica antes de escalar como diretriz de campanha (L3, decisão estratégica de posicionamento)
- Revisão de Competitive Brief de reação urgente — qualquer briefing com prazo de reação de 4h (mudança de Tier 1) deve ser revisado por Head de Marketing antes de ser entregue ao time de criativo (L3, velocidade não elimina o gate humano em movimentos críticos)
- Aprovação de itens do swipe file antes de publicação no ClickUp — revisão quinzenal pelo Head de Marketing dos itens aprovados por Sigma para garantir alinhamento estratégico com prioridades de campanha do período (L1, ciclo recorrente de curadoria editorial)
- Revisão mensal do Competitive Intelligence Baseline — CMO e Head de Vendas revisam com Orion quais concorrentes devem subir ou descer de tier, se novos concorrentes devem ser adicionados, e se os critérios de alerta precisam de ajuste (L1, governança estratégica do escopo do squad)
- Quando Sigma retorna BLOCKED em gate de compliance (risco de plágio ou evidência muito fraca) — revisão humana obrigatória antes de reprocessar o item ou descartar (L3, risco legal e reputacional)

## KPIs

- Tempo médio de detecção de mudança competitiva: meta abaixo de 48h entre o evento (novo ad, mudança de preço, novo ângulo) e o alerta chegar ao CMO — baseline atual tipicamente 2-4 semanas
- Cobertura de concorrentes monitorados: % de concorrentes Tier 1 com varredura diária ativa e pelo menos 1 alerta gerado nos últimos 7 dias (meta: 100% de cobertura Tier 1, 80% Tier 2)
- Ângulos swipe reutilizados por mês: número de itens do swipe file que foram usados como base de briefing de criativo — meta de 10+ itens reutilizados por mês indicando que a biblioteca é acionável
- Taxa de false positive de Sigma: % de alertas bloqueados por Sigma por evidência fraca ou hipótese sólida — meta abaixo de 20% (indica que Cipher e Falcon estão calibrados para sinal real, não ruído)
- Intelligence Quality Score médio: média dos scores de Sigma nos itens aprovados — meta acima de 7,5/10 (garante que velocidade não sacrifica qualidade da inteligência entregue)
- CTR delta de ads usando ângulos do swipe file: comparação de CTR médio de ads briefados com base em swipe file versus ads criados sem referência competitiva — meta de +20% de CTR em ads com swipe file como base
- Pricing Change Lead Time: quanto antes a empresa soube da mudança de preço do concorrente versus quando o cliente ou SDR reportou — meta de detectar 100% das mudanças de Tier 1 antes de chegar via canal humano
- Competitive Brief to Action Rate: % de Competitive Briefs entregues por Nexus que resultaram em ação concreta do time (novo criativo, ajuste de campanha, mudança de landing page) em 7 dias — meta acima de 60%

## Integrações

- Meta Ad Library (API pública) — fonte primária de ads de concorrentes no Meta/Instagram, varredura diária por Falcon com identificadores de anunciante configurados
- Google Ads Transparency Center — monitoramento de ads no Google Search e Display de concorrentes, varredura diária por Falcon
- TikTok Creative Center — biblioteca pública de ads no TikTok, varredura semanal para concorrentes Tier 1 com presença na plataforma
- LinkedIn Ad Library — monitoramento de ads B2B de concorrentes, especialmente relevante para o setor de serviços e SaaS
- ClickUp — prova de trabalho central: swipe files estruturados, Competitive Briefs, tasks de reação com prazo e responsável, dashboard de cobertura de concorrentes e alertas pendentes
- Slack — canal #competitive-intel para alertas em tempo real de movimentos críticos, notificações de Sigma BLOCKED para revisão humana urgente, Competitive Week Review automatizado toda segunda-feira
- HubSpot CRM — campo customizado de Competitive Threat Level por deal ativo, integração de Context Cards de concorrentes nos deals em andamento, alertas de mudança de preço de concorrente para deals em negociação
- n8n — orquestração de workflows de varredura, webhooks de detecção de mudança em páginas monitoradas (Prism), automação de diff de landing pages e páginas de preço, notificações de alerta
- Apify (via MCP Docker) — scraping estruturado de landing pages e páginas de preço para Prism (diff semanal), extração de reviews de G2/Capterra por concorrente, coleta de conteúdo orgânico de blogs de concorrentes
- Semrush / Similarweb — dados de tráfego e share of voice de concorrentes, keywords em que estão investindo organicamente (Prism usa para correlacionar estratégia de conteúdo com estratégia de ads)
- Langfuse — observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de movimento competitivo, evals de qualidade de classificação de ângulos de Cipher
- Google Drive / Notion (opcional) — repositório de snapshots históricos de landing pages e Positioning Diffs para auditoria e análise de linha do tempo

## Entregável (prova de trabalho)

Competitive Intelligence Weekly Pack entregue toda segunda-feira no ClickUp e Slack contendo: (1) Competitive Activity Dashboard — Competitive Activity Score por concorrente com variação versus semana anterior e highlight dos 3 movimentos mais relevantes da semana; (2) New Winning Ads — ads de concorrentes Tier 1 com 30+ dias de veiculação identificados por Cipher com análise completa de ângulo e hipótese de performance; (3) Swipe File Weekly Update — novos itens adicionados por Echo com contexto de reutilização e sugestão de adaptação para a empresa; (4) Positioning Diff Report — mudanças detectadas por Prism em landing pages e preços de Tier 1 com destaque do que mudou literalmente; (5) Category Trend Alert (quando aplicável) — síntese de Volta sobre convergências de ângulo, formato ou oferta detectadas com hipótese estratégica; (6) Competitive Briefs da semana — movimentos que geraram briefings de reação com status de execução pelo time; (7) Intelligence Quality Metrics — Intelligence Quality Score médio da semana, false positive rate, cobertura de concorrentes monitorados. Artefato verificável: task no ClickUp fechada por Orion com todos os documentos anexados, rastreável por data e responsável.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base direta para Volta (Trend Synthesizer) e Cipher (Ad Intelligence Analyst): estrutura completa de coleta, hierarquização e síntese de inteligência estratégica de múltiplas fontes reutilizável diretamente no ciclo de Market Intelligence Report quinzenal e na construção do Competitor Creative Strategy Profile
- Skeptic Protocol (5 agentes, red-team/QA) — acelera a construcao de Sigma (Critic & Intelligence Verifier): framework de questionamento adversarial, deteccao de viés de confirmacao e validacao de evidencias ja implementados — customizar as regras de critica para o contexto de inteligencia competitiva e qualidade de swipe file
- Data Quality Guardian (5 agentes, qualidade de dados) — complementa Sigma na validação de evidências brutas de Falcon e Prism: lógica de detecção de anomalias, scoring de qualidade de dado e identificação de falsos positivos já estruturados — adaptar para o contexto de dados de bibliotecas de ads públicas com suas limitações conhecidas

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M4 · TopSquad de Inteligência de Mercado, ICP & Concorrência** — Para quem falar, contra quem competir e onde está o fit — atualizado continuamente.

- **Missão:** O squad que define a direção: espia anúncios e movimentos da concorrência, pesquisa o mercado e o product-market fit, e mantém um ICP vivo que se atualiza com os dados reais de quem converte. A inteligência que abastece os squads de execução de marketing.
- **Por que consolidar:** Os três respondem à mesma pergunta — "qual é o terreno?" — por lentes complementares: concorrência, mercado e cliente ideal. O ICP vivo se nutre da pesquisa de mercado e do que a concorrência mira. Separados, repetiam coleta; juntos, formam um único radar estratégico de marketing.
- **Squads irmãos:** Competitive Intelligence & Ad-Spy, PMF & Market Deep Research, Living ICP Profiler

## Estrutura

```
marketing-competitive-adspy/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
