---
task: argos()
responsavel: "Argos"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Eventos de comportamento do lead (webhooks de CRM, email tracking, ad signals) + dossie do Sherlock + ficha de qualificacao do Socrates"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Executa em batch a cada 15 minutos e em tempo real para eventos de alta intencao"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score atualizado (0-100) por lead no CRM + lista ranqueada dos top-10 leads para acao imediata + alertas Slack/WhatsApp para o closer responsavel quando lead cruza threshold de 'quente' (score >= 75)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task de alerta 'Lead Quente Detectado' com link direto ao contato no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento de comportamento recebido (email aberto, link clicado, pagina de preco visitada, formulario de interesse preenchido pela segunda vez). Tambem executa em batch horario para re-ranking geral."
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

# Priorizar Leads

**Task ID:** `argos()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Priorizar Leads |
| **status** | `pending` |
| **responsible_executor** | Argos (Argos — Worker de Lead Scoring e Priorizacao) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pontua e re-ranqueia continuamente todos os leads do funil com base em fit com ICP, sinais de comportamento (abertura de email, clique, visita ao site, interacao com anuncio), dados de enriquecimento e progressao da conversa. Gera lista priorizada para o time comercial humano e aciona alertas de lead quente.

## Input

- Eventos de comportamento do lead (webhooks de CRM, email tracking, ad signals) + dossie do Sherlock + ficha de qualificacao do Socrates
- Executa em batch a cada 15 minutos e em tempo real para eventos de alta intencao

## Output

- Score atualizado (0-100) por lead no CRM + lista ranqueada dos top-10 leads para acao imediata + alertas Slack/WhatsApp para o closer responsavel quando lead cruza threshold de 'quente' (score >= 75)
- Artefato ClickUp: task de alerta 'Lead Quente Detectado' com link direto ao contato no CRM

## Trigger

Evento de comportamento recebido (email aberto, link clicado, pagina de preco visitada, formulario de interesse preenchido pela segunda vez). Tambem executa em batch horario para re-ranking geral.

## Knowledge base (o que o executor consulta)

- Modelo de scoring calibrado com deals ganhos e perdidos historicos do CRM
- pesos por tipo de evento comportamental
- limiares de score por produto/segmento
- regras de decaimento de score para leads inativos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Eventos de comportamento do lead (webhooks de CRM, email tracking, ad signals) + dossie do Sherlock + ficha de qualific…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score atualizado (0-100) por lead no CRM + lista ranqueada dos top-10 leads para acao imediata + alertas Slack/WhatsApp…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score atualizado (0-100) por lead no CRM + lista ranqueada dos top-10 leads para acao imediata + alertas Slack/WhatsApp para o closer responsavel quando lead c…
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

- **to:** Eco
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
