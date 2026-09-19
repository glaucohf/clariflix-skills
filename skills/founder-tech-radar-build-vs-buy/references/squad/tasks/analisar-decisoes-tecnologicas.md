---
task: kai()
responsavel: "Kai"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Necessidade tecnica descrita (o que precisa ser resolvido"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "funcional e nao-funcional), Radar Score e posicao atual no Tech Radar do componente em questao fornecidos por Nox, sinais de ecossistema de Vera sobre alternativas disponiveis e seus estados de maturidade, dados de TCO historicos de componentes similares ja analisados (calibracao de estimativas), pesos das 7 dimensoes do BvB configurados pelo founder no Discovery (o que e mais importante para este negocio especifico), restricoes tecnicas e de arquitetura fornecidas pelo CTO ou founder via Lens (constraints nao-negociaveis), budget e timeline reais disponivel para implementacao"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "BvB Analysis Report completo (estrutura padrao: Executive Summary com recomendacao e nivel de confianca, Tabela BvB-7 com pontuacao por dimensao e peso, TCO Comparison (build vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "buy, 24-36 meses), Risk Matrix (riscos de cada opcao com probabilidade e impacto), Vendor Selection Matrix quando aplicavel com top 3 alternativas ranqueadas, Recomendacao Final com criterios explicitos e pre-condicoes para revisao da decisao"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "ex: 'manter recomendacao de Buy enquanto Lock-in Score do vendor escolhido permanecer abaixo de 7 e preco nao crescer mais de 20% ao ano')"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Vendor Shortlist detalhada para decisoes de 'buy' (top 3 vendors com pros/cons por criterio, links para demos, trials e referencias de clientes verificaveis), Decision Criteria Card (uma pagina"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "o que precisaria mudar para reconsiderar a decisao, para revisao anual pelo founder/CTO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lens triggra BvB Analysis para: (a) nova necessidade tecnica identificada pelo founder/CTO acima do threshold de criticidade definido no Discovery; (b) componente Tier 1 ou Tier 2 que Nox moveu para…"
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

# Analisar Decisoes Tecnologicas

**Task ID:** `kai()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Decisoes Tecnologicas |
| **status** | `pending` |
| **responsible_executor** | Kai (Kai — Arquiteto de Decisoes Build-vs-Buy) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Motor de analise racional de decisoes de tecnologia — aplica o framework BvB-7 para cada decisao de componente acima do threshold de criticidade, produzindo recomendacoes rastreavels com criterios explicitos e nivel de confianca declarado. Nao tem opinioes proprias sobre tecnologia — tem metodologia e dados. O framework BvB-7 avalia sete dimensoes com pesos configurados pelo founder no Discovery: (1) CUSTO TOTAL DE PROPRIEDADE (TCO) — custo de build: estimativa de horas de engenheiro x rate, custo de manutencao perpetua estimada como % do build inicial, custo de opportunity cost de capacidade desviada; custo de buy: licenca, infra, integracao, suporte tecnico, treinamento do time; horizonte de analise configuravel (tipicamente 24-36 meses); (2) TIME-TO-VALUE — quanto tempo leva para ter funcionalidade equivalente com cada opcao, e qual e o custo do atraso para o negocio (receita nao gerada, clientes nao servidos, problema nao resolvido); (3) DIFERENCIACAO ESTRATEGICA — este componente e parte do diferencial competitivo do produto? (regra de ouro: so construir quando da vantagem que nenhum vendor pode replicar — para todo o resto, buy); (4) RISCO DE LOCK-IN — qual e o custo de saida se a opcao 'buy' piorar (preco, features, suporte)? existe alternativa equivalente? qual e a facilidade de migracao? pontuado como Lock-in Score 0-10; (5) MATURIDADE DE ALTERNATIVAS — a opcao 'buy' mais adequada e suficientemente madura para producao critica? qual e o track record em empresas de porte similar? ha referencias verificaveis?; (6) DEMANDA DE MANUTENCAO INTERNA — se build, qual e o overhead de manutencao perpetua em % da capacidade do time de engenharia?; (7) ALINHAMENTO COM TRAJETORIA TECNICA — a escolha e compativel com a direcao tecnica de longo prazo da empresa? nao cria acoplamento indesejado com outros componentes? Para decisoes de 'buy', Kai tambem executa Vendor Selection Matrix quando ha multiplas alternativas — pontuacao por criterios ponderados (seguranca, integracao, suporte, precificacao, roadmap, comunidade) com dados coletados por Vera.

## Input

- Necessidade tecnica descrita (o que precisa ser resolvido
- funcional e nao-funcional), Radar Score e posicao atual no Tech Radar do componente em questao fornecidos por Nox, sinais de ecossistema de Vera sobre alternativas disponiveis e seus estados de maturidade, dados de TCO historicos de componentes similares ja analisados (calibracao de estimativas), pesos das 7 dimensoes do BvB configurados pelo founder no Discovery (o que e mais importante para este negocio especifico), restricoes tecnicas e de arquitetura fornecidas pelo CTO ou founder via Lens (constraints nao-negociaveis), budget e timeline reais disponivel para implementacao

## Output

- BvB Analysis Report completo (estrutura padrao: Executive Summary com recomendacao e nivel de confianca, Tabela BvB-7 com pontuacao por dimensao e peso, TCO Comparison (build vs
- buy, 24-36 meses), Risk Matrix (riscos de cada opcao com probabilidade e impacto), Vendor Selection Matrix quando aplicavel com top 3 alternativas ranqueadas, Recomendacao Final com criterios explicitos e pre-condicoes para revisao da decisao
- ex: 'manter recomendacao de Buy enquanto Lock-in Score do vendor escolhido permanecer abaixo de 7 e preco nao crescer mais de 20% ao ano')
- Vendor Shortlist detalhada para decisoes de 'buy' (top 3 vendors com pros/cons por criterio, links para demos, trials e referencias de clientes verificaveis), Decision Criteria Card (uma pagina
- o que precisaria mudar para reconsiderar a decisao, para revisao anual pelo founder/CTO)

## Trigger

Lens triggra BvB Analysis para: (a) nova necessidade tecnica identificada pelo founder/CTO acima do threshold de criticidade definido no Discovery; (b) componente Tier 1 ou Tier 2 que Nox moveu para quadrante HOLD ou ASSESS baseado em sinais de Vera; (c) vendor Tier 1 com Vendor Health Score de Nox abaixo de 6 (revisao de alternativas urgente); (d) renovacao de contrato de vendor acima de threshold de custo (janela natural para reavaliar); (e) ciclo trimestral de revisao dos items em HOLD do Tech Radar (sao oportunidades de substituicao planejada); (f) founder ou CTO traz decisao tecnica ad-hoc urgente (modo prioritario, BvB em 48-72h)

## Knowledge base (o que o executor consulta)

- Historico completo de BvB Analyses anteriores com outcomes reais (o que foi recomendado, o que foi decidido, qual foi o resultado
- ciclo de aprendizado critico para calibrar estimativas futuras), biblioteca de TCO benchmarks por categoria de componente (quanto custa construir e manter um sistema de autenticacao, um sistema de billing, um pipeline de dados, um motor de busca
- benchmarks de mercado calibrados por tamanho de time e setor), Vendor Evaluation Database
- resultados de avaliacoes de vendors por categoria com scores historicos (para nao repetir due diligence de vendors ja avaliados), pesos BvB-7 configurados pelo founder (o que e mais importante para este negocio
- alta aversao a lock-in? foco em time-to-market? otimizacao de custo?), criterios de diferenciacao estrategica do negocio (quais capacidades tecnicas sao core business e devem ser construidas internamente versus commodities que devem ser compradas)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Necessidade tecnica descrita (o que precisa ser resolvido).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (BvB Analysis Report completo (estrutura padrao: Executive Summary com recomendacao e nivel de confianca, Tabela BvB-7 c…) e persistir no artefato do squad.
4. Entregar ao critic ARIA 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: BvB Analysis Report completo (estrutura padrao: Executive Summary com recomendacao e nivel de confianca, Tabela BvB-7 com pontuacao por dimensao e peso, TCO Co…
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

- **to:** Vox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
