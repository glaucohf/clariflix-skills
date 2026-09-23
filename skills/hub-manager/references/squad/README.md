# Hub Manager Squad

**Version:** 0.1.0  
**Command:** `@hub-chief`  
**Type:** Operational Squad

## Overview

O Hub Manager Squad ajuda embaixadores aprovados da Academia Lendaria a operar hubs locais com clareza e baixo atrito.

Ele foi desenhado para responder perguntas praticas como:

- o que fazer esta semana no hub
- que post publicar agora
- como receber novos membros
- como reativar quem sumiu
- como planejar um encontro simples
- como entender se o hub esta saudavel ou esfriando

## Agents

| Agent | Command | Specialty |
|---|---|---|
| Hub Chief | `@hub-chief` | Orquestracao, plano semanal e diagnostico |
| Hub Content | `@hub-content` | Posts, convites, CTAs e lembretes |
| Hub Members | `@hub-members` | Onboarding, reativacao e acompanhamento |
| Hub Events | `@hub-events` | Encontros, rituais locais e follow-up |

## Routing

Use `@hub-chief` como entrypoint:

- `"planejar a semana do meu hub"` -> `plan-weekly-hub`
- `"diagnosticar meu hub"` -> `diagnose-hub-health`
- `"organizar o mes do hub"` -> `plan-monthly-calendar`
- `"criar um post para o encontro"` -> `@hub-content`
- `"me ajuda a receber novos membros"` -> `@hub-members`
- `"planejar um encontro local"` -> `@hub-events`

## Core Tasks

- `plan-weekly-hub`: organizar a semana do hub
- `create-hub-post`: criar posts, convites e CTAs
- `create-event-plan`: planejar encontros e rituais
- `onboard-hub-member`: receber novos membros
- `reactivate-members`: reengajar membros silenciosos
- `diagnose-hub-health`: ler o momento do hub e priorizar acoes
- `plan-monthly-calendar`: organizar o mes
- `analyze-event-results`: ajustar a operacao apos um evento

## Workflows

- `workflows/weekly-operating-cycle.yaml`
- `workflows/event-launch-cycle.yaml`
- `workflows/member-reactivation-cycle.yaml`
- `workflows/hub-diagnostic-cycle.yaml`

## Checklists

- `checklists/weekly-ops-checklist.md`
- `checklists/event-readiness-checklist.md`

## Principles

- linguagem simples para nao tecnicos
- respostas curtas e acionaveis
- sempre sugerir o proximo passo
- diagnostico leve, sem depender de stack de dados
- coerencia entre mensagem, rito e objetivo sem expor framework pesado

## Quick Start

```text
@hub-chief planejar a semana do meu hub
@hub-chief diagnosticar meu hub
@hub-content criar um post para convidar membros para o encontro de quinta
@hub-members me ajuda a receber novos membros
@hub-events planejar um encontro local sobre IA na pratica
```

## Notes

- Fontes upstream de referencia:
  - `aios-lendario-rodrigo/squads/comunidade-bu`
  - `aios-lendario-rodrigo/squads/movement`
- O squad final evita copiar a complexidade completa desses sistemas.
- O foco aqui e utilidade pratica para o embaixador.
- Configuracao canonica em `config.yaml`.
- Troubleshooting em `docs/TROUBLESHOOTING.md`.
