# Create Event Plan

**Task ID:** `create-event-plan`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Create Event Plan |
| **status** | `pending` |
| **responsible_executor** | Hub Events |
| **execution_type** | `Agent` |
| **estimated_time** | `25-40m` |
| **input** | 5 inputs |
| **output** | 5 outputs |
| **action_items** | 6 steps |

## Overview

Estruturar um encontro local simples com proposta, plano de comunicacao, checklist basico e roteiro curto de abertura.

## Input

- **tema_do_encontro** (text)
- **objetivo** (text)
- **publico** (text)
- **data_aproximada** (text)
- **duracao_desejada** (text)

## Output

- **titulo** (text)
- **proposta** (text)
- **plano_de_comunicacao** (list)
- **checklist_pre_evento** (list)
- **roteiro_de_abertura** (text)

## Templates

- `templates/event-plan-tmpl.md`

## Checklists

- `checklists/event-readiness-checklist.md`

## Action Items

1. Validar o objetivo do encontro.
2. Definir formato simples e aderente ao momento do hub.
3. Criar titulo e proposta.
4. Montar plano de comunicacao pre-evento.
5. Preparar checklist basico.
6. Escrever roteiro curto de abertura.

## Acceptance Criteria

- O objetivo do encontro esta claro.
- O formato proposto e simples de executar.
- O plano de comunicacao cobre pelo menos antecipacao e lembrete.
- Existe checklist pre-evento.
- O roteiro de abertura cabe em uma abertura curta.

## Veto Conditions

- Nao concluir sem objetivo claro.
- Nao concluir se o evento exigir complexidade fora do MVP.
- Nao concluir sem algum plano de comunicacao.

## Anti-Patterns

- Planejar um evento grande para um hub frio.
- Criar encontro sem CTA de presenca.
- Fazer um roteiro de abertura maior que o proprio encontro.

## Output Example

- titulo: encontro local sobre IA na pratica para o hub
- proposta: troca guiada com exemplos simples e proximo passo
- plano de comunicacao: post principal + lembrete + chamada final
- checklist: titulo, horario, convite, roteiro
- roteiro: boas-vindas, objetivo, 3 pontos, chamada final
