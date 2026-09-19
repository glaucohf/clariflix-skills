---
task: sage()
responsavel: "Sage"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Brief Estratégico estruturado e verificado do Orion + corpus de treinamento do founder (textos, decisões passadas, frameworks preferidos) + instrução de formato desejado (denso/executivo/narrativo/tabular)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Brief Estratégico no tom e estilo do founder"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Seção 'O que eu (founder) faria com isso' com 2-3 reflexões estratégicas em primeira pessoa"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Versão curta (1-pager executivo) e versão longa (análise completa)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Pronto para compartilhar com board, investidores ou time"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Orion após Vera dar GO na síntese. Ativação opcional — pode ser desligado se founder preferir brief neutro. Ativado diretamente pelo founder via '/rewrite [estilo]' para reprocessar brief…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vera 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicação financeira direta — Orion apresenta o Research Brief ao founder para aprovação antes de disparar workers. Custo estimado de tokens também é apresentado."
    - "[ ] HITL: REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciência do risco e confirmar se deseja prosseguir antes de receber recomendações estratégicas naquele domínio. Recomendação de consultor jurídico parceiro é incluída."
    - "[ ] HITL: CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief é retido e o founder recebe notificação com lista dos claims não verificados, podendo aprovar release com ressalvas ou solicitar re-pesquisa."
    - "[ ] HITL: COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado como 'obtained via unclear method' é automaticamente removido e o founder é notificado. Toda coleta passa por whitelist de fontes permitidas."
    - "[ ] HITL: FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder deve revisar e aprovar. Sage pode enviar internamente (Notion, Slack privado) sem aprovação, mas envio externo é sempre L3."
---

# Humanizar Briefs

**Task ID:** `sage()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Humanizar Briefs |
| **status** | `pending` |
| **responsible_executor** | Sage (Sage — O Clone do Founder) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de reescrita e síntese no tom, linguagem, frameworks mentais e estilo decisório do founder. Recebe o brief verificado do Orion e o humaniza: reescreve no vocabulário do founder, aplica os frameworks que o founder usa habitualmente (ex: Jobs-to-be-Done, 3 Horizontes, JTBD, princípios do founder), adiciona comentários estratégicos no estilo do founder, e formata o output como o founder prefere consumir informação (ex: bullet denso, narrativa, tabela comparativa). Treinado no corpus de textos, decisões e comunicações do founder.

## Input

- Brief Estratégico estruturado e verificado do Orion + corpus de treinamento do founder (textos, decisões passadas, frameworks preferidos) + instrução de formato desejado (denso/executivo/narrativo/tabular)

## Output

- Brief Estratégico no tom e estilo do founder
- Seção 'O que eu (founder) faria com isso' com 2-3 reflexões estratégicas em primeira pessoa
- Versão curta (1-pager executivo) e versão longa (análise completa)
- Pronto para compartilhar com board, investidores ou time

## Trigger

Ativado por Orion após Vera dar GO na síntese. Ativação opcional — pode ser desligado se founder preferir brief neutro. Ativado diretamente pelo founder via '/rewrite [estilo]' para reprocessar brief existente.

## Knowledge base (o que o executor consulta)

- Corpus do founder: textos públicos (LinkedIn, artigos, apresentações), decisões estratégicas documentadas, frameworks favoritos, vocabulário característico, tom de comunicação (indexados no Vector DB privado)
- Histórico de briefs anteriores aprovados pelo founder
- Preferências de formato configuradas no perfil do founder

## Action Items

1. Confirmar o gatilho e carregar a entrada (Brief Estratégico estruturado e verificado do Orion + corpus de treinamento do founder (textos, decisões passadas, fram…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Brief Estratégico no tom e estilo do founder) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Brief Estratégico no tom e estilo do founder
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vera 2 registrado
- [ ] Gate HITL respeitado: INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer op…
- [ ] Gate HITL respeitado: REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder…
- [ ] Gate HITL respeitado: CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE (L3): Antes de iniciar pesquisa que envolva análise de empresas específicas para M&A, due diligence de parceiros ou qualquer operação com implicaçã… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — REGULATORY FLAG (L1→L3): Quando Lex classifica risco regulatório como Alto ou Crítico — Vera bloqueia o brief e aciona HITL gate. O founder deve confirmar ciên… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — CLAIM UNVERIFIED THRESHOLD (L2→L3): Se após verificação de Vera a taxa de claims Unverified superar 15% em brief classificado como 'decisão crítica' — o brief… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — COMPETITOR INTELLIGENCE ETHICS (L3): Blade nunca coleta dados via técnicas de scraping agressivo ou acesso não autorizado. Qualquer dado de concorrente marcado… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — FOUNDER CLONE REWRITE (L1): Antes de Sage publicar ou enviar externamente um brief no tom do founder (ex: draft de memo para board ou investidores) — o founder… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — COST THRESHOLD (L3): Se estimativa de custo de tokens de uma pesquisa superar limite configurado (default: U$5 por brief) — Orion pausa e solicita aprovação ex… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Vera 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vera 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
