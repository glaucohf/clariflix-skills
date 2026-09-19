---
task: cronos()
responsavel: "Cronos"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de deals sem próxima atividade agendada ou com atividade vencida (do CRM) + histórico de interações do deal + estágio atual + perfil do contato + notas do closer"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sugestão de próximo passo formatada por deal: {deal_id, próximo_passo_sugerido, data_sugerida, canal_sugerido, contexto_relevante, justificativa}, criação automática de tarefa no ClickUp após aprovação HITL"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Deal ativo sem próxima atividade agendada por mais de 48h + atividade vencida sem reagendamento + novo deal entrado em estágio de Proposta ou Negociação sem follow-up definido"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Nemesis antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora da empresa"
    - "[ ] L3: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM"
    - "[ ] L2: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa"
    - "[ ] L2: Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle"
    - "[ ] L1: Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal"
---

# Sugerir Próximo Passo

**Task ID:** `cronos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sugerir Próximo Passo |
| **status** | `pending` |
| **responsible_executor** | Cronos (Cronos — Gestor de Próximo Passo) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em detectar deals sem próximo passo definido e sem data de follow-up agendada. Varre o CRM buscando deals onde a próxima atividade está vazia ou vencida. Para cada deal identificado, gera uma sugestão contextualizada de próximo passo baseada no estágio, histórico da conta e no que o closer anotou. Apresenta ao closer via HITL para confirmação antes de criar a tarefa no ClickUp.

## Input

- Lista de deals sem próxima atividade agendada ou com atividade vencida (do CRM) + histórico de interações do deal + estágio atual + perfil do contato + notas do closer

## Output

- Sugestão de próximo passo formatada por deal: {deal_id, próximo_passo_sugerido, data_sugerida, canal_sugerido, contexto_relevante, justificativa}, criação automática de tarefa no ClickUp após aprovação HITL

## Trigger

Deal ativo sem próxima atividade agendada por mais de 48h + atividade vencida sem reagendamento + novo deal entrado em estágio de Proposta ou Negociação sem follow-up definido

## Knowledge base (o que o executor consulta)

- Playbook de vendas do cliente (cadências por estágio), histórico de sequências de atividade que levaram a fechamentos, SLA de follow-up por estágio e valor do deal, preferências de canal do contato

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de deals sem próxima atividade agendada ou com atividade vencida (do CRM) + histórico de interações do deal + est…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sugestão de próximo passo formatada por deal: {deal_id, próximo_passo_sugerido, data_sugerida, canal_sugerido, contexto…) e persistir no artefato do squad.
4. Entregar ao critic Nemesis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sugestão de próximo passo formatada por deal: {deal_id, próximo_passo_sugerido, data_sugerida, canal_sugerido, contexto_relevante, justificativa}, criação auto…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Nemesis registrado
- [ ] Gate L3 respeitado: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem…
- [ ] Gate L3 respeitado: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM
- [ ] Gate L2 respeitado: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora d… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM | BLOQUEIA até decisão humana |
| VETO-003 | L2 — Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Nemesis | BLOQUEIA entrega |

## Handoff

- **to:** Nemesis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
