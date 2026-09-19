---
task: herald()
responsavel: "HERALD"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "JSON agregado e validado pelo SENTINEL, tempo até a reunião, canal de entrega preferido do vendedor, template de formatação do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossie de Conta formatado (PDF/Notion/ClickUp doc), Battlecard formatado (tabela), notificacao com resumo de 5 bullets enviada ao vendedor, tarefa marcada como concluida no ClickUp com link para os artefatos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo NEXUS após aprovação do SENTINEL. Se SENTINEL rejeitar, NEXUS re-roteia para correção antes de acionar HERALD."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM de produção"
    - "[ ] L3: Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio automático sem leitura humana"
    - "[ ] L2: Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta o que não se aplica"
    - "[ ] L1: Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão parcial ou aguardar correção"
    - "[ ] L1: Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes de qualquer ação"
---

# Entregar Artefatos Formatados

**Task ID:** `herald()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Inteligência de Conta e Battlecards

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Entregar Artefatos Formatados |
| **status** | `pending` |
| **responsible_executor** | HERALD (HERALD — O Formatador e Entregador) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker responsável pela síntese final e entrega multicanal. Recebe os outputs validados pelo SENTINEL (Critic) e os formata nos dois artefatos finais: Dossiê de Conta e Battlecard. Adapta o nível de detalhe ao tempo disponível antes da reunião (se < 2h: versão executiva 1 página; se > 24h: versão completa). Cria a tarefa/artefato no ClickUp como prova de trabalho, envia notificação ao vendedor pelo canal preferido (Slack, WhatsApp, email) com resumo executivo e link para o dossiê completo.

## Input

- JSON agregado e validado pelo SENTINEL, tempo até a reunião, canal de entrega preferido do vendedor, template de formatação do cliente

## Output

- Dossie de Conta formatado (PDF/Notion/ClickUp doc), Battlecard formatado (tabela), notificacao com resumo de 5 bullets enviada ao vendedor, tarefa marcada como concluida no ClickUp com link para os artefatos

## Trigger

Disparo pelo NEXUS após aprovação do SENTINEL. Se SENTINEL rejeitar, NEXUS re-roteia para correção antes de acionar HERALD.

## Knowledge base (o que o executor consulta)

- Templates de dossie e battlecard do cliente, preferencias de formatacao por vendedor (armazenadas em perfil), regras de marca/comunicacao do cliente, mapeamento de canais de entrega por vendedor

## Action Items

1. Confirmar o gatilho e carregar a entrada (JSON agregado e validado pelo SENTINEL, tempo até a reunião, canal de entrega preferido do vendedor, template de format…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossie de Conta formatado (PDF/Notion/ClickUp doc), Battlecard formatado (tabela), notificacao com resumo de 5 bullets…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossie de Conta formatado (PDF/Notion/ClickUp doc), Battlecard formatado (tabela), notificacao com resumo de 5 bullets enviada ao vendedor, tarefa marcada como…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SENTINEL registrado
- [ ] Gate L3 respeitado: Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistênci…
- [ ] Gate L3 respeitado: Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do…
- [ ] Gate L2 respeitado: Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio a… | BLOQUEIA até decisão humana |
| VETO-003 | L2 — Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta… | BLOQUEIA até decisão humana |
| VETO-004 | L1 — Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão p… | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** MEMORIA
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
