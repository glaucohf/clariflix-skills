# Coding Standards — token-optimizer

## Convencoes de nomenclatura
- Agent IDs: kebab-case (`squad-scanner`, `anti-pattern-detector`)
- Agent names: PascalCase (`SquadScanner`, `AntiPatternDetector`)
- Task identifiers: camelCase() (`scanSquad()`, `detectAntiPatterns()`)
- Workflow names: snake_case (`squad_optimization_pipeline`)
- Campos Entrada/Saida: camelCase (`squadPath`, `antiPatternsReport`)
- Comandos: `*sqopt-{action}` com prefixo do squad

## Arquivos de saida intermediarios
- Formato: JSON para dados estruturados, Markdown para relatorios
- Naming: kebab-case (`squad-inventory.json`, `anti-patterns-report.json`)
- Local: diretorio de trabalho temporario (`.sqopt-tmp/`)

## Principios de design
1. **Router Puro** — orquestrador nunca gera, nunca le outputs brutos
2. **Files as Contracts** — comunicacao inter-agente exclusivamente via filesystem
3. **Retornos Minimos** — agentes retornam "Done: {path}" ao orquestrador
4. **Ler 1x, Usar N** — Single Source of Truth, zero re-reads
