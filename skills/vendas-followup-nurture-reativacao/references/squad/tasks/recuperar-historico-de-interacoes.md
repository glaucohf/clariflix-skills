---
task: memento()
responsavel: "Memento"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "request de contexto do Maestro ou do Volta antes de redigir mensagem"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "novas interações a serem registradas (mensagem enviada, resposta recebida, call transcrita)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resumo de contexto em texto (max 500 tokens): últimos N toques, objeções registradas, compromissos feitos, ângulos já utilizados, recomendação de ângulo não utilizado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Histórico atualizado no CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Deduplicação de conteúdo (flag se ângulo já foi usado)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Request de contexto antes de qualquer novo toque pelo Volta; conclusão de call (webhook do Gong/Chorus); resposta recebida do lead (para registrar e atualizar histórico)"
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

# Recuperar Histórico de Interações

**Task ID:** `memento()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Recuperar Histórico de Interações |
| **status** | `pending` |
| **responsible_executor** | Memento (Memento — Worker de Histórico e Contexto Conversacional) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mantem e recupera o historico completo de interacoes de cada lead: todas as mensagens enviadas e recebidas, calls transcritas (integracao com Gong/Chorus ou transcricao local), objecoes levantadas, compromissos feitos, motivos de recusa anteriores. Antes de qualquer novo toque, fornece ao Volta um contexto resumido para que a mensagem nao seja generica e referencie o historico de forma inteligente ('Voce mencionou que o budget seria revisado em julho — chegou esse momento?'). Evita que o lead receba a mesma mensagem duas vezes.

## Input

- request de contexto do Maestro ou do Volta antes de redigir mensagem
- novas interações a serem registradas (mensagem enviada, resposta recebida, call transcrita)

## Output

- Resumo de contexto em texto (max 500 tokens): últimos N toques, objeções registradas, compromissos feitos, ângulos já utilizados, recomendação de ângulo não utilizado
- Histórico atualizado no CRM
- Deduplicação de conteúdo (flag se ângulo já foi usado)

## Trigger

Request de contexto antes de qualquer novo toque pelo Volta; conclusão de call (webhook do Gong/Chorus); resposta recebida do lead (para registrar e atualizar histórico)

## Knowledge base (o que o executor consulta)

- Histórico completo de interações no CRM
- transcrições de calls (Gong, Chorus ou Whisper local)
- templates de ângulos utilizados por cadência
- mapeamento de objeções mais comuns e contra-argumentos testados

## Action Items

1. Confirmar o gatilho e carregar a entrada (request de contexto do Maestro ou do Volta antes de redigir mensagem).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resumo de contexto em texto (max 500 tokens): últimos N toques, objeções registradas, compromissos feitos, ângulos já u…) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resumo de contexto em texto (max 500 tokens): últimos N toques, objeções registradas, compromissos feitos, ângulos já utilizados, recomendação de ângulo não ut…
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

- **to:** Vigia
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
