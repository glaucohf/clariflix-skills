---
task-id: an-assess-sources-score
name: "Score Sources with 25 Binary Checkpoints"
version: 1.0.0
execution_type: Hybrid
model: Haiku
model_rationale: "Script handles all 25 checkpoints deterministically. LLM only for interpretation overlay."
haiku_eligible: true
worker_script: "scripts/assess-sources.sh"
estimated-time: 10 min
complexity: medium

inputs:
  required:
    - raw_sources_list: "Lista catalogada de fontes (output de an-assess-sources-collect)"
  optional:
    - sources_dir: "Caminho para diretorio com fontes baixadas (para worker script)"

outputs:
  primary:
    - scored_sources: "Fontes com scores 0-5 em cada uma das 5 dimensoes"

elicit: false
---

# Task: Score Sources with 25 Binary Checkpoints

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `an-assess-sources-score` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `@oalanicolas` |
| **Execution Type** | `Hybrid (Worker 80% + Agent 20%)` |

## Metadata

- **Parent Task:** `an-assess-sources` (orchestrator stub)
- **Sequence:** Phase 2 of 4
- **Previous Task:** `an-assess-sources-collect`
- **Next Task:** `an-assess-sources-prioritize`

## Purpose

Avaliar cada fonte com 25 checkpoints binarios (5 dimensoes x 5 checks), gerando scores 0-5 por dimensao.

## Prerequisites

- `an-assess-sources-collect` completed with `raw_sources_list`
- Sources available (local files or metadata for manual assessment)

## MANDATORY PREFLIGHT: Run Worker Script FIRST

```
EXECUTE FIRST — when sources directory exists with downloaded files:

  bash squads/squad-creator-pro/scripts/assess-sources.sh <sources-dir> > /tmp/preflight-assess-sources.yaml

IF the command fails -> FIX the script error. Do NOT proceed manually.
IF the command succeeds -> READ /tmp/preflight-assess-sources.yaml. Use as baseline scores.

VETO: If sources are already downloaded as files, do NOT grep checkpoints yourself.
      The script scores all 25 checkpoints per source in <1s each.

      Your job is INTERPRETATION ONLY:
      - Add context the script cannot detect (e.g., source type, duration, URL)
      - Override scores where domain knowledge matters (e.g., D3 Atualidade for books)
      - Generate recommendations and gap analysis

NOTE: Script works on FILE content (grep patterns). For sources not yet downloaded
      or for evaluating metadata (URL, duration, type), use manual assessment.
```

## Scoring Calibration (CRITICAL)

```yaml
scoring_philosophy:
  principle: "SCORE O QUE EXISTE, nao o que falta"
  bias_correction: "Haiku tende a sub-pontuar. Compensar sendo generoso."
  evidence_rule: "Se existe evidencia, conta ponto. Gaps vao para recommendations."

  checkpoint_rules:
    - "PASS = evidence EXISTS (not perfect)"
    - "FAIL = evidence MISSING (not weak)"
    - "Partial = PASS (generous interpretation)"
    - "Duvida = PASS (benefit of the doubt)"
```

## Workflow / Steps

### Step 1: Dimensao 1 — AUTENTICIDADE (5 checkpoints)

| # | Checkpoint | O que procurar | Passa se... |
|---|------------|----------------|-------------|
| 1 | Espontaneidade | Tom de voz, padrao de fala | Nao parece scripted/teleprompter |
| 2 | Vulnerabilidade | Admite erros, duvidas | Mostra pelo menos 1 momento de vulnerabilidade |
| 3 | Respostas dificeis | Responde perguntas incomodas | Nao desvia de perguntas challenging |
| 4 | Nuance presente | Muda de ideia, nuances | Mostra evolucao ou nuance, nao binario |
| 5 | Storytelling pessoal | Historias proprias | Conta experiencias de primeira mao |

**Score Autenticidade = count(passed) -> 0-5**

### Step 2: Dimensao 2 — PROFUNDIDADE (5 checkpoints)

| # | Checkpoint | O que procurar | Passa se... |
|---|------------|----------------|-------------|
| 1 | Porque explicado | Raciocinio por tras | Explica motivacao, nao so acao |
| 2 | Framework presente | Metodologia/modelo | Tem estrutura repetivel SE/ENTAO |
| 3 | Exemplos especificos | Cases com detalhes | Cita nomes, numeros, datas especificos |
| 4 | Trade-offs discutidos | Pros e contras | Mostra decisoes e o que sacrificou |
| 5 | Conexoes cross-domain | Liga ideias | Conecta conceitos de areas diferentes |

**Score Profundidade = count(passed) -> 0-5**

