---
task: sentinelaMorPersonaVitorAnalistaSeniorDeOperacoesComObsessaoPorSlaPipeline()
responsavel: "Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA"
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
    descricao: "Artefato de prova de trabalho auditável e verificável no ClickUp: para cada ticket com SLA ativo, campo 'sla_monitor_log' com histórico de todos os ciclos de avaliação (timestamp, breach_probability_score, risk_status, ação_tomada)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para cada escalonamento proativo, sub-task vinculada ao ticket-pai com: escalation_timestamp (anterior ao sla_deadline), triggered_by (Cronos score que atingiu threshold), notified_parties (supervisor + canal), recommended_action, resolution_outcome (breach evitado: sim/não, preenchido ao fechar o ticket)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard de SLA Health em tempo real no ClickUp mostrando: breach_rate_7d, avg_antecedencia_horas, sla_compliance_pct por tier de cliente, top-3 causas de risco esta semana"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Relatório semanal do Histos com tendências e recomendações"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Este artefato é o que o cliente apresenta ao seu board para provar que SLA está sendo gerenciado proativamente"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "não de forma reativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestra o ciclo contínuo de monitoramento: a cada 15 minutos, varre todos os tickets abertos com SLA ativo, distribui para workers especializados em paralelo, consolida scores de risco, decide se e…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Cético de SLA antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade baixa (interrompe o fluxo do agente atual)."
    - "[ ] HITL: Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders. Ação de alto impacto e irreversível em termos de alarme organizacional."
    - "[ ] HITL: Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes do envio. Toda comunicação com cliente é revisada por humano."
    - "[ ] HITL: Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. Ocorre quando dados são ambíguos ou incompletos."
    - "[ ] HITL: Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para avaliação manual do risco de breach. Cronos não especula sem dados."
---

# Orquestrar Pipeline do SLA & Health Monitoring Operacional

