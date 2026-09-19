---
task: scout()
responsavel: "SCOUT"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Nome da empresa, domínio, CNPJ (opcional), setor declarado ou inferido, nome do contato principal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON estruturado com: dados firmográficos, tecnologias detectadas, timeline de eventos recentes (últimos 90 dias), estimativa de maturidade digital, sinais de compra (ex: contratação de cargo relacionado ao produto), fontes com URLs e datas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo NEXUS após validação de que não existe dossiê recente em cache. Também acionado manualmente pelo vendedor via comando no ClickUp ou chat."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM de produção"
    - "[ ] L3: Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio automático sem leitura humana"
    - "[ ] L2: Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta o que não se aplica"
    - "[ ] L1: Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão parcial ou aguardar correção"
    - "[ ] L1: Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes de qualquer ação"
---

# Investigar Empresa Completa

**Task ID:** `scout()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Inteligência de Conta e Battlecards

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Investigar Empresa Completa |
| **status** | `pending` |
| **responsible_executor** | SCOUT (SCOUT — O Investigador de Empresa) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em enriquecimento e pesquisa de conta. Varre fontes públicas e APIs de dados para construir o perfil completo da empresa: tamanho, receita estimada, stack tecnológica, notícias recentes (funding, expansão, demissões, contratações estratégicas), presença digital, clientes conhecidos, casos de uso publicados e momento atual do negócio.

## Input

- Nome da empresa, domínio, CNPJ (opcional), setor declarado ou inferido, nome do contato principal

## Output

- JSON estruturado com: dados firmográficos, tecnologias detectadas, timeline de eventos recentes (últimos 90 dias), estimativa de maturidade digital, sinais de compra (ex: contratação de cargo relacionado ao produto), fontes com URLs e datas

## Trigger

Disparo pelo NEXUS após validação de que não existe dossiê recente em cache. Também acionado manualmente pelo vendedor via comando no ClickUp ou chat.

## Knowledge base (o que o executor consulta)

- APIs: Apollo.io (firmografia e contatos), Clearbit Enrichment, LinkedIn Company API, Google News, Common Crawl, BuiltWith (stack tecnologica)
- Contexto interno: historico de contas similares no CRM, playbooks de setor, ICP (Ideal Customer Profile) documentado pelo cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Nome da empresa, domínio, CNPJ (opcional), setor declarado ou inferido, nome do contato principal).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON estruturado com: dados firmográficos, tecnologias detectadas, timeline de eventos recentes (últimos 90 dias), esti…) e persistir no artefato do squad.
4. Entregar ao critic SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON estruturado com: dados firmográficos, tecnologias detectadas, timeline de eventos recentes (últimos 90 dias), estimativa de maturidade digital, sinais de…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic SENTINEL registrado
- [ ] Gate L3 respeitado: Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistênci…
- [ ] Gate L3 respeitado: Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do…
- [ ] Gate L2 respeitado: Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Atualização de stage e dados críticos no CRM pelo MEMÓRIA: vendedor confirma resultado da reunião e valida informações antes de persistência permanente no CRM… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Qualquer ação de outreach gerada como sugestão pelo dossiê (ex: envio de email de follow-up personalizado): vendedor aprova texto antes do envio, nunca envio a… | BLOQUEIA até decisão humana |
| VETO-003 | L2 — Revisão do dossiê completo pelo vendedor antes da reunião: o artefato é uma ferramenta de preparo, não um script — o vendedor valida o que vai usar e descarta… | BLOQUEIA até decisão humana |
| VETO-004 | L1 — Quando SENTINEL emite REJEITADO: NEXUS pausa pipeline e notifica o vendedor sobre o gap de qualidade, permitindo que ele decida se quer prosseguir com versão p… | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Identificação de stakeholders de alto risco (ex: prospect e ex-funcionário de empresa cliente com conflito): IRIS sinaliza e vendedor decide como abordar antes… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** IRIS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
