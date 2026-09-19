---
task: orionPipeline()
responsavel: "Orion"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Incident Card no ClickUp por anomalia detectada (prova de trabalho verificavel): (1) Alerta estruturado do Argus"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "pipeline, timestamp, anomaly_type, severity, evidencia bruta"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Root Cause Report do Remi"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "root cause confirmado, confidence score, evidence chain, recommended action"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Verification Report do Vega"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "verdict APPROVED/BLOCKED com justificativa por dimensao"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestra o ciclo completo de detecção -> diagnóstico -> recuperação -> documentação. Mantém o estado de todos os pipelines monitorados, prioriza incidentes por impacto downstream, delega para os wor…"
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

# Orquestrar Pipeline do Self-Healing ETL Squad

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Self-Healing ETL Squad |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — O Maestro de Confiabilidade) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 11 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestra o ciclo completo de detecção -> diagnóstico -> recuperação -> documentação. Mantém o estado de todos os pipelines monitorados, prioriza incidentes por impacto downstream, delega para os workers especializados na sequência correta e garante que cada incidente gere uma prova de trabalho verificável no ClickUp. Em modo normal, opera em background orquestrando o Monitor Argus e recebendo alertas. Em modo incidente, assume controle ativo: coleta diagnóstico do Remi, decide se aciona recuperação automática (Finn) ou escalonamento HITL (L3 via Loki). Mantém o registro de estado de cada pipeline no Supabase. Nunca executa ação destrutiva diretamente — sempre delega para worker especializado com validação do Vega.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Incident Card no ClickUp por anomalia detectada (prova de trabalho verificavel): (1) Alerta estruturado do Argus
- pipeline, timestamp, anomaly_type, severity, evidencia bruta
- (2) Root Cause Report do Remi
- root cause confirmado, confidence score, evidence chain, recommended action
- (3) Verification Report do Vega
- verdict APPROVED/BLOCKED com justificativa por dimensao
- (4) Recovery Action Record do Finn (para auto-resolucao) OU Fix Plan do Coda (para HITL L3)
- acao tomada, resultado, rows recovered, freshness restored at
- (5) Post-recovery freshness timestamp confirmando que o pipeline voltou ao SLA
- (6) Task fechada no ClickUp com historico completo de timestamps por etapa (MTTD e MTTR calculados automaticamente)
- Bonus semanal: Weekly Incident Report com metricas agregadas de confiabilidade e ROI de horas salvas

## Trigger

Orquestra o ciclo completo de detecção -> diagnóstico -> recuperação -> documentação. Mantém o estado de todos os pipelines monitorados, prioriza incidentes por impacto downstream, delega para os workers especializados na sequência correta e garante que cada incidente gere uma prova de trabalho verificável no ClickUp. Em modo normal, opera em background orquestrando o Monitor Argus e recebendo alertas. Em modo incidente, assume controle ativo: coleta diagnóstico do Remi, decide se aciona recuperação automática (Finn) ou escalonamento HITL (L3 via Loki). Mantém o registro de estado de cada pipeline no Supabase. Nunca executa ação destrutiva diretamente — sempre delega para worker especializado com validação do Vega.

## Knowledge base (o que o executor consulta)

- Airbyte / Matillion / Workato / Peliqan
- ETL tools principais: webhooks de execução (success/failure), API para reexecução de runs (Finn), acesso a logs de run, configuração de schedules
- Supabase / Postgres / BigQuery / Snowflake
- destinos de dados: acesso de leitura para schema inspection (Argus, Rémi), acesso de escrita limitado a staging para patches (Finn), schema history e fingerprints (Nexus)
- ClickUp (Brain² / Super Agents / Autopilot Agents + MCP)
- hub de tasks e prova de trabalho: task por incidente (Loki), HITL L³ approval flow, Weekly Reports, integração com AIOX via espelhamento de workflow
- notificações em tempo real: P1/P2 alertas imediatos com context card (pipeline, root cause, ação tomada ou pendente), HITL L3 aprovação urgente, Weekly Incident Report no canal #data-reliability
- observabilidade OTEL: tracing de cada incidente (deteccao -> diagnostico -> validacao -> recuperacao), evals automatizados por tipo de root cause, quality gates (dev 70% / staging 85% / prod 95% task success), dashboard de MTTR e MTTD por pipeline
- PagerDuty / Datadog / incident.io
- AIOps integration: receber alertas de infra correlacionados (ex: source database down confirmado pelo Datadog antes do Remi investigar), escalonamento de P1 para on-call engineer via PagerDuty quando HITL nao responde no SLA
- GitHub / GitLab
- acesso de leitura ao repositório de transformações (Coda para identificar linha exata do bug), PR automático com fix sugerido para aprovação humana em casos de transformation bug
- dbt (se aplicável)
- acesso a manifests e lineage graph para mapeamento de dependências downstream (Rémi/Coda), identificação de modelos afetados por schema drift
- Claude Agent SDK / LangGraph
- orquestração multi-agente (Orion coordenando Argus, Rémi, Finn, Coda, Nexus, Vega, Loki), state management do pipeline de incidentes
- MCP Servers (camada de integração universal)
- ClickUp MCP, Supabase MCP, GitHub MCP para acesso padronizado sem implementação custom por cliente

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Vega 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Incident Card no ClickUp por anomalia detectada (prova de trabalho verificavel): (1) Alerta estruturado do Argus
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

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
