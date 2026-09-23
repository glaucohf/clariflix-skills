# Task: Discover Tools Recommend (Extension Wrapper)

**Task ID:** discover-tools-recommend
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega recomendação e priorização ao owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task base

---

## Purpose

Este wrapper preserva o contexto do `pro`, mas a lógica real de priorização continua sendo herdada do base.

O owner canônico permanece em:

- `squads/squad-creator/tasks/discover-tools-recommend.md`

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `evaluated_tools` | list | Yes | Ferramentas avaliadas |
| `scan_output` | object | Yes | Baseline de gaps e cobertura |
| `domain` | string | Yes | Domínio alvo |

---

## Workflow

### Step 1: Delegate to Base Recommendation Task

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/discover-tools-recommend.md"
  payload:
    - evaluated_tools
    - scan_output
    - domain
  prohibition:
    - "Do NOT keep a second impact-vs-effort matrix in squad-creator-pro"
```

### Step 2: Reconcile Outputs

```yaml
reconcile_outputs:
  primary_output: ".aiox/squad-runtime/discovery/{domain}/recommendations.yaml"
  return_shape:
    delegated_task: "squads/squad-creator/tasks/discover-tools-recommend.md"
    recommendations: ".aiox/squad-runtime/discovery/{domain}/recommendations.yaml"
```

---

## Output

```yaml
output:
  name: delegated_discover_tools_recommend
  format: yaml
  structure:
    delegated_task: "squads/squad-creator/tasks/discover-tools-recommend.md"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] A recomendação continua sendo determinada pelo owner canônico do base
- [ ] O workflow do pro passa a ter owner atômico explícito na fase decisória
- [ ] Nenhuma matriz paralela de decisão permanece neste wrapper

---

## Related Documents

- `squads/squad-creator/tasks/discover-tools-recommend.md` -- owner canônico
- `workflows/wf-discover-tools.yaml` -- consumidor local no pro

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed discover-tools-recommend output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified
