# Ágentic Analytics (Pergunte aos Seus Dados)

> O founder faz a pergunta em português e recebe a resposta em 30 segundos — sem analista, sem fila, sem achismo.

**Área:** Founder Office · **TopSquad:** F2 Performance, KPIs & Calibração de Decisões · **Prioridade:** alta · **Agentes:** 8 (6 workers + orquestrador + critic)

Gerado em 2026-09-16 a partir da especificação da página "Máquina de Receita · Organograma da Máquina" (Gabriel Marcondes). O texto de problema, impacto, papéis, contratos, gates, KPIs, integrações e entregável é literal; passos, critérios, exemplos e smoke tests são derivados por regra e estão marcados. Formato: AIOX (squad-creator-pro) e marketplace squads.sh (`squad.yaml`).

## Problema

O founder depende de analistas para responder perguntas de negócio com dados, criando fila de 24-72h e atraso na tomada de decisão. Sem governança semântica, cada analista interpreta métricas diferente, gerando inconsistência. Mensurável por: tempo pergunta->resposta (baseline: 24-72h -> meta: <2min), % de queries respondidas sem intervenção humana (baseline: 0% -> meta: >80%), e divergência de métricas entre analistas (baseline: frequente -> meta: zero, porque todos consultam a mesma camada semântica).

## Impacto esperado

ROI estimado: Se o founder toma 5 decisões/semana que dependem de dados e cada uma atrasa 1 dia por falta de resposta rápida, são 5 dias/semana de decisão subótima. Com ticket médio de impacto de R$50k por decisão estratégica, o custo de atraso é alto. Squad paga em si na primeira semana de uso intenso. Métricas concretas: redução de 90% no tempo de resposta a perguntas de dados; eliminação de 100% das inconsistências de definição de métricas (single source of truth); liberação de 8-12h/semana de analista para trabalho de maior valor; decisões mais rápidas = vantagem competitiva mensurável em MRR e CAC.

## Time

| Agente | Papel | Nível | Task |
|---|---|---|---|
| `orquestrador-analitico` · Orquestrador Analítico | Sigma (Orquestrador Analítico) | L2 · orquestra / decide | `orquestrar-pipeline.md` |
| `text-to-sql-worker` · Text-to-SQL Worker | Hermes (Text-to-SQL Worker) | L1 · worker autônomo | `traduzir-pergunta-para-sql.md` |
| `context-enricher` · Context Enricher | Mnemosyne (Context Enricher) | L1 · worker autônomo | `enriquecer-resultado-com-contexto.md` |
| `anomaly-alert-detector` · Anomaly & Alert Detector | Cassandra (Anomaly & Alert Detector) | L2 · orquestra / decide | `detectar-anomalias-estatisticas.md` |
| `strategic-query-analyst` · Strategic Query Analyst | Athena (Strategic Query Analyst) | L2 · orquestra / decide | `sintetizar-respostas-analiticas.md` |
| `semantic-layer-guardian` · Semantic Layer Guardian | Ariadné (Semantic Layer Guardian) | L3 · aprovação humana | `registrar-gap-semantico.md` |
| `decision-logger` · Decision Logger | Clio (Decision Logger) | L2 · orquestra / decide | `registrar-decisoes-baseadas-em-dados.md` |
| `sql-semantic-verifier` · SQL & Semantic Verifier | Themis (SQL & Semantic Verifier) | CRITIC | `verificar-saidas.md` |

## Como usar

1. Ative o orquestrador: `@founder-agentic-analytics:orquestrador-analitico` (ou instale via `npx squads add ./founder-agentic-analytics`).
2. Rode o pipeline: `*orquestrar-pipeline` — o workflow `workflows/founder-agentic-analytics-pipeline.yaml` aciona os workers na ordem e passa tudo pelo critic.
3. Gates humanos param o fluxo nas condições listadas abaixo; nada irreversível acontece sem aprovação.

## Gates humanos (HITL)

- Aprovação de nova métrica na camada semântica (Ariadne propõe, founder ou data owner aprova antes de adicionar ao schema — L3, irreversível pois altera definições que afetam todas as queries futuras)
- Resolução de conflito de definição entre métricas (quando duas métricas existentes têm definições inconsistentes, founder decide qual é a oficial — L3)
- Configuração de thresholds de alerta para Cassandra (founder define o que é 'crítico' vs 'atenção' para cada métrica do seu negócio — L3 no setup inicial, L2 depois)
- Confirmação de decisão tomada com base em dados para o Clío registrar (founder confirma que vai agir — não é automático para evitar log de decisões não tomadas)
- Acesso a novas fontes de dados não mapeadas (conectar novo banco, nova planilha, nova API ao schema — L3 por impacto na governança)

## KPIs

