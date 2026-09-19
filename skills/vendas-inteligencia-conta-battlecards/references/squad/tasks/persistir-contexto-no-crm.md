---
task: memoria()
responsavel: "MEMORIA"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Output do dossie entregue, notas pos-reuniao do vendedor (texto livre ou transcricao de call), resultado da reuniao (avancou / nao avancou / motivo), dados de contato atualizados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "CRM atualizado com: campos de conta enriquecidos, novas atividades registradas, stage do deal atualizado, battlecard incrementado com objeções reais, alerta para o vendedor se detectar mudança de stakeholder ou sinal de risco no deal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo automático 2 horas após o horário da reunião (via cron/webhook de calendário). Também acionado manualmente pelo vendedor ao registrar resultado da reunião."
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

# Persistir Contexto No Crm

**Task ID:** `memoria()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Inteligência de Conta e Battlecards

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Persistir Contexto No Crm |
| **status** | `pending` |
| **responsible_executor** | MEMORIA (MEMÓRIA — O Gestor de CRM e Histórico) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de RevOps responsável por garantir que o contexto gerado pelo squad seja persistido no CRM e enriqueça futuras interações. Após a reunião (sinal de fim de evento no calendário ou input manual do vendedor), extrai pontos-chave do dossiê que foram validados/refutados, atualiza campos do CRM, registra objeções reais levantadas, atualiza o battlecard com novos dados de campo e incrementa a base de win/loss. Também faz dedup e enriquecimento contínuo dos contatos no CRM.

## Input

- Output do dossie entregue, notas pos-reuniao do vendedor (texto livre ou transcricao de call), resultado da reuniao (avancou / nao avancou / motivo), dados de contato atualizados

## Output

- CRM atualizado com: campos de conta enriquecidos, novas atividades registradas, stage do deal atualizado, battlecard incrementado com objeções reais, alerta para o vendedor se detectar mudança de stakeholder ou sinal de risco no deal

## Trigger

Disparo automático 2 horas após o horário da reunião (via cron/webhook de calendário). Também acionado manualmente pelo vendedor ao registrar resultado da reunião.

## Knowledge base (o que o executor consulta)

- CRM do cliente (HubSpot/Pipedrive via MCP), histórico de interações da conta, base de battlecards (para atualização), perfis de stakeholders gerados pelo IRIS, regras de higiene de CRM definidas pelo cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Output do dossie entregue, notas pos-reuniao do vendedor (texto livre ou transcricao de call), resultado da reuniao (av…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (CRM atualizado com: campos de conta enriquecidos, novas atividades registradas, stage do deal atualizado, battlecard in…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: CRM atualizado com: campos de conta enriquecidos, novas atividades registradas, stage do deal atualizado, battlecard incrementado com objeções reais, alerta pa…
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

- **to:** SENTINEL
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
