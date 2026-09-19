---
task: diagnoseCaption()
responsavel: caption-strategist
responsavel_type: Agente
atomic_layer: Analysis
Entrada:
  - nome: existing_caption
    tipo: string
    obrigatorio: true
  - nome: format
    tipo: "feed | reels | carousel | stories"
    obrigatorio: true
  - nome: goal
    tipo: "engagement | authority | sale"
    obrigatorio: true
  - nome: niche
    tipo: string
    obrigatorio: true
Saida:
  - nome: diagnosis
    tipo: "Identified weak points per element (hook, body, CTA)"
    obrigatorio: true
  - nome: rewritten_caption
    tipo: string
    obrigatorio: true
  - nome: improvement_summary
    tipo: "What changed and why"
    obrigatorio: true
Checklist:
  - Original caption received before starting
  - Weak points identified with specific explanation
  - Rewritten caption follows hook + development + CTA structure
  - Improvement summary delivered
---

# diagnose-caption

## Description
Receives an existing caption, diagnoses what is weak, and delivers a rewritten version with an explanation of each improvement.

---

## Required Inputs

| Input | Required |
|-------|----------|
| Original caption | Yes |
| Post goal | Yes |
| Format | Yes |
| Niche | Yes |

---

## Execution Flow

```
STEP 1 — Diagnosis
→ Evaluate hook (stops the scroll? yes/no)
→ Evaluate structure (paragraphs, spacing)
→ Evaluate CTA (clear? single? coherent with goal?)
→ Evaluate tone (consistent from start to finish?)
→ Evaluate length (appropriate for the format?)

STEP 2 — Problem list
→ Identify the 3–5 weakest points with justification

STEP 3 — Rewrite
→ Rewrite the caption fixing the identified problems
→ Preserve the creator's voice — don't replace, improve

STEP 4 — Change explanation
→ For each change, explain what was done and why
```

---

## Output

```
DIAGNOSIS
=========
Hook: [WEAK / AVERAGE / STRONG] — [reason]
Structure: [WEAK / AVERAGE / STRONG] — [reason]
CTA: [WEAK / AVERAGE / STRONG] — [reason]
Tone: [CONSISTENT / INCONSISTENT] — [reason]
Length: [APPROPRIATE / TOO LONG / TOO SHORT]

MAIN ISSUES:
1. [issue + why it hurts performance]
2. [issue + why it hurts performance]
3. [issue + why it hurts performance]

REWRITTEN CAPTION:
==================
[fixed caption]

WHAT CHANGED:
- [change 1 → reason]
- [change 2 → reason]
- [change 3 → reason]
```

---

## Veto Conditions

- Do not rewrite without diagnosing first — the user needs to understand the why
- Do not change the creator's tone without flagging it — respect the original voice

---

## Completion Criteria

- [ ] Diagnosis delivered across all 5 dimensions with score and comment
- [ ] List of 3–5 issues with justification
- [ ] Complete rewritten caption (not just excerpts)
- [ ] Explanation of each change made
