---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de qualificacao do Socrates com classificacao SQL + preferencias de horario coletadas na conversa"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Canal de comunicacao ativo"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Evento criado no calendario (Google/Outlook) com link de videoconferencia"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "confirmacao enviada ao lead via canal preferido"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "lembrete configurado"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "registro no CRM (campo 'reuniao_agendada_em', 'status_reuniao')"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Reuniao Agendada' com dados do evento"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead classificado como SQL pelo Socrates. Tambem acionado por no-show detectado (reuniao nao ocorreu) para reagendamento automatico."
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

# Agendar Reunião

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Agendar Reunião |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Worker de Agendamento) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Coordena o agendamento da reuniao/demo com o closer humano diretamente na conversa com o lead. Verifica disponibilidade em tempo real, propoe 3 horarios, confirma, envia convite no calendario, envia lembretes (D-1 e H-1) e gerencia reagendamentos sem interacao humana.

## Input

- Ficha de qualificacao do Socrates com classificacao SQL + preferencias de horario coletadas na conversa
- Canal de comunicacao ativo

## Output

- Evento criado no calendario (Google/Outlook) com link de videoconferencia
- confirmacao enviada ao lead via canal preferido
- lembrete configurado
- registro no CRM (campo 'reuniao_agendada_em', 'status_reuniao')
- Artefato ClickUp: task 'Reuniao Agendada' com dados do evento

## Trigger

Lead classificado como SQL pelo Socrates. Tambem acionado por no-show detectado (reuniao nao ocorreu) para reagendamento automatico.

## Knowledge base (o que o executor consulta)

- Regras de disponibilidade de cada closer (horarios bloqueados, territorios, produtos de especialidade)
- templates de confirmacao e lembrete por canal
- politica de reagendamento (maximo de tentativas, intervalo entre tentativas)
- integracao com Google Calendar/Outlook via MCP

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ficha de qualificacao do Socrates com classificacao SQL + preferencias de horario coletadas na conversa).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Evento criado no calendario (Google/Outlook) com link de videoconferencia) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Evento criado no calendario (Google/Outlook) com link de videoconferencia
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

- **to:** Argos
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
