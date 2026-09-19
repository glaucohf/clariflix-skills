---
task: cassandra()
responsavel: "Cassandra"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "implementation-plan-draft.yaml"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "status de tasks no ClickUp (via MCP polling ou webhook)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "histórico de onboardings similares"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "dados de saúde do cliente (logins, ativações, tickets abertos)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "risk-matrix.json na fase de planejamento"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "alertas graduados (Amber/Red) com contexto e recomendação de ação"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "atualização do campo 'risk_score' por marco no ClickUp"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "relatório semanal de desvios para o Maestro"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Plano publicado no ClickUp (inicia monitoramento); webhook de task com status 'overdue'; polling diário às 08h; marco com data em menos de 3 dias úteis sem conclusão"
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

# Monitorar Desvios De Cronograma

**Task ID:** `cassandra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Desvios De Cronograma |
| **status** | `pending` |
| **responsible_executor** | Cassandra (Cassandra — Agente de Risco e Monitoramento) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Motor preditivo de risco e monitor contínuo de delivery. Em fase de planejamento, analisa o plano e histórico para identificar riscos antes do projeto começar (dependências sem owner, integrações técnicas subestimadas, marcos sem buffer, cliente sem ponto focal definido). Em fase de execução, monitora o ClickUp em tempo real, detecta desvios de cronograma (tarefa atrasada >2 dias úteis, marco em risco), calcula probabilidade de atraso e emite alertas graduados por severidade (Amber/Red). Nunca envia comunicação externa sozinha — escala para Hermes ou HITL.

## Input

- implementation-plan-draft.yaml
- status de tasks no ClickUp (via MCP polling ou webhook)
- histórico de onboardings similares
- dados de saúde do cliente (logins, ativações, tickets abertos)

## Output

- risk-matrix.json na fase de planejamento
- alertas graduados (Amber/Red) com contexto e recomendação de ação
- atualização do campo 'risk_score' por marco no ClickUp
- relatório semanal de desvios para o Maestro

## Trigger

Plano publicado no ClickUp (inicia monitoramento); webhook de task com status 'overdue'; polling diário às 08h; marco com data em menos de 3 dias úteis sem conclusão

## Knowledge base (o que o executor consulta)

- Histórico de onboardings com padrões de atraso (quais tarefas atrasam mais, em qual semana, em qual segmento), benchmarks de TTV por produto, regras de negócio de SLA de onboarding, perfil de risco por tipo de integração técnica

## Action Items

1. Confirmar o gatilho e carregar a entrada (implementation-plan-draft.yaml).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (risk-matrix.json na fase de planejamento) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: risk-matrix.json na fase de planejamento
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

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
