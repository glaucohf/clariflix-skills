# Source Tree — token-optimizer

```
token-optimizer/
├── squad.yaml                    # Manifesto do squad
├── start.md                      # Entry point interativo
├── run.md                        # Execucao direta sem perguntas
├── IDEATION.md                   # Racional de design
├── context-manifest.json         # Manifesto de contexto e tech verification
├── agents/
│   ├── squad-scanner.md          # Cataloga estrutura do squad alvo
│   ├── anti-pattern-detector.md  # Detecta anti-patterns de tokens
│   ├── optimization-planner.md   # Planeja otimizacoes por ROI
│   ├── optimization-executor.md  # Executa reescrita otimizada
│   └── quality-auditor.md        # Valida e produz relatorio final
├── tasks/
│   ├── scan-squad.md             # scanSquad() — inventario estruturado
│   ├── detect-anti-patterns.md   # detectAntiPatterns() — findings + severity
│   ├── plan-optimization.md      # planOptimization() — plano priorizado
│   ├── execute-optimization.md   # executeOptimization() — arquivos otimizados
│   └── audit-quality.md          # auditQuality() — relatorio before/after
├── workflows/
│   ├── optimization-pipeline.yaml  # Pipeline completo (5 fases)
│   └── audit-only.yaml             # Auditoria rapida (3 fases)
└── config/
    ├── coding-standards.md       # Convencoes de nomenclatura e design
    ├── tech-stack.md             # Stack tecnica e modelos
    └── source-tree.md            # Este arquivo
```
