---
task-id: an-fidelity-score
name: "Fidelity Score"
version: 3.0.0
execution_type: Orchestrator
model: Haiku
model_rationale: "Orchestrator stub -- delegates to 3 atomic sub-tasks. 95% deterministic via worker script."
haiku_eligible: true
note: "Decomposed from v2.0.0 monolith (340 lines, 8 layers) into 3 atomic tasks."
estimated-time: 15-20 min
complexity: medium

inputs:
  required:
    - clone_path: "Path to the clone agent file"

outputs:
  primary:
    - fidelity_report: "Complete fidelity report with scores, classification, and gaps"

worker_script: "scripts/fidelity-score.sh"
load: "data/an-clone-validation.yaml"
elicit: false
---

# Fidelity Score

**Command:** `*fidelity-score`

> **MANDATORY PREFLIGHT:** Run worker script FIRST. Do NOT score manually.

---

## Pipeline (3 Atomic Tasks)

| Phase | Task ID | Name | Est. Time |
|-------|---------|------|-----------|
| 1 | `an-fidelity-score-identify` | Identify Clone Files & Run Script | 5 min |
| 2 | `an-fidelity-score-layers` | Execute 8 Layer Checklists | 5 min |
| 3 | `an-fidelity-score-calculate` | Calculate Score, Classify & Report | 5 min |

---

## Execution Flow

```
an-fidelity-score-identify
  | clone_files, preflight_scores
  v
an-fidelity-score-layers
  | layer_scores (8 layers x 5 checkpoints each)
  v
an-fidelity-score-calculate
  | fidelity_report (FINAL OUTPUT)
  v
[DONE]
```

---

## Worker Script (MANDATORY PREFLIGHT)

```bash
bash squads/squad-creator-pro/scripts/fidelity-score.sh <clone-path> > /tmp/preflight-fidelity-score.yaml
```

**VETO:** If preflight file does not exist, BLOCK. Do NOT score manually.

---

## Scoring Calibration

```yaml
scoring_philosophy:
  principle: "SCORE O QUE EXISTE, nao o que falta"
  bias_correction: "Haiku tende a sub-pontuar. Compensar sendo generoso."
  evidence_rule: "Se existe evidencia, conta ponto. Gaps vao para recommendations."
```

---

## Checklist Reference

Before marking complete, verify against: `checklists/mind-validation.md`

---

## Completion Criteria

- [ ] 8 layers avaliados com checklists binarios
- [ ] Cada checkpoint marcado PASS ou FAIL com evidencia
- [ ] Score ponderado calculado com formula
- [ ] Classificacao atribuida deterministicamente
- [ ] Gaps listados com acao especifica
- [ ] Report YAML gerado no formato especificado

## Task Anatomy

> **Skill:** This task is also available as a skill: `fidelity-score` -- invoke directly for standalone scoring with accountability contract.

- **Executor:** Agent
- **Inputs:** clone_path
- **Outputs:** Complete fidelity report with scores, classification, and gaps
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] Output artifact produced: Complete fidelity report with scores, classification, and gaps
- [ ] Task output validated against quality standards
