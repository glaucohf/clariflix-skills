---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Base de leads com campos de CRM, sinais de intenção (visitas ao site, abertura de emails, engajamento social), histórico de interações, critérios de ICP configurados pelo cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Fila de discagem priorizada e ordenada por score (JSON), score individual de cada lead (0-100) com breakdown de fatores, leads marcados como Alta Prioridade notificados ao gestor comercial, relatório de distribuição de score semanal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo lead adicionado ao CRM. Sinal de intenção detectado para lead existente. Revisão periódica da fila (a cada 4 horas). Antes de cada sessão de discagem do Vox Agent."
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

# Ranquear Leads

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Ranquear Leads |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar (Worker de Lead Scoring e Priorização de Fila)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pontua e re-ranqueia continuamente todos os leads da fila de discagem com base em: completude do enriquecimento, sinais de intencao detectados, fit com ICP, historico de interacoes anteriores e urgencia de timing (ex: lead que visitou pagina de preco = score alto). Garante que Vox Agent sempre disca o lead com maior probabilidade de conversao no momento certo.

## Input

- Base de leads com campos de CRM, sinais de intenção (visitas ao site, abertura de emails, engajamento social), histórico de interações, critérios de ICP configurados pelo cliente

## Output

- Fila de discagem priorizada e ordenada por score (JSON), score individual de cada lead (0-100) com breakdown de fatores, leads marcados como Alta Prioridade notificados ao gestor comercial, relatório de distribuição de score semanal

## Trigger

Novo lead adicionado ao CRM. Sinal de intenção detectado para lead existente. Revisão periódica da fila (a cada 4 horas). Antes de cada sessão de discagem do Vox Agent.

## Knowledge base (o que o executor consulta)

- Modelo de scoring do cliente (pesos por critério de ICP), histórico de conversões para calibragem do modelo, sinais de intenção via plataformas de intent data (se disponível), regras de negócio do cliente (territórios, segmentos prioritários)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Base de leads com campos de CRM, sinais de intenção (visitas ao site, abertura de emails, engajamento social), históric…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Fila de discagem priorizada e ordenada por score (JSON), score individual de cada lead (0-100) com breakdown de fatores…) e persistir no artefato do squad.
4. Entregar ao critic Filtro 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Fila de discagem priorizada e ordenada por score (JSON), score individual de cada lead (0-100) com breakdown de fatores, leads marcados como Alta Prioridade no…
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

- **to:** Insight
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
