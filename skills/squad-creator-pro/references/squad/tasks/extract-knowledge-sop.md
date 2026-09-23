---
task: "Extract Knowledge: SOP Extraction"
task_id: extract-knowledge-sop
version: 1.0.0
execution_type: Agent
model: Opus
model_rationale: "SOP decomposition into atomic steps with 8-field task anatomy requires deep comprehension."
haiku_eligible: false
responsavel: "@tim-ferriss"
responsavel_type: agent
atomic_layer: task
elicit: false
phase: discovery
parent_task: extract-knowledge

workflows:
  - wf-extraction-pipeline
config:
  - squad-config
---

# Task: SOP Extraction

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `extract-knowledge-sop` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |
| **Estimated Time** | `45-90 min` |

## Metadata

| Key | Value |
|-----|-------|
| Parent Task | `extract-knowledge` |
| Phase | 2 (SOP Extraction) |
| Gate | `SOP_QUALITY` |
| Depends On | Phase 1 (Framework) if triplet mode |
| Skip Condition | `format == 'framework' OR format == 'checklist'` |

## Purpose

Extract a Standard Operating Procedure from author source materials, decomposed into atomic steps with 8-field task anatomy. Every step must trace to a source citation. Produces the SOP document and agent blueprint.

## Prerequisites

- Phase 0 (Source Validation) passed
- Phase 1 (Framework) completed if running in triplet mode
- Sources with relevance >= 5/10 accessible

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| author_name | string | Yes | Author/expert name |
| topic | string | Yes | Specific topic to extract |
| sources_path | path | Yes | Path to source materials |
| framework | file | No | Framework output from Phase 1 (if triplet mode) |

## Workflow / Steps

### Step 2.1: Identify Author's Process

```yaml
question: "O autor descreve uma sequencia de acoes?"
search_patterns:
  - "First... Then... Finally..."
  - "Step 1... Step 2..."
  - "Start by... Next... End with..."
sources:
  - Framework from Phase 1
  - Practical examples in source material
output:
  process_outline:
    - phase: "[Phase name]"
      steps: ["Step 1", "Step 2", ...]
      source: "[SOURCE: page/minute]"
```

### Step 2.2: Decompose into Atomic Steps

For each identified step:

```yaml
step_template:
  step_number: X
  step_name: "[Verb] + [Object]"

  # 8-Field Task Anatomy
  description: "[What to do - from author]"
  cognitive_type: "Perception|Analysis|Synthesis|Judgment|Creativity|Memory|Empathy|Accountability"
  automation_potential: "High|Medium|Low"
  executor: "Human|Agent|Worker|Hybrid"
  precondition: "[What must exist before]"
  output: "[What is produced]"
  guardrails: "[Limits and validations]"
  decision_rule: "IF [condition] THEN [next step]"

  # Source tracking
  source: "[SOURCE: page/minute]"
```

**Cognitive Types:** Perception, Memory, Analysis, Synthesis, Judgment, Creativity, Empathy, Accountability. Map from author signals (e.g., "Look at..." = Perception, "Decide..." = Judgment).

### Step 2.3: Extract Decision Rules

```yaml
question: "Onde o autor indica decisoes/bifurcacoes?"
search_patterns: ["If... then...", "When... do...", "Depends on...", "Unless..."]
format: "RULE: [name] | IF: [condition] | THEN: [action] | ELSE: [alt] | SOURCE: [ref]"
```

### Step 2.4: Document Exceptions

```yaml
question: "O autor menciona casos especiais?"
search_patterns: ["Except when...", "Unless...", "The only time...", "Never do this if..."]
output:
  exceptions:
    - scenario: "[Exception scenario]"
      handling: "[What to do instead]"
      source: "[SOURCE: page/minute]"
```

### Step 2.5: Define Expected Outputs

```yaml
question: "O que cada fase produz?"
output:
  phase_outputs:
    - phase: "[Phase name]"
      deliverable: "[What is produced]"
      format: "[How it looks]"
      source: "[SOURCE: page/minute]"
```

### Step 2.6: Compile Appendix D

```yaml
requirement: "50+ references with [SOURCE: page/minute]"
format: |
  | ID | Quote/Reference | Source | Page/Min | SOP Section |
  |----|-----------------|--------|----------|-------------|
  | 001 | "[Quote]" | [Book/Video] | p.47 | Part 5, Step 3 |
```

### SOP Quality Gate

| Criterion | Requirement | Status |
|-----------|-------------|--------|
| Steps documented | 8+ steps | [ ] |
| Task Anatomy | 8 fields per step | [ ] |
| Decision rules | All forks covered | [ ] |
| Appendix D | 50+ references | [ ] |
| Zero invention | All steps sourced | [ ] |
| Logical flow | Start to finish | [ ] |

**Threshold:** 6/6 required

### Anti-Invention Check (SOP)

- [ ] Every step sourced, Appendix D 50+ refs, no "general experience", decision rules from author, guardrails from author warnings

## Output

| Output | Type | Location | Description |
|--------|------|----------|-------------|
| sop | MD | `squads/{squad}/docs/sops/{topic}-sop.md` | Operational process (steps, executors) |
| blueprint | YAML | `squads/{squad}/docs/sops/{topic}-squad-blueprint.yaml` | Agent configuration |

## Acceptance Criteria

- [ ] 8+ atomic steps documented with 8-field task anatomy
- [ ] All decision rules extracted with source citations
- [ ] Exceptions documented with author references
- [ ] Phase outputs defined per SOP section
- [ ] Appendix D compiled with 50+ references
- [ ] SOP_QUALITY gate: 6/6 passed
- [ ] Anti-invention check: all items verified
- [ ] `{topic}-sop.md` and `{topic}-squad-blueprint.yaml` written

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EKN-003 | Zero-invention constraint must be verifiable | Validate all steps have SOURCE citations | VETO - BLOCK. Delete unsourced steps or find literal source. |

## Related Documents

| Document | Relationship |
|----------|-------------|
| `extract-knowledge.md` | Parent task (stub) |
| `extract-knowledge-framework.md` | Previous phase (dependency in triplet mode) |
| `extract-knowledge-checklist.md` | Next phase |
