# Task: Diagnose Clone (Stub)

**Command:** `*diagnose-clone`
**Execution Type:** Hybrid
**Model:** Sonnet
**Haiku Eligible:** NO
**Load:** `data/an-clone-anti-patterns.yaml`

## Purpose

Diagnosticar por que um clone esta fraco, mapeando sintomas para causas raiz e prescrevendo tratamento.

---

## CHECKPOINT CLARIFICATIONS (Haiku Compatibility)

```yaml
checkpoint_conversions:
  root_cause_real:
    OLD: "Mapeei a CAUSA RAIZ real ou so o sintoma?"
    NEW: "SE sintoma esta na tabela Sintoma->Causa -> causa raiz = valor da tabela"
    rule: "Usar SEMPRE a tabela de lookup. Nao inferir causas fora da tabela."

  transformacao_profunda:
    OLD: "Tratamento gera transformacao PROFUNDA?"
    NEW: "SE causa esta na tabela Causa->Tratamento -> tratamento = valor da tabela"
    rule: "Usar SEMPRE a tabela de lookup. Nao inventar tratamentos."

  diagnostico_claro:
    OLD: "Diagnostico tem causa raiz CLARA e tratamento ACIONAVEL?"
    NEW: "SE report YAML tem todos campos preenchidos (non-empty) -> CLARO"
    rule: "Verificar presenca de campos, nao julgar qualidade do conteudo."
```

---

## Sub-Tasks (Atomic Execution)

| # | Sub-Task | File | Responsibility |
|---|----------|------|----------------|
| 1 | Symptoms + Root Cause | `an-diagnose-clone-symptoms.md` | Identify symptoms, map to root causes using lookup table |
| 2 | Verify Trinity | `an-diagnose-clone-verify-trinity.md` | Binary trinity check + source quality + fidelity calculation |
| 3 | Prescribe + Report | `an-diagnose-clone-prescribe.md` | Prescribe treatment from lookup table, generate diagnosis report |

---

## Execution Flow

```
Step 1: an-diagnose-clone-symptoms
  Input: user description of clone problems
  Output: symptoms list + root causes (from lookup table)

Step 2: an-diagnose-clone-verify-trinity
  Input: clone file path
  Output: trinity status + source quality + fidelity score

Step 3: an-diagnose-clone-prescribe
  Input: root causes + trinity/fidelity data
  Output: treatment plan + diagnosis_report YAML
```

---

## Completion Criteria

- [ ] Sintomas identificados
- [ ] Causas raiz mapeadas
- [ ] Trindade verificada
- [ ] Tratamento prescrito com prioridades
- [ ] Report de diagnostico gerado

---

_Task Version: 2.0.0_
_Atomized: 2026-03-26_
_Sub-tasks: an-diagnose-clone-symptoms, an-diagnose-clone-verify-trinity, an-diagnose-clone-prescribe_

## Task Anatomy

- **Executor:** Agent
- **Inputs:** Task-specific context and prior pipeline outputs
- **Outputs:** Completed an-diagnose-clone output artifact
- **Completion Criteria:** All items in Quality Check/Completion Criteria above are satisfied
- **Guardrails:** None identified

## Acceptance Criteria

- [ ] Sintomas identificados
- [ ] Causas rai
