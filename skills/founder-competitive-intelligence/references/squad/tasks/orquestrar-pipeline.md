---
task: atlasPipeline()
responsavel: "Atlas"
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
    descricao: "Competitive Intelligence Weekly Pack entregue toda sexta-feira no ClickUp (task fechada por Atlas com todos os artefatos anexados) e no canal Slack #competitive-intel, contendo: (1) Competitive Activity Dashboard"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Competitive Activity Index por concorrente Tier 1 e Tier 2 com variacao versus semana anterior e top 3 movimentos da semana com scoring de Lynx"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Counter-Play Briefs da semana"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "todos os FLASH alerts gerados com hipotese estrategica de Ares, contra-jogadas recomendadas e status de execucao pelo founder"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Movement Profiles Update"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "o que mudou nos perfis estrategicos de cada Tier 1 (preco atual, headcount delta, foco de produto aparente, saude financeira aparente)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Persona: estrategista paranoid com cerebro de Grand Master de xadrez — assume que cada movimento do concorrente e parte de uma sequencia maior, nunca um evento isolado. Decompoe o ciclo de inteligenc…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Veritas 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento por concorrente, critérios de alerta por categoria de movimento e janela de reação por tipo antes de qualquer monitoramento ir ao ar (L3, gate obrigatório — define o escopo de toda a operação e a sensibilidade dos alertas)"
    - "[ ] HITL: Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atual e as restrições reais do negócio capturados por Atlas para alimentar o Wargame Engine — sem calibração, as contra-jogadas de Ares são genéricas (L3, input crítico que define qualidade das recomendações)"
    - "[ ] HITL: Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirma se as classificações de movimento fazem sentido para o contexto real do mercado e calibra thresholds de scoring de Lynx (L3, calibração crítica antes de produção)"
    - "[ ] HITL: Aprovação de Competitive Flash antes de Counter-Play urgente (score >= 9 em Tier 1) — quando Hermes recebe sinal CRÍTICO aprovado por Veritás, o founder deve confirmar ciência e decisão antes de qualquer ação irreversível ser executada (L3, irreversível por natureza — resposta competitiva errada pode ser pior que nenhuma resposta)"
    - "[ ] HITL: Revisão mensal do Competitive Landscape Report — founder revisa com Atlas o cenário competitivo do mês, valida os cenários de wargame de Ares para os próximos 90 dias, aprova os playbooks de resposta como diretriz estratégica e ajusta os critérios de alerta do Competitive Map se necessário (L3, governança estratégica mensal obrigatória)"
---

# Orquestrar Pipeline do Inteligência Competitiva Contínua

