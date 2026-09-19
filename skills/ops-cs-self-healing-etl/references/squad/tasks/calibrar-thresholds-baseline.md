---
task: nexus()
responsavel: "Nexus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Histórico de execuções dos últimos 30-90 dias por pipeline (rows, latência, error rate, schema versions), log de incidentes resolvidos (para distinguir anomalias reais de falsos positivos), calendário do negócio (feriados, campanhas, sazonalidade), feedback humano sobre alertas (true positive / false positive tagging no ClickUp)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "anomaly_config.json atualizado por pipeline (thresholds de volume [min/max por hora/dia/semana], latência máxima aceitável, null_rate_threshold por coluna, schema_stability_score, criticidade do pipeline)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Calibration Report semanal (Markdown: pipelines recalibrados, thresholds alterados com justificativa, taxa de falsos positivos na semana, recomendações de ajuste manual)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron semanal (domingo 03h00) para recalibração geral + chamado pelo Orion quando taxa de falsos positivos do Argus supera 30% na semana + onboarding de novo pipeline."
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

# Calibrar Thresholds Baseline

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calibrar Thresholds Baseline |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — O Calibrador de Baseline) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável pelo aprendizado contínuo dos padrões normais de cada pipeline. Na fase de Discovery/onboarding, analisa 30 dias de histórico para definir os thresholds iniciais. Em operação continua, recalibra os thresholds semanalmente para adaptar a mudanças de volume (crescimento do negócio, sazonalidade). Também monitora a taxa de falsos positivos do Argus: se o Argus está alertando demais para eventos normais, Nexus ajusta os thresholds para cima com justificativa. Gera o Calibration Report semanal para revisão humana.

## Input

- Histórico de execuções dos últimos 30-90 dias por pipeline (rows, latência, error rate, schema versions), log de incidentes resolvidos (para distinguir anomalias reais de falsos positivos), calendário do negócio (feriados, campanhas, sazonalidade), feedback humano sobre alertas (true positive / false positive tagging no ClickUp)

## Output

- anomaly_config.json atualizado por pipeline (thresholds de volume [min/max por hora/dia/semana], latência máxima aceitável, null_rate_threshold por coluna, schema_stability_score, criticidade do pipeline)
- Calibration Report semanal (Markdown: pipelines recalibrados, thresholds alterados com justificativa, taxa de falsos positivos na semana, recomendações de ajuste manual)

## Trigger

Cron semanal (domingo 03h00) para recalibração geral + chamado pelo Orion quando taxa de falsos positivos do Argus supera 30% na semana + onboarding de novo pipeline.

## Knowledge base (o que o executor consulta)

- Histórico de execuções por pipeline (90 dias rolling), log de incidentes com classificação true/false positive, calendário de sazonalidade do negócio, benchmarks de volume por tipo de fonte (API REST vs
- database CDC vs
- file-based), histórico de alterações de configuração de thresholds com resultado

## Action Items

1. Confirmar o gatilho e carregar a entrada (Histórico de execuções dos últimos 30-90 dias por pipeline (rows, latência, error rate, schema versions), log de incide…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (anomaly_config.json atualizado por pipeline (thresholds de volume [min/max por hora/dia/semana], latência máxima aceitá…) e persistir no artefato do squad.
4. Entregar ao critic Vega 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: anomaly_config.json atualizado por pipeline (thresholds de volume [min/max por hora/dia/semana], latência máxima aceitável, null_rate_threshold por coluna, sch…
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

- **to:** Vega
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
