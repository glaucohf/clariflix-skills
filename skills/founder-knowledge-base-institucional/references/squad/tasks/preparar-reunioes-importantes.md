---
task: chiefOfStaff()
responsavel: "CHIEF OF STAFF"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Calendário do founder (Google Calendar / Outlook via MCP), inbox de email (Gmail via MCP), ClickUp (tarefas e projetos), Slack (mensagens marcadas como high-priority), grafo de conhecimento (para responder demandas sem interromper o founder), lista de OKRs e prioridades do trimestre"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Briefing pre-reuniao (1 pagina, Notion), digest de follow-ups pendentes (Slack, segunda-feiras 8h), relatorio de demandas filtradas (log de quantas foram respondidas pelo clone sem interromper o founder), agenda estrategica semanal com top-3 decisoes prioritarias"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tudo como tarefas verificaveis no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Execução proativa: briefings disparados 24h antes de reuniões detectadas no calendário. Digest de follow-ups toda segunda-feira 8h. Filtragem de demandas em tempo real quando outros squads consultam…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic AUDITOR antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automaticamente — pausa e apresenta ao founder os dois claims com contexto (data, situacao) para ele determinar qual e a posicao atual e por que evoluiu. Irreversivel porque altera permanentemente o grafo canônico."
    - "[ ] L3: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída para fora da empresa exige leitura e aprovação explícita do founder. O clone fala pela empresa — erro de representação e irreversível reputacionalmente."
    - "[ ] L3: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com anotações de contexto por seção para facilitar a revisão, mas o envio nunca é automático."
    - "[ ] L2: Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para reunião'. O founder decide o que fazer com o sinal, não o squad."
    - "[ ] L2: Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao ha ingestao forçada — o founder controla o ritmo de captura do proprio conhecimento."
---

# Preparar Reuniões Importantes

**Task ID:** `chiefOfStaff()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Preparar Reuniões Importantes |
| **status** | `pending` |
| **responsible_executor** | CHIEF OF STAFF (CHIEF OF STAFF — O Agente de Alta Alavancagem) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker que opera como extensão operacional do founder para gestão de atenção e foco estratégico. Funções principais: (1) Preparação de reuniões — 24h antes de qualquer reunião importante, puxa contexto relevante do grafo, histórico de interações com os participantes, agenda proposta e entrega um briefing executivo de 1 página; (2) Gestão de follow-ups — monitora ClickUp e integração de email/calendário para identificar compromissos não cumpridos e itens de ação pendentes, emite lembretes priorizados; (3) Filtragem de demandas — quando outro squad ou membro do time pede input do founder, verifica primeiro se o grafo já responde (e delega ao Persona Forge) antes de escalar para o founder; (4) Síntese de agenda — gera revisão semanal de prioridades alinhando decisões pendentes com os objetivos estratégicos do grafo.

## Input

- Calendário do founder (Google Calendar / Outlook via MCP), inbox de email (Gmail via MCP), ClickUp (tarefas e projetos), Slack (mensagens marcadas como high-priority), grafo de conhecimento (para responder demandas sem interromper o founder), lista de OKRs e prioridades do trimestre

## Output

- Briefing pre-reuniao (1 pagina, Notion), digest de follow-ups pendentes (Slack, segunda-feiras 8h), relatorio de demandas filtradas (log de quantas foram respondidas pelo clone sem interromper o founder), agenda estrategica semanal com top-3 decisoes prioritarias
- Tudo como tarefas verificaveis no ClickUp

## Trigger

Execução proativa: briefings disparados 24h antes de reuniões detectadas no calendário. Digest de follow-ups toda segunda-feira 8h. Filtragem de demandas em tempo real quando outros squads consultam o founder. Relatório semanal todo domingo 18h para revisão na segunda-feira.

## Knowledge base (o que o executor consulta)

- Grafo de conhecimento (para filtragem de demandas)
- Calendário e agenda do founder
- Histórico de reuniões e follow-ups
- OKRs e prioridades estratégicas do trimestre
- Lista de stakeholders chave com histórico de interações
- Templates de briefing por tipo de reunião (1:1, board, cliente estratégico, investidor)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Calendário do founder (Google Calendar / Outlook via MCP), inbox de email (Gmail via MCP), ClickUp (tarefas e projetos)…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Briefing pre-reuniao (1 pagina, Notion), digest de follow-ups pendentes (Slack, segunda-feiras 8h), relatorio de demand…) e persistir no artefato do squad.
4. Entregar ao critic AUDITOR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Briefing pre-reuniao (1 pagina, Notion), digest de follow-ups pendentes (Slack, segunda-feiras 8h), relatorio de demandas filtradas (log de quantas foram respo…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic AUDITOR registrado
- [ ] Gate L3 respeitado: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o graf…
- [ ] Gate L3 respeitado: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, m…
- [ ] Gate L3 respeitado: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scriv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automat… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída pa… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com ano… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao h… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão do mapa de lacunas gerado no Discovery: antes de priorizar quais tópicos capturar, o founder valida se a taxonomia e as lacunas identificadas fazem sen… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic AUDITOR | BLOQUEIA entrega |

## Handoff

- **to:** WARGAME
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
