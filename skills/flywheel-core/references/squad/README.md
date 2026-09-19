# Flywheel Core — Super Sistema de Agentes Autônomos

> Implementação rigorosa da metodologia **Agent Flywheel** (Jeffrey Emanuel) para orquestração de enxames de agentes com foco em Raciocínio Estratégico, Memória Executável (Beads) e Feedback Sistêmico.

## 🌪️ O Ciclo Flywheel

Este squad opera através do triângulo de coordenação e dos 4 pilares fundamentais:

1.  **Reasoning (Raciocínio):** Focado no *Plan Space*. Planos estratégicos de alta densidade antes de qualquer execução.
2.  **Memory (Memória):** Uso de **Beads** como unidades de contexto autocontidas e memória executável.
3.  **Tools (Ferramentas):** Coordenação via `br` (locks), `bv` (grafos) e `Agent Mail`.
4.  **Feedback (Retroalimentação):** Ciclos de *Hardening*, *Blunder Hunts* e revisão multi-modelo.

## 👥 Agentes do Enxame

| Ícone | Agente | Papel | Responsabilidade |
| :--- | :--- | :--- | :--- |
| 🧠 | **FlywheelArchitect** | Architect | Mapeia o *Plan Space* e gera a estratégia global. |
| 📿 | **BeadManager** | Builder | Converte planos em Beads e realiza o polimento iterativo (N vezes). |
| 🧭 | **SwarmCoordinator** | Flow_Master | Gerencia o triângulo de coordenação, locks e priorização via grafos. |
| 🛡️ | **HardeningSpecialist** | Guardian | Auditoria de bugs (UBS), caça a blunders e revisões cruzadas. |

## 🔄 Workflows Principais

### `flywheel_execution_cycle`
O pipeline mestre que move o sistema da ideia à entrega:
`Plan (Architect) → Bead Polishing (Bead-Master) → Coordinated Execution (Swarm) → Hardening (Guardian)`

### `hardening_pipeline`
Focado exclusivamente em blindar o sistema contra regressões e erros latentes.

## 🛠️ Instalação e Uso

Para ativar o squad no ambiente AIOS:

```bash
/SQUADS:flywheel:flywheel-architect  # Iniciar planejamento estratégico
/SQUADS:flywheel:bead-manager        # Polir e preparar execução
```

## 📜 Autor

**Marcio Bisognin**
*Squads Platform Instagram* [@marciobisognin](https://instagram.com/marciobisognin)

---
**Squads Platform Instagram @marciobisognin**
