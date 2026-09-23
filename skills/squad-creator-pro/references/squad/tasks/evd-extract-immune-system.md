---
task-id: evd-extract-immune-system
name: "Voice DNA: Extract Immune System (Automatic Rejections)"
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
    - immune_system_block: "YAML com automatic_rejections, emotional_boundaries, fierce_defenses"

elicit: true
parent_task: extract-voice-dna.md
related_tasks:
  - evd-extract-anti-patterns.md
  - evd-extract-contradictions.md
---

# Task: Voice DNA -- Extract Immune System

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-extract-immune-system` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** 7 of 8
- **Model:** Opus (emotional/reactive pattern extraction requires deep interpretation)

## Purpose

Extract what the expert rejects BEFORE even thinking -- automatic, reflexive responses to triggers. This includes instant rejections, emotional boundaries, and values they defend ferociously. The immune system defines the hardcoded limits of the expert's voice.

## Prerequisites

- `evd-collect-sources` completed
- Anti-patterns extraction completed (provides context for deeper rejection analysis)

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `validated_sources` | list | Yes | Output from evd-collect-sources |
| `mind_name` | string | Yes | Nome do expert |

## Workflow / Steps

### Step 1: Extract Automatic Rejections

```yaml
automatic_rejections:
  - trigger: "Pedido para simplificar demais"
    response_speed: "imediato|rápido|após reflexão"
    typical_response: ""
    tone_shift: "como o tom muda"
    exceptions: "quando aceita"

  - trigger: "Sugestão antiética"
    response_speed: "reflexivo"
    typical_response: ""
```

### Step 2: Map Emotional Boundaries

```yaml
emotional_boundaries:
  - boundary: "Ser condescendido"
    auto_defense: "como reage"
    intensity: "1-10"
    recovery_time: "quanto tempo para voltar ao normal"

  - boundary: "Ter expertise questionada"
    auto_defense: ""
    intensity: ""
```

### Step 3: Identify Fierce Defenses

```yaml
fierce_defenses:
  - value: "Integridade intelectual"
    how_hard: "até onde vai"
    cost_acceptable: "disposto a perder relacionamento?"
    observable_signs: "como perceber que ativou"
```

## Output

```yaml
immune_system:
  automatic_rejections:
    - trigger: ""
      response_speed: ""
      typical_response: ""
      tone_shift: ""
      exceptions: ""

  emotional_boundaries:
    - boundary: ""
      auto_defense: ""
      intensity: ""
      recovery_time: ""

  fierce_defenses:
    - value: ""
      how_hard: ""
      cost_acceptable: ""
      observable_signs: ""
```

## Acceptance Criteria

- [ ] 2+ automatic rejections documented with triggers and responses
- [ ] Tone shift documented for each rejection (how voice changes under trigger)
- [ ] Emotional boundaries mapped with intensity ratings
- [ ] Fierce defenses identified with cost tolerance
- [ ] All entries traceable to observed behavior in sources

## Veto Conditions

None specific to this phase. General source traceability applies.

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `evd-extract-anti-patterns.md` (previous step)
- `evd-extract-contradictions.md` (next step)
