---
task: argus()
responsavel: "Argus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Registro de pipelines ativos com anomaly_config.json por pipeline (thresholds calibrados pelo Nexus), webhooks de execução do ETL tool (Airbyte/Matillion/Workato), acesso de leitura ao schema atual das tabelas de destino (Supabase/Postgres/BigQuery/Snowflake), log de execuções das últimas 24h"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Evento de anomalia (JSON estruturado: pipeline_id, timestamp, anomaly_type [SCHEMA_DRIFT | SOURCE_DOWN | VOLUME_ANOMALY | HIGH_ERROR_RATE | FRESHNESS_VIOLATION | NULL_EXPLOSION], severity [P1-P4], evidência bruta, upstream_pipelines_affected, downstream_pipelines_affected, last_successful_run)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Também emite HEARTBEAT a cada ciclo para confirmar que o monitoramento está ativo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron a cada 5 minutos (configurável por pipeline por criticidade: pipelines P1 a cada 1min, P4 a cada 15min) + webhooks de failure de execução do ETL tool + chamada manual do Orion."
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

# Monitorar Pipelines

**Task ID:** `argus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Pipelines |
| **status** | `pending` |
| **responsible_executor** | Argus (Argus — O Vigia de Pipelines) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente todos os pipelines registrados. Verifica freshness (ultima execucao bem-sucedida vs. freshness_sla configurado), volume (rows ingested vs. baseline +- threshold), schema fingerprint (hash do schema atual vs. ultimo conhecido) e error rate (erros na janela de 1h vs. baseline). Gera eventos de anomalia estruturados com severity, pipeline_id, anomaly_type e evidencia bruta. Opera em modo polling (configurable: 1-15min) ou event-driven via webhooks do ETL tool.

## Input

- Registro de pipelines ativos com anomaly_config.json por pipeline (thresholds calibrados pelo Nexus), webhooks de execução do ETL tool (Airbyte/Matillion/Workato), acesso de leitura ao schema atual das tabelas de destino (Supabase/Postgres/BigQuery/Snowflake), log de execuções das últimas 24h

## Output

- Evento de anomalia (JSON estruturado: pipeline_id, timestamp, anomaly_type [SCHEMA_DRIFT | SOURCE_DOWN | VOLUME_ANOMALY | HIGH_ERROR_RATE | FRESHNESS_VIOLATION | NULL_EXPLOSION], severity [P1-P4], evidência bruta, upstream_pipelines_affected, downstream_pipelines_affected, last_successful_run)
- Também emite HEARTBEAT a cada ciclo para confirmar que o monitoramento está ativo

## Trigger

Cron a cada 5 minutos (configurável por pipeline por criticidade: pipelines P1 a cada 1min, P4 a cada 15min) + webhooks de failure de execução do ETL tool + chamada manual do Orion.

## Knowledge base (o que o executor consulta)

- Registro de pipelines com anomaly_config.json (thresholds por pipeline), histórico de execuções (30 dias), schema fingerprints por tabela (versão atual e anterior), mapa de dependências upstream/downstream, SLAs de freshness por pipeline, calendário de manutenção de fontes externas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Registro de pipelines ativos com anomaly_config.json por pipeline (thresholds calibrados pelo Nexus), webhooks de execu…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Evento de anomalia (JSON estruturado: pipeline_id, timestamp, anomaly_type [SCHEMA_DRIFT | SOURCE_DOWN | VOLUME_ANOMALY…) e persistir no artefato do squad.
4. Entregar ao critic Vega 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Evento de anomalia (JSON estruturado: pipeline_id, timestamp, anomaly_type [SCHEMA_DRIFT | SOURCE_DOWN | VOLUME_ANOMALY | HIGH_ERROR_RATE | FRESHNESS_VIOLATION…
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

- **to:** Remi
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
