# Task: Create Squad Template (Extension Wrapper)

**Task ID:** create-template
**Version:** 3.0.0
**Purpose:** Preservar compatibilidade do `squad-creator-pro` enquanto delega a criação real de templates ao owner canônico no `squad-creator`
**Orchestrator:** @squad-chief
**Mode:** Delegation-first
**Quality Standard:** Herdado da task base

---

## Purpose

Este wrapper existe para manter compatibilidade com chamadas do `squad-creator-pro` que ainda usam `create-template`.

O `squad-creator-pro` não deve manter uma segunda implementação completa de criação de templates quando o comportamento é o mesmo do base. O owner canônico permanece em:

- `squads/squad-creator/tasks/create-template.md`

O papel desta task é apenas:

1. normalizar inputs legados do pro;
2. reconciliar `pack_name` com `squad_name`;
3. encaminhar a execução para a task base;
4. devolver o resultado no formato esperado pelos chamadores do pro.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `template_name` | string | Yes | Nome humano do template |
| `template_id` | string | Yes | Identificador em kebab-case |
| `squad_name` | string | No | Nome canônico do squad alvo |
| `pack_name` | string | No | Alias legado do pro; deve virar `squad_name` |
| `output_format` | enum | Yes | `md`, `yaml`, `json`, `html` |
| `source_artifacts` | list | No | Artefatos que ajudem a detalhar placeholders e estrutura |

---

## Preconditions

- [ ] `squads/squad-creator/tasks/create-template.md` existe
- [ ] O squad alvo existe em `squads/{squad_name}/` ou `squads/{pack_name}/`
- [ ] O chamador entende que este wrapper não define pipeline próprio

---

## Workflow

### Step 1: Normalize Target Squad

```yaml
normalize_target:
  rules:
    - if: "squad_name is empty AND pack_name exists"
      then: "set squad_name = pack_name"
    - if: "both squad_name and pack_name exist AND differ"
      then: "block and reconcile target"
```

### Step 2: Delegate to Base Task

```yaml
delegate_to_base:
  task: "squads/squad-creator/tasks/create-template.md"
  payload:
    - template_name
    - template_id
    - squad_name
    - output_format
    - source_artifacts
  prohibition:
    - "Do NOT maintain a parallel template-creation methodology in squad-creator-pro"
```

### Step 3: Reconcile Outputs

```yaml
reconcile_outputs:
  primary_output: "squads/{squad_name}/templates/{template_id}-tmpl.{ext}"
  return_shape:
    template_file: "path to created template"
    delegated_task: "squads/squad-creator/tasks/create-template.md"
    execution_mode: "base-delegated"
```

---

## Output

```yaml
output:
  name: delegated_template_creation
  format: yaml
  structure:
    template_file: "squads/{squad_name}/templates/{template_id}-tmpl.{ext}"
    delegated_task: "squads/squad-creator/tasks/create-template.md"
    normalized_squad_name: "{squad_name}"
    status: "delegated"
```

---

## Acceptance Criteria

- [ ] `pack_name` e `squad_name` são reconciliados corretamente
- [ ] A criação real do template é delegada ao base
- [ ] Nenhuma implementação paralela de create-template permanece no pro
- [ ] Chamadas existentes do pro continuam compatíveis

---

## Veto Conditions

- `squad_name` e `pack_name` apontarem para squads diferentes
- A task base `create-template.md` não existir
- O `pro` tentar manter regras locais incompatíveis com o base

---

## Related Documents

- `squads/squad-creator/tasks/create-template.md` -- owner canônico

---

_Task Version: 3.0.0_
_Role: compatibility wrapper for upgrade-pack delegation_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed create-template output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above
