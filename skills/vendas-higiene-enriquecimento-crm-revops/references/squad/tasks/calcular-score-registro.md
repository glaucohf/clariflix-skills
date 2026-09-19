---
task: pythia()
responsavel: "Pythia"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Registro CRM completo com todos os campos e metadados de validação/enriquecimento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score card: { contact_id, quality_score: 0-100, tier: gold|silver|bronze, missing_critical_fields: [], last_enriched: date, recommendation: string }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Atualizado como campo customizado no CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Dashboard agregado exportado para ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Após qualquer update de enriquecimento ou validação; agendamento semanal para re-scoring da base completa; solicitação de relatório pelo operador RevOps."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)"
    - "[ ] HITL: Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)"
    - "[ ] HITL: Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)"
    - "[ ] HITL: Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal)"
    - "[ ] HITL: Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente)"
---

# Calcular Score Registro

**Task ID:** `pythia()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Higiene e Enriquecimento de CRM (RevOps)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Score Registro |
| **status** | `pending` |
| **responsible_executor** | Pythia (Pythia (Scorer de Qualidade de Registro)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Calcula score de completude e qualidade de cada registro (0-100) com base em: campos obrigatórios preenchidos (peso 40%), campos críticos para scoring preenchidos (peso 30%), dados validados sem flags de erro (peso 20%), data de último enriquecimento <90 dias (peso 10%). Segmenta base em: Gold (>80), Silver (60-80), Bronze (<60). Registros Bronze com deal aberto disparam alerta prioritário.

## Input

- Registro CRM completo com todos os campos e metadados de validação/enriquecimento

## Output

- Score card: { contact_id, quality_score: 0-100, tier: gold|silver|bronze, missing_critical_fields: [], last_enriched: date, recommendation: string }
- Atualizado como campo customizado no CRM
- Dashboard agregado exportado para ClickUp

## Trigger

Após qualquer update de enriquecimento ou validação; agendamento semanal para re-scoring da base completa; solicitação de relatório pelo operador RevOps.

## Knowledge base (o que o executor consulta)

- Pesos de campos por importância para o ICP do cliente (definidos no onboarding)
- Histórico de scores para detectar degradação de qualidade ao longo do tempo
- Benchmarks de taxa de completude por setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Registro CRM completo com todos os campos e metadados de validação/enriquecimento).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score card: { contact_id, quality_score: 0-100, tier: gold|silver|bronze, missing_critical_fields: [], last_enriched: d…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score card: { contact_id, quality_score: 0-100, tier: gold|silver|bronze, missing_critical_fields: [], last_enriched: date, recommendation: string }
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual)
- [ ] Gate HITL respeitado: Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3)
- [ ] Gate HITL respeitado: Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez)

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de merges de duplicatas com confidence score 0.75-0.89 (Gemini, fila no Slack/ClickUp com justificativa e diff visual) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação de exclusão definitiva de registros marcados como 'podres' por Cassandra (irreversível — sempre L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de alteração em massa de campo crítico (ex: mudar setor de 200 registros de uma vez) | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Revisão de registros Golden Bronze com deal aberto (operador RevOps decide: enriquecer manualmente ou descartar deal) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Configuração inicial do playbook de golden record no onboarding (quem decide vence em cada campo — decisão estratégica do cliente) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de integração de nova fonte de dados ao pipeline (ex: adicionar novo formulário ou importação de lista de parceiro) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Cassandra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
