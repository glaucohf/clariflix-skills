---
task: aegis()
responsavel: "Aegis"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Copy e criativos gerados pelo Vox (antes de qualquer upload para plataforma) + Plano de ação de bid/budget do Midas (antes de execução) + Brand voice guidelines do cliente + Políticas de publicidade das plataformas (Google Ads policies, Meta advertising standards) + Guardrails financeiros aprovados"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Verdict estruturado por item: APPROVED / NEEDS_REVISION / BLOCKED + Justificativa detalhada para cada item reprovado + Sugestões de correção específicas (não apenas o problema, mas a solução) + Score de conformidade (0-100) por dimensão (brand voice, compliance legal, compliance plataforma, coerência de PMF)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado obrigatoriamente antes de qualquer upload de copy/criativo para plataforma (gate de qualidade pré-publicação). Também acionado antes de execução de ações L3 do Midas para segunda verificação…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aegis 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de ROAS para escala, orçamento máximo em risco por ciclo) — sem essa aprovação o squad não opera"
    - "[ ] HITL: Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget total ou pausar campanha inteira) requer aprovação explícita via Slack/WhatsApp antes de execução pelo Midas"
    - "[ ] HITL: Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos de mensagem sem histórico) requer aprovação humana — irreversível em termos de impressão inicial"
    - "[ ] HITL: Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de threshold) requerem OK do gestor antes de ativação automática"
    - "[ ] HITL: Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com os guardrails mais recentes aprovados"
---

# Verificar Conformidade Compliance

**Task ID:** `aegis()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Conformidade Compliance |
| **status** | `pending` |
| **responsible_executor** | Aegis (Aegis — Compliance & Brand Guard) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente crítico/verificador que atua como gate de qualidade antes de qualquer publicação ou mudança de campanha. Valida que toda copy gerada pelo Vox está em conformidade com as políticas das plataformas (Google Ads, Meta), alinhada com brand voice do cliente, livre de claims enganosos ou ilegais, e coerente com o posicionamento de PMF. Também verifica se ajustes de bid/budget do Midas estão dentro dos guardrails aprovados antes da execução.

## Input

- Copy e criativos gerados pelo Vox (antes de qualquer upload para plataforma) + Plano de ação de bid/budget do Midas (antes de execução) + Brand voice guidelines do cliente + Políticas de publicidade das plataformas (Google Ads policies, Meta advertising standards) + Guardrails financeiros aprovados

## Output

- Verdict estruturado por item: APPROVED / NEEDS_REVISION / BLOCKED + Justificativa detalhada para cada item reprovado + Sugestões de correção específicas (não apenas o problema, mas a solução) + Score de conformidade (0-100) por dimensão (brand voice, compliance legal, compliance plataforma, coerência de PMF)

## Trigger

Acionado obrigatoriamente antes de qualquer upload de copy/criativo para plataforma (gate de qualidade pré-publicação). Também acionado antes de execução de ações L3 do Midas para segunda verificação de guardrails

## Knowledge base (o que o executor consulta)

- Brand voice guidelines completos (tom, vocabulário proibido, claims aprovados e não aprovados), Políticas vigentes de publicidade Google Ads e Meta Ads (atualizado mensalmente), Guardrails financeiros aprovados pelo cliente, Histórico de rejeições de anúncios por plataforma (aprendizado de erros passados), Legislação aplicável (LGPD, CONAR, regulações setoriais do cliente)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Copy e criativos gerados pelo Vox (antes de qualquer upload para plataforma) + Plano de ação de bid/budget do Midas (an…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Verdict estruturado por item: APPROVED / NEEDS_REVISION / BLOCKED + Justificativa detalhada para cada item reprovado +…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Verdict estruturado por item: APPROVED / NEEDS_REVISION / BLOCKED + Justificativa detalhada para cada item reprovado + Sugestões de correção específicas (não a…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aegis 2 registrado
- [ ] Gate HITL respeitado: Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA…
- [ ] Gate HITL respeitado: Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: move…
- [ ] Gate HITL respeitado: Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos forma…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação inicial de Guardrails Financeiros: cliente define e assina as bandas de autonomia (% máximo de realocação por ciclo, teto de CPA aceitável, floor de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Gate L3 — Realocação acima da banda: qualquer realocação de budget ou mudança de bid strategy que exceda o threshold pre-aprovado (ex: mover > 20% do budget to… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Gate L3 — Lançamento de novos criativos: upload de novos anúncios para plataforma (não apenas rotação de ativos existentes, mas novos formatos ou novos ângulos… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação semanal do relatório de inteligência do Sentinel: recomendações proativas de escala para próxima semana (aumento de orçamento semanal acima de thresh… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Revisão mensal de thresholds e guardrails: reunião obrigatória de 30min para calibrar bandas com base em performance real do mês anterior — o squad opera com o… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Onboarding de nova plataforma ou canal: qualquer expansão para nova plataforma de mídia (ex: adicionar TikTok Ads, Pinterest Ads, CTV) requer aprovação e confi… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Bloqueio por anomalia crítica: se Argos detectar anomalia CRITICAL (ex: ROAS caiu > 50% em 1h ou spend disparou 300% acima do target), o squad pausa todas as a… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Aegis 2 | BLOQUEIA entrega |

## Handoff

- **to:** Aegis 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
