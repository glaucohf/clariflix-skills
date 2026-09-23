# Task: Validate Clone (Stub)

**Command:** `*validate-clone`
**Execution Type:** Hybrid (Worker script 90% + Agent hackability test 10%)
**Worker Script:** `scripts/validate-clone.sh`
**Model:** `Haiku` (QUALIFIED -- script handles fidelity + authenticity, LLM only for hackability)
**Haiku Eligible:** YES
**Load:** `data/an-clone-validation.yaml` + `data/an-output-examples.yaml`

## Purpose

Validar qualidade de um clone existente usando fidelity score, hackability test e authenticity markers.

---

## MANDATORY PREFLIGHT: Run Worker Script FIRST

```
EXECUTE FIRST -- before ANY manual validation:

  bash squads/squad-creator-pro/scripts/validate-clone.sh <clone-path> > /tmp/preflight-validate-clone.yaml

IF the command fails -> FIX the script error. Do NOT proceed manually.
IF the command succeeds -> READ /tmp/preflight-validate-clone.yaml. Use ONLY these scores.

VETO: If /tmp/preflight-validate-clone.yaml does not exist -> BLOCK.
      Your job is HACKABILITY ONLY -- run the 4 interactive tests.
```

## Checklist Reference

Before marking this task complete, verify against: `checklists/mind-validation.md`

---

## SCORING CALIBRATION (CRITICAL)

```yaml
scoring_philosophy:
  principle: "SCORE O QUE EXISTE, nao o que falta"
  bias_correction: "Haiku tende a sub-pontuar. Compensar sendo generoso."
  evidence_rule: "Se existe evidencia, conta ponto. Gaps vao para recommendations."
```

---

## Sub-Tasks (Atomic Execution)

| # | Sub-Task | File | Responsibility |
|---|----------|------|----------------|
| 1 | Fidelity Score | `an-validate-clone-fidelity.md` | 8 layers x 5 checkpoints = 40 total, observable/deep weighting |
| 2 | Hackability + Authenticity | `an-validate-clone-hackability.md` | 4 binary hack tests + 10 authenticity markers |
| 3 | Verdict + Report | `an-validate-clone-verdict.md` | Deterministic decision tree + final report generation |

---

## Execution Flow

```
Step 1: an-validate-clone-fidelity
  Input: clone file + preflight YAML
  Output: fidelity_percent (0-100), layer breakdown

Step 2: an-validate-clone-hackability
  Input: clone file (interactive tests)
  Output: hackability_score (0-4), authenticity_score (0-10)

Step 3: an-validate-clone-verdict
  Input: fidelity_percent + hackability_score + authenticity_score
  Output: validation_report YAML with PASS|REVIEW|FAIL verdict
```

---

## Completion Criteria

- [ ] Fidelity score calculated (an-fidelity-score v2.0 methodology)
- [ ] Hackability test executed (4 binary tests)
- [ ] Authenticity markers verified (10 checkpoints)
- [ ] Final verdict determined by decision tree
- [ ] Report generated with evidence for each checkpoint

---

_Task Version: 2.0.0_
_Atomized: 2026-03-26_
_Sub-tasks: an-validate-clone-fidelity, an-validate-clone-hackability, an-validate-clone-verdict_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Task-specific context and prior pipeline outputs
- **Outputs:** Completed an-validate-clone output artifact
- **Completion Criteria:** All items in Quality Check/Completion Criteria above are satisfied
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] Fidelity score calculated (an-fidelity-score v2.0 methodology)
- [ ] Hackability test executed (4 binary tests)
- [ ] Authenticity markers verified (10 checkpoints)
- [ ] Final verdict determined by decision tree
- [ ] Report generated with evidence for each checkpoint
