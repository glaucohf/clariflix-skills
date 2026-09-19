# DealForge

### 能成交的提案。几分钟，不是几天。

<br>

> _"当你还在Google Docs里拼提案时，竞争对手已经发出了个性化方案。"_

<br>

你的销售团队因为速度慢、凭感觉定价、千篇一律的提案而丢单。DealForge 是一个由 4 个 AI 代理组成的团队，将原始客户数据转化为**完整的、有说服力的商业提案，并附有成交率预测** — 一切在你的咖啡变凉之前完成。

## 安装

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## 你的机构为什么丢单

| 症状 | 后果 |
|------|------|
| 提案需要**好几天** | 客户冷却，竞争对手抢先 |
| 定价靠**感觉** | 要价太高失去客户，太低损失利润 |
| **复制粘贴**范围 | 千篇一律的提案，不针对客户需求 |
| 异议来得**措手不及** | "太贵了"、"要考虑" — 你却没有答案 |
| 成交率**完全不可见** | 发送前不知道是30%还是80%的机会 |

## DealForge 如何解决

```
客户数据 ──▶ [ DealForge ] ──▶ 成品提案 + 预测成交率
```

流水线经过 **4 个专业代理**，每个负责一个关键阶段：

### 1. 客户透视
**ProspectAnalyzer** 深入数据 — 公司、行业、预算、痛点、历史 — 交付完整的机会与风险地图。

### 2. 三版本范围
**ScopeArchitect** 设计三个战略选项 — 基础版、推荐版、高级版 — 利用价格锚定引导客户选择最佳版本。

### 3. 智能定价
**PricingStrategist** 计算最优价格：健康利润率 x 最大成交率。告别拍脑袋。

### 4. 杀手级提案
**ProposalComposer** 将一切整合为有说服力的提案 — 个性化文案、预判异议、战略性行动号召。

**结果：** 几分钟内生成专业提案，附有批准率预测。

## 团队

| | 代理 | 原型 | 职责 |
|---|------|------|------|
| 🔍 | **ProspectAnalyzer** | Guardian | 分析客户、历史，映射痛点和异议 |
| 📐 | **ScopeArchitect** | Builder | 设计3版本范围，含时间线和里程碑 |
| 💰 | **PricingStrategist** | Balancer | 以优化利润率和预测性成交率定价 |
| 📝 | **ProposalComposer** | Flow_Master | 撰写有说服力的提案，处理异议 |

## 工作流

### `proposal_generation_pipeline` — 完整流水线
一个命令，从零到最终提案。
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — 快速修订
根据客户反馈调整现有提案。
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## 使用方法

```bash
# 完整流水线 — 从客户到最终提案
/SQUADS:pe:prospect-analyzer

# 或使用单个代理
/SQUADS:pe:prospect-analyzer     # 客户透视
/SQUADS:pe:scope-architect       # 范围设计
/SQUADS:pe:pricing-strategist    # 战略定价
/SQUADS:pe:proposal-composer     # 提案撰写
```

## 任务

| 任务 | 负责人 | 层级 |
|------|--------|------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## 作者

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## 许可证

MIT
