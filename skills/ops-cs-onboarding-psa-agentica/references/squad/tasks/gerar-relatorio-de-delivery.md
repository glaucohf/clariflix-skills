---
task: crono()
responsavel: "Crono"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Status de todas as tasks e marcos no ClickUp (via MCP)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "risk-matrix.json do Cassandra"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "health-score-report.json do Vitor"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "histórico de comunicações do Hermes"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "notas de calls da semana"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "delivery-status-report.md (versão executiva para cliente) + delivery-ops-briefing.md (versão operacional para time interno)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "atualização do dashboard de delivery no ClickUp"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "draft de email/WhatsApp para aprovação HITL antes do envio ao cliente"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo semanal automático (toda sexta-feira às 16h); solicitação do Maestro ou CSM; milestone crítico concluído ou Red Alert emitido; reunião de status com cliente agendada no calendário"
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

# Gerar Relatório De Delivery

**Task ID:** `crono()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Relatório De Delivery |
| **status** | `pending` |
| **responsible_executor** | Crono (Crono — Agente de Relatório de Delivery) |
| **execution_type** | `Agent` |
| **input** | 5 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerador de relatórios de status de delivery para consumo interno e externo. Toda semana consolida o estado atual do plano de implementação em um Delivery Status Report com semáforo RAG por fase e marco, % de conclusão geral, tasks concluídas vs. planejadas, desvios de cronograma acumulados, bloqueios ativos e projeção de go-live. Gera duas versões: executiva (para o cliente e sponsor) e operacional (para o time interno). Publica no Slack, ClickUp e envia para o cliente via email/WhatsApp mediante aprovação HITL.

## Input

- Status de todas as tasks e marcos no ClickUp (via MCP)
- risk-matrix.json do Cassandra
- health-score-report.json do Vitor
- histórico de comunicações do Hermes
- notas de calls da semana

## Output

- delivery-status-report.md (versão executiva para cliente) + delivery-ops-briefing.md (versão operacional para time interno)
- atualização do dashboard de delivery no ClickUp
- draft de email/WhatsApp para aprovação HITL antes do envio ao cliente

## Trigger

Ciclo semanal automático (toda sexta-feira às 16h); solicitação do Maestro ou CSM; milestone crítico concluído ou Red Alert emitido; reunião de status com cliente agendada no calendário

## Knowledge base (o que o executor consulta)

- Templates de relatório de delivery (executivo e operacional), histórico de relatórios anteriores do cliente, benchmarks de delivery do mercado, glossário de termos de status (RAG, milestone, etc.) adaptado ao vocabulário do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Status de todas as tasks e marcos no ClickUp (via MCP)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (delivery-status-report.md (versão executiva para cliente) + delivery-ops-briefing.md (versão operacional para time inte…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: delivery-status-report.md (versão executiva para cliente) + delivery-ops-briefing.md (versão operacional para time interno)
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

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
