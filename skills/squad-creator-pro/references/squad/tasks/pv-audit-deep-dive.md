# Task: Process Audit -- Deep-Dive

**Task ID:** pv-audit-deep-dive
**Parent Task:** `pv-audit.md`
**Purpose:** On-demand deep analysis of a specific agent, workflow, or DNA file (~3k token budget)
**Execution Type:** Agent
**Model:** Opus
**Haiku Eligible:** NO

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Process Audit -- Deep-Dive |
| **status** | `active` |
| **responsible_executor** | @pedro-valerio |
| **execution_type** | Agent |
| **input** | Specific agent/workflow/dna name from user |
| **output** | `deep_dive` YAML with wrong paths, veto proposals, verdict |
| **action_items** | 2 steps |
| **acceptance_criteria** | Target analyzed, wrong paths found, veto conditions proposed |

---

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-PVA-003 | Must not execute without user direction | User must explicitly request specific agent/workflow/dna analysis | VETO - BLOCK. Phase 3 is on-demand only. |

---

## CRITICAL: Token Budget

**This phase: ~3k tokens maximum.**

**Read ONLY the file explicitly requested by user.**

---

## Commands

- `*audit {squad} agent:{name}` -- Audit 1 specific agent
- `*audit {squad} workflow:{name}` -- Audit 1 specific workflow
- `*audit {squad} dna` -- Verify DNA files

---

## Workflow

### Step 1: Read Target File

Read ONLY the requested file. Apply diagnostic framework:

- "If the executor does not read the instructions, what happens?"
- "If the executor tries to skip a step, can they?"
- "If the executor makes a mistake, does the system detect it automatically?"

Identify wrong paths -- decision points where the executor can go wrong.

### Step 2: Propose Veto Conditions

For each wrong path found, propose a veto condition:

```yaml
veto_conditions_proposed:
  - id: "V{n}"
    condition: "{description}"
    check: "{how to verify}"
    action: "VETO - {what to do}"
```

---

## Output Contract

```yaml
deep_dive:
  target: "{agent/workflow name}"
  wrong_paths_found:
    - point: "{decision point}"
      wrong_path: "{what can go wrong}"
      current_protection: "none | alert | block"
      recommendation: "{veto condition}"
  veto_conditions_proposed:
    - id: "V{n}"
      condition: "{description}"
      check: "{how to verify}"
      action: "VETO - {what to do}"
  verdict: "PASS | NEEDS WORK | REDESIGN"
```

---

## Completion Criteria

- [ ] Target file read (only the one requested)
- [ ] Wrong paths identified with current protection level
- [ ] Veto conditions proposed for unprotected paths
- [ ] Verdict assigned (PASS / NEEDS WORK / REDESIGN)
- [ ] Token budget respected (~3k)

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of pv-audit.md_

## Acceptance Criteria

- [ ] Target analyzed
- [ ] wrong paths found
- [ ] veto conditions proposed
