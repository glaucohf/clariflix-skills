# Plan Weekly Hub

**Task ID:** `plan-weekly-hub`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Plan Weekly Hub |
| **status** | `pending` |
| **responsible_executor** | Hub Chief |
| **execution_type** | `Agent` |
| **estimated_time** | `20-30m` |
| **input** | 4 inputs |
| **output** | 5 outputs |
| **action_items** | 6 steps |

## Overview

Montar um plano semanal do hub com foco principal, acoes em ordem, risco central e checkpoint recomendado.

## Input

- **objetivo_da_semana** (text)
  - Description: o resultado mais importante que o embaixador quer gerar
- **momento_atual_do_hub** (text)
  - Description: sinais de aquecimento, estabilidade, silencio ou instabilidade
- **evento_ou_ritual_marcado** (text)
  - Description: encontro ja previsto, se existir
- **principal_preocupacao** (text)
  - Description: a principal duvida ou trava do embaixador

## Output

- **foco_da_semana** (text)
- **acoes_priorizadas** (list)
- **responsavel_sugerido** (list)
- **risco_principal** (text)
- **checkpoint_recomendado** (text)

## Templates

- `templates/weekly-plan-tmpl.md`

## Checklists

- `checklists/weekly-ops-checklist.md`

## Action Items

1. Ler o momento do hub a partir dos sinais disponiveis.
2. Definir um foco principal para a semana.
3. Escolher de 3 a 5 acoes maximas.
4. Ordenar as acoes por impacto e urgencia.
5. Sinalizar o maior risco da semana.
6. Encerrar com checkpoint e proximo passo.

## Acceptance Criteria

- O foco semanal esta claro em uma frase.
- Existem no maximo 5 acoes priorizadas.
- A ordem das acoes faz sentido para o momento do hub.
- O risco principal foi explicitado.
- O checkpoint final orienta a proxima revisao.

## Veto Conditions

- Nao seguir se o foco semanal estiver vago ou contraditorio.
- Nao seguir se a lista de acoes ultrapassar 5 itens sem justificativa.
- Nao concluir sem explicitar o risco principal.

## Anti-Patterns

- Criar uma semana superlotada para um hub em retomada.
- Misturar planejamento semanal com estrategia trimestral.
- Entregar lista de acoes sem ordem de prioridade.

## Output Example

- foco da semana: reativar o ritmo do hub com um encontro simples e um convite claro
- acoes:
  - definir tema e formato do encontro
  - publicar convite principal
  - mandar mensagem de reativacao para membros silenciosos
  - revisar resposta em 3 dias
- risco principal: excesso de acoes para uma semana de retomada
- checkpoint: revisar na quinta-feira se o convite gerou retorno
