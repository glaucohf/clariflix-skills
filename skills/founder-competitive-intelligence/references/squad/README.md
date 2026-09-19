# Inteligência Competitiva Contínua

> Enquanto seus concorrentes executam o próximo movimento, você já tem a contra-jogada pronta — monitoramento 24/7 com alertas preditivos que transformam inteligência em vantagem antes que a janela de reação feche.

**Área:** Founder Office · **TopSquad:** F3 Inteligência Competitiva & de Mercado · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Movimentos competitivos criticos — mudancas de preco, lancamento de produto, contratacoes estrategicas, captacao de rodada, entrada em novo mercado — sao descobertos tarde, quando a janela de reacao ja fechou. O founder depende de alertas manuais esporadicos, scans ocasionais de LinkedIn, e relatos de clientes para entender o que a concorrencia esta fazendo. Nao existe processo sistematico que monitore continuamente sinais de multiplas fontes (precificacao, hiring, produto, captacao, parcerias, conteudo estrategico), correlacione esses sinais em teses competitivas coerentes, e entregue contra-jogadas especificas com janela de acao estimada. Resultado mensuravel: (1) tempo medio de deteccao de movimento competitivo relevante e de 2-6 semanas — quando o sinal chega, o mercado ja absorbeu o impacto; (2) menos de 20% dos movimentos detectados resultam em contra-jogada concreta, por falta de briefing acionavel; (3) decisoes estrategicas do founder (preco, produto, posicionamento) sao tomadas sem inteligencia competitiva estruturada, aumentando risco de erros de posicionamento de alto custo. O squad monitora 24/7 um conjunto configurado de concorrentes diretos e adjacentes atraves de sinais publicos (paginas de preco, job postings, LinkedIn, blog/conteudo, crunchbase, Product Hunt, reviews, newsletters) e privados (feeds configurados, alertas de mencao), sintetiza os sinais em movimentos competitivos hierarquizados por impacto estrategico, e entrega para o founder um briefing semanal de estado da competicao mais alertas em tempo real para movimentos criticos — cada alerta acompanhado de uma contra-jogada especifica, janela de acao recomendada e prova de trabalho rastreavel.

## Impacto esperado

