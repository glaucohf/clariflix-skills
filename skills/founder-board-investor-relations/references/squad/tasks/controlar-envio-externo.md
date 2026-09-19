---
task: gate()
responsavel: "Gate"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefato pronto para envio (board pack, investor email, IC memo)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Score de rastreabilidade do Vera"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Sinalização do Critic (aprovado/pendências)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Lista de destinatários e canal de envio"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Contexto do envio (tipo, urgência, consequência de erro)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Tela de confirmação para o founder: resumo de 1 página do que está sendo enviado, para quem, e os 3 principais riscos identificados"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Após aprovação: execução do envio com log de confirmação (timestamp, destinatários, versão do artefato)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Após recusa: flag de pendência no ClickUp com motivo registrado"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Qualquer ação de envio externo solicitada por qualquer agente do squad. Acionado automaticamente ao final do pipeline quando Cassidy sinaliza 'pronto para envio'. Nunca pode ser bypassado — é o últim…"
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

# Controlar Envio Externo

**Task ID:** `gate()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Controlar Envio Externo |
| **status** | `pending` |
| **responsible_executor** | Gate (Gate — HITL Compliance & Send Controller) |
| **execution_type** | `Hybrid` |
| **input** | 5 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Intercepta 100% das ações de envio externo antes de executar. Nenhum email, PDF, Notion share ou mensagem sai do sistema sem passar por este agente. Apresenta ao founder um resumo de revisão final: destinatários, artefato, score de rastreabilidade do Vera, sinalização do Critic, e exige aprovação explícita antes de qualquer envio. Em caso de envio de informação financeira ou comprometimento de guidance de valuation/rodada, escala para L3 com checklist de confirmação dupla.

## Input

- Artefato pronto para envio (board pack, investor email, IC memo)
- Score de rastreabilidade do Vera
- Sinalização do Critic (aprovado/pendências)
- Lista de destinatários e canal de envio
- Contexto do envio (tipo, urgência, consequência de erro)

## Output

- Tela de confirmação para o founder: resumo de 1 página do que está sendo enviado, para quem, e os 3 principais riscos identificados
- Após aprovação: execução do envio com log de confirmação (timestamp, destinatários, versão do artefato)
- Após recusa: flag de pendência no ClickUp com motivo registrado

## Trigger

Qualquer ação de envio externo solicitada por qualquer agente do squad. Acionado automaticamente ao final do pipeline quando Cassidy sinaliza 'pronto para envio'. Nunca pode ser bypassado — é o último gate antes de qualquer saída.

## Knowledge base (o que o executor consulta)

- Lista de destinatários aprovados por categoria (board, investidores, potenciais, advisors)
- Histórico de envios anteriores (para evitar duplicatas ou envio de versão errada)
- Política de NDA e confidencialidade por destinatário
- Regras de compliance do squad configuradas pelo founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Artefato pronto para envio (board pack, investor email, IC memo)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Tela de confirmação para o founder: resumo de 1 página do que está sendo enviado, para quem, e os 3 principais riscos i…) e persistir no artefato do squad.
4. Entregar ao critic Axiom; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Tela de confirmação para o founder: resumo de 1 página do que está sendo enviado, para quem, e os 3 principais riscos identificados
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

- **to:** Axiom
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