- Tempo pergunta->resposta: baseline 24-72h, meta <2min (redução de 98%)
- % de queries respondidas sem intervenção humana: baseline 0%, meta >80% em 90 dias
- Acurácia das respostas (validada por amostragem semanal pelo founder): meta >92%
- Cobertura da camada semântica: número de métricas formalmente mapeadas (meta: 50 métricas em 30 dias, 100 em 90 dias)
- Taxa de rejeição do Themis (% de respostas rejeitadas antes de chegar ao founder): meta <15% (indica qualidade do pipeline)
- Queries por semana (adoção): meta de 30+ queries/semana pelo founder em 60 dias
- Número de decisões registradas no Clio com resultado confirmado: meta 10/mês
- Taxa de acerto das análises preditivas (Clio feedback loop): meta >70% de decisões com resultado dentro do esperado
- Gaps de cobertura resolvidos por mês (Ariadne): meta: top 10 gaps do mês anterior resolvidos no mês seguinte

## Integrações

- WrenAI ou equivalente open-source (camada semântica governada, contexto semântico sobre SQL, suporte a 20+ fontes)
- PostgreSQL / MySQL / BigQuery / Snowflake (banco de dados transacional ou warehouse da empresa)
- HubSpot ou Salesforce CRM (métricas de pipeline, conversão, receita por fonte)
- Stripe / Conta Azul / Omie (métricas financeiras: MRR, churn, LTV, inadimplência)
- Google Ads / Meta Ads (CAC por canal, ROAS, CPC, impressões)
- Google Sheets / Notion (fontes de dados semi-estruturadas do founder)
- ClickUp (registro de decisões, audit trail, follow-ups do Clio)
- Slack (entrega de alertas críticos da Cassandra, interface conversacional opcional)
- Langfuse (observabilidade OTEL: rastreamento de cada query, custo de tokens, latência, acurácia)
- Claude Agent SDK + LangGraph (orquestração stateful das sessões analíticas multi-turno)

## Entregável (prova de trabalho)

Resposta analítica source-grounded: número preciso + SQL transparente + interpretação contextualizada + nível de confiança + recomendação de ação — tudo rastreável à fonte de dados governada. Artefatos secundários: (1) Semantic Layer Glossary (documento vivo com todas as métricas definidas formalmente); (2) Daily Anomaly Digest (email/Slack diário com sinais relevantes ou confirmação de normalidade); (3) Decision Audit Trail no ClickUp (histórico de todas as decisões tomadas com dados); (4) Monthly Analytics Health Report (cobertura, acurácia, gaps, evolução de adoção).

## Bases gratuitas reutilizáveis (citadas na especificação)

- Data Quality Guardian (5 agentes de qualidade de dados) — base direta para o Themis (Critic) e para o processo de validacao do schema semantico da Ariadne. Reutiliza os patterns de validacao, deteccao de anomalias e auditoria de dados.
- Athenaeum (11 agentes, inteligência estratégica) — base para o Athena (Strategic Query Analyst) e para o pipeline de síntese estratégica. Reutiliza a arquitetura de decomposição de perguntas complexas em sub-hipóteses e agregação de evidências.
- Skeptic Protocol (5 agentes, red-team/QA) — base para o protocolo de validação do Themis antes de entregar respostas ao founder. Reutiliza o framework de verificação de claims, rastreabilidade de afirmações e detecção de alucinação.

As bases citadas que estão neste repositório ficam em `../../squads-gratuitos/`.

## Contexto da TopSquad

**F2 · TopSquad de Performance, KPIs & Calibração de Decisões** — Pergunte aos dados, acompanhe as metas e calibre o próprio julgamento ao longo do tempo.

- **Missão:** O squad que mede e aprende: responde perguntas em linguagem natural sobre os dados, monitora KPIs/OKRs com alertas, e registra decisões + postmortems para calibrar o julgamento do founder ao longo do tempo.
- **Por que consolidar:** Os três giram o mesmo ciclo: medir (analytics), comparar com a meta (KPI/OKR) e refletir sobre a decisão (journal). O KPI Pulse lê os mesmos dados do analytics; o decision journal precisa do resultado dos KPIs para o postmortem. Unidos, formam um loop fechado de decisão informada → resultado medido → aprendizado.
- **Squads irmãos:** Agentic Analytics (Pergunte aos Seus Dados), KPI/OKR Pulse, Decision Journal & Postmortem

## Estrutura

```
founder-agentic-analytics/
├── squad.yaml            ← manifesto do marketplace (validado por @squads-sh/validator)
├── config.yaml           ← config AIOX (entry_agent, metadata)
├── agents/               ← orquestrador, workers, critic
├── tasks/                ← uma task por agente (HO-TP-001, 8 campos)
├── workflows/            ← pipeline com fases, checkpoints, veto e gates
├── checklists/           ← checklist do critic
└── config/               ← tech-stack, source-tree, coding-standards
```
