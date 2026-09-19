---
task: sibila()
responsavel: "Sibila"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Scores e probabilidades do Oracle para todos os deals ativos + metas de receita do período (30/60/90 dias, extraídas do CRM ou inseridas manualmente) + histórico de accuracy dos forecasts anteriores"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de forecast em três cenarios (PDF + JSON para dashboard): {período, cenario_pessimista_R$, cenario_provável_R$, cenario_otimista_R$, meta_R$, gap_R$, accuracy_historica_%, deals_em_risco_top5, deals_saudáveis_top5, recomendação_de_foco}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job semanal (toda segunda-feira 07h00) + job mensal (dia 1 de cada mês) + solicitação manual do gestor + 5 dias antes do fim do mês/trimestre"
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

# Gerar Forecast Pipeline

**Task ID:** `sibila()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Forecast Pipeline |
| **status** | `pending` |
| **responsible_executor** | Sibila (Síbila — Vidente do Forecast) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de geração do forecast de pipeline. Agrega os scores do Oracle e projeta o fechamento esperado para os próximos 30/60/90 dias com três cenarios: pessimista (apenas deals verdes), provável (verdes + amarelos com desconto de risco) e otimista (todos os deals ativos ponderados). Compara com meta do período e aponta o gap.

## Input

- Scores e probabilidades do Oracle para todos os deals ativos + metas de receita do período (30/60/90 dias, extraídas do CRM ou inseridas manualmente) + histórico de accuracy dos forecasts anteriores

## Output

- Relatório de forecast em três cenarios (PDF + JSON para dashboard): {período, cenario_pessimista_R$, cenario_provável_R$, cenario_otimista_R$, meta_R$, gap_R$, accuracy_historica_%, deals_em_risco_top5, deals_saudáveis_top5, recomendação_de_foco}

## Trigger

Job semanal (toda segunda-feira 07h00) + job mensal (dia 1 de cada mês) + solicitação manual do gestor + 5 dias antes do fim do mês/trimestre

## Knowledge base (o que o executor consulta)

- Histórico de fechamentos por período (sazonalidade), metas comerciais por período, accuracy dos forecasts anteriores do próprio squad (auto-melhoria), benchmarks de conversão por estágio do funil

## Action Items

1. Confirmar o gatilho e carregar a entrada (Scores e probabilidades do Oracle para todos os deals ativos + metas de receita do período (30/60/90 dias, extraídas do…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de forecast em três cenarios (PDF + JSON para dashboard): {período, cenario_pessimista_R$, cenario_provável_R…) e persistir no artefato do squad.
4. Entregar ao critic Nemesis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de forecast em três cenarios (PDF + JSON para dashboard): {período, cenario_pessimista_R$, cenario_provável_R$, cenario_otimista_R$, meta_R$, gap_R$,…
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

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
