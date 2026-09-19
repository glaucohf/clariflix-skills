---
task: gate()
responsavel: "GATE"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ação proposta por qualquer worker (tipo, descrição, impacto estimado, reversibilidade, urgência), output do worker que gerou a ação, contexto da demanda original, classificação de risco calculada pelo ORION"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Briefing de aprovação com: (1) Descrição clara da ação em linguagem não técnica, (2) Contexto"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "por que está sendo proposta, (3) Impacto se APROVADO vs se REJEITADO, (4) Risco de reversibilidade (escala 1-5), (5) Opções: texto exato do que será executado / alternativa mais conservadora / cancelamento, (6) Log registrado no ClickUp independente da decisão"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Notificação ao founder via canal preferido (WhatsApp prioritário para L3 urgente, Slack para padrão)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Interceptação automática de qualquer ação L3 antes da execução — não pode ser bypassado. Disparado pelo ORION toda vez que classifica uma ação como IRREVERSÍVEL, FINANCEIRA, ENVIO EXTERNO CRÍTICO ou…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio – o squad nunca envia comunicação externa autonomamente"
    - "[ ] L3: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política interna – founder aprova com opções claras antes da execução"
    - "[ ] L3: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao de pensamento antes de ser persistida no corpus canônico"
    - "[ ] L2: ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma aproximação e pode escalonar"
    - "[ ] L2: STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer caminho seja comunicado como recomendacao oficial do squad"
---

# Controlar Ações L3

**Task ID:** `gate()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Clône Estratégico do Founder — Digital Twin

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Controlar Ações L3 |
| **status** | `pending` |
| **responsible_executor** | GATE (GATE — O Agente HITL e Guardião de Fronteiras) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de controle e governança do squad. Intercepta toda ação classificada como L3 (irreversível, financeira, envio externo, decisão com impacto político/legal) antes da execução. Prepara um briefing executivo da ação proposta: o que será feito, por que, qual o contexto, quais os riscos se aprovado e quais os riscos se negado. Apresenta ao founder com opções claras (APROVAR / REJEITAR / MODIFICAR) e garante que nenhuma ação de alto impacto ocorra sem confirmação humana explícita. Também mantém o log de todas as ações L3 para auditoria e aprendizado. Monitora proativamente se algum worker está tentando executar ação L3 sem passar pelo gate — BLOQUEIO IMEDIATO e alerta ao founder.

## Input

- Ação proposta por qualquer worker (tipo, descrição, impacto estimado, reversibilidade, urgência), output do worker que gerou a ação, contexto da demanda original, classificação de risco calculada pelo ORION

## Output

- Briefing de aprovação com: (1) Descrição clara da ação em linguagem não técnica, (2) Contexto
- por que está sendo proposta, (3) Impacto se APROVADO vs se REJEITADO, (4) Risco de reversibilidade (escala 1-5), (5) Opções: texto exato do que será executado / alternativa mais conservadora / cancelamento, (6) Log registrado no ClickUp independente da decisão
- Notificação ao founder via canal preferido (WhatsApp prioritário para L3 urgente, Slack para padrão)

## Trigger

Interceptação automática de qualquer ação L3 antes da execução — não pode ser bypassado. Disparado pelo ORION toda vez que classifica uma ação como IRREVERSÍVEL, FINANCEIRA, ENVIO EXTERNO CRÍTICO ou NOVO TERRITÓRIO ESTRATÉGICO. Também monitora outputs de todos os workers em busca de ações L3 não sinalizadas.

## Knowledge base (o que o executor consulta)

- Matriz de classificação de risco (reversibilidade x impacto x tipo de ação), histórico de aprovações e rejeições anteriores (para calibrar threshold), contatos e canais do founder por urgência, regras de compliance e governança definidas na fase Discovery, log de todas as ações L3 executadas ou negadas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ação proposta por qualquer worker (tipo, descrição, impacto estimado, reversibilidade, urgência), output do worker que…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Briefing de aprovação com: (1) Descrição clara da ação em linguagem não técnica, (2) Contexto) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Briefing de aprovação com: (1) Descrição clara da ação em linguagem não técnica, (2) Contexto
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SENTINEL registrado
- [ ] Gate L3 respeitado: HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder ante…
- [ ] Gate L3 respeitado: GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou…
- [ ] Gate L3 respeitado: Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuin…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — HERALD: todo draft de comunicação externa (board memo, email para investidor, comunicado público) exige aprovação explícita do founder antes de qualquer envio… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — GATE intercepta: qualquer decisão ou ação classificada como irreversível, com impacto financeiro direto, novo posicionamento estratégico ou mudança de política… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Atualizacao do Knowledge Graph com novos frameworks ou correcoes de principios fundamentais: founder valida que a mudanca representa genuinamente sua evolucao… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — ECHO em modo MÉDIA CONFIANÇA (50-69%): resposta e entregue com flag explícita de incerteza e solicitação de validação ao founder – o usuário sabe que é uma apr… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — STRATEGOS em analises de cenarios para decisoes de alta irreversibilidade: founder revisa a arvore de decisao e as probabilidades estimadas antes que qualquer… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — VIGIL ao detectar sinal competitivo CRÍTICO fora do ciclo semanal: notificação imediata ao founder com proposta de contra-jogada — founder decide se ativa resp… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — CHRONICLE ao identificar gap crítico no corpus que impacta a confiabilidade do ECHO em categoria de alto volume: agenda sessão de captura de conhecimento com o… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** SENTINEL
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
