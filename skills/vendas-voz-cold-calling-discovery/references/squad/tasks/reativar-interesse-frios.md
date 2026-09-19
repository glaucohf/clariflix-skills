---
task: eco()
responsavel: "Eco"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de leads frios com motivo de rejeição, cadência configurada (intervalos e canais), biblioteca de conteúdo de nurture por vertical, sinal de reengajamento (abertura de email, resposta de WhatsApp, nova visita ao site)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens enviadas por canal com timestamp, score de engajamento atualizado, leads reativados re-inseridos na fila do Vox Agent, relatório de cadência semanal no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead marcado como Sem Resposta apos 3 tentativas. Lead classificado como Nao Qualificado Agora com data de retorno. Sinal de reengajamento detectado (abertura de email, clique, resposta). Trigger de…"
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

# Reativar Interesse Frios

**Task ID:** `eco()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reativar Interesse Frios |
| **status** | `pending` |
| **responsible_executor** | Eco (Eco (Worker de Follow-up e Nurture de Frios)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia leads que não atenderam (sem resposta após 3 tentativas), não qualificaram agora (retorno em 30/60/90 dias) ou deram opt-out temporário. Executa cadências multi-canal (voz + WhatsApp + email) com mensagens de valor (caso de uso, insight de mercado, social proof) para reativar interesse sem ser invasivo. Aciona Vox Agent quando lead reabre engajamento.

## Input

- Lista de leads frios com motivo de rejeição, cadência configurada (intervalos e canais), biblioteca de conteúdo de nurture por vertical, sinal de reengajamento (abertura de email, resposta de WhatsApp, nova visita ao site)

## Output

- Mensagens enviadas por canal com timestamp, score de engajamento atualizado, leads reativados re-inseridos na fila do Vox Agent, relatório de cadência semanal no ClickUp

## Trigger

Lead marcado como Sem Resposta apos 3 tentativas. Lead classificado como Nao Qualificado Agora com data de retorno. Sinal de reengajamento detectado (abertura de email, clique, resposta). Trigger de calendari de reativacao (30/60/90 dias).

## Knowledge base (o que o executor consulta)

- Biblioteca de mensagens de nurture por vertical e por motivo de rejeição, regras de frequência máxima por canal (LGPD), score de engajamento histórico do lead, melhores horários de envio por perfil de prospect

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de leads frios com motivo de rejeição, cadência configurada (intervalos e canais), biblioteca de conteúdo de nurt…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens enviadas por canal com timestamp, score de engajamento atualizado, leads reativados re-inseridos na fila do V…) e persistir no artefato do squad.
4. Entregar ao critic Filtro 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens enviadas por canal com timestamp, score de engajamento atualizado, leads reativados re-inseridos na fila do Vox Agent, relatório de cadência semanal…
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

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
