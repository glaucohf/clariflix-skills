# Coding Standards - Flywheel Core

Este documento define as convenções de código e documentação para o enxame Flywheel.

## Princípios Gerais
- **Plan First:** Nenhuma implementação deve ocorrer sem um plano estratégico aprovado no `PLAN_SPACE.md`.
- **Bead-Driven Development:** Todo trabalho deve ser decomposto em Beads granulares no `BEADS.md`.
- **Test Obligations:** Cada Bead deve incluir explicitamente os critérios de aceitação e as obrigações de teste.
- **No Slop:** Evite código redundante, "just-in-case" ou improvisações arquiteturais.

## Naming Conventions
- **Files:** kebab-case (ex: `auth-service.js`)
- **Variables/Functions:** camelCase (ex: `validateToken()`)
- **Classes:** PascalCase (ex: `PaymentProcessor`)
- **Constants:** UPPER_SNAKE_CASE (ex: `MAX_RETRIES`)

## Documentation
- **Beads:** Devem seguir o template `bead.template.md`.
- **Comments:** Focados no "Why", não no "How" (o código e o plano já explicam o "How").
- **Logs:** Registre transições de estado, erros críticos e metadados de execução.
