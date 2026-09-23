# Task: Upgrade Squad - Plan

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `upgrade-squad-plan` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: upgrade-squad-plan
name: "Upgrade Squad Plan"
category: upgrade
agent: squad-chief
elicit: true
autonomous: false
description: "Compõe o plano herdado do base com uma segunda trilha qualitativa, sem misturar automação segura com conteúdo que depende de evidência."
```

## Purpose

Transformar o gap report em um plano de duas trilhas:
- `structural_auto_track`: upgrades seguros herdados do base
- `qualitative_track`: upgrades que exigem contexto, evidência, pesquisa ou TODO explícito

## Workflow / Steps

### Step 1: Gerar o plano estrutural herdado

- Ler `squads/squad-creator/tasks/upgrade-squad-plan.md`.
- Produzir as fases estruturais, esforço e escopo aprovável no padrão do base.

### Step 2: Anexar a trilha qualitativa

- Para cada gap qualitativo, definir um destes destinos:
  - `apply_now` quando houver evidência suficiente
  - `delegate_research` para `extract-voice-dna`, `extract-thinking-dna` ou task equivalente
  - `mark_todo` quando a automação seria inventiva demais

## Output

```yaml
output:
  schema:
    structural_auto_track: {}
    qualitative_track:
      apply_now: []
      delegate_research: []
      mark_todo: []
```

## Acceptance Criteria

- [ ] O plano estrutural continua alinhado ao base
- [ ] A trilha qualitativa não aprova invenção silenciosa
- [ ] Em `auto`, itens ambíguos caem em `delegate_research` ou `mark_todo`

## Related Documents

- `squads/squad-creator/tasks/upgrade-squad-plan.md`
- `upgrade-squad-qualitative.md`
