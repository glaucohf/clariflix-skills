---
task: praxis()
responsavel: "Praxis"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dimensão de sizing bottom-up do Atlas + definição de unidade econômica base (ex: PMEs com 10-50 funcionários no setor X no Brasil) + ticket médio ou range + frequência de compra estimada + taxa de penetração alvo + fontes de contagem de unidades (CNPJ, RAIS, censos setoriais)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sizing bottom-up estruturado: { base_unit_count, base_unit_source_url, avg_ticket, avg_ticket_source_url, purchase_frequency, penetration_assumption, penetration_rationale, sam_value, som_value, som_rationale, sensitivity_table: [{scenario, penetration_rate, som_value}], confidence_level, key_assumptions }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tabela de sensibilidade com 3 cenários (conservador/base/otimista)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Atlas roteia dimensão como 'bottom-up sizing' ou 'unit economics sizing'. Ativado em análises de Customer Segment Expansion e Adjacent Product onde o mercado não tem dados macro consolidados. Sempre…"
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

# Contar Unidades Econômicas

**Task ID:** `praxis()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Contar Unidades Econômicas |
| **status** | `pending` |
| **responsible_executor** | Praxis (Praxis — O Engenheiro Bottom-Up) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em sizing pela metodologia bottom-up: conta o número de unidades econômicas endereçáveis (clientes potenciais, empresas no segmento, domicílios, transações), multiplica pelo ticket médio ou frequência de compra e produz um SAM/SOM construído da base para cima. Esta metodologia é o contraponto de sanidade para o top-down: quando os dois convergem, a tese é sólida. Quando divergem, o gap é oportunidade de investigação adicional.

## Input

- Dimensão de sizing bottom-up do Atlas + definição de unidade econômica base (ex: PMEs com 10-50 funcionários no setor X no Brasil) + ticket médio ou range + frequência de compra estimada + taxa de penetração alvo + fontes de contagem de unidades (CNPJ, RAIS, censos setoriais)

## Output

- Sizing bottom-up estruturado: { base_unit_count, base_unit_source_url, avg_ticket, avg_ticket_source_url, purchase_frequency, penetration_assumption, penetration_rationale, sam_value, som_value, som_rationale, sensitivity_table: [{scenario, penetration_rate, som_value}], confidence_level, key_assumptions }
- Tabela de sensibilidade com 3 cenários (conservador/base/otimista)

## Trigger

Atlas roteia dimensão como 'bottom-up sizing' ou 'unit economics sizing'. Ativado em análises de Customer Segment Expansion e Adjacent Product onde o mercado não tem dados macro consolidados. Sempre ativado em paralelo com Cosmos para triangulação.

## Knowledge base (o que o executor consulta)

- Bases cadastrais públicas (CNPJ ativo por CNAE
- dados Receita Federal, RAIS/CAGED para contagem de empresas por setor)
- Pesquisas de consumo e hábitos de compra (POF/IBGE, pesquisas setoriais)
- Benchmarks de ticket médio e LTV por vertical (SaaS, marketplace, fintech, B2B services
- indexados no Vector DB)
- Dados de penetração de categoria em mercados análogos internacionais para benchmark

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dimensão de sizing bottom-up do Atlas + definição de unidade econômica base (ex: PMEs com 10-50 funcionários no setor X…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sizing bottom-up estruturado: { base_unit_count, base_unit_source_url, avg_ticket, avg_ticket_source_url, purchase_freq…) e persistir no artefato do squad.
4. Entregar ao critic Axiom 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sizing bottom-up estruturado: { base_unit_count, base_unit_source_url, avg_ticket, avg_ticket_source_url, purchase_frequency, penetration_assumption, penetrati…
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

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
