---
task: coda()
responsavel: "Coda"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Root Cause Report do Remi (incluindo fix_plan_for_human), codigo-fonte das transformacoes envolvidas (acesso de leitura ao repositorio), schema atual e desejado das tabelas afetadas, historico de incidentes similares anteriores, documentacao da fonte externa (changelog de API, se disponivel), impacto downstream mapeado pelo Remi"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Fix Plan Document (Markdown estruturado: resumo executivo em 3 linhas, root cause confirmado, acoes passo-a-passo numeradas com responsavel e SLA estimado, DDL/codigo de fix com syntax highlight, rollback procedure, impacto se nao corrigido em 1h/6h/24h, opcoes alternativas com trade-offs, custo estimado de execucao)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tambem gera o contexto estruturado para a task HITL L3 no ClickUp (titulo, descricao, checklist de aprovacao, assignee sugerido, deadline recomendado)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Chamado pelo Orion quando o Root Cause Report do Remi classifica a acao necessaria como IRREVERSIBLE ou severity P1-P2 sem acao automatica segura disponivel. Tambem chamado quando o Finn falha em rec…"
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

# Gerar Plano De Remediacao

**Task ID:** `coda()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Plano De Remediacao |
| **status** | `pending` |
| **responsible_executor** | Coda (Códa — O Arquiteto de Fíx) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Atua exclusivamente em incidentes P1-P2 ou ações irreversíveis. Recebe o Root Cause Report do Remi e produz um plano de remediação detalhado e executável para aprovação humana (L3): o que exatamente fazer, em que ordem, qual o impacto esperado, qual o rollback se der errado, qual o custo estimado (em horas e em compute/storage). Para schema drift complexo, gera o DDL de migração com comentários explicativos. Para bugs em transformação, identifica a linha exata do código de transformação que falhou e sugere o fix com justificativa. Para source outage prolongada, mapeia opções de contingência (dado atrasado vs. dado parcial vs. dado de cache) e recomenda a melhor opção com trade-offs explicitados.

## Input

- Root Cause Report do Remi (incluindo fix_plan_for_human), codigo-fonte das transformacoes envolvidas (acesso de leitura ao repositorio), schema atual e desejado das tabelas afetadas, historico de incidentes similares anteriores, documentacao da fonte externa (changelog de API, se disponivel), impacto downstream mapeado pelo Remi

## Output

- Fix Plan Document (Markdown estruturado: resumo executivo em 3 linhas, root cause confirmado, acoes passo-a-passo numeradas com responsavel e SLA estimado, DDL/codigo de fix com syntax highlight, rollback procedure, impacto se nao corrigido em 1h/6h/24h, opcoes alternativas com trade-offs, custo estimado de execucao)
- Tambem gera o contexto estruturado para a task HITL L3 no ClickUp (titulo, descricao, checklist de aprovacao, assignee sugerido, deadline recomendado)

## Trigger

Chamado pelo Orion quando o Root Cause Report do Remi classifica a acao necessaria como IRREVERSIBLE ou severity P1-P2 sem acao automatica segura disponivel. Tambem chamado quando o Finn falha em recuperacao automatica e precisa escalar.

## Knowledge base (o que o executor consulta)

- Playbook de fixes por tipo de root cause (schema drift, source outage, transformation bug, data quality degradation), repositório de transformações do cliente (acesso de leitura), histórico de migração de schemas anteriores, documentação de APIs das fontes externas, runbook de contingência por pipeline crítico

## Action Items

1. Confirmar o gatilho e carregar a entrada (Root Cause Report do Remi (incluindo fix_plan_for_human), codigo-fonte das transformacoes envolvidas (acesso de leitura…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Fix Plan Document (Markdown estruturado: resumo executivo em 3 linhas, root cause confirmado, acoes passo-a-passo numer…) e persistir no artefato do squad.
4. Entregar ao critic Vega 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Fix Plan Document (Markdown estruturado: resumo executivo em 3 linhas, root cause confirmado, acoes passo-a-passo numeradas com responsavel e SLA estimado, DDL…
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
