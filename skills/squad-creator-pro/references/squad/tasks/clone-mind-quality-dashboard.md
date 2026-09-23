# Task: Clone Mind Quality Dashboard

**Task ID:** clone-mind-quality-dashboard
**Version:** 1.0.0
**Purpose:** Gerar dashboard de qualidade específico de clone a partir de fontes, DNA extraído e resultado do smoke test
**Orchestrator:** @oalanicolas
**Mode:** Reporting

---

## Purpose

Esta task existe para a fase `quality-dashboard-generation` de `wf-clone-mind.yaml`.

Ela NÃO usa analytics genérico de squad. O objetivo é consolidar métricas específicas do clone:

- quantidade e qualidade de fontes;
- cobertura de Voice DNA;
- cobertura de Thinking DNA;
- resultado do smoke test;
- `fidelity_estimate`.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `sources_inventory` | file/object | Yes | Inventário de fontes |
| `voice_dna` | file/object | Yes | Artefato final de Voice DNA |
| `thinking_dna` | file/object | Yes | Artefato final de Thinking DNA |
| `smoke_test_result` | file/object | Yes | Resultado do smoke test comportamental |
| `fidelity_estimate` | number/string | No | Estimativa consolidada de fidelidade |

---

## Workflow

### Step 1: Aggregate Clone Metrics

Calcular e consolidar:

- `sources_count`
- `tier_1_ratio`
- `voice_score`
- `thinking_score`
- `smoke_test_result`
- `fidelity_estimate`

### Step 2: Render Dashboard

Gerar dashboard usando:

- `squads/squad-creator/templates/quality-dashboard-tmpl.md`

### Step 3: Produce Recommendations

Listar gaps prioritários e próximas ações para elevar fidelidade e robustez do clone.

---

## Output

```yaml
output:
  primary:
    - quality_dashboard
  artifacts:
    - quality_dashboard.md
```

---

## Acceptance Criteria

- [ ] O dashboard é específico de clone, não analytics genérico de squad
- [ ] As métricas do workflow são refletidas explicitamente no output
- [ ] O artefato final lista gaps e recommendations acionáveis

---

## Related Documents

- `workflows/wf-clone-mind.yaml` -- fase consumidora
- `squads/squad-creator/templates/quality-dashboard-tmpl.md` -- template canônico

---

_Task Version: 1.0.0_
_Role: clone-specific quality dashboard contract_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed clone-mind-quality-dashboard output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** None identified
