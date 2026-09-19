---
task: prism()
responsavel: "Prism"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Competitive Map com URLs de landing pages, páginas de preço e páginas de produto de cada concorrente, snapshot da semana anterior de cada página (para gerar diff), lista de review sites relevantes por concorrente com identificadores de perfil, critérios de alerta de mudança crítica configurados por Orion (ex: mudança de preço = alerta imediato"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "mudança de headline = alerta diário)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Positioning Diff semanal por concorrente (o que mudou literalmente"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "texto anterior vs"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "atual com highlight), Pricing Change Alert em menos de 24h quando qualquer mudanca de preco e detectada em Tier 1, Offer Evolution Timeline por concorrente (como a estrutura de oferta evoluiu nos ultimos 6 meses), Review Pattern Report mensal (principais criticas recorrentes por concorrente"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "'pontos fracos exploraveis'), Content Authority Map por concorrente (em quais topicos esta investindo autoridade organica"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "indica estrategia de ads futura), Landing Page Competitive Benchmark comparando a propria empresa versus os tres principais concorrentes em estrutura e clareza de proposta de valor"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job de varredura semanal de todas as páginas monitoradas com geração de diff; alerta imediato quando mudança de preço é detectada (varredura diária de páginas de preço de Tier 1); Orion solicita snap…"
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

# Monitorar Mudanças Concorrenciais

**Task ID:** `prism()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Mudanças Concorrenciais |
| **status** | `pending` |
| **responsible_executor** | Prism (Prism — Positioning & Pricing Intelligence) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em rastrear mudancas de posicionamento, oferta e preco dos concorrentes fora do ambiente de ads — nas propriedades proprias deles. Monitora: (1) Landing pages de vendas com diff semanal automatico — detecta mudancas de headline, sub-headline, bullets de beneficios, garantias, CTAs e estrutura de oferta; (2) Paginas de preco com alerta de qualquer mudanca de valor, estrutura de tier ou politica de desconto; (3) Paginas de produto ou servico com mudanca de escopo ou posicionamento de proposta de valor; (4) Reviews publicas em G2, Capterra e Reclame Aqui — detecta padroes de critica que o concorrente pode estar adressando com mudancas de oferta ou comunicacao; (5) Conteudo organico estrategico em blog e LinkedIn que sinaliza onde o concorrente esta tentando construir autoridade (precede a estrategia de ads em 4-6 semanas). Produto central: 'Positioning Diff' semanal — o que mudou em cada concorrente versus a semana anterior.

## Input

- Competitive Map com URLs de landing pages, páginas de preço e páginas de produto de cada concorrente, snapshot da semana anterior de cada página (para gerar diff), lista de review sites relevantes por concorrente com identificadores de perfil, critérios de alerta de mudança crítica configurados por Orion (ex: mudança de preço = alerta imediato
- mudança de headline = alerta diário)

## Output

- Positioning Diff semanal por concorrente (o que mudou literalmente
- texto anterior vs
- atual com highlight), Pricing Change Alert em menos de 24h quando qualquer mudanca de preco e detectada em Tier 1, Offer Evolution Timeline por concorrente (como a estrutura de oferta evoluiu nos ultimos 6 meses), Review Pattern Report mensal (principais criticas recorrentes por concorrente
- 'pontos fracos exploraveis'), Content Authority Map por concorrente (em quais topicos esta investindo autoridade organica
- indica estrategia de ads futura), Landing Page Competitive Benchmark comparando a propria empresa versus os tres principais concorrentes em estrutura e clareza de proposta de valor

## Trigger

Job de varredura semanal de todas as páginas monitoradas com geração de diff; alerta imediato quando mudança de preço é detectada (varredura diária de páginas de preço de Tier 1); Orion solicita snapshot imediato de concorrente antes de lançamento de campanha própria; ciclo mensal de Review Pattern Report; novo concorrente adicionado ao Competitive Map (setup inicial de monitoramento de páginas)

## Knowledge base (o que o executor consulta)

- Snapshots históricos de todas as páginas monitoradas (últimos 6 meses) para timeline de evolução, critérios de alerta de mudança crítica configurados por categoria de mudança, mapeamento de proposta de valor própria da empresa para contextualizar gaps competitivos detectados, histórico de reviews por concorrente com categorização de temas (price, support, features, delivery), calendário de lançamentos e sazonalidade do setor para distinguir mudanças estratégicas de ajustes táticos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Competitive Map com URLs de landing pages, páginas de preço e páginas de produto de cada concorrente, snapshot da seman…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Positioning Diff semanal por concorrente (o que mudou literalmente) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Positioning Diff semanal por concorrente (o que mudou literalmente
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

- **to:** Echo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
