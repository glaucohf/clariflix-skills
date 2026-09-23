# Project Setup Recommendation - Revenue OS Sales App

## Decisao recomendada (projeto real)

Para um projeto real de vendas do Revenue OS, o ideal e iniciar em uma pasta dedicada nova em `/CODE`, nao dentro de `rodrigo-hubs`.

Exemplo recomendado:
- `/Users/rodrigofeldman/CODE/revenue-os-sales`

## Por que pasta dedicada

- isolamento de escopo (produto comercial vs celeiro de ideias)
- repositorio limpo para CI/CD, deploy e auditoria
- controle de versao e rollback mais previsiveis
- menos ruido de arquivos/experimentos paralelos

## Quando usar rodrigo-hubs

Use `rodrigo-hubs` para:
- ideacao
- prototipos curtos
- testes exploratorios

Quando houver validacao de produto, promova para pasta dedicada.

## Estrutura minima sugerida

- `app/` (LP + checkout)
- `ops/` (CRM, automacoes, playbooks)
- `analytics/` (dashboards e definicao de KPI)
- `content/` (criativos e email)
- `docs/` (oferta, ICP, roadmap, runbooks)
