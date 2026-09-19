---
task: pixel()
responsavel: "Pixel"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Hipótese de layout a testar (ex: 'mover CTA para above-the-fold no mobile aumenta conversão'), evidência comportamental do Hera que motiva a hipótese (heatmap, scroll depth), copy produzida pelo Muse para esta variação, screenshot ou código da página atual (controle), constraints técnicos da stack da landing page (Unbounce, Webflow, custom HTML, etc.)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Layout Spec Document por variação: wireframe textual estruturado (seção por seção com instruções de posicionamento), especificações de hierarquia visual (o que é H1/H2/H3, o que é destaque visual), instruções específicas de mobile vs desktop (thumb-zone, CTA tamanho, espaçamento), lista de elementos a remover/adicionar/reposicionar vs controle, estimativa de esforço de implementação (horas) para o time de desenvolvimento"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro aprova hipotese de layout para producao; Hera detecta problema de layout especifico no mapa de friccoes (ex: CTA fora do fold no mobile para 60% dos usuarios); nova landing page sendo constru…"
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

# Traduzir Hipoteses De Layout

**Task ID:** `pixel()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Traduzir Hipoteses De Layout |
| **status** | `pending` |
| **responsible_executor** | Pixel (Pixel — Layout & UX Specs Agent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em especificações de layout e UX para conversão. Não é dev nem designer executivo — produz specs técnicas e wireframes de baixa fidelidade (em texto estruturado ou ferramentas como Whimsical/Figma com MCP) que o time implementa. Traduz as hipóteses de layout (posicionamento de CTA, hierarquia visual, redução de campos de formulário, social proof placement, uso de urgência visual) em especificações implementáveis. Referencia os princípios de design de conversão (heatmap evidence, F-pattern reading, thumb-zone mobile, above-the-fold priority). Alias: 'Pixel' — cada pixel tem uma função de conversão.

## Input

- Hipótese de layout a testar (ex: 'mover CTA para above-the-fold no mobile aumenta conversão'), evidência comportamental do Hera que motiva a hipótese (heatmap, scroll depth), copy produzida pelo Muse para esta variação, screenshot ou código da página atual (controle), constraints técnicos da stack da landing page (Unbounce, Webflow, custom HTML, etc.)

## Output

- Layout Spec Document por variação: wireframe textual estruturado (seção por seção com instruções de posicionamento), especificações de hierarquia visual (o que é H1/H2/H3, o que é destaque visual), instruções específicas de mobile vs desktop (thumb-zone, CTA tamanho, espaçamento), lista de elementos a remover/adicionar/reposicionar vs controle, estimativa de esforço de implementação (horas) para o time de desenvolvimento

## Trigger

Maestro aprova hipotese de layout para producao; Hera detecta problema de layout especifico no mapa de friccoes (ex: CTA fora do fold no mobile para 60% dos usuarios); nova landing page sendo construida do zero; resultado de teste de copy inconclusivo sugere que layout pode ser confundindo o teste

## Knowledge base (o que o executor consulta)

- Princípios de CRO visual (heatmap patterns, F-pattern, thumb-zone mobile), biblioteca de layouts de landing pages de alta conversão por vertical, resultados de experimentos de layout anteriores com lift documentado, constraints técnicos de cada ferramenta de landing page usada pelo cliente (Unbounce drag-and-drop limits, Webflow CMS, etc.), diretrizes de acessibilidade WCAG básicas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Hipótese de layout a testar (ex: 'mover CTA para above-the-fold no mobile aumenta conversão'), evidência comportamental…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Layout Spec Document por variação: wireframe textual estruturado (seção por seção com instruções de posicionamento), es…) e persistir no artefato do squad.
4. Entregar ao critic Rex 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Layout Spec Document por variação: wireframe textual estruturado (seção por seção com instruções de posicionamento), especificações de hierarquia visual (o que…
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

- **to:** Darwin
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
