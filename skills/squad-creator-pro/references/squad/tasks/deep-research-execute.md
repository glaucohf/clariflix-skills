# Task: Execute Deep Research

## Task Anatomy

| Field | Value |
|-------|-------|
| **Task ID** | `deep-research-execute` |
| **Version** | `1.0.0` |
| **Status** | `active` |
| **Responsible Executor** | `squad-chief` |
| **Execution Type** | `agent` |

## Metadata

| Key | Value |
|-----|-------|
| **Model** | Opus |
| **Haiku Eligible** | NO |
| **Parent Task** | `deep-research-pre-agent` (stub) |
| **Phase** | 3 of 4 |
| **Created** | 2026-03-26 |
| **Part of** | squads/squad-creator-pro |

## Purpose

Execute the research plan generated in Phase 2 by processing local knowledge, running web research queries, and consolidating all findings into a comprehensive research document. This is the core execution phase that produces the primary research artifact.

## Prerequisites

- Research prompt from Phase 2 (all 7 components)
- Local catalog from Phase 1 (if specialist exists)
- WebSearch and WebFetch tools available

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `research_prompt` | structured text | Yes | 7-component prompt from Phase 2 |
| `local_catalog` | YAML | No | From Phase 1 (files found, gaps) |
| `specialist_slug` | string | No | For file naming and local file lookup |
| `specialist_name` | string | No | For query construction |
| `activity` | string | Yes | For file naming and query construction |
| `agent_purpose` | string | Yes | For relevance filtering |
| `domain` | string | Yes | For query construction |
| `retry_count` | integer | No | Current retry attempt (0-2), default 0 |

## Workflow / Steps

### Step 3.1: Process Local Knowledge

**Condition:** Only if local files exist from Phase 1.

```yaml
if local_files exist:
  for each file:
    - Read complete file
    - Extract sections relevant to agent_purpose
    - Note key quotes and frameworks
    - Mark what's covered vs gaps

  output: local_synthesis.md
```

### Step 3.2: Execute Web Research

Run structured queries and extract content from results:

```yaml
research_queries:
  - "{specialist_name} {activity} methodology framework"
  - "{specialist_name} {activity} process steps how-to"
  - "{specialist_name} {activity} examples case studies"
  - "{specialist_name} best practices rules principles"
  - "{activity} {domain} expert techniques"

for each query:
  - WebSearch(query)
  - For top 5-8 results:
      - WebFetch(url)
      - Extract relevant content
      - Note source URL for citation

  output: web_findings.md
```

When `specialist_name` is null, adjust queries to use domain-generic formulations (e.g., `"{activity} {domain} expert techniques best practices"`).

### Step 3.3: Consolidate Research

Merge all findings into a single structured document:

```yaml
consolidation:
  - Merge: local_synthesis + web_findings
  - Remove duplicates
  - Organize by scope sections (from research prompt)
  - Add citations throughout
  - Format as comprehensive document

output: docs/research/{specialist_slug}-{activity}-research.md
```

If no specialist, use `{domain}-{activity}-research.md` as filename.

## Output

### Research Document Structure

The output document MUST contain these sections in order:

1. **Header** -- Title, date, agent_purpose, domain, specialist
2. **Executive Summary** -- 2-3 paragraph overview of findings
3. **Scope Sections (1-6)** -- One per scope angle from the prompt, each containing:
   - Key Findings (organized by sub-points)
   - Primary Evidence (quotes with source/year)
   - Extracted Framework (structured, not prose)
4. **Consolidated Framework** -- Principles (cited), Process (steps), Structure/Anatomy (table), Quality Criteria (excellent vs weak), Checklist (actionable checks)
5. **Sources** -- Numbered list with URLs where available
6. **Research Metadata** -- Total lines, local/web source percentages, primary evidence count, quality score

## Acceptance Criteria

- [ ] Local knowledge processed first (if specialist with local files)
- [ ] At least 5 web queries executed
- [ ] Top 5-8 results fetched per query
- [ ] All content has source attribution (URL or file path)
- [ ] Research document organized by scope sections from prompt
- [ ] Document includes Executive Summary
- [ ] Document includes Consolidated Framework section
- [ ] Document includes Sources section with URLs
- [ ] Document includes Research Metadata
- [ ] Output written to `docs/research/{slug}-{activity}-research.md`

## Veto Conditions

| ID | Condition | Check | Result |
|----|-----------|-------|--------|
| VETO-DRE-001 | Existing research document at target path must be backed up before overwrite | Check if `docs/research/{slug}-{activity}-research.md` already exists | VETO - BLOCK. Create backup or rename existing file before writing new output. |

## Error Handling

| Scenario | Action |
|----------|--------|
| No local knowledge found | Continue with web-only research |
| WebSearch returns few results | Try alternative query formulations |
| Specialist not in MMOS | Treat as comprehensive research (web-only) |

## Related Documents

| Document | Relationship |
|----------|-------------|
| `deep-research-pre-agent.md` | Parent stub (orchestrator) |
| `deep-research-check-local-knowledge.md` | Phase 1 (provides local catalog) |
| `deep-research-generate-prompt.md` | Phase 2 (provides research prompt) |
| `deep-research-validate.md` | Next phase (Phase 4) -- validates this output |
| `docs/research/david-ogilvy-research-engineering-meta-framework.md` | Gold standard (1,179 lines) |
