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
    descricao: "Fundraising Readiness Package"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "artefato verificável e auditável entregue antes do roadshow, composto de: (1) Investor Universe Map ranqueado com 80–150 investidores e score de fit, warm intro paths e Intelligence Briefs individuais para os top 20"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Data Room completo e auditado com 95%+ dos documentos requeridos, cada dado rastreável à fonte e versão controlada"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Pitch Narrative Framework com one-liner, elevator pitch, estrutura de deck por slide e variantes por perfil de investidor"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(4) Objection Playbook com 25–40 objeções categorizadas, contra-argumentos com dado de suporte e Top 5 'buracos da tese' com plano de mitigação"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "(5) Roadshow Tracker no ClickUp com pipeline de investidores, sequência de outreach personalizada pronta para aprovação e dashboard de funil"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do squad de Investor & Fundraising Ops. Recebe o intent estratégico do founder (ex: 'quero estar pronto para roadshow em 3 semanas', 'preciso mapear VCs para Série A de R$15M') e…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Hades antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível"
    - "[ ] HITL: Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão do documento, nível de acesso)"
    - "[ ] HITL: Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades abordar proativamente vs deixar sem abordar"
    - "[ ] HITL: Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta priorização"
    - "[ ] HITL: Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente vs delegar à IA para rascunho"
---

# Orquestrar Pipeline do Investor & Fundraising Ops

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Investor & Fundraising Ops |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Fundraising Ops Orchestrator) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do squad de Investor & Fundraising Ops. Recebe o intent estratégico do founder (ex: 'quero estar pronto para roadshow em 3 semanas', 'preciso mapear VCs para Série A de R$15M') e decompõe em tarefas atômicas distribuídas aos workers especializados. Mantém o estado completo da operação de captação: status do data room por documento, estágio de cada investidor no pipeline, versão atual da narrativa, objeções já testadas. Prioriza o trabalho dos agentes de acordo com o cronograma do roadshow (o que é crítico para o primeiro meeting vs o que pode ser refinado depois). Sintetiza todos os outputs em artefatos coesos e rastreáveis. Nunca envia mensagem para investidor real — roteia tudo pelo HITL Gate. Apresenta ao founder uma visão de 'Fundraising Readiness Score' (0–100%) que sobe conforme data room, narrativa e prep de objeções ficam prontos.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Fundraising Readiness Package
- artefato verificável e auditável entregue antes do roadshow, composto de: (1) Investor Universe Map ranqueado com 80–150 investidores e score de fit, warm intro paths e Intelligence Briefs individuais para os top 20
- (2) Data Room completo e auditado com 95%+ dos documentos requeridos, cada dado rastreável à fonte e versão controlada
- (3) Pitch Narrative Framework com one-liner, elevator pitch, estrutura de deck por slide e variantes por perfil de investidor
- (4) Objection Playbook com 25–40 objeções categorizadas, contra-argumentos com dado de suporte e Top 5 'buracos da tese' com plano de mitigação
- (5) Roadshow Tracker no ClickUp com pipeline de investidores, sequência de outreach personalizada pronta para aprovação e dashboard de funil
- (6) Knowledge Graph inicial da operação de captação (Mnemo) populado com histórico disponível
- Após roadshow iniciado: atualização contínua do Objection Playbook com objeções reais recebidas, briefing pré-meeting 48h antes de cada reunião e relatório semanal de funil com projeção de fechamento

## Trigger

Orquestrador central do squad de Investor & Fundraising Ops. Recebe o intent estratégico do founder (ex: 'quero estar pronto para roadshow em 3 semanas', 'preciso mapear VCs para Série A de R$15M') e decompõe em tarefas atômicas distribuídas aos workers especializados. Mantém o estado completo da operação de captação: status do data room por documento, estágio de cada investidor no pipeline, versão atual da narrativa, objeções já testadas. Prioriza o trabalho dos agentes de acordo com o cronograma do roadshow (o que é crítico para o primeiro meeting vs o que pode ser refinado depois). Sintetiza todos os outputs em artefatos coesos e rastreáveis. Nunca envia mensagem para investidor real — roteia tudo pelo HITL Gate. Apresenta ao founder uma visão de 'Fundraising Readiness Score' (0–100%) que sobe conforme data room, narrativa e prep de objeções ficam prontos.

## Knowledge base (o que o executor consulta)

- Crunchbase / PitchBook dados públicos (mapeamento de portfólios de VCs e histórico de investimentos para o Vega)
- LinkedIn API / Sales Navigator (warm intro path mapping, perfis de GPs e managing partners para o Vega e Mnemo)
- EXA / Perplexity MCP (pesquisa em tempo real de atividade de investidores, teses publicadas, notícias de mercado)
- Gmail / Outlook MCP (histórico de comunicações com investidores para o Mnemo, envio controlado via Gate)
- Google Drive / Notion (repositório do data room, versionamento de documentos pelo Atlas)
- Dealroom / Captable.io / Carta (cap table atualizado, documentos de rodadas anteriores para o Atlas)
- Stripe / QuickBooks / Conta Azul (dados financeiros reais para o financial model e métricas do Atlas)
- HubSpot / Salesforce CRM (cohort de clientes, churn, expansão, CAC
- métricas de tração para Atlas e Brutus)
- Mixpanel / Amplitude / PostHog (métricas de produto, DAU/MAU, NPS, engagement para o data room)
- ClickUp (Roadshow Tracker
- pipeline de captação, tasks, follow-ups, audit trail de toda a operação)
- Sembly / Fireflies / Otter.ai (transcrições automáticas de meetings com investidores para o Mnemo)
- Langfuse (observabilidade OTEL
- tracing de tokens, custo por agente, task success rate por pipeline)
- Vector DB
- Pinecone / Qdrant (Knowledge Graph do Mnemo, corpus de Intelligence Briefs do Vega, histórico de narrativas)
- Slack (interface conversacional do founder com o Orion
- recebe alertas, approva mensagens, consulta status do roadshow)
- DocSend / Docsend-compatible viewer (rastreamento de visualização do data room
- quem abriu, quanto tempo em cada seção)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Hades antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Fundraising Readiness Package
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Hades registrado
- [ ] Gate HITL respeitado: Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass p…
- [ ] Gate HITL respeitado: Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto,…
- [ ] Gate HITL respeitado: Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide qua…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão d… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta p… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação da Pitch Narrative Framework pelo founder antes de qualquer variante ser usada em meeting — founder valida o posicionamento, o use of funds e o valua… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do Knowledge Graph do Mnemo — founder autoriza explicitamente quais fontes de dados históricos (emails, transcrições) podem ser ingeridas… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança nos termos da rodada refletida nos artefatos (ticket, valuation, estrutura) requer aprovação explícita antes de Hermes atualizar mensagens de… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Hades | BLOQUEIA entrega |

## Handoff

- **to:** Vega
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
