---
task: atlasPipeline()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Attribution Intelligence Report"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "relatório semanal multi-formato (Executive Brief 2p + Marketing Ops Report detalhado + Finance Report) gerado automaticamente todo domingo às 20h, contendo: (1) Attribution Scorecard com crédito por canal em 4 modelos, (2) Anomaly Log do período com status de resolução, (3) Pipeline Forecast para as próximas 4 semanas com confidence interval, (4) UTM Health Score com lista de itens de ação, (5) Top-3 recomendações priorizadas por impacto estimado em R$"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato registrado no ClickUp como task fechada (prova de trabalho verificável) e entregue via Notion/Google Docs + Slack summary"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do squad. Recebe metas de aquisição e perguntas de negócio (ex: 'qual canal está gerando mais pipeline qualificado este mês?'), decompõe em subtasks para os workers especializado…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Skeptic antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar ou corrigir antes do go-live. SLA: 30min para resposta, após isso o sistema notifica o gestor direto."
    - "[ ] L3: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor de media antes de execucao. O squad gera o racional completo, humano aprova ou rejeita com comentario."
    - "[ ] L3: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing de 5 linhas e aguarda confirmação de que foi visto (acknowledgment) antes de escalar para investigação automática mais profunda."
    - "[ ] L2: Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta. Previne drift de sensibilidade ao longo do tempo."
    - "[ ] L2: Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP de Marketing. Revisão trimestral."
---

# Orquestrar Pipeline do Funnel Analytics & Attribution Squad

**Task ID:** `atlasPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Funnel Analytics & Attribution Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Funnel Analytics & Attribution Squad |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Maestro de Inteligência de Funil) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do squad. Recebe metas de aquisição e perguntas de negócio (ex: 'qual canal está gerando mais pipeline qualificado este mês?'), decompõe em subtasks para os workers especializados, consolida insights e sintetiza o relatório executivo final. Monitora SLAs de cada worker, prioriza qual anomalia investigar primeiro quando múltiplas ocorrem simultaneamente e decide quando escalar para HITL. Gerencia o estado do pipeline de dados e garante que nenhum dado crítico seja reportado sem validação do Critic.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Attribution Intelligence Report
- relatório semanal multi-formato (Executive Brief 2p + Marketing Ops Report detalhado + Finance Report) gerado automaticamente todo domingo às 20h, contendo: (1) Attribution Scorecard com crédito por canal em 4 modelos, (2) Anomaly Log do período com status de resolução, (3) Pipeline Forecast para as próximas 4 semanas com confidence interval, (4) UTM Health Score com lista de itens de ação, (5) Top-3 recomendações priorizadas por impacto estimado em R$
- Artefato registrado no ClickUp como task fechada (prova de trabalho verificável) e entregue via Notion/Google Docs + Slack summary

## Trigger

Orquestrador central do squad. Recebe metas de aquisição e perguntas de negócio (ex: 'qual canal está gerando mais pipeline qualificado este mês?'), decompõe em subtasks para os workers especializados, consolida insights e sintetiza o relatório executivo final. Monitora SLAs de cada worker, prioriza qual anomalia investigar primeiro quando múltiplas ocorrem simultaneamente e decide quando escalar para HITL. Gerencia o estado do pipeline de dados e garante que nenhum dado crítico seja reportado sem validação do Critic.

## Knowledge base (o que o executor consulta)

- Google Ads API (via MCP server)
- ingestão de impressões, cliques, CPC, conversões, spend por campanha/ad group/keyword
- Meta Ads API (via MCP server)
- ingestão de métricas de performance de Facebook/Instagram Ads com breakdown por objetivo
- LinkedIn Ads API (via MCP server)
- ingestão de métricas de campanhas B2B com audience insights
- Google Analytics 4 / Segment (via MCP server ou webhook)
- eventos de conversão no site, jornada anônima de usuário, sessões por source/medium
- HubSpot CRM API (via MCP server)
- oportunidades criadas, stage transitions, MQL/SQL/Closed-Won com valores, contatos e companies para match com touchpoints
- Salesforce API (alternativa ao HubSpot)
- pipeline, opportunities, closed-won, lead source nativo
- ClickUp API
- criação automática de tasks para anomalias P1/P2 (prova de trabalho), tracking de itens de ação de relatório, status de campanhas ativas
- Slack Webhook
- alertas de anomalia em tempo real por severidade (P1: canal #alerts-críticos, P2/P3: canal #marketing-ops)
- Notion ou Google Sheets
- output de relatórios executivos (Oracle escreve diretamente via API)
- observabilidade OTEL de todas as chamadas de agente, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de custo por execução
- n8n (opcional, no-code orchestration layer)
- alternativa para schedule de jobs e webhooks sem necessidade de infra custom
- BigQuery ou Snowflake (data warehouse)
- persistência do dataset canônico de touchpoints gerado pelo Nexus, base para todos os modelos

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Skeptic antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Attribution Intelligence Report
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Skeptic registrado
- [ ] Gate L3 respeitado: Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de cam…
- [ ] Gate L3 respeitado: Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovaca…
- [ ] Gate L3 respeitado: Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de bloqueio de campanha pelo Lumen: quando Lumen bloqueia lançamento por UTM inválido, um humano (marketing ops ou gerente de campanha) deve aprovar… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendacao de realocacao de budget >R$10k: quando Hermes ou Cassandra recomendam mover budget significativo entre canais, requer aprovacao do CMO ou gestor d… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Alerta de anomalia P1 com impacto >R$50k de pipeline: quando Argus detecta anomalia P1 de alta severidade, notifica imediatamente o CMO via Slack com briefing… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Calibração de thresholds de anomalia: mensalmente, um humano (analista de dados ou marketing ops) revisa os thresholds de detecção do Argus e aprova ou ajusta.… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Seleção de modelo de atribuição primário: o Hermes recomenda, mas a decisão final de qual modelo usar como 'source of truth' para budget decisions é do CMO/VP… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão de relatório executivo antes de envio ao board: Oracle gera, Skeptic valida, mas um humano (CMO ou analista sênior) faz leitura final antes de envio ao… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Skeptic | BLOQUEIA entrega |

## Handoff

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
