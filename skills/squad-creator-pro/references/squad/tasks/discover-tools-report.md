# Task: Discover Tools Report (Extension Wrapper)

**Task ID:** discover-tools-report
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a geração dos artefatos finais ao owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task base

---

## Purpose

Este wrapper existe para fechar o pipeline do pro com um owner explícito de reporting sem duplicar a lógica do base.

O owner canônico permanece em:

- `squads/squad-creator/tasks/discover-tools-report.md`

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `recommend_output` | object | Yes | Recomendações consolidadas |
| `scan_output` | object | Yes | Baseline de scan |
| `domain` | string | Yes | Domínio alvo |

---

## Workflow

### Step 1: Delegate to Base Report Task

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/discover-tools-report.md"
  payload:
    - recommend_output
    - scan_output
    - domain
  prohibition:
    - "Do NOT duplicate report generation logic in squad-creator-pro"
```

### Step 2: Reconcile Outputs

```yaml
reconcile_outputs:
  outputs:
    - ".aiox/squad-runtime/discovery/{domain}/tool-discovery-report.md"
    - ".aiox/squad-runtime/discovery/{domain}/capability-tools.yaml"
    - ".aiox/squad-runtime/discovery/{domain}/tool-integration-plan.md"
  return_shape:
    delegated_task: "squads/squad-creator/tasks/discover-tools-report.md"
    status: "delegated"
```

---

## Output

```yaml
output:
  name: delegated_discover_tools_report
  format: yaml
  structure:
    delegated_task: "squads/squad-creator/tasks/discover-tools-report.md"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] A geração dos artefatos finais continua centralizada no base
- [ ] O workflow do pro passa a ter owner atômico explícito na fase de handoff
- [ ] Nenhuma implementação paralela de relatório permanece aqui

---

## Related Documents

- `squads/squad-creator/tasks/discover-tools-report.md` -- owner canônico
- `workflows/wf-discover-tools.yaml` -- consumidor local no pro

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed discover-tools-report output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified
