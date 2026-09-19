---
task: vigia()
responsavel: "Vigia"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Rascunho de mensagem do Volta com metadados: {canal, lead_id, ângulo, template_usado, dados_de_personalização_aplicados}"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "dossiê do lead do Sherlock"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "política de compliance da empresa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredicto: APROVADO | REPROVADO com score por dimensão (0-10) e instrução de correção se reprovado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Mensagem aprovada liberada para envio pelo Volta"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Log de verificação no ClickUp: 'Vigia-Review-{mensagem_id}' com score detalhado e justificativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda mensagem gerada pelo Volta antes do envio (gate obrigatorio); re-review apos correcao do Volta (max 2 iteracoes antes de escalar para HITL)"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vigia 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou edita antes do envio pelo Volta"
    - "[ ] L3: Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio"
    - "[ ] L3: Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar"
    - "[ ] L3: Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordagem antes de qualquer novo toque"
    - "[ ] HITL: Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão manual"
---

# Verificar Mensagem

**Task ID:** `vigia()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Mensagem |
| **status** | `pending` |
| **responsible_executor** | Vigia (Vigia — Crític / Verifier de Mensagens) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Red-team e verificador de qualidade antes de qualquer envio externo. Analisa cada mensagem gerada pelo Volta em 5 dimensões: (1) Personalização — a mensagem usa dados reais do lead ou é genérica? (2) Tom — está alinhado com a voz da marca e o momento da cadência? (3) Compliance — respeita LGPD, opt-out, CAN-SPAM, sem promessas não autorizadas? (4) Factualidade — os fatos sobre a empresa do lead estão corretos (cross-check com dossiê do Sherlock)? (5) Eficácia — o CTA está claro e é um único pedido? Reprova mensagens que falhem em qualquer dimensão crítica e devolve com instrução de correção específica.

## Input

- Rascunho de mensagem do Volta com metadados: {canal, lead_id, ângulo, template_usado, dados_de_personalização_aplicados}
- dossiê do lead do Sherlock
- política de compliance da empresa

## Output

- Veredicto: APROVADO | REPROVADO com score por dimensão (0-10) e instrução de correção se reprovado
- Mensagem aprovada liberada para envio pelo Volta
- Log de verificação no ClickUp: 'Vigia-Review-{mensagem_id}' com score detalhado e justificativa

## Trigger

Toda mensagem gerada pelo Volta antes do envio (gate obrigatorio); re-review apos correcao do Volta (max 2 iteracoes antes de escalar para HITL)

## Knowledge base (o que o executor consulta)

- Política de tom e voz da marca
- checklist de compliance LGPD/CAN-SPAM/WhatsApp Business Policy
- biblioteca de promessas não autorizadas
- critérios de personalização mínima por canal
- histórico de mensagens reprovadas para aprendizado

## Action Items

1. Confirmar o gatilho e carregar a entrada (Rascunho de mensagem do Volta com metadados: {canal, lead_id, ângulo, template_usado, dados_de_personalização_aplicados}).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Veredicto: APROVADO | REPROVADO com score por dimensão (0-10) e instrução de correção se reprovado) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredicto: APROVADO | REPROVADO com score por dimensão (0-10) e instrução de correção se reprovado
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vigia 2 registrado
- [ ] Gate L3 respeitado: Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico;…
- [ ] Gate L3 respeitado: Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio
- [ ] Gate L3 respeitado: Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualifi…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Envio para leads estratégicos (ticket acima de threshold definido, ex: acima de R$50k): Maestro apresenta rascunho da mensagem e histórico; humano aprova ou ed… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Qualquer mensagem que mencione desconto, condição especial ou prazo de oferta: exige aprovação do gestor comercial antes do envio | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Re-agendamento de lead que já deu no-show 2x ou mais: Agenda apresenta proposta de abordagem; closer decide se vale continuar ou desqualificar | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Lead que responde negativamente (não tenho interesse, cancela definitivamente): Maestro notifica o closer para decisão de desqualificação ou mudança de abordag… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Escalation do Vigia – Quando o Volta falha 2x na correção de uma mensagem reprovada: Vigia escala para humano com o draft e o feedback detalhado para revisão m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Revisão semanal de cadências — Atlas gera relatório de performance; gestor aprova ajustes de parâmetros (intervalos, canais, thresholds de score) antes de sere… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out recebido — Qualquer pedido de descadastro é interrompido imediatamente pelo Cronos e notificado ao responsável para confirmação de remoção do CRM | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Vigia 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vigia 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
