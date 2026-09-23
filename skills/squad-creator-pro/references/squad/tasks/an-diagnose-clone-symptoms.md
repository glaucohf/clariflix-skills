# Task: Diagnose Clone -- Symptoms + Root Cause

**Task ID:** an-diagnose-clone-symptoms
**Parent Task:** `an-diagnose-clone.md`
**Purpose:** Identify clone symptoms and map to root causes using deterministic lookup table
**Execution Type:** Agent
**Model:** Sonnet
**Haiku Eligible:** NO
**Load:** `data/an-clone-anti-patterns.yaml`

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Diagnose Clone -- Symptoms + Root Cause |
| **status** | `active` |
| **responsible_executor** | @squad-chief |
| **execution_type** | Agent |
| **input** | User description of clone problems |
| **output** | Symptoms list + root causes from lookup table |
| **action_items** | 2 steps |
| **acceptance_criteria** | All symptoms mapped to causes via table, no inference |

---

## Workflow

### Step 1: Identify Symptoms

Ask the user: "O que esta errado com o clone?"

Common symptoms:

- "Responde generico" -> probably missing Framework
- "Nao parece a pessoa" -> bronze sources or no Voice DNA
- "Se perde em conversas longas" -> monolithic prompt, needs stages
- "Quebra facil" -> no veto conditions, weak immune system
- "Inventa coisas" -> no Swipe File, no limits
- "Muito robotico" -> no productive contradictions, no storytelling

### Step 2: Map to Root Cause (BINARY -- Use Table Only)

```yaml
checkpoint_root_cause:
  rule: "SE sintoma esta na tabela abaixo -> usar causa da tabela"
  NO_INFERENCE: "Nao inventar causas fora da tabela"
  validation: "Causa DEVE estar na coluna 'Causa Raiz Provavel'"
```

Use `an-clone-anti-patterns.yaml` to diagnose:

| Sintoma | Causa Raiz Provavel | Anti-pattern |
|---------|---------------------|-------------|
| Generico | Falta Framework | So Playbook, sem SE/ENTAO |
| Nao parece pessoa | Fontes bronze | Volume sem curadoria |
| Se perde | Prompt monolitico | Sem estagios |
| Quebra facil | Sem immune system | Sem veto conditions |
| Inventa | Sem Swipe File | Sem exemplos reais |
| Robotico | Sem paradoxos | Contradictions resolvidas |

---

## Output Contract

```yaml
symptom_diagnosis:
  clone: "{name}"
  symptoms:
    - symptom: "{description}"
      root_cause: "{from lookup table}"
      anti_pattern: "{from lookup table}"
  unmapped_symptoms: []  # symptoms not in lookup table
```

---

## Completion Criteria

- [ ] All reported symptoms documented
- [ ] Each symptom mapped to root cause via lookup table
- [ ] No causes invented outside the table
- [ ] Unmapped symptoms flagged separately

---

## Handoff

| Attribute | Value |
|-----------|-------|
| **Next Task** | `an-diagnose-clone-verify-trinity.md` |
| **Trigger** | Symptoms mapped |
| **Artifact** | `symptom_diagnosis` YAML |

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of an-diagnose-clone.md_

## Acceptance Criteria

- [ ] All symptoms mapped to causes via table
- [ ] no inference
