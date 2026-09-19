---
task: vega2Verificar()
responsavel: "Vega 2"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] L3: Ações irreversíveis ou P1-P2: qualquer ação que altere schema em produção, reprocesse mais de 24h de dados, faça rollback de tabela ou envolva custo de compute significativo requer aprovação explícita. Loki cria task no ClickUp com Fix Plan do Coda (checklist de aprovação) e notifica via Slack. SLA de resposta: P1 = 30min, P2 = 2h. Se SLA expirar sem resposta, Orion escala para gestor do pipeline."
    - "[ ] L3: Vega emite BLOCKED: quando a verificacao do Vega reprova qualquer dimensao (proporcionalidade, reversibilidade, scope, precedente), a acao e bloqueada independente da classificacao original. Requer override explicito humano com justificativa registrada."
    - "[ ] L3: Schema drift complexo: quando Remi identifica schema drift que não se enquadra nos patches automáticos seguros (ex: renomeação ambígua, remoção de campo usado downstream, mudança de tipo com perda de dados), o Coda prepara o plano de migração DDL completo para aprovação humana antes de qualquer alteração."
    - "[ ] L2: Revisão do Calibration Report semanal do Nexus: humano (engenheiro de dados responsável) revisa os thresholds recalibrados antes da aplicação. Não bloqueia operação, mas permite ajuste fino de sensibilidade por pipeline crítico."
    - "[ ] L2: Onboarding de novo pipeline: antes de iniciar monitoramento de um pipeline novo, humano valida o anomaly_config.json gerado pelo Nexus (thresholds, criticidade, recovery_policy) e confirma os assignees responsáveis por incidentes HITL."
---

# Verificar Saídas do Self-Healing ETL Squad

**Task ID:** `vega2Verificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Self-Healing ETL Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Self-Healing ETL Squad |
| **status** | `pending` |
| **responsible_executor** | Vega 2 (Vega – O Verificador de Ações) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Vega – O Verificador de Ações – Critic/Verifier do squad. Atua como gate obrigatório antes de TODA execução automática pelo Finn. Valida 4 dimensões (proporcionalidade, reversibilidade, scope/blast-radius, precedente) e emite veredicto APPROVED ou BLOCKED com justificativa estruturada. Opera em modo adversarial: assume que toda ação automática é potencialmente danosa até provar o contrário. Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 10%. Taxa alvo de falsos positivos (APPROVED quando devia ser BLOCKED): < 1%. Também realiza auditoria retroativa mensal de 20% dos incidentes auto-resolvidos para detectar deriva de qualidade nas decisões automáticas.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Vega – O Verificador de Ações – Critic/Verifier do squad
- Atua como gate obrigatório antes de TODA execução automática pelo Finn
- Valida 4 dimensões (proporcionalidade, reversibilidade, scope/blast-radius, precedente) e emite veredicto APPROVED ou BLOCKED com justificativa estruturada
- Opera em modo adversarial: assume que toda ação automática é potencialmente danosa até provar o contrário
- Taxa alvo de falsos negativos (BLOCKED quando devia ser APPROVED): < 10%
- Taxa alvo de falsos positivos (APPROVED quando devia ser BLOCKED): < 1%
- Também realiza auditoria retroativa mensal de 20% dos incidentes auto-resolvidos para detectar deriva de qualidade nas decisões automáticas

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Orion para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Orion
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
