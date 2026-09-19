---
task: calculatePricing()
responsavel: "PricingStrategist"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectProfile
    tipo: file
    descricao: "analyzeProspect() output — budget e sensibilidade a preco"
    obrigatorio: true
  - nome: historicalAnalysis
    tipo: file
    descricao: "analyzeProspect() output — historico de conversao por faixa de preco"
    obrigatorio: true
  - nome: scopeDesign
    tipo: file
    descricao: "designScope() output — 3 versoes de escopo com horas estimadas"
    obrigatorio: true

Saida:
  - nome: pricingStrategy
    tipo: file
    descricao: "pricing-strategy.md — Precificacao por versao com custo base, margem, preco de venda, descontos condicionais e justificativa de valor. Consumido por composeProposal()"
    obrigatorio: true
  - nome: winRateAnalysis
    tipo: file
    descricao: "win-rate-analysis.md — Previsao de win-rate por versao/preco com variaveis consideradas e intervalo de confianca. Consumido por composeProposal()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] prospect-profile.md existe com budget e sensibilidade a preco"
    - "[ ] scope-design.md existe com 3 versoes e horas estimadas"
    - "[ ] historical-analysis.md existe com benchmarks de conversao"
  post-conditions:
    - "[ ] pricing-strategy.md contem preco para cada versao de escopo"
    - "[ ] Margem minima de 30% verificada para todas as versoes"
    - "[ ] Descontos condicionais definidos com regras claras"
    - "[ ] win-rate-analysis.md contem previsao para cada versao"
    - "[ ] Win-rate considera pelo menos 5 variaveis"
    - "[ ] Tabela comparativa das 3 versoes formatada"

Performance:
  duration_expected: "1-3 minutos"
  cost_estimated: "~3500 tokens (Opus)"
  cacheable: false
  parallelizable: false
  skippable_when: "Nunca — pricing e prerequisito para a proposta"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "3s"
  fallback: "Se historico insuficiente, use margem padrao de 40% e win-rate baseado em benchmarks do setor"
---
