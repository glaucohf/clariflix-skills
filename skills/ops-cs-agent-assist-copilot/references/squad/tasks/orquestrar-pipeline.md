---
task: compassPipeline()
responsavel: "Compass"
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
    descricao: "Por atendimento concluido: Task no ClickUp com (1) ID do ticket e atendente responsavel, (2) intencoes detectadas na conversa com confianca scores, (3) numero de sugestoes exibidas vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "aceitas vs"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "rejeitadas vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "editadas, (4) resumo de resolucao gerado pelo Memo, (5) alertas do Shield disparados (se houver), (6) AHT do atendimento, (7) flags de next-step do Lumen acionadas, (8) timestamp de cada step do pipeline Compass"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Dashboard Langfuse com: adoption rate em tempo real por atendente e por intencao, AHT trending semanal, critic rejection breakdown por dimensao, top macros aceitas e rejeitadas, mapa de heat das violacoes do Shield por tipo"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Relatorio semanal do Echo no Slack com analise de qualidade das sugestoes e recomendacoes de melhoria"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe cada nova mensagem do cliente via webhook do helpdesk (Zendesk/Intercom), identifica o estado atual da conversa (abertura, medio, resolucao, escalonamento), enriquece com contexto da conta (da…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Prism antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar conscientemente ou corrigir"
    - "[ ] HITL: Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — responda manualmente'"
    - "[ ] HITL: Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico"
    - "[ ] HITL: Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromisso"
    - "[ ] HITL: Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente"
---

# Orquestrar Pipeline do Copíloto do Agente Humano

**Task ID:** `compassPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Copíloto do Agente Humano |
| **status** | `pending` |
| **responsible_executor** | Compass (Compass — Orchestrator de Assist em Tempo Real) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe cada nova mensagem do cliente via webhook do helpdesk (Zendesk/Intercom), identifica o estado atual da conversa (abertura, medio, resolucao, escalonamento), enriquece com contexto da conta (dados do CRM, historico de tickets, plano e MRR), classifica a intencao primaria com confianca score, distribui para o worker especializado correto, aguarda o draft da sugestao, aciona o Critic para validacao, formata a sugestao para exibicao no overlay do atendente com metadados (fonte, confianca, macro-base) e registra o evento no ClickUp e Langfuse. Gerencia o fluxo sem bloquear o atendente — toda operacao deve completar em < 3 segundos.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Por atendimento concluido: Task no ClickUp com (1) ID do ticket e atendente responsavel, (2) intencoes detectadas na conversa com confianca scores, (3) numero de sugestoes exibidas vs
- aceitas vs
- rejeitadas vs
- editadas, (4) resumo de resolucao gerado pelo Memo, (5) alertas do Shield disparados (se houver), (6) AHT do atendimento, (7) flags de next-step do Lumen acionadas, (8) timestamp de cada step do pipeline Compass
- Dashboard Langfuse com: adoption rate em tempo real por atendente e por intencao, AHT trending semanal, critic rejection breakdown por dimensao, top macros aceitas e rejeitadas, mapa de heat das violacoes do Shield por tipo
- Relatorio semanal do Echo no Slack com analise de qualidade das sugestoes e recomendacoes de melhoria

## Trigger

Recebe cada nova mensagem do cliente via webhook do helpdesk (Zendesk/Intercom), identifica o estado atual da conversa (abertura, medio, resolucao, escalonamento), enriquece com contexto da conta (dados do CRM, historico de tickets, plano e MRR), classifica a intencao primaria com confianca score, distribui para o worker especializado correto, aguarda o draft da sugestao, aciona o Critic para validacao, formata a sugestao para exibicao no overlay do atendente com metadados (fonte, confianca, macro-base) e registra o evento no ClickUp e Langfuse. Gerencia o fluxo sem bloquear o atendente — toda operacao deve completar em < 3 segundos.

## Knowledge base (o que o executor consulta)

- Zendesk (webhook de nova mensagem + API de ticket + campo de resolução)
- helpdesk primário
- Intercom (webhook conversation.message.created + Fin AI overlay API)
- helpdesk alternativo
- ClickUp (Brain2 / MCP server)
- task por atendimento como prova de trabalho espelhando AIOX
- CRM: HubSpot ou Salesforce
- dados de conta, MRR, renovação, notas do CSM via MCP
- CS Platform: ChurnZero / Gainsight / Custify
- health score, uso do produto, alertas de churn
- ERP / OMS
- consulta de pedidos, status, histórico de compras via MCP customizado
- Supabase / Postgres
- cache de contexto de conta, log de sugestões e feedbacks, macros vetorizadas
- observabilidade OTEL, tracing de cada step do pipeline, adoption rate, AHT delta, quality gates
- alertas de SLA em risco, relatorio semanal do Echo, alertas de macro com alta rejection rate
- Claude Agent SDK / LangGraph
- orquestração do pipeline multi-agente com latência controlada
- Widget de overlay no Zendesk/Intercom (extensão de browser ou app interno)
- UI de exibição das sugestões e coleta de feedback do atendente
- Webhook de composição do helpdesk
- captura rascunho do atendente para o Shield em tempo real

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Prism antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Por atendimento concluido: Task no ClickUp com (1) ID do ticket e atendente responsavel, (2) intencoes detectadas na conversa com confianca scores, (3) numero…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Prism registrado
- [ ] Gate HITL respeitado: Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atenden…
- [ ] Gate HITL respeitado: Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'int…
- [ ] Gate HITL respeitado: Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso esp…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar co… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — resp… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromis… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Vault retorna flag 'cliente_em_risco_de_churn' (health score < 50): todas as sugestões do Scribe são marcadas com indicador visual e Lumen adiciona sugestão de… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Echo detecta que uma macro tem rejection_rate > 60% por 7 dias consecutivos: dispara alerta para gestor de CS no Slack pedindo revisão manual da macro antes de… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Shield detecta promessa de desconto ou benefício financeiro no rascunho do atendente: alerta de policy_violation com valor exato do limite autorizado e botão d… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Prism | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
