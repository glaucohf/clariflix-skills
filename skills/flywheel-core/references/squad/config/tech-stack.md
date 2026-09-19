# Tech Stack - Flywheel Core

Tecnologias e ferramentas utilizadas pelo enxame para operar o ciclo Flywheel.

## Core Runtime
- **Node.js:** Ambiente principal para ferramentas de coordenação.
- **AIOS Framework:** Infraestrutura de agentes, tarefas e workflows.
- **Claude Code / Gemini CLI:** Interfaces de execução de agentes.

## Flywheel Tools (Internal)
- **br (Bead Repository):** Gestão de reservas consultivas de arquivos e estado de Beads.
- **bv (Bead Viewer):** Análise de grafos de dependência e priorização de tarefas.
- **Agent Mail:** Camada de comunicação de alta largura de banda entre agentes.
- **UBS (Ultimate Bug Scanner):** Scanner profundo para detecção de incoerências e falhas.

## Language Focus
- **JavaScript / TypeScript:** Principal linguagem de implementação das ferramentas de coordenação.
- **YAML / Markdown:** Para definições de agentes, tarefas e Plan Space.

## Infrastructure
- **Git:** Gerenciamento de versão em branch único (`main`).
- **Locks Consultivos:** Prevenção de conflitos via reservas de arquivo com TTL.
