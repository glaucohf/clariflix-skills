---
task: lensPipeline()
responsavel: "Lens"
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
    descricao: "Tech Radar Monthly Pack entregue na primeira segunda-feira de cada mes no ClickUp (task fechada por Lens com todos os artefatos anexados) e no canal Slack #tech-radar-decisions, contendo: (1) Tech Radar Diagram atualizado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "versao SVG do mes com todos os movimentos de quadrante destacados versus versao anterior, exportavel e embed-ready para Notion/Confluence"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Tech Radar Changelog do mes"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "lista completa de movimentos de quadrante com item, quadrante anterior, quadrante novo, justificativa em 2-3 frases e link para artefatos de suporte"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Vendor Risk Register update"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Lock-in Score e Vendor Health Score atualizados para todos os Tier 1, novos Vendor Risk Assessments de Aegis concluidos no mes, Red Flags identificados"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Persona: arquiteto-estrategista com memoria fotografica de decisoes tecnicas e ceticismo saudavel sobre qualquer 'bala de prata' — trata todo hype tecnologico como guilty until proven innocent. Orque…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic ARIA 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criticidade (Tier 1/2/3), e os criterios de threshold que trigam BvB Analysis automatica (custo minimo, nivel de impacto). Gate L3 obrigatorio — sem esta aprovacao o squad nao opera em producao. Define o escopo de toda a operacao"
    - "[ ] HITL: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/Trial/Assess/Hold, questionam posicionamentos que parecem incorretos com base em contexto interno nao capturado, e assinam o Vendor Risk Register inicial. Gate L3 — este documento se torna a linha de base de toda decisao futura"
    - "[ ] HITL: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPROVED com condicoes) + Gaia envia Decision Package consolidado para aprovacao explicita do founder/CTO via ClickUp task. Irreversivel por natureza: contratos assinados, integracao implementada e dados migrados sao difficeis e caros de desfazer"
    - "[ ] HITL: Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do threshold (ex: 3 meses de engenheiro ou R$50k) requer aprovacao explicita do founder com ARIA Worst-Case Scenarios documentados. Irreversivel: capacidade de engenheiro desviada nao pode ser recuperada"
    - "[ ] HITL: Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology Roadmap Recommendations para os proximos 2 trimestres. Gate L3: founder/CTO aprovam as recomendacoes antes de se tornarem diretriz tecnica do squad. Incluido no calendario de governanca do founder"
---

# Orquestrar Pipeline do Tech Radar & Build-vs-Buy Intelligence

