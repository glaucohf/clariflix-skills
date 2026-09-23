# Create Hub Post

**Task ID:** `create-hub-post`
**Pattern:** HO-TP-001
**Version:** 1.0.0

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Create Hub Post |
| **status** | `pending` |
| **responsible_executor** | Hub Content |
| **execution_type** | `Agent` |
| **estimated_time** | `15-25m` |
| **input** | 5 inputs |
| **output** | 4 outputs |
| **action_items** | 6 steps |

## Overview

Criar post, convite, lembrete ou CTA curto para o hub com linguagem simples, objetivo claro e chamada para acao.

## Input

- **tema** (text)
- **objetivo** (text)
- **publico** (text)
- **formato_desejado** (text)
- **cta_esperado** (text)

## Output

- **texto_principal** (text)
- **variacao_curta** (text)
- **cta_final** (text)
- **sugestao_de_uso** (text)

## Templates

- `templates/weekly-plan-tmpl.md`

## Checklists

- `checklists/weekly-ops-checklist.md`

## Action Items

1. Entender o momento do hub e do publico.
2. Escolher o melhor angulo de mensagem.
3. Escrever o texto principal.
4. Criar uma variacao curta.
5. Fechar com CTA claro.
6. Sugerir horario ou contexto de publicacao.

## Acceptance Criteria

- O texto principal comunica o objetivo de forma clara.
- Existe uma variacao curta reaproveitavel.
- O CTA esta explicito.
- A mensagem nao promete algo que o hub nao entrega.

## Veto Conditions

- Nao concluir sem CTA claro.
- Nao concluir se a mensagem estiver generica demais para o objetivo.
- Nao concluir se o texto contradizer o momento atual do hub.

## Anti-Patterns

- CTA escondido ou ambiguo.
- Texto longo demais para um convite simples.
- Mensagem que promete algo que o hub nao entrega.

## Output Example

- texto principal: convite para encontro de quinta com beneficio claro
- variacao curta: lembrete curto para WhatsApp
- CTA: responder "quero ir" ou entrar no link do encontro
- sugestao de uso: publicar no inicio da tarde e reforcar no dia anterior
