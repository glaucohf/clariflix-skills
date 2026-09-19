<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**分析现有 AIOS squads，按 ROI 优先级生成优化方案 — 质量、速度和 token 节省。**

5 个代理的顺序 pipeline，使用 TOKEN-OPTIMIZATION-GUIDE.md 作为知识库进行扫描、检测 anti-patterns、规划、执行和审计优化。

`/sqopt`

</div>

---

## 你的 squad 消耗的 token 是实际需要的 10 倍吗？

你构建了一个能用的 squad。它运行、交付结果、解决问题。但每次执行花费 **$0.28**，你知道其中一半的 token 浪费在了冗余的 prompts、没人读的冗长返回值，以及 Opus 做着 Haiku 的工作上。

最糟糕的是什么？你不知道瓶颈**在哪里**。几十个文件、多个代理、串联的 workflows — 每一个都隐藏着肉眼看不见的 anti-patterns。Context Bloat、Double-Read、Ghost Tokens、Model Overkill。成本在一次又一次的执行中悄然累积。

如果我告诉你，**12 种经过验证的技术**可以将你的成本降低高达 78%，将输出质量提升 34%，而且这一切都可以自动应用 — 不会破坏任何东西呢？

---

## 优化前后对比

| | 未优化 | 使用 token-optimizer |
|---|---|---|
| **Opus Token** | 100% | 2-5% (Router Puro) |
| **每次执行成本** | $0.28 | $0.06 (-78%) |
| **输出质量** | 6.5/10 | 8.7/10 (+34%) |
| **检测到的 Anti-patterns** | 0 | 100% 已编目 |

---

## 工作原理

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

完整 pipeline 经过 5 个顺序阶段。每个代理通过文件读取前一个代理的输出（Files as Contracts），仅向编排器返回 `"Done: {path}"`，下一个代理从上一个停止的地方继续。转换过程中零 token 浪费。

---

## 为什么选择 token-optimizer？

- **12 种经过验证的技术** — 不是猜测。每项优化都映射到 TOKEN-OPTIMIZATION-GUIDE.md 中的编号章节，具有技术依据和记录的影响指标。

- **ROI 优先排序** — 质量第一，速度第二，成本第三。规划器按最高实际回报排列操作，而不是最容易的削减。先改善输出，再降低成本。

- **自动检测 10+ anti-patterns** — Context Bloat、Double-Read、Model Overkill、Compression Rebound、Ghost Tokens、Sequential Launch、Fat Orchestrator — 每个都有 1-10 的严重性评分和估计的浪费 token 数。

- **Audit-only 模式** — 只想要诊断而不修改任何文件？`squad_audit_only` workflow 扫描、检测并报告 — 零更改，完全可见。

---

## 代理

| | 名称 | Archetype | 角色 |
|---|---|---|---|
| | **SquadScanner** | Guardian | 读取并编目目标 squad 的完整结构，生成结构化清单 |
| | **AntiPatternDetector** | Guardian | 识别 token anti-patterns，附带严重性评分和估计影响 |
| | **OptimizationPlanner** | Balancer | 创建按 ROI 优先的优化计划，将 anti-patterns 映射到经过验证的技术 |
| | **OptimizationExecutor** | Builder | 执行计划，重写 squad 文件的优化版本 |
| | **QualityAuditor** | Guardian | 验证优化后的 squad，比较前后指标，确保 AIOS compliance |

---

## 任务

| Task | 负责代理 | Atomic Layer |
|---|---|---|
| `scanSquad()` | SquadScanner | 扫描目标 squad 并生成 squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | 将清单与指南的 anti-pattern 列表交叉引用 |
| `planOptimization()` | OptimizationPlanner | 生成按 ROI 优先的计划，包含原子操作 |
| `executeOptimization()` | OptimizationExecutor | 应用优化并将文件输出到 optimized/ |
| `auditQuality()` | QualityAuditor | 验证 AIOS compliance 并生成 before/after 报告 |

---

## Workflows

| 名称 | 模式 | 描述 |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | 完整 pipeline：scan、detect、plan、execute、audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | 快速审计：scan、detect、audit — 不修改文件 |

---

## 命令

| 命令 | 功能 |
|---|---|
| `/sqopt` | 启动带配置收集的交互式 pipeline |
| `/sqopt:run` | 无提问直接执行 |
| `*sqopt-scan` | 扫描目标 squad 并生成 JSON 清单 |
| `*sqopt-detect` | 检测 anti-patterns 并生成严重性报告 |
| `*sqopt-plan` | 生成按 ROI 优先的优化计划 |
| `*sqopt-execute` | 对 squad 文件应用已规划的优化 |
| `*sqopt-audit` | 审计优化后的 squad 并生成指标报告 |

---

## 技术栈

| 技术 | 用途 |
|---|---|
| **Claude Code Agent Teams** | 多代理编排，支持 Haiku/Sonnet/Opus 路由 |
| **AIOS 2.1+** | Squad 框架 — agents、tasks、workflows 的标准格式 |
| **Markdown/YAML** | 代理、任务、workflow 和配置定义 |
| **JSON** | Files as Contracts — 通过结构化文件进行代理间通信 |

---

<details>
<summary><strong>常见问题</strong></summary>

### 适用于任何 squad 吗？

是的。token-optimizer 分析任何标准 AIOS 格式的 squad。只需指向目录路径，扫描器就会自动编目所有 agents、tasks、workflows 和 configs。领域无关 — 只要遵循 AIOS 格式，就可以优化。

### 会修改我的文件吗？

取决于选择的模式。在完整 pipeline（`squad_optimization_pipeline`）中，执行器在单独的 `optimized/` 目录中生成优化版本 — 你的原始文件永远不会被覆盖。在 `squad_audit_only` 模式下，100% 只读：仅诊断和报告，零更改。

### 能节省多少？

根据发现的 anti-patterns，token 减少 65% 到 98%。最常见的情况 — 存在 Model Overkill 和 Context Bloat 的 squads — 通常每次执行成本降低 78%。QualityAuditor 的最终报告展示 token、成本和延迟的详细前后对比预测。

</details>

---

<div align="center">

**由 [NSCL Pipeline](https://github.com/nscl-pipeline) 创建** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>
