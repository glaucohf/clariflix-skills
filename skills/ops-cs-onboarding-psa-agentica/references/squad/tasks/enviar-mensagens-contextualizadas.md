---
task: hermes()
responsavel: "Hermes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Alertas de risco do Cassandra (com severidade e contexto)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "instruções do Maestro"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "status de marcos"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "templates de mensagem por tipo de situação (atraso, pendência do cliente, marco concluído, go-live próximo)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens enviadas via Slack (time interno) e WhatsApp/email (cliente)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "log de comunicações no ClickUp"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "registro de 'pending_client_actions' para tracking de resposta"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "draft de mensagem para aprovação HITL em casos críticos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Alerta Amber do Cassandra → notificação interna no Slack; alerta Red → draft para aprovação HITL; marco concluído → mensagem de celebração para cliente; pendência do cliente sem resposta >48h → follo…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)"
    - "[ ] HITL: Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)"
    - "[ ] HITL: Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro"
    - "[ ] HITL: Aprovação do Delivery Status Report semanal antes do envio ao cliente"
    - "[ ] HITL: Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente"
---

# Enviar Mensagens Contextualizadas

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagens Contextualizadas |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — Agente de Comunicação e Notificações) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável por toda comunicação proativa com stakeholders internos e externos durante o onboarding. Recebe alertas do Cassandra ou instruções do Maestro e transforma em mensagens contextualizadas no canal correto (Slack para time interno, WhatsApp/email para cliente). Gerencia a sequência de follow-up para tarefas pendentes do cliente (ex: credenciais não enviadas, responsável não indicado). Nunca envia comunicação para o cliente sem aprovação HITL quando o conteúdo envolve mudança de escopo, atraso crítico ou impacto financeiro.

## Input

- Alertas de risco do Cassandra (com severidade e contexto)
- instruções do Maestro
- status de marcos
- templates de mensagem por tipo de situação (atraso, pendência do cliente, marco concluído, go-live próximo)

## Output

- Mensagens enviadas via Slack (time interno) e WhatsApp/email (cliente)
- log de comunicações no ClickUp
- registro de 'pending_client_actions' para tracking de resposta
- draft de mensagem para aprovação HITL em casos críticos

## Trigger

Alerta Amber do Cassandra → notificação interna no Slack; alerta Red → draft para aprovação HITL; marco concluído → mensagem de celebração para cliente; pendência do cliente sem resposta >48h → follow-up automatizado; 7 dias antes do go-live → checklist de pré-go-live para cliente

## Knowledge base (o que o executor consulta)

- Templates de comunicação por tipo de evento e tom (urgente, informativo, celebrativo), histórico de comunicações por cliente, preferências de canal por perfil de cliente, SLA de resposta esperada por tipo de pendência

## Action Items

1. Confirmar o gatilho e carregar a entrada (Alertas de risco do Cassandra (com severidade e contexto)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens enviadas via Slack (time interno) e WhatsApp/email (cliente)) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens enviadas via Slack (time interno) e WhatsApp/email (cliente)
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)
- [ ] Gate HITL respeitado: Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)
- [ ] Gate HITL respeitado: Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação do Delivery Status Report semanal antes do envio ao cliente | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Decisão de go/no-go para go-live quando health score < 60 ou mais de 2 marcos críticos em Red | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Iris
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
