# Source Tree — Brain Squad

```
brain-squad/
├── squad.yaml                    # Manifesto central
├── agents/
│   ├── theme-definer.md          # Define 10 tipos de associacao
│   ├── idea-generator.md         # Gera 10 itens (x10 paralelo)
│   ├── filter-ranker.md          # Filtra e ranqueia (Pareto)
│   ├── synthesizer.md            # Sintetiza output final Fase 1
│   ├── design-facilitator.md     # Facilita design interativo Fase 2
│   └── report-builder.md         # Consolida relatorio final
├── tasks/
│   ├── define-themes.md          # defineThemes()
│   ├── generate-ideas.md         # generateIdeas()
│   ├── filter-and-rank.md        # filterAndRank()
│   ├── synthesize-insights.md    # synthesizeInsights()
│   ├── facilitate-design.md      # facilitateDesign()
│   └── build-report.md           # buildReport()
├── workflows/
│   ├── brain-pipeline.yaml       # Pipeline completo (Diverge+Converge)
│   └── diverge-only.yaml         # Apenas Fase 1 (Diverge)
├── config/
│   ├── coding-standards.md       # Convencoes de codigo
│   ├── tech-stack.md             # Stack tecnologico
│   └── source-tree.md            # Este arquivo
├── shared/
│   └── macros.md                 # Regras compartilhadas (ler 1x)
├── templates/
│   └── schemas.md                # Schemas de output
└── README.md                     # Documentacao principal
```

## Runtime File Contracts (.brainstorm-tmp/)

```
.brainstorm-tmp/
├── topic.txt                     # Topico original
├── themes.json                   # 10 tipos de associacao
├── r1/
│   ├── agent-1.txt ... agent-10.txt  # 100 itens R1
├── top10.json                    # Top 10 ranqueados
├── top10_summary.txt             # Titulos do Top 10
├── r2/
│   ├── agent-1.txt ... agent-10.txt  # 100 itens R2
├── top3.json                     # Top 3 finais
├── final_output.md               # Output sintetizado Fase 1
├── selected_insight.json         # Insight escolhido no gate
├── design/
│   ├── understanding.md          # Resumo de entendimento
│   ├── design.md                 # Design validado
│   └── decisions.md              # Decision Log
└── brain_report.md               # Relatorio final consolidado
```
