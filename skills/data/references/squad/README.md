# Data Intelligence Pack v2.0

> Analytics Clone Squad - Time de especialistas em analytics organizados por Tier para decisoes baseadas em dados.

**Slash Prefix:** `/Data:*`

---

## Status de Implementacao

| Componente | Implementado | Total | Status |
|------------|--------------|-------|--------|
| Agents | 7 | 7 | COMPLETO |
| Tasks | 13 | 13 | COMPLETO |
| Workflows | 7 | 7 | COMPLETO |
| Views SQL | 8 | 8 | COMPLETO |
| Templates | 16 | 16 | COMPLETO |
| Checklists | 4 | 6 | PARCIAL |
| Docs Framework | 8 | 8 | COMPLETO |

**Completude: ~85%**

---

## Quick Start

### Ativar um Especialista

```
/Data:agents:data-chief
*workspace-preflight
*workspace-context {slug}
/Data:agents:data-chief       # Orquestrador - delega para clone certo
/Data:agents:peter-fader      # Tier 0 - CLV, RFM, Segmentacao
/Data:agents:sean-ellis       # Tier 0 - PMF, Viral, Growth
/Data:agents:nick-mehta       # Tier 1 - Health Score, Churn
/Data:agents:david-spinks     # Tier 1 - Community Metrics
/Data:agents:wes-kao          # Tier 1 - Learning Outcomes
/Data:agents:avinash-kaushik  # Tier 2 - Attribution, Reports
```

### Executar um Workflow

```
/Data:workflows:implement-customer-360     # Customer 360 completo
/Data:workflows:create-churn-system        # Sistema de Churn Alerts
/Data:workflows:implement-attribution      # Attribution Marketing
/Data:workflows:fix-completion-rate        # Aumentar Completion Rate
/Data:workflows:cohort-analysis-workflow   # Analise de Cohorts
/Data:workflows:optimize-community-workflow # Otimizar Comunidade
/Data:workflows:cohorts-diagnostic         # Diagnostico integrado de cohorts (6 artefatos)
```

### Executar uma Task

```
/Data:tasks:calculate-clv           # Calcular CLV
/Data:tasks:segment-rfm             # Segmentacao RFM
/Data:tasks:predict-churn           # Prever Churn
/Data:tasks:design-health-score     # Criar Health Score
/Data:tasks:build-attribution       # Attribution Model
/Data:tasks:analyze-cohort          # Analise de Cohort
/Data:tasks:measure-community       # Metricas de Comunidade
/Data:tasks:design-learning-outcomes # Learning Outcomes
/Data:tasks:run-pmf-test            # Sean Ellis PMF Test
/Data:tasks:define-north-star       # Definir North Star Metric
/Data:tasks:run-growth-experiment   # Experimentos de Growth
/Data:tasks:create-dashboard        # Criar Dashboard
/Data:tasks:load-workspace-context  # Carregar contexto workspace-first
```

---

## Workspace Integration Governance

O squad `data` opera em `workspace_first`.

Preflight obrigatório:

```bash
bash squads/data/scripts/bootstrap-data-workspace.sh {slug}
bash squads/data/scripts/validate-data-essentials.sh
```

### Regras de output

1. **Canonical (template-first):**
`workspace/businesses/{slug}/analytics/{artifact}.yaml`
Somente permitido se existir template correspondente em:
`workspace/_templates/analytics/{artifact}.yaml`

1.1 **Canonical Pack Cohorts (template-first):**
`workspace/businesses/{slug}/analytics/cohorts/{artifact}.yaml`
Somente permitido se existir template correspondente em:
`workspace/_templates/analytics/cohorts/{artifact}.yaml`

2. **Custom (ad-hoc):**
`docs/data/{slug}/{artifact}.md`
Permitido para relatórios personalizados sem contrato canônico.

### Catálogo de templates analytics

`customer-360.yaml`, `clv-report.yaml`, `cohort-analysis.yaml`, `health-score-report.yaml`, `churn-alert.yaml`, `attribution-report.yaml`, `dmmm.yaml`, `executive-report.yaml`, `community-health.yaml`, `learning-outcomes.yaml`

Pack `analytics/cohorts/`:

`segmentation-rfm.yaml`, `learning-journey.yaml`, `community-health.yaml`, `student-health-score.yaml`, `icp-deep-analysis.yaml`, `executive-summary.yaml`

Ownership direto do pack `cohorts`: `cmo-architect`, `@ry-schwartz`, `@data-chief`.

---

## Arquitetura de 3 Tiers

