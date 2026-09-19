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
    descricao: "Pipeline Scorecard em tempo real (dashboard ClickUp + CRM): rank dos leads por probabilidade de fechamento, fila do dia por rep, alertas de risco de deal, forecast semanal com intervalo de confiança"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato verificável por task: cada lead processado gera um Score Object rastreável no Langfuse com trace completo (features usadas, peso de cada feature, score anterior vs atual, ação recomendada, canal selecionado)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Briefing de Lead para cada Hot lead gerado pelo Nexus e aprovado via HITL"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central que recebe eventos do pipeline (novo lead, mudanca de estagio, engajamento, sinal de intencao), decompoe em subtarefas, roteia para workers especializados, mantem o estado do fun…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes do disparo. SLA de aprovação: 2h."
    - "[ ] HITL: HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do Closer ou Gerente Comercial."
    - "[ ] HITL: HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos."
    - "[ ] HITL: HITL-4 (L3): Alerta de deal em risco alto — gestor recebe notificação e deve confirmar qual ação tomar (intervir diretamente, escalar para diretor, ajustar proposta) antes de qualquer comunicação automatizada."
    - "[ ] HITL: HITL-5 (L2): Ajuste manual de score por SDR — SDR pode adicionar nota qualitativa (ex: 'falei com o CEO, orçamento confirmado') que sobe o score manualmente, com registro no log de auditoria."
---

# Orquestrar Pipeline do Lead Scoring Preditivo e Priorização

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Lead Scoring Preditivo e Priorização

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Lead Scoring Preditivo e Priorização |
| **status** | `pending` |
| **responsible_executor** | Orion (Maestro Comercial (Órion)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central que recebe eventos do pipeline (novo lead, mudanca de estagio, engajamento, sinal de intencao), decompoe em subtarefas, roteia para workers especializados, mantem o estado do funil no CRM e aciona HITL quando score ou acao ultrapassam threshold de autonomia. Opera em loop continuo — nao espera pedido, monitora o pipeline proativamente.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pipeline Scorecard em tempo real (dashboard ClickUp + CRM): rank dos leads por probabilidade de fechamento, fila do dia por rep, alertas de risco de deal, forecast semanal com intervalo de confiança
- Artefato verificável por task: cada lead processado gera um Score Object rastreável no Langfuse com trace completo (features usadas, peso de cada feature, score anterior vs atual, ação recomendada, canal selecionado)
- Briefing de Lead para cada Hot lead gerado pelo Nexus e aprovado via HITL

## Trigger

Orquestrador central que recebe eventos do pipeline (novo lead, mudanca de estagio, engajamento, sinal de intencao), decompoe em subtarefas, roteia para workers especializados, mantem o estado do funil no CRM e aciona HITL quando score ou acao ultrapassam threshold de autonomia. Opera em loop continuo — nao espera pedido, monitora o pipeline proativamente.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível) ou Pipedrive
- source of truth para lead e deal data, destino de todos os score writes e activity logs
- WhatsApp Business API: Gupshup ou AiSensy
- canal de outreach e recepção de sinais de engajamento (mensagem lida, respondida)
- Enriquecimento: Apollo.io (275M+ contatos) via API
- firmográficos, contatos adicionais, tech stack
- Enriquecimento complementar: Clay
- workflows de enriquecimento multi-fonte com waterfall
- Ads / Intent Signals: Facebook Lead Ads, Google Ads
- webhooks de novos leads com UTMs completos
- Gestão de tarefas: ClickUp
- Fila_do_Dia dos reps, proof-of-work por task, registro de artefatos verificáveis
- Comunicação interna: Slack
- alertas de deals em risco, leads Hot sem contato, aprovações HITL
- Calendário: Google Calendar
- disponibilidade dos reps para roteamento e agendamento
- Observabilidade: Langfuse (OTEL)
- evals de qualidade dos agentes, quality gates por ambiente, traces de todas as chamadas LLM
- Orquestração: LangGraph + Claude Agent SDK
- controle de estado do pipeline, workflows determinísticos
- Armazenamento de features: PostgreSQL/Supabase
- Feature Store com histórico de scores e features por lead

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Argus antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pipeline Scorecard em tempo real (dashboard ClickUp + CRM): rank dos leads por probabilidade de fechamento, fila do dia por rep, alertas de risco de deal, fore…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes d…
- [ ] Gate HITL respeitado: HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do…
- [ ] Gate HITL respeitado: HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL-1 (L3): Envio de qualquer mensagem para lead categorizado como Hot — SDR humano deve revisar e aprovar o briefing e a mensagem antes do disparo. SLA de ap… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL-2 (L3): Qualquer ação de outreach em conta estratégica (deal acima de threshold de valor configurável, ex R$50k) — requer aprovação do Closer ou Gerente C… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL-3 (L3): Re-scoring que resulta em Disqualificado — humano confirma antes de arquivar o lead no CRM para evitar falsos negativos. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL-4 (L3): Alerta de deal em risco alto — gestor recebe notificação e deve confirmar qual ação tomar (intervir diretamente, escalar para diretor, ajustar pro… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL-5 (L2): Ajuste manual de score por SDR — SDR pode adicionar nota qualitativa (ex: 'falei com o CEO, orçamento confirmado') que sobe o score manualmente, c… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL-6 (L1): Calibração mensal do modelo de scoring — analista de RevOps revisa os feature weights sugeridos pelo sistema e aprova ou ajusta antes do re-treino. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
