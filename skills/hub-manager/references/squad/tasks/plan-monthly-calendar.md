# Plan Monthly Calendar

**Task ID:** `plan-monthly-calendar`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Plan Monthly Calendar |
| **status** | `pending` |
| **responsible_executor** | Hub Chief |
| **execution_type** | `Agent` |
| **estimated_time** | `25-35m` |
| **input** | 4 inputs |
| **output** | 5 outputs |
| **action_items** | 5 steps |

## Overview

Organizar o mes do hub com foco, distribuicao semanal de temas e rituais e prioridades sem sobrecarregar o embaixador.

## Input

- **objetivo_do_mes** (text)
- **rituais_ou_eventos_fixos** (text)
- **janelas_disponiveis** (text)
- **principal_prioridade_do_hub** (text)

## Output

- **foco_do_mes** (text)
- **distribuicao_semanal** (list)
- **temas_e_rituais** (list)
- **prioridades** (list)
- **checkpoint_de_revisao** (text)

## Templates

- `templates/weekly-plan-tmpl.md`

## Checklists

- `checklists/weekly-ops-checklist.md`

## Action Items

1. Definir o foco do mes.
2. Escolher de 2 a 4 temas principais.
3. Distribuir eventos e comunicacoes por semana.
4. Evitar sobrecarga no calendario.
5. Fechar com criterio de revisao mensal.

## Acceptance Criteria

- O mes tem foco principal explicito.
- Os temas cabem no ritmo do hub.
- A distribuicao semanal e simples de entender.
- O calendario nao depende de alta complexidade operacional.

## Veto Conditions

- Nao concluir se o plano do mes estiver superlotado.
- Nao concluir sem checkpoint de revisao.
- Nao concluir se o foco do mes estiver disperso demais.

## Anti-Patterns

- Distribuir mais rituais do que o hub consegue sustentar.
- Planejar um mes inteiro sem prioridade principal.
- Tratar calendario mensal como backlog infinito.

## Output Example

- foco do mes: retomar o ritmo do hub e consolidar um ritual recorrente
- distribuicao: semana 1 convite; semana 2 encontro; semana 3 reativacao; semana 4 revisao
- temas: conexao, ativacao, encontro, continuidade
- checkpoint: revisar no fim da quarta semana
