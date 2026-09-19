---
task: vox()
responsavel: "Vox"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Solicitação estruturada do Prism (formato, ângulo, audiência, benchmark) + ICP personas do cliente (dores, linguagem, objeções) + Brand voice guidelines + Histórico de copy top performers (hooks validados, CTAs de alta conversão) + Informações de PMF e posicionamento (Research do cliente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de copy estruturado (JSON): variacoes de headline (5-10), primary text (3-5 extensoes), CTA options (3-5), angulo de mensagem principal, segmento de audiencia alvo, justificativa de hook baseada em ICP, metadados para tracking de variacao em plataforma"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Briefs de UGC/video quando solicitado (formato, duracao, roteiro de hook, CTA falado)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Prism quando banco de criativos cai abaixo do threshold ou quando novo ciclo de testes é solicitado pelo orquestrador. Também acionado manualmente via ClickUp task pelo cliente ou gesto…"
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

# Gerar Copy Para Ads

**Task ID:** `vox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Copy Para Ads |
| **status** | `pending` |
| **responsible_executor** | Vox (Vox — Copy & Creative Briefêr) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de geração de copy para ads e briefing de novos criativos. Produz 5-15 variações de headline, primary text e CTA por ciclo, estruturadas para teste A/B sistemático. Gera briefs detalhados para produção de UGC/video quando o banco de ativos precisa de reposição. Valida que toda copy gerada está alinhada com brand voice, compliance e posicionamento de PMF antes de enviar ao Critico.

## Input

- Solicitação estruturada do Prism (formato, ângulo, audiência, benchmark) + ICP personas do cliente (dores, linguagem, objeções) + Brand voice guidelines + Histórico de copy top performers (hooks validados, CTAs de alta conversão) + Informações de PMF e posicionamento (Research do cliente)

## Output

- Pacote de copy estruturado (JSON): variacoes de headline (5-10), primary text (3-5 extensoes), CTA options (3-5), angulo de mensagem principal, segmento de audiencia alvo, justificativa de hook baseada em ICP, metadados para tracking de variacao em plataforma
- Briefs de UGC/video quando solicitado (formato, duracao, roteiro de hook, CTA falado)

## Trigger

Acionado pelo Prism quando banco de criativos cai abaixo do threshold ou quando novo ciclo de testes é solicitado pelo orquestrador. Também acionado manualmente via ClickUp task pelo cliente ou gestor de mídia

## Knowledge base (o que o executor consulta)

- ICP personas detalhadas (dores, linguagem nativa, objeções comuns, momentos de decisão), Brand voice guidelines do cliente, Biblioteca de hooks validados por ROAS histórico, Frameworks de copy (AIDA, PAS, Before-After-Bridge), Políticas de compliance por plataforma (Google Ads policies, Meta advertising standards), Posicionamento de PMF e diferenciais competitivos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Solicitação estruturada do Prism (formato, ângulo, audiência, benchmark) + ICP personas do cliente (dores, linguagem, o…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de copy estruturado (JSON): variacoes de headline (5-10), primary text (3-5 extensoes), CTA options (3-5), angul…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de copy estruturado (JSON): variacoes de headline (5-10), primary text (3-5 extensoes), CTA options (3-5), angulo de mensagem principal, segmento de aud…
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

- **to:** Atlas
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