Founders e executivos com processo estruturado de inteligência competitiva reduzem em 60-70% o tempo de detecção de movimentos críticos (de semanas para horas), aumentam em 3-4x o número de contra-jogadas efetivamente executadas (de alertas sem contexto para briefings acionáveis com janela de ação), e evitam erros de posicionamento de alto custo que representam tipicamente 15-25% de churn adicional ou perda de deals em períodos de mudança competitiva intensa. Para uma empresa com ARR de R$1-5M, um movimento competitivo não detectado a tempo (mudança de preço de concorrente que erode diferenciais, lançamento de feature que obsoleta um argumento de venda, contratação de CRO que sinaliza ofensiva comercial) pode custar de R$150k a R$800k em oportunidades perdidas ou churn acelerado. O squad opera como um departamento de inteligência competitiva dedicado a custo de squad (R$5-10k/mês) versus analista sênior de estratégia (R$15-25k/mês CLT). ROI mensurável: redução de tempo de detecção abaixo de 48h, taxa de counter-play execution acima de 60% dos alertas críticos, e pelo menos 3 decisões estratégicas do founder por trimestre diretamente informadas por inteligência do squad com artefato verificável.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `atlas` · Atlas | Atlas — Strategist Orquestrador de Inteligência Competitiva | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `hawk` · Hawk | Hawk — Competitive Signal Collector | L2 · orquestra / decide | `coletar-sinais-competitivos.md` |
| `lynx` · Lynx | Lynx — Signal Intelligence Analyst | L2 · orquestra / decide | `classificar-movimentos-estrategicos.md` |
| `ares` · Ares | Áres — Wargame & Counter-Play Engine | L2 · orquestra / decide | `simular-cenarios-estrategicos.md` |
| `hermes` · Hermes | Hermes — Alert & Briefing Dispatcher | L3 · aprovação humana | `enviar-alertas-formatados.md` |
| `memo` · Memo | Memo — Board & Investor Intel Synthesizer | L2 · orquestra / decide | `sintetizar-inteligencia-competitiva.md` |
| `veritas` · Veritas | Veritás — Crític & Intelligênce Verífier | L3 · aprovação humana | `verificar-qualidade-da-evidencia.md` |
| `veritas-2` · Veritas 2 | Veritás — Critic & Intelligence Verifier | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-competitive-intelligence:atlas` (ou instale via `npx squads add ./founder-competitive-intelligence`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-competitive-intelligence-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento por concorrente, critérios de alerta por categoria de movimento e janela de reação por tipo antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação e a sensibilidade dos alertas)
- Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atual e as restrições reais do negócio capturados por Atlas para alimentar o Wargame Engine — sem calibração, as contra-jogadas de Ares são genéricas (L3, input crítico que define qualidade das recomendações)
- Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirma se as classificações de movimento fazem sentido para o contexto real do mercado e calibra thresholds de scoring de Lynx (L3, calibração crítica antes de produção)
- Aprovação de Competitive Flash antes de Counter-Play urgente (score >= 9 em Tier 1) — quando Hermes recebe sinal CRÍTICO aprovado por Veritás, o founder deve confirmar ciência e decisão antes de qualquer ação irreversível ser executada (L3, irreversível por natureza — resposta competitiva errada pode ser pior que nenhuma resposta)
- Revisão mensal do Competitive Landscape Report — founder revisa com Atlas o cenário competitivo do mês, valida os cenários de wargame de Ares para os próximos 90 dias, aprova os playbooks de resposta como diretriz estratégica e ajusta os critérios de alerta do Competitive Map se necessário (L3, governança estratégica mensal obrigatória)
- Aprovação pré-distribuição de Board Intelligence Pack e Decision Intelligence Brief de Memo — qualquer documento de Memo deve ser revisado e aprovado pelo founder antes de chegar à board ou investidores (L3, irreversível — documento compartilhado externamente não tem recall)
- Calibracao trimestral de scoring de Lynx — founder revisa junto com Atlas e Veritas os falsos positivos e falsos negativos dos ultimos 90 dias, ajusta os pesos de scoring por categoria e tier, e valida se os Movement Profiles de concorrentes Tier 1 estao acurados (L1, ciclo de melhoria continua da qualidade do squad)
- Quando Veritas retorna BLOCKED em gate de rastreabilidade ou hipótese inflatada — revisão obrigatória do founder antes de reprocessamento ou descarte do item, com log da razão do bloqueio para calibração futura (L3, risco de decisão estratégica baseada em inteligência de baixa qualidade)

## KPIs

- Tempo médio de detecção de movimento competitivo: meta abaixo de 48h entre o evento (mudança de preço publicada, job posting relevante, rodada anunciada) e o Competitive Flash Card chegar ao founder — baseline típico sem o squad e 2-6 semanas
- Counter-Play Execution Rate: porcentagem de Competitive Flash Alerts CRÍTICOS e ALTOS que resultaram em ação concreta do founder nos 7 dias subsequentes — meta acima de 60% (indica que os briefings são acionáveis e não apenas informativos)
- Intelligence Credibility Score medio de Veritas: media dos scores dos Counter-Play Briefs aprovados no periodo — meta acima de 7.5/10 com breakdown por dimensao (evidencia, hipotese, alternativas, completude, rastreabilidade)
- False Positive Rate de alertas: porcentagem de Competitive Flash Alerts que o founder classificou como 'não relevante ou não acionável' no feedback pós-revisão — meta abaixo de 15% (indica calibração sólida de Lynx e Veritas)
- Cobertura de concorrentes Tier 1: porcentagem de concorrentes Tier 1 com varredura diária ativa e pelo menos 1 sinal processado por Lynx nos últimos 7 dias — meta de 100% (nenhum ponto cego em Tier 1)
- Decisões estratégicas do founder com suporte de intel competitiva: número de decisões de alto impacto (preço, produto, parceria) no trimestre que tiveram Decision Intelligence Brief de Memo como input — meta de 100% das decisões do quadrante estratégico
- Board Pack Intelligence Coverage: porcentagem de afirmacoes competitivas em Board Intelligence Packs com footnote rastreavel aprovado por Veritas — meta de 100% (zero afirmacoes sem evidencia em documentos externos)
- Sequence Pattern Detection Rate: quantos movimentos competitivos maiores (funding, lançamento, ofensiva comercial) foram detectados antes do anúncio oficial via Sequence Pattern Alert de Lynx — meta de detectar 70% dos movimentos maiores de Tier 1 em fase preparatória (antes do anúncio público)
- Latência de Competitive Flash: tempo entre Veritas aprovar Counter-Play Brief e Hermes entregar o Flash Card ao founder — meta abaixo de 30 minutos (SLA de entrega pos-aprovação)

## Integrações

- LinkedIn (scraping via Apify Actor) — monitoramento diário de Company Pages dos concorrentes (headcount, job postings), perfis de fundadores e C-level para sinais de estratégia pública, detecção de mudanças de descrição de empresa que sinalizam reposicionamento
- Crunchbase (API ou scraping) — monitoramento de rodadas de investimento, aquisições, novas parcerias e mudanças de liderança dos concorrentes Tier 1 e Tier 2
- Product Hunt — alertas de novos launches de concorrentes ou de startups emergentes no mesmo espaço competitivo
- G2 / Capterra / Reclame Aqui (scraping via Apify) — monitoramento de novas reviews de concorrentes com extração de sentimento e temas críticos (pontos fracos exploráveis)
- ClickUp — prova de trabalho central: tasks de alertas com prioridade e janela de ação, Counter-Play Briefs anexados, Competitive Intelligence Baseline como documento de referência, dashboard de cobertura de concorrentes e SLA de detecção
- Slack — canal #competitive-intel para Competitive Flash Cards em tempo real, Competitive Intel Weekly Briefing toda sexta-feira, notificações de gate BLOCKED de Veritas para revisão humana urgente
- Notion — repositório dos Competitive Landscape Reports mensais, Board Intelligence Packs, Movement Profiles atualizados e Corpus do Founder estruturado como knowledge base do squad
- n8n — orquestração de workflows de varredura, webhooks de detecção de mudança em páginas monitoradas (diff de páginas de preço), agendamento de crons por frequência e tier, roteamento de sinais entre agentes
- Apify (via MCP Docker) — scraping estruturado de páginas de preço (diff automático), job postings de LinkedIn, reviews de G2/Capterra, conteúdo de blogs de concorrentes, perfis públicos de fundadores
- Langfuse — observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de sinal (SLA de detecção vs. alerta), evals de acurácia de classificação de Lynx e de qualidade de hipóteses de Ares, custo por alerta gerado
- HubSpot CRM (opcional) — campo Competitive Threat Level nos deals ativos, context cards de concorrentes em oportunidades em negociação, alerta automático para SDRs/AEs quando Hermes detecta mudança de preço de concorrente com deals em andamento
- EXÁ (via MCP Docker) — web search para contexto adicional de sinais de menor confiança, pesquisa de background de concorrentes emergentes detectados por Hawk, busca de cobertura de mídia de eventos competitivos relevantes
- Google Alerts / RSS Aggregator — camada complementar de monitoramento de menções públicas de concorrentes em mídia, redução de latência para eventos de alta visibilidade (funding announcements, lançamentos com cobertura de imprensa)

## Entregável (prova de trabalho)

Competitive Intelligence Weekly Pack entregue toda sexta-feira no ClickUp (task fechada por Atlas com todos os artefatos anexados) e no canal Slack #competitive-intel, contendo: (1) Competitive Activity Dashboard — Competitive Activity Index por concorrente Tier 1 e Tier 2 com variacao versus semana anterior e top 3 movimentos da semana com scoring de Lynx; (2) Counter-Play Briefs da semana — todos os FLASH alerts gerados com hipotese estrategica de Ares, contra-jogadas recomendadas e status de execucao pelo founder; (3) Movement Profiles Update — o que mudou nos perfis estrategicos de cada Tier 1 (preco atual, headcount delta, foco de produto aparente, saude financeira aparente); (4) Sequence Pattern Alerts (quando aplicavel) — padroes de multiplos sinais de mesmo concorrente sugerindo movimento maior em preparacao; (5) Intelligence Quality Metrics da semana — Intelligence Credibility Score medio, false positive rate, cobertura de Tier 1, latencia media de deteccao, custo por alerta (via Langfuse). ADICIONAL MENSAL: Competitive Landscape Report com Wargame dos proximos 90 dias e Strategic Opportunity Map. ADICIONAL SOB DEMANDA: Board Intelligence Pack e Decision Intelligence Brief. Artefato verificavel: task no ClickUp com numero sequencial, timestamp de entrega, assinatura digital de Atlas e link para todos os documentos — rastreavel por semana, por concorrente e por categoria de movimento.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athenaeum (11 agentes, inteligência estratégica) — base direta para a espinha dorsal do squad: estrutura completa de coleta hierarquizada, síntese de múltiplas fontes e produção de briefings estratégicos reutilizável diretamente na arquitetura de Lynx (Signal Intelligence Analyst) e Atlas (Strategist Orquestrador), especialmente o pipeline de ingestão de fontes heterogêneas e o framework de priorização de sinais por relevância estratégica
- Genius Athena Strange (5 agentes, decisão sob incerteza) — acelera a construção do Wargame Engine (Ares): framework de raciocínio sob incerteza, consideração de hipóteses alternativas e estruturação de cenários competitivos com probabilidades já implementados — customizar para o contexto de inteligência competitiva B2B com Corpus do Founder como input primário
- Skeptic Protocol (5 agentes, red-team/QA) — acelera a construcao de Veritas (Critic & Intelligence Verifier): framework de questionamento adversarial, deteccao de hipoteses inflatadas e validacao de nivel de confianca de claims ja estruturados — adaptar as regras de critica para o contexto de intelligence onde falsa certeza e mais danosa que incerteza declarada

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F3 · TopSquad de Inteligência Competitiva & de Mercado** — Onde estão as oportunidades, os concorrentes e as tecnologias que importam.

- **Missão:** O radar externo do founder: monitora concorrentes continuamente, dimensiona mercados e detecta oportunidades, e mantém um tech radar com decisões de build-vs-buy. A inteligência de "onde jogar" e "com o quê".
- **Por que consolidar:** Os três escaneiam o ambiente externo por lentes que se cruzam: concorrente, mercado e tecnologia. O tech radar informa o build-vs-buy que depende do tamanho do mercado que depende do que o concorrente faz. Separados, repetiam a varredura externa; juntos, um radar estratégico único.
- **Squads irmãos:** Inteligência Competitiva Contínua, Market Sizing & Opportunity Scout, Tech Radar & Build-vs-Buy

## Estrutura

```
founder-competitive-intelligence/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
