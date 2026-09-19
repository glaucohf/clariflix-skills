---
task: createContentPillars()
responsavel: caption-strategist
responsavel_type: Agente
atomic_layer: Strategy
Entrada:
  - nome: niche
    tipo: string
    obrigatorio: true
  - nome: profile_goal
    tipo: "sell | educate | inspire | grow"
    obrigatorio: true
  - nome: primary_avatar
    tipo: string
    obrigatorio: true
  - nome: product_service
    tipo: string
    obrigatorio: false
Saida:
  - nome: pillars
    tipo: "4–5 named content pillars with goal and % of content"
    obrigatorio: true
  - nome: post_ideas
    tipo: "3 post ideas per pillar with suggested format"
    obrigatorio: true
  - nome: profile_rules
    tipo: "Voice tone, prohibited content, ideal frequency per pillar"
    obrigatorio: true
Checklist:
  - Niche, goal, and avatar received before starting
  - Maximum 5 pillars defined (no more)
  - Sale pillar does not exceed 20% of content mix
  - 3 post ideas per pillar with format suggestion
  - Profile rules include tone, prohibitions, and frequency
---

# create-content-pillars

## Description
Defines the profile's content pillars based on niche, goal, and avatar. Delivers the strategic structure that guides all editorial planning.

---

## Required Inputs

| Input | Required |
|-------|----------|
| Niche | Yes |
| Profile goal (sell / educate / inspire / grow) | Yes |
| Primary avatar | Yes |
| Main product or service (if any) | No |

---

## What are Content Pillars

Pillars are the thematic categories that define what the profile talks about. A profile without pillars posts randomly. A profile with pillars builds a qualified audience.

Ideal structure: 4–5 pillars, including:
- 1–2 educational pillars (build authority)
- 1 entertainment/identification pillar (drive engagement)
- 1 behind-the-scenes/personal pillar (build connection)
- 1 sale/offer pillar (generate revenue) — optional, maximum 20% of content

---

## Execution Flow

```
STEP 1 — Avatar analysis
→ What does the avatar want to learn?
→ What does the avatar feel but not say?
→ What does the avatar buy?

STEP 2 — Pillar definition
→ 4–5 named pillars
→ Goal for each pillar
→ Suggested % of content

STEP 3 — Examples per pillar
→ 3 post ideas per pillar
→ Suggested format for each idea

STEP 4 — Profile rules
→ What the profile NEVER posts
→ Standardized voice tone
→ Ideal frequency per pillar
```

---

## Output

```
CONTENT PILLARS — [NICHE] / [PROFILE]
=======================================

PILLAR 1 — [NAME] ([%] of content)
Goal: [what this pillar does for the profile]
Examples:
- [post idea + format]
- [post idea + format]
- [post idea + format]

[repeat for each pillar]

PROFILE RULES:
→ Voice tone: [definition]
→ Never post: [list]
→ Ideal frequency: [posts/week per pillar]
```

---

## Veto Conditions

- Do not define more than 5 pillars — above that, the profile loses focus
- Do not create a sale pillar above 20% of the mix — unbalances the profile
- Do not execute without niche and goal defined

---

## Completion Criteria

- [ ] 4–5 pillars defined with name, goal, and % of content
- [ ] 3 post ideas per pillar with suggested format
- [ ] Profile rules defined (tone, prohibitions, frequency)
