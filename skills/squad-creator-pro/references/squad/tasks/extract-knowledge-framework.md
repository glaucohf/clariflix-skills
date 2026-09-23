---
task: "Extract Knowledge: Framework Extraction"
task_id: extract-knowledge-framework
version: 1.0.0
execution_type: Agent
model: Opus
model_rationale: "Semantic extraction of formulas, principles, and relationships requires deep comprehension."
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

# Task: Framework Extraction

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `extract-knowledge-framework` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |
| **Estimated Time** | `30-60 min` |

## Metadata

| Key | Value |
|-----|-------|
| Parent Task | `extract-knowledge` |
| Phase | 1 (Framework Extraction) |
| Gate | `FRAMEWORK_QUALITY` |
| Skip Condition | `format == 'sop' OR format == 'checklist'` |

## Purpose

Extract the conceptual model (formulas, principles, components, relationships) from author source materials. Every element must have a literal citation -- zero invention.

**Principle:** "Se nao esta na fonte, nao existe no output."

## Prerequisites

- Phase 0 (Source Validation) passed with GO or CONDITIONAL
- `source_inventory.yaml` available with scored sources
- Sources with relevance >= 5/10 accessible

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| author_name | string | Yes | Author/expert name |
| topic | string | Yes | Specific topic to extract |
| sources_path | path | Yes | Path to source materials |
| source_inventory | file | Yes | Output from source-validation phase |

## Workflow / Steps

### Step 1.1: Identify Core Formula

```yaml
question: "O autor resume o conceito em uma formula/equacao?"
search_patterns:
  - "equals", "is", "formula", "equation"
  - Mathematical notation
  - "X = Y / Z" patterns
output:
  core_formula: "[extracted formula]"
  source: "[SOURCE: page/minute]"
```

**Example:**
```
Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort & Sacrifice)
[SOURCE: $100M Offers, Chapter 6, p.47]
```

### Step 1.2: Map Components/Pillars

```yaml
question: "Quais sao os elementos fundamentais do framework?"
search_patterns:
  - "The X pillars", "The X steps"
  - Numbered lists
  - "First... Second... Third..."
output:
  components:
    - name: "[Component name]"
      description: "[Author's description]"
      source: "[SOURCE: page/minute]"
```

### Step 1.3: Extract Principles/Axioms

```yaml
question: "Quais verdades o autor considera absolutas?"
search_patterns:
  - "Always...", "Never..."
  - "The key is...", "The secret is..."
  - Emphasized statements
output:
  principles:
    - principle: "[Exact quote]"
      context: "[When it applies]"
      source: "[SOURCE: page/minute]"
```

### Step 1.4: Document Relationships

```yaml
question: "Como os componentes se conectam?"
output:
  relationships:
    - from: "[Component A]"
      to: "[Component B]"
      relation: "[increases/decreases/enables/blocks]"
      source: "[SOURCE: page/minute]"
```

### Step 1.5: Collect Author Examples

```yaml
question: "Como o autor demonstra o framework?"
requirement: "ONLY examples from the author - NEVER invented"
output:
  examples:
    - scenario: "[What the author described]"
      application: "[How framework was applied]"
      result: "[Outcome mentioned]"
      source: "[SOURCE: page/minute]"
```

### Step 1.6: Compile Literal Quotes

```yaml
requirement: "Minimum 15 quotes with [SOURCE: page/minute]"
format: |
  > "[Exact quote from author]"
  > -- {author_name}, [SOURCE: book/video, page/minute]
```

### Framework Quality Gate

| Criterion | Requirement | Status |
|-----------|-------------|--------|
| Core formula | Identified with citation | [ ] |
| Components | 3+ documented | [ ] |
| Principles | 5+ extracted | [ ] |
| Examples | 3+ from author (not invented) | [ ] |
| Quotes | 15+ with sources | [ ] |
| Zero invention | No unsourced claims | [ ] |

**Threshold:** 6/6 required

### Anti-Invention Check (Framework)

- [ ] Every formula has literal citation?
- [ ] Every principle comes from author quote?
- [ ] Every example is from author (not invented)?
- [ ] No generic "best practices" added?
- [ ] 15+ quotes with [SOURCE: page/minute]?

## Output

| Output | Type | Location | Description |
|--------|------|----------|-------------|
| framework | MD | `squads/{squad}/docs/frameworks/{topic}-framework.md` | Conceptual model (formulas, principles) |

## Acceptance Criteria

- [ ] Core formula identified with literal citation
- [ ] 3+ components documented with source references
- [ ] 5+ principles extracted as exact quotes
- [ ] 3+ author examples (never invented)
- [ ] 15+ literal quotes with [SOURCE: page/minute]
- [ ] FRAMEWORK_QUALITY gate: 6/6 passed
- [ ] Anti-invention check: all items verified
- [ ] `{topic}-framework.md` written to correct location

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EKN-003 | Zero-invention constraint must be verifiable | Validate all claims have SOURCE citations | VETO - BLOCK. Delete unsourced claims or find literal source. |
## Related Documents

| Document | Relationship |
|----------|-------------|
| `extract-knowledge.md` | Parent task (stub) |
| `extract-knowledge-source-validation.md` | Previous phase (dependency) |
| `extract-knowledge-sop.md` | Next phase (if triplet mode) |
