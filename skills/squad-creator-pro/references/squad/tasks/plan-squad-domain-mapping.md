# Task: Plan Squad Domain Mapping

**Task ID:** plan-squad-domain-mapping
**Execution Type:** Agent
**Purpose:** mapear problema, usuários, capacidades e workflows antes de desenhar arquitetura

## Inputs

- `planning_contract`
- `depth_rules`

## Steps

1. Identificar `current_pain`, `desired_outcomes` e `opportunity_cost`.
2. Listar usuários primários e secundários.
3. Mapear capabilities com outputs e por que existem.
4. Mapear workflows com categoria, complexidade, automação e dependências.
5. Emitir `capability_map`, `workflow_inventory` e `risk_inputs`.

## Output

```yaml
domain_map:
  problem: {}
  users: {}
  capabilities: []
  workflows: []
```

## Veto

- roadmap sem capability/workflow inventory