**Task ID:** `atlasPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Inteligência Competitiva Contínua

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Inteligência Competitiva Contínua |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Strategist Orquestrador de Inteligência Competitiva) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 14 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Persona: estrategista paranoid com cerebro de Grand Master de xadrez — assume que cada movimento do concorrente e parte de uma sequencia maior, nunca um evento isolado. Decompoe o ciclo de inteligencia competitiva em coleta (Hawk), analise de sinal (Lynx), simulacao estrategica (Ares) e dispatch de alerta (Hermes). Recebe o feed consolidado de sinais novos de Lynx, decide o nivel de urgencia (Competitive Flash imediato versus consolidacao no Weekly Briefing), orquestra Ares para simular hipoteses e contra-jogadas antes de qualquer entrega ao founder, e garante que Veritas faz o gate de qualidade em todos os briefings criticos. Conduiz a entrevista estruturada de Discovery com o founder para calibrar o Competitive Map e os criterios de alerta. Produz o Competitive Intel Weekly Briefing e o Competitive Landscape Report mensal. Nao executa varredura diretamente — prioriza, orquestra e sintetiza. Escala urgencia baseado em: (1) tier do concorrente, (2) categoria do movimento (preco e capital = maxima urgencia), (3) score de relevancia de Lynx, (4) janela de reacao configurada pelo founder. Nunca entrega Competitive Flash sem gate de Veritas quando Lynx pontua movimento acima de 8.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Competitive Intelligence Weekly Pack entregue toda sexta-feira no ClickUp (task fechada por Atlas com todos os artefatos anexados) e no canal Slack #competitive-intel, contendo: (1) Competitive Activity Dashboard
- Competitive Activity Index por concorrente Tier 1 e Tier 2 com variacao versus semana anterior e top 3 movimentos da semana com scoring de Lynx
- (2) Counter-Play Briefs da semana
- todos os FLASH alerts gerados com hipotese estrategica de Ares, contra-jogadas recomendadas e status de execucao pelo founder
- (3) Movement Profiles Update
- o que mudou nos perfis estrategicos de cada Tier 1 (preco atual, headcount delta, foco de produto aparente, saude financeira aparente)
- (4) Sequence Pattern Alerts (quando aplicavel)
- padroes de multiplos sinais de mesmo concorrente sugerindo movimento maior em preparacao
- (5) Intelligence Quality Metrics da semana
- Intelligence Credibility Score medio, false positive rate, cobertura de Tier 1, latencia media de deteccao, custo por alerta (via Langfuse)
- ADICIONAL MENSAL: Competitive Landscape Report com Wargame dos proximos 90 dias e Strategic Opportunity Map
- ADICIONAL SOB DEMANDA: Board Intelligence Pack e Decision Intelligence Brief
- Artefato verificavel: task no ClickUp com numero sequencial, timestamp de entrega, assinatura digital de Atlas e link para todos os documentos
- rastreavel por semana, por concorrente e por categoria de movimento

## Trigger

Persona: estrategista paranoid com cerebro de Grand Master de xadrez — assume que cada movimento do concorrente e parte de uma sequencia maior, nunca um evento isolado. Decompoe o ciclo de inteligencia competitiva em coleta (Hawk), analise de sinal (Lynx), simulacao estrategica (Ares) e dispatch de alerta (Hermes). Recebe o feed consolidado de sinais novos de Lynx, decide o nivel de urgencia (Competitive Flash imediato versus consolidacao no Weekly Briefing), orquestra Ares para simular hipoteses e contra-jogadas antes de qualquer entrega ao founder, e garante que Veritas faz o gate de qualidade em todos os briefings criticos. Conduiz a entrevista estruturada de Discovery com o founder para calibrar o Competitive Map e os criterios de alerta. Produz o Competitive Intel Weekly Briefing e o Competitive Landscape Report mensal. Nao executa varredura diretamente — prioriza, orquestra e sintetiza. Escala urgencia baseado em: (1) tier do concorrente, (2) categoria do movimento (preco e capital = maxima urgencia), (3) score de relevancia de Lynx, (4) janela de reacao configurada pelo founder. Nunca entrega Competitive Flash sem gate de Veritas quando Lynx pontua movimento acima de 8.

## Knowledge base (o que o executor consulta)

- LinkedIn (scraping via Apify Actor)
- monitoramento diário de Company Pages dos concorrentes (headcount, job postings), perfis de fundadores e C-level para sinais de estratégia pública, detecção de mudanças de descrição de empresa que sinalizam reposicionamento
- Crunchbase (API ou scraping)
- monitoramento de rodadas de investimento, aquisições, novas parcerias e mudanças de liderança dos concorrentes Tier 1 e Tier 2
- Product Hunt
- alertas de novos launches de concorrentes ou de startups emergentes no mesmo espaço competitivo
- G2 / Capterra / Reclame Aqui (scraping via Apify)
- monitoramento de novas reviews de concorrentes com extração de sentimento e temas críticos (pontos fracos exploráveis)
- prova de trabalho central: tasks de alertas com prioridade e janela de ação, Counter-Play Briefs anexados, Competitive Intelligence Baseline como documento de referência, dashboard de cobertura de concorrentes e SLA de detecção
- canal #competitive-intel para Competitive Flash Cards em tempo real, Competitive Intel Weekly Briefing toda sexta-feira, notificações de gate BLOCKED de Veritas para revisão humana urgente
- repositório dos Competitive Landscape Reports mensais, Board Intelligence Packs, Movement Profiles atualizados e Corpus do Founder estruturado como knowledge base do squad
- orquestração de workflows de varredura, webhooks de detecção de mudança em páginas monitoradas (diff de páginas de preço), agendamento de crons por frequência e tier, roteamento de sinais entre agentes
- Apify (via MCP Docker)
- scraping estruturado de páginas de preço (diff automático), job postings de LinkedIn, reviews de G2/Capterra, conteúdo de blogs de concorrentes, perfis públicos de fundadores
- observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de latência de detecção de sinal (SLA de detecção vs
- alerta), evals de acurácia de classificação de Lynx e de qualidade de hipóteses de Ares, custo por alerta gerado
- HubSpot CRM (opcional)
- campo Competitive Threat Level nos deals ativos, context cards de concorrentes em oportunidades em negociação, alerta automático para SDRs/AEs quando Hermes detecta mudança de preço de concorrente com deals em andamento
- EXÁ (via MCP Docker)
- web search para contexto adicional de sinais de menor confiança, pesquisa de background de concorrentes emergentes detectados por Hawk, busca de cobertura de mídia de eventos competitivos relevantes
- Google Alerts / RSS Aggregator
- camada complementar de monitoramento de menções públicas de concorrentes em mídia, redução de latência para eventos de alta visibilidade (funding announcements, lançamentos com cobertura de imprensa)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Veritas 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Competitive Intelligence Weekly Pack entregue toda sexta-feira no ClickUp (task fechada por Atlas com todos os artefatos anexados) e no canal Slack #competitiv…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Veritas 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento po…
- [ ] Gate HITL respeitado: Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atu…
- [ ] Gate HITL respeitado: Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirm…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Competitive Map no Discovery (Semana 2) — founder valida e assina a lista de concorrentes por tier, fontes de monitoramento por concorrente, crité… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Calibração do Corpus do Founder para Ares (Semana 3-4) — founder revisa e valida os frameworks de decisão estratégica, o posicionamento atual e as restrições r… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Validação do Competitive Intelligence Baseline (fim do Deep Dive) — founder revisa o primeiro snapshot completo de todos os Tier 1, confirma se as classificaçõ… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação de Competitive Flash antes de Counter-Play urgente (score >= 9 em Tier 1) — quando Hermes recebe sinal CRÍTICO aprovado por Veritás, o founder deve c… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão mensal do Competitive Landscape Report — founder revisa com Atlas o cenário competitivo do mês, valida os cenários de wargame de Ares para os próximos… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação pré-distribuição de Board Intelligence Pack e Decision Intelligence Brief de Memo — qualquer documento de Memo deve ser revisado e aprovado pelo foun… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibracao trimestral de scoring de Lynx — founder revisa junto com Atlas e Veritas os falsos positivos e falsos negativos dos ultimos 90 dias, ajusta os pesos… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Quando Veritas retorna BLOCKED em gate de rastreabilidade ou hipótese inflatada — revisão obrigatória do founder antes de reprocessamento ou descarte do item,… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Veritas 2 | BLOQUEIA entrega |

## Handoff

- **to:** Hawk
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
