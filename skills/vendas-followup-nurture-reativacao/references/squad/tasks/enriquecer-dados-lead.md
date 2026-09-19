---
task: sherlock()
responsavel: "Sherlock"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "lead_id com dados básicos do CRM (nome, email, empresa)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "request do Maestro para enriquecimento pré-cadência"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê do lead em JSON: {nome, cargo_atual, empresa, segmento, tamanho, tecnologias_usadas, notícias_recentes, conexões_em_comum, trigger_de_intenção_identificado, score_de_fit}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Campos atualizados no CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp: 'Sherlock-Dossiê-{lead_id}' com data de atualização"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo lead entrando em cadência de reativação; lead sem enriquecimento há mais de 30 dias; request manual do Maestro para re-enriquecimento"
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

# Enriquecer Dados Lead

**Task ID:** `sherlock()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Follow-up, Nurture e Reativacao

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dados Lead |
| **status** | `pending` |
| **responsible_executor** | Sherlock (Sherlock – Worker de Enriquecimento e Dossiê) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pesquisador de contas e leads. Antes de qualquer cadência iniciada para um lead, verifica se os dados estão completos e atualizados. Busca cargo atual, empresa, tamanho de time, stack de tecnologia, notícias recentes da empresa, mudanças de cargo no LinkedIn, sinais de intenção. Gera um dossiê resumido que o Volta usa para personalizar mensagens. Também realiza higiene no CRM: deduplicação, correção de emails inválidos, enriquecimento de campos vazios.

## Input

- lead_id com dados básicos do CRM (nome, email, empresa)
- request do Maestro para enriquecimento pré-cadência

## Output

- Dossiê do lead em JSON: {nome, cargo_atual, empresa, segmento, tamanho, tecnologias_usadas, notícias_recentes, conexões_em_comum, trigger_de_intenção_identificado, score_de_fit}
- Campos atualizados no CRM
- Task no ClickUp: 'Sherlock-Dossiê-{lead_id}' com data de atualização

## Trigger

Novo lead entrando em cadência de reativação; lead sem enriquecimento há mais de 30 dias; request manual do Maestro para re-enriquecimento

## Knowledge base (o que o executor consulta)

- APIs de enriquecimento (Clay, Apollo 275M+ contatos, Clearbit)
- LinkedIn Sales Navigator (sinais de mudança de cargo)
- critérios de ICP da empresa cliente
- mapeamento de campos CRM para enriquecimento

## Action Items

1. Confirmar o gatilho e carregar a entrada (lead_id com dados básicos do CRM (nome, email, empresa)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossiê do lead em JSON: {nome, cargo_atual, empresa, segmento, tamanho, tecnologias_usadas, notícias_recentes, conexões…) e persistir no artefato do squad.
4. Entregar ao critic Vigia 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossiê do lead em JSON: {nome, cargo_atual, empresa, segmento, tamanho, tecnologias_usadas, notícias_recentes, conexões_em_comum, trigger_de_intenção_identific…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
