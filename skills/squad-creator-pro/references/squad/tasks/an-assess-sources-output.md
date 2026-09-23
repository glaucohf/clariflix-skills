---
task-id: an-assess-sources-output
name: "Generate Source Map & Feedback Loop"
version: 1.0.0
execution_type: Hybrid
model: Haiku
model_rationale: "Source map generation is template-fill. Feedback loop requires light interpretation but bounded by evidence rules."
haiku_eligible: true
estimated-time: 10 min
complexity: medium

inputs:
  required:
    - prioritized_sources: "Fontes com tier e prioridade (output de an-assess-sources-prioritize)"
    - scored_sources: "Fontes com checkpoints detalhados (output de an-assess-sources-score)"
  optional:
    - extraction_results: "Resultados de extracao ja completada (para feedback loop)"

outputs:
  primary:
    - source_assessment: "Source map YAML completo com checkpoints, recommendations e gaps"

elicit: false
---

# Task: Generate Source Map & Feedback Loop

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-assess-sources-output` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@oalanicolas` |
| **Execution Type** | `Hybrid` |

## Metadata

- **Parent Task:** `an-assess-sources` (orchestrator stub)
- **Sequence:** Phase 4 of 4
- **Previous Task:** `an-assess-sources-prioritize`
- **Next Task:** None (final output)

## Purpose

Gerar o source map YAML final consolidando todos os dados das fases anteriores, incluindo recommendations, gap analysis, e o feedback loop pos-extracao quando aplicavel.

## Prerequisites

- `an-assess-sources-prioritize` completed with `prioritized_sources`
- `an-assess-sources-score` completed with `scored_sources` (for checkpoint details)

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `prioritized_sources` | Yes | Sources with tier and extraction priority |
| `scored_sources` | Yes | Sources with detailed 25-checkpoint data |
| `extraction_results` | No | Post-extraction data for feedback loop (GAP, Inversions, Evasion) |

## Workflow / Steps

### Step 1: Generate Source Map YAML

Assemble the final output combining all upstream data:

```yaml
source_assessment:
  mind: "{nome}"
  version: "2.0"
  assessment_date: "{ISO date}"

  summary:
    total_sources: {n}
    crown_jewel: {n}
    ouro: {n}
    mixed: {n}
    bronze: {n}
    average_quality: {media das medias}

  sources:
    - name: "{fonte}"
      type: "{video|podcast|livro|post|curso|entrevista}"
      url: "{link se disponivel}"
      duration: "{duracao/paginas}"
      checkpoints: # Full structure defined in an-assess-sources-score
        autenticidade: { ...5 bools, score: 0-5 }
        profundidade: { ...5 bools, score: 0-5 }
        atualidade: { ...5 bools, score: 0-5 }
        unicidade: { ...5 bools, score: 0-5 }
        completude: { ...5 bools, score: 0-5 }
      media: {A+P+At+U+C / 5}
      tier: "crown_jewel|ouro|mixed|bronze"
      extraction_priority: {1-n}
      notes: "{observacoes especificas}"

  recommendations:
    - action: "{acao recomendada}"
      priority: "urgente|alta|media"
      rationale: "{por que}"

  gaps_identified:
    - "{dimensao/aspecto que falta cobertura}"
```

### Step 2: Generate Recommendations

Based on scoring gaps:
- Dimensions with average < 3.0 across all sources -> recommend acquiring new sources
- Single-source coverage for key frameworks -> recommend triangulation
- Missing source types (e.g., no long interviews) -> recommend specific acquisition

### Step 3: Identify Gaps

Scan for systematic weaknesses:
- Dimensions consistently low across all sources
- Missing source types that would improve specific dimensions
- Temporal gaps (all sources from same period)

### Step 4: Post-Extraction Tier Reassessment (Conditional)

**When to execute:** ONLY after completing extraction (extract-framework, extract-implicit) on at least 1 source.

**Purpose:** Findings from the 3 lenses (GAP Analysis, Inversions, Evasion Scan) can CHANGE a source tier classification. Initial assessment is surface-level. Post-extraction provides deep evidence.

```yaml
tier_feedback_loop:
  upgrade_triggers:
    to_crown_jewel:
      - "GAP alto + >=2 inversoes reais com [SOURCE:] -> fonte tem pensamento ao vivo excepcional"
      - "Evasion Scan revela padrao unico (expert evade tema que TODOS no campo abordam) -> perspectiva singular"
    to_ouro:
      - "Fonte classificada MIXED mas GAP Analysis revelou desvios espontaneos com frameworks ocultos"
      - "Inversao encontrada em fonte que parecia generica -> reclassificar"

  downgrade_triggers:
    to_bronze:
      - "GAP baixo (zero desvios) + zero inversoes -> fonte e script, nao pensamento"
      - "Evasion Scan mostra evasao em temas CENTRAIS do expertise declarado -> fonte superficial"
    to_mixed:
      - "Fonte OURO mas Evasion Scan mostra evasao em >50% dos temas profundos -> confianca limitada"

  rules:
    - "Reclassificacao requer EVIDENCIA documentada com [SOURCE:]"
    - "NAO e override subjetivo — e atualizacao baseada em dados novos"
    - "Documentar ANTES e DEPOIS no source map com justificativa"
    - "Reclassificacao pode mudar prioridade de extracao das fontes restantes"

  template:
    source: "{nome da fonte}"
    tier_original: "{ouro/mixed/bronze}"
    tier_reassessed: "{novo tier}"
    trigger: "{qual trigger ativou}"
    evidence: "{dados da lente que justificam}"
    impact: "{mudou prioridade de extracao? como?}"
```

#### Checkpoint: Feedback Loop vs Override

```yaml
checkpoint_feedback_loop:
  consult: "VALUES.clareza_radical"
  question: "Reclassificacao e baseada em EVIDENCIA das lentes ou em OPINIAO pos-hoc?"
  if_evidencia: "Reclassificar e documentar no source map"
  if_opiniao: "VETO — manter tier original. Opiniao nao sobrescreve mecanica."
  rationale: "O feedback loop existe para incorporar DADOS NOVOS, nao para reinterpretar dados antigos."
```

## Output

The complete `source_assessment` YAML as defined in Step 1.

## Acceptance Criteria

- [ ] Source map YAML gerado com checkpoints detalhados para cada fonte
- [ ] Recommendations geradas baseadas em gaps de scoring
- [ ] Gaps identificados para busca de fontes adicionais
- [ ] Post-Extraction Feedback Loop executado (se extracao ja foi feita)
- [ ] Feedback loop usa apenas EVIDENCIA, nao opiniao

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-AS-007 | Feedback loop reclassification without [SOURCE:] evidence | BLOCK — evidence required |
| VETO-AS-008 | Opinion-based tier override in feedback loop | BLOCK — keep original tier |

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-assess-sources.md` | Parent orchestrator |
| `an-assess-sources-prioritize.md` | Previous phase (tier + priority) |
| `an-extract-framework.md` | Extraction task (provides feedback loop data) |
| `extract-implicit.md` | Implicit extraction (provides feedback loop data) |
