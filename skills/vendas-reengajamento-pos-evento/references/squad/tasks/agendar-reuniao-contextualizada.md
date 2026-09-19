---
task: atlasEvento()
responsavel: "Atlas Evento"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de qualificação do Argos Evento com classificação SQL + preferências de horário + histórico de engajamento no evento"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Acesso ao calendário do closer responsável"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Evento criado no calendário com link de videoconferência e pauta personalizada baseada na qualificação (budget discutido, need identificada, próximo passo esperado)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "confirmação enviada ao lead via canal preferido com referência ao evento"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "lembrete configurado"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "registro no CRM (campo 'reunião_agendada_em', 'origem_evento', 'pauta_reunião')"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Reunião Agendada"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "{nome do contato} ({nome do evento})' com dados do evento e pauta"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead classificado como SQL pelo Argos Evento. Também acionado por no-show detectado (para reagendamento automático com mensagem contextualizada no evento)."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vigilia antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer aprovação do closer responsável antes do primeiro envio"
    - "[ ] HITL: Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento"
    - "[ ] HITL: Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática"
    - "[ ] HITL: Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana"
    - "[ ] HITL: Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação"
---

# Agendar Reunião Contextualizada

**Task ID:** `atlasEvento()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Agendar Reunião Contextualizada |
| **status** | `pending` |
| **responsible_executor** | Atlas Evento (Atlas Evento — Worker de Agendamento Contextualizado) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe SQLs qualificados pelo Argos Evento e fecha o agendamento de reunião/demo com o closer responsável diretamente na conversa com o lead. Diferencial: usa o contexto específico do evento na confirmação ('Nossa reunião vai ser uma continuação do que você explorou na sessão de X no {nome do evento}'). Coordena disponibilidade, propõe 3 horários, confirma, envia convite com pauta personalizada baseada na qualificação, e gerencia lembretes (D-1 e H-1) e reagendamentos.

## Input

- Ficha de qualificação do Argos Evento com classificação SQL + preferências de horário + histórico de engajamento no evento
- Acesso ao calendário do closer responsável

## Output

- Evento criado no calendário com link de videoconferência e pauta personalizada baseada na qualificação (budget discutido, need identificada, próximo passo esperado)
- confirmação enviada ao lead via canal preferido com referência ao evento
- lembrete configurado
- registro no CRM (campo 'reunião_agendada_em', 'origem_evento', 'pauta_reunião')
- Artefato ClickUp: task 'Reunião Agendada
- {nome do contato} ({nome do evento})' com dados do evento e pauta

## Trigger

Lead classificado como SQL pelo Argos Evento. Também acionado por no-show detectado (para reagendamento automático com mensagem contextualizada no evento).

## Knowledge base (o que o executor consulta)

- Regras de disponibilidade de cada closer (horários, territórios, produtos de especialidade)
- templates de confirmação e lembrete com personalização de contexto de evento
- política de reagendamento (máximo de tentativas, intervalo)
- templates de pauta de reunião por tipo de qualificação e produto
- integração com Google Calendar/Outlook via MCP

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ficha de qualificação do Argos Evento com classificação SQL + preferências de horário + histórico de engajamento no eve…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Evento criado no calendário com link de videoconferência e pauta personalizada baseada na qualificação (budget discutid…) e persistir no artefato do squad.
4. Entregar ao critic Vigilia; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Evento criado no calendário com link de videoconferência e pauta personalizada baseada na qualificação (budget discutido, need identificada, próximo passo espe…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vigilia registrado
- [ ] Gate HITL respeitado: Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) —…
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento
- [ ] Gate HITL respeitado: Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Contas estratégicas detectadas na lista (já clientes ativos, prospects em negociação avançada no CRM, contas VIP definidas pelo cliente) — qualquer ação requer… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem bloqueada pelo Vigília na 3ª iteração de correção — exige revisão humana antes do envio, com log do problema para treinamento | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Lead Score A com ticket estimado acima do threshold definido pelo cliente (ex: >R$100k) — escala direto para closer sem cadência automática | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Participante do evento que é funcionário de concorrente identificado — qualquer abordagem requer decisão estratégica humana | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Solicitação de proposta comercial ou orçamento mencionada na resposta do lead — Argos Evento escala imediatamente para closer com ficha de qualificação | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Lead que solicita opt-out ou demonstra irritação com o contato — intervenção humana obrigatória, registro de opt-out e revisão da cadência | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Inconsistência crítica detectada entre dados do evento e CRM (ex: lead do evento e cliente com contrato ativo cancelado) — revisão humana antes de qualquer con… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Volume de lista acima de 1.000 contatos em evento único — revisão humana da segmentação antes do disparo em massa | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Vigilia | BLOQUEIA entrega |

## Handoff

- **to:** Vigilia
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
