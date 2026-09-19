---
task: magnus()
responsavel: "Magnus"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossie de conta (Sherlock), alerta de sinal (Radar), historico de interacoes do lead no CRM, configuracao de pesos do modelo de scoring (editavel pelo time comercial)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score numérico (0-100) com breakdown detalhado por dimensão: ICP Fit (0-25), Signal Strength (0-25), Engagement History (0-20), Deal Size Estimate (0-15), Timing Urgency (0-15)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tag de prioridade: HOT (>75), WARM (50-75), COLD (<50)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Atualização automática do campo de score no CRM e reordenação da fila no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Automaticamente apos Sherlock entregar o dossie. Re-trigger a cada novo sinal detectado pelo Radar para o mesmo lead. Re-trigger se o lead interagir com qualquer mensagem enviada."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo."
    - "[ ] HITL: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial."
    - "[ ] HITL: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual."
    - "[ ] HITL: Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo."
    - "[ ] HITL: Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach."
---

# Classificar Leads

**Task ID:** `magnus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Leads |
| **status** | `pending` |
| **responsible_executor** | Magnus (Magnus — Scorer e Priorizador de Leads) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pontua continuamente cada lead na fila com base no dossie do Sherlock, forca do sinal, fit de ICP, historico de engajamento anterior, tamanho do deal estimado e urgencia temporal do sinal. Re-ranqueia a fila de prospeccao em tempo real para que o Nexus e o SDR humano sempre trabalhem os leads de maior probabilidade de conversao primeiro.

## Input

- Dossie de conta (Sherlock), alerta de sinal (Radar), historico de interacoes do lead no CRM, configuracao de pesos do modelo de scoring (editavel pelo time comercial)

## Output

- Score numérico (0-100) com breakdown detalhado por dimensão: ICP Fit (0-25), Signal Strength (0-25), Engagement History (0-20), Deal Size Estimate (0-15), Timing Urgency (0-15)
- Tag de prioridade: HOT (>75), WARM (50-75), COLD (<50)
- Atualização automática do campo de score no CRM e reordenação da fila no ClickUp

## Trigger

Automaticamente apos Sherlock entregar o dossie. Re-trigger a cada novo sinal detectado pelo Radar para o mesmo lead. Re-trigger se o lead interagir com qualquer mensagem enviada.

## Knowledge base (o que o executor consulta)

- Modelo de scoring configurável (pesos por dimensão editáveis sem código)
- Histórico de deals fechados com seus scores no momento da qualificação (feedback loop para calibragem)
- Definição de ICP por tier (Tier 1: deal >R$20k, Tier 2: R$5-20k, Tier 3: <R$5k)
- Regras de fast-track para sinais de altíssima urgência (ex: lead que pediu demo = HOT automático)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossie de conta (Sherlock), alerta de sinal (Radar), historico de interacoes do lead no CRM, configuracao de pesos do m…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score numérico (0-100) com breakdown detalhado por dimensão: ICP Fit (0-25), Signal Strength (0-25), Engagement History…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score numérico (0-100) com breakdown detalhado por dimensão: ICP Fit (0-25), Signal Strength (0-25), Engagement History (0-20), Deal Size Estimate (0-15), Timi…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossi…
- [ ] Gate HITL respeitado: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do…
- [ ] Gate HITL respeitado: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação ant… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Unsubscribe ou resposta negativa agressiva: processado pelo Lumen, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Penna
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
