---
task: maestroPipeline()
responsavel: "Maestro"
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
    descricao: "Pacote de Cadências Ativas: conjunto de workflows LangGraph deployados com (1) 4 cadências codificadas (no-show, frio 30/60/90d, proposta fria, nurture longo) com todos os templates de mensagem aprovados pelo Vigia"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "(2) dashboard de pipeline de reativação no ClickUp com tasks verificáveis por lead e por toque"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(3) relatório semanal automático com leads trabalhados, toques realizados, respostas obtidas, reuniões reagendadas e pipeline resgatado em R$"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(4) mapa de calor de performance por canal x segmento x horário para otimização contínua"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe sinais do CRM (lead novo, no-show, lead frio, proposta sem resposta, trigger de intenção) e decompõe em subtarefas para os workers especializados. Mantém o estado completo do lead no funil: úl…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vigia 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou edita antes do envio pelo Volta"
    - "[ ] L3: Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio"
    - "[ ] L3: Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar"
    - "[ ] L3: Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordagem antes de qualquer novo toque"
    - "[ ] HITL: Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão manual"
---

# Orquestrar Pipeline do Follow-up, Nurture e Reativacao

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Follow-up, Nurture e Reativacao |
| **status** | `pending` |
| **responsible_executor** | Maestro (Maestro — Orquestrador de Cadencias) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe sinais do CRM (lead novo, no-show, lead frio, proposta sem resposta, trigger de intenção) e decompõe em subtarefas para os workers especializados. Mantém o estado completo do lead no funil: último toque, canal, resposta, score atual, segmento de cadência ativo. Decide qual cadência ativar, qual worker acionar, e quando escalar para HITL. Coordena a sequência de ações garantindo que nenhum lead receba mensagens conflitantes em paralelo. Registra prova de trabalho em ClickUp após cada ação executada.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote de Cadências Ativas: conjunto de workflows LangGraph deployados com (1) 4 cadências codificadas (no-show, frio 30/60/90d, proposta fria, nurture longo) com todos os templates de mensagem aprovados pelo Vigia
- (2) dashboard de pipeline de reativação no ClickUp com tasks verificáveis por lead e por toque
- (3) relatório semanal automático com leads trabalhados, toques realizados, respostas obtidas, reuniões reagendadas e pipeline resgatado em R$
- (4) mapa de calor de performance por canal x segmento x horário para otimização contínua

## Trigger

Recebe sinais do CRM (lead novo, no-show, lead frio, proposta sem resposta, trigger de intenção) e decompõe em subtarefas para os workers especializados. Mantém o estado completo do lead no funil: último toque, canal, resposta, score atual, segmento de cadência ativo. Decide qual cadência ativar, qual worker acionar, e quando escalar para HITL. Coordena a sequência de ações garantindo que nenhum lead receba mensagens conflitantes em paralelo. Registra prova de trabalho em ClickUp após cada ação executada.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível) ou Pipedrive
- fonte de verdade de leads, status de cadência, score, histórico
- WhatsApp Business API: Gupshup, AiSensy ou Evolution API (open-source)
- canal principal de reativação no Brasil
- Email: SMTP/SendGrid/Amazon SES via HubSpot ou Instantly.ai para sequências frias
- Calendário: Google Calendar / Outlook Calendar / Calendly
- re-agendamento e reminders do Agenda
- Enriquecimento: Clay (orquestrador de enriquecimento) + Apollo (base de contatos)
- alimentam o Sherlock
- Voz: Vapi (<600ms latência) ou Retell AI + ElevenLabs TTS
- para toques de voz em cadências de alto valor
- LinkedIn: LinkedIn Sales Navigator API ou PhantomBuster
- outreach e sinal de mudança de cargo
- Conversation Intelligence: Gong ou Chorus (webhook de transcrição pós-call)
- alimenta o Memento
- Gestão de tarefas / Prova de trabalho: ClickUp (cada ação do squad gera task verificável)
- Observabilidade: Langfuse (OTEL)
- tracking de todas as execuções, quality gates, evals de mensagem
- Orquestração: LangGraph (controle fino do fluxo de cadências) + Claude Agent SDK (Maestro como orchestrator)
- Sinais de intenção: G2, Bombora ou Apollo Intent
- triggeram reativação de leads que pesquisam a categoria

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Vigia 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de Cadências Ativas: conjunto de workflows LangGraph deployados com (1) 4 cadências codificadas (no-show, frio 30/60/90d, proposta fria, nurture longo)…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vigia 2 registrado
- [ ] Gate L3 respeitado: Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico;…
- [ ] Gate L3 respeitado: Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio
- [ ] Gate L3 respeitado: Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualifi…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou ed… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordag… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão semanal de cadências — Atlas gera relatório de performance; gestor aprova ajustes de parâmetros (intervalos, canais, thresholds de score) antes de sere… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out recebido — Qualquer pedido de descadastro é interrompido imediatamente pelo Cronos e notificado ao responsável para confirmação de remoção do CRM | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Vigia 2 | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
