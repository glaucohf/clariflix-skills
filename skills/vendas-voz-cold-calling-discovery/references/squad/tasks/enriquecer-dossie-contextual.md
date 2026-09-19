---
task: dossie()
responsavel: "Dossie"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead record (nome, empresa, cargo, telefone, email, origem do lead)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Opcional: URL do site, LinkedIn da empresa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossié JSON com: resumo da empresa (3-5 bullets), dores previstas por vertical, sinais de intenção detectados, score de enriquecimento (0-100), campos preenchidos no CRM (HubSpot/Pipedrive), contexto injetado no prompt do agente de voz"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo lead entra na fila de discagem. Lead reativado após 30 dias de frio. Antes de cada ligação de discovery agendada."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Filtro 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3)."
    - "[ ] HITL: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3)."
    - "[ ] HITL: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3)."
    - "[ ] HITL: Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3)."
    - "[ ] HITL: Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation)."
---

# Enriquecer Dossie Contextual

**Task ID:** `dossie()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz para Cold Calling e Discovery

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dossie Contextual |
| **status** | `pending` |
| **responsible_executor** | Dossie (Dossié (Worker de Enriquecimento e Pesquisa de Conta)) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe nome/empresa/telefone/email do lead e produz dossie de contexto antes da ligacao: setor, tamanho, noticias recentes, stack tecnologica provavel, sinais de intencao, cargo do contato e possiveis dores por vertical. Alimenta o roteiro dinamico do agente de voz com contexto personalizado.

## Input

- Lead record (nome, empresa, cargo, telefone, email, origem do lead)
- Opcional: URL do site, LinkedIn da empresa

## Output

- Dossié JSON com: resumo da empresa (3-5 bullets), dores previstas por vertical, sinais de intenção detectados, score de enriquecimento (0-100), campos preenchidos no CRM (HubSpot/Pipedrive), contexto injetado no prompt do agente de voz

## Trigger

Novo lead entra na fila de discagem. Lead reativado após 30 dias de frio. Antes de cada ligação de discovery agendada.

## Knowledge base (o que o executor consulta)

- Apollo (275M+ contatos), Clay para enriquecimento dinamico, base de ICP da empresa cliente (personas, verticais, criterios BANT), historico de conversas anteriores do lead no CRM, noticias recentes via web search

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead record (nome, empresa, cargo, telefone, email, origem do lead)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossié JSON com: resumo da empresa (3-5 bullets), dores previstas por vertical, sinais de intenção detectados, score de…) e persistir no artefato do squad.
4. Entregar ao critic Filtro 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossié JSON com: resumo da empresa (3-5 bullets), dores previstas por vertical, sinais de intenção detectados, score de enriquecimento (0-100), campos preenchi…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Filtro 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3).
- [ ] Gate HITL respeitado: Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3).
- [ ] Gate HITL respeitado: Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3).

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Blueprint Técnico e roteiros de voz antes da ativação em produção (gate de onboarding — L3). | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão de leads marcados como SUSPEITO pelo Filtro Agent antes de agendar com closer (L3). | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de ajustes no roteiro sugeridos pelo Insight Agent quando impacto estimado > 20% na taxa de conversão (L3). | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Autorização para discagem em contas estratégicas (ex: enterprise, parceiros atuais) — requer aprovação do gestor comercial (L3). | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão de leads com score de enriquecimento < 40 antes de entrar na fila de discagem (L2 -> L3 escalation). | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Confirmação de reagendamento quando prospect cancela reunião pela segunda vez consecutiva (decisão humana sobre continuar ou desqualificar — L3). | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Calibragem quinzenal de voz e persona do Vox Agent com gestor de vendas (revisão humana de amostras de áudio — L1). | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Filtro 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vox (Worker de Voz
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
