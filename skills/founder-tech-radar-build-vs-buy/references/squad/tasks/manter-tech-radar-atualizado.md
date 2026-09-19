---
task: nox()
responsavel: "Nox"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stack Audit inicial validado pelo founder (lista de todos os sistemas com metadados de criticidade e custo), sinais do ecossistema classificados por Vera (novos releases, mudancas de vendor, launches de alternativas, deprecacoes), historico de BvB Analyses de Kai para atualizar posicionamento de componentes analisados, feedback do founder/CTO sobre items movidos de quadrante (ciclo de aprendizado), dados de uso e custo de integrações existentes (via MCP com ferramentas de observabilidade ou input manual do CTO)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tech Radar Diagram atualizado (formato visual com Adopt/Trial/Assess/Hold, exportavel como SVG e JSON para embed no Notion), Tech Radar Changelog (lista de todos os movimentos de quadrante com data, item, quadrante anterior, quadrante novo e justificativa em 2-3 frases), Vendor Risk Register atualizado com Lock-in Score e Vendor Health Score por vendor Tier 1/2, Stack Complexity Map (grafo de dependencias entre componentes para identificar pontos de alto acoplamento e risco de cascata), Radar Score por componente (0-10 composto para priorizar quais items precisam de BvB Analysis urgente)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Stack Audit inicial no Discovery (setup completo); sinais de Vera indicando mudanca relevante no ecossistema de um componente monitorado (trigger de reavaliacao de quadrante); BvB Analysis de Kai con…"
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

# Manter Tech Radar Atualizado

**Task ID:** `nox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Tech Radar & Build-vs-Buy Intelligence

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Manter Tech Radar Atualizado |
| **status** | `pending` |
| **responsible_executor** | Nox (Nox — Cartografo do Stack & Tech Radar Keeper) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Guardiao vivo do Tech Radar — responsavel por manter o mapa atualizado de todo o ecossistema tecnico da empresa, posicionar corretamente cada componente nos quatro quadrantes (Adopt/Trial/Assess/Hold) com base em dados objetivos, e detectar quando um item deve mudar de quadrante com base nos sinais coletados por Vera. Opera em dois modos: (1) MODO AUDIT (Discovery e revisoes periodicas) — executa o Stack Audit completo levantando inventario de todos os sistemas, frameworks, bibliotecas e vendors ativos com seis dimensoes de avaliacao por item: versao e data de adocao, custo total (licenca + infra + manutencao interna em horas de engenheiro), nivel de uso (critico/relevante/legado), numero de integrações com outros sistemas (grau de acoplamento), bus factor de conhecimento interno, e data de ultimo review formal; (2) MODO RADAR (operacao continua) — processa os sinais de Vera para determinar se algum componente deve mudar de quadrante, calcula o Radar Score de cada item (composito de maturidade, custo, risco de lock-in, saude do vendor, alternativas disponiveis), e atualiza o Tech Radar Diagram com justificativas documentadas para cada posicao. Tambem mantem o Vendor Risk Register — registro vivo de todos os vendors Tier 1 e Tier 2 com: Lock-in Score (0-10, onde 10 = dependencia total sem alternativa), Migration Cost Estimate (horas de engenheiro para substituir), Vendor Health Score (saude financeira, crescimento, suporte — atualizado trimestral por Vera), e Status (Stable/Watch/At-Risk/Replace).

## Input

- Stack Audit inicial validado pelo founder (lista de todos os sistemas com metadados de criticidade e custo), sinais do ecossistema classificados por Vera (novos releases, mudancas de vendor, launches de alternativas, deprecacoes), historico de BvB Analyses de Kai para atualizar posicionamento de componentes analisados, feedback do founder/CTO sobre items movidos de quadrante (ciclo de aprendizado), dados de uso e custo de integrações existentes (via MCP com ferramentas de observabilidade ou input manual do CTO)

## Output

- Tech Radar Diagram atualizado (formato visual com Adopt/Trial/Assess/Hold, exportavel como SVG e JSON para embed no Notion), Tech Radar Changelog (lista de todos os movimentos de quadrante com data, item, quadrante anterior, quadrante novo e justificativa em 2-3 frases), Vendor Risk Register atualizado com Lock-in Score e Vendor Health Score por vendor Tier 1/2, Stack Complexity Map (grafo de dependencias entre componentes para identificar pontos de alto acoplamento e risco de cascata), Radar Score por componente (0-10 composto para priorizar quais items precisam de BvB Analysis urgente)

## Trigger

Stack Audit inicial no Discovery (setup completo); sinais de Vera indicando mudanca relevante no ecossistema de um componente monitorado (trigger de reavaliacao de quadrante); BvB Analysis de Kai concluida com recomendacao de substituicao ou adocao (atualiza posicao do componente e adiciona alternativa avaliada ao Radar); ciclo mensal de atualizacao do Tech Radar para o Monthly Update de Lens; ciclo trimestral para o Tech Strategy Quarterly; founder ou CTO adiciona novo vendor ou sistema ao stack (trigger de catalogacao imediata); qualquer vendor Tier 1 com Vendor Health Score abaixo de 6 triggra alerta para Lens

## Knowledge base (o que o executor consulta)

- Stack Audit historico completo com todas as versoes e datas de adocao de todos os componentes (arquivo vivo, nao snapshot), Tech Radar de todas as versoes anteriores com historico de movimentos de quadrante para analise de trajetoria, Vendor Risk Register com historico de Vendor Health Scores e Lock-in Scores por trimestre, biblioteca de criterios de posicionamento por categoria de componente (o que define ADOPT para um banco de dados versus para um framework de frontend versus para um servico de email marketing sao criterios diferentes), mapeamento de integracao entre todos os componentes (quem depende de quem
- essencial para calcular custo real de substituicao e risco de cascata)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stack Audit inicial validado pelo founder (lista de todos os sistemas com metadados de criticidade e custo), sinais do…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tech Radar Diagram atualizado (formato visual com Adopt/Trial/Assess/Hold, exportavel como SVG e JSON para embed no Not…) e persistir no artefato do squad.
4. Entregar ao critic ARIA 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tech Radar Diagram atualizado (formato visual com Adopt/Trial/Assess/Hold, exportavel como SVG e JSON para embed no Notion), Tech Radar Changelog (lista de tod…
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

- **to:** Vera
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
