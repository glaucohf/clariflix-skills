# Claude Code Mastery Squad -- Architecture

## 1. Three-Tier Architecture

```
                        ┌─────────────────────────────────┐
                        │         TIER 0: DIAGNOSIS        │
                        │      & ROUTING                   │
                        │                                  │
                        │   Orion (claude-mastery-chief)   │
                        │   Triage + Route + Cross-cutting │
                        └──────────┬──────────────────────┘
                                   │
               ┌───────────────────┼───────────────────────┐
               │                   │                       │
    ┌──────────▼──────────┐  ┌─────▼──────────┐  ┌────────▼──────────┐
    │    TIER 1: CORE     │  │   TIER 1: CORE │  │   TIER 1: CORE    │
    │     MASTERY         │  │    MASTERY     │  │    MASTERY        │
    │                     │  │                │  │                   │
    │ Latch    Piper      │  │ Nexus          │  │ Sigil             │
    │ (hooks)  (mcp)      │  │ (swarm)        │  │ (config)          │
    └─────────────────────┘  └────────────────┘  └───────────────────┘

    ┌──────────────────────────────────────────────────────────────────┐
    │              TIER 2: STRATEGIC & CONTEXT                        │
    │                                                                  │
    │  Anvil (skill-craftsman)   Conduit (project-integrator)         │
    │  Vigil (roadmap-sentinel)                                       │
    └──────────────────────────────────────────────────────────────────┘
```

**Tier 0 -- Diagnosis & Routing**
- Agent: `claude-mastery-chief` (Orion)
- Purpose: Triage requests, provide quick answers, route to specialists
- Handles cross-cutting questions directly

**Tier 1 -- Core Mastery**
- `hooks-architect` (Latch) -- Hooks, lifecycle events, automation pipelines
- `mcp-integrator` (Piper) -- MCP servers, tool composition, context budget
- `swarm-orchestrator` (Nexus) -- Subagents, agent teams, parallel execution
- `config-engineer` (Sigil) -- Settings, permissions, CLAUDE.md, sandbox

**Tier 2 -- Strategic & Context**
- `skill-craftsman` (Anvil) -- Skills, plugins, commands, context engineering
- `project-integrator` (Conduit) -- Project setup, CI/CD, brownfield integration
- `roadmap-sentinel` (Vigil) -- Changelog, feature adoption, plan-first methodology

---

## 2. Handoff Matrix

```
FROM \ TO              Orion  Latch  Piper  Nexus  Sigil  Anvil  Conduit  Vigil
──────────────────────────────────────────────────────────────────────────────────
Orion (chief)            --    route  route  route  route  route  route    route
Latch (hooks)          escal    --     .      .    collab  collab   .       .
Piper (mcp)            escal    .      --     .      .      .    collab     .
Nexus (swarm)          escal  collab   .      --   collab   .      .       .
Sigil (config)         escal  collab   .      .      --   collab  collab    .
Anvil (skills)         escal  collab   .      .    collab   --      .       .
Conduit (integration)  escal    .    collab   .    collab   .      --     collab
Vigil (roadmap)        escal    .      .      .      .      .    collab    --
```

**Legend:** `route` = Orion routes to specialist. `collab` = peer collaboration. `escal` = escalates back to Orion.

**Routing:** Orion routes to all 7 specialists based on keyword matching.
**Collaboration:** Specialists collaborate laterally on cross-domain tasks.
**Escalation:** All specialists escalate unresolved or ambiguous requests back to Orion.

---

## 3. AIOX-Core Bridge

This squad bridges Claude Code native features with the AIOX meta-framework.

| AIOX Concept | Claude Code Equivalent | Bridge Agent |
|---|---|---|
| Agents (`@dev`, `@qa`, etc.) | Subagents (`.claude/agents/*.md`) | Nexus |
| Tasks (`.aiox-core/development/tasks/`) | Skills (`.claude/skills/*/SKILL.md`) | Anvil |
| Workflows (multi-step sequences) | Multi-step sessions / command chains | Conduit |
| `core-config.yaml` | `.claude/settings.json` hierarchy | Sigil |
| Python hooks (`.aiox-core/monitor/hooks/`) | Native hooks (command/http/prompt/agent) | Latch |
| Quality gates (L1-L4 layers) | Hook-based validation (PreToolUse, Stop) | Latch + Sigil |
| Entity registry (740+ entities) | Tool Search + MCP server discovery | Piper |

**How the bridge works:**

1. AIOX agents map to Claude Code subagents via `.claude/agents/` markdown files with YAML frontmatter. Nexus handles the topology and coordination patterns.

2. AIOX tasks map to Claude Code skills. Anvil provides `*convert-task-to-skill` to automate the translation from task YAML to SKILL.md format.

