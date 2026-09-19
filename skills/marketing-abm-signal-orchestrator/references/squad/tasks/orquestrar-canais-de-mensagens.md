---
task: chronos()
responsavel: "Chronos"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Plano de campanha ABM completo (todos os touches planejados por canal), histórico de engajamento do stakeholder, configurações de frequência máxima por canal, timezone da conta"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Cronograma otimizado de touches por stakeholder (data/hora/canal para cada mensagem), alertas de conflito de canal, relatório de sequenciamento para aprovacao do Nexus"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo plano de campanha ABM aprovado pelo Nexus; detecção de sobreposição de canais pelo Nexus; revisão semanal de cronogramas ativos"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plataformas de ads"
    - "[ ] L3: Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad"
    - "[ ] L3: Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio"
    - "[ ] L2: Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha completa"
    - "[ ] L2: Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana sobre próximos passos"
---

# Orquestrar Canais De Mensagens

**Task ID:** `chronos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** ABM Signal Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Canais De Mensagens |
| **status** | `pending` |
| **responsible_executor** | Chronos (Chronos — Agente de Timing e Orquestração de Canais) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Determina o momento ótimo de cada toque por stakeholder e canal, evitando sobreposição de mensagens (ex: não mandar email frio e ad no mesmo dia), sequenciando os canais de forma que reforce a presença sem parecer spam. Analisa padrões de engajamento histórico (qual horário o stakeholder abre emails, quando está ativo no LinkedIn) e ajusta o cronograma de toda a campanha ABM da conta.

## Input

- Plano de campanha ABM completo (todos os touches planejados por canal), histórico de engajamento do stakeholder, configurações de frequência máxima por canal, timezone da conta

## Output

- Cronograma otimizado de touches por stakeholder (data/hora/canal para cada mensagem), alertas de conflito de canal, relatório de sequenciamento para aprovacao do Nexus

## Trigger

Novo plano de campanha ABM aprovado pelo Nexus; detecção de sobreposição de canais pelo Nexus; revisão semanal de cronogramas ativos

## Knowledge base (o que o executor consulta)

- Padrões de engajamento por persona e setor, benchmarks de melhor horário por canal (email, LinkedIn, WhatsApp), regras de frequência máxima por canal, histórico de performance por horário

## Action Items

1. Confirmar o gatilho e carregar a entrada (Plano de campanha ABM completo (todos os touches planejados por canal), histórico de engajamento do stakeholder, config…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Cronograma otimizado de touches por stakeholder (data/hora/canal para cada mensagem), alertas de conflito de canal, rel…) e persistir no artefato do squad.
4. Entregar ao critic Aegis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Cronograma otimizado de touches por stakeholder (data/hora/canal para cada mensagem), alertas de conflito de canal, relatório de sequenciamento para aprovacao…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis registrado
- [ ] Gate L3 respeitado: Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto…
- [ ] Gate L3 respeitado: Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi c…
- [ ] Gate L3 respeitado: Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Aprovação de lançamento de campanha de anúncio pago para conta (Pixel): humano valida budget, audiência e criativos antes de qualquer gasto financeiro em plata… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Aprovação de outreach externo para nova conta (Hermes): humano revisa a sequência completa antes do primeiro toque em conta que nunca foi contactada pelo squad | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Aprovação de mensagem WhatsApp para stakeholder C-Level (Hermes): canais de alta criticidade exigem revisão humana antes do envio | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Revisão do Account Intelligence Profile para contas Tier 1 (Atlas): humano valida mapeamento do buying committee e ICP score antes de Nexus decompor campanha c… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Revisão de anomalias críticas reportadas por Prism: contas Tier 1 com queda brusca de engajamento ou stakeholder que deixou a empresa requerem decisão humana s… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Curadoria do Account Universe Map: adicionar/remover contas do universo ABM e ajustar Tiers requer input estratégico humano (revisão quinzenal) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Aegis | BLOQUEIA entrega |

## Handoff

- **to:** Prism
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
