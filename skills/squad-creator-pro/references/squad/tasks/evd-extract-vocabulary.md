---
task-id: evd-extract-vocabulary
name: "Voice DNA: Extract Vocabulary"
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
    - vocabulary_block: "YAML com power_words, signature_phrases, metaphors, vocabulary_rules"

elicit: true
parent_task: extract-voice-dna.md
related_tasks:
  - evd-collect-sources.md
  - evd-extract-storytelling.md
---

# Task: Voice DNA -- Extract Vocabulary

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-extract-vocabulary` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** 2 of 8
- **Model:** Opus (semantic pattern extraction requires deep language interpretation)

## Purpose

Extract the expert's distinctive vocabulary: power words they use repeatedly with emotional weight, signature phrases that identify them, favorite metaphors, and vocabulary transformation rules.

## Prerequisites

- `evd-collect-sources` completed with 5+ validated sources
- Source materials accessible for citation

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `validated_sources` | list | Yes | Output from evd-collect-sources |
| `mind_name` | string | Yes | Nome do expert |

## Workflow / Steps

### Step 1: Extract Power Words (10-15)

Palavras que o expert usa REPETIDAMENTE com peso emocional.

```yaml
power_words:
  - word: ""
    source: "[SOURCE: documento, página/seção]"  # OBRIGATÓRIO
    context: "quando usa"
    emotional_weight: "alto|médio"
```

**REGRA:** Cada power word DEVE ter `source:` com citação exata.

### Step 2: Extract Signature Phrases (8-12)

Expressões que IDENTIFICAM a pessoa.

```yaml
signature_phrases:
  - phrase: ""
    source: "[SOURCE: documento, página/seção]"  # OBRIGATÓRIO
    meaning: ""
    use_when: ""
    example_usage: ""  # Como usar em copy NOVO (não só citar)
```

**REGRA:** Cada frase DEVE ter:
- `source:` com citação exata
- `example_usage:` mostrando aplicação prática

### Step 3: Extract Favorite Metaphors (3-5)

Como o expert explica conceitos complexos.

```yaml
metaphors:
  - concept: "o que explica"
    metaphor: "como explica"
    example: ""
```

### Step 4: Define Vocabulary Rules

```yaml
vocabulary_rules:
  always_use: []    # termos que SEMPRE usa
  never_use: []     # termos que EVITA
  transforms:       # como "traduz" jargão
    - from: "jargão comum"
      to: "como ele diz"
```

## Output

```yaml
vocabulary:
  power_words:
    - word: ""
      source: "[SOURCE: ]"
      context: ""
      emotional_weight: ""

  signature_phrases:
    - phrase: ""
      source: "[SOURCE: ]"
      meaning: ""
      use_when: ""
      example_usage: ""

  metaphors:
    - concept: ""
      metaphor: ""
      example: ""

  rules:
    always_use: []
    never_use: []
    transforms: []
```

## Acceptance Criteria

- [ ] 10+ power words extracted with [SOURCE:] citations
- [ ] 8+ signature phrases extracted (not just 5)
- [ ] Each signature phrase has `example_usage:` (new copy, not just citation)
- [ ] 3+ metaphors documented
- [ ] Vocabulary rules defined (always_use, never_use, transforms)
- [ ] ZERO content invented -- all extracted from sources

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EVD-003 | All power_words and signature_phrases must have SOURCE citations | Validate every entry has non-empty source field with [SOURCE: doc, page] format | VETO - BLOCK. Remove uncited entries or find supporting source references. |

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `evd-collect-sources.md` (prerequisite)
- `evd-extract-storytelling.md` (next step)
