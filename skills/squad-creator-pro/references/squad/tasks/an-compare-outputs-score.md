---
task-id: an-compare-outputs-score
name: "Score 4 Evaluation Dimensions"
version: 1.0.0
execution_type: Agent
model: Opus
model_rationale: "Opus REQUIRED for evaluator independence. Recommendation quality is subjective."
haiku_eligible: false
estimated-time: 10 min
complexity: medium

inputs:
  required:
    - comparable_items: "Normalized items from Phase 1"

outputs:
  primary:
    - dimension_scores: "Scores for all 4 dimensions with veto checks"

elicit: false
---

# Task: Score 4 Evaluation Dimensions

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-compare-outputs-score` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

- **Parent Task:** `an-compare-outputs` (orchestrator stub)
- **Sequence:** Phase 2 of 3
- **Previous Task:** `an-compare-outputs-load`
- **Next Task:** `an-compare-outputs-report`

## Purpose

Score each of the 4 evaluation dimensions using the rubric, and check veto conditions.

## Workflow / Steps

### Step 1: Dimension 1 -- TIER MATCH (40 points)

```yaml
tier_match:
  weight: 40
  calculation: "match_rate = count(opus_tier == haiku_tier) / total_items"
  scoring:
    perfect_match: 40    # 100%
    high_match: 32       # 90-99%
    moderate_match: 24   # 75-89%
    low_match: 16        # 50-74%
    poor_match: 0        # <50%
  veto: "IF match_rate < 0.75 -> VETO"
```

### Step 2: Dimension 2 -- SCORE VARIANCE (30 points)

```yaml
score_variance:
  weight: 30
  calculation: |
    FOR each item: variance = abs(opus - haiku) / opus * 100
    Use max_variance for scoring (worst case)
  scoring:
    within_5pct: 30
    within_10pct: 24
    within_15pct: 18
    within_20pct: 12
    beyond_20pct: 0
  veto: "IF max_variance > 25% -> VETO"
  review: "IF max_variance > 15% -> REVIEW"
```

### Step 3: Dimension 3 -- CHECKPOINT MATCH (20 points)

```yaml
checkpoint_match:
  weight: 20
  calculation: "match_rate = matching_checkpoints / total_checkpoints"
  scoring:
    perfect_match: 20    # 100%
    high_match: 16       # 95-99%
    moderate_match: 12   # 90-94%
    low_match: 8         # 80-89%
    poor_match: 0        # <80%
  note: "If task has no binary checkpoints, award 20 points"
```

### Step 4: Dimension 4 -- RECOMMENDATION QUALITY (10 points)

```yaml
recommendation_quality:
  weight: 10
  evaluation: "Would user take same action based on each output?"
  scoring:
    same_actions: 10
    similar_actions: 7
    different_actions: 3
    contradictory: 0
  veto: "IF contradictory -> VETO"
```

### Step 5: Check Veto Conditions

| ID | Condition | Severity |
|----|-----------|----------|
| MTQ_VC_001 | Score Variance >15% | review |
| MTQ_VC_002 | Score Variance >25% | veto |
| MTQ_VC_003 | Tier Match <90% | review |
| MTQ_VC_004 | Tier Match <75% | veto |
| MTQ_VC_005 | Contradictory Recommendations | veto |

## Output

```yaml
dimension_scores:
  tier_match:
    score: 0  # /40
    match_rate: "0%"
  score_variance:
    score: 0  # /30
    avg_variance: "0%"
    max_variance: "0%"
  checkpoint_match:
    score: 0  # /20
    match_rate: "0%"
  recommendation_quality:
    score: 0  # /10
    assessment: "same|similar|different|contradictory"
  total: 0  # /100
  vetos_triggered: []
  reviews_triggered: []
```

## Acceptance Criteria

- [ ] All 4 dimensions scored per rubric
- [ ] Calculations are reproducible and shown
- [ ] Veto conditions checked and documented
- [ ] Total score calculated

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-compare-outputs.md` | Parent orchestrator |
| `an-compare-outputs-load.md` | Previous phase |
| `an-compare-outputs-report.md` | Next phase |
