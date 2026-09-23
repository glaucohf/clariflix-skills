# Task: Validate Squad - Security

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-security` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Worker` |

## Metadata

```yaml
id: validate-squad-security
name: "Validate Squad Security"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Executa o scan bloqueante de segredos, credenciais e padroes inseguros no squad."
```

## Purpose

Isolar o scan de seguranca como gate proprio, para que qualquer exposicao de segredos ou credenciais interrompa a validacao imediatamente e com evidencias claras.

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
```

## Workflow / Steps

### Step 1: Procurar segredos bloqueantes

- API keys e tokens.
- Senhas e segredos hardcoded.
- Credenciais cloud e chaves privadas.
- URLs de banco com credenciais.
- Arquivos `.env`, `credentials*.json`, `service-account*.json`.

### Step 2: Marcar warnings nao bloqueantes

- Uso de `eval`/`exec`.
- Artefatos sensiveis que exijam revisao manual.

### Step 3: Produzir resultado do gate

- Qualquer achado critico => `ABORT`.
- Warnings nao bloqueiam, mas entram no relatorio final.

## Output

```yaml
output:
  schema:
    status: "PASS | ABORT"
    critical_count: N
    warning_count: N
    critical_findings: []
    warnings: []
```

## Acceptance Criteria

- [ ] Achados criticos bloqueiam a validacao
- [ ] Warnings sao preservados para o relatorio final
- [ ] O output separa claramente `critical_findings` de `warnings`

## Related Documents

- `validate-squad.md`
- `checklists/quality-gate-checklist.md`
