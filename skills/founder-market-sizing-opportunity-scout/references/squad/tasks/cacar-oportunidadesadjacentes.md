---
task: scout()
responsavel: "Scout"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Mercado atual do founder (produto, cliente atual, geografia atual, receita atual se disponível) + horizonte de expansão (6m, 12m, 24m) + critérios de filtro (ex: só expansões que não exijam mudança de produto core, só mercados com > R$50M de SAM) + tipo de expansão priorizada pelo founder"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mapa de Oportunidades estruturado: { opportunity_name, opportunity_type (Geographic/Vertical/Adjacent/Segment), estimated_sam, sam_confidence, estimated_entry_effort (1-5), estimated_time_to_revenue_months, strategic_fit_score (1-5), signals: [{signal_type, signal_description, source_url}], analogous_market_example, recommendation_rank }[]"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Top 3 oportunidades rankeadas por potencial x esforço x timing com narrativa de entrada"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Atlas quando tipo de análise é 'Opportunity Scouting', 'Expansion Strategy' ou 'Adjacent Market'. Sempre ativado na fase Framework para enriquecer o Market Opportunity Report com próximo…"
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

# Caçar OportunidadesAdjacentes

**Task ID:** `scout()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Caçar OportunidadesAdjacentes |
| **status** | `pending` |
| **responsible_executor** | Scout (Scout — O Caçador de Oportunidades) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em identificar e rankear oportunidades de expansão adjacentes ao mercado atual do founder: novos segmentos de cliente, novas geografias, produtos adjacentes e white spaces de demanda reprimida. Não apenas dimensiona — ele sugere a próxima jogada. Usa sinais de busca (keyword trends), sinais de funding (onde o capital está indo), sinais de hiring (o que concorrentes estão contratando) e padrões de mercados análogos internacionais que já passaram pelo estágio onde o cliente está hoje.

## Input

- Mercado atual do founder (produto, cliente atual, geografia atual, receita atual se disponível) + horizonte de expansão (6m, 12m, 24m) + critérios de filtro (ex: só expansões que não exijam mudança de produto core, só mercados com > R$50M de SAM) + tipo de expansão priorizada pelo founder

## Output

- Mapa de Oportunidades estruturado: { opportunity_name, opportunity_type (Geographic/Vertical/Adjacent/Segment), estimated_sam, sam_confidence, estimated_entry_effort (1-5), estimated_time_to_revenue_months, strategic_fit_score (1-5), signals: [{signal_type, signal_description, source_url}], analogous_market_example, recommendation_rank }[]
- Top 3 oportunidades rankeadas por potencial x esforço x timing com narrativa de entrada

## Trigger

Ativado pelo Atlas quando tipo de análise é 'Opportunity Scouting', 'Expansion Strategy' ou 'Adjacent Market'. Sempre ativado na fase Framework para enriquecer o Market Opportunity Report com próximos passos concretos. Pode ser ativado diretamente pelo founder via '/scout [mercado]' para análise rápida de uma oportunidade específica.

## Knowledge base (o que o executor consulta)

- Google Trends API (sinais de demanda crescente por keyword)
- Dados de funding setorial (CB Insights, Crunchbase
- onde o capital está apostando)
- Casos de expansão de empresas análogas internacionais (corpus indexado no Vector DB)
- Benchmarks de custo de entrada em novos mercados por tipo de expansão
- LinkedIn Sales Navigator para sinais de hiring de concorrentes em novos mercados
- Histórico de oportunidades mapeadas para o cliente (para evitar re-trabalho)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Mercado atual do founder (produto, cliente atual, geografia atual, receita atual se disponível) + horizonte de expansão…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mapa de Oportunidades estruturado: { opportunity_name, opportunity_type (Geographic/Vertical/Adjacent/Segment), estimat…) e persistir no artefato do squad.
4. Entregar ao critic Axiom 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mapa de Oportunidades estruturado: { opportunity_name, opportunity_type (Geographic/Vertical/Adjacent/Segment), estimated_sam, sam_confidence, estimated_entry_…
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

- **to:** Faro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
