---
task: vega()
responsavel: "Vega"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Root Cause Report do Remi (root_cause, recommended_action, reversibility, severity), mapa de dependencias downstream do pipeline afetado, historico de acoes anteriores com resultado (sucesso/falha/efeito colateral), limites de acao configurados no recovery_policy.json (quais acoes estao pre-autorizadas por tipo e contexto)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Verification Report (JSON: verdict [APPROVED | BLOCKED | ESCALATE_HITL], checks_passed [lista de dimensoes aprovadas], checks_failed [lista de dimensoes reprovadas com justificativa], blast_radius_assessment, rollback_feasibility_score 0-100, override_possible [true/false"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "se humano pode aprovar mesmo com BLOCKED], escalation_reason [preenchido apenas em BLOCKED/ESCALATE_HITL])"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orion SEMPRE antes de acionar o Finn para qualquer ação automática. Não há bypass — toda ação passa pelo Vega. Também chamado quando o Coda finaliza um Fix Plan antes de enviar para HITL…"
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

# Verificar Ações Automaticas

**Task ID:** `vega()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Ações Automaticas |
| **status** | `pending` |
| **responsible_executor** | Vega (Vega — O Verificador de Ações) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Critic/Verifier do squad. Valida TODA ação automática antes da execução pelo Finn. Recebe o Root Cause Report + ação proposta e verifica 4 dimensões: (1) Proporcionalidade — a ação proposta é a mínima necessária para resolver o problema? (2) Reversibilidade — a ação pode ser desfeita em < 30min se produzir efeito colateral? (3) Scope — a ação afeta apenas o pipeline/tabela identificada ou tem blast radius maior? (4) Precedente — essa combinação de root_cause + ação já foi executada antes com sucesso? Se todas as 4 dimensões passam, emite APPROVED. Se qualquer falha, emite BLOCKED com justificativa e escalona para HITL L3 independente da classificação original do Remi.

## Input

- Root Cause Report do Remi (root_cause, recommended_action, reversibility, severity), mapa de dependencias downstream do pipeline afetado, historico de acoes anteriores com resultado (sucesso/falha/efeito colateral), limites de acao configurados no recovery_policy.json (quais acoes estao pre-autorizadas por tipo e contexto)

## Output

- Verification Report (JSON: verdict [APPROVED | BLOCKED | ESCALATE_HITL], checks_passed [lista de dimensoes aprovadas], checks_failed [lista de dimensoes reprovadas com justificativa], blast_radius_assessment, rollback_feasibility_score 0-100, override_possible [true/false
- se humano pode aprovar mesmo com BLOCKED], escalation_reason [preenchido apenas em BLOCKED/ESCALATE_HITL])

## Trigger

Chamado pelo Orion SEMPRE antes de acionar o Finn para qualquer ação automática. Não há bypass — toda ação passa pelo Vega. Também chamado quando o Coda finaliza um Fix Plan antes de enviar para HITL (para garantir que o plano proposto é seguro de executar).

## Knowledge base (o que o executor consulta)

- recovery_policy.json (política de ações permitidas por tipo de pipeline e criticidade), histórico de ações executadas com resultado e efeitos colaterais, mapa de dependências atualizado (quais pipelines/dashboards/relatórios dependem de cada tabela), limites de escopo de cada ação (ex: BACKFILL_TRIGGER limitado a max 24h de dados)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Root Cause Report do Remi (root_cause, recommended_action, reversibility, severity), mapa de dependencias downstream do…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Verification Report (JSON: verdict [APPROVED | BLOCKED | ESCALATE_HITL], checks_passed [lista de dimensoes aprovadas],…) e persistir no artefato do squad.
4. Entregar ao critic Vega 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Verification Report (JSON: verdict [APPROVED | BLOCKED | ESCALATE_HITL], checks_passed [lista de dimensoes aprovadas], checks_failed [lista de dimensoes reprov…
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

- **to:** Loki
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
