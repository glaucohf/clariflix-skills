---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de tendências aprovado pelo HITL (PM ou Head de CS) com lista de ações recomendadas + mapeamento de projetos/listas do ClickUp por tipo de ação (produto, CS, engenharia, ops) + dados do score de tendência para cálculo de prioridade e prazo + histórico de tasks VOC já criadas (para evitar duplicatas de temas recorrentes sem resolução)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tasks criadas no ClickUp com todos os campos preenchidos, retornando lista de task URLs e IDs para o Orchestrator"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Notificação Slack para o responsável de cada task com contexto resumido em 2 linhas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Log de ativação no Supabase (tabela: voc_actions) com: task_id_clickup, tema_id, score_priorização_no_momento, timestamp_criação, responsável_atribuído"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Relatório mensal de conversão (% insights -> tasks -> concluídas -> impacto reportado) para Head de Produto e Head de CS"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orchestrator Orion após Lyra confirmar relatório semanal e HITL aprovar lista de ações; acionado para alerta de emergência classificado como CRÍTICO após notificação HITL e confirmação…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Cassandra antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia lembrete; sem resposta em 8h, relatório é enviado com disclaimer 'pendente de revisão humana'"
    - "[ ] HITL: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para atendimento) antes de aparecer no backlog ativo; aprovação via bot no Slack com preview da task"
    - "[ ] HITL: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefing imediato e Atlas cria task de emergência; se falso positivo, threshold é ajustado automaticamente"
    - "[ ] HITL: Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-processar histórico; impacto estimado em registros afetados e apresentado antes da aprovação"
    - "[ ] HITL: Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; indica possível drift na linguagem dos clientes ou bug na ingestão"
---

# Criar Tasks Rastreáveis

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Criar Tasks Rastreáveis |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas – Agente de Ativação e Prova de Trabalho no ClickUp) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Transforma insights aprovados em tarefas rastreáveis no ClickUp — o elo entre a inteligencia do squad e a acao do time. Apos aprovacao HITL do relatorio semanal ou de alerta de emergencia, cria tasks no ClickUp no projeto correto (produto, CS, engenharia ou ops) com: titulo padronizado ([VOC] Tema — Data), descricao com insight completo (volume, tendencia, verbatims, recomendacao), prioridade calculada pelo score de tendencia, prazo sugerido com base na urgencia (emergencia = 48h, tendencia critica = 7 dias, observacao = 30 dias), checklist de steps de investigacao ou acao, link para o relatorio completo no Notion/Supabase, e tag VOC para rastreabilidade. Monitora o status das tasks criadas: se task de emergencia nao aberta em 24h, escalona para manager. Calcula mensalmente: % de insights que viraram tasks, % de tasks concluidas, e impacto reportado pelo time (campo de resultado preenchido no ClickUp).

## Input

- Relatório de tendências aprovado pelo HITL (PM ou Head de CS) com lista de ações recomendadas + mapeamento de projetos/listas do ClickUp por tipo de ação (produto, CS, engenharia, ops) + dados do score de tendência para cálculo de prioridade e prazo + histórico de tasks VOC já criadas (para evitar duplicatas de temas recorrentes sem resolução)

## Output

- Tasks criadas no ClickUp com todos os campos preenchidos, retornando lista de task URLs e IDs para o Orchestrator
- Notificação Slack para o responsável de cada task com contexto resumido em 2 linhas
- Log de ativação no Supabase (tabela: voc_actions) com: task_id_clickup, tema_id, score_priorização_no_momento, timestamp_criação, responsável_atribuído
- Relatório mensal de conversão (% insights -> tasks -> concluídas -> impacto reportado) para Head de Produto e Head de CS

## Trigger

Acionado pelo Orchestrator Orion após Lyra confirmar relatório semanal e HITL aprovar lista de ações; acionado para alerta de emergência classificado como CRÍTICO após notificação HITL e confirmação de ação; acionado manualmente pelo PM via comando no ClickUp para criar task de insight específico

## Knowledge base (o que o executor consulta)

- Mapeamento de tipos de ação para projetos/listas/responsáveis no ClickUp (bug -> Engineering Backlog / responsável tech lead
- feature request -> Product Backlog / PM
- gap de KB -> CS Knowledge Base project / Head de CS
- processo falho -> Ops Improvement / Head de Ops), template de task VOC com campos obrigatórios e checklists por tipo de ação, regras de prioridade e prazo por score de tendência e urgência, histórico de tasks VOC com status e resultado (para detectar temas recorrentes sem resolução e escalar prioridade)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Relatório de tendências aprovado pelo HITL (PM ou Head de CS) com lista de ações recomendadas + mapeamento de projetos/…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tasks criadas no ClickUp com todos os campos preenchidos, retornando lista de task URLs e IDs para o Orchestrator) e persistir no artefato do squad.
4. Entregar ao critic Cassandra; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tasks criadas no ClickUp com todos os campos preenchidos, retornando lista de task URLs e IDs para o Orchestrator
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Cassandra registrado
- [ ] Gate HITL respeitado: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação e…
- [ ] Gate HITL respeitado: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto…
- [ ] Gate HITL respeitado: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmad…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para at… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefin… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-proce… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; in… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Publicacao de insight que menciona concorrente especifico por nome — Lyra sinaliza e o Head de CS aprova antes de distribuir para evitar vazamento de informaca… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Re-calibração de thresholds de alerta após detecção de falsos positivos recorrentes — o Rapid documenta a sugestão de ajuste e aguarda aprovação do PM ou Head… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de canal com volume insuficiente para análise estatística identificado pós-Discovery — Haruki notifica e aguarda decisão humana sobre incluir ou exclu… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Cassandra | BLOQUEIA entrega |

## Handoff

- **to:** Cassandra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
