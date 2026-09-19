---
task: cronos()
responsavel: "Cronos"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento do Radar com lead_id e segmento_cadência"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "histórico de interações do lead"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "configuração das cadências (YAML de sequência, intervalos, canais, ângulos)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Instrução de próximo toque: {canal, template_id, ângulo, dados_personalização, horário_envio, fallback_se_sem_resposta}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Estado atualizado da cadência gravado no CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp: 'Cronos-Próximo-Toque-{lead_id}' com status e prazo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento publicado pelo Radar; resposta (ou ausência) de toque anterior; expiração de timer de cadência"
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

# Sequenciar Toques Lead

**Task ID:** `cronos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sequenciar Toques Lead |
| **status** | `pending` |
| **responsible_executor** | Cronos (Cronos — Worker de Cadência e Sequenciamento) |
| **execution_type** | `Worker` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em cadências. Dado o segmento e o histórico do lead, seleciona a cadência correta, determina o próximo toque (canal + timing + ângulo de mensagem), e enfileira a ação para o worker de outreach correspondente. Controla o estado interno da cadência: quantos toques foram feitos, quais tiveram resposta, qual o próximo passo. Aplica lógica de fallback (se email não aberto em 48h, muda para WhatsApp). Encerra a cadência automaticamente se houver resposta positiva ou se o lead pedir opt-out.

## Input

- Evento do Radar com lead_id e segmento_cadência
- histórico de interações do lead
- configuração das cadências (YAML de sequência, intervalos, canais, ângulos)

## Output

- Instrução de próximo toque: {canal, template_id, ângulo, dados_personalização, horário_envio, fallback_se_sem_resposta}
- Estado atualizado da cadência gravado no CRM
- Task no ClickUp: 'Cronos-Próximo-Toque-{lead_id}' com status e prazo

## Trigger

Evento publicado pelo Radar; resposta (ou ausência) de toque anterior; expiração de timer de cadência

## Knowledge base (o que o executor consulta)

- Biblioteca de cadências por segmento (YAML/JSON com sequências de toque, intervalos, canais, ângulos de mensagem), melhores horários de contato por perfil/região, regras de opt-out e compliance LGPD, histórico de resposta por cadência para otimização contínua

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento do Radar com lead_id e segmento_cadência).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Instrução de próximo toque: {canal, template_id, ângulo, dados_personalização, horário_envio, fallback_se_sem_resposta}) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Instrução de próximo toque: {canal, template_id, ângulo, dados_personalização, horário_envio, fallback_se_sem_resposta}
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

- **to:** Volta
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
