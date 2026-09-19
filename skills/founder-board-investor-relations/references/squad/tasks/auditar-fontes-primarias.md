---
task: vera()
responsavel: "Vera"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft do board pack/investor update em qualquer versão"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Metrics Table canônica do Rex"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Context Brief do Marlowe"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Lista de claims identificados como 'afirmações de alto risco' (valuation, market size, competitive moat, churn causation)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Draft anotado com inline citations (formato [Fonte: X, Data: Y])"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Source Manifest (JSON): mapa completo de claim → fonte → nível de evidência → data de extração"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Score de rastreabilidade por seção (0–100%)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Lista de claims pendentes de fonte para revisão do founder"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Certificado de integridade ao final (% de claims rastreáveis)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Draft de qualquer seção submetido para validação. Antes de qualquer output chegar ao Critic. Check automático antes do HITL Gate liberar o documento para revisão do founder."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Axiom antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção"
    - "[ ] HITL: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores"
    - "[ ] HITL: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%"
    - "[ ] HITL: Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa não autorizada)"
    - "[ ] HITL: Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downround) entrarem no draft final"
---

# Auditar Fontes Primárias

**Task ID:** `vera()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Board & Investor Relations — Founder Office

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Auditar Fontes Primárias |
| **status** | `pending` |
| **responsible_executor** | Vera (Vera — Provenance & Source Integrity Agent) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Garante que 100% das afirmações factuais no draft tenham fonte primária rastreável. Audita o draft seção por seção, anota cada claim com sua fonte (dado interno, pesquisa externa, estimativa do founder), classifica o nível de evidência (dado real / estimativa / benchmark / opinião) e gera o Source Manifest do ciclo. Bloqueia aprovação de qualquer seção com claim não rastreável de nível crítico.

## Input

- Draft do board pack/investor update em qualquer versão
- Metrics Table canônica do Rex
- Context Brief do Marlowe
- Lista de claims identificados como 'afirmações de alto risco' (valuation, market size, competitive moat, churn causation)

## Output

- Draft anotado com inline citations (formato [Fonte: X, Data: Y])
- Source Manifest (JSON): mapa completo de claim → fonte → nível de evidência → data de extração
- Score de rastreabilidade por seção (0–100%)
- Lista de claims pendentes de fonte para revisão do founder
- Certificado de integridade ao final (% de claims rastreáveis)

## Trigger

Draft de qualquer seção submetido para validação. Antes de qualquer output chegar ao Critic. Check automático antes do HITL Gate liberar o documento para revisão do founder.

## Knowledge base (o que o executor consulta)

- Metrics Table canônica do ciclo (output do Rex)
- Context Brief com fontes externas (output do Marlowe)
- Histórico de Source Manifests de ciclos anteriores (para rastrear se claim recorrente teve fonte mudada)
- Data room da empresa (documentos financeiros auditados, contratos relevantes)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft do board pack/investor update em qualquer versão).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Draft anotado com inline citations (formato [Fonte: X, Data: Y])) e persistir no artefato do squad.
4. Entregar ao critic Axiom; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Draft anotado com inline citations (formato [Fonte: X, Data: Y])
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Axiom registrado
- [ ] Gate HITL respeitado: Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção
- [ ] Gate HITL respeitado: Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao b…
- [ ] Gate HITL respeitado: Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90%

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do founder antes de qualquer envio externo (email, PDF, Notion share) — Gate Agent é L3 por design, nenhuma exceção | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confirmação do founder antes de comprometer qualquer guidance de valuation, projeção financeira ou tese de rodada em documento enviado ao board ou investidores | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Revisão do Source Manifest (Vera) pelo founder quando % de rastreabilidade de claims críticos estiver abaixo de 90% | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação da lista de destinatários antes de qualquer novo ciclo — founder confirma quem receberá o board pack (evita envio para investidor errado ou pessoa nã… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Validação do Founder Clone (Sage) antes de seções estratégicas sensíveis (posicionamento competitivo, resposta a perda de guidance, narrativa de churn ou downr… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação do Q&A Brief do Quincy antes do board meeting — founder confirma quais respostas está confortável em dar publicamente | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Configuração inicial do corpus do Sage — founder revisa e aprova quais comunicações passadas entram no corpus de clonagem narrativa | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Qualquer mudança de metodologia de cálculo de métrica-chave (ex: mudança de definição de ARR, churn líquido vs bruto) requer aprovação explícita antes de ser r… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Axiom | BLOQUEIA entrega |

## Handoff

- **to:** Sage
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
