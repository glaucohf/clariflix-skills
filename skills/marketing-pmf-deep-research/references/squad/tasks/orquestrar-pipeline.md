---
task: orionPipeline()
responsavel: "Orion"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "PMF Framework Document (PDF/Notion, 10-15 páginas executivas) contendo: PMF Score (1-10) com breakdown, ICP Master Profile com 3-5 clusters rankeados, top-3 ângulos de posicionamento com justificativa de evidência, Persona Cards (3-5), Competitive Matrix, Angle Test Kit (3-5 headlines/hooks prontos por canal) e Roadmap de Validação (30 dias)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato registrado e versionado no ClickUp como prova de trabalho auditável"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Decompoe o objetivo de pesquisa em sub-tarefas mensuráveis, delega a workers especializados, monitora qualidade dos outputs via quality gates (dev 70% / staging 85% / prod 95%), sintetiza evidencias…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Brutus 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias de pesquisa na direção errada"
    - "[ ] HITL: Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx simular entrevistas"
    - "[ ] HITL: Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva documentada"
    - "[ ] HITL: Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução (Copywriter, Media Buying) — gate L3 porque decisões de mídia são financeiramente irreversíveis"
    - "[ ] HITL: Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser incluído no documento final"
---

# Orquestrar Pipeline do PMF & Market Deep Research Squad

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** PMF & Market Deep Research Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do PMF & Market Deep Research Squad |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Estrategista de Mercado) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Decompoe o objetivo de pesquisa em sub-tarefas mensuráveis, delega a workers especializados, monitora qualidade dos outputs via quality gates (dev 70% / staging 85% / prod 95%), sintetiza evidencias em PMF Framework Document e decide quando escalar para HITL. Opera em modo L2: executa autonomamente dentro do escopo aprovado, propoe proximos ciclos mas nao altera escopo sem aprovacao humana.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- PMF Framework Document (PDF/Notion, 10-15 páginas executivas) contendo: PMF Score (1-10) com breakdown, ICP Master Profile com 3-5 clusters rankeados, top-3 ângulos de posicionamento com justificativa de evidência, Persona Cards (3-5), Competitive Matrix, Angle Test Kit (3-5 headlines/hooks prontos por canal) e Roadmap de Validação (30 dias)
- Artefato registrado e versionado no ClickUp como prova de trabalho auditável

## Trigger

Decompoe o objetivo de pesquisa em sub-tarefas mensuráveis, delega a workers especializados, monitora qualidade dos outputs via quality gates (dev 70% / staging 85% / prod 95%), sintetiza evidencias em PMF Framework Document e decide quando escalar para HITL. Opera em modo L2: executa autonomamente dentro do escopo aprovado, propoe proximos ciclos mas nao altera escopo sem aprovacao humana.

## Knowledge base (o que o executor consulta)

- HubSpot / Salesforce
- leitura de dados de CRM para ICP profiling (Iris)
- waterfall enrichment de 100+ fontes para enriquecimento de ICP e sinais de intent
- Apollo.io
- prospecting e enriquecimento de contatos para validacao de ICP
- SEMrush / SimilarWeb
- share of voice, keywords e tráfego de concorrentes (Marco, Atlas)
- Meta Ad Library / Google Ads Transparency
- análise de criativos e copy de concorrentes (Atlas)
- G2 / Capterra / Trustpilot
- reviews públicos para signal sensing e competitive intel (Vesper, Atlas)
- sinais de hiring, conteúdo e movimentos estratégicos de concorrentes (Vesper, Atlas)
- Reddit / forums do nicho
- captura de linguagem de dor organica (Vesper)
- Notion / Google Docs
- entrega do PMF Framework Document e Persona Cards ao cliente
- registro de tasks, prova de trabalho e rastreamento de artefatos entregues por ciclo
- observabilidade OTEL, evals e quality gates dos agentes (dev 70% / staging 85% / prod 95%)
- Slack / WhatsApp Business
- notificações de HITL ao cliente/board para aprovações críticas

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Brutus 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: PMF Framework Document (PDF/Notion, 10-15 páginas executivas) contendo: PMF Score (1-10) com breakdown, ICP Master Profile com 3-5 clusters rankeados, top-3 ân…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Brutus 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começ…
- [ ] Gate HITL respeitado: Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a re…
- [ ] Gate HITL respeitado: Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva docume… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser i… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Brutus 2 | BLOQUEIA entrega |

## Handoff

- **to:** Marco
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