### Step 3: Dimensao 3 — ATUALIDADE (5 checkpoints)

| # | Checkpoint | O que procurar | Passa se... |
|---|------------|----------------|-------------|
| 1 | Recencia | Data de publicacao | Criado nos ultimos 3 anos (2023+) |
| 2 | Contexto atual | Referencias temporais | Menciona contexto relevante atual |
| 3 | Nao contradito | Posicoes posteriores | Nao contradiz declaracoes mais recentes da pessoa |
| 4 | Evolucao visivel | Mudanca de pensamento | Mostra amadurecimento vs OBRA ANTERIOR do autor |
| 5 | Aplicabilidade | Relevancia hoje | Conselho ainda funciona em 2026 |

**Score Atualidade = count(passed) -> 0-5**

**REGRA ESPECIAL — Checkpoint "Evolucao":**

```yaml
evolucao_rule:
  definition: "Compara com OBRA ANTERIOR do mesmo autor, nao evolucao interna do texto"
  first_work_rule: "SE e a primeira obra conhecida do autor -> evolucao = FALSE (sem baseline)"
  examples:
    - "$100M Offers (primeiro livro) -> FALSE | $100M Leads (segundo) -> TRUE se mostra mudanca"
  rationale: "Evolucao requer COMPARACAO. Primeira obra = always FALSE (MECANICO)."
```

### Step 4: Dimensao 4 — UNICIDADE (5 checkpoints)

| # | Checkpoint | O que procurar | Passa se... |
|---|------------|----------------|-------------|
| 1 | Contra-mainstream | Posicao diferente | Contradiz "senso comum" do mercado |
| 2 | Vocabulario proprio | Termos unicos | Usa palavras/expressoes signature |
| 3 | Framework original | Modelo nao-copiado | Metodologia nao encontrada em outros |
| 4 | Insight contra-intuitivo | Surpresa fundamentada | Conclusao inesperada com logica solida |
| 5 | Perspectiva singular | Angulo unico | Abordagem que outros autores nao tem |

**Score Unicidade = count(passed) -> 0-5**

### Step 5: Dimensao 5 — COMPLETUDE (5 checkpoints)

| # | Checkpoint | O que procurar | Passa se... |
|---|------------|----------------|-------------|
| 1 | Playbook presente | Passo a passo | Tem instrucoes acionaveis (faca X, depois Y) |
| 2 | Framework presente | SE/ENTAO | Tem regras condicionais documentadas |
| 3 | Exemplos reais | Cases | Tem pelo menos 2 exemplos concretos |
| 4 | Edge cases | Excecoes | Discute quando NAO funciona |
| 5 | Profundidade adequada | Duracao/extensao | >30min video OU >10 paginas texto |

**Score Completude = count(passed) -> 0-5**

## Output

```yaml
scored_sources:
  - name: "{fonte}"
    checkpoints:
      autenticidade: { espontaneidade: bool, vulnerabilidade: bool, respostas_dificeis: bool, nuance: bool, storytelling: bool, score: 0-5 }
      profundidade: { porque_explicado: bool, framework: bool, exemplos_especificos: bool, tradeoffs: bool, cross_domain: bool, score: 0-5 }
      atualidade: { recencia: bool, contexto_atual: bool, nao_contradito: bool, evolucao: bool, aplicabilidade: bool, score: 0-5 }
      unicidade: { contra_mainstream: bool, vocabulario_proprio: bool, framework_original: bool, insight_contraintuitivo: bool, perspectiva_singular: bool, score: 0-5 }
      completude: { playbook: bool, framework_presente: bool, exemplos_reais: bool, edge_cases: bool, profundidade_adequada: bool, score: 0-5 }
    media: {A+P+At+U+C / 5}
```

## Acceptance Criteria

- [ ] Cada fonte avaliada com 25 checkpoints binarios
- [ ] Worker script executado primeiro quando fontes locais existem
- [ ] Scoring calibration aplicada (generous interpretation)
- [ ] Regra especial de Evolucao aplicada corretamente
- [ ] Media calculada para cada fonte

## Veto Conditions

| ID | Condition | Result |
|----|-----------|--------|
| VETO-AS-003 | Worker script available but not executed first | BLOCK — run script |
| VETO-AS-004 | Subjective scoring override without evidence | BLOCK — use checkpoint rules |

## Related Documents

| Document | Relationship |
|----------|-------------|
| `an-assess-sources.md` | Parent orchestrator |
| `an-assess-sources-collect.md` | Previous phase (source collection) |
| `an-assess-sources-prioritize.md` | Next phase (tier + prioritization) |
| `data/an-source-tiers.yaml` | Tier definitions reference |
