---
task: axiom()
responsavel: "Axiom"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Corpus normalizado do Citadel + Sizing Brief original com metodologia acordada + benchmarks de mercados análogos configurados + thresholds de convergência (default: max 40% desvio entre métodos para classificação High confidence)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Corpus auditado com anotações de confiança por número"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatório de verificação: { tam_convergence_pct, confidence_classification (High/Medium/Low/Reject), methods_used, contradictions_found, red_team_som_findings, gaps_requiring_research }"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "GO/NO-GO para síntese"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Se NO-GO: instrução específica para qual worker e qual dimensão reprocessar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente após Citadel concluir normalização. Re-ativado pelo Atlas após workers complementares entregarem dados adicionais solicitados. Pode ser ativado manualmente pelo founder via '/…"
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

# Verificar Convergência E Sanity Check

**Task ID:** `axiom()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Convergência E Sanity Check |
| **status** | `pending` |
| **responsible_executor** | Axiom (Axiom — O Verificador de Sizing) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente critic/verifier especializado em validação de sizing de mercado. Executa verificação adversarial em quatro camadas: (1) Convergência de métodos — verifica se TAM top-down, TAM bottom-up e TAM por proxy competitivo estão dentro de margem aceitável (< 40% de desvio entre métodos; desvio > 40% dispara investigação adicional); (2) Sanity check de ordem de grandeza — compara sizing gerado com benchmarks conhecidos de mercados análogos para detectar números implausíveis (ex: um TAM de software B2B no Brasil maior que o PIB do setor é flag imediata); (3) Rastreabilidade — verifica se cada número crítico (TAM, SAM, SOM, CAGR) tem pelo menos 2 fontes independentes de credibilidade >= 3; (4) Red-team de SOM — tenta construir o argumento de que o SOM é 50% menor do que calculado, listando os fatores que o founder está subestimando. Se convergência falha ou rastreabilidade insuficiente, devolve para workers específicos com instrução precisa antes de liberar para síntese.

## Input

- Corpus normalizado do Citadel + Sizing Brief original com metodologia acordada + benchmarks de mercados análogos configurados + thresholds de convergência (default: max 40% desvio entre métodos para classificação High confidence)

## Output

- Corpus auditado com anotações de confiança por número
- Relatório de verificação: { tam_convergence_pct, confidence_classification (High/Medium/Low/Reject), methods_used, contradictions_found, red_team_som_findings, gaps_requiring_research }
- GO/NO-GO para síntese
- Se NO-GO: instrução específica para qual worker e qual dimensão reprocessar

## Trigger

Ativado automaticamente após Citadel concluir normalização. Re-ativado pelo Atlas após workers complementares entregarem dados adicionais solicitados. Pode ser ativado manualmente pelo founder via '/verify-sizing [número]' para fact-check pontual de um dado específico antes de usar em pitch.

## Knowledge base (o que o executor consulta)

- Corpus normalizado da sessão
- Base de benchmarks de tamanho de mercado por vertical (mercados SaaS B2B, fintech, e-commerce, healthtech, edtech no Brasil e LATAM
- usados como sanity check)
- Heurísticas de sizing: regras de plausibilidade por setor (ex: penetração de SaaS B2B em PMEs no Brasil raramente excede 15% no curto prazo)
- Histórico de sizings anteriores aprovados pelo founder (para calibração de nível de exigência)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Corpus normalizado do Citadel + Sizing Brief original com metodologia acordada + benchmarks de mercados análogos config…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Corpus auditado com anotações de confiança por número) e persistir no artefato do squad.
4. Entregar ao critic Axiom 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Corpus auditado com anotações de confiança por número
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

- **to:** Axiom 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
