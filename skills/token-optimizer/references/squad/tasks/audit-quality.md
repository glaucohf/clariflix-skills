---
task: auditQuality()
responsavel: "QualityAuditor"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: squadInventory
    tipo: JSON
    descricao: "squad-inventory.json → inventario original do SquadScanner"
    obrigatorio: true
  - nome: antiPatternsReport
    tipo: JSON
    descricao: "anti-patterns-report.json → findings do AntiPatternDetector"
    obrigatorio: true
  - nome: optimizedFiles
    tipo: directory
    descricao: "optimized/ → arquivos otimizados do OptimizationExecutor (opcional no modo audit-only)"
    obrigatorio: false
  - nome: changelog
    tipo: JSON
    descricao: "changelog.json → registro de modificacoes (opcional no modo audit-only)"
    obrigatorio: false
Saida:
  - nome: optimizationReport
    tipo: markdown
    descricao: "→ optimization-report.md entregue ao usuario final"
    obrigatorio: true
Checklist:
  pre-conditions:
    - "[ ] squad-inventory.json existe"
    - "[ ] anti-patterns-report.json existe"
  post-conditions:
    - "[ ] optimization-report.md salvo com metricas before/after"
    - "[ ] Compliance AIOS validado (7 categorias)"
    - "[ ] Projecao de savings em tokens, custo e latencia calculada"
---
# auditQuality()
```
[inventory + anti-patterns + optimized/] ──▶ [QualityAuditor] ──▶ [optimization-report.md]
```

Modo completo: valida arquivos otimizados (compliance AIOS, cross-references, naming), compara metricas projetadas antes/depois (tokens, custo, latencia, qualidade), produz relatorio final. Modo audit-only: analisa squad original, lista anti-patterns encontrados e projeta savings potenciais sem executar otimizacoes.
