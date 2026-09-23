# Task: Create From SOP -- Brief

**Task ID:** create-from-sop-brief
**Parent Task:** `create-from-sop.md`
**Purpose:** Generate creation brief assembling all artifacts from prior sub-tasks
**Execution Type:** Agent
**Model:** `Opus`
**Haiku Eligible:** NO

---

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Create From SOP -- Brief |
| **status** | `active` |
| **responsible_executor** | @pedro-valerio |
| **execution_type** | Agent |
| **input** | `source_classification` + `process_mapping` from prior sub-tasks |
| **output** | `squad_creation_brief` + `output_contract` YAML |
| **action_items** | 1 step |
| **acceptance_criteria** | Brief complete with all sections, gaps not invented |

---

## Workflow

### Step 5: Creation Brief

Assemble `squad_creation_brief` with:

- Objetivo do squad
- Fontes usadas como SSOT
- Processos executaveis mapeados
- Contexto de suporte incorporado
- Guardrails obrigatorios
- Gaps que impedem automacao completa

---

## Output Contract

```yaml
create_from_sop:
  business_slug: "{slug}"
  selectors:
    namespaces: []
    explicit_paths: []
  source_package:
    runtime_mode: full_workspace_mode
    source_of_truth: workspace_canonical
    loaded_sources: []
    missing_requested_sources: []
  creation_brief:
    objective: "{squad objective derived from SOPs}"
    canonical_sources:
      - path: "{path}"
        class: "executable_process|supporting_context|governance_signal"
    executable_processes:
      - task_name: "{name}"
        executor: "Human|Agent|Hybrid|Worker"
        inputs: []
        outputs: []
        guardrails: []
    supporting_context:
      - path: "{path}"
        provides: "{what context}"
    guardrails:
      - source: "{governance signal path}"
        rule: "{derived guardrail}"
    open_questions:
      - type: "MISSING|AMBIGUOUS|CONFLICT"
        description: "{what is unclear}"
        impact: "{what it blocks}"
```

---

## Completion Criteria

- [ ] Squad objective clearly defined from SOP evidence
- [ ] All canonical sources listed with classification
- [ ] Executable processes have executor + guardrails
- [ ] Supporting context separated from processes
- [ ] Gaps marked without invention
- [ ] Output contract fully populated

---

_Task Version: 1.0.0_
_Pattern: Atomic sub-task of create-from-sop.md_

## Acceptance Criteria

- [ ] Brief complete with all sections
- [ ] gaps not invented
