---
task: loki()
responsavel: "Loki"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de anomalia do Argus, Root Cause Report do Remi, Verification Report do Vega, Recovery Action Record do Finn (ou Fix Plan do Coda para L3), resultado final da recuperação, métricas de freshness pós-recuperação, assignee e SLA configurados por tier de pipeline no ClickUp"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Task no ClickUp por incidente (titulo padronizado: [PIPELINE] [SEVERITY] root_cause"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "status, com checklist de etapas, attachments dos reports, timestamp de cada etapa, prova de trabalho = freshness restaurada + rows_recovered)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Weekly Incident Report (Markdown: MTTR medio, MTTD medio, taxa de auto-resolucao, top-5 pipelines problematicos, custo evitado estimado, incidentes HITL L3 pendentes)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Para L3: task com Fix Plan formatado como checklist de aprovacao + deadline + assignee sugerido + Slack notification"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orion ao início de cada incidente (para criar a task) e ao final (para fechar com resultado). Também roda cron semanal (segunda 08h00) para gerar o Weekly Report. Dispara notificação Sla…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vega 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Ações irreversíveis ou P1-P2: qualquer ação que altere schema em produção, reprocesse mais de 24h de dados, faça rollback de tabela ou envolva custo de compute significativo requer aprovação explícita. Loki cria task no ClickUp com Fix Plan do Coda (checklist de aprovação) e notifica via Slack. SLA de resposta: P1 = 30min, P2 = 2h. Se SLA expirar sem resposta, Orion escala para gestor do pipeline."
    - "[ ] L3: Vega emite BLOCKED: quando a verificacao do Vega reprova qualquer dimensao (proporcionalidade, reversibilidade, scope, precedente), a acao e bloqueada independente da classificacao original. Requer override explicito humano com justificativa registrada."
    - "[ ] L3: Schema drift complexo: quando Remi identifica schema drift que não se enquadra nos patches automáticos seguros (ex: renomeação ambígua, remoção de campo usado downstream, mudança de tipo com perda de dados), o Coda prepara o plano de migração DDL completo para aprovação humana antes de qualquer alteração."
    - "[ ] L2: Revisão do Calibration Report semanal do Nexus: humano (engenheiro de dados responsável) revisa os thresholds recalibrados antes da aplicação. Não bloqueia operação, mas permite ajuste fino de sensibilidade por pipeline crítico."
    - "[ ] L2: Onboarding de novo pipeline: antes de iniciar monitoramento de um pipeline novo, humano valida o anomaly_config.json gerado pelo Nexus (thresholds, criticidade, recovery_policy) e confirma os assignees responsáveis por incidentes HITL."
---

# Documentar Incidente

**Task ID:** `loki()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Documentar Incidente |
| **status** | `pending` |
| **responsible_executor** | Loki (Loki — O Chronicler de Incidentes) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Documenta cada incidente como prova de trabalho verificavel. Para cada anomalia detectada, cria e fecha a task correspondente no ClickUp com o historico completo: alerta inicial (Argus), diagnostico (Remi), validacao (Vega), acao tomada (Finn ou Fix Plan do Coda), resultado e freshness restaurada. Tambem gera o Incident Report semanal com metricas agregadas (MTTR medio, taxa de auto-resolucao, top-5 pipelines mais instáveis, custo estimado de horas salvas). Para incidentes HITL L3, cria a task com o Fix Plan do Coda formatado como checklist de aprovacao e monitora o SLA de resposta humana.

## Input

- Evento de anomalia do Argus, Root Cause Report do Remi, Verification Report do Vega, Recovery Action Record do Finn (ou Fix Plan do Coda para L3), resultado final da recuperação, métricas de freshness pós-recuperação, assignee e SLA configurados por tier de pipeline no ClickUp

## Output

- Task no ClickUp por incidente (titulo padronizado: [PIPELINE] [SEVERITY] root_cause
- status, com checklist de etapas, attachments dos reports, timestamp de cada etapa, prova de trabalho = freshness restaurada + rows_recovered)
- Weekly Incident Report (Markdown: MTTR medio, MTTD medio, taxa de auto-resolucao, top-5 pipelines problematicos, custo evitado estimado, incidentes HITL L3 pendentes)
- Para L3: task com Fix Plan formatado como checklist de aprovacao + deadline + assignee sugerido + Slack notification

## Trigger

Chamado pelo Orion ao início de cada incidente (para criar a task) e ao final (para fechar com resultado). Também roda cron semanal (segunda 08h00) para gerar o Weekly Report. Dispara notificação Slack imediata para P1 e P2.

## Knowledge base (o que o executor consulta)

- Template de tasks de incidente no ClickUp (por severity), mapa de assignees por pipeline e tipo de incidente (quem e o dono de cada pipeline), SLAs de resposta HITL por severity (P1: 30min, P2: 2h, P3: 8h, P4: 24h), historico de incidentes fechados para calculo de metricas, configuracao de canais Slack por severity

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de anomalia do Argus, Root Cause Report do Remi, Verification Report do Vega, Recovery Action Record do Finn (ou…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Task no ClickUp por incidente (titulo padronizado: [PIPELINE] [SEVERITY] root_cause) e persistir no artefato do squad.
4. Entregar ao critic Vega 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Task no ClickUp por incidente (titulo padronizado: [PIPELINE] [SEVERITY] root_cause
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vega 2 registrado
- [ ] Gate L3 respeitado: Ações irreversíveis ou P1-P2: qualquer ação que altere schema em produção, reprocesse mais de 24h de dados, faça rollback de tabela ou envo…
- [ ] Gate L3 respeitado: Vega emite BLOCKED: quando a verificacao do Vega reprova qualquer dimensao (proporcionalidade, reversibilidade, scope, precedente), a acao…
- [ ] Gate L3 respeitado: Schema drift complexo: quando Remi identifica schema drift que não se enquadra nos patches automáticos seguros (ex: renomeação ambígua, rem…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Ações irreversíveis ou P1-P2: qualquer ação que altere schema em produção, reprocesse mais de 24h de dados, faça rollback de tabela ou envolva custo de compute… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Vega emite BLOCKED: quando a verificacao do Vega reprova qualquer dimensao (proporcionalidade, reversibilidade, scope, precedente), a acao e bloqueada independ… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Schema drift complexo: quando Remi identifica schema drift que não se enquadra nos patches automáticos seguros (ex: renomeação ambígua, remoção de campo usado… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Revisão do Calibration Report semanal do Nexus: humano (engenheiro de dados responsável) revisa os thresholds recalibrados antes da aplicação. Não bloqueia ope… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Onboarding de novo pipeline: antes de iniciar monitoramento de um pipeline novo, humano valida o anomaly_config.json gerado pelo Nexus (thresholds, criticidade… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Weekly Incident Report: gestor de dados recebe o relatório semanal do Loki e pode re-classificar incidentes (true/false positive), ajustar prioridades e confir… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Vega 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vega 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
