---
task: vera()
responsavel: "Vera"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Corpus normalizado do Parallax + Research Brief original com sub-questões + thresholds de qualidade configurados (ex: max 10% claims Unverified em briefs estratégicos críticos)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Corpus auditado com anotações inline de confiança"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatório de verificação: { total_claims, verified_high, verified_medium, verified_low, unverified, contradictions_found, red_team_findings }"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "GO/NO-GO para síntese"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Lista de gaps críticos que requerem pesquisa adicional"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado automaticamente após Parallax concluir normalização. Pode ser re-ativado pelo Orion se síntese gerar novo claim sem fonte. Ativado manualmente pelo founder via comando '/verify [claim]' para…"
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

# Verificar Contradições Claims

**Task ID:** `vera()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Deep Research Estratégico — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Contradições Claims |
| **status** | `pending` |
| **responsible_executor** | Vera (Vera — O Crítico Adversarial) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente critic/verifier responsável por verificação adversarial do corpus antes da síntese final. Executa: (1) verificação cruzada de claims entre workers para identificar contradições, (2) marcação de claims sem fonte suficiente como 'Unverified', (3) detecção de possível alucinação por inconsistência lógica ou ausência de evidência, (4) classificação de confiança por claim (High/Medium/Low/Unverified), (5) red-team: tenta falsificar as 3 principais conclusões com evidência contrária. Se taxa de claims Unverified > 20% ou se contradição crítica detectada, devolve para retrabalho dos workers antes de liberar para síntese.

## Input

- Corpus normalizado do Parallax + Research Brief original com sub-questões + thresholds de qualidade configurados (ex: max 10% claims Unverified em briefs estratégicos críticos)

## Output

- Corpus auditado com anotações inline de confiança
- Relatório de verificação: { total_claims, verified_high, verified_medium, verified_low, unverified, contradictions_found, red_team_findings }
- GO/NO-GO para síntese
- Lista de gaps críticos que requerem pesquisa adicional

## Trigger

Ativado automaticamente após Parallax concluir normalização. Pode ser re-ativado pelo Orion se síntese gerar novo claim sem fonte. Ativado manualmente pelo founder via comando '/verify [claim]' para fact-check pontual.

## Knowledge base (o que o executor consulta)

- Corpus normalizado da sessão
- Histórico de briefs anteriores (para identificar claims recorrentes que já foram validados)
- Heurísticas de detecção de alucinação (lista de padrões comuns)
- Referências de autoridade para cross-check (ex: para claims financeiros, checar contra fonte primária de balanço)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Corpus normalizado do Parallax + Research Brief original com sub-questões + thresholds de qualidade configurados (ex: m…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Corpus auditado com anotações inline de confiança) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Corpus auditado com anotações inline de confiança
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

- **to:** Sage
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
