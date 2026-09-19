---
task: atlas()
responsavel: "Atlas"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dados de engajamento do lead (abertura, clique, resposta, visita ao site)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "dossiê do Sherlock"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "histórico de interações"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "data de último toque"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "score anterior"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score atualizado (0-100) com breakdown por dimensão (fit, engajamento, intenção, urgência)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Lista re-ranqueada de leads por prioridade"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alertas de 'hot signal' ou 'risco de perda' para Maestro"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Campo 'lead_score' atualizado no CRM"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp: 'Atlas-Score-{lead_id}-{score}' com justificativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Qualquer evento de engajamento do lead (abertura, clique, visita); cron diário de re-scoring geral; evento de enriquecimento do Sherlock concluído"
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

# Calcular Score Lead

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Score Lead |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Worker de Lead Scoring e Priorização) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Calcula e atualiza continuamente o score de cada lead em cadência, combinando fit de perfil (ICP match), engajamento (aberturas, cliques, respostas, visitas), sinal de intenção e urgência temporal. Re-ranqueia a fila do Radar para garantir que os leads mais propensos a converter sejam trabalhados primeiro. Emite alertas para o Maestro quando um lead frio sobe de score rapidamente (sinal de compra) ou quando um lead quente esfria sem motivo (risco de perda).

## Input

- Dados de engajamento do lead (abertura, clique, resposta, visita ao site)
- dossiê do Sherlock
- histórico de interações
- data de último toque
- score anterior

## Output

- Score atualizado (0-100) com breakdown por dimensão (fit, engajamento, intenção, urgência)
- Lista re-ranqueada de leads por prioridade
- Alertas de 'hot signal' ou 'risco de perda' para Maestro
- Campo 'lead_score' atualizado no CRM
- Task no ClickUp: 'Atlas-Score-{lead_id}-{score}' com justificativa

## Trigger

Qualquer evento de engajamento do lead (abertura, clique, visita); cron diário de re-scoring geral; evento de enriquecimento do Sherlock concluído

## Knowledge base (o que o executor consulta)

- Modelo de scoring com pesos por dimensão (configurável por produto/mercado)
- histórico de leads que converteram (perfil de vencedor)
- thresholds de alerta por segmento de cadência
- dados de ICP e firmografia

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dados de engajamento do lead (abertura, clique, resposta, visita ao site)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score atualizado (0-100) com breakdown por dimensão (fit, engajamento, intenção, urgência)) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score atualizado (0-100) com breakdown por dimensão (fit, engajamento, intenção, urgência)
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

- **to:** Agenda
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
