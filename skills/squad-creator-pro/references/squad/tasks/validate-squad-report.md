# Task: Validate Squad - Report

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-report` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-report
name: "Validate Squad Report"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Calcula o score final, consolida os outputs das subtasks e emite relatorio humano + payload estruturado."
```

## Purpose

Consolidar o resultado final da validacao em formatos consumiveis por humano e maquina, preservando compatibilidade retroativa do comando `*validate-squad`.

## Inputs

```yaml
inputs:
  squad_name:
    type: string
    required: true
  squad_path:
    type: string
    required: false
    default: "squads/{squad_name}/"
  detected_type:
    type: string
    required: true
  quality_result:
    type: object
    required: true
  contextual_result:
    type: object
    required: true
  veto_result:
    type: object
    required: true
```

## Workflow / Steps

### Step 1: Calcular score final

- Se houver veto, resultado final = `FAIL`.
- Sem veto, aplicar peso principal em qualidade e peso secundario em contextual.

### Step 2: Montar payload estruturado

- `final_score`
- `result`
- `tier_results`
- `issues_by_priority`
- `recommendations`

### Step 3: Emitir relatorio humano

- Escrever `validation-report-{date}.md` em `docs/`.
- Escrever payload `.json` equivalente para automacao.

## Output

```yaml
output:
  files:
    report: "{squad_path}/docs/validation-report-{date}.md"
    json: "{squad_path}/docs/validation-report-{date}.json"
  schema:
    final_score: 0.0
    result: "PASS | CONDITIONAL | FAIL"
    detected_type: "expert | pipeline | hybrid"
```

## Acceptance Criteria

- [ ] O score final e consistente com qualidade, contextual e vetos
- [ ] O report humano e o payload estruturado sao emitidos
- [ ] O formato final continua compativel com o uso atual do comando

## Related Documents

- `validate-squad.md`
- `validate-squad-quality.md`
- `validate-squad-contextual.md`
- `validate-squad-veto.md`
