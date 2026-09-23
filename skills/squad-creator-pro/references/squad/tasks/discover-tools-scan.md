# Task: Discover Tools Scan (Extension Wrapper)

**Task ID:** discover-tools-scan
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a varredura estrutural de discovery ao owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task base

---

## Purpose

Este wrapper existe para manter o pipeline `wf-discover-tools.yaml` do `squad-creator-pro` alinhado ao modelo atômico do base sem duplicar a metodologia.

O owner canônico permanece em:

- `squads/squad-creator/tasks/discover-tools-scan.md`

O papel desta task é apenas:

1. preservar o contexto de overlay do pro;
2. repassar os inputs canônicos de domínio e casos de uso;
3. garantir que os artefatos locais do pack entrem na análise;
4. devolver o resultado no formato esperado pelo workflow do pro.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `domain` | string | Yes | Domínio ou squad alvo |
| `use_cases` | list | Yes | Casos de uso principais |
| `existing_tools` | list | No | Ferramentas já conhecidas |
| `capability_gaps` | list | No | Gaps já percebidos |
| `scope_hint` | string | No | Clarificação para domínio ambíguo |

---

## Preconditions

- [ ] `squads/squad-creator/tasks/discover-tools-scan.md` existe
- [ ] `data/internal-infrastructure-library.yaml` existe no `squad-creator-pro`
- [ ] O chamador entende que este wrapper não mantém lógica paralela local

---

## Workflow

### Step 1: Preserve Pro Overlay Context

```yaml
overlay_context:
  artifacts:
    - "data/internal-infrastructure-library.yaml"
    - "data/tool-registry.yaml"
  rule:
    - "Preserve pro-local infrastructure hints and tool memory"
```

### Step 2: Delegate to Base Scan Task

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/discover-tools-scan.md"
  payload:
    - domain
    - use_cases
    - existing_tools
    - capability_gaps
    - scope_hint
  overlay_inputs:
    - internal_infrastructure_library: "data/internal-infrastructure-library.yaml"
    - tool_registry: "data/tool-registry.yaml"
  prohibition:
    - "Do NOT reimplement scan logic inside squad-creator-pro"
```

### Step 3: Reconcile Outputs

```yaml
reconcile_outputs:
  primary_output: ".aiox/squad-runtime/discovery/{domain}/scan-results.yaml"
  return_shape:
    delegated_task: "squads/squad-creator/tasks/discover-tools-scan.md"
    execution_mode: "base-delegated-with-pro-overlay"
    scan_output: ".aiox/squad-runtime/discovery/{domain}/scan-results.yaml"
```

---

## Output

```yaml
output:
  name: delegated_discover_tools_scan
  format: yaml
  structure:
    delegated_task: "squads/squad-creator/tasks/discover-tools-scan.md"
    domain: "{domain}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] O `pro` não mantém uma segunda implementação da fase de scan
- [ ] O workflow local consegue referenciar um owner atômico explícito
- [ ] Os artefatos locais do pack continuam entrando na análise

---

## Related Documents

- `squads/squad-creator/tasks/discover-tools-scan.md` -- owner canônico
- `workflows/wf-discover-tools.yaml` -- consumidor local no pro

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed discover-tools-scan output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified
