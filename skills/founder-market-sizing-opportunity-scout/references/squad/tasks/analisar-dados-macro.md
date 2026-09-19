---
task: cosmos()
responsavel: "Cosmos"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dimensão de sizing top-down extraída pelo Atlas + mercado-alvo + geografia + moeda de referência + ano-base e projeção (ex: 2024 + CAGR 3 anos) + critérios de suficiência (mínimo 3 fontes independentes por estimativa de TAM)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sizing top-down estruturado: { market_name, tam_value, tam_currency, tam_year, sam_value, sam_rationale, calculation_steps: [{step, value, source_url, source_credibility}], cagr_estimate, cagr_source, confidence_level (High/Medium/Low), data_gaps }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Mínimo 5 fontes por sizing"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Atlas roteia dimensão classificada como 'top-down sizing' ou 'market size macro'. Ativado em toda análise de Market Entry e Geographic Expansion. Re-ativado se Axiom detectar divergência > 60% entre…"
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

# Analisar Dados Macro

**Task ID:** `cosmos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Dados Macro |
| **status** | `pending` |
| **responsible_executor** | Cosmos (Cosmos — O Analista Top-Down) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em sizing de mercado pela metodologia top-down: parte de dados macro (PIB setorial, população endereçável, gastos per capita, penetração da categoria) e afunila até o segmento específico usando taxas de penetração validadas. Usa relatórios de consultorias, bases de dados governamentais, filings públicos de empresas listadas e dados de institutos setoriais como fontes primárias. Retorna TAM e SAM com cálculo passo-a-passo e fonte por etapa — nenhum número sem citação.

## Input

- Dimensão de sizing top-down extraída pelo Atlas + mercado-alvo + geografia + moeda de referência + ano-base e projeção (ex: 2024 + CAGR 3 anos) + critérios de suficiência (mínimo 3 fontes independentes por estimativa de TAM)

## Output

- Sizing top-down estruturado: { market_name, tam_value, tam_currency, tam_year, sam_value, sam_rationale, calculation_steps: [{step, value, source_url, source_credibility}], cagr_estimate, cagr_source, confidence_level (High/Medium/Low), data_gaps }
- Mínimo 5 fontes por sizing

## Trigger

Atlas roteia dimensão classificada como 'top-down sizing' ou 'market size macro'. Ativado em toda análise de Market Entry e Geographic Expansion. Re-ativado se Axiom detectar divergência > 60% entre métodos e solicitar dados adicionais.

## Knowledge base (o que o executor consulta)

- Relatórios setoriais ingeridos (IBGE, FGV, BNDES setorial, Gartner, McKinsey Global Institute, CB Insights, Statista, relatórios ABECS/ABComm/ABFintechs por setor)
- Filings anuais de empresas listadas no setor (proxy de revenue total)
- Dados de PIB setorial por país/região (Banco Mundial, OCDE)
- Vector DB com histórico de sizings anteriores do cliente
- Acesso a web search via MCP (Brave Search / EXA API)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dimensão de sizing top-down extraída pelo Atlas + mercado-alvo + geografia + moeda de referência + ano-base e projeção…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sizing top-down estruturado: { market_name, tam_value, tam_currency, tam_year, sam_value, sam_rationale, calculation_st…) e persistir no artefato do squad.
4. Entregar ao critic Axiom 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sizing top-down estruturado: { market_name, tam_value, tam_currency, tam_year, sam_value, sam_rationale, calculation_steps: [{step, value, source_url, source_c…
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

- **to:** Praxis
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
