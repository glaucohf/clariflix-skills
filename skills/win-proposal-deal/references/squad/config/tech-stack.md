# Tech Stack — DealForge

## Runtime
- **Node.js** 20+ (LTS)

## AI / LLM
- **Claude API** (Sonnet/Opus) for prospect analysis, scope design and proposal composition
- **OpenAI API** (optional) for second-opinion scoring and win-rate validation

## Data Processing
- **JSON** for inter-agent communication and structured output
- **Markdown** for proposal composition and human-readable deliverables
- **zod** for schema validation

## Development
- **TypeScript** — Type safety for complex data pipelines
- **ESLint** + **Prettier** — Code formatting
- **Vitest** — Testing framework

## Output Formats
- Markdown (primary proposal format)
- JSON (machine-readable pipeline data)
- PDF (final client-facing deliverable via conversion)
