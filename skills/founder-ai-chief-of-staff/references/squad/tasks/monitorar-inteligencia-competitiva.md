---
task: intel()
responsavel: "Intel"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de concorrentes e palavras-chave monitoradas (configuradas pelo founder)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Feeds de news, LinkedIn, Twitter/X, blogs setoriais, Product Hunt, G2"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Frequência: scan diário às 7h, alerta imediato para eventos críticos"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Daily intel digest (formato Notion/Slack): 3–5 sinais relevantes do dia com fonte e impacto estimado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alerta urgente para eventos críticos com recomendação de resposta (contra-jogada)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Input para Briefing Agent quando interlocutor é de empresa monitorada"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Schedule diário (7h). Keyword hit em fonte monitorada. Menção da empresa do founder em fonte externa. Founder solicita análise de competidor específico."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Skeptic antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design"
    - "[ ] HITL: Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas)"
    - "[ ] HITL: Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado"
    - "[ ] HITL: Aprovação de escalation quando follow-up crítico está atrasado e envolve terceiros externos"
    - "[ ] HITL: Validação do Founder Clone Agent antes de qualquer resposta ser enviada em nome do founder"
---

# Monitorar Inteligência Competitiva

**Task ID:** `intel()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI Chief of Staff — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Inteligência Competitiva |
| **status** | `pending` |
| **responsible_executor** | Intel (Intel — Competitive Intelligence Monitor) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora concorrentes, setor e sinais de mercado 24/7. Detecta mudanças relevantes (novo produto, pricing, contratação-chave, funding, press release) e gera alerta com contra-jogada sugerida. Alimenta o contexto estratégico de Orion com inteligência competitiva contínua.

## Input

- Lista de concorrentes e palavras-chave monitoradas (configuradas pelo founder)
- Feeds de news, LinkedIn, Twitter/X, blogs setoriais, Product Hunt, G2
- Frequência: scan diário às 7h, alerta imediato para eventos críticos

## Output

- Daily intel digest (formato Notion/Slack): 3–5 sinais relevantes do dia com fonte e impacto estimado
- Alerta urgente para eventos críticos com recomendação de resposta (contra-jogada)
- Input para Briefing Agent quando interlocutor é de empresa monitorada

## Trigger

Schedule diário (7h). Keyword hit em fonte monitorada. Menção da empresa do founder em fonte externa. Founder solicita análise de competidor específico.

## Knowledge base (o que o executor consulta)

- Lista de competidores e temas monitorados (config)
- Histórico de movimentos dos competidores
- Feeds RSS, news APIs, LinkedIn Alerts
- Dados de pricing públicos e páginas de produto
- Vector DB com histórico de inteligência gerada

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de concorrentes e palavras-chave monitoradas (configuradas pelo founder)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Daily intel digest (formato Notion/Slack): 3–5 sinais relevantes do dia com fonte e impacto estimado) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Daily intel digest (formato Notion/Slack): 3–5 sinais relevantes do dia com fonte e impacto estimado
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Skeptic registrado
- [ ] Gate HITL respeitado: Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design
- [ ] Gate HITL respeitado: Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas)
- [ ] Gate HITL respeitado: Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder antes de qualquer envio externo (email, memo, board pack) — Memo Agent é L3 por design | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação antes de criar compromissos no calendário do founder (bloqueio de foco por Atlas) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Meeting Brief para reuniões de alto valor (deals >R$200k, board, investor) antes de ser considerado finalizado | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação de escalation quando follow-up crítico está atrasado e envolve terceiros externos | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Founder Clone Agent antes de qualquer resposta ser enviada em nome do founder | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Configuração inicial do corpus do Sage (founder revisa e aprova quais comunicações entram no corpus de clonagem) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Skeptic | BLOQUEIA entrega |

## Handoff

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
