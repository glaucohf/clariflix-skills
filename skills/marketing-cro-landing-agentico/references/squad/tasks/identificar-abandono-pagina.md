---
task: hera()
responsavel: "Hera"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Acesso a Hotjar/Microsoft Clarity (gravacoes e heatmaps), export de dados do Google Analytics 4 (funil de conversao, comportamento por segmento), taxa de rejeicao por fonte de trafego e dispositivo, resultados de experimentos encerrados pelo Darwin, feedback qualitativo de vendas sobre objecoes pre-compra"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mapa de Fricções do Funil (por etapa, com evidência de comportamento e severidade), Behavioral Insights Report por experimento encerrado (o que o comportamento explica sobre o resultado), lista priorizada de hipóteses de CRO com evidência comportamental, análise de segmento (desktop vs mobile, orgânico vs pago vs remarketing)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Início de ciclo Discovery; encerramento de experimento pelo Darwin (trigger automático para análise pós-teste); ciclo quinzenal de revisão de comportamento; Maestro solicita análise específica de seg…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Rex 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção"
    - "[ ] HITL: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final"
    - "[ ] HITL: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)"
    - "[ ] HITL: Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)"
    - "[ ] HITL: Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)"
---

# Identificar Abandono Página

**Task ID:** `hera()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Identificar Abandono Página |
| **status** | `pending` |
| **responsible_executor** | Hera (Hera — Behavioral Analyst) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analista comportamental do squad. Interpreta dados quantitativos (heatmaps, gravações de sessão, funil de conversão, scroll depth, tempo na página, taxa de rejeição por dispositivo/fonte) e qualitativos (pesquisas on-exit, feedback de vendas sobre objeções comuns) para identificar onde e por que os usuários abandonam a página. Gera o mapa de fricções do funil com evidências de comportamento. Principal executor do Discovery e do ciclo de análise pós-experimento. Alias: 'Hera' — deusa da perspicácia que vê o que os outros não veem nos dados.

## Input

- Acesso a Hotjar/Microsoft Clarity (gravacoes e heatmaps), export de dados do Google Analytics 4 (funil de conversao, comportamento por segmento), taxa de rejeicao por fonte de trafego e dispositivo, resultados de experimentos encerrados pelo Darwin, feedback qualitativo de vendas sobre objecoes pre-compra

## Output

- Mapa de Fricções do Funil (por etapa, com evidência de comportamento e severidade), Behavioral Insights Report por experimento encerrado (o que o comportamento explica sobre o resultado), lista priorizada de hipóteses de CRO com evidência comportamental, análise de segmento (desktop vs mobile, orgânico vs pago vs remarketing)

## Trigger

Início de ciclo Discovery; encerramento de experimento pelo Darwin (trigger automático para análise pós-teste); ciclo quinzenal de revisão de comportamento; Maestro solicita análise específica de segmento; taxa de conversão cai > 15% em 7 dias (alerta de anomalia)

## Knowledge base (o que o executor consulta)

- Histórico de heatmaps e gravações de sessão das últimas 8 semanas, funis de conversão por fonte e dispositivo no GA4, resultados de todos os experimentos anteriores com contexto comportamental, benchmarks de CRO do setor (taxas de conversão por indústria e tipo de página), pesquisas de exit intent respondidas por usuários

## Action Items

1. Confirmar o gatilho e carregar a entrada (Acesso a Hotjar/Microsoft Clarity (gravacoes e heatmaps), export de dados do Google Analytics 4 (funil de conversao, co…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mapa de Fricções do Funil (por etapa, com evidência de comportamento e severidade), Behavioral Insights Report por expe…) e persistir no artefato do squad.
4. Entregar ao critic Rex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mapa de Fricções do Funil (por etapa, com evidência de comportamento e severidade), Behavioral Insights Report por experimento encerrado (o que o comportamento…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Rex 2 registrado
- [ ] Gate HITL respeitado: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção d…
- [ ] Gate HITL respeitado: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na pág…
- [ ] Gate HITL respeitado: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel lega…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3)… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de pro… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qu… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão es… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hi… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Rex 2 | BLOQUEIA entrega |

## Handoff

- **to:** Sage
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
