---
task: remi()
responsavel: "Remi"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de anomalia do Argus (anomaly_type, severity, evidência bruta), acesso de leitura aos logs completos da run falhada no ETL tool, acesso de leitura ao schema atual e ao schema anterior (fingerprint history), amostra de 500 registros da última ingestão, histórico de incidentes anteriores do mesmo pipeline (para correlação de padrões recorrentes), calendário de manutenção de fontes externas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Root Cause Report (JSON: root_cause [SCHEMA_DRIFT | SOURCE_OUTAGE | SEASONAL_VOLUME | TRANSFORMATION_BUG | DATA_QUALITY_DEGRADATION | UNKNOWN], confidence_score 0-100, evidence_chain [lista de checagens e resultados], severity_final [P1-P4], reversibility [REVERSIBLE | IRREVERSIBLE | UNKNOWN], recommended_action [tipo de ação + parâmetros], estimated_recovery_time, downstream_impact_assessment, fix_plan_for_human [preenchido apenas para ações irreversíveis ou P1-P2])"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orion imediatamente após receber evento de anomalia do Argus. SLA interno: diagnóstico completo em < 5 minutos para P1-P2, < 15 minutos para P3-P4."
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

# Testar Hipóteses Sequenciais

**Task ID:** `remi()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Testar Hipóteses Sequenciais |
| **status** | `pending` |
| **responsible_executor** | Remi (Rémi — O Diagnosticador de Root Cause) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o evento de anomalia do Argus e executa diagnostico sistematico de root cause em ate 5 minutos. Testa hipoteses em sequencia de custo crescente: (1) fonte externa down — testa conectividade e ultimas respostas da API de origem, (2) schema drift — compara schema atual com fingerprint anterior e identifica campos adicionados/removidos/renomeados/retiped, (3) volume anomaly — verifica se e sazonalidade esperada (feriado, fim de mes) ou anomalia real, (4) transformacao com erro — inspeciona logs da ultima run, identifica a step exata que falhou, (5) data quality — amostra 100-500 registros da ultima ingestao e verifica nulos, tipos incorretos, valores fora de range. Classifica severidade final e reversibilidade da acao necessaria.

## Input

- Evento de anomalia do Argus (anomaly_type, severity, evidência bruta), acesso de leitura aos logs completos da run falhada no ETL tool, acesso de leitura ao schema atual e ao schema anterior (fingerprint history), amostra de 500 registros da última ingestão, histórico de incidentes anteriores do mesmo pipeline (para correlação de padrões recorrentes), calendário de manutenção de fontes externas

## Output

- Root Cause Report (JSON: root_cause [SCHEMA_DRIFT | SOURCE_OUTAGE | SEASONAL_VOLUME | TRANSFORMATION_BUG | DATA_QUALITY_DEGRADATION | UNKNOWN], confidence_score 0-100, evidence_chain [lista de checagens e resultados], severity_final [P1-P4], reversibility [REVERSIBLE | IRREVERSIBLE | UNKNOWN], recommended_action [tipo de ação + parâmetros], estimated_recovery_time, downstream_impact_assessment, fix_plan_for_human [preenchido apenas para ações irreversíveis ou P1-P2])

## Trigger

Chamado pelo Orion imediatamente após receber evento de anomalia do Argus. SLA interno: diagnóstico completo em < 5 minutos para P1-P2, < 15 minutos para P3-P4.

## Knowledge base (o que o executor consulta)

- Histórico de incidentes anteriores por pipeline (root causes e resoluções), documentação das fontes externas (endpoints, SLAs, histórico de outages), schema history por tabela (últimas 10 versões com diff), playbook de root causes conhecidos com ações de recuperação padrão, calendário de sazonalidade do negócio (feriados, campanhas, datas críticas)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de anomalia do Argus (anomaly_type, severity, evidência bruta), acesso de leitura aos logs completos da run falh…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Root Cause Report (JSON: root_cause [SCHEMA_DRIFT | SOURCE_OUTAGE | SEASONAL_VOLUME | TRANSFORMATION_BUG | DATA_QUALITY…) e persistir no artefato do squad.
4. Entregar ao critic Vega 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Root Cause Report (JSON: root_cause [SCHEMA_DRIFT | SOURCE_OUTAGE | SEASONAL_VOLUME | TRANSFORMATION_BUG | DATA_QUALITY_DEGRADATION | UNKNOWN], confidence_scor…
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

- **to:** Finn
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
