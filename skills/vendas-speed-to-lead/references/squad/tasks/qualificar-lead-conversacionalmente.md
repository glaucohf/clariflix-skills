---
task: socrates()
responsavel: "Sócrates"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossie do Sherlock + transcricao da conversa ate o momento + criterios BANT/MEDDIC calibrados do cliente"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Acionado pelo Orchestrator apos enriquecimento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de qualificacao preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada, Timeline definida) + classificacao SQL/MQL/DQ + resumo de objecoes + proximo passo recomendado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registrado no CRM como nota de qualificacao"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Qualificacao Concluida' com scorecard BANT"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Dossie de enriquecimento recebido + lead respondeu ao primeiro contato. Tambem acionado por re-engajamento de lead frio (trigger do Worker de Follow-up)."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead"
    - "[ ] HITL: Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto"
    - "[ ] HITL: Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio"
    - "[ ] HITL: Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel"
    - "[ ] HITL: Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano"
---

# Qualificar Lead Conversacionalmente

**Task ID:** `socrates()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Qualificar Lead Conversacionalmente |
| **status** | `pending` |
| **responsible_executor** | Sócrates (Sócrates — Worker de Qualificacao Conversacional) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Conduz a qualificacao BANT/MEDDIC via conversa natural no canal preferido do lead (WhatsApp, chat ou email). Faz perguntas abertas, detecta sinais de compra e objecoes, classifica o lead como SQL (Sales Qualified Lead), MQL (Marketing Qualified Lead) ou DQ (desqualificado), e passa handoff estruturado para o Closer humano ou para o Worker de Agendamento.

## Input

- Dossie do Sherlock + transcricao da conversa ate o momento + criterios BANT/MEDDIC calibrados do cliente
- Acionado pelo Orchestrator apos enriquecimento

## Output

- Ficha de qualificacao preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada, Timeline definida) + classificacao SQL/MQL/DQ + resumo de objecoes + proximo passo recomendado
- Registrado no CRM como nota de qualificacao
- Artefato ClickUp: task 'Qualificacao Concluida' com scorecard BANT

## Trigger

Dossie de enriquecimento recebido + lead respondeu ao primeiro contato. Tambem acionado por re-engajamento de lead frio (trigger do Worker de Follow-up).

## Knowledge base (o que o executor consulta)

- Criterios BANT/MEDDIC do cliente
- perguntas de qualificacao calibradas por produto/segmento
- respostas a objecoes frequentes (mapa de objecoes x respostas vencedoras)
- exemplos de conversas de qualificacao bem-sucedidas extraidas de calls gravadas
- limiares de score para SQL vs

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossie do Sherlock + transcricao da conversa ate o momento + criterios BANT/MEDDIC calibrados do cliente).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ficha de qualificacao preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada, Timeline definid…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ficha de qualificacao preenchida (Budget confirmado/estimado, Authority confirmada, Need identificada, Timeline definida) + classificacao SQL/MQL/DQ + resumo d…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead
- [ ] Gate HITL respeitado: Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto
- [ ] Gate HITL respeitado: Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao de ligacao por voz (Vox) fora do horario comercial (18h-9h) — irreversivel, contato direto com lead | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao de ligacao por voz para contas com ticket acima do threshold definido pelo cliente (ex: >R$50k) — risco comercial alto | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Mensagem bloqueada pelo Sentinel na 3a iteracao de correcao — exige revisao humana antes de envio | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead classificado como conta estrategica (lista VIP do CRM) — qualquer acao requer aprovacao do closer responsavel | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Desconto ou concessao comercial mencionada na conversa — Eco/Socrates escalam imediatamente para closer humano | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Reagendamento apos segundo no-show — Atlas escala para closer decidir se continua ou descarta lead | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Lead demonstra sinal negativo forte (reclamacao de contato excessivo, solicitacao de opt-out) — intervencao humana obrigatoria e imediata | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
