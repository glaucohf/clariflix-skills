# Task: Validate Squad — Governance Framework Compliance

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `validate-squad-compliance` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `Hybrid` |

## Metadata

```yaml
id: validate-squad-compliance
name: "Validate Squad Governance Framework Compliance"
category: validation
agent: squad-chief
elicit: false
autonomous: true
description: "Check governance framework compliance: artifact_contracts, bu_mapping, supported_modes, lifecycle states, and local token contract."
```

## Purpose

Validate that a squad conforms to governance framework extension requirements. This is a standalone compliance check that can run independently or as part of the full validation pipeline. It verifies artifact contracts, BU mapping, supported modes, and lifecycle state declarations.

## Prerequisites

- [ ] Squad `config.yaml` exists and is valid YAML
- [ ] Composition rules accessible

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
  config:
    type: file
    required: true
    path: "{squad_path}/config.yaml"
```

## Workflow / Steps

### Step 1: Check artifact_contracts (REQUIRED)

Every squad MUST declare the artifacts it produces.

```yaml
artifact_contracts_check:
  id: "FW-AC-001"
  severity: BLOCKING
  check: "config.yaml contains artifact_contracts[] array"
  validation:
    - "artifact_contracts[] exists and is non-empty"
    - "Each contract has: artifact_id, template_path, lifecycle_states"
    - "template_path references a file that exists in templates/"
    - "lifecycle_states is a valid subset of [draft, validated, approved, superseded, archived]"
  on_fail: "BLOCK - artifact_contracts missing or malformed"
```

### Step 2: Check bu_mapping (RECOMMENDED)

```yaml
bu_mapping_check:
  id: "FW-BU-001"
  severity: WARNING
  check: "config.yaml contains bu_mapping field"
  validation:
    - "bu_mapping references a valid BU from bu-map.yaml"
    - "Referenced BU exists in workspace or data layer"
  on_missing: "WARNING - bu_mapping not declared (recommended)"
```

### Step 3: Check supported_modes (RECOMMENDED)

```yaml
supported_modes_check:
  id: "FW-SM-001"
  severity: WARNING
  check: "config.yaml contains supported_modes[] array"
  validation:
    - "Each mode is one of: CRIAR, RESOLVER, GERENCIAR, ENTENDER, VALIDAR, CONFIGURAR, PLANEJAR, EXPLORAR"
    - "At least 1 mode declared"
    - "Declared modes align with squad capabilities"
  on_missing: "WARNING - supported_modes not declared (recommended)"
```

### Step 4: Check Lifecycle State Coverage

```yaml
lifecycle_check:
  id: "FW-LC-001"
  severity: WARNING
  check: "Artifact lifecycle states are properly managed"
  validation:
    - "Templates referenced in artifact_contracts exist"
    - "Templates contain lifecycle state transitions"
    - "Tasks that produce artifacts reference the correct template"
    - "Artifacts flow: draft -> validated -> approved (minimum viable lifecycle)"
  on_fail: "WARNING - Lifecycle state coverage incomplete"
```

### Step 5: Check Agnosticism (NON-NEGOTIABLE)

```yaml
agnosticism_check:
  id: "FW-AG-001"
  severity: BLOCKING
  check: "Squad contains no business-specific data"
  validation:
    - "No product names, prices, or client data in squad files"
    - "No business-specific URLs or endpoints hardcoded"
    - "Templates use placeholders, not concrete values"
    - "Data files contain frameworks/rules, not business instances"
  on_fail: "BLOCK - Squad contains business-specific data"
```

### Step 6: Score Compliance

```yaml
compliance_scoring:
  artifact_contracts: "present + valid = 30 points"
  bu_mapping: "present + valid = 15 points"
  supported_modes: "present + valid = 15 points"
  lifecycle_coverage: "templates exist + transitions defined = 20 points"
  agnosticism: "no business data = 20 points"
  total: "100 points"

  interpretation:
    90-100: "FULL COMPLIANCE"
    70-89: "PARTIAL COMPLIANCE - recommended improvements"
    50-69: "LOW COMPLIANCE - required improvements"
    0-49: "NON-COMPLIANT - blocking"
```

## Output

```yaml
output:
  schema:
    compliance_score: 0-100
    compliance_level: "FULL | PARTIAL | LOW | NON_COMPLIANT"
    checks:
      artifact_contracts:
        status: "PASS | FAIL | MISSING"
        count: N
        valid: N
      bu_mapping:
        status: "PASS | MISSING"
        value: "bu-name | null"
      supported_modes:
        status: "PASS | MISSING"
        modes: [...]
      lifecycle:
        status: "PASS | PARTIAL | FAIL"
        coverage: "N%"
      agnosticism:
        status: "PASS | FAIL"
        violations: [...]
    blocking_issues: []
    warnings: []
```

## Acceptance Criteria

- [ ] artifact_contracts validated against template existence
- [ ] bu_mapping validated against known BU definitions
- [ ] supported_modes validated against canonical mode list
- [ ] Lifecycle states checked for completeness
- [ ] Agnosticism check catches business-specific data
- [ ] Compliance score calculated correctly from weighted checks
- [ ] Blocking issues prevent PASS in parent validation

## Veto Conditions

- artifact_contracts missing entirely -> BLOCK (governance framework REQUIRED field)
- Business-specific data found in squad -> BLOCK (agnosticism violation)

## Related Documents

- `validate-squad.md` (parent composed task)
- `governance/composition-rules.yaml` (canonical composition rules)
- `data/process-token-map.yaml` (contrato local de tokens do processo)
- `.claude/rules/squads.md` (squad structure rules)
- `.claude/rules/workspace-docs.md` (agnosticism rules)
