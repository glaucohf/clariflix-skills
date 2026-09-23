---
task-id: extract-voice-dna
name: Extract Voice DNA (Communication & Writing Style)
version: 2.0.0
execution_type: Agent
model: Opus
haiku_eligible: false
model_rationale: "Extração semântica de padrões de comunicação requer interpretação profunda de linguagem natural - não determinístico"
note: "Exemplos usam copywriting. Substitua pelo seu domínio."
estimated-time: 1-2 hours
complexity: medium
decomposed: true

specialist: "@oalanicolas"
specialist_guidance: |
  Use DNA Mental 8-layer architecture.
  Apply curadoria ouro vs bronze para fontes.
  Extract: power_words, signature_phrases, storytelling, anti-patterns, immune_system.
  Follow Playbook + Framework + Swipe File trinity.

inputs:
  required:
    - mind_name: "Nome do expert/mind a clonar"
    - sources: "Mínimo 5 fontes (livros, artigos, entrevistas, podcasts)"

outputs:
  primary:
    - voice_dna: "Bloco YAML com DNA de comunicação/escrita"

elicit: true
related_tasks:
  - extract-thinking-dna.md
---

# Extract Voice DNA

> **Objetivo:** Extrair COMO um expert se comunica e escreve.
>
> **Complemento:** Use `extract-thinking-dna.md` para frameworks e decisões.
>
> **Status:** Decomposed into 9 atomic tasks (v2.0.0).

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EVD-001 | Minimum 5 sources must be available | Verify sources >= 5 items of varied types | VETO - BLOCK. Run collect-sources first. |
| VETO-EVD-002 | Existing voice_dna must be backed up | Check if target agent.md has voice_dna section | VETO - BLOCK. Snapshot before overwriting. |
| VETO-EVD-003 | All entries must have SOURCE citations | Validate [SOURCE: doc, page] format | VETO - BLOCK. Remove uncited entries. |

---

## Execution Pipeline (9 Atomic Tasks)

Execute in order. Each task is self-contained with its own inputs, outputs, and acceptance criteria.

| Phase | Task ID | File | Est. Time |
|-------|---------|------|-----------|
| 1. Collect | `evd-collect-sources` | `evd-collect-sources.md` | 10 min |
| 2. Vocabulary | `evd-extract-vocabulary` | `evd-extract-vocabulary.md` | 15 min |
| 3. Storytelling | `evd-extract-storytelling` | `evd-extract-storytelling.md` | 15 min |
| 4. Writing Style | `evd-extract-writing-style` | `evd-extract-writing-style.md` | 15 min |
| 5. Tone & Voice | `evd-extract-tone` | `evd-extract-tone.md` | 10 min |
| 6. Anti-Patterns | `evd-extract-anti-patterns` | `evd-extract-anti-patterns.md` | 10 min |
| 7. Immune System | `evd-extract-immune-system` | `evd-extract-immune-system.md` | 10 min |
| 8. Contradictions | `evd-extract-contradictions` | `evd-extract-contradictions.md` | 10 min |
| 9. Assembly | `evd-assemble-voice-dna` | `evd-assemble-voice-dna.md` | 15 min |

### Dependencies

```
evd-collect-sources
  |
  +---> evd-extract-vocabulary
  +---> evd-extract-storytelling
  +---> evd-extract-writing-style
  +---> evd-extract-tone
  +---> evd-extract-anti-patterns
  +---> evd-extract-immune-system
  +---> evd-extract-contradictions
           |
           +---> evd-assemble-voice-dna (requires ALL above)
```

Phases 2-8 depend on Phase 1 (sources). Phase 9 (assembly) depends on all phases 2-8.

---

## Canonical Owner

This stub remains the backward-compatible entrypoint for direct task invocation.
The canonical owner of the atomic execution flow is:

- `workflows/wf-extract-voice-dna.yaml`

---

## Quality Gate (enforced in evd-assemble-voice-dna)

### Minimum Quantities (8/10 required)

- [ ] 10+ power words com [SOURCE:]
- [ ] 8+ frases assinatura
- [ ] 3+ metáforas
- [ ] 3+ histórias/anedotas recorrentes
- [ ] Story structure mapeado
- [ ] Todas dimensões de voz preenchidas (1-10)
- [ ] Tom por contexto definido
- [ ] 5+ anti-patterns de comunicação
- [ ] 2+ rejeições automáticas (immune system)
- [ ] 1+ paradoxo/contradição documentado

### Mandatory Requirements (100% required)

- [ ] TODOS power words têm `source:` com [SOURCE: doc, page]
- [ ] TODAS signature_phrases têm `source:` + `example_usage:`
- [ ] TODOS anti-patterns têm `example_wrong:` + `example_correct:`
- [ ] ZERO conteúdo inventado

---

**Squad Architect | Voice DNA Extractor v2.0**
*"Capture how they communicate, not just what they say"*

## Task Anatomy

- **Executor:** Agent
- **Inputs:** mind_name; sources
- **Outputs:** Bloco YAML com DNA de comunicação/escrita
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] All veto conditions checked and none triggered
- [ ] Output artifact produced: Bloco YAML com DNA de comunicação/escrita
- [ ] Task output validated against quality standards
