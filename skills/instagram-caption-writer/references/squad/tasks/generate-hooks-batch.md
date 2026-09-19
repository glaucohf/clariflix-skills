---
task: generateHooksBatch()
responsavel: hook-generator
responsavel_type: Agente
atomic_layer: Content
Entrada:
  - nome: niche
    tipo: string
    obrigatorio: true
  - nome: goal
    tipo: "engagement | authority | sale"
    obrigatorio: true
  - nome: quantity
    tipo: integer
    obrigatorio: false
Saida:
  - nome: hooks_by_type
    tipo: "Grouped hooks by type: curiosity, controversy, identification, data, story, pain, authority"
    obrigatorio: true
  - nome: total_hooks
    tipo: integer
    obrigatorio: true
Checklist:
  - Niche and goal received before generating
  - Hooks grouped by type (minimum 7 types covered)
  - Minimum 20 hooks delivered
  - Each hook is a complete opening sentence, not a category description
---

# generate-hooks-batch

## Description
Generates a bank of 20+ hooks for a specific niche. The user ends up with a stock of ready-to-use first lines for any post.

---

## Required Inputs

| Input | Required |
|-------|----------|
| Niche | Yes |
| Primary goals | Yes (engagement / authority / sale) |
| Voice tone | Yes |
| Recurring topics (optional) | No |

---

## Execution Flow

```
STEP 1 — hook-generator
→ Generates 20 hooks covering all 7 types
→ Distributes by goal (engagement / authority / sale)

STEP 2 — Organization
→ Groups by hook type
→ Marks which goal each hook best serves

STEP 3 — Bonus
→ Delivers 5 niche-specific hooks
→ Based on patterns that work in that segment
```

---

## Output

```
HOOK BANK — [NICHE]
====================

ENGAGEMENT (7 hooks)
---------------------
1. [hook] — type: [curiosity/identification/question]
2. ...

AUTHORITY (7 hooks)
--------------------
1. [hook] — type: [data/provocation/promise]
2. ...

SALE (6 hooks)
---------------
1. [hook] — type: [direct promise/pain/social proof]
2. ...

BONUS — NICHE-SPECIFIC (5 hooks)
----------------------------------
1. [highly specific hook for the segment]
2. ...
```

---

## Veto Conditions

- Do not repeat the same hook type more than 4 times in the same group
- No hook can start with "Hey", "Hi", or emojis
- No hook can exceed 15 words

---

## Completion Criteria

- [ ] Minimum 20 hooks delivered across 3 goal categories
- [ ] 5 niche-specific bonus hooks included
- [ ] Each hook labeled with type and best goal
- [ ] No type repeated more than 4 times per group
