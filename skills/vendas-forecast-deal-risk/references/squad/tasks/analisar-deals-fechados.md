---
task: mnemosine()
responsavel: "Mnemosine"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Deals fechados nos últimos 30 dias (won/lost/abandoned) + score de risco que o Oracle havia atribuído + alertas que foram disparados + ações de intervenção registradas + motivo de perda (se registrado no CRM)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio mensal de aprendizado: {accuracy_do_forecast_%, falsos_negativos_top5 (deals que perdemos sem alerta), falsos_positivos_top5 (deals que alarmamos mas fecharam), padroes_novos_identificados, sugestoes_de_ajuste_nos_thresholds, ROI_estimado_das_intervencoes}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job mensal (dia 5 de cada mês, após fechamento do período anterior) + acumulação de 10+ deals fechados desde último ciclo de aprendizado + solicitação manual do gestor"
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

# Analisar Deals Fechados

**Task ID:** `mnemosine()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Deals Fechados |
| **status** | `pending` |
| **responsible_executor** | Mnemosine (Mnemosine — Arquivista de Deals) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de analise post-mortem e aprendizado continuo. Analisa todos os deals fechados (won e lost) para identificar padroes que o modelo de risco ainda nao captura. Gera insights acionaveis: quais sinais precederam perdas sistematicamente, quais intervencoes funcionaram, onde o forecast errou. Alimenta o feedback loop para melhorar o Oracle.

## Input

- Deals fechados nos últimos 30 dias (won/lost/abandoned) + score de risco que o Oracle havia atribuído + alertas que foram disparados + ações de intervenção registradas + motivo de perda (se registrado no CRM)

## Output

- Relatorio mensal de aprendizado: {accuracy_do_forecast_%, falsos_negativos_top5 (deals que perdemos sem alerta), falsos_positivos_top5 (deals que alarmamos mas fecharam), padroes_novos_identificados, sugestoes_de_ajuste_nos_thresholds, ROI_estimado_das_intervencoes}

## Trigger

Job mensal (dia 5 de cada mês, após fechamento do período anterior) + acumulação de 10+ deals fechados desde último ciclo de aprendizado + solicitação manual do gestor

## Knowledge base (o que o executor consulta)

- Base histórica de deals fechados com seus scores finais e motivos de perda, registro de intervenções e seus resultados, modelo atual de scoring do Oracle (para propor ajustes), benchmarks de forecast accuracy do mercado (55-85%)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Deals fechados nos últimos 30 dias (won/lost/abandoned) + score de risco que o Oracle havia atribuído + alertas que for…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio mensal de aprendizado: {accuracy_do_forecast_%, falsos_negativos_top5 (deals que perdemos sem alerta), falsos…) e persistir no artefato do squad.
4. Entregar ao critic Nemesis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio mensal de aprendizado: {accuracy_do_forecast_%, falsos_negativos_top5 (deals que perdemos sem alerta), falsos_positivos_top5 (deals que alarmamos mas…
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

- **to:** Cronos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
