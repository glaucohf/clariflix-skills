---
task: planOptimization()
responsavel: "OptimizationPlanner"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: antiPatternsReport
    tipo: JSON
    descricao: "anti-patterns-report.json → findings do AntiPatternDetector"
    obrigatorio: true
  - nome: optimizationPriority
    tipo: string
    descricao: "config.json → prioridade de otimizacao (quality|speed|cost|balanced)"
    obrigatorio: false
Saida:
  - nome: optimizationPlan
    tipo: JSON
    descricao: "→ optimization-plan.json consumido por OptimizationExecutor e QualityAuditor"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] anti-patterns-report.json existe com ao menos 1 finding"
    - "[ ] TOKEN-OPTIMIZATION-GUIDE.md acessivel para mapeamento de tecnicas"
  post-conditions:
    - "[ ] optimization-plan.json salvo com acoes priorizadas por ROI"
    - "[ ] Cada acao mapeia anti-pattern → tecnica do guia → instrucao atomica"
    - "[ ] Estimativa de impacto total (tokens, custo, latencia, qualidade)"
---
# planOptimization()
```
[anti-patterns-report.json] ──▶ [OptimizationPlanner] ──▶ [optimization-plan.json]
```

Recebe anti-patterns detectados e cria plano de otimizacao ordenado por ROI. Prioridade padrao: qualidade > velocidade > custo. Para cada anti-pattern: identifica tecnica(s) corretiva(s) do guia (secao + numero), calcula ROI (impacto estimado / esforco de implementacao), gera instrucao atomica para o executor. Agrupa acoes em waves de implementacao respeitando dependencias entre otimizacoes.
