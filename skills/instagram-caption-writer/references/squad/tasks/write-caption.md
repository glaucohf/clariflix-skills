---
task: writeCaption()
responsavel: instagram-caption-chief
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: post_topic
    tipo: string
    obrigatorio: true
  - nome: format
    tipo: "feed | reels | carousel | stories"
    obrigatorio: true
  - nome: goal
    tipo: "engagement | authority | sale"
    obrigatorio: true
  - nome: voice_tone
    tipo: string
    obrigatorio: true
  - nome: niche
    tipo: string
    obrigatorio: true
  - nome: product_service
    tipo: string
    obrigatorio: false
Saida:
  - nome: caption_variation_a
    tipo: string
    obrigatorio: true
  - nome: caption_variation_b
    tipo: string
    obrigatorio: true
  - nome: caption_variation_c
    tipo: string
    obrigatorio: true
  - nome: hashtags
    tipo: "30 segmented hashtags (10 large + 10 medium + 10 small)"
    obrigatorio: true
  - nome: cta_recommendation
    tipo: string
    obrigatorio: true
  - nome: posting_time
    tipo: string
    obrigatorio: true
Checklist:
  - All required inputs collected before execution
  - caption-strategist defined angle and structure first
  - 3 complete variations delivered (emotional / logical / provocative)
  - 30 hashtags segmented in 3 groups
  - CTA and posting time included in output
---

# write-caption

## Description
Main flow for creating an Instagram caption. From user input to final output with 3 caption variations + 30 hashtags.

---

## Required Inputs

Collect before starting:

| Input | Required | Example |
|-------|----------|---------|
| Post topic | Yes | "How to use email marketing to sell" |
| Format | Yes | feed / reels / carousel / stories |
| Goal | Yes | engagement / authority / sale |
| Voice tone | Yes | casual / direct / inspirational / educational |
| Niche | Yes | digital marketing / fitness / cooking |
| Product/service | If sale | "Email marketing course — $297" |

If any field is missing, **ask before executing.**

---

## Execution Flow

```
STEP 1 — caption-strategist
→ Analyzes inputs
→ Chooses hook angle
→ Defines caption structure
→ Delivers blueprint

STEP 2 — caption-writer
→ Receives blueprint
→ Writes 3 complete variations (A / B / C)
→ Respects format rules

STEP 3 — hashtag-researcher
→ Receives niche + topic + format
→ Delivers 30 segmented hashtags
→ Includes usage instructions

STEP 4 — final output
→ Compiles using template caption-output.md
→ Presents to user
```

---

## Veto Conditions

- Do not execute without format defined — feed and reels have completely different rules
- Do not execute without goal defined — CTA changes completely by goal
- Do not deliver fewer than 3 variations — this is the squad's core differentiator

---

## Completion Criteria

- [ ] caption-strategist blueprint delivered and validated
- [ ] 3 caption variations written respecting format rules
- [ ] 30 hashtags segmented in 3 groups
- [ ] Posting time recommendation included
- [ ] Output formatted with caption-output.md template
