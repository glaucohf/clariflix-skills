---
task: radar()
responsavel: "Radar"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de players do mercado-alvo (top 5-10 concorrentes diretos e adjacentes) + tipo de empresa (pública, privada, startup) + tipo de dado desejado (revenue, ARR, GMV, usuários) + janela temporal de análise"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Competitive sizing estruturado: { player_name, revenue_estimate, revenue_source_url, revenue_year, market_share_estimate, market_share_rationale, implied_tam, growth_rate, growth_source_url }[]"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "TAM implícito calculado por método competitivo com intervalo de confiança"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Ranking de players por tamanho"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Análise de dinâmica de crescimento do mercado (expansão vs"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "share-shift)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Atlas sempre ativa Radar em paralelo com Cosmos e Praxis para triangulação. Ativado de forma isolada quando o objetivo é entender dinâmica competitiva de um mercado antes de entrada. Re-ativado por A…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Axiom 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado de tokens é apresentado ao founder para aprovação explícita. Perguntas que envolvam sizing de mercados para M&A, captação ou due diligence de parceiros têm este gate obrigatório e não podem ser puladas."
    - "[ ] HITL: REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, autorização CADE) — o Market Opportunity Report é retido e o founder recebe alerta com a barreira descrita. O SOM do relatório final é ajustado para refletir a barreira e marcado como 'pendente de validação jurídica' até que especialista humano confirme a análise. Inclui recomendação de consultor jurídico parceiro."
    - "[ ] HITL: CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolverem o gap — o relatório é enviado ao founder com flag explícita de 'sizing com alta incerteza metodológica'. O founder decide se aceita o intervalo de incerteza ou solicita pesquisa adicional paga (escopo ampliado)."
    - "[ ] HITL: INVESTMENT MEMO / PITCH USE (L3): Quando o founder sinaliza que vai usar o Market Opportunity Report em pitch a investidores, board pack ou material de captação — Axiom executa uma rodada adicional de verificação adversarial de nível máximo (100% de claims quantitativos devem ter fonte credibilidade >= 4) e o founder deve revisar e assinar o relatório antes do envio externo. Nexar (Founder Clone) não escreve versão de pitch sem este gate."
    - "[ ] HITL: COST THRESHOLD (L3): Se a estimativa de custo de tokens de uma pesquisa superar o limite configurado (default: U$8 por análise de sizing completo) — Atlas pausa, apresenta o breakdown de custo por worker e solicita aprovação explícita antes de continuar."
---

# Estimar Mercado Competitivo

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Estimar Mercado Competitivo |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — O Leitor de Concorrentes) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em sizing competitivo: usa as receitas, crescimento e participação de mercado dos players existentes como proxy independente do tamanho real do mercado. Se os top-5 players faturam R$500M combinados e têm estimada 40% de penetração do mercado, o TAM real é ~R$1.25B. Este método é o mais confiável quando disponível, pois usa números reais de empresas, não estimativas. Também mapeia velocidade de crescimento dos players como sinal de expansão do mercado.

## Input

- Lista de players do mercado-alvo (top 5-10 concorrentes diretos e adjacentes) + tipo de empresa (pública, privada, startup) + tipo de dado desejado (revenue, ARR, GMV, usuários) + janela temporal de análise

## Output

- Competitive sizing estruturado: { player_name, revenue_estimate, revenue_source_url, revenue_year, market_share_estimate, market_share_rationale, implied_tam, growth_rate, growth_source_url }[]
- TAM implícito calculado por método competitivo com intervalo de confiança
- Ranking de players por tamanho
- Análise de dinâmica de crescimento do mercado (expansão vs
- share-shift)

## Trigger

Atlas sempre ativa Radar em paralelo com Cosmos e Praxis para triangulação. Ativado de forma isolada quando o objetivo é entender dinâmica competitiva de um mercado antes de entrada. Re-ativado por Axiom quando sizing top-down e bottom-up divergem mais de 50% — Radar serve como árbitro.

## Knowledge base (o que o executor consulta)

- Filings públicos (CVM, SEC para empresas listadas)
- Relatórios de resultados públicos de concorrentes
- Crunchbase / PitchBook (ARR e valuations públicos de startups)
- SimilarWeb / SEMrush (proxy de receita por tráfego para SaaS/marketplace)
- LinkedIn Sales Navigator (proxy de tamanho por headcount e crescimento de contratações)
- Notícias e press releases de concorrentes indexados via RSS + web search

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de players do mercado-alvo (top 5-10 concorrentes diretos e adjacentes) + tipo de empresa (pública, privada, star…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Competitive sizing estruturado: { player_name, revenue_estimate, revenue_source_url, revenue_year, market_share_estimat…) e persistir no artefato do squad.
4. Entregar ao critic Axiom 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Competitive sizing estruturado: { player_name, revenue_estimate, revenue_source_url, revenue_year, market_share_estimate, market_share_rationale, implied_tam,…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Axiom 2 registrado
- [ ] Gate HITL respeitado: SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado…
- [ ] Gate HITL respeitado: REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, a…
- [ ] Gate HITL respeitado: CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolver…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado de tokens é apresent… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, autorização CADE) — o… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolverem o gap — o relatór… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — INVESTMENT MEMO / PITCH USE (L3): Quando o founder sinaliza que vai usar o Market Opportunity Report em pitch a investidores, board pack ou material de captaçã… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — COST THRESHOLD (L3): Se a estimativa de custo de tokens de uma pesquisa superar o limite configurado (default: U$8 por análise de sizing completo) — Atlas paus… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — NEW MARKET ENTRY RECOMMENDATION (L3): Quando Scout ranquear uma oportunidade com recomendação de ação imediata (ex: janela de entrada fechando em < 3 meses, si… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Axiom 2 | BLOQUEIA entrega |

## Handoff

- **to:** Scout
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
