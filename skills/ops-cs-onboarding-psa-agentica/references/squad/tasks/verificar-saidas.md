---
task: argusVerificar()
responsavel: "Argus"
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
    - "[ ] HITL: Revisão e aprovação do project-brief.json antes de criar o plano (CSM valida campos extraídos pela Iris com baixa confiança)"
    - "[ ] HITL: Aprovação do implementation-plan-draft.yaml antes da publicação no ClickUp (CSM/Gerente de CS valida fases, estimativas e owners)"
    - "[ ] HITL: Aprovação de qualquer comunicação para o cliente que envolva atraso crítico (Red Alert), mudança de escopo ou impacto financeiro"
    - "[ ] HITL: Aprovação do Delivery Status Report semanal antes do envio ao cliente"
    - "[ ] HITL: Ação em alertas Red de Cassandra que requeiram renegociação de prazo ou escalonamento para o executivo do cliente"
---

# Verificar Saídas do Onboarding & Implementação

**Task ID:** `argusVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Onboarding & Implementação (PSA Agêntica)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Onboarding & Implementação |
| **status** | `pending` |
| **responsible_executor** | Argus (Argus — Crítico de Qualidade e Completude) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Argus — Crítico de Qualidade e Completude — Agente verificador que revisa o plano de implementação antes da publicação no ClickUp (HITL gate) e audita os relatórios de delivery antes do envio ao cliente. Checklists de validação: plano (todos os marcos têm owner? todas as tarefas têm critério de aceite? dependências externas estão sinalizadas? datas são realistas dado o histórico?); relatório (dados batem com o ClickUp? semáforo RAG está correto? linguagem é adequada para o cliente? não há informações confidenciais expostas?). Bloqueia publicação/envio se checklist não passar com score >=85%.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Crítico de Qualidade e Completude
- Agente verificador que revisa o plano de implementação antes da publicação no ClickUp (HITL gate) e audita os relatórios de delivery antes do envio ao cliente
- Checklists de validação: plano (todos os marcos têm owner? todas as tarefas têm critério de aceite? dependências externas estão sinalizadas? datas são realistas dado o histórico?)
- relatório (dados batem com o ClickUp? semáforo RAG está correto? linguagem é adequada para o cliente? não há informações confidenciais expostas?)
- Bloqueia publicação/envio se checklist não passar com score >=85%

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Maestro para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Maestro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
