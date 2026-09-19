# DealForge

### Proposals that close. In minutes, not days.

<br>

> _"While you're building proposals in Google Docs, your competitor already sent a personalized one."_

<br>

Your sales team loses deals because of slow turnaround, gut-feel pricing, and generic proposals that convince no one. DealForge is a squad of 4 AI agents that transforms raw prospect data into a **complete, persuasive commercial proposal with win-rate prediction** — all before your coffee gets cold.

## Installation

```bash
npx squads add Renat0z/squads-sh-aios/proposal-engine
```

## Why your agency loses deals

| Symptom | Consequence |
|---------|-------------|
| Proposals take **days** | Prospect goes cold, competitor gets there first |
| Pricing is **guesswork** | Overcharge and lose, or undercharge and bleed margin |
| **Copy-paste** scope | Generic proposals that don't speak the prospect's language |
| Objections catch you **off guard** | "Too expensive", "need to think" — and you have no answer |
| **Zero visibility** on win-rate | No idea if you have 30% or 80% chance before hitting send |

## How DealForge solves it

```
Prospect data ──▶ [ DealForge ] ──▶ Ready proposal + Predicted Win-Rate
```

The pipeline runs through **4 specialized agents**, each owning a critical stage:

### 1. Prospect X-Ray
**ProspectAnalyzer** dives into the data — company, industry, budget, pain points, history — and delivers a complete map of opportunities and risks.

### 2. Scope in 3 Versions
**ScopeArchitect** designs three strategic options — Essential, Recommended, and Premium — with price anchoring that guides the prospect toward the ideal version.

### 3. Smart Pricing
**PricingStrategist** calculates the optimal price: healthy margin x maximum win-rate. No more guesswork.

### 4. Killer Proposal
**ProposalComposer** brings it all together into a persuasive proposal with personalized copy, pre-handled objections, and a strategic CTA.

**Result:** professional proposal in minutes, with approval rate prediction.

## Squad

| | Agent | Archetype | What it does |
|---|-------|-----------|-------------|
| 🔍 | **ProspectAnalyzer** | Guardian | Analyzes prospect, history and maps pain points/objections |
| 📐 | **ScopeArchitect** | Builder | Designs scope in 3 versions with timeline and milestones |
| 💰 | **PricingStrategist** | Balancer | Prices with optimized margin and predictive win-rate |
| 📝 | **ProposalComposer** | Flow_Master | Composes persuasive proposal with objection handling |

## Workflows

### `proposal_generation_pipeline` — Full pipeline
From zero to final proposal in one command.
```
[ProspectAnalyzer] → [ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

### `proposal_revision_flow` — Quick revision
Adjusts existing proposal based on prospect feedback.
```
[ScopeArchitect] → [PricingStrategist] → [ProposalComposer]
```

## Usage

```bash
# Full pipeline — from prospect to final proposal
/SQUADS:pe:prospect-analyzer

# Or use individual agents
/SQUADS:pe:prospect-analyzer     # Prospect x-ray
/SQUADS:pe:scope-architect       # Scope design
/SQUADS:pe:pricing-strategist    # Strategic pricing
/SQUADS:pe:proposal-composer     # Proposal composition
```

## Tasks

| Task | Owner | Layer |
|------|-------|-------|
| `analyzeProspect()` | ProspectAnalyzer | Organism |
| `designScope()` | ScopeArchitect | Organism |
| `calculatePricing()` | PricingStrategist | Organism |
| `composeProposal()` | ProposalComposer | Organism |

## Author

**Renato Medeiros** ([@Renat0z](https://github.com/Renat0z))

## License

MIT