```
+---------------------------------------------------------------------+
|                    TIER 0 - FUNDAMENTACAO                            |
|              "Quem importa e como crescer"                           |
|              USAR ANTES de qualquer metrica                          |
+---------------------------------------------------------------------+
|   @peter-fader (Wharton)     |   @sean-ellis (GrowthHackers)        |
|   CLV, RFM, Segmentacao      |   Viral, Referral, PMF               |
|   "Quem vale mais?"          |   "Como crescer?"                    |
+---------------------------------------------------------------------+
                                |
                                v
+---------------------------------------------------------------------+
|                    TIER 1 - OPERACIONALIZACAO                        |
|              "Como monitorar, medir e alertar"                       |
+---------------------------------------------------------------------+
|  @nick-mehta    |  @david-spinks   |  @wes-kao                      |
|  (Gainsight)    |  (CMX)           |  (Maven)                       |
|  Health/Churn   |  Community       |  Learning                      |
+---------------------------------------------------------------------+
                                |
                                v
+---------------------------------------------------------------------+
|                    TIER 2 - COMUNICACAO                              |
|              "Como traduzir em acao e apresentar"                    |
+---------------------------------------------------------------------+
|                      @avinash-kaushik (ex-Google)                    |
|                      Attribution, Reports, So What                   |
+---------------------------------------------------------------------+
```

### Regra de Ouro

> **Nunca implemente uma metrica sem passar por pelo menos 1 fundamentador (Tier 0).**

---

## Views SQL Implementadas

Views disponiveis em `supabase/migrations/20260123_001_data_intelligence_views.sql`:

### Tier 0 - CLV & RFM (Peter Fader)

| View | Descricao |
|------|-----------|
| `v_rfm_segments` | Scores R, F, M por customer |
| `v_rfm_customer_classification` | Classificacao (Champions, Loyal, At Risk, etc) |
| `v_customer_lifetime_value` | CLV historico e preditivo |
| `v_clv_cohort_comparison` | CLV por cohort de aquisicao |

### Tier 1 - Health & Churn (Nick Mehta)

| View | Descricao |
|------|-----------|
| `v_customer_health_composite` | Health Score multi-dimensional (DEAR) |
| `v_health_components_breakdown` | Detalhamento por componente DEAR |
| `v_churn_risk_scores` | Score de risco 0-100 |
| `v_churn_leading_indicators` | Sinais de churn + playbooks |

### Queries de Exemplo

```sql
-- Top clientes por CLV
SELECT mind_slug, historical_clv_brl, clv_tier
FROM v_customer_lifetime_value
ORDER BY historical_clv_brl DESC
LIMIT 10;

-- Clientes em risco de churn
SELECT mind_slug, churn_risk_score, risk_category, recommended_playbook
FROM v_churn_leading_indicators
WHERE churn_risk_score > 70
ORDER BY churn_risk_score DESC;

-- Distribuicao de Health Score
SELECT health_category, COUNT(*) as customers
FROM v_customer_health_composite
GROUP BY health_category
ORDER BY COUNT(*) DESC;

-- Segmentos RFM
SELECT segment, COUNT(*) as customers,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as pct
FROM v_rfm_customer_classification
GROUP BY segment
ORDER BY customers DESC;
```

---

## Workflows Disponiveis (7/7)

| # | Workflow | Comando | Fases | Clones |
|---|----------|---------|-------|--------|
| 1 | **Customer 360** | `/Data:workflows:implement-customer-360` | 3 | Fader -> Mehta -> Kaushik |
| 2 | **Churn System** | `/Data:workflows:create-churn-system` | 3 | Mehta -> Fader -> Spinks -> Kao |
| 3 | **Attribution** | `/Data:workflows:implement-attribution` | 4 | Kaushik -> Ellis -> Fader |
| 4 | **Fix Completion** | `/Data:workflows:fix-completion-rate` | 5 | Kao -> Spinks -> Mehta -> Kaushik |
| 5 | **Cohort Analysis** | `/Data:workflows:cohort-analysis-workflow` | 4 | Fader -> Ellis -> Kao -> Kaushik |
| 6 | **Optimize Community** | `/Data:workflows:optimize-community-workflow` | 4 | Spinks -> Mehta -> Kao -> Kaushik |
| 7 | **Cohorts Diagnostic** | `/Data:workflows:cohorts-diagnostic` | 6 | Fader -> Kao -> Spinks -> Mehta -> Ry Schwartz -> Kaushik |

---

## Agents (7/7)

### Tier 0 - Fundamentadores

| Agent | Especialidade | Frameworks |
|-------|---------------|------------|
| **@peter-fader** | CLV, RFM, Customer Centricity | Customer Centricity, BG/NBD, Gamma-Gamma |
| **@sean-ellis** | PMF, AARRR, North Star | AARRR, ICE Score, Sean Ellis Test, Viral Coefficient |

### Tier 1 - Operacionalizadores

| Agent | Especialidade | Frameworks |
|-------|---------------|------------|
| **@nick-mehta** | Health Score, Churn | DEAR Framework, Churn Signals, CS Playbooks |
| **@david-spinks** | Community Metrics | SPACES Model, Three-Level Strategy |
| **@wes-kao** | Learning Outcomes | Course Mechanics Canvas, State Change Method |

### Tier 2 - Comunicadores

| Agent | Especialidade | Frameworks |
|-------|---------------|------------|
| **@avinash-kaushik** | Attribution, Reports | DMMM, So What Framework, See-Think-Do-Care |

### Orquestrador

| Agent | Funcao |
|-------|--------|
| **@data-chief** | Delega para clone correto, coordena workflows |

---

## Tasks (13/13)

