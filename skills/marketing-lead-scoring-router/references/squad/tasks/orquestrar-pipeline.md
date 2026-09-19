---
task: orionPipeline()
responsavel: "Orion"
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
    descricao: "Pipeline de scoring e roteamento de leads em produção entregando: (1) Score Card automático por lead (Fit + Intent + Composto + Tier + Reasoning narrativo) publicado no CRM em < 60 segundos da entrada do lead, (2) Roteamento automático de leads Hot para SDR designado em < 5 minutos com brief completo (empresa, score breakdown, sinal de intent, histórico de interações, próximos passos sugeridos), (3) Ativação automática de sequências de email + WhatsApp para leads Warm com personalização baseada no score, (4) Dashboard de KPIs em tempo real no ClickUp (speed-to-lead, distribuição de tiers, health dos webhooks, taxa de órfãos), (5) Relatório semanal de performance do modelo com Precision/Recall por tier e recomendações de calibração, (6) Score Card Model versionado com histórico de performance por versão e changelog de calibrações"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion e o controlador central do pipeline de leads. Recebe notificacao de novo lead de qualquer fonte, coordena a cascata de enriquecimento e scoring, decide o tier do lead (Hot/Warm/Cold/Unfit) com…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Critique 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o threshold de 75 é ajustável) e validar a Routing Matrix antes de ativar em produção (L3)"
    - "[ ] HITL: Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads (L3)"
    - "[ ] HITL: Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique deve ser aprovada pelo Sales Lead antes de Orion aplicar em produção (L3)"
    - "[ ] HITL: Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerteza (L3)"
    - "[ ] HITL: Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3)"
---

# Orquestrar Pipeline do Lead Scoring & Router

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Lead Scoring & Router

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Lead Scoring & Router |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Maestro de Scoring & Roteamento) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orion e o controlador central do pipeline de leads. Recebe notificacao de novo lead de qualquer fonte, coordena a cascata de enriquecimento e scoring, decide o tier do lead (Hot/Warm/Cold/Unfit) com base no Score composto, e delega o roteamento ao Vector. Monitora continuamente a saude do modelo: detecta drift de conversao, aciona recalibracao quando a taxa de acerto cai abaixo de threshold, e escala para HITL quando um lead e ambiguo (score entre 65-80 e sinais contraditories). Opera no padrao orchestrator-worker: nunca executa enriquecimento ou envio diretamente, apenas orquestra, prioriza e sintetiza. Persona: metodico, orientado a velocidade sem abrir mao de qualidade, obsessivo com speed-to-lead.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pipeline de scoring e roteamento de leads em produção entregando: (1) Score Card automático por lead (Fit + Intent + Composto + Tier + Reasoning narrativo) publicado no CRM em < 60 segundos da entrada do lead, (2) Roteamento automático de leads Hot para SDR designado em < 5 minutos com brief completo (empresa, score breakdown, sinal de intent, histórico de interações, próximos passos sugeridos), (3) Ativação automática de sequências de email + WhatsApp para leads Warm com personalização baseada no score, (4) Dashboard de KPIs em tempo real no ClickUp (speed-to-lead, distribuição de tiers, health dos webhooks, taxa de órfãos), (5) Relatório semanal de performance do modelo com Precision/Recall por tier e recomendações de calibração, (6) Score Card Model versionado com histórico de performance por versão e changelog de calibrações

## Trigger

Orion e o controlador central do pipeline de leads. Recebe notificacao de novo lead de qualquer fonte, coordena a cascata de enriquecimento e scoring, decide o tier do lead (Hot/Warm/Cold/Unfit) com base no Score composto, e delega o roteamento ao Vector. Monitora continuamente a saude do modelo: detecta drift de conversao, aciona recalibracao quando a taxa de acerto cai abaixo de threshold, e escala para HITL quando um lead e ambiguo (score entre 65-80 e sinais contraditories). Opera no padrao orchestrator-worker: nunca executa enriquecimento ou envio diretamente, apenas orquestra, prioriza e sintetiza. Persona: metodico, orientado a velocidade sem abrir mao de qualidade, obsessivo com speed-to-lead.

## Knowledge base (o que o executor consulta)

- HubSpot CRM
- campo customizado Lead Score (0-100), Tier (Hot/Warm/Cold/Unfit), Score Breakdown (JSON), SDR Designado, Fonte Normalizada
- webhook de novo contato para Scout
- criação automática de deal por Vector para leads Warm+
- ativação de sequences para Warm
- Meta Lead Ads API
- webhook de novo lead de campanhas Facebook/Instagram Lead Ads para Scout
- Google Ads Lead Form Extensions
- webhook de novo lead de formulários Google Ads para Scout
- LinkedIn Lead Gen Forms
- webhook de novo lead de anúncios LinkedIn para Scout
- WhatsApp Business API (via Patagon AI ou Leadsales)
- evento de novo contato iniciado para Scout
- envio de mensagem de primeiro contato automatizado para leads Warm (Vector aciona)
- waterfall enrichment primary engine, ICP custom tables, intent signals de 100+ fontes (via MCP)
- Apollo.io
- enriquecimento complementar de contatos e prospecting (via MCP ou API direta)
- enriquecimento GDPR-compliant para contatos internacionais (via API)
- Apify MCP
- scraping de perfil LinkedIn para validacao de cargo/empresa quando email disponıvel
- prova de trabalho: task automatica por lead Hot com brief completo, dashboard de KPIs em tempo real, relatorio semanal de performance, formulario de feedback dos SDRs
- alertas de lead Hot sem contato (Warning/Critical), notificação push para SDR designado, relatório diário de pipeline para Sales Lead
- orquestracao de workflows de normalizacao de leads de fontes nao-padrao e notificacoes complexas (complemento no-code para integrações customizadas)
- observabilidade OTEL de todos os agents, rastreamento de latência de scoring (meta < 60s), quality gates (dev 70% / staging 85% / prod 95% task success), log de todas as decisões de roteamento para auditoria
- Google Sheets / Looker Studio
- dashboard executivo de KPIs (speed-to-lead, conversão por tier, volume por fonte) para CMO e Sales Lead

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Critique 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pipeline de scoring e roteamento de leads em produção entregando: (1) Score Card automático por lead (Fit + Intent + Composto + Tier + Reasoning narrativo) pub…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Critique 2 registrado
- [ ] Gate HITL respeitado: Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa…
- [ ] Gate HITL respeitado: Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de p…
- [ ] Gate HITL respeitado: Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) prop…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique de… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerte… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Desvio crítico de performance detectado por Critique — quando Precision@Hot cai abaixo de 40% ou Recall cai abaixo de 50%, o squad entra em modo de revisão e n… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Ativação de nova fonte de leads (novo canal, novo formulário) — Scout não ativa fonte nova automaticamente, requer validação do schema de campos e regras de no… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Ajuste de capacidade de SDR na Routing Matrix — quando SDR entra em ferias ou saı da empresa, Vector nao rebalanceia automaticamente sem confirmacao do Sales L… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Critique 2 | BLOQUEIA entrega |

## Handoff

- **to:** Scout
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
