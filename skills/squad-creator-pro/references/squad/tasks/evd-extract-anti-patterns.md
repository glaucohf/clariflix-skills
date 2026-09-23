---
task-id: evd-extract-anti-patterns
name: "Voice DNA: Extract Communication Anti-Patterns"
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
    - anti_patterns_block: "YAML com never_say, never_do, rejected_styles"

elicit: true
parent_task: extract-voice-dna.md
related_tasks:
  - evd-extract-tone.md
  - evd-extract-immune-system.md
---

# Task: Voice DNA -- Extract Communication Anti-Patterns

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-extract-anti-patterns` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** 6 of 8
- **Model:** Opus (identifying what someone avoids requires deep inference)

## Purpose

Extract what the expert NEVER does or says in communication. Anti-patterns are as important as patterns -- they define the negative space of the voice, preventing the clone from producing content that would violate the expert's identity.

## Prerequisites

- `evd-collect-sources` completed
- Previous vocabulary and tone extraction provide context for identifying rejections

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `validated_sources` | list | Yes | Output from evd-collect-sources |
| `mind_name` | string | Yes | Nome do expert |

## Workflow / Steps

### Step 1: Extract Never-Say Terms (5+)

```yaml
communication_anti_patterns:
  never_say:
    - term: ""
      source: "[SOURCE: inferido de documento, página]"  # De onde inferiu
      reason: "Por que evita"
      substitute: "O que usa no lugar"
      example_wrong: "Frase que violaria a voz"
      example_correct: "Frase corrigida na voz do expert"

  # Exemplo Gary Halbert:
  never_say:
    - term: "synergy"
      source: "[SOURCE: The Boron Letters, Letter 3, p.15 - rejeita 'fancy words']"
      reason: "Corporate bullshit - viola 'simple works'"
      substitute: "work together"
      example_wrong: "Let's leverage our synergies to optimize outcomes."
      example_correct: "Let's work together to get more sales."
```

**REGRA:** Cada anti-pattern DEVE ter:
- `example_wrong:` mostrando o que NAO fazer
- `example_correct:` mostrando a correção na voz do expert

### Step 2: Extract Behavioral Avoidances

```yaml
never_do_communication:
  - behavior: ""
    context: ""
    reason: ""
    workaround: "como contorna"

  # Exemplo:
  - behavior: "Small talk prolongado"
    context: "Reuniões de negócio"
    reason: "Desperdiça tempo"
    workaround: "Vai direto ao ponto após 30s"
```

### Step 3: Identify Rejected Styles

```yaml
rejected_styles:
  - style: ""
    reason: ""
    observed_discomfort: "como reage quando forçado"
```

## Output

```yaml
anti_patterns:
  never_say:
    - term: ""
      source: "[SOURCE: ]"
      reason: ""
      substitute: ""
      example_wrong: ""
      example_correct: ""

  never_do:
    - behavior: ""
      context: ""
      reason: ""
      workaround: ""

  rejected_styles:
    - style: ""
      reason: ""
      observed_discomfort: ""
```

## Acceptance Criteria

- [ ] 5+ anti-patterns of communication documented
- [ ] ALL anti-patterns have `example_wrong:` + `example_correct:`
- [ ] All anti-patterns have `source:` with inference citation
- [ ] `example_correct` sounds like the expert would actually say it
- [ ] Behavioral avoidances documented with workarounds
- [ ] Rejected styles identified with discomfort observations

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EVD-003 | All anti-patterns must have source citations | Validate source field for each entry | VETO - BLOCK. Remove uncited entries or find supporting references. |

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `evd-extract-tone.md` (previous step)
- `evd-extract-immune-system.md` (next step)
