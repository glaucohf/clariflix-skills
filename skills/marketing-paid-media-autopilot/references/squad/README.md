# Paid Media Autopilot

> Seu budget nunca mais vai dormir enquanto o concorrente escala — autonomia L2/L3 para bid, pacing e criativo em tempo real.

**Área:** Marketing · **TopSquad:** M2 Performance: Paid Media, CRO & Attribution · **Prioridade:** must‑have · **Agentes:** 9 (7 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Gestão manual de campanhas reage com atraso de 24-72h a variações de performance, desperdiçando budget em criativos fatigados e perdendo janelas de escala por falta de realocação em tempo real. O squad substitui o loop humano de análise-decisão-execução por um ciclo autônomo de monitoramento contínuo, rotação de criativo e ajuste de bid/budget dentro de bandas pré-aprovadas (guardrails financeiros), com gate L3 para decisões irreversíveis ou de alto impacto.

## Impacto esperado

Redução estimada de 25-40% no CAC via eliminação de budget desperdiçado em criativos fatigados (frequência > threshold) e realocação dinâmica para ad sets de ROAS > baseline. Melhoria de 30-50% no ROAS médio por rotação antecipada e testes de criativo sistemáticos (30-50 variações/ciclo). Desvio de pacing diário reduzido de ~15% para < 3% com ajuste automático a cada 2h. ROI estimado: para cliente com R$50k/mês em mídia, economia de R$12-20k/mês em budget mal alocado + ganho de receita pela melhoria de ROAS — payback do squad em 1-2 meses.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Orquestrador de Mídia Paga | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `argos` · Argos | Argos — Performance Monitor | L0 · worker determinístico | `monitorar-performance-campanhas.md` |
| `midas` · Midas | Midas — Bid & Budget Optimizer | L3 · aprovação humana | `ajustar-bid-e-realocar-budget.md` |
| `prism` · Prism | Prism — Creative Rotation Agent | L2 · orquestra / decide | `rotacionar-criativos.md` |
| `vox` · Vox | Vox — Copy & Creative Briefêr | L2 · orquestra / decide | `gerar-copy-para-ads.md` |
| `atlas` · Atlas | Atlas — Attribution & Analytics Agent | L1 · worker autônomo | `consolidar-dados-de-performance.md` |
| `sentinel` · Sentinel | Sentinel — Signal & Intent Monitor | L1 · worker autônomo | `monitorar-sinais-de-mercado.md` |
| `aegis` · Aegis | Aegis — Compliance & Brand Guard | L2 · orquestra / decide | `verificar-conformidade-compliance.md` |
| `aegis-2` · Aegis 2 | Aegis — Compliance & Brand Guard | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-paid-media-autopilot:orion` (ou instale via `npx squads add ./marketing-paid-media-autopilot`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-paid-media-autopilot-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de ROAS para escala, orçamento máximo em risco por ciclo) — sem essa aprovação o squad não opera
- Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget total ou pausar campanha inteira) requer aprovação explícita via Slack/WhatsApp antes de execução pelo Midas
- Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos de mensagem sem histórico) requer aprovação humana — irreversível em termos de impressão inicial
- Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de threshold) requerem OK do gestor antes de ativação automática
- Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com os guardrails mais recentes aprovados
- Onboarding de nova plataforma ou canal: qualquer expansão para nova plataforma de mídia (ex: adicionar TikTok Ads, Pinterest Ads, CTV) requer aprovação e configuração supervisionada pelo humano responsável
- Bloqueio por anomalia crítica: se Argos detectar anomalia CRITICAL (ex: ROAS caiu > 50% em 1h ou spend disparou 300% acima do target), o squad pausa todas as ações autônomas e aguarda instrução humana explícita antes de retomar

## KPIs

- ROAS médio das campanhas gerenciadas (target: melhoria >= 30% vs baseline pre-squad em 90 dias)
- CAC (Custo de Aquisição de Cliente) por canal (target: redução >= 25% vs baseline em 90 dias)
- Desvio de pacing diário (target: < 3% de desvio vs target de spend diário — vs ~15% média manual)
- Percentual de budget alocado em criativos com ROAS acima do threshold (target: > 70% do budget ativo)
- Frequência média de criativo no momento da rotação (target: rotação antes de atingir frequência crítica, reduzindo fadiga em >= 40%)
- Tempo médio de detecção-execução de anomalia (target: < 30 minutos vs 24-72h manual)
- Taxa de aprovação no gate do Aegis (target: > 85% de copy gerada aprovada sem revisão na primeira iteração)
- Número de variações de criativo testadas por mês (target: >= 20 variações ativas simultaneamente)
- Taxa de task success do squad no Langfuse (target: >= 95% em produção)
- Tempo de retorno sobre investimento no squad (target: payback < 60 dias para clientes com >= R$30k/mês em mídia)

## Integrações

- Google Ads API (MCP server) — leitura de métricas e execução de ajustes de bid/budget/status de criativo
- Meta Marketing API (MCP server) — leitura de métricas e execução de ações em campanhas Facebook/Instagram Ads
- HubSpot CRM (MCP server) — closed-loop attribution (lead source, deal value, lifecycle stage por campanha de origem)
- ClickUp (MCP server) — registro de toda ação executada como task/prova de trabalho auditável, gestão do backlog de criativos solicitados
- Slack (MCP server) — canal de alertas em tempo real, gate de aprovação L3 (aprovação via reaction/botão no próprio canal)
- WhatsApp Business API — canal alternativo de alertas urgentes e aprovação L3 para gestores fora do escritório
- Google Trends API — monitoramento de sinais de demanda pelo Sentinél
- Meta Ads Library API — monitoramento de criativos de concorrentes pelo Sentinel
- Google Search Console API — dados de demanda organica como proxy de intent pelo Sentinel
- Langfuse (observabilidade OTEL) — rastreamento de todas as execuções de agentes, quality gates (dev 70% / staging 85% / prod 95%), evals de performance do squad
- Google Sheets / Looker Studio — dashboard de KPIs compartilhado com cliente (visualização de ROAS, CAC, pacing, score de criativo em tempo real)
- n8n — orquestração de automações complementares (webhooks de conversão offline, sincronização de dados entre plataformas, notificações customizadas)

## Entregável (prova de trabalho)

Paid Media Autopilot Report — relatório consolidado diário (gerado automaticamente às 08h) contendo: (1) Performance snapshot D-1 (ROAS, CAC, pacing, CPL por campanha/canal), (2) Ações autônomas executadas no período (rotações de criativo, ajustes de bid/budget com antes/depois), (3) Ações pendentes de aprovação L3 (aguardando OK humano), (4) Score de saúde do banco de criativos (quantos ativos, quantos fatigados, quantos em produção), (5) Alertas de oportunidade da semana (sinais do Sentinel), (6) Projeção de performance para próximos 7 dias com recomendações proativas. Formato: PDF executivo + JSON estruturado para integração + ClickUp board com todas as tasks auditáveis.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 agentes) — base para o pipeline de validação e limpeza de dados de métricas de plataforma antes de qualquer decisão do Argos; reutilizar os padrões de detecção de anomalia e validação de schema para os feeds de API do Google Ads e Meta Ads
- Skeptic Protocol (5 agentes, red-team/QA) — base direta para o agente Aegis (Compliance & Brand Guard); o padrao de red-team adversarial do Skeptic Protocol se mapeia exatamente na funcao de critic/verifier do gate de copy e acoes financeiras
- Token-Optimizer — base para otimização de custo do squad em produção; dado o volume de polling contínuo (Argos a cada 15-30min) e geração de copy (Vox), o Token-Optimizer reduz custo operacional via cache inteligente e roteamento Opus/Sonnet por complexidade de task

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M2 · TopSquad de Performance: Paid Media, CRO & Attribution** — O loop fechado da mídia: investe, otimiza a página, acerta o timing e prova o que deu retorno.

- **Missão:** O ciclo fechado de performance: aloca e otimiza mídia paga, melhora a landing page para converter, dispara no melhor horário e mede a atribuição real — fechando o loop investir → converter → medir → reinvestir.
- **Por que consolidar:** Mídia, CRO, timing e atribuição são o mesmo loop de otimização visto de ângulos diferentes — e a atribuição é justamente o sinal que deveria realimentar a mídia. Em squads isolados, o de mídia não enxergava o que a atribuição via, e o de CRO otimizava cego. Unidos, a medição fecha o ciclo.
- **Squads irmãos:** Paid Media Autopilot, CRO & Landing Page Agêntico, Intelligent Timing Orchestrator, Funnel Analytics & Attribution

## Estrutura

```
marketing-paid-media-autopilot/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
