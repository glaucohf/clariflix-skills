---
task: sage()
responsavel: "Sage"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft de seção ou documento completo para alinhamento de voz"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Contexto do público-alvo (board existente que conhece a empresa vs novo investidor)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Guidance do ciclo anterior (o que foi prometido, como o board percebe a empresa)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Pergunta ad-hoc ('como explico este churn sem soar defensivo?')"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Seção reescrita com voz e lógica do founder"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Score de alinhamento narrativo (0–10) com justificativa para cada seção"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Lista de pontos onde o rascunho diverge do posicionamento histórico do founder"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Sugestão de 3 perguntas que o board provavelmente fará com base na narrativa apresentada e pré-respostas no estilo do founder"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Draft de seção disponível para revisão narrativa. Founder solicita reescrita específica. Critic sinaliza inconsistência de tom ou argumento fraco. Preparação de Q&A para board meeting."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Axiom antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção"
    - "[ ] HITL: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores"
    - "[ ] HITL: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%"
    - "[ ] HITL: Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)"
    - "[ ] HITL: Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final"
---

# Alinhar Narrativa

**Task ID:** `sage()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Alinhar Narrativa |
| **status** | `pending` |
| **responsible_executor** | Sage (Sage — Founder Clone & Narrative Aligner) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Aplica a lógica estratégica, os frameworks preferidos e o tom de comunicação do founder à narrativa do board pack. Reescreve seções que estejam técnicas demais, genéricas demais ou desalinhadas com o posicionamento que o founder quer transmitir. Responde a perguntas 'como o founder explicaria isso ao board?' para cada seção. Valida se a narrativa está coerente com a tese da rodada ou com o guidance dado no ciclo anterior.

## Input

- Draft de seção ou documento completo para alinhamento de voz
- Contexto do público-alvo (board existente que conhece a empresa vs novo investidor)
- Guidance do ciclo anterior (o que foi prometido, como o board percebe a empresa)
- Pergunta ad-hoc ('como explico este churn sem soar defensivo?')

## Output

- Seção reescrita com voz e lógica do founder
- Score de alinhamento narrativo (0–10) com justificativa para cada seção
- Lista de pontos onde o rascunho diverge do posicionamento histórico do founder
- Sugestão de 3 perguntas que o board provavelmente fará com base na narrativa apresentada e pré-respostas no estilo do founder

## Trigger

Draft de seção disponível para revisão narrativa. Founder solicita reescrita específica. Critic sinaliza inconsistência de tom ou argumento fraco. Preparação de Q&A para board meeting.

## Knowledge base (o que o executor consulta)

- Corpus de comunicações passadas do founder com investidores (emails, board updates anteriores, cartas de acionistas)
- Frameworks estratégicos documentados (como o founder explica unit economics, moat, TAM)
- Histórico de board packs anteriores (narrativa e positioning por ciclo)
- Transcrições de investor calls aprovadas
- Tese da rodada atual ou last round docs

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft de seção ou documento completo para alinhamento de voz).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Seção reescrita com voz e lógica do founder) e persistir no artefato do squad.
4. Entregar ao critic Axiom; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Seção reescrita com voz e lógica do founder
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Axiom registrado
- [ ] Gate HITL respeitado: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- [ ] Gate HITL respeitado: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao b…
- [ ] Gate HITL respeitado: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90% | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa nã… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downr… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser r… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Axiom | BLOQUEIA entrega |

## Handoff

- **to:** Quincy
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
