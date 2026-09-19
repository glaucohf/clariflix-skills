---
task: hermes()
responsavel: "Hermes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Score e recomendação do Oracle + perfil do deal + template de alerta por tipo de risco e canal + lista de stakeholders mapeados (closer responsável, gestor da área) + histórico de alertas anteriores para evitar spam"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens formatadas por canal (WhatsApp Business API, Slack webhook, email) prontas para envio, com contexto do deal, risco específico e ação recomendada"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato de log: {deal_id, alerta_enviado, canal, timestamp, ação_recomendada, status_entrega}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Aprovação do Critic (Nemesis) + deal classificado como Vermelho ou Morto pelo Oracle + ausência de intervenção em deal Amarelo por mais de 24h + solicitação manual de alerta"
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

# Formatar Alertas Contextualizados

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Formatar Alertas Contextualizados |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — Alertador de Risco) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de comunicação e alerta. Recebe os scores e recomendações do Oracle e formata alertas contextualizados para cada stakeholder: closer (alerta no WhatsApp/Slack com o que fazer agora), gestor (digest diário de risco no Slack/email com visão de portfolio), board (report semanal sintetico). Cada alerta inclui o contexto específico do deal, o risco identificado e a ação recomendada pelo squad.

## Input

- Score e recomendação do Oracle + perfil do deal + template de alerta por tipo de risco e canal + lista de stakeholders mapeados (closer responsável, gestor da área) + histórico de alertas anteriores para evitar spam

## Output

- Mensagens formatadas por canal (WhatsApp Business API, Slack webhook, email) prontas para envio, com contexto do deal, risco específico e ação recomendada
- Artefato de log: {deal_id, alerta_enviado, canal, timestamp, ação_recomendada, status_entrega}

## Trigger

Aprovação do Critic (Nemesis) + deal classificado como Vermelho ou Morto pelo Oracle + ausência de intervenção em deal Amarelo por mais de 24h + solicitação manual de alerta

## Knowledge base (o que o executor consulta)

- Templates de alerta por tipo de risco (estagnação, queda de engajamento, proposta sem resposta, fim de trimestre, deal Morto), preferências de canal por stakeholder, histórico de alertas enviados (controle de frequência), playbook de intervenção por estágio

## Action Items

1. Confirmar o gatilho e carregar a entrada (Score e recomendação do Oracle + perfil do deal + template de alerta por tipo de risco e canal + lista de stakeholders…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens formatadas por canal (WhatsApp Business API, Slack webhook, email) prontas para envio, com contexto do deal,…) e persistir no artefato do squad.
4. Entregar ao critic Nemesis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens formatadas por canal (WhatsApp Business API, Slack webhook, email) prontas para envio, com contexto do deal, risco específico e ação recomendada
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

- **to:** Mnemosine
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
