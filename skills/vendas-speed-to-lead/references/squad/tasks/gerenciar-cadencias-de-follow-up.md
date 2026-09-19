---
task: eco()
responsavel: "Eco"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de leads sem resposta (>24h sem interacao) + MQLs em nurture + gatilhos de reativacao do Argos"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Recebe configuracao de cadencia (numero de tentativas, intervalos, canais) do Orchestrator"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Mensagens de follow-up enviadas com registro de entrega"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "deteccao de resposta e interrupcao de cadencia"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "leads reativados passados de volta ao Socrates para qualificacao"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task por lead com log completo de cadencia (tentativa, canal, timestamp, status de resposta)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead sem resposta por 24h apos primeiro contato do Flash. Lead classificado como MQL pelo Socrates. Gatilho de reativacao disparado pelo Argos (sinal de intencao em lead frio). Cancelamento de reunia…"
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

# Gerenciar Cadências De Follow-Up

**Task ID:** `eco()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerenciar Cadências De Follow-Up |
| **status** | `pending` |
| **responsible_executor** | Eco (Eco — Worker de Follow-up e Nurture) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia cadencias de follow-up para leads que nao responderam ao primeiro contato e para MQLs em nurture. Executa sequencias multicanal (WhatsApp, email, LinkedIn) com espacamento inteligente, detecta resposta e interrompe cadencia automaticamente. Reativa leads frios com gatilhos de contexto (novo conteudo, evento do setor, mudanca de cargo detectada).

## Input

- Lista de leads sem resposta (>24h sem interacao) + MQLs em nurture + gatilhos de reativacao do Argos
- Recebe configuracao de cadencia (numero de tentativas, intervalos, canais) do Orchestrator

## Output

- Mensagens de follow-up enviadas com registro de entrega
- deteccao de resposta e interrupcao de cadencia
- leads reativados passados de volta ao Socrates para qualificacao
- Artefato ClickUp: task por lead com log completo de cadencia (tentativa, canal, timestamp, status de resposta)

## Trigger

Lead sem resposta por 24h apos primeiro contato do Flash. Lead classificado como MQL pelo Socrates. Gatilho de reativacao disparado pelo Argos (sinal de intencao em lead frio). Cancelamento de reuniao detectado.

## Knowledge base (o que o executor consulta)

- Templates de follow-up por posicao na cadencia (tentativa 1 = curiosidade, tentativa 2 = valor, tentativa 3 = urgencia, tentativa 4 = break-up)
- regras de espacamento por canal
- politica de desistencia (maximo de tentativas antes de marcar como 'inativo')
- conteudos de nurture por segmento e estagio do funil

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de leads sem resposta (>24h sem interacao) + MQLs em nurture + gatilhos de reativacao do Argos).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Mensagens de follow-up enviadas com registro de entrega) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Mensagens de follow-up enviadas com registro de entrega
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

- **to:** SDR por Ligacao
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
