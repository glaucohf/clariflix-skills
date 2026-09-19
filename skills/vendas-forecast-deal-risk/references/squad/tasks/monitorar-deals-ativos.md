---
task: argus()
responsavel: "Argus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Feed de eventos do CRM (deals ativos, timestamps de ultima atividade, estagio atual, owner, data de fechamento prevista, historico de interacoes) + thresholds de alerta configurados por estagio"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lista de eventos de risco padronizados (JSON): {deal_id, tipo_risco, severidade [1-5], último_contato, dias_estagnado, estágio_atual, owner, valor_deal, trigger_específico}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job agendado a cada 4h OU webhook de mudança no CRM OU comando manual do gestor via ClickUp"
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

# Monitorar Deals Ativos

**Task ID:** `argus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Deals Ativos |
| **status** | `pending` |
| **responsible_executor** | Argus (Argus — Vigia de Sinais) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de monitoramento contínuo do CRM. Varre todos os deals ativos a cada 4 horas (ou via webhook em mudança de estágio). Detecta anomalias: ausência de atividade, estágio congelado, data de fechamento passada sem update, queda de engajamento de contato. Gera evento de risco padronizado para a Cassandra processar.

## Input

- Feed de eventos do CRM (deals ativos, timestamps de ultima atividade, estagio atual, owner, data de fechamento prevista, historico de interacoes) + thresholds de alerta configurados por estagio

## Output

- Lista de eventos de risco padronizados (JSON): {deal_id, tipo_risco, severidade [1-5], último_contato, dias_estagnado, estágio_atual, owner, valor_deal, trigger_específico}

## Trigger

Job agendado a cada 4h OU webhook de mudança no CRM OU comando manual do gestor via ClickUp

## Knowledge base (o que o executor consulta)

- Histórico de deals dos últimos 12 meses (won/lost/stalled), thresholds de alerta por estágio (configurados no onboarding), calendário comercial (feriados, fim de trimestre), SLA de resposta por estágio do funil

## Action Items

1. Confirmar o gatilho e carregar a entrada (Feed de eventos do CRM (deals ativos, timestamps de ultima atividade, estagio atual, owner, data de fechamento prevista…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lista de eventos de risco padronizados (JSON): {deal_id, tipo_risco, severidade [1-5], último_contato, dias_estagnado,…) e persistir no artefato do squad.
4. Entregar ao critic Nemesis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lista de eventos de risco padronizados (JSON): {deal_id, tipo_risco, severidade [1-5], último_contato, dias_estagnado, estágio_atual, owner, valor_deal, trigge…
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

- **to:** Oracle
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
