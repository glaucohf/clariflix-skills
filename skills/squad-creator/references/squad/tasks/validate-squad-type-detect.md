# Task: Validate Squad — Type Detection

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-type-detect` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-type-detect
name: "Validate Squad Type Detection"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Detect squad type (Expert/Pipeline/Hybrid/Operational) from config + structural signals."
```

## Purpose

Determine the squad type using a deterministic algorithm with dominant signal overrides and a fallback scoring system. The detected type drives which requirements and veto conditions apply in downstream validation tasks.

## Prerequisites

- [ ] Preflight completed successfully (`validate-squad-preflight`)
- [ ] `/tmp/preflight-results.yaml` exists with signal data
- [ ] `data/squad-type-definitions.yaml` accessible

## Inputs

```yaml
inputs:
  squad_name:
    type: string
    required: true
  squad_path:
    type: string
    required: false
    default: "squads/{squad_name}/"
  type_override:
    type: string
    required: false
    description: "Force squad type: expert, pipeline, hybrid, operational"
  preflight_results:
    type: file
    required: true
    path: "/tmp/preflight-results.yaml"
```

## Workflow / Steps

### Step 1: Collect Signals (from preflight data)

Read signal values from preflight results. Do NOT re-collect manually.

```yaml
signal_collection:
  agents_count: "N (from preflight)"
  voice_dna_count: "N (agents containing 'voice_dna:')"
  voice_dna_percentage: "voice_dna_count / agents_count * 100"
  workflow_count: "N (.yaml files in workflows/)"
  has_heuristic_ids: "true/false (patterns PV_|SC_|HO_ present)"
  tasks_count: "N (.md files in tasks/, recursive)"
  has_real_person_names: "true/false (e.g. gary-halbert, eugene-schwartz)"
  has_tier_organization: "true/false ('tier:' or 'Tier 0' in config/agents)"
```

### Step 2: Check Type Override

If `type_override` is provided, skip detection and use the override directly. Log that override was applied.

### Step 3: Check Dominant Signals

Dominant signals are EXCLUSIVE -- only ONE type has them. If triggered, skip scoring.

```yaml
dominant_signals:
  expert_override:
    condition: "voice_dna_percentage >= 50"
    action: "TYPE = Expert (OVERRIDE)"
    rationale: "Pipeline and Hybrid squads NEVER have voice_dna in agents."

  hybrid_override:
    condition: "has_heuristic_ids == true"
    action: "TYPE = Hybrid (OVERRIDE)"
    rationale: "Only Hybrid squads use heuristic IDs (PV_*, SC_*, HO_*)."
```

### Step 4: Scoring Algorithm (only if no dominant signal)

```yaml
detection_algorithm:
  expert_score: 0
  pipeline_score: 0
  hybrid_score: 0

  # EXCLUSIVE signals - HIGH weight
  if voice_dna_percentage >= 50:  expert_score += 5
  if has_heuristic_ids:           hybrid_score += 5
  if has_real_person_names:       expert_score += 3

  # SHARED signals - LOW weight
  if agents_count >= 5:           expert_score += 1
  if has_tier_organization:       expert_score += 1
  if workflow_count > 0:          pipeline_score += 2
  if tasks_count > agents_count * 3: pipeline_score += 1

  # NEGATIVE weights
  if voice_dna_percentage >= 50:  pipeline_score -= 3
  if has_heuristic_ids:           pipeline_score -= 2

  # Shared neutral signals
  if has_orchestrator_agent:      pipeline_score += 1
  if has_persona_profile_pattern: hybrid_score += 2

  # Determine winner
  detected_type: max(expert_score, pipeline_score, hybrid_score)

  # Tie-breaking
  if tie:
    if has_real_person_names: "expert"
    elif workflow_count > 0: "pipeline"
    else: "pipeline"  # default
```

### Step 5: Load Type Requirements

```yaml
load_requirements:
  file: "data/squad-type-definitions.yaml"
  section: "squad_types.{detected_type}"
  output:
    required_components: [...]
    optional_components: [...]
    veto_conditions: [...]
    benchmarks: {...}
```

## Output

```yaml
output:
  schema:
    detected_type: "expert | pipeline | hybrid | operational"
    confidence: 0.0-1.0
    detection_method: "dominant_signal | scoring | override"
    signals:
      agents_count: N
      voice_dna_present: true/false
      voice_dna_percentage: N
      has_workflow: true/false
      has_heuristic_ids: true/false
      task_agent_ratio: N
    requirements_loaded: true/false
    required_components: [...]
    veto_conditions: [...]
```

## Acceptance Criteria

- [ ] Type is detected deterministically from structural signals
- [ ] Dominant signals short-circuit the scoring algorithm
- [ ] Override parameter bypasses detection entirely
- [ ] Type-specific requirements are loaded from `squad-type-definitions.yaml`
- [ ] Confidence score reflects detection method quality

## Veto Conditions

- Squad does not exist -> VETO (should be caught by preflight)
- No agents found -> VETO (cannot determine type without agents)
- `squad-type-definitions.yaml` missing -> VETO (cannot load requirements)

## Related Documents

- `validate-squad.md` (parent composed task)
- `validate-squad-preflight.md` (provides signal data)
- `data/squad-type-definitions.yaml` (type definitions and requirements)
