---
task: faro()
responsavel: "Faro"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Mercado-alvo + tipo de expansão identificado por Scout + perfil do cliente (estágio, capital disponível, equipe) + tipo de barreira a investigar (regulatória, competitiva, financeira, tecnológica, cultural)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Barrier Map estruturado: { barrier_type, severity (Alto/Médio/Baixo), description, mitigation_path, time_to_overcome_months, cost_estimate, source_url, recommendation }[]"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "SOM adjustment factor: multiplicador aplicado ao SAM para chegar ao SOM realista no horizonte de 12-24 meses, com justificativa"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Flag de HITL quando barreira regulatória é classificada como Alta"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "requer validação jurídica antes de usar o SOM em pitch a investidores"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Atlas em toda análise que envolva nova geografia, novo produto regulado ou nova vertical com players estabelecidos. Sempre ativado antes da síntese final para calibrar o SOM. Ativação ma…"
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

# Mapear Barreiras Regulatórias

**Task ID:** `faro()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Mapear Barreiras Regulatórias |
| **status** | `pending` |
| **responsible_executor** | Faro (Faro — O Guardião de Barreiras) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em mapear barreiras de entrada, requisitos regulatórios e fatores que limitam o SOM atingível no horizonte de análise. O SOM é a parte mais crítica e mais frequentemente inflada de qualquer sizing — Faro existe para garantir que o número final seja defensável. Mapeia: barreiras regulatórias (licenças, certificações, compliance), barreiras de distribuição (controle de canais por players estabelecidos), barreiras de capital (custo de entrada e payback), barreiras de switching (lock-in do cliente com incumbentes) e barreiras de timing (janela de oportunidade aberta ou fechando).

## Input

- Mercado-alvo + tipo de expansão identificado por Scout + perfil do cliente (estágio, capital disponível, equipe) + tipo de barreira a investigar (regulatória, competitiva, financeira, tecnológica, cultural)

## Output

- Barrier Map estruturado: { barrier_type, severity (Alto/Médio/Baixo), description, mitigation_path, time_to_overcome_months, cost_estimate, source_url, recommendation }[]
- SOM adjustment factor: multiplicador aplicado ao SAM para chegar ao SOM realista no horizonte de 12-24 meses, com justificativa
- Flag de HITL quando barreira regulatória é classificada como Alta
- requer validação jurídica antes de usar o SOM em pitch a investidores

## Trigger

Ativado pelo Atlas em toda análise que envolva nova geografia, novo produto regulado ou nova vertical com players estabelecidos. Sempre ativado antes da síntese final para calibrar o SOM. Ativação manual pelo founder via '/barriers [mercado]' para quick check antes de reunião estratégica.

## Knowledge base (o que o executor consulta)

- Base de dados regulatórios por setor e geography (Banco Central, ANVISA, BACEN, CADE, CVM, regulações estaduais
- indexados no Vector DB)
- Análises de barreiras de entrada de mercados análogos
- Dados de Capex médio de entrada por vertical (benchmarks de M&A e greenfield)
- Rede de especialistas jurídicos parceiros para escalada HITL em casos de risco Alto

## Action Items

1. Confirmar o gatilho e carregar a entrada (Mercado-alvo + tipo de expansão identificado por Scout + perfil do cliente (estágio, capital disponível, equipe) + tipo…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Barrier Map estruturado: { barrier_type, severity (Alto/Médio/Baixo), description, mitigation_path, time_to_overcome_mo…) e persistir no artefato do squad.
4. Entregar ao critic Axiom 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Barrier Map estruturado: { barrier_type, severity (Alto/Médio/Baixo), description, mitigation_path, time_to_overcome_months, cost_estimate, source_url, recomme…
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

- **to:** Citadel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
