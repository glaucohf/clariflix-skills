# Onboard Hub Member

**Task ID:** `onboard-hub-member`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Onboard Hub Member |
| **status** | `pending` |
| **responsible_executor** | Hub Members |
| **execution_type** | `Agent` |
| **estimated_time** | `15-25m` |
| **input** | 3 inputs |
| **output** | 3 outputs |
| **action_items** | 5 steps |

## Overview

Receber um novo membro com mensagem de boas-vindas, primeiro passo claro e sequencia curta de ativacao.

## Input

- **perfil_do_membro** (text)
- **canal_de_entrada** (text)
- **primeira_acao_desejada** (text)

## Output

- **mensagem_de_boas_vindas** (text)
- **sequencia_curta_de_ativacao** (list)
- **convite_para_primeira_acao** (text)

## Templates

- `templates/onboarding-message-tmpl.md`

## Action Items

1. Definir o tom da recepcao.
2. Montar a mensagem de boas-vindas.
3. Indicar o primeiro passo mais facil.
4. Planejar 1 ou 2 follow-ups leves.
5. Sugerir criterio simples de ativacao inicial.

## Acceptance Criteria

- A mensagem acolhe sem sobrecarregar.
- O primeiro passo e claro e simples.
- Existe pelo menos uma acao de follow-up.
- O texto final nao depende de automacao externa para ser util.

## Veto Conditions

- Nao concluir se o primeiro passo estiver confuso.
- Nao concluir se a mensagem ficar longa demais para onboarding inicial.
- Nao concluir se a sequencia exigir stack externa obrigatoria.

## Anti-Patterns

- Onboarding com cinco proximos passos de uma vez.
- Mensagem fria ou burocratica.
- Convite para uma acao dificil demais como primeiro movimento.

## Output Example

- mensagem: boas-vindas com convite simples para se apresentar ou participar do proximo ritual
- sequencia: boas-vindas hoje + lembrete em 3 dias
- convite: responder a mensagem ou entrar no encontro da semana
