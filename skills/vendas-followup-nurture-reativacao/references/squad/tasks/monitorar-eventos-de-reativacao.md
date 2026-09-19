---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Webhook do CRM com mudanças de status, dados de abertura de email/click (HubSpot/Pipedrive), agenda do calendário (Google/Outlook), sinais de intent data (Apollo, Clay)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Evento estruturado com: lead_id, segmento_cadência, urgência (1-5), canal_preferencial, último_toque, histórico_resumido, score_atual"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Publicado na fila do Maestro"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato verificável no ClickUp: task 'Radar-Sinal-{lead_id}-{timestamp}' com todos os campos preenchidos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron job a cada 15 minutos sobre CRM; webhooks em tempo real para no-show (cancelamento de reunião) e abertura de email; revisão diária às 7h para leads frios de 30/60/90 dias"
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

# Monitorar Eventos De Reativacao

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Eventos De Reativacao |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Worker de Sinais e Segmentação) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente o CRM e os canais de entrada para detectar eventos que disparam reativacao: lead sem toque ha X dias, email aberto sem clique, proposta expirada, no-show confirmado, mudança de cargo do lead, visita ao site apos periodo de silencio, expiracao de trial. Classifica cada lead no segmento correto de cadencia (frio, no-show, ghosting, nurture longo) e publica o evento no Maestro para orquestracao. Responsavel por manter a fila priorizada de leads a serem trabalhados.

## Input

- Webhook do CRM com mudanças de status, dados de abertura de email/click (HubSpot/Pipedrive), agenda do calendário (Google/Outlook), sinais de intent data (Apollo, Clay)

## Output

- Evento estruturado com: lead_id, segmento_cadência, urgência (1-5), canal_preferencial, último_toque, histórico_resumido, score_atual
- Publicado na fila do Maestro
- Artefato verificável no ClickUp: task 'Radar-Sinal-{lead_id}-{timestamp}' com todos os campos preenchidos

## Trigger

Cron job a cada 15 minutos sobre CRM; webhooks em tempo real para no-show (cancelamento de reunião) e abertura de email; revisão diária às 7h para leads frios de 30/60/90 dias

## Knowledge base (o que o executor consulta)

- Regras de segmentação por dias-sem-toque, thresholds de score por produto/ticket, mapeamento de canais por perfil de lead (ICP), histórico de cadências anteriores do lead, blacklist de leads opt-out

## Action Items

1. Confirmar o gatilho e carregar a entrada (Webhook do CRM com mudanças de status, dados de abertura de email/click (HubSpot/Pipedrive), agenda do calendário (Goog…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Evento estruturado com: lead_id, segmento_cadência, urgência (1-5), canal_preferencial, último_toque, histórico_resumid…) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Evento estruturado com: lead_id, segmento_cadência, urgência (1-5), canal_preferencial, último_toque, histórico_resumido, score_atual
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

- **to:** Cronos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
