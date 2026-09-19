---
task: calibreScorer()
responsavel: "Calibre Scorer"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossie de conta (Scout Profiler)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "ICP Card com criterios de fit por tier (ICP Cartografo)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Historico de interacoes do lead no CRM (emails abertos, links clicados, respostas anteriores)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Configuracao de pesos do modelo de scoring editavel pelo time comercial"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Sinais de intent quando disponiveis (Clay, Bombora, LinkedIn Sales Navigator)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score numérico (0-100) com breakdown por dimensão: ICP Fit (0-30, peso maior por ser o critério mais preditivo), Intent Signal Strength (0-25), Engagement History (0-20), Deal Size Estimate (0-15), Timing Urgency (0-10)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tag de prioridade: FIRE (>80, processar imediatamente), HOT (60-80, processar em 2h), WARM (40-60, processar em 24h), COLD (<40, queue de baixa prioridade)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Atualização automática do campo de score no CRM e reordenação da fila no ClickUp"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Log de auditoria com razão do score"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Automaticamente apos Scout Profiler entregar o dossie completo. Re-trigger a cada novo sinal de intent detectado para o mesmo lead. Re-trigger se o lead interagir com qualquer mensagem enviada (abert…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR humano com draft completo, dossiê e score para aprovação ou rejeição com 1 clique antes de qualquer disparo."
    - "[ ] HITL: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o feedback detalhado do critic para reescritura manual."
    - "[ ] HITL: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente não envia com informação não verificada."
    - "[ ] HITL: Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para assumir a conversa — o squad nao conduz negociacao, apenas entrega o contexto completo e recua."
    - "[ ] HITL: Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do gestor comercial antes de qualquer envio."
---

# Pontuar Leads

**Task ID:** `calibreScorer()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Pontuar Leads |
| **status** | `pending` |
| **responsible_executor** | Calibre Scorer (Calibre Scorer — O Priorizador Frio) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pontua cada lead/conta da fila com base em 5 dimensões calibradas ao histórico de conversão do cliente e re-ranqueia continuamente a fila para que o Maestro e o SDR humano sempre trabalhem os leads de maior probabilidade de conversão primeiro. Opera de forma deterministicamente — sem opinião, sem subjetividade: aplica os pesos configurados, produz o score com breakdown auditável e atualiza o CRM. E o único agente autorizado a definir prioridade de processamento na fila.

## Input

- Dossie de conta (Scout Profiler)
- ICP Card com criterios de fit por tier (ICP Cartografo)
- Historico de interacoes do lead no CRM (emails abertos, links clicados, respostas anteriores)
- Configuracao de pesos do modelo de scoring editavel pelo time comercial
- Sinais de intent quando disponiveis (Clay, Bombora, LinkedIn Sales Navigator)

## Output

- Score numérico (0-100) com breakdown por dimensão: ICP Fit (0-30, peso maior por ser o critério mais preditivo), Intent Signal Strength (0-25), Engagement History (0-20), Deal Size Estimate (0-15), Timing Urgency (0-10)
- Tag de prioridade: FIRE (>80, processar imediatamente), HOT (60-80, processar em 2h), WARM (40-60, processar em 24h), COLD (<40, queue de baixa prioridade)
- Atualização automática do campo de score no CRM e reordenação da fila no ClickUp
- Log de auditoria com razão do score

## Trigger

Automaticamente apos Scout Profiler entregar o dossie completo. Re-trigger a cada novo sinal de intent detectado para o mesmo lead. Re-trigger se o lead interagir com qualquer mensagem enviada (abertura de email, click, resposta). Trigger manual pelo SDR humano para re-avaliar conta especifica.

## Knowledge base (o que o executor consulta)

- Modelo de scoring configurável
- pesos por dimensão editáveis sem código via arquivo YAML
- Histórico de deals fechados com seus scores no momento da qualificação para feedback loop de calibragem trimestral
- Definição de tiers por deal size (configurada no onboarding)
- Regras de fast-track automático: lead que pediu demo manualmente = FIRE sem scoring
- Regras de exclusão: empresas em negociação ativa ou clientes existentes = skip automático

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossie de conta (Scout Profiler)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score numérico (0-100) com breakdown por dimensão: ICP Fit (0-30, peso maior por ser o critério mais preditivo), Intent…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score numérico (0-100) com breakdown por dimensão: ICP Fit (0-30, peso maior por ser o critério mais preditivo), Intent Signal Strength (0-25), Engagement Hist…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloquei…
- [ ] Gate HITL respeitado: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para…
- [ ] Gate HITL respeitado: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR h… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o f… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente nã… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para a… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ICP Cartografo detecta shift significativo de mercado (nova objecao emergindo em >30% das respostas, queda de >20% no reply rate em 2 semanas consecutivas): al… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out ou resposta negativa agressiva: processado pelo Pulse Analyst, sequência cancelada automaticamente, CRM atualizado, notificação ao SDR para decisão sob… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Cyrano Copywriter
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
