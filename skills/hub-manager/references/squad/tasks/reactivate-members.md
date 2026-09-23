# Reactivate Members

**Task ID:** `reactivate-members`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reactivate Members |
| **status** | `pending` |
| **responsible_executor** | Hub Members |
| **execution_type** | `Agent` |
| **estimated_time** | `20-30m` |
| **input** | 3 inputs |
| **output** | 4 outputs |
| **action_items** | 5 steps |

## Overview

Reativar membros silenciosos com mensagem de reengajamento, CTA de baixa friccao e follow-up leve.

## Input

- **quem_esta_silencioso** (text)
- **ha_quanto_tempo** (text)
- **convite_ou_oportunidade_atual** (text)

## Output

- **segmentacao_simples** (text)
- **mensagem_de_reengajamento** (text)
- **cta** (text)
- **follow_up_sugerido** (text)

## Templates

- `templates/reactivation-message-tmpl.md`

## Action Items

1. Identificar o tipo de silencio.
2. Escolher o angulo de reativacao.
3. Escrever a mensagem de reengajamento.
4. Definir CTA pequeno e claro.
5. Sugerir follow-up leve.

## Acceptance Criteria

- A mensagem reduz friccao de resposta.
- O CTA pede uma acao pequena e viavel.
- Existe follow-up sugerido.
- O tom acolhe em vez de pressionar.

## Veto Conditions

- Nao concluir sem CTA claro.
- Nao concluir se a mensagem culpabilizar o membro silencioso.
- Nao concluir se o convite exigir grande esforco de retorno.

## Anti-Patterns

- Pressionar o membro como se ele estivesse em falta.
- Pedir uma acao grande para quem ja esta distante.
- Mandar reativacao sem contexto de oportunidade atual.

## Output Example

- segmentacao: membros que sumiram nas ultimas 2-4 semanas
- mensagem: convite curto para voltar por um encontro leve
- CTA: responder a mensagem ou confirmar presenca
- follow-up: reforco 3 dias depois com versao ainda mais curta
