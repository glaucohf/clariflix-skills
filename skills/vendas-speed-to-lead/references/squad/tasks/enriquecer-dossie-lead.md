---
task: sherlock()
responsavel: "Sherlock"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Email corporativo e/ou nome + empresa do lead"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Recebe do Orchestrator apos primeiro contato ser enviado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Dossie estruturado (JSON) com: empresa (nome, setor, tamanho, receita estimada), cargo e seniority do lead, score de fit com ICP (0-100), sinais de intencao detectados, links de perfil LinkedIn/site, historico CRM"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registrado como nota enriquecida no contato do CRM"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato ClickUp: task 'Enriquecimento Concluido' com score de completude dos campos"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orchestrator imediatamente apos criacao do lead, em paralelo ao Flash. Re-acionado quando novo dado de contato e adicionado ao CRM."
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

# Enriquecer Dossiê Lead

**Task ID:** `sherlock()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Speed-to-Lead

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dossiê Lead |
| **status** | `pending` |
| **responsible_executor** | Sherlock (Sherlock — Worker de Enriquecimento de Lead) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Constrói o dossie completo do lead/conta em paralelo ao primeiro contato: empresa, cargo, setor, tamanho, sinais de intencao, presenca digital, fit com ICP, historico de interacoes anteriores no CRM. Alimenta o Lead Scoring com dados estruturados.

## Input

- Email corporativo e/ou nome + empresa do lead
- Recebe do Orchestrator apos primeiro contato ser enviado

## Output

- Dossie estruturado (JSON) com: empresa (nome, setor, tamanho, receita estimada), cargo e seniority do lead, score de fit com ICP (0-100), sinais de intencao detectados, links de perfil LinkedIn/site, historico CRM
- Registrado como nota enriquecida no contato do CRM
- Artefato ClickUp: task 'Enriquecimento Concluido' com score de completude dos campos

## Trigger

Acionado pelo Orchestrator imediatamente apos criacao do lead, em paralelo ao Flash. Re-acionado quando novo dado de contato e adicionado ao CRM.

## Knowledge base (o que o executor consulta)

- Criterios de ICP do cliente (setor, porte, cargo, regiao, budget estimado)
- integracao com Clay/Apollo para busca de dados
- criterios de scoring por dimensao
- historico de deals do CRM para padroes de ICP real

## Action Items

1. Confirmar o gatilho e carregar a entrada (Email corporativo e/ou nome + empresa do lead).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Dossie estruturado (JSON) com: empresa (nome, setor, tamanho, receita estimada), cargo e seniority do lead, score de fi…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Dossie estruturado (JSON) com: empresa (nome, setor, tamanho, receita estimada), cargo e seniority do lead, score de fit com ICP (0-100), sinais de intencao de…
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

- **to:** Sócrates
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
