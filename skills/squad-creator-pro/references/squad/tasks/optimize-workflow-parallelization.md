# Task: Optimize Workflow - Parallelization

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `optimize-workflow-parallelization` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Agent` |

## Metadata

```yaml
id: optimize-workflow-parallelization
name: "Optimize Workflow Parallelization"
category: optimization
agent: squad-chief
elicit: false
autonomous: true
description: "Constrói o grafo de dependências e identifica grupos de fases paralelizáveis sem colidir em recurso ou output."
```

## Purpose

Executar a dimensão D2. Esta task procura economia de tempo sem quebrar dependências reais do workflow.

## Inputs

```yaml
inputs:
  phase_necessity_table:
    type: object
    required: true
```

## Workflow / Steps

### Step 1: Construir o grafo

- Mapear `depends_on`, `produces` e `consumes` por fase.

### Step 2: Encontrar oportunidades

- Sinalizar fases independentes.
- Excluir grupos que competem pelo mesmo agente/recurso.

## Output

```yaml
output:
  schema:
    dependency_graph: []
    parallel_groups: []
    estimated_time_savings: []
```

## Acceptance Criteria

- [ ] Toda recomendação de paralelização vem com justificativa de dependência
- [ ] Grupos conflitantes ficam explicitamente excluídos

## Related Documents

- `optimize-workflow.md`
- `optimize-workflow-checkpoints.md`
