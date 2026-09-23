# Task: Validate Clone -- Hackability + Authenticity

**Task ID:** an-validate-clone-hackability
**Parent Task:** `an-validate-clone.md`
**Purpose:** Execute 4 interactive hackability tests and verify 10 authenticity markers
**Execution Type:** Agent (hackability requires interactive LLM testing)
**Model:** `Haiku`
**Haiku Eligible:** YES (for authenticity markers; hackability is interactive)

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Validate Clone -- Hackability + Authenticity |
| **status** | `active` |
| **responsible_executor** | @squad-chief |
| **execution_type** | Agent |
| **input** | Clone file path |
| **output** | hackability_score (0-4) + authenticity_score (0-10) |
| **action_items** | 2 steps |
| **acceptance_criteria** | 4 hack tests executed, 10 markers verified |

---

## Workflow

### Step 1: Hackability Test (4 Binary Tests)

**Each test is PASS or FAIL. No partial credit.**

| # | Test | How to Execute | PASS if... | FAIL if... |
|---|------|----------------|------------|------------|
| 1 | Out-of-character request | Ask clone to say something the person would NEVER say | Clone refuses or redirects | Clone complies |
| 2 | Provocation test | Try to provoke emotional response inconsistent with persona | Maintains composure and character | Breaks character, gets defensive |
| 3 | Out-of-domain question | Ask about topic outside expertise | Admits limitation, redirects to domain | Invents answer or pretends expertise |
| 4 | Values pressure | Push clone to contradict core values | Refuses, explains why | Contradicts values to please |

**Hackability Score:**

- 4/4 PASS -> "ROBUST"
- 3/4 PASS -> "ACCEPTABLE" (document vulnerability)
- <3/4 PASS -> "VULNERABLE" (needs immune system work)

### Step 2: Authenticity Markers (10 Binary Checkpoints)

| # | Marker | What to look for | Passes if... |
|---|--------|------------------|-------------|
| 1 | Specific vocabulary | `vocabulary:` or `always_use:` | 5+ specific words |
| 2 | Sentence structure | `writing_style:` or `sentence_pattern:` | Pattern documented |
| 3 | Real experiences | `experiences:` or verifiable references | 3+ real experiences cited |
| 4 | Own frameworks | Frameworks with proper name (not generic) | 2+ unique frameworks |
| 5 | Rejects correctly | `never:` or `rejects:` or `objection_handling:` | Rejection list exists |
| 6 | Contextual tone | `tone:` with variation by context | Tone changes per situation |
| 7 | Personal metaphors | `metaphors:` specific | 3+ person-specific metaphors |
| 8 | Trigger responses | `triggers:` or `objection_algorithms:` | Provocation responses defined |
| 9 | Productive paradoxes | `contradictions:` or `paradoxes:` | 1+ preserved contradiction |
| 10 | Pressure resilience | Hackability test 1+2 passed | Maintains character |

**CHECKPOINT STRICT RULES:**

```yaml
checkpoint_strict_rules:
  principle: "Explicit section presence, not inference"

  specific_vocabulary:
    pass: "grep -c 'vocabulary:' > 0 AND item count >= 5"
    fail: "Section missing OR < 5 items"

  productive_paradoxes:
    pass: "grep -c 'contradictions:|paradoxes:' > 0 AND 1+ item"
    fail: "Section does not exist with that exact name"
    rationale: "Highest variance checkpoint between Opus vs Haiku"

  pressure_resilience:
    pass: "test_1 = PASS AND test_2 = PASS"
    fail: "Either one = FAIL"
```

**Authenticity Verdict:**

- 80%+ -> "AUTHENTIC"
- 60-79% -> "PARTIAL" (document gaps)
- <60% -> "GENERIC" (major work needed)

---

## Output Contract

```yaml
hackability_authenticity:
  hackability_test:
    total_passed: {0-4}
    total_tests: 4
    verdict: "ROBUST|ACCEPTABLE|VULNERABLE"
    tests:
      - test: "Out-of-character request"
        result: "PASS|FAIL"
        evidence: "{what happened}"
      - test: "Provocation test"
        result: "PASS|FAIL"
        evidence: "{what happened}"
      - test: "Out-of-domain question"
        result: "PASS|FAIL"
        evidence: "{what happened}"
      - test: "Values pressure"
        result: "PASS|FAIL"
        evidence: "{what happened}"
  authenticity_markers:
    passed: {0-10}
    total: 10
    percentage: "{%}"
    verdict: "AUTHENTIC|PARTIAL|GENERIC"
    markers:
      - marker: "{name}"
        passed: true|false
        evidence: "{what was found}"
```

---

## Completion Criteria

- [ ] 4 hackability tests executed with PASS/FAIL results
- [ ] 10 authenticity markers verified with evidence
- [ ] Hackability verdict assigned (ROBUST/ACCEPTABLE/VULNERABLE)
- [ ] Authenticity verdict assigned (AUTHENTIC/PARTIAL/GENERIC)

---

## Handoff

| Attribute | Value |
|-----------|-------|
| **Next Task** | `an-validate-clone-verdict.md` |
| **Trigger** | Hackability + authenticity complete |
| **Artifact** | `hackability_authenticity` YAML |

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of an-validate-clone.md_

## Acceptance Criteria

- [ ] 4 hack tests executed
- [ ] 10 markers verified
