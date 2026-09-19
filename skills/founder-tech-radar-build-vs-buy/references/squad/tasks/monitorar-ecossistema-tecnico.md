---
task: vera()
responsavel: "Vera"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de componentes monitorados do Tech Radar com metadados por item (vendor, repositorio GitHub, feed de changelog, perfil do Crunchbase, pagina de preco, blog do vendor), criterios de filtragem por categoria de sinal configurados por Lens (quais categorias de ferramenta sao relevantes para este negocio especifico"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "ex: infra de dados, payment processing, email marketing), lista de empresas peers para monitoramento de stack (configurada no Discovery pelo founder/CTO), feeds RSS e webhooks configurados por vendor monitorado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Feed diario de sinais classificados (JSON estruturado por componente: tipo de sinal, fonte, timestamp, classificacao URGENT/RELEVANT/REFERENCE, resumo de 2-3 frases do que mudou e por que importa para o stack), Ecosystem Radar Digest semanal (consolidacao de todos os sinais RELEVANT e REFERENCE da semana agrupados por categoria"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "novas alternativas identificadas, mudancas de vendor, tendencias emergentes), URGENT Alert imediato para Lens quando detecta CVE critico, EOL anunciado, ou mudanca de preco/modelo Tier 1 (latencia maxima de 4h entre deteccao e alerta), Technology Trend Report trimestral (tendencias de adocao no ecossistema, tecnologias em ascensao e declinio, novas categorias emergentes relevantes para o negocio)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diario automatico (changelogs e releases Tier 1 a cada 6h, newsletters e agregadores a cada 12h, Crunchbase e Product Hunt a cada 24h, Tier 2 e Tier 3 a cada 48h); webhook de deteccao de mudanca…"
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

# Monitorar Ecossistema Tecnico

**Task ID:** `vera()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Ecossistema Tecnico |
| **status** | `pending` |
| **responsible_executor** | Vera (Vera — Scout de Ecossistema Tecnico) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Antena continua do squad no ecossistema tecnico relevante — coleta sistematicamente sinais de evolucao do mercado de tecnologia para manter o Tech Radar vivo e alertar sobre mudancas que afetam o stack atual ou abrem oportunidades de melhoria. Opera em tres camadas de monitoramento: (1) STACK LAYER — monitora todos os componentes atualmente no Tech Radar da empresa: novos releases e changelogs (breaking changes, features relevantes, deprecacoes), issues de seguranca e CVEs criticos, mudancas de preco ou modelo de licenciamento, aquisicoes ou mudancas de controle (sinais de risco de vendor), e mensagens de fim de suporte (EOL/EOS) em frameworks e plataformas; (2) ECOSYSTEM LAYER — varre o ecossistema mais amplo para identificar alternativas emergentes aos vendors atuais e novas categorias de ferramentas relevantes para o negocio: Product Hunt daily digest filtrado por categorias tecnicas relevantes, Hacker News (posts com 100+ points sobre novas ferramentas ou criticas de vendors existentes), newsletters tecnicas (TLDR Tech, The Pragmatic Engineer, Pointer.io, Changelog), GitHub Trending e repositorios com crescimento explosivo em categorias monitoradas, Crunchbase para rodadas em startups de infra/dev tools que possam tornar vendors atuais obsoletos; (3) COMPETITIVE STACK LAYER — monitora sinais publicos do stack tecnico de empresas peers (job postings com requisitos tecnicos revelam adocao de ferramentas, engineering blog posts de concorrentes, entrevistas publicas do CTO). Vera classifica cada sinal coletado em tres categorias: URGENT (mudanca que requer acao imediata — CVE critico, EOL anunciado, mudanca de preco acima de 30%), RELEVANT (sinal que deve informar proxima atualizacao do Radar), REFERENCE (informacao de contexto sem acao imediata).

## Input

- Lista de componentes monitorados do Tech Radar com metadados por item (vendor, repositorio GitHub, feed de changelog, perfil do Crunchbase, pagina de preco, blog do vendor), criterios de filtragem por categoria de sinal configurados por Lens (quais categorias de ferramenta sao relevantes para este negocio especifico
- ex: infra de dados, payment processing, email marketing), lista de empresas peers para monitoramento de stack (configurada no Discovery pelo founder/CTO), feeds RSS e webhooks configurados por vendor monitorado

## Output

- Feed diario de sinais classificados (JSON estruturado por componente: tipo de sinal, fonte, timestamp, classificacao URGENT/RELEVANT/REFERENCE, resumo de 2-3 frases do que mudou e por que importa para o stack), Ecosystem Radar Digest semanal (consolidacao de todos os sinais RELEVANT e REFERENCE da semana agrupados por categoria
- novas alternativas identificadas, mudancas de vendor, tendencias emergentes), URGENT Alert imediato para Lens quando detecta CVE critico, EOL anunciado, ou mudanca de preco/modelo Tier 1 (latencia maxima de 4h entre deteccao e alerta), Technology Trend Report trimestral (tendencias de adocao no ecossistema, tecnologias em ascensao e declinio, novas categorias emergentes relevantes para o negocio)

## Trigger

Cron diario automatico (changelogs e releases Tier 1 a cada 6h, newsletters e agregadores a cada 12h, Crunchbase e Product Hunt a cada 24h, Tier 2 e Tier 3 a cada 48h); webhook de deteccao de mudanca em paginas de preco de vendors monitorados; URGENT Alert quando detecta CVE CVSS >= 7.0 em componente Tier 1, EOL announcement, ou mudanca de preco acima de 30%; ciclo semanal de Ecosystem Digest; ciclo trimestral de Technology Trend Report; novo componente adicionado ao stack pelo CTO triggra setup imediato de monitoramento em todas as fontes

## Knowledge base (o que o executor consulta)

- Catalogo completo de fontes de monitoramento por categoria de componente (cada tipo de tecnologia tem seu ecossistema de sinais especifico
- banco de dados tem HackerNews e DBA newsletters, frameworks JS tem GitHub e dev Twitter, vendors SaaS tem Crunchbase e G2), historico de 12 meses de sinais coletados por componente para detectar tendencias de velocidade de mudanca (vendor que nao lanca nada ha 6 meses e sinal diferente de vendor com releases frequentes), CVE database e feeds de seguranca por linguagem e framework monitorados, mapeamento de alternativas por categoria de ferramenta (para cada vendor Tier 1, quais sao as 3-5 alternativas mais maduras que Kai pode avaliar em BvB Analysis)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de componentes monitorados do Tech Radar com metadados por item (vendor, repositorio GitHub, feed de changelog, p…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Feed diario de sinais classificados (JSON estruturado por componente: tipo de sinal, fonte, timestamp, classificacao UR…) e persistir no artefato do squad.
4. Entregar ao critic ARIA 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Feed diario de sinais classificados (JSON estruturado por componente: tipo de sinal, fonte, timestamp, classificacao URGENT/RELEVANT/REFERENCE, resumo de 2-3 f…
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

- **to:** Kai
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
