---
task: filtro()
responsavel: "Filtro"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição completa da call, campos BANT preenchidos pelo Vox Agent, roteiro de referência, regras de compliance configuradas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score de qualidade da call (0-100), veredicto de qualificação (VÁLIDO/SUSPEITO/INVÁLIDO), flags de compliance (se houver), lista de campos BANT que precisam de confirmação humana, recomendação de próximo passo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Imediatamente após o encerramento de cada call pelo Vox Agent. Quando Vox sinaliza qualificação positiva antes de passar ao Worker de Agendamento."
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

# Analisar Transcricao Call

**Task ID:** `filtro()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Transcricao Call |
| **status** | `pending` |
| **responsible_executor** | Filtro (Filtro (Critic/Verifier de Qualificação e Compliance)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analisa a transcrição da call em tempo real (ou pós-call em <2s) para verificar: (1) se o roteiro foi seguido sem desvios críticos, (2) se os campos BANT foram genuinamente preenchidos ou assumidos, (3) se houve promessas comerciais não autorizadas, (4) se o tom foi adequado ao perfil do prospect, (5) compliance com regras de LGPD e opt-out. Bloqueia leads mal qualificados de avançarem no funil sem revisão humana.

## Input

- Transcrição completa da call, campos BANT preenchidos pelo Vox Agent, roteiro de referência, regras de compliance configuradas

## Output

- Score de qualidade da call (0-100), veredicto de qualificação (VÁLIDO/SUSPEITO/INVÁLIDO), flags de compliance (se houver), lista de campos BANT que precisam de confirmação humana, recomendação de próximo passo

## Trigger

Imediatamente após o encerramento de cada call pelo Vox Agent. Quando Vox sinaliza qualificação positiva antes de passar ao Worker de Agendamento.

## Knowledge base (o que o executor consulta)

- Criterios BANT/MEDDIC da empresa cliente, regras de compliance LGPD (lista de opt-out, horários proibidos), histórico de calls com veredicto de qualidade para calibragem contínua, thresholds de score por vertical

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcrição completa da call, campos BANT preenchidos pelo Vox Agent, roteiro de referência, regras de compliance confi…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score de qualidade da call (0-100), veredicto de qualificação (VÁLIDO/SUSPEITO/INVÁLIDO), flags de compliance (se houve…) e persistir no artefato do squad.
4. Entregar ao critic Filtro 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score de qualidade da call (0-100), veredicto de qualificação (VÁLIDO/SUSPEITO/INVÁLIDO), flags de compliance (se houver), lista de campos BANT que precisam de…
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

- **to:** Agenda
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
