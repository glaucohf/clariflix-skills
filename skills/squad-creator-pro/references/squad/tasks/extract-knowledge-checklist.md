---
task: "Extract Knowledge: Checklist Generation"
task_id: extract-knowledge-checklist
version: 1.0.0
execution_type: Agent
model: Sonnet
model_rationale: "Checklist generation is deterministic transformation from SOP -- no deep comprehension needed."
haiku_eligible: true
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

# Task: Checklist Generation

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `extract-knowledge-checklist` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |
| **Estimated Time** | `15-30 min` |

## Metadata

| Key | Value |
|-----|-------|
| Parent Task | `extract-knowledge` |
| Phase | 3 (Checklist Generation) |
| Gate | `CHECKLIST_QUALITY` |
| Depends On | Phase 2 (SOP Extraction) |
| Skip Condition | `format == 'framework' OR format == 'sop'` |

## Purpose

Generate a validation checklist with 1:1 correspondence to the SOP. Every checkbox maps to an SOP element. No "safety" additions -- zero invention.

## Prerequisites

- Phase 2 (SOP Extraction) completed
- `{topic}-sop.md` available and passed SOP_QUALITY gate

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| topic | string | Yes | Specific topic |
| sop_file | file | Yes | SOP output from Phase 2 |

## Workflow / Steps

### Step 3.1: Read Complete SOP

```yaml
action: "Load SOP from Phase 2"
input: "{topic}-sop.md"
extract:
  - all_steps
  - all_preconditions
  - all_outputs
  - all_guardrails
  - all_decision_rules
```

### Step 3.2: Generate Step Checkboxes

For each SOP step:

```markdown
### Step X: [Step Name]

**Preconditions:**
- [ ] [Precondition 1 from SOP]
- [ ] [Precondition 2 from SOP]

**Execution:**
- [ ] [Action item 1 from SOP]
- [ ] [Action item 2 from SOP]

**Output Validation:**
- [ ] [Output 1] produced
- [ ] [Output 1] meets [quality criteria from SOP]

**Guardrails:**
- [ ] [Guardrail 1] verified
- [ ] [Guardrail 2] verified
```

### Step 3.3: Generate Gate Checkboxes

For each quality gate in SOP:

```markdown
### Quality Gate: [Gate Name]

- [ ] [Criterion 1 from SOP]
- [ ] [Criterion 2 from SOP]
- [ ] [Criterion 3 from SOP]
- [ ] Minimum score achieved: [X/Y]

**Decision:**
- [ ] PASS -> Proceed to next phase
- [ ] FAIL -> Return to [step] for remediation
```

### Step 3.4: Validate 1:1 Correspondence

```yaml
validation:
  for_each_checkbox:
    - has_corresponding_sop_element: true
    - source_traceable: true
  for_each_sop_step:
    - has_checkbox_coverage: true
  invented_checkboxes: 0
```

### Checklist Quality Gate

| Criterion | Requirement | Status |
|-----------|-------------|--------|
| Step coverage | 100% of SOP steps | [ ] |
| Checkbox mapping | Each -> SOP element | [ ] |
| Zero invention | No "safety" additions | [ ] |
| Gates included | All quality gates | [ ] |
| Logical sequence | Matches SOP order | [ ] |

**Threshold:** 5/5 required

### Anti-Invention Check (Checklist)

- [ ] Every checkbox maps to SOP step?
- [ ] No "safety" checkboxes invented?
- [ ] Sequence reflects SOP faithfully?

## Output

| Output | Type | Location | Description |
|--------|------|----------|-------------|
| checklist | MD | `squads/{squad}/checklists/{topic}-sop-checklist.md` | Validation checklist |

## Acceptance Criteria

- [ ] 100% SOP step coverage in checkboxes
- [ ] Each checkbox maps to a specific SOP element
- [ ] All quality gates from SOP included as gate checkboxes
- [ ] Zero invented checkboxes (no "safety" additions)
- [ ] Logical sequence matches SOP order
- [ ] CHECKLIST_QUALITY gate: 5/5 passed
- [ ] Anti-invention check: all items verified
- [ ] `{topic}-sop-checklist.md` written to correct location

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-EKN-003 | Zero-invention constraint | Validate every checkbox traces to SOP element | VETO - BLOCK. Remove invented checkboxes. |

## Related Documents

| Document | Relationship |
|----------|-------------|
| `extract-knowledge.md` | Parent task (stub) |
| `extract-knowledge-sop.md` | Previous phase (dependency) |
| `extract-knowledge-validation.md` | Next phase (final validation) |
