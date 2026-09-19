---
task: nexusPipeline()
responsavel: "Nexus"
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
    descricao: "ABM Campaign Package por conta ativada"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "artefato verificavel no ClickUp contendo: Account Intelligence Profile (buying committee mapeado, ICP score, sinais detectados), ABM Copy Package aprovado pelo Aegis (email sequences, LinkedIn messages, ad copy, call script), cronograma de touches aprovado pelo Chronos, campanhas ativas nas plataformas de ads, sequencias ativas no CRM, e Account Engagement Dashboard com tracking em tempo real"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Cada campanha e uma task no ClickUp com checklist de aprovacoes HITL, historico de versoes de copy e metricas de performance linkadas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Recebe sinais de intent qualificados, determina Tier e urgencia da conta, decompoe o playbook ABM correspondente em tasks paralelas, delega a workers especializados (ICP, Copy, Outreach, Ads), monito…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plataformas de ads"
    - "[ ] L3: Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad"
    - "[ ] L3: Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio"
    - "[ ] L2: Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha completa"
    - "[ ] L2: Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana sobre próximos passos"
---

# Orquestrar Pipeline do ABM Signal Orchestrator

**Task ID:** `nexusPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do ABM Signal Orchestrator |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Orquestrador ABM) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe sinais de intent qualificados, determina Tier e urgencia da conta, decompoe o playbook ABM correspondente em tasks paralelas, delega a workers especializados (ICP, Copy, Outreach, Ads), monitora progresso e sintetiza os outputs em uma Campanha ABM coerente e cronometrada. Opera como hub central que garante que marketing e vendas falem a mesma lingua para a mesma conta ao mesmo tempo.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- ABM Campaign Package por conta ativada
- artefato verificavel no ClickUp contendo: Account Intelligence Profile (buying committee mapeado, ICP score, sinais detectados), ABM Copy Package aprovado pelo Aegis (email sequences, LinkedIn messages, ad copy, call script), cronograma de touches aprovado pelo Chronos, campanhas ativas nas plataformas de ads, sequencias ativas no CRM, e Account Engagement Dashboard com tracking em tempo real
- Cada campanha e uma task no ClickUp com checklist de aprovacoes HITL, historico de versoes de copy e metricas de performance linkadas

## Trigger

Recebe sinais de intent qualificados, determina Tier e urgencia da conta, decompoe o playbook ABM correspondente em tasks paralelas, delega a workers especializados (ICP, Copy, Outreach, Ads), monitora progresso e sintetiza os outputs em uma Campanha ABM coerente e cronometrada. Opera como hub central que garante que marketing e vendas falem a mesma lingua para a mesma conta ao mesmo tempo.

## Knowledge base (o que o executor consulta)

- HubSpot CRM
- fonte de verdade de contas, contatos, deals e histórico de interações
- receptor de todos os touches e atualizações de engajamento
- waterfall enrichment com 100+ fontes para Account Intelligence Profile
- source primária de sinais de intent via Clay Intelligence
- Apollo.io
- prospecting, enriquecimento de contatos, sequenciamento de email frio via Apollo Sequences
- Instantly
- cold email infrastructure com alta deliverabilidade, rotação de caixas de entrada, warmup automático
- LinkedIn (via API/Phantombuster)
- connection requests, messages, monitoramento de atividade de stakeholders
- Meta Business Manager
- campanhas de Account-Based Advertising com custom audiences por conta
- Google Ads
- campanhas RLSA e Customer Match para contas-alvo
- LinkedIn Campaign Manager
- Matched Audiences por empresa e lista de contatos
- WhatsApp Business API (via Patagon AI ou Leadsales)
- canal de outreach para stakeholders qualificados, pós-proibição Meta de chatbots gênericos
- camada de prova-de-trabalho: cada campanha ABM criada vira task com artefatos verificáveis, checklists e histórico de aprovações HITL
- observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95%), rastreamento de custo por campanha ABM
- Bombora / G2 / TechTarget
- sinais de intent third-party por topico e categoria de produto
- Clearbit / Crunchbase
- funding signals, hiring signals, tech stack changes para enriquecimento do Radar

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Aegis antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: ABM Campaign Package por conta ativada
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis registrado
- [ ] Gate L3 respeitado: Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto…
- [ ] Gate L3 respeitado: Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi c…
- [ ] Gate L3 respeitado: Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plata… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha c… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana s… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Curadoria do Account Universe Map: adicionar/remover contas do universo ABM e ajustar Tiers requer input estratégico humano (revisão quinzenal) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Aegis | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
