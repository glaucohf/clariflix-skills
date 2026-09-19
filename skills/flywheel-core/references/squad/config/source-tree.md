# Source Tree - Flywheel Core

Estrutura de diretórios esperada para o squad e seus artefatos.

## Flywheel Core Squad
```text
squads/flywheel-core/
├── agents/             # Definições de agentes AIOS
├── tasks/              # Definições de tarefas executáveis
├── workflows/          # Arquivos YAML de fluxos de trabalho
├── config/             # Configurações de domínio e padrões
├── templates/          # Templates para Plan Space e Beads
├── checklists/         # Gates de qualidade e validação
├── scripts/            # Ferramentas internas (br, bv, ubs)
├── README.md           # Guia central do squad
└── squad.yaml          # Manifesto do squad
```

## Workspace Artifacts (Generated)
```text
flywheel/
├── PLAN_SPACE.md       # Plano estratégico de alta densidade
├── BEADS.md            # Repositório de unidades executáveis
├── LOCKS.json          # Estado atual de reservas de arquivos
├── UBS_REPORT.md       # Relatório de auditoria e bugs
└── AGENTS.md           # Manual de operações para o enxame
```
