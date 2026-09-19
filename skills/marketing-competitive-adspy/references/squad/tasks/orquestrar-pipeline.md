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
    descricao: "Competitive Intelligence Weekly Pack entregue toda segunda-feira no ClickUp e Slack contendo: (1) Competitive Activity Dashboard"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Competitive Activity Score por concorrente com variação versus semana anterior e highlight dos 3 movimentos mais relevantes da semana"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) New Winning Ads"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "ads de concorrentes Tier 1 com 30+ dias de veiculação identificados por Cipher com análise completa de ângulo e hipótese de performance"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Swipe File Weekly Update"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "novos itens adicionados por Echo com contexto de reutilização e sugestão de adaptação para a empresa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Decompoe o ciclo de monitoramento competitivo em varreduras, analises e alertas. Recebe o feed consolidado de Falcon (novos ads detectados) e Prism (mudancas de posicionamento/preco), decide a priori…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sigma 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente e critérios de alerta antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação)"
    - "[ ] HITL: Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fazem sentido para o contexto do setor antes do squad entrar em produção completa (L3, calibração crítica de taxonomia)"
    - "[ ] HITL: Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e decidir sobre reação antes de qualquer briefing ser disparado ao time (L3, irreversível — reação de preço e decisão estratégica)"
    - "[ ] HITL: Aprovação de Category Trend Alert — quando Volta detecta convergência de 3+ concorrentes, o CMO deve validar a hipótese estratégica antes de escalar como diretriz de campanha (L3, decisão estratégica de posicionamento)"
    - "[ ] HITL: Revisão de Competitive Brief de reação urgente — qualquer briefing com prazo de reação de 4h (mudança de Tier 1) deve ser revisado por Head de Marketing antes de ser entregue ao time de criativo (L3, velocidade não elimina o gate humano em movimentos críticos)"
---

# Orquestrar Pipeline do Competitive Intelligence & Ad-Spy

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Competitive Intelligence & Ad-Spy |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Orquestrador de Inteligência Competitiva) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 15 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Decompoe o ciclo de monitoramento competitivo em varreduras, analises e alertas. Recebe o feed consolidado de Falcon (novos ads detectados) e Prism (mudancas de posicionamento/preco), decide a prioridade de analise (quais movimentos exigem resposta imediata versus inclusao no ciclo semanal), orquestra a sequencia correta de Cipher (analise de ad), Echo (curadoria de swipe file) e Volta (sintese de tendencia). Nao executa monitoramento diretamente — prioriza, decide e orquestra. Persona: estrategico e paranoid o suficiente para assumir que o concorrente ja encontrou o proximo angulo vencedor. Escala urgencia baseado em tres fatores: (1) tier do concorrente, (2) velocidade de escala do ad detectado, (3) proximidade com lancamento ou periodo critico do cliente. Nunca entrega briefing de swipe ao time sem gate de Sigma.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Competitive Intelligence Weekly Pack entregue toda segunda-feira no ClickUp e Slack contendo: (1) Competitive Activity Dashboard
- Competitive Activity Score por concorrente com variação versus semana anterior e highlight dos 3 movimentos mais relevantes da semana
- (2) New Winning Ads
- ads de concorrentes Tier 1 com 30+ dias de veiculação identificados por Cipher com análise completa de ângulo e hipótese de performance
- (3) Swipe File Weekly Update
- novos itens adicionados por Echo com contexto de reutilização e sugestão de adaptação para a empresa
- (4) Positioning Diff Report
- mudanças detectadas por Prism em landing pages e preços de Tier 1 com destaque do que mudou literalmente
- (5) Category Trend Alert (quando aplicável)
- síntese de Volta sobre convergências de ângulo, formato ou oferta detectadas com hipótese estratégica
- (6) Competitive Briefs da semana
- movimentos que geraram briefings de reação com status de execução pelo time
- (7) Intelligence Quality Metrics
- Intelligence Quality Score médio da semana, false positive rate, cobertura de concorrentes monitorados
- Artefato verificável: task no ClickUp fechada por Orion com todos os documentos anexados, rastreável por data e responsável

## Trigger

