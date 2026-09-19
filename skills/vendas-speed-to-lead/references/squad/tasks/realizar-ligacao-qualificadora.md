---
task: sdrPorLigacao()
responsavel: "SDR por Ligacao"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead com score >= 60 + telefone validado + historico de tentativas de contato sem resposta (minimo 2 tentativas via texto)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Autorizacao do HITL Gatekeeper para ligar fora do horario comercial ou para contas estrategicas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Transcricao da call com sumario estruturado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "atualizacao de qualificacao no CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "reuniao agendada (se aplicavel) ou proximo passo registrado"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Call Realizada' com link para transcricao e recording"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Alerta imediato ao closer se lead demonstrou interesse alto"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead com score >= 60 sem resposta a texto em 48h. Acionado pelo Orchestrator com confirmacao de HITL para ligacoes fora do horario 9h-18h ou para contas com ticket > threshold definido pelo cliente."
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

# Realizar Ligação Qualificadora

**Task ID:** `sdrPorLigacao()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Realizar Ligação Qualificadora |
| **status** | `pending` |
| **responsible_executor** | SDR por Ligacao (Vox — Worker de Voz (SDR por Ligacao)) |
| **execution_type** | `Hybrid` |
| **input** | 2 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Realiza ligacoes de qualificacao por voz usando IA conversacional (<600ms de latencia) para leads de alta prioridade (score >= 60) quando tentativas de texto nao obtiveram resposta. Conduz roteiro de qualificacao, detecta interesse, agenda reuniao na propria ligacao e transcreve a call automaticamente para o CRM.

## Input

- Lead com score >= 60 + telefone validado + historico de tentativas de contato sem resposta (minimo 2 tentativas via texto)
- Autorizacao do HITL Gatekeeper para ligar fora do horario comercial ou para contas estrategicas

## Output

- Transcricao da call com sumario estruturado
- atualizacao de qualificacao no CRM
- reuniao agendada (se aplicavel) ou proximo passo registrado
- Artefato ClickUp: task 'Call Realizada' com link para transcricao e recording
- Alerta imediato ao closer se lead demonstrou interesse alto

## Trigger

Lead com score >= 60 sem resposta a texto em 48h. Acionado pelo Orchestrator com confirmacao de HITL para ligacoes fora do horario 9h-18h ou para contas com ticket > threshold definido pelo cliente.

## Knowledge base (o que o executor consulta)

- Roteiro de qualificacao por voz calibrado com linguagem natural
- respostas a objecoes frequentes em formato de conversa
- regras de horario permitido para ligacao (LGPD/compliance)
- criterios para transferir para closer humano ao vivo
- integracao com Vapi/Retell AI + ElevenLabs para voz da marca

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead com score >= 60 + telefone validado + historico de tentativas de contato sem resposta (minimo 2 tentativas via tex…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Transcricao da call com sumario estruturado) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Transcricao da call com sumario estruturado
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

- **to:** Sentinel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
