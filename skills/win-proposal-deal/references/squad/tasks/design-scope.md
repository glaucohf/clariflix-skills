---
task: designScope()
responsavel: "ScopeArchitect"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectProfile
    tipo: file
    descricao: "analyzeProspect() output — perfil do prospect com dores priorizadas"
    obrigatorio: true
  - nome: historicalAnalysis
    tipo: file
    descricao: "analyzeProspect() output — propostas similares e padroes"
    obrigatorio: true

Saida:
  - nome: scopeDesign
    tipo: file
    descricao: "scope-design.md — Escopo detalhado com 3 versoes (essencial, recomendado, premium), entregaveis, marcos e criterios de aceite. Consumido por calculatePricing() e composeProposal()"
    obrigatorio: true
  - nome: timeline
    tipo: file
    descricao: "timeline.md — Cronograma com fases, dependencias, buffers e marcos de aceite. Consumido por composeProposal()"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] prospect-profile.md existe com dores priorizadas"
    - "[ ] historical-analysis.md existe com benchmarks de escopo"
  post-conditions:
    - "[ ] scope-design.md contem 3 versoes de escopo (essencial, recomendado, premium)"
    - "[ ] Cada entregavel mapeia para pelo menos 1 dor do prospect"
    - "[ ] Horas estimadas por perfil (junior/pleno/senior) para cada entregavel"
    - "[ ] timeline.md contem fases com duracao, dependencias e marcos"
    - "[ ] Buffer de 15-20% incluido na timeline"
    - "[ ] Criterios de aceite mensuraveis para cada fase"

Performance:
  duration_expected: "2-4 minutos"
  cost_estimated: "~4000 tokens (Opus)"
  cacheable: false
  parallelizable: false
  skippable_when: "Nunca — escopo e prerequisito para pricing e proposta"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "5s"
---