3. AIOX workflows map to multi-step Claude Code sessions. Conduit designs integration patterns that compose skills, commands, and hooks into coherent workflows.

4. AIOX `core-config.yaml` settings have equivalents in the `.claude/settings.json` hierarchy. Sigil manages the mapping and ensures configurations are at the correct scope (managed > user > project > local).

5. AIOX Python hooks in `.aiox-core/monitor/hooks/` complement Claude Code's native hook system. Latch ensures new hooks do not duplicate existing AIOX monitoring hooks and follows the `enrich_event()` + `send_event()` pattern.

6. AIOX quality gates (L1-L4 boundary protection) are enforced through deny/allow rules in `.claude/settings.json`. Sigil configures boundary protection; Latch designs PreToolUse hooks for runtime enforcement.

7. AIOX entity registry capabilities are replaced by Claude Code's ToolSearch for on-demand tool discovery and MCP server catalogs. Piper manages the tool composition strategy.

---

## 4. Feature Coverage Map

| Claude Code Feature | Events / Scope | Primary Agent | Secondary |
|---|---|---|---|
| **Hooks** (17 lifecycle events) | SessionStart, SessionEnd, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, Notification, SubagentStart, SubagentStop, Stop, TeammateIdle, TaskCompleted, ConfigChange, WorktreeCreate, WorktreeRemove, PreCompact | Latch | Sigil (scope) |
| **MCP Integration** | stdio, HTTP Streamable, SSE transports; 200+ servers; Tool Search | Piper | Conduit (project) |
| **Subagents & Teams** | Agent tool, Agent Teams, worktree isolation, parallel execution | Nexus | Latch (hooks for teams) |
| **Settings & Permissions** | 5-layer hierarchy, allow/ask/deny rules, sandbox, managed policies | Sigil | Conduit (project setup) |
| **Skills & Plugins** | SKILL.md, .claude/commands/, .claude-plugin/, marketplace | Anvil | Sigil (config) |
| **Project Integration** | CLAUDE.md, .claude/rules/, CI/CD headless, brownfield, git workflow | Conduit | Sigil (settings) |
| **Roadmap & Updates** | Changelog, feature radar, version tracking, plan-first methodology | Vigil | Conduit (adoption) |

---

## 5. Routing Algorithm

Orion classifies incoming requests using a keyword-matching routing matrix.

```
User Request
     |
     v
+------------------+
| Extract Keywords |
| from request     |
+------------------+
     |
     v
+--------------------+
| Match against      |
| routing_matrix:    |
|                    |
| hooks keywords --> Latch     (hook, pre_tool_use, lifecycle, intercept, block, exit code...)
| mcp keywords ----> Piper     (mcp, server, tool search, stdio, sse, context7, exa...)
| subagent kw -----> Nexus     (subagent, team, swarm, teammate, worktree, parallel...)
| config keywords -> Sigil     (settings, permission, CLAUDE.md, rules, sandbox, managed...)
| skills keywords -> Anvil     (skill, command, plugin, SKILL.md, context engineering...)
| integration kw --> Conduit   (integrate, repository, CI/CD, headless, brownfield...)
| roadmap keywords-> Vigil     (update, changelog, version, roadmap, migration, upgrade...)
+--------------------+
     |
     +-------+-------+
     |               |
     v               v
Cross-cutting    Domain-specific
(no match or     (keyword match)
 multi-domain)
     |               |
     v               v
Answer directly  Quick answer
from quick_ref   + route to
                 specialist
```

**Decision rules:**

1. If keywords match a single domain with high confidence, route to that specialist.
2. If keywords match multiple domains, Orion provides a synthesized answer and suggests the most relevant specialist.
3. If no domain match, Orion answers directly from the quick reference knowledge base.
4. Cross-cutting questions (how features relate, AIOX overview, comparison questions) are always answered directly by Orion.

---

## 6. Quality Standards

```yaml
quality_standards:
  voice_dna_required: true      # Every specialist must have voice_dna with tone + signature_phrases
  thinking_dna_required: true   # Every specialist must have thinking_dna with decision framework
  min_score: 7.0                # Minimum quality score for squad activation (out of 10)
  smoke_tests: 3                # Number of smoke test queries per agent
```

**Voice DNA:** Defines each agent's communication personality -- tone, vocabulary, signature phrases, and anti-patterns. Ensures consistent, recognizable agent identity.

**Thinking DNA:** Defines each agent's decision-making framework -- heuristics, evaluation criteria, and quality gates. Ensures systematic, reproducible reasoning.

**Orchestrator exception:** The orchestrator (Orion) has minimal voice_dna (tone + 2-3 routing phrases) and no thinking_dna. The orchestrator's role is to route, not to reason deeply about domain-specific problems.

---

*Claude Code Mastery Squad v1.0 -- Architecture Document*
