# Lead Scoring & Router

> Nenhum lead quente espera fila: score em tempo real, roteamento inteligente e o lead certo na mão certa em menos de 5 minutos.

**Área:** Marketing · **TopSquad:** M5 Captura, Qualificação & Reativação de Leads · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

Leads qualificados chegam por multiplos canais (ads, site, WhatsApp, LinkedIn, eventos) e caem no mesmo balde — uma fila generica que o SDR errado vai abordar horas depois, quando o interesse ja esfriou. Sem score unificado cross-platform, o time nao distingue um lead quente de um lead curioso e trata todos igualmente. Resultado mensuravel: speed-to-lead medio acima de 4h, taxa de conversao abaixo de 12% em leads de topo e ate 30% de leads orfaos (sem followup em 48h). O squad captura leads de todas as fontes, calcula um Score de Fit + Score de Intent em tempo real via cascata de enriquecimento, e roteia automaticamente para o canal certo (SDR humano tier 1, sequencia automatica tier 2, nurture tier 3) com o contexto completo do lead ja preparado.

## Impacto esperado

Empresas que implementam scoring + roteamento inteligente reportam redução de speed-to-lead de horas para minutos (+300% de velocidade), aumento de 25-40% na taxa de conversão de leads para oportunidade qualificada, e eliminação de leads órfãos (de 30% para menos de 3%). Para uma empresa com 500 leads/mês e ticket médio de R$20k, um aumento de 8 pontos percentuais na conversão (de 12% para 20%) representa R$800k/mês de pipeline adicional. ROI do squad estimado em 30-60 dias de operação. KPI primário: speed-to-lead < 5 minutos para leads hot (score >= 75) em 30 dias de produção.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orion` · Orion | Orion — Maestro de Scoring & Roteamento | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `scout` · Scout | Scout — Lead Intake & Source Mapper | L0 · worker determinístico | `monitorar-e-normalizar-leads.md` |
| `apex` · Apex | Apex — Scoring Engine Agent | L1 · worker autônomo | `calcular-score-lead.md` |
| `iris` · Iris | Íris — Enrichment Cascade Agent | L2 · orquestra / decide | `enriquecer-dados-lead.md` |
| `vector` · Vector | Vector — Intelligent Router Agent | L2 · orquestra / decide | `rotear-lead-para-destino-correto.md` |
| `pulse` · Pulse | Pulse — Pipeline Monitor & Anomaly Detector | L2 · orquestra / decide | `monitorar-pipeline-de-scoring.md` |
| `critique` · Critique | Critique — Critic & Model Calibration Agent | L3 · aprovação humana | `calibrar-modelo-scoring.md` |
| `critique-2` · Critique 2 | Critique — Critic & Model Calibration Agent | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@marketing-lead-scoring-router:orion` (ou instale via `npx squads add ./marketing-lead-scoring-router`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/marketing-lead-scoring-router-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o threshold de 75 é ajustável) e validar a Routing Matrix antes de ativar em produção (L3)
- Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads (L3)
- Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique deve ser aprovada pelo Sales Lead antes de Orion aplicar em produção (L3)
- Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerteza (L3)
- Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3)
- Desvio crítico de performance detectado por Critique — quando Precision@Hot cai abaixo de 40% ou Recall cai abaixo de 50%, o squad entra em modo de revisão e não processa novos leads sem autorização humana (L3)
- Ativação de nova fonte de leads (novo canal, novo formulário) — Scout não ativa fonte nova automaticamente, requer validação do schema de campos e regras de normalização pelo time de operações (L1)
- Ajuste de capacidade de SDR na Routing Matrix — quando SDR entra em ferias ou saı da empresa, Vector nao rebalanceia automaticamente sem confirmacao do Sales Lead (L1)

## KPIs

- Speed-to-lead para leads Hot: meta < 5 minutos do Scout ao SDR designado (baseline atual a medir no Discovery, tipicamente > 4h)
- Taxa de leads órfãos: meta < 3% (sem followup em 48h) — baseline típico de 25-30%
- Precisão do modelo (Precision@Hot): % de leads Hot que o SDR confirma como qualificados — meta > 60% em 90 dias
- Recall do modelo (Recall@Hot): % dos leads que converteram que foram classificados como Hot ou Warm — meta > 75% em 90 dias
- Taxa de conversão Lead -> Oportunidade Qualificada por tier: Hot meta > 30%, Warm meta > 15%, Cold meta > 5% (rastreado separadamente para validar poder preditivo do modelo)
- Cobertura de enriquecimento: >= 85% dos campos prioritários preenchidos para leads Hot antes do roteamento
- SLA de roteamento cumprido: >= 95% dos leads Hot roteados em < 5 minutos, >= 90% dos leads Warm em < 2h
- Score de qualidade de auditoria (Critique): Precision@Hot e Recall@Hot dentro das metas acima — qualquer semana abaixo do threshold dispara revisão de modelo
- Redução de CAC por segmento: meta de 15% em 6 meses via melhora de targeting e velocidade de resposta
- Volume de leads processados sem erro: >= 99% dos leads normalizados e roteados sem falha técnica (health do pipeline)

