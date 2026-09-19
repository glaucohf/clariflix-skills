---
task: prism()
responsavel: "Prism"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Score de criativo por ativo (CTR, frequência, hook rate, conversion rate, spend acumulado) + Banco de criativos disponíveis (status: ativo/em_standby/fatigado/arquivado) + Thresholds de fadiga configurados (frequência máxima, CTR decay percentual, dias mínimos de veiculação) + Estrutura de ad sets por campanha"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Plano de rotação executado (quais criativos foram pausados/ativados, motivo, timestamp), Score atualizado do banco de criativos, Solicitação estruturada de novos criativos para o Vox (brief com formato, ângulo de mensagem, audiência-alvo, benchmark de criativo de referência), Relatório de performance comparada (antes/depois da rotação)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo relatório de fadiga do Argos (creative_fatigue anomalia). Também executa varredura proativa diária às 06h para identificar criativos com tendência de fadiga nas próximas 24-48h"
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

# Rotacionar Criativos

**Task ID:** `prism()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Paid Media Autopilot

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Rotacionar Criativos |
| **status** | `pending` |
| **responsible_executor** | Prism (Prism — Creative Rotation Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente especialista em rotação e teste de criativos. Monitora o score de cada criativo ativo (CTR, hook rate, thumb-stop rate, conversion rate por criativo), detecta fadiga antecipada (antes do colapso de CTR), seleciona o próximo criativo do banco de ativos para substituição, executa a troca via API (pausa o fatigado, ativa o substituto), e dispara solicitação de novos criativos ao Vox quando o banco de ativos cai abaixo do threshold de cobertura.

## Input

- Score de criativo por ativo (CTR, frequência, hook rate, conversion rate, spend acumulado) + Banco de criativos disponíveis (status: ativo/em_standby/fatigado/arquivado) + Thresholds de fadiga configurados (frequência máxima, CTR decay percentual, dias mínimos de veiculação) + Estrutura de ad sets por campanha

## Output

- Plano de rotação executado (quais criativos foram pausados/ativados, motivo, timestamp), Score atualizado do banco de criativos, Solicitação estruturada de novos criativos para o Vox (brief com formato, ângulo de mensagem, audiência-alvo, benchmark de criativo de referência), Relatório de performance comparada (antes/depois da rotação)

## Trigger

Acionado pelo relatório de fadiga do Argos (creative_fatigue anomalia). Também executa varredura proativa diária às 06h para identificar criativos com tendência de fadiga nas próximas 24-48h

## Knowledge base (o que o executor consulta)

- Catálogo completo de criativos com histórico de performance, Regras de frequência máxima por formato e plataforma, Playbook de ângulos de mensagem aprovados pelo cliente, ICP personas e seus hooks de conversão historicamente validados, Biblioteca de referências de criativos top performers

## Action Items

1. Confirmar o gatilho e carregar a entrada (Score de criativo por ativo (CTR, frequência, hook rate, conversion rate, spend acumulado) + Banco de criativos disponí…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Plano de rotação executado (quais criativos foram pausados/ativados, motivo, timestamp), Score atualizado do banco de c…) e persistir no artefato do squad.
4. Entregar ao critic Aegis 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Plano de rotação executado (quais criativos foram pausados/ativados, motivo, timestamp), Score atualizado do banco de criativos, Solicitação estruturada de nov…
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

- **to:** Vox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
