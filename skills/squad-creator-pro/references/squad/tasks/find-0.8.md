# Task: find-0.8 (Stub)

> **Pareto ao Cubo** | Identificar 0,8% genialidade, 4% excelencia, 20% impacto, 80% merda

**Task ID:** find-0.8
**Execution Type:** Agent (requires judgment to classify activities)
**Model:** `Sonnet` (needs reasoning for activity classification)
**Haiku Eligible:** NO
**Orchestrator:** @squad-chief

## Objetivo

Aplicar Pareto ao Cubo para mapear atividades/conhecimentos nas 4 zonas e priorizar o que realmente importa.

## Contexto

Pareto ao Cubo e a aplicacao tripla da regra 80/20:

- **1a aplicacao**: 20% geram 80% dos resultados
- **2a aplicacao**: 4% (20% de 20%) geram 64% dos resultados
- **3a aplicacao**: 0,8% (20% de 4%) geram ~51% dos resultados

---

## CHECKPOINT INTEGRAL

```yaml
checkpoint_pareto_integral:
  consult: "MODELS.pareto_ao_cubo + OBSESSIONS.eficiencia_alavancagem_maxima"
  question: "Apliquei o framework COMPLETO (4 testes + 3 niveis de leverage)?"
  veto: "Task SEM framework completo = FAIL automatico"
  hierarchy: "ELIMINA (80%) -> AUTOMATIZA (restante) -> AMPLIFICA (0.8%)"
```

---

## Sub-Tasks (Atomic Execution)

| # | Sub-Task | File | Responsibility |
|---|----------|------|----------------|
| 1 | Classify | `find-0.8-classify.md` | Apply 4 zones + Checklist Lendario decision flow to classify activities |
| 2 | Recommend | `find-0.8-recommend.md` | Generate action recommendations per zone + output report |

---

## Execution Flow

```
Step 1: find-0.8-classify
  Input: list of activities/knowledge areas
  Output: classified activities in 4 zones with justifications

Step 2: find-0.8-recommend
  Input: classified activities
  Output: action plan (eliminate/automate/delegate/protect) + report YAML
```

---

## Completion Criteria

| Criterio | Status |
|----------|--------|
| Todas atividades passaram pelo Checklist Lendario | [ ] |
| Cada atividade classificada em uma zona | [ ] |
| Justificativa para cada classificacao | [ ] |
| Recomendacoes de acao para cada zona | [ ] |
| 0,8% claramente identificado e protegido | [ ] |

---

## Nota Importante

> O que e "Zona de Merda" (80%) para uma pessoa pode ser "Zona de Genialidade" (0,8%) para outra.

A classificacao depende de: habilidades unicas, paixao, potencial de impacto, capacidade de execucao.

---

_Task Version: 2.0.0_
_Atomized: 2026-03-26_
_Sub-tasks: find-0.8-classify, find-0.8-recommend_

*"0,8% produz 51% dos resultados. Proteja a genialidade, elimine a merda."*

## Task Anatomy

- **Executor:** Agent
- **Inputs:** Pipeline context from prior tasks
- **Outputs:** Completed find-0.8 output artifact
- **Completion Criteria:** All items in Quality Check/Completion Criteria above are satisfied
- **Guardrails:** See Veto Conditions above

## Acceptance Criteria

- [ ] Output artifact produced: Completed find-0.8 output artifact
- [ ] Task output validated against quality standards
