---
task: weeklyContentPlan()
responsavel: "Link"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: week
    tipo: string
    obrigatorio: false
  - nome: posts
    tipo: integer
    obrigatorio: false
  - nome: include_draft
    tipo: boolean
    obrigatorio: false
Saida:
  - nome: weekly_plan
    tipo: string
    obrigatorio: true
  - nome: content_draft
    tipo: string
    obrigatorio: false
  - nome: action_items
    tipo: string
    obrigatorio: true
Checklist:
  - "[ ] Pilar da semana definido com rotação adequada"
  - "[ ] Rascunho completo gerado se solicitado"
  - "[ ] Dia, horário e ações complementares definidos"
---


# Task: Weekly Content Plan

**Task ID:** weekly-content-plan
**Agent:** @linkedin-chief
**Priority:** HIGH
**Tools Required:** Read, WebSearch

---

## Objetivo

Gerar plano de conteúdo semanal para o LinkedIn, incluindo tema, formato, rascunho e calendário de publicação.

> Este é o workflow principal do squad — roda semanalmente para manter a consistência.

---

## Inputs

| Parameter | Description | Default |
|-----------|-------------|---------|
| WEEK | Semana alvo | `próxima semana` |
| POSTS | Quantidade de posts | `1` |
| INCLUDE_DRAFT | Gerar rascunho junto | `true` |

---

## Workflow

### Step 1: Review da Semana Anterior

- Qual foi o último post publicado?
- Qual pilar foi usado?
- Como foi o engajamento? (se disponível)
- Há follow-ups pendentes de comentários?

### Step 2: Selecionar Pilar da Semana

Rotacionar entre os 4 pilares:

| Semana | Pilar |
|--------|-------|
| 1 | Segurança Ofensiva |
| 2 | Automação com IA |
| 3 | Bastidores (dia a dia) |
| 4 | Mentoria (dicas juniores) |

> Ajustar se houver algo trending que demande atenção imediata.

### Step 3: Consultar Trends

Acionar @trend-scout para verificar:
- Algo trending que se encaixa no pilar da semana?
- Algum evento/notícia que vale capitalizar?
- Algum tema do backlog que ficou maduro?

### Step 4: Definir Tema e Formato

| Critério | Decisão |
|----------|---------|
| Tem história real para contar? | → Storytelling |
| Tem lista/framework para ensinar? | → Carrossel |
| Tem opinião forte sobre algo? | → Post de opinião |
| Tem tutorial prático? | → Carrossel tutorial |
| Quer compartilhar insight rápido? | → Post curto |

### Step 5: Gerar Rascunho

Se INCLUDE_DRAFT = true:
- Acionar @ghostwriter (post texto) ou @carousel-designer (carrossel)
- Gerar rascunho completo
- Incluir 3 opções de hook

### Step 6: Montar Plano Final

Consolidar tudo em um plano acionável.

---

## Output

```markdown
# Plano de Conteúdo — Semana de {{DATE}}

## Contexto
- **Último post:** {{tema do último post}} ({{data}})
- **Pilar anterior:** {{pilar}}
- **Pilar desta semana:** {{pilar atual}}

## Post da Semana

| Campo | Valor |
|-------|-------|
| **Tema** | {{tema}} |
| **Pilar** | {{pilar}} |
| **Formato** | {{formato}} |
| **Ângulo** | {{ângulo específico}} |
| **Dia sugerido** | {{dia da semana}} |
| **Horário** | {{horário}} |

## Rascunho

{{DRAFT_CONTENT}}

## Ações Complementares

- [ ] Revisar e personalizar rascunho
- [ ] Preparar visual (se carrossel)
- [ ] Publicar no dia/horário sugerido
- [ ] Responder comentários nas primeiras 2h
- [ ] Comentar em 3 posts relevantes na semana

## Backlog Atualizado

| # | Tema | Pilar | Formato | Para quando |
|---|------|-------|---------|-------------|
| 1 | ... | ... | ... | Próxima semana |
| 2 | ... | ... | ... | Quando oportuno |
```

---

## Success Criteria

- [ ] Pilar da semana definido (com rotação)
- [ ] Tema específico (não genérico)
- [ ] Formato adequado ao tema
- [ ] Rascunho completo (se solicitado)
- [ ] Dia e horário sugeridos
- [ ] Ações complementares listadas

---

*Task Version: 1.0*
*Created: 2026-03-11*