Decompoe o ciclo de monitoramento competitivo em varreduras, analises e alertas. Recebe o feed consolidado de Falcon (novos ads detectados) e Prism (mudancas de posicionamento/preco), decide a prioridade de analise (quais movimentos exigem resposta imediata versus inclusao no ciclo semanal), orquestra a sequencia correta de Cipher (analise de ad), Echo (curadoria de swipe file) e Volta (sintese de tendencia). Nao executa monitoramento diretamente — prioriza, decide e orquestra. Persona: estrategico e paranoid o suficiente para assumir que o concorrente ja encontrou o proximo angulo vencedor. Escala urgencia baseado em tres fatores: (1) tier do concorrente, (2) velocidade de escala do ad detectado, (3) proximidade com lancamento ou periodo critico do cliente. Nunca entrega briefing de swipe ao time sem gate de Sigma.

## Knowledge base (o que o executor consulta)

- Meta Ad Library (API pública)
- fonte primária de ads de concorrentes no Meta/Instagram, varredura diária por Falcon com identificadores de anunciante configurados
- Google Ads Transparency Center
- monitoramento de ads no Google Search e Display de concorrentes, varredura diária por Falcon
- TikTok Creative Center
- biblioteca pública de ads no TikTok, varredura semanal para concorrentes Tier 1 com presença na plataforma
- LinkedIn Ad Library
- monitoramento de ads B2B de concorrentes, especialmente relevante para o setor de serviços e SaaS
- prova de trabalho central: swipe files estruturados, Competitive Briefs, tasks de reação com prazo e responsável, dashboard de cobertura de concorrentes e alertas pendentes
- canal #competitive-intel para alertas em tempo real de movimentos críticos, notificações de Sigma BLOCKED para revisão humana urgente, Competitive Week Review automatizado toda segunda-feira
- HubSpot CRM
- campo customizado de Competitive Threat Level por deal ativo, integração de Context Cards de concorrentes nos deals em andamento, alertas de mudança de preço de concorrente para deals em negociação
- orquestração de workflows de varredura, webhooks de detecção de mudança em páginas monitoradas (Prism), automação de diff de landing pages e páginas de preço, notificações de alerta
- Apify (via MCP Docker)
- scraping estruturado de landing pages e páginas de preço para Prism (diff semanal), extração de reviews de G2/Capterra por concorrente, coleta de conteúdo orgânico de blogs de concorrentes
- Semrush / Similarweb
- dados de tráfego e share of voice de concorrentes, keywords em que estão investindo organicamente (Prism usa para correlacionar estratégia de conteúdo com estratégia de ads)
- observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de movimento competitivo, evals de qualidade de classificação de ângulos de Cipher
- Google Drive / Notion (opcional)
- repositório de snapshots históricos de landing pages e Positioning Diffs para auditoria e análise de linha do tempo

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Sigma 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Competitive Intelligence Weekly Pack entregue toda segunda-feira no ClickUp e Slack contendo: (1) Competitive Activity Dashboard
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sigma 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente…
- [ ] Gate HITL respeitado: Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fa…
- [ ] Gate HITL respeitado: Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Competitive Map no Discovery (Semana 2) — CMO valida lista de concorrentes Tier 1/2/3, plataformas a monitorar por concorrente e critérios de aler… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação dos primeiros 10 Winning Ads identificados por Cipher no Deep Dive — Head de Marketing confirma se as classificações de ângulo fazem sentido para o c… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de Pricing Change Alert de concorrente Tier 1 — quando Prism detecta mudança de preço, o CMO ou Head de Produto deve revisar e decidir sobre reação a… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação de Category Trend Alert — quando Volta detecta convergência de 3+ concorrentes, o CMO deve validar a hipótese estratégica antes de escalar como diret… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de Competitive Brief de reação urgente — qualquer briefing com prazo de reação de 4h (mudança de Tier 1) deve ser revisado por Head de Marketing antes… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de itens do swipe file antes de publicação no ClickUp — revisão quinzenal pelo Head de Marketing dos itens aprovados por Sigma para garantir alinhame… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisão mensal do Competitive Intelligence Baseline — CMO e Head de Vendas revisam com Orion quais concorrentes devem subir ou descer de tier, se novos concorr… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Quando Sigma retorna BLOCKED em gate de compliance (risco de plágio ou evidência muito fraca) — revisão humana obrigatória antes de reprocessar o item ou desca… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Falcon
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
