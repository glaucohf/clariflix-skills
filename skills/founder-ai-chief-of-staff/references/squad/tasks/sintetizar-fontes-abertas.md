---
task: kira()
responsavel: "Kira"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Query de pesquisa estruturada com escopo (pessoa / empresa / setor / tema) e nível de profundidade (rápido 15min / padrão 1h / profundo 4h)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Disparada por Orion ou pelo founder diretamente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Research Brief: sumário executivo (3 parágrafos), achados-chave com fonte citada, gaps de informação identificados, recomendação de ação"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Formato: Notion page + JSON estruturado para outros agentes consumirem"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Reunião de alto impacto (investor, board, deal >R$100k). Pergunta estratégica ad-hoc do founder. Alerta de competidor disparado por Intel Agent."
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

# Sintetizar Fontes Abertas

**Task ID:** `kira()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** AI Chief of Staff — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Fontes Abertas |
| **status** | `pending` |
| **responsible_executor** | Kira (Kira — Deep Research Worker) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Pesquisa profunda e paralela sobre pessoa, empresa ou tema estratégico. Especialista em síntese de fontes abertas (LinkedIn, news, filings, relatórios setoriais). Executa 3–5 buscas simultâneas em vetores diferentes (mercado, competidor, regulação, tese, financeiro) e entrega síntese com citações rastreáveis.

## Input

- Query de pesquisa estruturada com escopo (pessoa / empresa / setor / tema) e nível de profundidade (rápido 15min / padrão 1h / profundo 4h)
- Disparada por Orion ou pelo founder diretamente

## Output

- Research Brief: sumário executivo (3 parágrafos), achados-chave com fonte citada, gaps de informação identificados, recomendação de ação
- Formato: Notion page + JSON estruturado para outros agentes consumirem

## Trigger

Reunião de alto impacto (investor, board, deal >R$100k). Pergunta estratégica ad-hoc do founder. Alerta de competidor disparado por Intel Agent.

## Knowledge base (o que o executor consulta)

- Web search (Brave/Perplexity MCP)
- Fontes financeiras públicas (CVM, Crunchbase, LinkedIn)
- Arquivos internos (relatórios, propostas anteriores)
- Vector DB com corpus setorial do founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Query de pesquisa estruturada com escopo (pessoa / empresa / setor / tema) e nível de profundidade (rápido 15min / padr…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Research Brief: sumário executivo (3 parágrafos), achados-chave com fonte citada, gaps de informação identificados, rec…) e persistir no artefato do squad.
4. Entregar ao critic Skeptic; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Research Brief: sumário executivo (3 parágrafos), achados-chave com fonte citada, gaps de informação identificados, recomendação de ação
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

- **to:** Vance
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
