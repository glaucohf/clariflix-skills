# viral-post-anatomy

## Description
Workflow that analyzes a viral post from the user's niche, extracts the structural pattern that made it perform, and replicates it with the user's topic.

---

## Required Inputs

| Input | Required |
|-------|----------|
| Viral post caption (paste the text) | Yes |
| Post metrics (likes, comments, shares — approximate) | Optional |
| Niche | Yes |
| User's topic to replicate | Yes |

---

## Workflow Phases

### Phase 1 — Viral Post Deconstruction
**Agent:** caption-strategist

Analyzes the viral post and identifies:
- Hook type used
- Paragraph structure
- Emotional pattern (which emotion dominates)
- CTA type
- Why it worked (evidence-based hypothesis)

Output: viral post anatomy in structured format.

---

### Phase 2 — Pattern Extraction
**Agent:** caption-strategist

Extracts the replicable pattern:
- Structure template (not the content, the skeleton)
- Angle that generated the engagement
- Implicit rules of the post

Output: extracted pattern template.

---

### Phase 3 — Replication with User's Topic
**Agent:** caption-writer

Applies the extracted pattern to the user's topic.
Delivers 2 variations:
- Variation A: faithful to the original pattern
- Variation B: pattern adapted with the user's niche twist

**Checkpoint:** Present Variation A and B to the user before generating hashtags.
If the user rejects the replication, stop here without proceeding.

---

### Phase 4 — Hashtags
**Agent:** hashtag-researcher

Generates hashtags for the replicated post.

---

## Output

```
VIRAL POST ANATOMY — [ORIGINAL THEME]
=======================================

VIRAL POST ANATOMY:
→ Hook type: [type]
→ Structure: [skeleton]
→ Dominant emotion: [emotion]
→ CTA: [type]
→ Why it worked: [hypothesis]

EXTRACTED PATTERN:
→ [line 1: structure]
→ [line 2: structure]
→ [...]

REPLICATION — TOPIC: [USER'S TOPIC]
=====================================
Variation A (faithful to pattern):
[full caption]

Variation B (adapted pattern):
[full caption]

HASHTAGS:
[full set]
```

---

## Veto Conditions

- Do not copy the content — copy the structural pattern
- Do not execute without the original viral post — no reference input = no real analysis
- Make it clear to the user that the replication is of the pattern, not the text
