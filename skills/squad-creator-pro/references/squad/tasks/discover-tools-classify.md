# Task: Discover Tools Classify (Extension Wrapper)

**Task ID:** discover-tools-classify
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a classificação de candidatos ao owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task base

---

## Purpose

Este wrapper existe para permitir que o workflow do pro explicite `task_ref` na fase de busca/classificação sem manter uma segunda implementação da lógica.

O owner canônico permanece em:

- `squads/squad-creator/tasks/discover-tools-classify.md`

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `scan_output` | object | Yes | Saída da fase de scan |
| `domain` | string | Yes | Domínio ou squad alvo |
| `use_cases` | list | Yes | Casos de uso principais |
| `budget_tier` | enum | No | Faixa de custo alvo |

---

## Workflow

### Step 1: Preserve Pro Scope

```yaml
overlay_scope:
  rules:
    - "Honor external-only gaps produced by the pro scan step"
    - "Keep pro-local exclusions and internal-first decisions"
```

### Step 2: Delegate to Base Classification Task

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/discover-tools-classify.md"
  payload:
    - scan_output
    - domain
    - use_cases
    - budget_tier
  prohibition:
    - "Do NOT fork classification logic in squad-creator-pro"
```

### Step 3: Reconcile Outputs

```yaml
reconcile_outputs:
  primary_output: ".aiox/squad-runtime/discovery/{domain}/classified-tools.yaml"
  return_shape:
    delegated_task: "squads/squad-creator/tasks/discover-tools-classify.md"
    classified_tools: ".aiox/squad-runtime/discovery/{domain}/classified-tools.yaml"
```

---

## Output

```yaml
output:
  name: delegated_discover_tools_classify
  format: yaml
  structure:
    delegated_task: "squads/squad-creator/tasks/discover-tools-classify.md"
    domain: "{domain}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] A classificação real ocorre no owner canônico do base
- [ ] O workflow do pro passa a ter owner atômico explícito
- [ ] Nenhuma lógica paralela de classificação permanece aqui

---

## Related Documents

- `squads/squad-creator/tasks/discover-tools-classify.md` -- owner canônico
- `workflows/wf-discover-tools.yaml` -- consumidor local no pro

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed discover-tools-classify output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified
