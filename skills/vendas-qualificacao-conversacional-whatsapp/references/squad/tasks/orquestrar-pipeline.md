---
task: maestroComercialPipeline()
responsavel: "Maestro Comercial"
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
    descricao: "Dossiê de Qualificação Acionável: para cada lead processado, o squad entrega ao closer um artefato padronizado contendo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(1) qualification_scorecard.json com score 0-100 por dimensão BANT/MEDDIC, (2) conversation_log completo anotado com as respostas-chave do lead, (3) resumo executivo em 5 bullets (dor principal, budget confirmado, decisor identificado, urgência, objeção principal), (4) slot de reunião agendado ou próximo passo recomendado, (5) deal criado/atualizado no HubSpot com todos os campos preenchidos"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato linkado no ClickUp como prova de trabalho verificável"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe cada sinal de novo lead (webhook de ad, mensagem de WhatsApp, form fill, upload de lista), decompõe em subtarefas ordenadas (enriquecer -> qualificar -> pontuar -> rotear -> agendar), mantém o…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Censor Comercial antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comercial aprova batch antes do disparo."
    - "[ ] HITL: HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por desconto, Vera responde 'vou verificar com nosso especialista' e escala ao closer via notificação imediata."
    - "[ ] HITL: HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes de qualquer ação automática adicional. Closer decide se assume a conversa ou deixa o squad continuar."
    - "[ ] HITL: HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada."
    - "[ ] HITL: HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor responde o que fazer; resposta é adicionada ao playbook para aprendizado."
---

# Orquestrar Pipeline do Qualificação Conversacional

**Task ID:** `maestroComercialPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Qualificação Conversacional |
| **status** | `pending` |
| **responsible_executor** | Maestro Comercial (Maestro Comercial — Orion) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe cada sinal de novo lead (webhook de ad, mensagem de WhatsApp, form fill, upload de lista), decompõe em subtarefas ordenadas (enriquecer -> qualificar -> pontuar -> rotear -> agendar), mantém o estado do funil por lead_id no CRM, decide qual worker acionar em cada etapa, consolida o dossiê final e decide o roteamento (closer / nurture / descarte). Opera em modo reativo (event-driven por webhook) e proativo (varre pipeline em aberto a cada 4h para reativar leads travados).

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Dossiê de Qualificação Acionável: para cada lead processado, o squad entrega ao closer um artefato padronizado contendo
- (1) qualification_scorecard.json com score 0-100 por dimensão BANT/MEDDIC, (2) conversation_log completo anotado com as respostas-chave do lead, (3) resumo executivo em 5 bullets (dor principal, budget confirmado, decisor identificado, urgência, objeção principal), (4) slot de reunião agendado ou próximo passo recomendado, (5) deal criado/atualizado no HubSpot com todos os campos preenchidos
- Artefato linkado no ClickUp como prova de trabalho verificável

## Trigger

Recebe cada sinal de novo lead (webhook de ad, mensagem de WhatsApp, form fill, upload de lista), decompõe em subtarefas ordenadas (enriquecer -> qualificar -> pontuar -> rotear -> agendar), mantém o estado do funil por lead_id no CRM, decide qual worker acionar em cada etapa, consolida o dossiê final e decide o roteamento (closer / nurture / descarte). Opera em modo reativo (event-driven por webhook) e proativo (varre pipeline em aberto a cada 4h para reativar leads travados).

## Knowledge base (o que o executor consulta)

- WhatsApp Business API via Gupshup ou AiSensy (envio/recepção de mensagens, webhooks de status)
- HubSpot CRM via MCP HubSpot oficial (leitura e escrita de contatos, deals, propriedades customizadas, activities)
- Google Calendar ou Calendly API (disponibilidade de closers, criação de eventos, webhooks de cancelamento)
- Meta Ads Lead Ads (webhook de novo lead -> N8N -> Orchestrator)
- Apollo.io ou Clay (enriquecimento de dados B2B: empresa, cargo, contato)
- N8N como middleware de webhook (recebe sinais de múltiplas fontes e normaliza payload para o Orchestrator)
- ClickUp (artefatos verificáveis por task: scorecards, conversation logs, relatórios de higiene e intelligence)
- Langfuse OTEL (observabilidade de todas as chamadas LLM: latência, tokens, task success rate por agente, evals customizados)
- LangGraph (orquestração do grafo de agentes com estado persistente por lead_id)
- Claude API
- Opus 4 para Orchestrator e Critic
- Sonnet 4 para workers (balanço custo/performance)
- Píxel de site do cliente (sinais de reativação para o Lázaro via webhook de evento personalizado)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Censor Comercial antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossiê de Qualificação Acionável: para cada lead processado, o squad entrega ao closer um artefato padronizado contendo
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Censor Comercial registrado
- [ ] Gate HITL respeitado: HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputaci…
- [ ] Gate HITL respeitado: HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se l…
- [ ] Gate HITL respeitado: HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL-1 (L3): Aprovação humana obrigatória antes de qualquer mensagem proativa para lista importada (cold outbound) — risco legal e reputacional. Gestor comerci… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL-2 (L3): Concessão de desconto ou alteração de condições comerciais mencionadas na conversa — Vera nunca cita preço sem aprovação. Se lead pergunta por des… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL-3 (L3): Lead VIP (score >= 85 + empresa > 200 funcionários ou deal value estimado > R$100k) — Orchestrator notifica closer diretamente via WhatsApp antes… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL-4 (L2): Reagendamento após segunda recusa do lead — Tempo tenta 2x automaticamente; na 3ª recusa, notifica o closer para abordagem manual personalizada. | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL-5 (L2): Objecão não mapeada detectada pelo Veto na conversa da Vera — Vera pausa, escala notificação ao gestor comercial com contexto completo. Gestor res… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL-6 (L1): Relatório semanal do Eco com sugestões de ajuste de prompt — gestor revisa e aprova antes de qualquer alteração ser aplicada nos prompts da Vera o… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Censor Comercial | BLOQUEIA entrega |

## Handoff

- **to:** Investigador de Lead
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
