---
task: analyzeProspect()
responsavel: "ProspectAnalyzer"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectData
    tipo: object
    descricao: "Dados do prospect: empresa, setor, tamanho, budget, dores, decisor, timeline"
    obrigatorio: true
  - nome: proposalHistory
    tipo: array<object>
    descricao: "Historico de propostas anteriores com resultados (win/loss/pending) e metadados"
    obrigatorio: false

Saida:
  - nome: prospectProfile
    tipo: file
    descricao: "prospect-profile.md — Perfil completo do prospect com scoring, dores priorizadas e objecoes mapeadas. Consumido por designScope() e calculatePricing()"
    obrigatorio: true
  - nome: historicalAnalysis
    tipo: file
    descricao: "historical-analysis.md — Analise de propostas similares, padroes de win/loss e win-rate previsto. Consumido por calculatePricing()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] Dados minimos do prospect fornecidos: empresa, setor, pelo menos 1 dor"
    - "[ ] Budget declarado ou faixa estimada disponivel"
  post-conditions:
    - "[ ] prospect-profile.md gerado com scoring de qualificacao (1-10)"
    - "[ ] Pelo menos 3 dores mapeadas com urgencia e impacto"
    - "[ ] Objecoes provaveis identificadas com contra-argumentos"
    - "[ ] Win-rate previsto com intervalo de confianca"
    - "[ ] historical-analysis.md gerado com pelo menos 3 propostas similares referenciadas"

Performance:
  duration_expected: "1-3 minutos"
  cost_estimated: "~3000 tokens (Sonnet)"
  cacheable: true
  parallelizable: false
  skippable_when: "Nunca — analise do prospect e prerequisito para todo o pipeline"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "3s"
  fallback: "Se historico indisponivel, use benchmarks do setor como proxy"
---