## Integrações

- HubSpot CRM — campo customizado Lead Score (0-100), Tier (Hot/Warm/Cold/Unfit), Score Breakdown (JSON), SDR Designado, Fonte Normalizada; webhook de novo contato para Scout; criação automática de deal por Vector para leads Warm+; ativação de sequences para Warm
- Meta Lead Ads API — webhook de novo lead de campanhas Facebook/Instagram Lead Ads para Scout
- Google Ads Lead Form Extensions — webhook de novo lead de formulários Google Ads para Scout
- LinkedIn Lead Gen Forms — webhook de novo lead de anúncios LinkedIn para Scout
- WhatsApp Business API (via Patagon AI ou Leadsales) — evento de novo contato iniciado para Scout; envio de mensagem de primeiro contato automatizado para leads Warm (Vector aciona)
- Clay — waterfall enrichment primary engine, ICP custom tables, intent signals de 100+ fontes (via MCP)
- Apollo.io — enriquecimento complementar de contatos e prospecting (via MCP ou API direta)
- Cognism — enriquecimento GDPR-compliant para contatos internacionais (via API)
- Apify MCP — scraping de perfil LinkedIn para validacao de cargo/empresa quando email disponıvel
- ClickUp — prova de trabalho: task automatica por lead Hot com brief completo, dashboard de KPIs em tempo real, relatorio semanal de performance, formulario de feedback dos SDRs
- Slack — alertas de lead Hot sem contato (Warning/Critical), notificação push para SDR designado, relatório diário de pipeline para Sales Lead
- n8n — orquestracao de workflows de normalizacao de leads de fontes nao-padrao e notificacoes complexas (complemento no-code para integrações customizadas)
- Langfuse — observabilidade OTEL de todos os agents, rastreamento de latência de scoring (meta < 60s), quality gates (dev 70% / staging 85% / prod 95% task success), log de todas as decisões de roteamento para auditoria
- Google Sheets / Looker Studio — dashboard executivo de KPIs (speed-to-lead, conversão por tier, volume por fonte) para CMO e Sales Lead

## Entregável (prova de trabalho)

Pipeline de scoring e roteamento de leads em produção entregando: (1) Score Card automático por lead (Fit + Intent + Composto + Tier + Reasoning narrativo) publicado no CRM em < 60 segundos da entrada do lead, (2) Roteamento automático de leads Hot para SDR designado em < 5 minutos com brief completo (empresa, score breakdown, sinal de intent, histórico de interações, próximos passos sugeridos), (3) Ativação automática de sequências de email + WhatsApp para leads Warm com personalização baseada no score, (4) Dashboard de KPIs em tempo real no ClickUp (speed-to-lead, distribuição de tiers, health dos webhooks, taxa de órfãos), (5) Relatório semanal de performance do modelo com Precision/Recall por tier e recomendações de calibração, (6) Score Card Model versionado com histórico de performance por versão e changelog de calibrações.

## Bases gratuitas reutilizáveis (citadas na especificação)

- Mãe Intuitiva CRM (CRM/leads) — base direta para a lógica de roteamento e gestão de leads do Vector: estrutura de priorização, atribuição e notificação de leads já implementada, customizar para as regras de scoring e a Routing Matrix específica do cliente
- Data Quality Guardian (5 agentes, qualidade de dados) — acelera a construcao do Critique: logica de auditoria por amostragem, deteccao de anomalias e scoring de qualidade ja disponıveis, adaptar para auditar Score Cards e detectar falsos positivos/negativos
- Athenaeum (11 agentes, inteligencia estrategica) — acelera o modulo de calibracao continua do Critique: estrutura de coleta de evidencias, analise de padroes e sıntese de recomendacoes ja implementada, reutilizar para o ciclo quinzenal de auditoria do modelo de scoring

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**M5 · TopSquad de Captura, Qualificação & Reativação de Leads** — Da captura à qualificação e ao reaquecimento da base adormecida.

- **Missão:** A ponte entre Marketing e Vendas: pontua e roteia os leads gerados pelas campanhas, qualifica via WhatsApp e reativa a base adormecida que o marketing já pagou para adquirir. Garante que nenhum lead capturado se perca.
- **Por que consolidar:** Os três operam sobre o mesmo objeto — o lead que o marketing capturou — em momentos distintos: na entrada (score/router), na conversa (WhatsApp) e no esfriamento (reativação). É o mesmo ciclo de vida do lead de marketing, partido em três. Espelha o V2/V3/V4 de Vendas; aqui fica do lado de marketing por nutrir o lead pago.
- **Squads irmãos:** Lead Scoring & Router, WhatsApp Qualifier, Dormant Lead Reactivation

## Estrutura

```
marketing-lead-scoring-router/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
