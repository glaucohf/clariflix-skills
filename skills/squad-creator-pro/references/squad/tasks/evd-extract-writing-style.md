---
task-id: evd-extract-writing-style
name: "Voice DNA: Extract Writing Style"
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
    - writing_style_block: "YAML com structure, rhetorical_devices, formatting, sentence_patterns"

elicit: true
parent_task: extract-voice-dna.md
related_tasks:
  - evd-extract-storytelling.md
  - evd-extract-tone.md
---

# Task: Voice DNA -- Extract Writing Style

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-extract-writing-style` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** 4 of 8
- **Model:** Opus (stylistic pattern recognition requires nuanced analysis)

## Purpose

Extract the expert's writing style DNA: text structure preferences, rhetorical devices, formatting habits, and characteristic sentence patterns.

## Prerequisites

- `evd-collect-sources` completed with 5+ validated sources
- Written source materials available for structural analysis

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `validated_sources` | list | Yes | Output from evd-collect-sources |
| `mind_name` | string | Yes | Nome do expert |

## Workflow / Steps

### Step 1: Analyze Text Structure

```yaml
writing_structure:
  paragraph_length: "curto|médio|longo"
  sentence_length: "curta|média|longa"
  list_usage: "frequente|moderado|raro"
  headers_style: ""
  opening_pattern: "como abre textos/seções"
  closing_pattern: "como fecha textos/seções"
```

### Step 2: Identify Rhetorical Devices

```yaml
rhetorical_devices:
  questions: "usa perguntas retóricas? como?"
  repetition: "usa repetição? padrão?"
  contrast: "usa contraste? padrão?"
  direct_address: "fala direto com leitor? como?"
  humor: "usa humor? tipo?"
  provocation: "provoca? como?"
```

### Step 3: Document Formatting Habits

```yaml
formatting_habits:
  emphasis: "negrito|itálico|CAPS|aspas"
  parentheses: "frequente|raro"
  dashes: "frequente|raro"
  ellipsis: "frequente|raro"
  special_chars: []  # ex: "->", "*", etc
```

### Step 4: Extract Sentence Patterns (3-5)

```yaml
sentence_patterns:
  - pattern: "Nome do padrão"
    description: "O que caracteriza"
    example: "Exemplo real do expert"
    source: "[SOURCE: documento, página]"
    when_to_use: "Quando aplicar esse padrão"

# Exemplos de padrões comuns:
# - Fragmentos curtos para ênfase: "A starving crowd. That's what you need."
# - Anáfora (repetição): "Hard work. Daily work. Consistent work."
# - Escolhas binárias: "You can be a whiner or you can be a winner."
# - Imperativos diretos: "Listen up. Read this carefully."
```

## Output

```yaml
writing_style:
  structure:
    paragraph_length: ""
    sentence_length: ""
    list_usage: ""
    headers_style: ""
    opening_pattern: ""
    closing_pattern: ""

  sentence_patterns:
    - pattern: ""
      description: ""
      example: ""
      source: "[SOURCE: ]"
      when_to_use: ""

  rhetorical_devices:
    questions: ""
    repetition: ""
    contrast: ""
    direct_address: ""
    humor: ""
    provocation: ""

  formatting:
    emphasis: ""
    parentheses: ""
    dashes: ""
    ellipsis: ""
    special_chars: []
```

## Acceptance Criteria

- [ ] Text structure fully mapped (paragraph, sentence, list, headers, patterns)
- [ ] All 6 rhetorical device dimensions analyzed
- [ ] Formatting habits documented
- [ ] 3-5 sentence patterns extracted with real examples and [SOURCE:] citations
- [ ] Each sentence pattern has `when_to_use` guidance

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EVD-003 | Sentence patterns must have SOURCE citations | Validate source field for each pattern | VETO - BLOCK. Remove uncited patterns. |

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `evd-extract-storytelling.md` (previous step)
- `evd-extract-tone.md` (next step)
