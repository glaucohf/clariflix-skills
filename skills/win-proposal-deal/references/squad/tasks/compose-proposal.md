---
task: composeProposal()
responsavel: "ProposalComposer"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: prospectProfile
    tipo: file
    descricao: "analyzeProspect() output — perfil e objecoes do prospect"
    obrigatorio: true
  - nome: scopeDesign
    tipo: file
    descricao: "designScope() output — 3 versoes de escopo detalhado"
    obrigatorio: true
  - nome: timeline
    tipo: file
    descricao: "designScope() output — cronograma com marcos"
    obrigatorio: true
  - nome: pricingStrategy
    tipo: file
    descricao: "calculatePricing() output — precificacao estrategica"
    obrigatorio: true
  - nome: winRateAnalysis
    tipo: file
    descricao: "calculatePricing() output — previsao de win-rate"
    obrigatorio: true

Saida:
  - nome: proposalFinal
    tipo: file
    descricao: "proposal-final.md — Proposta comercial completa, formatada e pronta para envio ao prospect"
    obrigatorio: true
  - nome: objectionPlaybook
    tipo: file
    descricao: "objection-playbook.md — Guia de objecoes com contra-argumentos para uso no follow-up"
    obrigatorio: true

Checklist:
  pre-conditions:
    - "[ ] prospect-profile.md existe com objecoes mapeadas"
    - "[ ] scope-design.md existe com 3 versoes completas"
    - "[ ] timeline.md existe com marcos e dependencias"
    - "[ ] pricing-strategy.md existe com precos e justificativas"
    - "[ ] win-rate-analysis.md existe com previsoes"
  post-conditions:
    - "[ ] proposal-final.md contem todas as 10 secoes obrigatorias"
    - "[ ] Tom da proposta e adequado ao perfil do prospect"
    - "[ ] Versao recomendada destacada visualmente"
    - "[ ] Data de validade incluida (15-30 dias)"
    - "[ ] Call-to-action com proximo passo concreto"
    - "[ ] objection-playbook.md contem todas as objecoes com contra-argumentos"
    - "[ ] Zero jargao tecnico nao explicado"
    - "[ ] Win-rate previsto mencionado internamente (nao para o prospect)"

Performance:
  duration_expected: "3-5 minutos"
  cost_estimated: "~6000 tokens (Opus)"
  cacheable: false
  parallelizable: false
  skippable_when: "Nunca — proposta e o output final do pipeline"

Error Handling:
  strategy: retry
  retry:
    max_attempts: 2
    delay: "5s"
---
