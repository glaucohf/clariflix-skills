---
task: orquestradorComercialDeVozPipeline()
responsavel: "Orquestrador Comercial de Voz"
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
    descricao: "Artefato principal por ciclo de operação: Relatório Diário de Discagem (JSON + dashboard) contendo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "leads discados, taxa de conexão do dia, leads qualificados com campos BANT preenchidos, reuniões agendadas, calls com flag de HITL pendente, e score de qualidade médio"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefatos secundários: Dossiês de Lead (pré-call), Transcrições e Gravações de Call (pós-call), Relatório Semanal de Conversation Intelligence, e Fila de Discagem Priorizada pelo Radar Agent"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Todos os artefatos rastreados no ClickUp com link direto ao registro do CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe o sinal de lead (inbound form, lista de prospectos, intent data), decompoem em subtarefas, roteia workers especializados, mantém estado do funil no CRM, decide escalação para humano e consolid…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Filtro 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3)."
    - "[ ] HITL: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3)."
    - "[ ] HITL: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3)."
    - "[ ] HITL: Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3)."
    - "[ ] HITL: Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation)."
---

# Orquestrar Pipeline do Voz para Cold Calling e Discovery

**Task ID:** `orquestradorComercialDeVozPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Voz para Cold Calling e Discovery |
| **status** | `pending` |
| **responsible_executor** | Orquestrador Comercial de Voz (Maestro (Orquestrador Comercial de Voz)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o sinal de lead (inbound form, lista de prospectos, intent data), decompoem em subtarefas, roteia workers especializados, mantém estado do funil no CRM, decide escalação para humano e consolida resultado de cada interação em artefato verificável no ClickUp. Opera em modo L2: humano define regras e limites, Maestro executa e orquestra dentro deles.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Artefato principal por ciclo de operação: Relatório Diário de Discagem (JSON + dashboard) contendo
- leads discados, taxa de conexão do dia, leads qualificados com campos BANT preenchidos, reuniões agendadas, calls com flag de HITL pendente, e score de qualidade médio
- Artefatos secundários: Dossiês de Lead (pré-call), Transcrições e Gravações de Call (pós-call), Relatório Semanal de Conversation Intelligence, e Fila de Discagem Priorizada pelo Radar Agent
- Todos os artefatos rastreados no ClickUp com link direto ao registro do CRM

## Trigger

Recebe o sinal de lead (inbound form, lista de prospectos, intent data), decompoem em subtarefas, roteia workers especializados, mantém estado do funil no CRM, decide escalação para humano e consolida resultado de cada interação em artefato verificável no ClickUp. Opera em modo L2: humano define regras e limites, Maestro executa e orquestra dentro deles.

## Knowledge base (o que o executor consulta)

- Vapi ou Rétell AI (plataforma de agente de voz sub-600ms)
- Deepgram (STT
- Speech-to-Text de baixa latência)
- ElevenLabs (TTS
- Text-to-Speech com voz personalizada)
- HubSpot CRM (MCP disponível
- leitura e escrita de leads, deals, activities)
- Google Calendar ou Outlook (agendamento e gestão de disponibilidade do closer)
- WhatsApp Business API via Gupshup ou AiSensy (confirmações, lembretes, nurture)
- Apollo.io (enriquecimento de leads
- 275M+ contatos)
- Clay (enriquecimento dinâmico e waterfall de dados)
- ClickUp (gestão de tarefas e artefatos verificáveis por story)
- Langfuse (observabilidade OTEL, evals e quality gates por fase)
- LangGraph (orquestração do grafo de estados conversacional do Vox Agent)
- Twilio ou Vonage (gateway de telefonia para discagem programática)
- Google Sheets ou Airtable (lista de prospectos e relatórios para clientes sem CRM robusto)
- Slack ou Teams (notificações de leads qualificados e alertas de HITL para gestor comercial)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Filtro 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Artefato principal por ciclo de operação: Relatório Diário de Discagem (JSON + dashboard) contendo
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Filtro 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3).
- [ ] Gate HITL respeitado: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3).
- [ ] Gate HITL respeitado: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3).

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3). | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3). | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3). | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3). | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation). | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Confirmação de reagendamento quando prospect cancela reunião pela segunda vez consecutiva (decisão humana sobre continuar ou desqualificar — L3). | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibragem quinzenal de voz e persona do Vox Agent com gestor de vendas (revisão humana de amostras de áudio — L1). | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Filtro 2 | BLOQUEIA entrega |

## Handoff

- **to:** Dossie
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
