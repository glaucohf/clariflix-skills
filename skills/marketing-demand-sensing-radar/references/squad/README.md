# Demand Sensing Radar

> Seu time para de reagir e começa a antecipar: radar de sinais de mercado e intenção de compra que dispara playbooks antes dos concorrentes chegarem.

**Área:** Marketing · **TopSquad:** M1 Demand Gen & ABM Orchestration · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Times de marketing e vendas vivem no modo reativo — só descobrem que uma conta estava em janela de compra depois que o concorrente fechou o contrato. Não existe processo sistemático para capturar sinais de demanda latente (funding rounds, job postings críticos, adoção de tecnologia complementar, picos de busca orgânica, atividade em review sites). O resultado mensurável: lead-time de antecipação próximo de zero (o time age junto com o mercado, não antes), win-rate médio de 15-25% em contas onde reagiu tarde, e budget de ads gasto em mercado frio enquanto contas quentes passam sem abordagem. O squad monitora continuamente 8+ categorias de sinais externos, combina com dados de intent B2B, e dispara playbooks de engajamento personalizados antes que a janela de compra abra — transformando antecipação em vantagem competitiva mensurável.

## Impacto esperado

Empresas que operam com demand sensing estruturado reportam aumento de 40-70% no win-rate em contas previamente sinalizadas versus contas abordadas sem sinal, redução de 35% no ciclo de vendas (porque o time chega quando a dor já existe, não tenta criar urgência), e lead-time de antecipação de 2-8 semanas antes do momento de compra ativo. Para uma empresa com 20 closings/mês e ticket médio de R$15k, elevar win-rate de 20% para 30% em contas sinalizadas representa R$30k de receita incremental/mês. ROI do squad positivo em 60-90 dias. KPI primário: lead-time de antecipação médio acima de 14 dias e win-rate em contas sinalizadas acima de 35% em 90 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `radar` · Radar | Radar — Orquestrador de Demand Sensing | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `pulse` · Pulse | Pulse — Signal Intelligence Agent | L2 · orquestra / decide | `monitorar-sinais-mercado.md` |
| `vortex` · Vortex | Vórtex — Market Deep Research Agent | L2 · orquestra / decide | `analisar-sinais-de-demanda.md` |
| `nexus` · Nexus | Nexus — Playbook Dispatcher Agent | L3 · aprovação humana | `disparar-playbook-correto.md` |
| `sage` · Sage | Sage — Analytics & Attribution Agent | L2 · orquestra / decide | `calcular-roi-sinal.md` |
| `bolt` · Bolt | Bolt — Content & Copy Activation Agent | L3 · aprovação humana | `gerar-anuncio-especifico.md` |
| `sigma` · Sigma | Sigma — Crític & Compliance Verifier | L3 · aprovação humana | `verificar-conformidade-e-qualidade.md` |
| `sigma-2` · Sigma 2 | Sigma — Crític & Compliance Verifier | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-demand-sensing-radar:radar` (ou instale via `npx squads add ./marketing-demand-sensing-radar`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-demand-sensing-radar-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)
- Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)
- Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)
- Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)
- Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)
- Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3)
- Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal)

## KPIs

- Lead-time de antecipação médio: meta > 14 dias antes do momento de compra ativo (medido como distância entre data do sinal e data de abertura de oportunidade no CRM)
- Win-rate em contas sinalizadas: meta > 35% em contas abordadas com pelo menos 1 sinal Hot vs. baseline histórico sem sinal (~15-20%)
- Sinais acionados por semana: volume de Hot Accounts identificadas (meta de 10-30/semana dependendo do tamanho do TAM do cliente)
- Precisão do sinal (Signal Precision Rate): % de contas Hot que viraram oportunidade real em 45 dias — meta > 40% (filtra falsos positivos)
- Tempo de resposta ao sinal: média de < 24h entre detecção de sinal Hot e primeiro toque (Nexus + Sigma + SDR)
- Pipeline atribuído ao radar: R$ de pipeline gerado por oportunidades originadas em contas sinalizadas — meta de cobertura de 3x o custo mensal do squad em 90 dias
- Quality Score médio de Sigma: média >= 8/10 nas avaliações de copy e playbooks (garante que velocidade não sacrifica qualidade)
- Taxa de recalibração de sinal: número de vezes que baseline de categoria de sinal precisa ser ajustado por mês — meta < 2 (indica que o squad está aprendendo e estabilizando)

## Integrações

- Clay — motor primário de intent data agregado de 100+ fontes, waterfall enrichment de contas, job posting tracking, technographics e sinais de funding
- Bombora / 6sense — intent data B2B por tópico específico, surge score por conta e segmento
- HubSpot CRM — campo customizado de Signal Score por conta, propriedade de ùltimo sinal detectado, webhook de stage change para atribuiçạ̃o, task automática para SDR/AE quando conta sobe para Hot
- LinkedIn Sales Navigator / LinkedIn API — company updates, mudanças de liderança, job postings críticos, atividade de contatos-alvo
- SEMrush Enterprise — monitoramento de picos de busca orgânica por keyword de problema, share of voice por segmento, menções em AI Overviews
- Crunchbase / PitchBook (via MCP ou webhook) — alertas de funding rounds, M&A, expansão geográfica
- Google Ads + Meta Ads – ativação de campanhas de retargeting disparadas por Demand Surge Playbook (via aprovação HITL)
- ClickUp – prova de trabalho: task automática por conta Hot identificada, dashboard de lead-time de antecipação, registro de playbooks disparados com status
- n8n – orquestração de workflows de monitoramento, webhooks de sinais e notificações no-code (camada complementar de automação)
- Langfuse – observabilidade OTEL de todos os agents, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de sinal
- Slack – alertas em tempo real de Hot Accounts para canal #demand-radar, notificações de Sigma BLOCKED para revisão humana urgente
- WhatsApp Business API (via Patagon AI / BotPenguin) – canal de outreach pós-aprovação Sigma para playbooks onde WhatsApp é o canal de preferência do ICP

## Entregável (prova de trabalho)

Demand Intelligence Report semanal entregue no ClickUp contendo: (1) Hot Accounts da semana com Signal Score, breakdown de sinais detectados e Context Card por conta, (2) Playbooks disparados com status (aprovados, enviados, respostas obtidas), (3) Dashboard de lead-time de antecipação e win-rate em contas sinalizadas, (4) Macro-Trend Report com 3-5 tendências setoriais e janela de oportunidade estimada, (5) ROI por categoria de sinal (qual tipo de sinal está gerando mais pipeline), (6) Pipeline atribuído ao radar no período, (7) Alertas de recalibração de threshold com recomendação de ajuste para aprovação do CMO.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Athênaeum (11 agentes, inteligência estratégica) — base direta para Vórtex (Market Deep Research Agent): estrutura completa de coleta, síntese e hierarquização de inteligência de mercado reutilizável no ciclo de Macro-Trend Research e na construção do Buy Signal Fingerprint histórico
- Data Quality Guardian (5 agentes, qualidade de dados) — acelera a construção de Sigma (Critic & Compliance Verifier): lógica de validação, detecção de anomalias em dados e scoring de qualidade já implementados — customizar as regras para sinais de intent e compliance LGPD em outreach B2B
- Genius Athena Strange (5 agentes, decisão sob incerteza) — complementa Sage (Analytics Agent) na detecção de anomalias e calibração de thresholds: framework de decisão sob incerteza e útil para diferenciar sinal real de ruído em categorias de intent com alta variância

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M1 · TopSquad de Demand Gen & ABM Orchestration** — Detecta a demanda antes do concorrente e orquestra o toque certo em contas e criadores.

- **Missão:** O motor de geração de demanda baseado em sinais: sente o mercado esquentando (demand sensing), seleciona contas-alvo (ABM) e criadores relevantes, e orquestra o outreach coordenado — anúncio, e-mail, conteúdo, criador — para chegar à conta no momento certo.
- **Por que consolidar:** Os quatro partem do mesmo insumo — sinais de intenção de mercado — e divergem só no destino do toque (conta, lead, criador). Demand sensing alimenta o ABM, que define quem o AI SDR aborda e quais criadores ativar. Separados, cada um tinha seu próprio radar de sinais; juntos, um radar serve a todos.
- **Squads irmãos:** ABM Signal Orchestrator, AI SDR Outbound Agêntico, Demand Sensing Radar, Influencer & Creator Outreach Agêntico

## Estrutura

```
marketing-demand-sensing-radar/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
