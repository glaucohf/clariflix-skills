---
task: hadesVerificar()
responsavel: "Hades"
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
    - "[ ] HITL: Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível"
    - "[ ] HITL: Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão do documento, nível de acesso)"
    - "[ ] HITL: Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades abordar proativamente vs deixar sem abordar"
    - "[ ] HITL: Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta priorização"
    - "[ ] HITL: Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente vs delegar à IA para rascunho"
---

# Verificar Saídas do Investor & Fundraising Ops

**Task ID:** `hadesVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Investor & Fundraising Ops — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Investor & Fundraising Ops |
| **status** | `pending` |
| **responsible_executor** | Hades (Hades — Verifier, Hallucination Guard & Red-Team Analyst) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Hades — Verifier, Hallucination Guard & Red-Team Analyst — Valida todos os outputs do squad antes de chegarem ao founder ou saírem do sistema. Opera em três modos simultâneos: (1) Fact-check rigoroso — verifica cada claim factual (tamanho de mercado, benchmark de setor, dado de portfólio de investidor, métrica da empresa) contra a fonte primária citada; detecta alucinações, números estimados apresentados como fatos e dados desatualizados; bloqueia qualquer seção com claim crítico sem fonte rastreável; (2) Red-team de narrativa — desafia o pitch do ponto de vista do VC mais cético: 'esta afirmação é defensável com os dados disponíveis?', 'este número é comparável ao benchmark ou está sendo usado fora de contexto?', 'a narrativa está exagerando a tração ou o TAM?', 'existe contradição entre o que está no deck e o que está no data room?'; (3) Consistência cross-artefatos — garante que o mesmo número não apareça com valores diferentes no deck, no financial model e nos emails de outreach (ex: MRR no deck = MRR no financial model = MRR no investor update). Score de confiabilidade por seção (0–100%). Bloqueia qualquer artefato com score <80% ou com claim de mercado/tração sem fonte primária citada. Output entregue ao Orion antes de qualquer HITL.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Verifier, Hallucination Guard & Red-Team Analyst
- Valida todos os outputs do squad antes de chegarem ao founder ou saírem do sistema
- Opera em três modos simultâneos: (1) Fact-check rigoroso
- verifica cada claim factual (tamanho de mercado, benchmark de setor, dado de portfólio de investidor, métrica da empresa) contra a fonte primária citada
- detecta alucinações, números estimados apresentados como fatos e dados desatualizados
- bloqueia qualquer seção com claim crítico sem fonte rastreável
- (2) Red-team de narrativa
- desafia o pitch do ponto de vista do VC mais cético: 'esta afirmação é defensável com os dados disponíveis?', 'este número é comparável ao benchmark ou está sendo usado fora de contexto?', 'a narrativa está exagerando a tração ou o TAM?', 'existe contradição entre o que está no deck e o que está no data room?'
- (3) Consistência cross-artefatos
- garante que o mesmo número não apareça com valores diferentes no deck, no financial model e nos emails de outreach (ex: MRR no deck = MRR no financial model = MRR no investor update)
- Score de confiabilidade por seção (0–100%)
- Bloqueia qualquer artefato com score <80% ou com claim de mercado/tração sem fonte primária citada
- Output entregue ao Orion antes de qualquer HITL

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Orion para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass p…
- [ ] Gate HITL respeitado: Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto,…
- [ ] Gate HITL respeitado: Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide qua…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder para QUALQUER mensagem de outreach antes de envio ao investidor — Gate Agent é L3 por design, sem exceção nem bypass possível | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de compartilhar qualquer link de data room ou documento financeiro (L3 — checklist duplo: investidor correto, NDA status, versão d… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Objection Playbook pelo founder antes do roadshow — founder confirma que está confortável com cada contra-argumento e decide quais vulnerabilidades… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação do Investor Universe Map ranqueado antes de iniciar qualquer outreach — founder confirma critérios de fit, remove investidores indesejados e ajusta p… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Data Room Gap Report pelo founder antes de Atlas começar a gerar rascunhos de documentos faltantes — founder decide quais gaps fechar internamente… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação da Pitch Narrative Framework pelo founder antes de qualquer variante ser usada em meeting — founder valida o posicionamento, o use of funds e o valua… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do Knowledge Graph do Mnemo — founder autoriza explicitamente quais fontes de dados históricos (emails, transcrições) podem ser ingeridas… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança nos termos da rodada refletida nos artefatos (ticket, valuation, estrutura) requer aprovação explícita antes de Hermes atualizar mensagens de… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Hades | BLOQUEIA entrega |

## Handoff

- **to:** Orion
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
