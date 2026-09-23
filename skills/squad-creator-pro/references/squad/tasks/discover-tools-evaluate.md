# Task: Discover Tools Evaluate (Extension Wrapper)

**Task ID:** discover-tools-evaluate
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega scoring e compatibilidade ao owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task base

---

## Purpose

Este wrapper evita duplicação do modelo de scoring e compatibilidade dentro do `squad-creator-pro`.

O owner canônico permanece em:

- `squads/squad-creator/tasks/discover-tools-evaluate.md`

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `classified_tools` | list | Yes | Ferramentas classificadas |
| `prioritized_gaps` | list | Yes | Gaps priorizados |
| `budget_tier` | enum | No | Faixa de custo alvo |

---

## Workflow

### Step 1: Delegate to Base Evaluation Task

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/discover-tools-evaluate.md"
  payload:
    - classified_tools
    - prioritized_gaps
    - budget_tier
  prohibition:
    - "Do NOT fork tool scoring in squad-creator-pro"
```

### Step 2: Reconcile Outputs

```yaml
reconcile_outputs:
  primary_output: ".aiox/squad-runtime/discovery/{domain}/evaluated-tools.yaml"
  return_shape:
    delegated_task: "squads/squad-creator/tasks/discover-tools-evaluate.md"
    evaluated_tools: ".aiox/squad-runtime/discovery/{domain}/evaluated-tools.yaml"
```

---

## Output

```yaml
output:
  name: delegated_discover_tools_evaluate
  format: yaml
  structure:
    delegated_task: "squads/squad-creator/tasks/discover-tools-evaluate.md"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] O scoring é herdado do base
- [ ] O workflow do pro passa a ter owner atômico explícito na fase de avaliação
- [ ] Nenhuma lógica paralela de score ou threshold permanece aqui

---

## Related Documents

- `squads/squad-creator/tasks/discover-tools-evaluate.md` -- owner canônico
- `workflows/wf-discover-tools.yaml` -- consumidor local no pro

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed discover-tools-evaluate output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified
