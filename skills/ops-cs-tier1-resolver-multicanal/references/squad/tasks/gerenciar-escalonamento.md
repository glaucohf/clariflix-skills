---
task: hermes()
responsavel: "Hermes"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal de escalonamento do Orchestrator ou do Critic + transcrição completa da conversa + ações executadas + confiança score + dados do cliente (tier, histórico, LTV)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Ticket criado no Zendesk/Intercom com prioridade, tags e resumo executivo em 5 bullets"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Notificação Slack para fila correta"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp com motivo de escalonamento e contexto"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Mensagem ao cliente confirmando transferência com ETA humano"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Critic retorna 'ESCALATE'; confianca do classifier < 0.72; valor financeiro > limite de autonomia; palavras-chave de risco legal detectadas; cliente em tier VIP/Enterprise; terceira tentativa sem res…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário"
    - "[ ] HITL: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo"
    - "[ ] HITL: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados"
    - "[ ] HITL: Terceira interação na mesma sessão sem resolução confirmada pelo cliente"
    - "[ ] HITL: Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação"
---

# Gerenciar Escalonamento

**Task ID:** `hermes()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Suporte Conversacional Multicanal (Tier-1 Resolver)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerenciar Escalonamento |
| **status** | `pending` |
| **responsible_executor** | Hermes (Hermes — Agente de Handoff & Escalonamento HITL) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia transferências para humanos: identifica triggers de escalonamento (confiança baixa, ação irreversível acima de limite, sentimento muito negativo, menção de termos jurídicos/imprensa/PROCON, terceira interação sem resolução), prepara o pacote de contexto completo para o agente humano (resumo da conversa, intenção, ações já tentadas, dados do cliente, sugestão de resolução), cria ticket no helpdesk com prioridade correta e notifica o time no Slack.

## Input

- Sinal de escalonamento do Orchestrator ou do Critic + transcrição completa da conversa + ações executadas + confiança score + dados do cliente (tier, histórico, LTV)

## Output

- Ticket criado no Zendesk/Intercom com prioridade, tags e resumo executivo em 5 bullets
- Notificação Slack para fila correta
- Task no ClickUp com motivo de escalonamento e contexto
- Mensagem ao cliente confirmando transferência com ETA humano

## Trigger

Critic retorna 'ESCALATE'; confianca do classifier < 0.72; valor financeiro > limite de autonomia; palavras-chave de risco legal detectadas; cliente em tier VIP/Enterprise; terceira tentativa sem resolucao na mesma sessao

## Knowledge base (o que o executor consulta)

- Matriz de escalonamento (criticidade x reversibilidade x tier de cliente), templates de notificação por canal (Slack, email, Zendesk), SLAs por fila humana, lista de palavras-chave de risco (jurídico, PROCON, chargeback, redes sociais), histórico de escalonamentos anteriores

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinal de escalonamento do Orchestrator ou do Critic + transcrição completa da conversa + ações executadas + confiança s…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Ticket criado no Zendesk/Intercom com prioridade, tags e resumo executivo em 5 bullets) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Ticket criado no Zendesk/Intercom com prioridade, tags e resumo executivo em 5 bullets
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário
- [ ] Gate HITL respeitado: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo
- [ ] Gate HITL respeitado: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Terceira interação na mesma sessão sem resolução confirmada pelo cliente | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Menção de palavras-chave de risco: 'advogado', 'PROCON', 'Reclame Aqui', 'processo', 'imprensa', 'TV' | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Solicitacao de troca/devolucao fora do prazo de politica ou em categoria inelegivel — Volta escalona para decisao humana com contexto | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Health score do cliente cai abaixo de 45 durante a interação — Pulse dispara alerta para CSM responsável | BLOQUEIA até decisão humana |
| VETO-009 | HITL — Áudio com qualidade ASR < 0.80 de confiança — Vox marca para revisão humana antes de processar | BLOQUEIA até decisão humana |
| VETO-010 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Pulse
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
