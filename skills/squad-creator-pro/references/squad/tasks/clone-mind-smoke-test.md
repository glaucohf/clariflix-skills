# Task: Clone Mind Smoke Test

**Task ID:** clone-mind-smoke-test
**Version:** 1.0.0
**Purpose:** Executar smoke tests comportamentais do clone recém-sintetizado para validar aderência ao expert original
**Orchestrator:** @oalanicolas
**Mode:** Validation

---

## Purpose

Esta task existe para a fase `smoke-tests` de `wf-clone-mind.yaml`.

Ela NÃO valida roteamento de modelo. O objetivo aqui é testar o comportamento do clone em cenários reais do domínio.

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `clone_bundle` | file/object | Yes | Bundle consolidado do clone |
| `agent_block` | file/object | Yes | Agent block gerado na fase de síntese |
| `mind_name` | string | Yes | Nome da mente clonada |
| `domain` | string | Yes | Domínio da mente |

---

## Workflow

### Step 1: Load Smoke Checklist

Usar:

- `squads/squad-creator/checklists/smoke-test-agent.md`

### Step 2: Run 3 Behavioral Tests

Executar os três testes definidos no workflow:

1. conhecimento do domínio;
2. tomada de decisão;
3. resposta a objeção.

### Step 3: Record Evidence

Gerar evidência por teste com:

- prompt usado;
- saída observada;
- checks que passaram/falharam;
- decisão final PASS ou FAIL.

---

## Output

```yaml
output:
  primary:
    - smoke_test_result
  artifacts:
    - smoke_test_result.yaml
```

---

## Acceptance Criteria

- [ ] A task valida comportamento do clone, não routing técnico
- [ ] Os 3 testes do workflow são executados
- [ ] O output final registra evidência verificável por teste

---

## Related Documents

- `workflows/wf-clone-mind.yaml` -- fase consumidora
- `squads/squad-creator/checklists/smoke-test-agent.md` -- checklist canônico

---

_Task Version: 1.0.0_
_Role: behavioral smoke-test contract for clone-mind workflow_

## Task Anatomy

- **Executor:** Worker
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed clone-mind-smoke-test output artifact
- **Completion Criteria:** All outputs produced and validated
- **Guardrails:** Execution halts on quality gate failure
