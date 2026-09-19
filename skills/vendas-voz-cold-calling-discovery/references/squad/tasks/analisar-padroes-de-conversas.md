---
task: insight()
responsavel: "Insight"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Batch de transcrições e gravações da semana, veredictos do Filtro Agent, taxa de conversão por roteiro/vertical/horário, feedback qualitativo do closer sobre qualidade dos leads entregues"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório semanal de Conversation Intelligence (PDF + dashboard): top 5 objeções da semana, frases com maior taxa de sucesso, momento médio de perda de interesse na call, score de aderência ao roteiro por ligação, sugestões de ajuste de roteiro priorizadas por impacto estimado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Encerramento da semana (trigger semanal automático). Quando taxa de conversão cai >15% em relação à média móvel de 4 semanas. Solicitação manual do gestor comercial."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Filtro 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3)."
    - "[ ] HITL: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3)."
    - "[ ] HITL: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3)."
    - "[ ] HITL: Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3)."
    - "[ ] HITL: Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation)."
---

# Analisar Padroes De Conversas

**Task ID:** `insight()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Padroes De Conversas |
| **status** | `pending` |
| **responsible_executor** | Insight (Insight (Worker de Conversation Intelligence e Coaching)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analisa o corpus de calls gravadas para identificar padrões de sucesso e fracasso: frases que aumentam taxa de agendamento, momentos de perda de interesse, objeções não tratadas, tempo médio por fase do roteiro. Gera relatório semanal de coaching com sugestões de melhoria de roteiro e calibragem do Vox Agent. Alimenta loop de melhoria contínua do squad.

## Input

- Batch de transcrições e gravações da semana, veredictos do Filtro Agent, taxa de conversão por roteiro/vertical/horário, feedback qualitativo do closer sobre qualidade dos leads entregues

## Output

- Relatório semanal de Conversation Intelligence (PDF + dashboard): top 5 objeções da semana, frases com maior taxa de sucesso, momento médio de perda de interesse na call, score de aderência ao roteiro por ligação, sugestões de ajuste de roteiro priorizadas por impacto estimado

## Trigger

Encerramento da semana (trigger semanal automático). Quando taxa de conversão cai >15% em relação à média móvel de 4 semanas. Solicitação manual do gestor comercial.

## Knowledge base (o que o executor consulta)

- Corpus de calls gravadas e transcritas, roteiros de referência por versão (para comparar A/B), benchmarks de mercado de taxa de conversão SDR, modelos de análise de sentimento e intenção conversacional

## Action Items

1. Confirmar o gatilho e carregar a entrada (Batch de transcrições e gravações da semana, veredictos do Filtro Agent, taxa de conversão por roteiro/vertical/horário…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório semanal de Conversation Intelligence (PDF + dashboard): top 5 objeções da semana, frases com maior taxa de su…) e persistir no artefato do squad.
4. Entregar ao critic Filtro 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório semanal de Conversation Intelligence (PDF + dashboard): top 5 objeções da semana, frases com maior taxa de sucesso, momento médio de perda de interes…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Filtro 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3).
- [ ] Gate HITL respeitado: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3).
- [ ] Gate HITL respeitado: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3).

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3). | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3). | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3). | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3). | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation). | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Confirmação de reagendamento quando prospect cancela reunião pela segunda vez consecutiva (decisão humana sobre continuar ou desqualificar — L3). | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibragem quinzenal de voz e persona do Vox Agent com gestor de vendas (revisão humana de amostras de áudio — L1). | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Filtro 2 | BLOQUEIA entrega |

## Handoff

- **to:** Filtro 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
