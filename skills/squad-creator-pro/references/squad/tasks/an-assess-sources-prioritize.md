---
task-id: an-assess-sources-prioritize
name: "Calculate Tier & Prioritize Sources"
version: 1.0.0
execution_type: Deterministic
model: Haiku
model_rationale: "Tier calculation is purely mechanical (thresholds + special rules). No interpretation needed."
haiku_eligible: true
estimated-time: 5 min
complexity: low

inputs:
  required:
    - scored_sources: "Fontes com scores por dimensao (output de an-assess-sources-score)"

outputs:
  primary:
    - prioritized_sources: "Fontes com tier classificado e prioridade de extracao ordenada"

elicit: false
---

# Task: Calculate Tier & Prioritize Sources

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-assess-sources-prioritize` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@oalanicolas` |
| **Execution Type** | `Deterministic` |

## Metadata

- **Parent Task:** `an-assess-sources` (orchestrator stub)
- **Sequence:** Phase 3 of 4
- **Previous Task:** `an-assess-sources-score`
- **Next Task:** `an-assess-sources-output`

## Purpose

Calcular tier de cada fonte mecanicamente a partir dos scores e ordenar por prioridade de extracao.

## Prerequisites

- `an-assess-sources-score` completed with `scored_sources`
- All sources have media (average) calculated

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `scored_sources` | Yes | Sources with 5-dimension scores and media |

## Workflow / Steps

### Step 1: Calculate Tier (MECHANICAL)

```yaml
tier_calculation:
  formula: "media = (A + P + At + U + C) / 5"

  thresholds:
    ouro:
      range: ">= 4.0"
      meaning: "Fonte premium - prioridade maxima de extracao"
      checkpoints_passed: "20+ de 25"

    mixed:
      range: "3.0 - 3.9"
      meaning: "Usar com cautela - complementar, nao base"
      checkpoints_passed: "15-19 de 25"

    bronze:
      range: "< 3.0"
      meaning: "Descartar como base - baixo ROI"
      checkpoints_passed: "<15 de 25"

  special_rules:
    - "SE Autenticidade < 3 -> BRONZE (independente do resto)"
    - "SE Profundidade = 5 AND Autenticidade >= 4 -> CROWN JEWEL"
    - "SE todas dimensoes >= 4 -> CROWN JEWEL"

  # ANTI-OVERRIDE RULE (CRITICAL)
  no_subjective_override:
    principle: "Tier classification e MECANICA, nao subjetiva"
    rule: |
      SE special_rules sao satisfeitas -> APLICAR tier automaticamente
      NUNCA fazer override com julgamentos como:
        - "e livro 3 de 3, menos original"
        - "e sintese, nao criacao"
        - "parece menos importante"

    examples:
      correto:
        - "Score 5/5/5/5/5 -> CROWN JEWEL (todas dimensoes >= 4)"
        - "Score 5/5/4/4/4 -> CROWN JEWEL (Profundidade=5 AND Autenticidade>=4)"
      incorreto:
        - "Score 5/5/5/5/5 -> OURO porque 'e livro 3'" # PROIBIDO
        - "Score 5/5/5/5/5 -> OURO porque 'e sintese'" # PROIBIDO

    enforcement: |
      APOS calcular scores, APLICAR special_rules mecanicamente.
      Tier e DETERMINADO pelos numeros, nao por interpretacao.
      Notas subjetivas vao em "notes:", nao afetam tier.
```

### Step 2: Prioritize Sources by Extraction Value

Ordenar fontes OURO por valor de extracao:

```yaml
extraction_priority:
  crown_jewel:
    description: "0.8% - gera 51% do resultado"
    types:
      - "Entrevistas longas (>1h) com perguntas dificeis"
      - "Podcasts em formato conversacional profundo"
      - "Debates/discussoes com challengers"

  ouro:
    description: "4% - gera 33% do resultado"
    types:
      - "Comentarios respondendo perguntas reais de audiencia"
      - "Cases detalhados com analise de decisoes"
      - "Livros com metodologia propria"

  impacto:
    description: "20% - gera 16% do resultado"
    types:
      - "Stories espontaneos"
      - "Posts com insights especificos"
      - "Cursos (secoes de Q&A)"

  bronze:
    description: "80% - ELIMINAR"
    types:
      - "Conteudo scripted/promocional"
      - "Reposts/compilacoes de outros"
      - "Material datado sem insights unicos"
```

### Step 3: Assign Extraction Priority Numbers

For each source, assign `extraction_priority: {1-n}` based on:
1. Crown Jewels first (ordered by completude score)
2. Ouro next (ordered by profundidade score)
3. Mixed last (ordered by autenticidade score)
4. Bronze excluded from extraction queue

## Output

```yaml
prioritized_sources:
  summary:
    total_sources: {n}
    crown_jewel: {n}
    ouro: {n}
    mixed: {n}
    bronze: {n}
    average_quality: {media das medias}

  sources:
    - name: "{fonte}"
      media: {score}
      tier: "crown_jewel|ouro|mixed|bronze"
      extraction_priority: {1-n}
      notes: "{observacoes especificas — subjective notes go HERE}"
```

## Acceptance Criteria

- [ ] Tier calculado por media das 5 dimensoes para cada fonte
- [ ] Special rules aplicadas mecanicamente (Crown Jewel detection)
- [ ] Nenhum override subjetivo no tier (notas subjetivas em "notes:" apenas)
- [ ] Prioridade de extracao definida e ordenada
- [ ] Summary com contagens por tier

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-AS-005 | Subjective override of mechanical tier | BLOCK — tier is determined by numbers only |
| VETO-AS-006 | Crown Jewel criteria met but not applied | BLOCK — apply special rules |

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-assess-sources.md` | Parent orchestrator |
| `an-assess-sources-score.md` | Previous phase (checkpoint scoring) |
| `an-assess-sources-output.md` | Next phase (source map generation) |
