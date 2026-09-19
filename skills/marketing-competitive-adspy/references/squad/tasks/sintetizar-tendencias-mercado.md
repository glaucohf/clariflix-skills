---
task: volta()
responsavel: "Volta"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Competitor Creative Strategy Profiles atualizados de Cipher (últimos 90 dias por concorrente), Positioning Diff histórico de Prism (mudanças de oferta e posicionamento por concorrente), Ad Intelligence Cards agregados por período para análise de tendência, contexto de mercado externo relevante (notícias de setor, mudanças regulatórias, novos entrantes) de fontes abertas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Market Intelligence Report quinzenal (tendências de ângulo, formato e oferta detectadas com evidências de múltiplos concorrentes e hipótese estratégica), Category Trend Alert quando convergência de 3+ concorrentes é detectada em menos de 30 dias (entregue em 24h para CMO), Strategic Gap Analysis semestral (ângulos e formatos que nenhum concorrente está usando"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "white space de posicionamento), Competitive Narrative Map por trimestre (como o mercado como um todo está posicionando a categoria"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "útil para posicionamento diferenciado da empresa)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo quinzenal automático de síntese de tendências; Category Trend Alert quando Cipher ou Prism detecta convergência de 3+ concorrentes; lançamento de nova campanha própria sendo planejada (input de…"
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

# Sintetizar Tendencias Mercado

**Task ID:** `volta()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Competitive Intelligence & Ad-Spy

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Tendencias Mercado |
| **status** | `pending` |
| **responsible_executor** | Volta (Volta — Trend Synthesizer & Market Intelligence) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Eleva a inteligencia de individual para estrategico — sintetiza movimentos de multiplos concorrentes para identificar tendencias de categoria que nenhum monitoramento individual captura. Funciona em tres dimensoes: (1) Convergencia de angulos — quando tres ou mais concorrentes migram para o mesmo angulo narrativo em menos de 30 dias, sinaliza tendencia de mercado (nao coincidencia), o que pode indicar que uma pesquisa de consumidor ou dado de mercado novo esta guiando o setor; (2) Convergencia de formato — quando concorrentes de Tier 1 e 2 abandonam formato em favor de outro (ex: carrossel para video curto), sinaliza mudanca de plataforma ou comportamento de audiencia; (3) Convergencia de oferta — quando multiplos concorrentes mudam estrutura de preco ou garantia no mesmo periodo, sinaliza pressao de mercado (commoditizacao, novo entrante disruptivo, mudanca regulatoria). Referencia direta ao 'copy/ads/conteudo/analise' e 'Deepresearch / Researchs do Alan' do board.

## Input

- Competitor Creative Strategy Profiles atualizados de Cipher (últimos 90 dias por concorrente), Positioning Diff histórico de Prism (mudanças de oferta e posicionamento por concorrente), Ad Intelligence Cards agregados por período para análise de tendência, contexto de mercado externo relevante (notícias de setor, mudanças regulatórias, novos entrantes) de fontes abertas

## Output

- Market Intelligence Report quinzenal (tendências de ângulo, formato e oferta detectadas com evidências de múltiplos concorrentes e hipótese estratégica), Category Trend Alert quando convergência de 3+ concorrentes é detectada em menos de 30 dias (entregue em 24h para CMO), Strategic Gap Analysis semestral (ângulos e formatos que nenhum concorrente está usando
- white space de posicionamento), Competitive Narrative Map por trimestre (como o mercado como um todo está posicionando a categoria
- útil para posicionamento diferenciado da empresa)

## Trigger

Ciclo quinzenal automático de síntese de tendências; Category Trend Alert quando Cipher ou Prism detecta convergência de 3+ concorrentes; lançamento de nova campanha própria sendo planejada (input de contexto competitivo para briefing); evento de mercado relevante detectado (mudança regulatória, novo entrante, funding de concorrente) que pode acelerar mudanças de posicionamento; revisão trimestral de Strategic Gap Analysis

## Knowledge base (o que o executor consulta)

- Histórico agregado de movimentos competitivos dos últimos 12 meses (dados de Cipher e Prism consolidados), biblioteca de tendências setoriais anteriores com como se desenvolveram ao longo do tempo (para calibrar velocidade de adoção), fontes de inteligência de categoria: relatórios de setor, earnings calls de empresas listadas no segmento, estudos de comportamento de consumidor relevantes, contexto regulatório do setor monitorado

## Action Items

1. Confirmar o gatilho e carregar a entrada (Competitor Creative Strategy Profiles atualizados de Cipher (últimos 90 dias por concorrente), Positioning Diff históri…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Market Intelligence Report quinzenal (tendências de ângulo, formato e oferta detectadas com evidências de múltiplos con…) e persistir no artefato do squad.
4. Entregar ao critic Sigma 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Market Intelligence Report quinzenal (tendências de ângulo, formato e oferta detectadas com evidências de múltiplos concorrentes e hipótese estratégica), Categ…
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
