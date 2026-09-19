---
task: atlas()
responsavel: "Átlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "project-brief.json (SOW parseado), template de plano de implementação, histórico de projetos similares (ex: mesmo segmento, mesmo produto contratado)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "implementation-plan-draft.yaml com fases, tarefas, subtarefas, owners, estimativas em dias, dependências e critérios de aceite por marco"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "pronto para revisão HITL e publicação no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: project-brief.json criado pelo Discovery; ou rascunho de plano existente marcado como 'needs-revision' pelo CSM"
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

# Criar Plano De Implementação

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Criar Plano De Implementação |
| **status** | `pending` |
| **responsible_executor** | Átlas (Átlas — Arquiteto de Projeto) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em decomposição de escopo e criação de plano de implementação. Lê o project-brief.json gerado no Discovery, quebra o escopo em fases MECE (Mutually Exclusive, Collectively Exhaustive), cria WBS (Work Breakdown Structure) com estimativas de esforço, dependências entre tarefas, owners por papel (CSM, cliente, tech, produto) e marcos com critérios de aceite mensuráveis. Gera o plano no formato nativo do ClickUp para publicação via MCP.

## Input

- project-brief.json (SOW parseado), template de plano de implementação, histórico de projetos similares (ex: mesmo segmento, mesmo produto contratado)

## Output

- implementation-plan-draft.yaml com fases, tarefas, subtarefas, owners, estimativas em dias, dependências e critérios de aceite por marco
- pronto para revisão HITL e publicação no ClickUp

## Trigger

project-brief.json criado pelo Discovery; ou rascunho de plano existente marcado como 'needs-revision' pelo CSM

## Knowledge base (o que o executor consulta)

- Biblioteca de planos de implementação anteriores (successes + failures), templates de WBS por tipo de produto/segmento, matriz de owners padrão por papel, critérios de aceite históricos aprovados por clientes

## Action Items

1. Confirmar o gatilho e carregar a entrada (project-brief.json (SOW parseado), template de plano de implementação, histórico de projetos similares (ex: mesmo segme…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (implementation-plan-draft.yaml com fases, tarefas, subtarefas, owners, estimativas em dias, dependências e critérios de…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: implementation-plan-draft.yaml com fases, tarefas, subtarefas, owners, estimativas em dias, dependências e critérios de aceite por marco
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

- **to:** Cassandra
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
