# Task: Next Action -- Implement

**Task ID:** next-action-implement
**Parent Task:** `next-action.md`
**Purpose:** Apply Next Action pattern to greeting script, add CTA callout, create validation tests
**Orchestrator:** @squad-chief
**Execution Type:** `Agent`
**Model:** `Opus`
**Haiku Eligible:** NO

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Next Action -- Implement |
| **status** | `active` |
| **responsible_executor** | @squad-chief |
| **execution_type** | Agent |
| **input** | `gap_map` YAML from `next-action-gap-map.md` + greeting script path |
| **output** | Updated greeting script + validation tests + upgrade report |
| **action_items** | 3 steps |
| **acceptance_criteria** | Greeting ends with `**Next Action:** \`...\`` matching gaps/continuity |

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-NA-004 | Greeting alterado sem teste minimo | Verificar teste unitario ou de contrato cobrindo o CTA final | VETO - BLOCK. Nao deixar heuristica de continuidade sem protecao automatizada. |

---

## Workflow

### Step 1: Implement Inference Functions

Add to the greeting script:

```js
function inferNextAction(context) {
  // Priority 1: Blocking gaps
  for (const signal of gap_map.blocking) {
    if (detectSignal(signal, context)) return signal.next_action;
  }
  // Priority 2: Non-blocking gaps
  for (const signal of gap_map.non_blocking) {
    if (detectSignal(signal, context)) return signal.next_action;
  }
  // Priority 3: Ready state
  return gap_map.ready_state.next_action;
}

function buildNextActionCallout(context) {
  const nextAction = inferNextAction(context);
  return `**Next Action:** \`${nextAction}\``;
}
```

### Step 2: Insert CTA in Greeting

- Preserve the existing context block
- Add the CTA callout at the **end** of the greeting output

Target format:

```text
## Starter Commands

- `*help`
- `*show-context`
- `*triage {request}`

**Next Action:** `*triage {request}`
```

### Step 3: Create Validation Tests

Create automated tests covering:

```yaml
tests:
  - scenario: "no runtime context"
    setup: "empty or missing session-context.yaml"
    expected_next_action: "bootstrap command (e.g., set-active-context)"
  - scenario: "blocking gap present"
    setup: "missing required file (e.g., campaign-brief.yaml)"
    expected_next_action: "gap remediation command"
  - scenario: "ready context"
    setup: "all signals clear, context fully loaded"
    expected_next_action: "intake or execution command"
```

Validation checks:

- Greeting renders without error
- CTA final is at the end of output
- CTA command is consistent with the gap/context of the scenario

---

## Output Contract

```yaml
next_action_upgrade:
  squad_name: "{squad_name}"
  mode: "apply"
  greeting_script: "{path}"
  context_sources: []
  gaps_detected: []
  next_action_rules:
    blocking: []
    non_blocking: []
    ready_state: ""
  cta_added: true
  tests_added: []
  final_result: "PASS|FAIL"
```

---

## Completion Criteria

- [ ] `inferNextAction(context)` function added to greeting script
- [ ] `buildNextActionCallout(context)` function added
- [ ] CTA callout inserted at end of greeting output
- [ ] Validation tests created for 3 scenarios (no context, blocking gap, ready)
- [ ] All tests pass

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of next-action.md_

## Acceptance Criteria

- [ ] Greeting ends with `**Next Action:** \`...\`` matching gaps/continuity
