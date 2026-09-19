# Funnel Analytics & Attribution Squad

> Pare de adivinhar o que gera receita: atribuição cross-channel precisa, anomalias detectadas em minutos, forecast de pipeline com intervalo de confiança real.

**Área:** Marketing · **TopSquad:** M2 Performance: Paid Media, CRO & Attribution · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Atribuição fragmentada entre canais impede saber o que realmente gera receita e anomalias passam despercebidas por dias. Sem visibilidade unificada, budget é alocado por feeling, CAC é subestimado e oportunidades de escalar canais ganhadores são perdidas. Mensurável por: cobertura de atribuição (meta: >95%), tempo de detecção de anomalia (meta: <2h vs média de mercado 48-72h) e acurácia de pipeline forecast (meta: erro absoluto médio <12%).

## Impacto esperado

ROI estimado: redução de 20-35% de spend desperdiçado em canais de baixa atribuição, aumento de 15-25% na eficiência do CAC por realocação de budget para canais com atribuição comprovada, e redução de 80% no tempo de detecção de anomalias (de 48-72h para <2h), evitando perdas de pipeline por campanhas com anomalia não detectada. Para uma empresa com R$200k/mês em média paga, isso representa potencial de R$40-70k/mês em budget recuperado ou melhor alocado, pagando o squad em <30 dias.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `atlas` · Atlas | Atlas — Maestro de Inteligência de Funil | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `nexus` · Nexus | Nexus — Agente de Coleta e Unificação de Dados | L0 · worker determinístico | `coletar-etl-dados.md` |
| `hermes` · Hermes | Hermes — Agente de Atribuição Multi-Model | L1 · worker autônomo | `calcular-atribuicao-multi-modelo.md` |
| `argus` · Argus | Argus — Agente de Detecção de Anomalias | L2 · orquestra / decide | `detectar-anomalias-kpis.md` |
| `cassandra` · Cassandra | Cassandra — Agente de Forecast de Pipelíne | L1 · worker autônomo | `gerar-forecast-pipeline.md` |
| `lumen` · Lumen | Lúmen — Agente de Qualidade de Tracking e UTM | L3 · aprovação humana | `auditar-qualidade-de-tracking.md` |
| `oracle` · Oracle | Oracle — Agente de Relatório e Narrativa Executiva | L1 · worker autônomo | `gerar-relatorios-executivos.md` |
| `skeptic` · Skeptic | Skeptic — Agente Crítico de Integridade de Dados e Narrativa | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-funnel-analytics-attribution:atlas` (ou instale via `npx squads add ./marketing-funnel-analytics-attribution`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-funnel-analytics-attribution-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- L3 — Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar ou corrigir antes do go-live. SLA: 30min para resposta, após isso o sistema notifica o gestor direto.
- L3 — Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor de media antes de execucao. O squad gera o racional completo, humano aprova ou rejeita com comentario.
- L3 — Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing de 5 linhas e aguarda confirmação de que foi visto (acknowledgment) antes de escalar para investigação automática mais profunda.
- L2 — Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta. Previne drift de sensibilidade ao longo do tempo.
- L2 — Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP de Marketing. Revisão trimestral.
- L1 — Revisão de relatório executivo antes de envio ao board: Oracle gera, Skeptic valida, mas um humano (CMO ou analista sênior) faz leitura final antes de envio ao CEO/board. Opcional para relatórios internos de time.

## KPIs

- Attribution Coverage Score: % do pipeline com pelo menos 1 touchpoint rastreável — meta >95% (baseline típico: 60-75%)
- Tempo médio de detecção de anomalia P1: da ocorrência ao alerta — meta <2h (baseline indústria: 48-72h)
- Acurácia do forecast de pipeline: Mean Absolute Percentage Error (MAPE) — meta <12% no horizonte de 30 dias
- % de campanhas lançadas sem UTM inválido: meta 100% (zero campanhas sem UTM correto após 30 dias de operação)
- Tempo de resposta a alerta P1 (HITL acknowledgment): meta <30 min em horário comercial
- Redução de CAC por canal pos-otimização: meta de redução de 15-25% nos primeiros 90 dias por realocação baseada em atribuição
- Task success rate no Langfuse: dev >70%, staging >85%, prod >95% por workflow do squad
- Frequência de relatório executivo entregue no prazo: meta 100% dos relatórios semanais entregues antes de segunda-feira 8h

## Integrações

- Google Ads API (via MCP server) — ingestão de impressões, cliques, CPC, conversões, spend por campanha/ad group/keyword
- Meta Ads API (via MCP server) — ingestão de métricas de performance de Facebook/Instagram Ads com breakdown por objetivo
- LinkedIn Ads API (via MCP server) — ingestão de métricas de campanhas B2B com audience insights
- Google Analytics 4 / Segment (via MCP server ou webhook) — eventos de conversão no site, jornada anônima de usuário, sessões por source/medium
- HubSpot CRM API (via MCP server) — oportunidades criadas, stage transitions, MQL/SQL/Closed-Won com valores, contatos e companies para match com touchpoints
- Salesforce API (alternativa ao HubSpot) — pipeline, opportunities, closed-won, lead source nativo
- ClickUp API — criação automática de tasks para anomalias P1/P2 (prova de trabalho), tracking de itens de ação de relatório, status de campanhas ativas
- Slack Webhook — alertas de anomalia em tempo real por severidade (P1: canal #alerts-críticos, P2/P3: canal #marketing-ops)
- Notion ou Google Sheets — output de relatórios executivos (Oracle escreve diretamente via API)
- Langfuse — observabilidade OTEL de todas as chamadas de agente, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de custo por execução
- n8n (opcional, no-code orchestration layer) — alternativa para schedule de jobs e webhooks sem necessidade de infra custom
- BigQuery ou Snowflake (data warehouse) — persistência do dataset canônico de touchpoints gerado pelo Nexus, base para todos os modelos

## Entregável (prova de trabalho)

Attribution Intelligence Report — relatório semanal multi-formato (Executive Brief 2p + Marketing Ops Report detalhado + Finance Report) gerado automaticamente todo domingo às 20h, contendo: (1) Attribution Scorecard com crédito por canal em 4 modelos, (2) Anomaly Log do período com status de resolução, (3) Pipeline Forecast para as próximas 4 semanas com confidence interval, (4) UTM Health Score com lista de itens de ação, (5) Top-3 recomendações priorizadas por impacto estimado em R$. Artefato registrado no ClickUp como task fechada (prova de trabalho verificável) e entregue via Notion/Google Docs + Slack summary.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 agentes de qualidade de dados, squads.sh) — base direta para o agente Lumen (UTM/tracking hygiene) e para a lógica de validação do Nexus; reutilizar os padrões de detecção de anomalia de schema e validação de integridade referencial.
- Skeptic Protocol (5 agentes de red-team/QA, squads.sh) — base para o agente Crític do squad; os padrões de adversarial questioning e validation checklist do Skeptic Protocol aceleram a implementação do verificador de narrativa do Oracle.
- Five Vitals (diagnóstico de sistemas, myclaude) — acelera a fase de Discovery do squad, especificamente o 'Mapa de Cobertura de Dados'; o framework de health check dos 5 vitais é diretamente adaptável para o Attribution Coverage Score e o UTM Health Score.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M2 · TopSquad de Performance: Paid Media, CRO & Attribution** — O loop fechado da mídia: investe, otimiza a página, acerta o timing e prova o que deu retorno.

- **Missão:** O ciclo fechado de performance: aloca e otimiza mídia paga, melhora a landing page para converter, dispara no melhor horário e mede a atribuição real — fechando o loop investir → converter → medir → reinvestir.
- **Por que consolidar:** Mídia, CRO, timing e atribuição são o mesmo loop de otimização visto de ângulos diferentes — e a atribuição é justamente o sinal que deveria realimentar a mídia. Em squads isolados, o de mídia não enxergava o que a atribuição via, e o de CRO otimizava cego. Unidos, a medição fecha o ciclo.
- **Squads irmãos:** Paid Media Autopilot, CRO & Landing Page Agêntico, Intelligent Timing Orchestrator, Funnel Analytics & Attribution

## Estrutura

```
marketing-funnel-analytics-attribution/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
