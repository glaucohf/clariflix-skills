---
task: finn()
responsavel: "Finn"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Root Cause Report do Remi (root_cause, recommended_action, parâmetros), validação do Vega (APPROVED), acesso de escrita ao ETL tool para reexecução de runs, acesso de escrita limitado ao schema de staging (NÃO de produção diretamente), configuração de ações permitidas por pipeline (quais ações estão habilitadas por tipo de pipeline e criticidade)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Recovery Action Record (JSON: action_taken, action_params, execution_timestamp, result [SUCCESS | PARTIAL | FAILED], rows_recovered, freshness_restored_at, side_effects, rollback_procedure_if_needed)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Em caso de FAILED, gera Escalation Request para o Orion com contexto completo para HITL L3"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orion após Root Cause Report do Remi + validação APPROVED do Vega, SOMENTE para ações reversíveis em pipelines P3-P4 (ou P2 com autorização explícita). NUNCA chamado diretamente — sempre…"
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

# Curar Falhas Reversíveis

**Task ID:** `finn()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Curar Falhas Reversíveis |
| **status** | `pending` |
| **responsible_executor** | Finn (Finn — O Curador de Recuperação) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa a recuperação automática para falhas classificadas como reversíveis e de baixa criticidade (P3-P4 por padrão, P2 mediante autorização do Orion). Tem um catálogo de ações de recuperação padrão: RETRY (reexecuta a run falhada com backoff exponencial), SKIP_AND_ALERT (marca a run como skipped e notifica sem bloquear o pipeline), SCHEMA_PATCH (aplica patch automático em casos de schema drift simples: novo campo opcional, renomeação mapeável), SOURCE_FAILOVER (troca para fonte de backup configurada), QUARANTINE_AND_CONTINUE (move registros anômalos para tabela de quarentena e continua ingestão dos válidos), BACKFILL_TRIGGER (dispara reprocessamento da janela afetada, limitado a 24h de dados para evitar custos excessivos). Nunca executa ações em tabelas de produção sem validação do Vega.

## Input

- Root Cause Report do Remi (root_cause, recommended_action, parâmetros), validação do Vega (APPROVED), acesso de escrita ao ETL tool para reexecução de runs, acesso de escrita limitado ao schema de staging (NÃO de produção diretamente), configuração de ações permitidas por pipeline (quais ações estão habilitadas por tipo de pipeline e criticidade)

## Output

- Recovery Action Record (JSON: action_taken, action_params, execution_timestamp, result [SUCCESS | PARTIAL | FAILED], rows_recovered, freshness_restored_at, side_effects, rollback_procedure_if_needed)
- Em caso de FAILED, gera Escalation Request para o Orion com contexto completo para HITL L3

## Trigger

Chamado pelo Orion após Root Cause Report do Remi + validação APPROVED do Vega, SOMENTE para ações reversíveis em pipelines P3-P4 (ou P2 com autorização explícita). NUNCA chamado diretamente — sempre via Orion + Vega.

## Knowledge base (o que o executor consulta)

- Catálogo de ações de recuperação com pré-condições e pós-condições, configuração de ações permitidas por pipeline (recovery_policy.json), schema de staging e produção por tabela, histórico de recuperações anteriores com taxa de sucesso por ação, limites de custo para backfill automático (ex: max 24h de dados, max X GB)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Root Cause Report do Remi (root_cause, recommended_action, parâmetros), validação do Vega (APPROVED), acesso de escrita…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Recovery Action Record (JSON: action_taken, action_params, execution_timestamp, result [SUCCESS | PARTIAL | FAILED], ro…) e persistir no artefato do squad.
4. Entregar ao critic Vega 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Recovery Action Record (JSON: action_taken, action_params, execution_timestamp, result [SUCCESS | PARTIAL | FAILED], rows_recovered, freshness_restored_at, sid…
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

- **to:** Coda
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
