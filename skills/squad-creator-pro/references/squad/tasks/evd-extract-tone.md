---
task-id: evd-extract-tone
name: "Voice DNA: Extract Tone & Voice Dimensions"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
estimated-time: 10 min
complexity: medium

inputs:
  required:
    - validated_sources: "Lista validada de 5+ fontes"
    - mind_name: "Nome do expert"

outputs:
  primary:
    - tone_block: "YAML com voice_dimensions, contextual_tone, identity_statement"

elicit: true
parent_task: extract-voice-dna.md
related_tasks:
  - evd-extract-writing-style.md
  - evd-extract-anti-patterns.md
---

# Task: Voice DNA -- Extract Tone & Voice Dimensions

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-extract-tone` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** 5 of 8
- **Model:** Opus (voice calibration requires subjective assessment)

## Purpose

Map the expert's voice across 7 tonal dimensions on a 1-10 scale, document how tone shifts by context (teaching, persuading, storytelling, criticizing, celebrating), and craft the identity statement that captures their essence.

## Prerequisites

- `evd-collect-sources` completed
- Vocabulary and storytelling extraction completed (provides context for calibration)

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `validated_sources` | list | Yes | Output from evd-collect-sources |
| `mind_name` | string | Yes | Nome do expert |

## Workflow / Steps

### Step 1: Calibrate Voice Dimensions (1-10)

```yaml
voice_dimensions:
  warmth_distance: 5      # 1=caloroso, 10=distante
  direct_indirect: 5      # 1=direto, 10=indireto
  formal_casual: 5        # 1=formal, 10=casual
  complex_simple: 5       # 1=complexo, 10=simples
  emotional_rational: 5   # 1=emocional, 10=racional
  humble_confident: 5     # 1=humilde, 10=confiante
  serious_playful: 5      # 1=sério, 10=brincalhão
```

### Step 2: Map Contextual Tone

```yaml
contextual_tone:
  teaching: ""        # quando ensina
  persuading: ""      # quando convence
  storytelling: ""    # quando conta história
  criticizing: ""     # quando critica
  celebrating: ""     # quando elogia
```

### Step 3: Craft Identity Statement

The Trinity Phrase that captures the expert's communication essence:

> "[Nome] escreve/fala como ________________"

This single sentence must be distinctive enough that someone familiar with the expert would immediately recognize them from it.

## Output

```yaml
tone:
  dimensions:
    warmth_distance: 5
    direct_indirect: 5
    formal_casual: 5
    complex_simple: 5
    emotional_rational: 5
    humble_confident: 5
    serious_playful: 5

  by_context:
    teaching: ""
    persuading: ""
    storytelling: ""
    criticizing: ""
    celebrating: ""

  identity_statement: ""
```

## Acceptance Criteria

- [ ] All 7 voice dimensions calibrated (not left at default 5)
- [ ] Each dimension justified with observed evidence from sources
- [ ] All 5 contextual tones defined
- [ ] Identity statement crafted (Trinity Phrase)
- [ ] Identity statement is distinctive and recognizable

## Veto Conditions

None specific to this phase. General VETO-EVD-003 (source traceability) applies.

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `evd-extract-writing-style.md` (previous step)
- `evd-extract-anti-patterns.md` (next step)
