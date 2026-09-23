# Task: Squad Fusion -- Analysis

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `squad-fusion-analysis` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `hybrid` (Worker + Agent) |

## Metadata

```yaml
id: squad-fusion-analysis
name: "Squad Fusion Analysis"
category: fusion
agent: squad-chief
elicit: false
autonomous: true
description: "Detecta duplicatas, conflitos e gaps nos componentes inventariados. Produz merge plan categorizado (keep/merge/discard)."
```

## Purpose

Detectar duplicatas, conflitos e gaps entre os componentes inventariados. Produzir um merge plan que categoriza cada componente em keep, merge ou discard -- com rationale documentado.

## Workflow / Steps

### Step 1: Detect Duplicates

```yaml
detect_duplicates:
  method: "multi-criteria"
  criteria:
    - name_similarity: 0.8   # Threshold for filename match
    - content_similarity: 0.7 # Threshold for content overlap
    - purpose_match: true     # Semantic purpose alignment
  output: "duplicates.yaml"
  per_duplicate:
    - component_a: "{path}"
    - component_b: "{path}"
    - similarity_score: N
    - recommendation: "keep_a | keep_b | merge | keep_both"
```

### Step 2: Detect Conflicts

```yaml
detect_conflicts:
  types:
    - name_collision: "Same filename in different squads"
    - config_conflict: "Different values for same key in config.yaml"
    - dependency_conflict: "Incompatible dependencies between squads"
  output: "conflicts.yaml"
  per_conflict:
    - type: "{conflict_type}"
    - description: "{human-readable description}"
    - sources: ["{squad-a}", "{squad-b}"]
    - resolution_options: ["option_1", "option_2", ...]
```

### Step 3: Identify Gaps

```yaml
identify_gaps:
  check:
    - "Missing orchestrator agent in combined set"
    - "Missing config.yaml fields for target"
    - "Missing README.md content"
    - "Orphan dependencies (referenced but not present)"
  output: "gaps.yaml"
  per_gap:
    - type: "{gap_type}"
    - severity: "blocking | recommended"
    - remediation: "{suggested fix}"
```

### Step 4: Generate Merge Plan

```yaml
generate_merge_plan:
  output: "merge-plan.yaml"
  contents:
    components_to_keep:
      - "{path}" # Unique components, no conflicts
    components_to_merge:
      - sources: ["{path_a}", "{path_b}"]
        strategy: "content_merge | best_of"
    components_to_discard:
      - path: "{path}"
        reason: "{why discarded}"
    conflicts_requiring_decision:
      - "{conflict reference}" # Only in QUALITY mode
```

### Step 5: Checkpoint

```yaml
checkpoint:
  type: "{mode == 'quality' ? 'human' : 'automatic'}"
  display: |
    ANALYSIS REPORT

    Duplicates Found: {duplicates.count}
    Conflicts Found: {conflicts.count}
    Gaps Identified: {gaps.count}

    DUPLICATES:
    {for dup in duplicates}
      - {dup.name}: {dup.sources}
        Similarity: {dup.similarity}%
        Recommendation: {dup.recommendation}
    {/for}

    CONFLICTS:
    {for conflict in conflicts}
      - {conflict.type}: {conflict.description}
        Resolution options: {conflict.options}
    {/for}

  validate:
    - "Merge plan generated"
    - "All duplicates categorized"
    - "All conflicts have resolution options"
```

## Output

Four YAML files:

| File | Content |
|------|---------|
| `duplicates.yaml` | All detected duplicate pairs with similarity scores |
| `conflicts.yaml` | All detected conflicts with resolution options |
| `gaps.yaml` | All identified gaps with remediation suggestions |
| `merge-plan.yaml` | Categorized component list (keep/merge/discard) |

## Acceptance Criteria

- [ ] Every component from inventory appears in exactly one merge-plan category
- [ ] No component is silently omitted from analysis
- [ ] Duplicate detection uses both name and content similarity
- [ ] All conflicts have at least 2 resolution options
- [ ] QUALITY mode presents human checkpoint; YOLO mode auto-validates

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-SFU-002 | Analysis reports not generated before proceeding to merge | BLOCK. Execute analysis first. |

## Related Documents

- `squad-fusion.md` -- Parent stub task
- `squad-fusion-discovery.md` -- Previous phase (Phase 1)
- `squad-fusion-resolution.md` -- Next phase (Phase 3)
