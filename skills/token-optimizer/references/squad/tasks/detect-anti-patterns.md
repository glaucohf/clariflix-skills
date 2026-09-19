---
task: detectAntiPatterns()
responsavel: "AntiPatternDetector"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: squadInventory
    tipo: JSON
    descricao: "squad-inventory.json → inventario produzido por SquadScanner"
    obrigatorio: true
  - nome: guideReference
    tipo: filepath
    descricao: "TOKEN-OPTIMIZATION-GUIDE.md → base de conhecimento de anti-patterns"
    obrigatorio: true
Saida:
  - nome: antiPatternsReport
    tipo: JSON
    descricao: "→ anti-patterns-report.json consumido por OptimizationPlanner e QualityAuditor"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] squad-inventory.json existe e esta completo"
    - "[ ] TOKEN-OPTIMIZATION-GUIDE.md acessivel"
  post-conditions:
    - "[ ] anti-patterns-report.json salvo com todos os findings"
    - "[ ] Cada finding tem severidade (1-10) e tokens desperdicados estimados"
    - "[ ] Nenhum anti-pattern do guia foi ignorado na checagem"
---
# detectAntiPatterns()
```
[squad-inventory.json] ──▶ [AntiPatternDetector] ──▶ [anti-patterns-report.json]
```

Itera sobre a lista completa de anti-patterns da Secao 13 do guia. Para cada anti-pattern, verifica no inventario se ha ocorrencias. Registra: tipo do anti-pattern, arquivo(s) afetado(s), severidade (1-10), tokens estimados desperdicados por execucao, e tecnica de correcao recomendada (referencia numerada do guia). Ordena findings por severidade decrescente.