**Task ID:** `sentinelaMorPersonaVitorAnalistaSeniorDeOperacoesComObsessaoPorSlaPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de SLA & Health Monitoring Operacional

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do SLA & Health Monitoring Operacional |
| **status** | `pending` |
| **responsible_executor** | Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA (Sentinela-Mor (persona: Vítor, analista sênior de operações com obsessão por SLA — ex-NOC de telco que nunca perdeu um uptime em 8 anos)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestra o ciclo contínuo de monitoramento: a cada 15 minutos, varre todos os tickets abertos com SLA ativo, distribui para workers especializados em paralelo, consolida scores de risco, decide se escalonamento é necessário e aciona a árvore de escalada. Vítor é cirúrgico e nunca alarmista — só escala quando o modelo diz que o risco é real. Mantém o state machine de cada ticket (VERDE/AMARELO/VERMELHO/BREACH) e garante que cada decisão de escalonamento seja registrada como prova de trabalho auditável no ClickUp. Gerencia a agenda de execução (15min por padrão, configurável), retries em caso de falha de integração e relatório de saúde do próprio squad.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Artefato de prova de trabalho auditável e verificável no ClickUp: para cada ticket com SLA ativo, campo 'sla_monitor_log' com histórico de todos os ciclos de avaliação (timestamp, breach_probability_score, risk_status, ação_tomada)
- Para cada escalonamento proativo, sub-task vinculada ao ticket-pai com: escalation_timestamp (anterior ao sla_deadline), triggered_by (Cronos score que atingiu threshold), notified_parties (supervisor + canal), recommended_action, resolution_outcome (breach evitado: sim/não, preenchido ao fechar o ticket)
- Dashboard de SLA Health em tempo real no ClickUp mostrando: breach_rate_7d, avg_antecedencia_horas, sla_compliance_pct por tier de cliente, top-3 causas de risco esta semana
- Relatório semanal do Histos com tendências e recomendações
- Este artefato é o que o cliente apresenta ao seu board para provar que SLA está sendo gerenciado proativamente
- não de forma reativa

## Trigger

Orquestra o ciclo contínuo de monitoramento: a cada 15 minutos, varre todos os tickets abertos com SLA ativo, distribui para workers especializados em paralelo, consolida scores de risco, decide se escalonamento é necessário e aciona a árvore de escalada. Vítor é cirúrgico e nunca alarmista — só escala quando o modelo diz que o risco é real. Mantém o state machine de cada ticket (VERDE/AMARELO/VERMELHO/BREACH) e garante que cada decisão de escalonamento seja registrada como prova de trabalho auditável no ClickUp. Gerencia a agenda de execução (15min por padrão, configurável), retries em caso de falha de integração e relatório de saúde do próprio squad.

## Knowledge base (o que o executor consulta)

- ClickUp (Brain2 / Autopilot Agents + API MCP): hub central do squad
- campos customizados de SLA (sla_deadline, breach_probability, risk_status, sla_monitor_log), sub-tasks de escalonamento, dashboard de KPIs em tempo real, view de tickets-em-risco filtrada por VERMELHO/AMARELO
- Zendesk / Intercom (via MCP server): sistemas de helpdesk de onde o Radar coleta tickets em tempo real via API
- campo de SLA deadline lido nativamente das configurações de SLA do helpdesk
- Slack (Webhooks + Slack MCP): canal dedicado '#sla-monitor-alertas' para notificações do Alarme com template estruturado (ticket, deadline, score, link direto) + canal '#sla-war-room' para P1 críticos + DM para supervisor de plantão
- HubSpot / Salesforce CRM (via MCP): dados de tier do cliente, ARR, data de renovação e cláusulas de SLA contratual
- alimentam o cálculo de prioridade do Cronos e a definição de threshold de escalonamento por conta
- ChurnZero / Custify / Chargebee: health score do cliente e status de renovação
- agravante de risco quando cliente em renovação tem ticket em breach risk (complexity multiplier adicional)
- Supabase / Postgres: banco de dados de estado persistente do squad
- log de auditoria de todos os ciclos, histórico de breach/não-breach para recalibração do Cronos pelo Histos, pesos do modelo preditivo, perfis de velocidade dos agentes
- Langfuse (OTEL): observabilidade completa do squad
- tracing de cada ciclo de 15min (latência total, tokens por agente, scores gerados, decisões tomadas), quality gates por ambiente (dev 70% / staging 85% / prod 95% de acurácia preditiva), dashboard de drift do modelo
- Google Calendar / Outlook Calendar (via API): disponibilidade dos supervisores de plantão para o Alarme saber quem notificar em qual escalonamento (integração com escala de plantão da equipe)
- PagerDuty / incident.io (opcional, para clientes com stack de AIOps): integração para tickets P1 que viram incidentes
- o Alarme pode criar um PagerDuty incident além do war-room no ClickUp
- MCP Servers (camada de integração universal): MCP ClickUp, MCP Zendesk/Intercom, MCP CRM
- abstraem chamadas de API para os workers e garantem rate limiting seguro

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Cético de SLA antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Artefato de prova de trabalho auditável e verificável no ClickUp: para cada ticket com SLA ativo, campo 'sla_monitor_log' com histórico de todos os ciclos de a…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Cético de SLA registrado
- [ ] Gate HITL respeitado: Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executa…
- [ ] Gate HITL respeitado: Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar mú…
- [ ] Gate HITL respeitado: Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Escalonamento com reatribuição de ticket (Alarme quer mudar o agente responsável): L3 — supervisor confirma a reatribuição antes de executar. Reversibilidade b… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Convocação de war-room P1 (breach_probability >90%): L3 — ops manager confirma abertura de canal de incidentes antes do Alarme notificar múltiplos stakeholders… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Escalonamento para C-level ou cliente final (ticket de cliente enterprise em risco de breach contratual com multa): L3 — CS Manager aprova a comunicação antes… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Cassandra bloqueia um escalonamento por inconsistência no score: humano (supervisor ou ops lead) revisa o caso manualmente antes de decidir se escala ou não. O… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Novo tipo de ticket sem histórico suficiente para calibrar Cronos (confidence_level=LOW): Sentinela-Mor pausa a decisão automática e notifica supervisor para a… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Histos detecta breach rate semanal acima do threshold crítico: relatório é revisado por ops manager antes de publicação, que decide se aciona revisão de proces… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Recalibração mensal do modelo do Cronos (Histos gera novo dataset): pesos atualizados são revisados por ops lead antes de ir para produção. Mudança no modelo p… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Cético de SLA | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
