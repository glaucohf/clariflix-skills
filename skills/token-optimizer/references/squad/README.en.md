<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**Analyzes existing AIOS squads and produces ROI-prioritized optimizations — quality, speed, and token savings.**

Sequential 5-agent pipeline that scans, detects anti-patterns, plans, executes, and audits optimizations using TOKEN-OPTIMIZATION-GUIDE.md as its knowledge base.

`/sqopt`

</div>

---

## Is your squad burning 10x more tokens than it should?

You built a working squad. It runs, delivers results, solves the problem. But every execution costs **$0.28** and you know half those tokens are wasted on redundant prompts, verbose returns nobody reads, and Opus doing Haiku's job.

The worst part? You don't know **where** the bottlenecks are. Dozens of files, multiple agents, chained workflows — each one hiding anti-patterns invisible to the naked eye. Context Bloat, Double-Read, Ghost Tokens, Model Overkill. The cost piles up silently, execution after execution.

What if I told you that **12 proven techniques** can cut your cost by up to 78%, boost output quality by 34%, and all of it can be applied automatically — without breaking anything?

---

## The Before and After

| | Without Optimization | With token-optimizer |
|---|---|---|
| **Opus Tokens** | 100% | 2-5% (Router Puro) |
| **Cost per execution** | $0.28 | $0.06 (-78%) |
| **Output quality** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns detected** | 0 | 100% cataloged |

---

## How It Works

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

The full pipeline runs through 5 sequential phases. Each agent reads the previous agent's output via file (Files as Contracts), returns only `"Done: {path}"` to the orchestrator, and the next agent picks up where the last one left off. Zero tokens wasted on transitions.

---

## Why token-optimizer?

- **12 proven techniques** — No guesswork. Every optimization maps to a numbered section in TOKEN-OPTIMIZATION-GUIDE.md, with technical rationale and documented impact metrics.

- **ROI-first prioritization** — Quality first, speed second, cost third. The planner ranks actions by highest real return, not the easiest cut. You improve output before slashing costs.

- **Automatic detection of 10+ anti-patterns** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — each scored by severity 1-10 with estimated wasted tokens.

- **Audit-only mode** — Want a diagnosis without touching any files? The `squad_audit_only` workflow scans, detects, and reports — zero changes, full visibility.

---

## Agents

| | Name | Archetype | Role |
|---|---|---|---|
| | **SquadScanner** | Guardian | Reads and catalogs a target squad's full structure, producing a structured inventory |
| | **AntiPatternDetector** | Guardian | Identifies token anti-patterns with severity scores and estimated impact |
| | **OptimizationPlanner** | Balancer | Creates an ROI-prioritized optimization plan mapping anti-patterns to proven techniques |
| | **OptimizationExecutor** | Builder | Executes the plan, rewriting optimized versions of the squad's files |
| | **QualityAuditor** | Guardian | Validates the optimized squad, compares before/after metrics, and ensures AIOS compliance |

---

## Tasks

| Task | Responsible Agent | Atomic Layer |
|---|---|---|
| `scanSquad()` | SquadScanner | Scans target squad and produces squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | Cross-references inventory against the guide's anti-pattern list |
| `planOptimization()` | OptimizationPlanner | Generates ROI-prioritized plan with atomic actions |
| `executeOptimization()` | OptimizationExecutor | Applies optimizations and outputs files to optimized/ |
| `auditQuality()` | QualityAuditor | Validates AIOS compliance and produces before/after report |

---

## Workflows

| Name | Pattern | Description |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | Full pipeline: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | Quick audit: scan, detect, audit — no file modifications |

---

## Commands

| Command | What it does |
|---|---|
| `/sqopt` | Starts the interactive pipeline with configuration collection |
| `/sqopt:run` | Direct execution without questions |
| `*sqopt-scan` | Scans target squad and produces JSON inventory |
| `*sqopt-detect` | Detects anti-patterns and produces severity report |
| `*sqopt-plan` | Generates ROI-prioritized optimization plan |
| `*sqopt-execute` | Applies planned optimizations to squad files |
| `*sqopt-audit` | Audits optimized squad and generates metrics report |

---

## Tech Stack

| Technology | Usage |
|---|---|
| **Claude Code Agent Teams** | Multi-agent orchestration with Haiku/Sonnet/Opus routing |
| **AIOS 2.1+** | Squad framework — standard format for agents, tasks, workflows |
| **Markdown/YAML** | Agent, task, workflow, and configuration definitions |
| **JSON** | Files as Contracts — inter-agent communication via structured files |

---

<details>
<summary><strong>FAQ</strong></summary>

### Does it work with any squad?

Yes. token-optimizer analyzes any squad in standard AIOS format. Just point it to the directory path and the scanner automatically catalogs all agents, tasks, workflows, and configs. Domain doesn't matter — if it follows the AIOS format, it can be optimized.

### Does it modify my files?

Depends on the mode. In the full pipeline (`squad_optimization_pipeline`), the executor generates optimized versions in a separate `optimized/` directory — your originals are never overwritten. In `squad_audit_only` mode, it's 100% read-only: diagnosis and report only, zero changes.

### How much does it save?

Between 65% and 98% token reduction, depending on the anti-patterns found. The most common case — squads with Model Overkill and Context Bloat — typically sees a 78% reduction in cost per execution. The QualityAuditor's final report shows detailed before/after projections for tokens, cost, and latency.

</details>

---

<div align="center">

**Created by [NSCL Pipeline](https://github.com/nscl-pipeline)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>
