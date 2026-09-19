---
task: eco()
responsavel: "Eco"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Scorecard consolidado + Red Flag Register + Tese de Aquisição rascunho (output do Nexus) + corpus de decisões do founder (histórico de memos, emails de M&A, teses passadas gravadas no knowledge base)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Investment Memo personalizado (PDF + Markdown): Executive Summary (meia página), Contexto do Target, Financials & Valuation, Red Flags com plano de mitigação, Tese de Aquisição, Recomendação (Go/Conditional Go/No-Go) com justificativa, Próximos Passos"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Tom: voz do founder, frameworks dele, nível de assertividade dele"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Nexus após consolidação dos 5 sub-relatórios e validação pelo Critic (Columbo). Último agente ativado antes do HITL Gate final."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Columbo 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complementa com dados adicionais (especialmente se completude < 60). Criticidade: ALTA — avançar com dados incompletos invalida todo o pipeline."
    - "[ ] HITL: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFIED/DISPUTED para decisão: aceitar o risco e prosseguir, solicitar pesquisa adicional (re-ativa workers específicos), ou cancelar a triagem do target."
    - "[ ] HITL: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20% do valuation estimado, irregularidade fiscal grave) pausa o pipeline e exige confirmação do founder antes de prosseguir. Pode levar ao cancelamento imediato da triagem."
    - "[ ] HITL: HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilhamento com advisors, bancos, co-investidores ou o próprio target. Ações irreversíveis (envio externo) sempre requerem aprovação humana explícita."
    - "[ ] HITL: HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados pontos. Eco re-executa com instruções específicas. Não é irreversível, mas é um checkpoint de qualidade importante."
---

# Reescrever Tese

**Task ID:** `eco()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Due Diligence / M&A Screening

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Reescrever Tese |
| **status** | `pending` |
| **responsible_executor** | Eco (Eco — O Clône Estratégico do Founder) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de Sintese e Personalizacao. Reescreve o Investment Memo e a Tese de Aquisicao na voz, tom e frameworks de decisao especificos do founder. Usa o corpus de decisoes passadas do founder (como ele raciocionava em M&As anteriores, seus criterios de go/no-go, suas heuristicas), para que o memo leia como se ele mesmo tivesse escrito — nao como output generativo generico. Tambem adapta o nivel de detalhe conforme o perfil do leitor (board vs advisors vs equipe interna).

## Input

- Scorecard consolidado + Red Flag Register + Tese de Aquisição rascunho (output do Nexus) + corpus de decisões do founder (histórico de memos, emails de M&A, teses passadas gravadas no knowledge base)

## Output

- Investment Memo personalizado (PDF + Markdown): Executive Summary (meia página), Contexto do Target, Financials & Valuation, Red Flags com plano de mitigação, Tese de Aquisição, Recomendação (Go/Conditional Go/No-Go) com justificativa, Próximos Passos
- Tom: voz do founder, frameworks dele, nível de assertividade dele

## Trigger

Ativado pelo Nexus após consolidação dos 5 sub-relatórios e validação pelo Critic (Columbo). Último agente ativado antes do HITL Gate final.

## Knowledge base (o que o executor consulta)

- Corpus do founder: memos de M&A anteriores, emails de decisão estratégica, teses de investimento passadas, frameworks de decisão documentados (ex: critérios de valuation, thresholds de red flag, linguagem de recomendação)
- Armazenado em Vector DB do squad
- Atualizado a cada novo memo aprovado pelo founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Scorecard consolidado + Red Flag Register + Tese de Aquisição rascunho (output do Nexus) + corpus de decisões do founde…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Investment Memo personalizado (PDF + Markdown): Executive Summary (meia página), Contexto do Target, Financials & Valua…) e persistir no artefato do squad.
4. Entregar ao critic Columbo 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Investment Memo personalizado (PDF + Markdown): Executive Summary (meia página), Contexto do Target, Financials & Valuation, Red Flags com plano de mitigação,…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Columbo 2 registrado
- [ ] Gate HITL respeitado: HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude…
- [ ] Gate HITL respeitado: HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a list…
- [ ] Gate HITL respeitado: HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passiv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL Gate L3 — Aprovação do Target Profile v0: Antes de avançar para o Deep Dive, o founder recebe o Target Profile com score de completude e aprova ou complem… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL Gate L3 — Columbo Score < 75: Se o Critic retorna confiança geral abaixo de 75, o Nexus pausa o pipeline e apresenta ao founder a lista de claims UNVERIFI… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL Gate L3 — Red Flag Critical Detectado: Qualquer red flag classificado como 'Critical' (ex: ação penal criminal contra fundador, passivo trabalhista > 20%… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL Gate L3 — Aprovação do Investment Memo para envio externo: O memo personalizado pelo Eco e entregue ao founder para revisão antes de qualquer compartilham… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL Gate L2 — Ajuste de Tom/Voz do Memo: O founder pode solicitar reescrita do memo pelo Eco com ajustes de tom, nível de detalhe ou ênfase em determinados po… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL Gate L1 — Configuração Inicial do Target: O founder define a intenção estratégica (por que este target, qual a tese inicial, quais setores/mercados são re… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Columbo 2 | BLOQUEIA entrega |

## Handoff

- **to:** Columbo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
