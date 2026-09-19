---
task: executeOptimization()
responsavel: "OptimizationExecutor"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: optimizationPlan
    tipo: JSON
    descricao: "optimization-plan.json → plano priorizado do OptimizationPlanner"
    obrigatorio: true
  - nome: squadPath
    tipo: string
    descricao: "config.json → caminho do squad original para leitura"
    obrigatorio: true
Saida:
  - nome: optimizedFiles
    tipo: directory
    descricao: "→ diretorio optimized/ com arquivos otimizados consumidos por QualityAuditor"
    obrigatorio: true
  - nome: changelog
    tipo: JSON
    descricao: "→ changelog.json com diff de cada arquivo modificado"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] optimization-plan.json existe com ao menos 1 acao"
    - "[ ] Arquivos originais do squad acessiveis em squadPath"
  post-conditions:
    - "[ ] Diretorio optimized/ criado com todos os arquivos otimizados"
    - "[ ] changelog.json registra cada modificacao com before/after"
    - "[ ] Arquivos originais NAO foram sobrescritos"
---
# executeOptimization()
```
[optimization-plan.json + squadPath] ──▶ [OptimizationExecutor] ──▶ [optimized/ + changelog.json]
```

Executa cada acao do plano de otimizacao em ordem de wave. Para cada arquivo afetado: le o original, aplica a(s) otimizacao(oes) especificada(s), grava versao otimizada em diretorio optimized/ espelhando a estrutura original. Registra cada modificacao no changelog com: arquivo, tecnica aplicada, diff resumido, tokens estimados antes/depois.
