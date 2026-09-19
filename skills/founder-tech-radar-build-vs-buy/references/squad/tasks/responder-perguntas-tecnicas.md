---
task: vox()
responsavel: "Vox"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Pergunta tecnica do founder (free-form via Slack ou interface configurada), contexto relevante do Stack Audit e Tech Radar atual (fornecido automaticamente por Nox via contexto do squad), Corpus do Founder Tecnico (frameworks de decisao, opinioes sobre categorias de tecnologia, restricoes inegociaveis, historico de decisoes com outcomes documentados), BvB Analyses recentes de Kai para contexto de decisoes em andamento, sinais recentes de Vera que sejam relevantes para a pergunta"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Quick Answer estruturada (para Quick Consult Mode: contexto da resposta no caso especifico + recomendacao + caveats + pre-condicoes para rever a resposta"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "sempre com nivel de confianca declarado e indicacao do que Vox nao sabe com certeza), Pre-Decision Brief (para Decision Prep Mode: 5-7 perguntas criticas nao respondidas + 3-5 riscos nao considerados + referencias especificas para verificar antes de decidir"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "com prazo sugerido para tomada de decisao), Founder Tech Talking Points (para Tech Briefing Mode: narrativa estruturada da decisao com linguagem calibrada para a audiencia, analogias para audiencias nao tecnicas, dados de benchmark para audiencias tecnicas)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Mensagem direta do founder para Vox via Slack ou interface configurada (Quick Consult, latencia maxima de 30min para Quick Answer); Lens identifica que decisao tecnica iminente se beneficiaria de Pre…"
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

# Responder Perguntas Técnicas

**Task ID:** `vox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Responder Perguntas Técnicas |
| **status** | `pending` |
| **responsible_executor** | Vox (Vox — Founder Clone Tech Advisor) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Replica cognitiva do expert tecnico do founder — responde a perguntas tecnicas com o raciocinio, os frameworks e o tom de um arquiteto senior treinado no corpus especifico do negocio. Funciona como o CTO virtual do founder para consultas rapidas que nao justificam uma BvB Analysis completa de Kai ou uma pesquisa de ecossistema de Vera, mas precisam de mais do que uma resposta generica. Opera em tres modos: (1) QUICK CONSULT MODE — responde perguntas tecnicas ad-hoc do founder ('qual a diferenca real entre Postgres e MongoDB para este caso de uso especifico?', 'o que acontece se a gente escalar o Shopify Plus?', 'faz sentido usar serverless para esta funcao?') com a logica e os tradeoffs especificos do contexto do negocio — nao respostas genericas de Stack Overflow, mas raciocinios contextualizados com as restricoes, a trajetoria tecnica e o stack atual da empresa; (2) DECISION PREP MODE — quando o founder ou CTO esta prestes a tomar uma decisao tecnica, Vox prepara um Pre-Decision Brief: o que voce precisa saber antes de tomar esta decisao (perguntas que voce ainda nao fez, riscos que voce ainda nao considerou, referencias que voce deveria verificar) — funciona como 'advogado do diabo' tecnico antes da decisao final; (3) TECH BRIEFING MODE — quando o founder precisa conversar com um CTO, board tecnico ou investidor sobre uma decisao tecnica, Vox prepara o Founder Tech Talking Points: como explicar a decisao tomada, as alternativas consideradas e o raciocinio por tras dela com a linguagem certa para o audiencia especifica (board nao tecnico, investidor tecnico, CTO potencial, engenheiro senior). Vox usa o Corpus do Founder Tecnico — um conjunto de documentos que capturam o raciocinio tecnico, as opinioes consolidadas e as restricoes inegociaveis do founder sobre tecnologia.

## Input

- Pergunta tecnica do founder (free-form via Slack ou interface configurada), contexto relevante do Stack Audit e Tech Radar atual (fornecido automaticamente por Nox via contexto do squad), Corpus do Founder Tecnico (frameworks de decisao, opinioes sobre categorias de tecnologia, restricoes inegociaveis, historico de decisoes com outcomes documentados), BvB Analyses recentes de Kai para contexto de decisoes em andamento, sinais recentes de Vera que sejam relevantes para a pergunta

## Output

- Quick Answer estruturada (para Quick Consult Mode: contexto da resposta no caso especifico + recomendacao + caveats + pre-condicoes para rever a resposta
- sempre com nivel de confianca declarado e indicacao do que Vox nao sabe com certeza), Pre-Decision Brief (para Decision Prep Mode: 5-7 perguntas criticas nao respondidas + 3-5 riscos nao considerados + referencias especificas para verificar antes de decidir
- com prazo sugerido para tomada de decisao), Founder Tech Talking Points (para Tech Briefing Mode: narrativa estruturada da decisao com linguagem calibrada para a audiencia, analogias para audiencias nao tecnicas, dados de benchmark para audiencias tecnicas)

## Trigger

Mensagem direta do founder para Vox via Slack ou interface configurada (Quick Consult, latencia maxima de 30min para Quick Answer); Lens identifica que decisao tecnica iminente se beneficiaria de Pre-Decision Brief antes de triggar BvB Analysis completa de Kai (Prep Brief em menos de 2h); founder agenda reuniao tecnica com board, CTO, investidor ou candidato senior tecnico (Tech Briefing Mode com 24h de antecedencia); ciclo mensal de Tech Q&A sintetico onde Vox consolida as perguntas mais frequentes do mes e as respostas em FAQ tecnico para o knowledge base

## Knowledge base (o que o executor consulta)

- Corpus do Founder Tecnico
- documento vivo com: opinioes tecnicas consolidadas do founder por categoria (cloud, dados, frontend, backend, integracao), decisoes tecnicas historicas com contexto e outcomes (o que foi decidido, por que, o que aconteceu), restricoes inegociaveis de arquitetura (ex: 'nunca mais vendor sem SLA de 99.9%', 'sempre open-source para componentes de dados sensiveis'), principios tecnicos do founder (ex: 'prefiro pagar mais por servico gerenciado do que manter infra proprio abaixo de R$50k/mes de receita'), analogias tecnicas preferidas pelo founder para comunicacao com nao-tecnicos (ciclo de aprendizado de Vox para calibrar o tom correto), Tech Radar atual e BvB Analyses recentes para contexto de respostas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Pergunta tecnica do founder (free-form via Slack ou interface configurada), contexto relevante do Stack Audit e Tech Ra…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Quick Answer estruturada (para Quick Consult Mode: contexto da resposta no caso especifico + recomendacao + caveats + p…) e persistir no artefato do squad.
4. Entregar ao critic ARIA 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Quick Answer estruturada (para Quick Consult Mode: contexto da resposta no caso especifico + recomendacao + caveats + pre-condicoes para rever a resposta
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

- **to:** Aegis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
