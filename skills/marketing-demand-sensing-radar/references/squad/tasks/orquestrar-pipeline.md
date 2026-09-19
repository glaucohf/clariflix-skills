---
task: radarPipeline()
responsavel: "Radar"
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
    descricao: "Demand Intelligence Report semanal entregue no ClickUp contendo: (1) Hot Accounts da semana com Signal Score, breakdown de sinais detectados e Context Card por conta, (2) Playbooks disparados com status (aprovados, enviados, respostas obtidas), (3) Dashboard de lead-time de antecipação e win-rate em contas sinalizadas, (4) Macro-Trend Report com 3-5 tendências setoriais e janela de oportunidade estimada, (5) ROI por categoria de sinal (qual tipo de sinal está gerando mais pipeline), (6) Pipeline atribuído ao radar no período, (7) Alertas de recalibração de threshold com recomendação de ajuste para aprovação do CMO"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Decompõe a meta de antecipação em ciclos de monitoramento, calibração e ativação. Recebe o feed consolidado de sinais de Pulse, decide quais contas sobem de tier (Warm->Hot), qual playbook é mais ade…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sigma 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)"
    - "[ ] HITL: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)"
    - "[ ] HITL: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)"
    - "[ ] HITL: Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)"
    - "[ ] HITL: Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)"
---

# Orquestrar Pipeline do Demand Sensing Radar

**Task ID:** `radarPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Demand Sensing Radar |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Orquestrador de Demand Sensing) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Decompõe a meta de antecipação em ciclos de monitoramento, calibração e ativação. Recebe o feed consolidado de sinais de Pulse, decide quais contas sobem de tier (Warm->Hot), qual playbook é mais adequado por tipo de sinal, e orquestra a sequência correta de agentes workers. Não executa monitoramento ou envio diretamente — orquestra, prioriza e decide. Persona: cirúrgico, obsessivo com timing, não dispara playbook sem evidência de sinal múltiplo (pelo menos 2 categorias de sinal convergentes para uma conta). Opera padrão orchestrator-worker com gate de Sigma antes de qualquer ação externa irreversível.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Demand Intelligence Report semanal entregue no ClickUp contendo: (1) Hot Accounts da semana com Signal Score, breakdown de sinais detectados e Context Card por conta, (2) Playbooks disparados com status (aprovados, enviados, respostas obtidas), (3) Dashboard de lead-time de antecipação e win-rate em contas sinalizadas, (4) Macro-Trend Report com 3-5 tendências setoriais e janela de oportunidade estimada, (5) ROI por categoria de sinal (qual tipo de sinal está gerando mais pipeline), (6) Pipeline atribuído ao radar no período, (7) Alertas de recalibração de threshold com recomendação de ajuste para aprovação do CMO

## Trigger

Decompõe a meta de antecipação em ciclos de monitoramento, calibração e ativação. Recebe o feed consolidado de sinais de Pulse, decide quais contas sobem de tier (Warm->Hot), qual playbook é mais adequado por tipo de sinal, e orquestra a sequência correta de agentes workers. Não executa monitoramento ou envio diretamente — orquestra, prioriza e decide. Persona: cirúrgico, obsessivo com timing, não dispara playbook sem evidência de sinal múltiplo (pelo menos 2 categorias de sinal convergentes para uma conta). Opera padrão orchestrator-worker com gate de Sigma antes de qualquer ação externa irreversível.

## Knowledge base (o que o executor consulta)

- motor primário de intent data agregado de 100+ fontes, waterfall enrichment de contas, job posting tracking, technographics e sinais de funding
- Bombora / 6sense
- intent data B2B por tópico específico, surge score por conta e segmento
- HubSpot CRM
- campo customizado de Signal Score por conta, propriedade de ùltimo sinal detectado, webhook de stage change para atribuiçạ̃o, task automática para SDR/AE quando conta sobe para Hot
- LinkedIn Sales Navigator / LinkedIn API
- company updates, mudanças de liderança, job postings críticos, atividade de contatos-alvo
- SEMrush Enterprise
- monitoramento de picos de busca orgânica por keyword de problema, share of voice por segmento, menções em AI Overviews
- Crunchbase / PitchBook (via MCP ou webhook)
- alertas de funding rounds, M&A, expansão geográfica
- Google Ads + Meta Ads – ativação de campanhas de retargeting disparadas por Demand Surge Playbook (via aprovação HITL)
- ClickUp – prova de trabalho: task automática por conta Hot identificada, dashboard de lead-time de antecipação, registro de playbooks disparados com status
- n8n – orquestração de workflows de monitoramento, webhooks de sinais e notificações no-code (camada complementar de automação)
- Langfuse – observabilidade OTEL de todos os agents, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de sinal
- Slack – alertas em tempo real de Hot Accounts para canal #demand-radar, notificações de Sigma BLOCKED para revisão humana urgente
- WhatsApp Business API (via Patagon AI / BotPenguin) – canal de outreach pós-aprovação Sigma para playbooks onde WhatsApp é o canal de preferência do ICP

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Sigma 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Demand Intelligence Report semanal entregue no ClickUp contendo: (1) Hot Accounts da semana com Signal Score, breakdown de sinais detectados e Context Card por…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sigma 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o…
- [ ] Gate HITL respeitado: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cad…
- [ ] Gate HITL respeitado: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squ… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprova… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3) | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Pulse
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
