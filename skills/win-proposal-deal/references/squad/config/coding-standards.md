# Coding Standards — DealForge

## Language & Runtime
- **Runtime:** Node.js 20+
- **Language:** TypeScript preferred, JavaScript accepted
- **Module system:** ESM (import/export)

## Code Style
- Use `const` by default, `let` only when reassignment is needed
- Async/await over raw Promises
- Descriptive variable names: `prospectProfile` not `pp`
- Functions should do one thing and do it well

## Data Formats
- All inter-agent communication uses JSON
- Prospect objects follow: `{ company, industry, budget, painPoints, history, objections }`
- Scope objects follow: `{ version, deliverables, timeline, milestones, hours, complexity }`
- Pricing objects follow: `{ version, cost, price, margin, winRate, discounts }`
- Proposal objects follow: `{ sections[], metadata, winRate, validUntil }`
- Timestamps in ISO 8601 format

## Error Handling
- Every async operation must have error handling
- Use structured error objects: `{ code, message, agent, recoverable }`
- Log all errors to execution log

## Naming Conventions
- Files: kebab-case (`analyze-prospect.js`)
- Functions: camelCase (`analyzeProspect()`)
- Classes: PascalCase (`ProspectAnalyzer`)
- Constants: UPPER_SNAKE_CASE (`MIN_MARGIN_PERCENT`)
- Agent IDs: kebab-case (`prospect-analyzer`)

## Output Standards
- All deliverables include metadata: timestamp, agent, version, execution time
- Pricing tables always show 3 versions side by side
- Win-rate predictions include confidence interval
