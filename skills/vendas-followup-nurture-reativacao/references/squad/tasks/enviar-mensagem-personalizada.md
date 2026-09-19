---
task: volta()
responsavel: "Volta"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Instrução de toque do Cronos com {canal, template_id, ângulo, dados_personalização, lead_id}"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "dossiê do lead (nome, empresa, cargo, histórico, dor identificada)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "aprovação do Crítico"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagem enviada com registro de: canal_utilizado, conteúdo_enviado, timestamp, status_entrega, id_da_mensagem_no_canal"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Evento de retorno para Cronos atualizar estado da cadência"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato no ClickUp: 'Volta-Envio-{lead_id}-{canal}-{timestamp}' com screenshot/log do envio"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Instrução aprovada pelo Crítico e liberada pelo Maestro; horário de envio definido pelo Cronos atingido"
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

# Enviar Mensagem Personalizada

**Task ID:** `volta()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagem Personalizada |
| **status** | `pending` |
| **responsible_executor** | Volta (Volta — Worker de Outreach Multicanal) |
| **execution_type** | `Hybrid` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executor de outreach. Recebe a instrução do Cronos e redige a mensagem personalizada para o canal especificado (email, WhatsApp, LinkedIn, voz), usando os dados do lead e o ângulo definido. Antes de enviar, submete a mensagem ao Crítico para validação. Após aprovação, realiza o envio via API do canal correspondente e registra o resultado (enviado, aberto, clicado, respondido, erro). Para voz, gera o script e aciona o agente de voz (Vapi/Retell). É o único worker que toca sistemas externos de envio.

## Input

- Instrução de toque do Cronos com {canal, template_id, ângulo, dados_personalização, lead_id}
- dossiê do lead (nome, empresa, cargo, histórico, dor identificada)
- aprovação do Crítico

## Output

- Mensagem enviada com registro de: canal_utilizado, conteúdo_enviado, timestamp, status_entrega, id_da_mensagem_no_canal
- Evento de retorno para Cronos atualizar estado da cadência
- Artefato no ClickUp: 'Volta-Envio-{lead_id}-{canal}-{timestamp}' com screenshot/log do envio

## Trigger

Instrução aprovada pelo Crítico e liberada pelo Maestro; horário de envio definido pelo Cronos atingido

## Knowledge base (o que o executor consulta)

- Biblioteca de templates por canal x segmento x ângulo (email em HTML, WhatsApp em texto rico, LinkedIn em texto plano, scripts de voz em SSML), guia de tom e voz da marca, dados de personalização do lead (Clay/Apollo enrichment), limites de envio por canal (rate limits das APIs), regras de compliance LGPD/CAN-SPAM

## Action Items

1. Confirmar o gatilho e carregar a entrada (Instrução de toque do Cronos com {canal, template_id, ângulo, dados_personalização, lead_id}).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagem enviada com registro de: canal_utilizado, conteúdo_enviado, timestamp, status_entrega, id_da_mensagem_no_canal) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagem enviada com registro de: canal_utilizado, conteúdo_enviado, timestamp, status_entrega, id_da_mensagem_no_canal
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

- **to:** Sherlock
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
