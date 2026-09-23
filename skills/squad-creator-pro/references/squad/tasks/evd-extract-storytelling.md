---
task-id: evd-extract-storytelling
name: "Voice DNA: Extract Storytelling Patterns"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
estimated-time: 15 min
complexity: medium

inputs:
  required:
    - validated_sources: "Lista validada de 5+ fontes"
    - mind_name: "Nome do expert"

outputs:
  primary:
    - storytelling_block: "YAML com recurring_stories, anecdotes, examples, story_structure"

elicit: true
parent_task: extract-voice-dna.md
related_tasks:
  - evd-extract-vocabulary.md
  - evd-extract-writing-style.md
---

# Task: Voice DNA -- Extract Storytelling Patterns

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-extract-storytelling` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** 3 of 8
- **Model:** Opus (narrative pattern recognition requires deep interpretation)

## Purpose

Extract the expert's storytelling DNA: recurring stories they tell repeatedly, personal anecdotes used as proof, favorite external examples, and the structural patterns of how they build narratives.

## Prerequisites

- `evd-collect-sources` completed with 5+ validated sources
- Source materials accessible for narrative extraction

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `validated_sources` | list | Yes | Output from evd-collect-sources |
| `mind_name` | string | Yes | Nome do expert |

## Workflow / Steps

### Step 1: Extract Recurring Stories

Histórias que o expert conta REPETIDAMENTE para ilustrar pontos.

```yaml
recurring_stories:
  - title: "Nome/descrição curta"
    summary: "O que acontece"
    lesson: "O ponto que ilustra"
    trigger: "Quando conta essa história"
    source: "Onde aparece"
```

### Step 2: Extract Personal Anecdotes

Experiências pessoais que usa como prova/exemplo.

```yaml
personal_anecdotes:
  - event: ""
    lesson_extracted: ""
    emotional_tone: ""
    use_for: "tipo de argumento que suporta"
```

### Step 3: Extract Favorite Examples

Cases/exemplos externos que referencia frequentemente.

```yaml
favorite_examples:
  - example: ""
    domain: ""
    point_it_makes: ""
    frequency: "sempre|frequente|ocasional"
```

### Step 4: Map Story Structure

Como o expert estrutura histórias.

```yaml
story_structure:
  opening: "como começa histórias"
  build_up: "como desenvolve tensão"
  payoff: "como entrega o ponto"
  callback: "se/como referencia de volta"
```

## Output

```yaml
storytelling:
  recurring_stories:
    - title: ""
      summary: ""
      lesson: ""
      trigger: ""
      source: ""

  personal_anecdotes:
    - event: ""
      lesson_extracted: ""
      emotional_tone: ""
      use_for: ""

  favorite_examples:
    - example: ""
      domain: ""
      point_it_makes: ""
      frequency: ""

  story_structure:
    opening: ""
    build_up: ""
    payoff: ""
    callback: ""
```

## Acceptance Criteria

- [ ] 3+ recurring stories documented with triggers and lessons
- [ ] Personal anecdotes extracted with emotional tone mapping
- [ ] Favorite external examples catalogued with frequency
- [ ] Story structure pattern fully mapped (opening, build_up, payoff, callback)
- [ ] All stories traceable to source materials

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EVD-003 | All entries must have source traceability | Verify stories and anecdotes reference source materials | VETO - BLOCK. Remove unverifiable entries. |

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `evd-extract-vocabulary.md` (previous step)
- `evd-extract-writing-style.md` (next step)
