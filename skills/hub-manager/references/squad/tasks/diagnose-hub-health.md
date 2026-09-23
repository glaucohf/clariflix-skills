# Diagnose Hub Health

**Task ID:** `diagnose-hub-health`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Diagnose Hub Health |
| **status** | `pending` |
| **responsible_executor** | Hub Chief |
| **execution_type** | `Agent` |
| **estimated_time** | `20-30m` |
| **input** | 5 inputs |
| **output** | 5 outputs |
| **action_items** | 5 steps |

## Overview

Ler o momento atual do hub a partir de sinais basicos e sugerir top 3 proximas acoes.

## Input

- **frequencia_recente_de_posts** (text)
- **presenca_ou_ausencia_de_encontros** (text)
- **novos_membros_ou_silencio** (text)
- **energia_percebida_do_hub** (text)
- **feedbacks_ou_sinais_observaveis** (text)

## Output

- **estado_do_hub** (text)
- **pontos_fortes** (list)
- **pontos_de_atencao** (list)
- **top_3_acoes_recomendadas** (list)
- **proxima_revisao_sugerida** (text)

## Templates

- `templates/diagnosis-report-tmpl.md`

## Checklists

- `checklists/weekly-ops-checklist.md`

## Action Items

1. Coletar os sinais disponiveis.
2. Avaliar ritmo, membros, eventos e resposta.
3. Classificar o momento do hub.
4. Listar pontos fortes e pontos de atencao.
5. Priorizar top 3 acoes.

## Acceptance Criteria

- O estado do hub esta nomeado com clareza.
- Pontos fortes e de atencao aparecem separados.
- Existem 3 acoes priorizadas.
- A recomendacao funciona mesmo com dados incompletos.

## Veto Conditions

- Nao concluir sem classificar o estado do hub.
- Nao concluir se as acoes recomendadas nao tiverem prioridade.
- Nao concluir se o texto depender de metricas que o usuario nao tem.

## Anti-Patterns

- Diagnostico abstrato demais para gerar acao.
- Usar metricas que o embaixador nao consegue observar.
- Sugerir mais de 3 prioridades de uma vez.

## Output Example

- estado: atencao
- pontos fortes: existe base interessada; ainda ha ritual reconhecivel
- pontos de atencao: baixa resposta recente; encontro sem repercussao
- top 3 acoes: definir encontro simples; publicar convite claro; reativar membros silenciosos
- proxima revisao: em 7 dias
