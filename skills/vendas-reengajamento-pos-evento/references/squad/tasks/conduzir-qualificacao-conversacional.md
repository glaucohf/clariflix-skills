---
task: argosEvento()
responsavel: "Argos Evento"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead responsivo com histórico da conversa pós-evento + dossiê de enriquecimento do Sherlock Evento + metadados de engajamento do evento"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Criterios BANT/MEDDIC calibrados por produto/segmento do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de qualificação preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada com referência ao tópico do evento, Timeline definida) + classificação SQL/MQL/DQ + resumo de objeções identificadas + próximo passo recomendado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registrado no CRM como nota de qualificação com link para o evento de origem"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Qualificação Concluída"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "{nome do contato}' com scorecard BANT e classificação"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead Score A ou B respondeu ao outreach do Cypher ou Nova. Tambem acionado quando lead Score C (baixo engajamento) responde espontaneamente a qualquer mensagem da cadencia."
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

# Conduzir Qualificação Conversacional

**Task ID:** `argosEvento()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Reengajamento Pós-Evento e Webinar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Conduzir Qualificação Conversacional |
| **status** | `pending` |
| **responsible_executor** | Argos Evento (Argos Evento — Worker de Qualificação Pós-Resposta) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe leads responsivos (Score A ou B que responderam ao outreach) e conduz a qualificação conversacional BANT/MEDDIC via canal ativo (WhatsApp ou email). Contexto do evento é usado como alavanca de qualificação: 'Vi que você ficou até o final da sessão sobre X — isso significa que você já tem um processo de Y em andamento ou ainda é tudo manual?' Classifica como SQL (reunião imediata), MQL (nurture qualificado) ou DQ (desqualificado). Entrega handoff estruturado ao closer com toda a inteligência coletada.

## Input

- Lead responsivo com histórico da conversa pós-evento + dossiê de enriquecimento do Sherlock Evento + metadados de engajamento do evento
- Criterios BANT/MEDDIC calibrados por produto/segmento do cliente

## Output

- Ficha de qualificação preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada com referência ao tópico do evento, Timeline definida) + classificação SQL/MQL/DQ + resumo de objeções identificadas + próximo passo recomendado
- Registrado no CRM como nota de qualificação com link para o evento de origem
- Artefato ClickUp: task 'Qualificação Concluída
- {nome do contato}' com scorecard BANT e classificação

## Trigger

Lead Score A ou B respondeu ao outreach do Cypher ou Nova. Tambem acionado quando lead Score C (baixo engajamento) responde espontaneamente a qualquer mensagem da cadencia.

## Knowledge base (o que o executor consulta)

- Criterios BANT/MEDDIC calibrados por produto/segmento
- perguntas de qualificação que usam o contexto do evento como alavanca de abertura
- respostas a objeções frequentes ligadas ao tema do evento ('vi que você tem dúvida sobre X
- na nossa solução isso funciona assim...')
- exemplos de qualificações bem-sucedidas com leads de eventos anteriores
- limiares de score para SQL vs
- MQL por ticket médio do produto

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead responsivo com histórico da conversa pós-evento + dossiê de enriquecimento do Sherlock Evento + metadados de engaj…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ficha de qualificação preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada com referência ao…) e persistir no artefato do squad.
4. Entregar ao critic Vigilia; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ficha de qualificação preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada com referência ao tópico do evento, Timeline definida) +…
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

- **to:** Eco Evento
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
