# Coding Standards — Brain Squad

## Naming Conventions

Seguir estritamente as regras de `shared/macros.md` {{NAMING_RULES}}.

| Elemento | Convencao | Exemplo |
|----------|-----------|---------|
| Agent ID | kebab-case | `filter-ranker` |
| Agent name | PascalCase | `FilterRanker` |
| Task ID | camelCase() | `filterAndRank()` |
| Task file | kebab-case.md | `filter-and-rank.md` |
| Workflow name | snake_case | `brain_pipeline` |
| Commands | `*kebab-case` | `*filter-rank-r1` |

## File Organization

- Um agente por arquivo em `agents/`
- Uma task por arquivo em `tasks/`
- Workflows em `workflows/`
- Regras compartilhadas em `shared/macros.md` (ler uma vez, referenciar)

## YAML Standards

- Indentacao: 2 espacos (sem tabs)
- Strings com caracteres especiais entre aspas
- Sem Norway Problem (bare yes/no)

## File Contracts

- Todos os dados intermediarios passam por `.brainstorm-tmp/`
- Agentes geradores retornam apenas "Done"
- Resultados estruturados em JSON (top10.json, top3.json)

## Model Routing

- Haiku: geracao de itens (output previsivel, baixo custo)
- Sonnet: filtragem, ranking, sintese (raciocinio moderado)
- Opus: orquestracao, facilitacao de design (raciocinio profundo)
