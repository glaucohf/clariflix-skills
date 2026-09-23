# Analyze Event Results

**Task ID:** `analyze-event-results`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analyze Event Results |
| **status** | `pending` |
| **responsible_executor** | Hub Events |
| **execution_type** | `Agent` |
| **estimated_time** | `15-25m` |
| **input** | 4 inputs |
| **output** | 4 outputs |
| **action_items** | 5 steps |

## Overview

Analisar o resultado de um encontro local para identificar acertos, gargalos e o melhor ajuste para a proxima iteracao.

## Input

- **objetivo_do_evento** (text)
- **o_que_aconteceu** (text)
- **sinais_de_participacao** (text)
- **feedbacks_ou_percepcoes** (text)

## Output

- **acertos** (list)
- **gargalos** (list)
- **ajuste_recomendado** (text)
- **proximo_passo** (text)

## Templates

- `templates/diagnosis-report-tmpl.md`

## Checklists

- `checklists/event-readiness-checklist.md`

## Action Items

1. Comparar objetivo e execucao.
2. Identificar o que funcionou.
3. Identificar o que travou.
4. Sugerir um ajuste pratico para o proximo encontro.
5. Definir o follow-up recomendado.

## Acceptance Criteria

- O objetivo do evento foi comparado com o que ocorreu.
- Existem acertos e gargalos separados.
- O ajuste recomendado e pratico.
- O proximo passo fecha a analise.

## Veto Conditions

- Nao concluir sem um ajuste recomendado.
- Nao concluir se os gargalos estiverem vagos demais.
- Nao concluir sem proximo passo.

## Anti-Patterns

- Fazer post-mortem sem comparacao com o objetivo.
- Listar gargalos sem propor ajuste.
- Encerrar a analise sem dizer o que fazer agora.

## Output Example

- acertos: tema gerou conversa; abertura foi clara
- gargalos: convite saiu tarde; follow-up nao aconteceu
- ajuste recomendado: antecipar convite em 3 dias
- proximo passo: preparar novo convite com CTA mais simples
