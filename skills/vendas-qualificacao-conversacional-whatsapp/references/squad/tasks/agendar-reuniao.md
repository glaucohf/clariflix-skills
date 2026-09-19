---
task: agendadorDeReunioes()
responsavel: "Agendador de Reuniões"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead qualificado com score HOT ou WARM (flag do Magnus)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Disponibilidade do calendário do closer (via Google Calendar / Calendly API)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Contato do lead (WhatsApp)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Dados do closer responsável pela conta"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Agendamento confirmado no calendario"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Evento criado com descricao contendo o dossie de qualificacao completo para o closer"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Mensagens de confirmacao e lembrete enviadas ao lead"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Status atualizado no HubSpot: stage = 'Meeting Scheduled'"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato: booking_confirmation.json com evidencia de confirmacao do lead"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado pelo Orchestrator quando Magnus classifica lead como HOT ou WARM. Também disparado por webhook de cancelamento do Calendly para iniciar reagendamento."
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

# Agendar Reunião

**Task ID:** `agendadorDeReunioes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Qualificação Conversacional (WhatsApp)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Agendar Reunião |
| **status** | `pending` |
| **responsible_executor** | Agendador de Reuniões (Agendador de Reuniões — Tempo) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de Agendamento. Para leads qualificados (HOT/WARM), conduz a etapa final da conversa de WhatsApp: apresenta slots disponíveis do calendário do closer responsável, confirma o agendamento, envia confirmação com link de videochamada, lembra o lead 24h e 1h antes, reagenda automaticamente em caso de cancelamento (até 2 tentativas antes de escalar para humano).

## Input

- Lead qualificado com score HOT ou WARM (flag do Magnus)
- Disponibilidade do calendário do closer (via Google Calendar / Calendly API)
- Contato do lead (WhatsApp)
- Dados do closer responsável pela conta

## Output

- Agendamento confirmado no calendario
- Evento criado com descricao contendo o dossie de qualificacao completo para o closer
- Mensagens de confirmacao e lembrete enviadas ao lead
- Status atualizado no HubSpot: stage = 'Meeting Scheduled'
- Artefato: booking_confirmation.json com evidencia de confirmacao do lead

## Trigger

Disparado pelo Orchestrator quando Magnus classifica lead como HOT ou WARM. Também disparado por webhook de cancelamento do Calendly para iniciar reagendamento.

## Knowledge base (o que o executor consulta)

- Regras de roteamento de closer (por território, segmento ou disponibilidade)
- Templates de mensagem de confirmação e lembrete (tom da marca)
- Política de reagendamento (quantas tentativas, intervalo mínimo)
- Fuso horário do lead (detectado pelo prefixo do telefone ou declarado na conversa)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead qualificado com score HOT ou WARM (flag do Magnus)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Agendamento confirmado no calendario) e persistir no artefato do squad.
4. Entregar ao critic Censor Comercial; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Agendamento confirmado no calendario
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

- **to:** Reativador de Pipeline
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
