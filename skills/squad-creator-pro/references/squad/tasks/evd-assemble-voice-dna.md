---
task-id: evd-assemble-voice-dna
name: "Voice DNA: Assemble Final Output & Quality Check"
version: 1.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
estimated-time: 15 min
complexity: medium

inputs:
  required:
    - vocabulary_block: "Output from evd-extract-vocabulary"
    - storytelling_block: "Output from evd-extract-storytelling"
    - writing_style_block: "Output from evd-extract-writing-style"
    - tone_block: "Output from evd-extract-tone"
    - anti_patterns_block: "Output from evd-extract-anti-patterns"
    - immune_system_block: "Output from evd-extract-immune-system"
    - contradictions_block: "Output from evd-extract-contradictions"
    - mind_name: "Nome do expert"

outputs:
  primary:
    - voice_dna: "Bloco YAML completo com DNA de comunicação/escrita"

elicit: false
parent_task: extract-voice-dna.md
related_tasks:
  - extract-thinking-dna.md
---

# Task: Voice DNA -- Assemble Final Output & Quality Check

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `evd-assemble-voice-dna` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

- **Parent:** `extract-voice-dna.md`
- **Phase:** Assembly (post-extraction)
- **Model:** Opus (final assembly and quality validation)

## Purpose

Assemble all extracted voice DNA components into the final unified YAML block and run the quality check to ensure minimum thresholds and mandatory requirements are met.

## Prerequisites

- ALL 8 extraction phases completed:
  1. `evd-collect-sources` -- sources validated
  2. `evd-extract-vocabulary` -- power words, phrases, metaphors, rules
  3. `evd-extract-storytelling` -- stories, anecdotes, examples, structure
  4. `evd-extract-writing-style` -- structure, devices, formatting, patterns
  5. `evd-extract-tone` -- dimensions, contextual tone, identity statement
  6. `evd-extract-anti-patterns` -- never-say, never-do, rejected styles
  7. `evd-extract-immune-system` -- rejections, boundaries, defenses
  8. `evd-extract-contradictions` -- paradoxes, inconsistencies, preservation

## Inputs

All outputs from the 8 extraction phases.

## Workflow / Steps

### Step 1: Assemble Voice DNA Block

Merge all phase outputs into the unified structure:

```yaml
# =====================================================
# VOICE DNA - {MIND_NAME}
# Focus: Communication & Writing Style
# Extracted: {DATE}
# =====================================================

voice_dna:
  identity_statement: ""  # From evd-extract-tone

  vocabulary:       # From evd-extract-vocabulary
    power_words: []
    signature_phrases: []
    metaphors: []
    rules: {}

  storytelling:     # From evd-extract-storytelling
    recurring_stories: []
    personal_anecdotes: []
    favorite_examples: []
    story_structure: {}

  writing_style:    # From evd-extract-writing-style
    structure: {}
    sentence_patterns: []
    rhetorical_devices: {}
    formatting: {}

  tone:             # From evd-extract-tone
    dimensions: {}
    by_context: {}

  anti_patterns:    # From evd-extract-anti-patterns
    never_say: []
    never_do: []
    rejected_styles: []

  immune_system:    # From evd-extract-immune-system
    automatic_rejections: []
    emotional_boundaries: []
    fierce_defenses: []

  voice_contradictions:  # From evd-extract-contradictions
    paradoxes: []
    authentic_inconsistencies: []
    preservation_note: ""
```

### Step 2: Run Quality Check -- Minimum Quantities

- [ ] 10+ power words com [SOURCE:]
- [ ] 8+ frases assinatura (não apenas 5)
- [ ] 3+ metáforas
- [ ] 3+ histórias/anedotas recorrentes
- [ ] Story structure mapeado
- [ ] Todas dimensões de voz preenchidas (1-10)
- [ ] Tom por contexto definido
- [ ] 5+ anti-patterns de comunicação
- [ ] 2+ rejeições automáticas (immune system)
- [ ] 1+ paradoxo/contradição documentado

### Step 3: Run Quality Check -- Mandatory Requirements

- [ ] TODOS power words têm `source:` com [SOURCE: doc, page]
- [ ] TODAS signature_phrases têm `source:` com [SOURCE: doc, page]
- [ ] TODAS signature_phrases têm `example_usage:` (copy NOVO, não citação)
- [ ] TODOS anti-patterns têm `example_wrong:` + `example_correct:`
- [ ] ZERO conteúdo inventado - apenas extraído das fontes

### Step 4: Final Verification

- [ ] Posso rastrear cada claim até uma fonte específica?
- [ ] Os example_usage são copy NOVO (não apenas repetir a citação)?
- [ ] Os example_correct soam como o expert falaria?

**Score mínimo:** 8/10 quantidades + 100% requisitos de qualidade --> PASS

### Step 5: Backup Check (if modifying existing agent)

If target agent.md already contains a voice_dna section, create snapshot before overwriting.

## Output

The complete `voice_dna:` YAML block ready for insertion into the agent file.

## Acceptance Criteria

- [ ] All 8 phase outputs merged into single unified block
- [ ] Minimum quantities checklist: 8/10 items pass
- [ ] Mandatory requirements: 100% pass (no exceptions)
- [ ] Final verification: all 3 checks pass
- [ ] Existing voice_dna backed up if applicable (VETO-EVD-002)

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EVD-002 | Existing voice_dna block must be backed up before modification | Check if target agent.md already contains a voice_dna section | VETO - BLOCK. Create snapshot before overwriting. |
| VETO-EVD-003 | All entries must have SOURCE citations | Validate every vocabulary entry has non-empty source field | VETO - BLOCK. Remove uncited entries or find supporting references. |

## Related Documents

- `extract-voice-dna.md` (parent stub)
- `extract-thinking-dna.md` (complementary: frameworks and decisions)
