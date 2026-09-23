---
task-id: evd-extract-contradictions
name: "Voice DNA: Extract Voice Contradictions (Authentic Paradoxes)"
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
    - contradictions_block: "YAML com paradoxes, inconsistencies, clone instructions"

elicit: true
parent_task: extract-voice-dna.md
related_tasks:
  - evd-extract-immune-system.md
  - evd-assemble-voice-dna.md
---

# Task: Voice DNA -- Extract Voice Contradictions

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-extract-contradictions` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** 8 of 8
- **Model:** Opus (paradox recognition requires high-order reasoning)

## Purpose

Extract the expert's authentic contradictions and paradoxes. Contradictions make humans REAL. Resolving paradoxes makes clones FAKE. This phase preserves the tensions that give the voice depth and authenticity.

> Contradições são features, não bugs. Se o clone for "consistente demais", está errado.

## Prerequisites

- All previous phases completed (full picture needed to identify paradoxes)
- Understanding of expert's vocabulary, tone, and anti-patterns

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `validated_sources` | list | Yes | Output from evd-collect-sources |
| `mind_name` | string | Yes | Nome do expert |

## Workflow / Steps

### Step 1: Identify Communication Paradoxes

```yaml
voice_contradictions:
  - paradox: "Defende transparência MAS mantém vida pessoal privada"
    how_appears: "Como isso aparece na fala/escrita"
    trigger_for_switch: "O que faz mudar de um para outro"
    audience_dependent: "Muda com diferentes audiências?"
    clone_instruction: "NÃO RESOLVER - preservar o paradox"

  # Exemplo:
  - paradox: "Simplifica para ensinar MAS usa frameworks complexos"
    how_appears: "Alterna entre linguagem simples e jargão técnico"
    trigger_for_switch: "Nível percebido da audiência"
    clone_instruction: "Manter ambos modos disponíveis"
```

### Step 2: Document Authentic Inconsistencies

```yaml
authentic_inconsistencies:
  - inconsistency: ""
    context_A: "quando faz X"
    context_B: "quando faz Y (oposto)"
    why_both_are_authentic: ""
```

### Step 3: Write Clone Preservation Instructions

```yaml
paradox_handling:
  preserve_these:
    - "Lista de paradoxos que NÃO devem ser resolvidos"

  guidance: |
    Contradições são features, não bugs.
    Se o clone for "consistente demais", está errado.
```

## Output

```yaml
voice_contradictions:
  paradoxes:
    - paradox: ""
      how_appears: ""
      trigger_for_switch: ""
      audience_dependent: ""
      clone_instruction: "NÃO RESOLVER"

  authentic_inconsistencies:
    - inconsistency: ""
      context_A: ""
      context_B: ""
      why_both_are_authentic: ""

  preservation_note: |
    Contradições são features, não bugs.
    Clone "consistente demais" = clone falso.
```

## Acceptance Criteria

- [ ] 1+ paradox/contradiction documented
- [ ] Each paradox has `clone_instruction` explicitly saying NOT to resolve it
- [ ] Trigger for switching between contradictory modes identified
- [ ] Audience dependency analyzed
- [ ] Preservation note included for clone guidance

## Veto Conditions

None specific to this phase. The key constraint is philosophical: NEVER resolve paradoxes.

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `evd-extract-immune-system.md` (previous step)
- `evd-assemble-voice-dna.md` (assembly step)
