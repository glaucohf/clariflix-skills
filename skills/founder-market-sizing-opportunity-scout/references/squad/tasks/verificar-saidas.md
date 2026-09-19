---
task: axiom2Verificar()
responsavel: "Axiom 2"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: SIZING BRIEF APPROVAL (L3): Antes de Atlas disparar qualquer worker, o Sizing Brief com metodologia proposta, fontes-alvo e custo estimado de tokens é apresentado ao founder para aprovação explícita. Perguntas que envolvam sizing de mercados para M&A, captação ou due diligence de parceiros têm este gate obrigatório e não podem ser puladas."
    - "[ ] HITL: REGULATORY BARRIER FLAG (L1→L3): Quando Faro classifica uma barreira regulatória como Alta (ex: exige licença BACEN, certificação ANVISA, autorização CADE) — o Market Opportunity Report é retido e o founder recebe alerta com a barreira descrita. O SOM do relatório final é ajustado para refletir a barreira e marcado como 'pendente de validação jurídica' até que especialista humano confirme a análise. Inclui recomendação de consultor jurídico parceiro."
    - "[ ] HITL: CONVERGENCE FAILURE ALERT (L2→L3): Se Axiom detectar divergência > 60% entre os três métodos de sizing e os workers adicionais não resolverem o gap — o relatório é enviado ao founder com flag explícita de 'sizing com alta incerteza metodológica'. O founder decide se aceita o intervalo de incerteza ou solicita pesquisa adicional paga (escopo ampliado)."
    - "[ ] HITL: INVESTMENT MEMO / PITCH USE (L3): Quando o founder sinaliza que vai usar o Market Opportunity Report em pitch a investidores, board pack ou material de captação — Axiom executa uma rodada adicional de verificação adversarial de nível máximo (100% de claims quantitativos devem ter fonte credibilidade >= 4) e o founder deve revisar e assinar o relatório antes do envio externo. Nexar (Founder Clone) não escreve versão de pitch sem este gate."
    - "[ ] HITL: COST THRESHOLD (L3): Se a estimativa de custo de tokens de uma pesquisa superar o limite configurado (default: U$8 por análise de sizing completo) — Atlas pausa, apresenta o breakdown de custo por worker e solicita aprovação explícita antes de continuar."
---

# Verificar Saídas do Market Sizing & Opportunity Scout

**Task ID:** `axiom2Verificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Market Sizing & Opportunity Scout — Founder Strategy Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Market Sizing & Opportunity Scout |
| **status** | `pending` |
| **responsible_executor** | Axiom 2 (Axiom — O Verificador de Sizing) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Axiom — O Verificador de Sizing — Axiom é o agente critic/verifier do squad, especializado na dimensão mais crítica de qualquer tese de mercado: a confiabilidade dos números. Opera em quatro camadas de verificação: (1) convergência metodológica — três métodos de sizing (top-down, bottom-up, proxy competitivo) devem convergir dentro de 40%; divergências maiores disparam investigação e nunca são 'resolvidas' pela média, mas pelo entendimento do porquê divergem; (2) sanity check de ordem de grandeza — números impossíveis (TAM > PIB do setor, penetração > 100% do público endereçável) são rejeitados com explicação; (3) rastreabilidade mínima — todo número de sizing publicado no relatório final deve ter >= 2 fontes independentes de credibilidade >= 3; (4) red-team de SOM — Axiom constrói ativamente o caso pessimista para o SOM antes de liberar a síntese, forçando o founder a tomar a decisão com olhos abertos. É o mecanismo que transforma o squad de um gerador de otimismo em uma ferramenta de decisão confiável.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- O Verificador de Sizing
- Axiom é o agente critic/verifier do squad, especializado na dimensão mais crítica de qualquer tese de mercado: a confiabilidade dos números
- Opera em quatro camadas de verificação: (1) convergência metodológica
- três métodos de sizing (top-down, bottom-up, proxy competitivo) devem convergir dentro de 40%
- divergências maiores disparam investigação e nunca são 'resolvidas' pela média, mas pelo entendimento do porquê divergem
- (2) sanity check de ordem de grandeza
- números impossíveis (TAM > PIB do setor, penetração > 100% do público endereçável) são rejeitados com explicação
- (3) rastreabilidade mínima
- todo número de sizing publicado no relatório final deve ter >= 2 fontes independentes de credibilidade >= 3
- (4) red-team de SOM
- Axiom constrói ativamente o caso pessimista para o SOM antes de liberar a síntese, forçando o founder a tomar a decisão com olhos abertos
- É o mecanismo que transforma o squad de um gerador de otimismo em uma ferramenta de decisão confiável

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Atlas para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