| Task | Agent | Descricao |
|------|-------|-----------|
| `calculate-clv` | @peter-fader | Calcular CLV historico e preditivo |
| `segment-rfm` | @peter-fader | Segmentacao RFM de clientes |
| `analyze-cohort` | @peter-fader | Analise de cohort para retencao |
| `design-health-score` | @nick-mehta | Criar Health Score com DEAR |
| `predict-churn` | @nick-mehta | Sistema de predicao de churn |
| `run-pmf-test` | @sean-ellis | Executar Sean Ellis PMF Test |
| `define-north-star` | @sean-ellis | Definir North Star Metric |
| `run-growth-experiment` | @sean-ellis | Experimentos com ICE scoring |
| `measure-community` | @david-spinks | Metricas SPACES de comunidade |
| `design-learning-outcomes` | @wes-kao | Learning outcomes e completion |
| `build-attribution` | @avinash-kaushik | Modelo de attribution marketing |
| `create-dashboard` | @avinash-kaushik | Dashboard com DMMM e So What |
| `load-workspace-context` | @data-chief | Preflight e roteamento canonical/custom |

---

## Templates (16/16)

| Template | Agent | Status |
|----------|-------|--------|
| `customer-360.yaml` | @peter-fader | Implementado |
| `clv-report.yaml` | @peter-fader | Implementado |
| `cohort-analysis.yaml` | @peter-fader | Implementado |
| `health-score-report.yaml` | @nick-mehta | Implementado |
| `churn-alert.yaml` | @nick-mehta | Implementado |
| `attribution-report.yaml` | @avinash-kaushik | Implementado |
| `dmmm.yaml` | @avinash-kaushik | Implementado |
| `executive-report.yaml` | @avinash-kaushik | Implementado |
| `community-health.yaml` | @david-spinks | Implementado |
| `learning-outcomes.yaml` | @wes-kao | Implementado |
| `cohorts/segmentation-rfm.yaml` | @peter-fader | Implementado |
| `cohorts/learning-journey.yaml` | @wes-kao | Implementado |
| `cohorts/community-health.yaml` | @david-spinks | Implementado |
| `cohorts/student-health-score.yaml` | @nick-mehta | Implementado |
| `cohorts/icp-deep-analysis.yaml` | @ry-schwartz | Implementado |
| `cohorts/executive-summary.yaml` | @avinash-kaushik | Implementado |

---

## Checklists (4/6)

| Checklist | Agent | Status |
|-----------|-------|--------|
| `customer-360-checklist.md` | ALL | Implementado |
| `health-score-checklist.md` | @nick-mehta | Implementado |
| `pre-implementation-checklist.md` | ALL | Implementado |
| `so-what-checklist.md` | @avinash-kaushik | Implementado |

---

## Matriz de Selecao Rapida

| Pergunta | Clone |
|----------|-------|
| "Quem sao melhores clientes?" | @peter-fader |
| "Quanto vale cada cliente?" | @peter-fader |
| "Programa de indicacao funciona?" | @sean-ellis |
| "Qual North Star Metric?" | @sean-ellis |
| "Quem em risco de churn?" | @nick-mehta |
| "Que acao tomar com cliente X?" | @nick-mehta |
| "Comunidade esta saudavel?" | @david-spinks |
| "Por que membros nao participam?" | @david-spinks |
| "Por que completion 3%?" | @wes-kao |
| "Como redesenhar curso?" | @wes-kao |
| "Qual fonte traz clientes?" | @avinash-kaushik |
| "Como apresentar pro CEO?" | @avinash-kaushik |

---

## Estrutura do Pack

```
squads/data/
+-- config.yaml                    # Configuracao do pack
+-- README.md                      # Este arquivo
+-- agents/                        # Definicoes dos clones (7)
+-- tasks/                         # Tarefas executaveis (13)
+-- workflows/                     # Workflows completos (7)
+-- templates/                     # Templates fonte do squad (16)
+-- checklists/                    # Validacao (4)
+-- scripts/                       # Bootstrap + validação workspace-first
+-- docs/framework/                # Documentacao do framework (8)
```

---

## Changelog

### v2.0.0 (2026-01-23)

**MAJOR UPGRADE - Framework de Clones Completo**

- 7 agents implementados (100%)
- 12 tasks implementadas (100%)
- 6 workflows implementados (100%)
- 8 views SQL implementadas (Churn, Health, CLV, RFM)
- Integracao com Claude Code via slash commands `/Data:*`

**Views SQL:**
`v_rfm_segments`, `v_rfm_customer_classification`, `v_customer_lifetime_value`, `v_clv_cohort_comparison`, `v_customer_health_composite`, `v_health_components_breakdown`, `v_churn_risk_scores`, `v_churn_leading_indicators`

**Workflows:**
`implement-customer-360`, `create-churn-system`, `implement-attribution`, `fix-completion-rate`, `cohort-analysis-workflow`, `optimize-community-workflow`, `cohorts-diagnostic`

---

*Data Intelligence Pack v2.0*
*Analytics Clone Squad for Data-Driven Decisions*
*Last Updated: 2026-01-23*