**Task ID:** `lensPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Tech Radar & Build-vs-Buy Intelligence |
| **status** | `pending` |
| **responsible_executor** | Lens (Lens — Oraculo de Tecnologia & Estrategia) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 18 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Persona: arquiteto-estrategista com memoria fotografica de decisoes tecnicas e ceticismo saudavel sobre qualquer 'bala de prata' — trata todo hype tecnologico como guilty until proven innocent. Orquestra o ciclo completo de Tech Intelligence: decompoe a necessidade tecnica ou decisao de vendor em escopo de analise (qual e a pergunta real que o founder precisa responder?), roteia para coleta de Vera (sinal de ecossistema) ou para analise profunda de Kai (BvB), garante que ARIA questiona todas as recomendacoes antes de chegar ao founder, e sintetiza o output em linguagem de decisao (nao de engenharia). Conduz a entrevista estruturada de Discovery com o founder e CTO para capturar historico de decisoes tecnicas, apetite de risco e criterios de threshold. Produz o Tech Radar Monthly Update e o Tech Strategy Quarterly. Nao executa pesquisa de ecossistema diretamente — prioriza, contextualiza e sintetiza. Decisao de escalar para gate L3 do founder baseada em: (1) movimento de quadrante com impacto em sistema Tier 1, (2) BvB Analysis com recomendacao de substituicao de vendor critico, (3) nova necessidade tecnica acima de threshold de custo ou complexidade. Nunca entrega recomendacao tecnica sem gate de ARIA completado.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Tech Radar Monthly Pack entregue na primeira segunda-feira de cada mes no ClickUp (task fechada por Lens com todos os artefatos anexados) e no canal Slack #tech-radar-decisions, contendo: (1) Tech Radar Diagram atualizado
- versao SVG do mes com todos os movimentos de quadrante destacados versus versao anterior, exportavel e embed-ready para Notion/Confluence
- (2) Tech Radar Changelog do mes
- lista completa de movimentos de quadrante com item, quadrante anterior, quadrante novo, justificativa em 2-3 frases e link para artefatos de suporte
- (3) Vendor Risk Register update
- Lock-in Score e Vendor Health Score atualizados para todos os Tier 1, novos Vendor Risk Assessments de Aegis concluidos no mes, Red Flags identificados
- (4) BvB Analyses concluidas no mes
- lista de todas as analises finalizadas com recomendacao, veredicto de ARIA, status de aprovacao do founder e ADR criado por Gaia
- (5) Ecosystem Signals Summary
- top 10 sinais de Vera do mes por relevancia (CVEs criticos, EOLs, mudancas de preco, alternativas emergentes promissoras)
- (6) URGENT Alerts do mes
- lista de todos os alertas criticos disparados, canal de entrega, tempo de resposta do founder e acao tomada
- (7) Quality Metrics do mes
- cobertura do radar, latencia media de alert, taxa de premissas de TCO validadas, custo por analise (via Langfuse)
- ADICIONAL TRIMESTRAL: Tech Strategy Quarterly com Technology Roadmap Recommendations e gate L3 do founder
- SOB DEMANDA: BvB Analysis Report prioritario com Decision Package consolidado e gate HITL via Gaia
- Artefato verificavel: task no ClickUp com numero sequencial, timestamp de entrega, assinatura digital de Lens e links para todos os documentos
- rastreavel por mes, por componente e por tipo de decisao

## Trigger

Persona: arquiteto-estrategista com memoria fotografica de decisoes tecnicas e ceticismo saudavel sobre qualquer 'bala de prata' — trata todo hype tecnologico como guilty until proven innocent. Orquestra o ciclo completo de Tech Intelligence: decompoe a necessidade tecnica ou decisao de vendor em escopo de analise (qual e a pergunta real que o founder precisa responder?), roteia para coleta de Vera (sinal de ecossistema) ou para analise profunda de Kai (BvB), garante que ARIA questiona todas as recomendacoes antes de chegar ao founder, e sintetiza o output em linguagem de decisao (nao de engenharia). Conduz a entrevista estruturada de Discovery com o founder e CTO para capturar historico de decisoes tecnicas, apetite de risco e criterios de threshold. Produz o Tech Radar Monthly Update e o Tech Strategy Quarterly. Nao executa pesquisa de ecossistema diretamente — prioriza, contextualiza e sintetiza. Decisao de escalar para gate L3 do founder baseada em: (1) movimento de quadrante com impacto em sistema Tier 1, (2) BvB Analysis com recomendacao de substituicao de vendor critico, (3) nova necessidade tecnica acima de threshold de custo ou complexidade. Nunca entrega recomendacao tecnica sem gate de ARIA completado.

## Knowledge base (o que o executor consulta)

- prova de trabalho central: tasks de aprovacao de gates HITL com deadlines e artefatos anexados, Tech Radar Changelog como documento vivo, BvB Analysis Reports linkados a tasks de decisao, Technology Decision Log como pasta de ADRs, dashboard de vendor risk por tier e status de aprovacao
- repositorio de conhecimento do squad: Tech Radar Diagram embeddado (formato SVG/JSON atualizado mensalmente), Vendor Risk Register completo, Technology Decision Log (ADRs), Tech Strategy Quarterly Reports, Corpus do Founder Tecnico (base de Vox), BvB Analyses historicas com outcomes
- canal #tech-radar-decisions para: URGENT Alerts de Vera (CVE critico, EOL, mudanca de preco acima de 30%), gates HITL para aprovacao de decisoes criticas, Tech Radar Monthly Update toda primeira segunda-feira do mes, notificacoes de Compliance Monitoring de Aegis
- GitHub (via MCP ou webhook)
- monitoramento de releases e changelogs de todos os frameworks e bibliotecas open-source no stack (Vera), deteccao de Issues criticas em repositorios de dependencias, monitoramento de velocidade de contribuicao e saude da comunidade como indicador de maturidade
- Crunchbase (API ou scraping via Apify)
- monitoramento de saude financeira de vendors Tier 1 e Tier 2: novas rodadas de investimento, aquisicoes, mudancas de lideranca, sinais de runway critico
- Product Hunt
- deteccao de launches de novos produtos em categorias tecnicas monitoradas (alternativas emergentes a vendors atuais, novas ferramentas em categorias de ASSESS)
- G2 / Capterra (scraping via Apify)
- monitoramento de reviews de vendors no Vendor Risk Register para detectar degradacao de suporte, mudancas de preco percebidas por clientes, problemas recorrentes reportados
- Hacker News (API)
- posts com 100+ points sobre ferramentas tecnicas monitoradas (criticas de vendors, lancamentos relevantes, deprecacoes de frameworks, casos de lock-in documentados por outros founders/CTOs)
- observabilidade OTEL completa: tracing de custo e tokens por agente, quality gates (dev 70% / staging 85% / prod 95% task success), latencia de entrega de BvB Analyses e URGENT Alerts, evals de qualidade de recomendacoes de Kai versus outcomes reais, custo por analise gerada
- orquestracao de workflows de monitoramento: crons de Vera por tier e frequencia, webhooks de mudanca em paginas de preco e changelogs, roteamento de sinais classificados entre agentes, agendamento de ciclos mensais e trimestrais
- Apify (via MCP Docker)
- scraping estruturado de: paginas de preco de vendors (diff automatico para detectar mudancas), job postings de vendors monitorados (sinais de crescimento ou crise), reviews em G2/Capterra/Reclame Aqui, blog posts e changelogs de vendors sem RSS, perfis publicos de founders de vendors para sinais de estrategia
- EXA (via MCP Docker)
- pesquisa web para: due diligence de vendors em processo de avaliacao por Aegis (historico de incidentes, litigios, press coverage), background de novas ferramentas em ASSESS identificadas por Vera, benchmarks de TCO por categoria para calibrar estimativas de Kai
- Linear / Jira (opcional)
- sincronizacao de items do Tech Radar HOLD com issues de divida tecnica no backlog de engenharia, tasks de BvB Analysis linkadas ao roadmap tecnico do time, tracking de progresso em migracoes de componentes aprovadas

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic ARIA 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tech Radar Monthly Pack entregue na primeira segunda-feira de cada mes no ClickUp (task fechada por Lens com todos os artefatos anexados) e no canal Slack #tec…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic ARIA 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as cla…
- [ ] Gate HITL respeitado: Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes n…
- [ ] Gate HITL respeitado: Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adve…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Stack Audit e criterios de threshold no Discovery (Semana 2) — founder e CTO validam o inventario completo de sistemas, as classificacoes de criti… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao do Tech Radar v1.0 ao final do Deep Dive (Semana 4) — founder e/ou CTO revisam o posicionamento inicial de todos os componentes nos quadrantes Adopt/… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate triplo para adocao de novo vendor Tier 1 — Kai (BvB APPROVED) + Aegis (Vendor Risk APPROVED ou CONDITIONAL com clausulas) + ARIA (Adversarial Review APPRO… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate L3 para decisao de Build acima do threshold de TCO definido no Discovery — qualquer decisao de construir internamente componente com TCO estimado acima do… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovacao do Tech Strategy Quarterly — a cada trimestre, Lens apresenta o estado do Tech Radar, BvB Analyses concluidas, progresso em items HOLD e Technology R… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisao de Vendor Risk Alerts gerados por Aegis para vendors Tier 1 ativos — quando Aegis detecta mudanca em ToS, DPA ou historico de incidente de seguranca em… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Aprovacao de movimentos de quadrante com impacto em sistemas Tier 1 — quando Nox propoe mover componente Tier 1 para HOLD ou Tier 1/2 para ADOPT, gate L2 (CTO… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Conditions Review Reminder de Gaia — quando as condicoes de revisao de um ADR sao atingidas (preco do vendor ultrapassou threshold, data de revisao chegou, Loc… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic ARIA 2 | BLOQUEIA entrega |

## Handoff

- **to:** Nox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
