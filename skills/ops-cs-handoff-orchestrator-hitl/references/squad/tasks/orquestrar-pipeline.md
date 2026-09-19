---
task: hieronimusPipeline()
responsavel: "Hieronimus"
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
    descricao: "Artefato central"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Decisão de Handoff Registrada: cada interação do squad gera uma task no ClickUp com: (1) action_id único, (2) tier atribuído com justificativa, (3) briefing de contexto empacotado, (4) quem recebeu o handoff e quando, (5) decisão tomada (aprovado/rejeitado/modificado) com timestamp, (6) tempo de resolução, (7) feedback de qualidade da classificação"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard semanal: Relatório de Saúde da Matriz com distribuição de tiers, taxa de acerto, volume de handoffs por tipo, SLA compliance e proposta de recalibração"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central que intercepta TODA acao antes da execucao, aplica a matriz criticidade x reversibilidade, atribui o tier de autonomia correto (L0-L3), e despacha para o worker especializado ou…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vitor antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de qualquer execução, sem exceção."
    - "[ ] HITL: L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cláusula contratual, bloqueio/banimento de usuário."
    - "[ ] HITL: L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que mencione termos legais ou rescisão."
    - "[ ] HITL: L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, respostas à imprensa."
    - "[ ] HITL: Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operações."
---

# Orquestrar Pipeline do Handoff Orchestrator HITL

**Task ID:** `hieronimusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Handoff Orchestrator HITL

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Handoff Orchestrator HITL |
| **status** | `pending` |
| **responsible_executor** | Hieronimus (Hieronimus — O Juiz de Fronteira) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central que intercepta TODA acao antes da execucao, aplica a matriz criticidade x reversibilidade, atribui o tier de autonomia correto (L0-L3), e despacha para o worker especializado ou para o humano com contexto pre-empacotado. Nao executa acoes — decide quem executa e com qual nivel de supervisao. Opera em modo reativo (intercepta chamadas de outros agentes) e proativo (monitora filas de tickets e detecta acoes de alto risco pendentes).

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Artefato central
- Decisão de Handoff Registrada: cada interação do squad gera uma task no ClickUp com: (1) action_id único, (2) tier atribuído com justificativa, (3) briefing de contexto empacotado, (4) quem recebeu o handoff e quando, (5) decisão tomada (aprovado/rejeitado/modificado) com timestamp, (6) tempo de resolução, (7) feedback de qualidade da classificação
- Dashboard semanal: Relatório de Saúde da Matriz com distribuição de tiers, taxa de acerto, volume de handoffs por tipo, SLA compliance e proposta de recalibração

## Trigger

Orquestrador central que intercepta TODA acao antes da execucao, aplica a matriz criticidade x reversibilidade, atribui o tier de autonomia correto (L0-L3), e despacha para o worker especializado ou para o humano com contexto pre-empacotado. Nao executa acoes — decide quem executa e com qual nivel de supervisao. Opera em modo reativo (intercepta chamadas de outros agentes) e proativo (monitora filas de tickets e detecta acoes de alto risco pendentes).

## Knowledge base (o que o executor consulta)

- ClickUp (Brain2/Autopilot Agents)
- hub de tasks, prova de trabalho, registro de cada decisão de handoff como task com checklist, espelho do AIOX
- Claude Agent SDK + LangGraph
- orquestração multi-agente, grafo de decisão do Hieronimus, estados de handoff
- observabilidade OTEL completa, tracing de cada classificação, dashboard de KPIs, quality gates (dev 70% / staging 85% / prod 95%)
- Supabase/Postgres
- estado persistente dos handoffs abertos, log de decisões, banco de treinamento da matriz, histórico de feedbacks
- Slack (Webhooks + Workflow Builder)
- canal #hitl-approvals para briefings L3, botões de ação direta (Aprovar/Rejeitar/Modificar), lembretes de SLA
- Zendesk / Intercom
- webhook de interceptação de ações antes da execução, registro de decisões em tickets, integração com filas de atendimento
- WhatsApp Business API
- interceptação de ações de alto risco iniciadas em atendimentos via WhatsApp antes do envio
- HubSpot / Salesforce
- contexto do cliente (LTV, tier, histórico de contratos, health score) para enriquecer classificação de criticidade
- MCP Servers (camada universal)
- ClickUp MCP, CRM MCP, helpdesk MCP para acesso unificado sem hardcode de API keys

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Vitor antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Artefato central
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vitor registrado
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — hum…
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assin…
- [ ] Gate HITL respeitado: L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qual…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — L3 obrigatório: toda ação com impacto financeiro acima do threshold configurado (ex: reembolso >R$500, crédito >R$200, desconto >20%) — humano aprova antes de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — L3 obrigatório: toda ação irreversível independente de valor — cancelamento definitivo de conta, exclusão de dados, envio de contrato assinado, alteração de cl… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — L3 obrigatório: toda ação com risco legal ou de compliance — compartilhamento de dados com terceiros, resposta a solicitação jurídica, qualquer comunicação que… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — L3 obrigatório: toda ação de impacto reputacional alto — publicação de resposta pública em canal externo (redes sociais, review sites), comunicados de crise, r… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação humana para recalibração da matriz (output do Selene): nenhum threshold de autonomia é alterado sem validação do supervisor CS ou gerente de operaçõe… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão humana quinzenal do Relatório de Auditoria do Vitor: supervisor CS assina o score de qualidade e valida as correções propostas. | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Gate humano na primeira semana pos-implantacao: humano revisa 100% das classificacoes (nao apenas L3) para construir confianca na matriz antes de operar em mod… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Vitor | BLOQUEIA entrega |

## Handoff

- **to:** Cassio
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
