---
task: zara()
responsavel: "Zara"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de contas-alvo do ICP (tier 1/2/3), keywords de intent configuradas, thresholds de pontuação de sinal por categoria, janela de tempo de monitoramento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Signal Feed diário com contas priorizadas por score de intent, Intent Score por conta (0-100), breakdown de sinais detectados por categoria, alertas de Hot Accounts (score > 70) para ação imediata no CRM, tendências de segmento (quais setores estão mais ativos)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job de monitoramento diário automático (cron 6h); alerta de funding round detectado via webhook; Maestro solicita análise de sinais para segmento específico; revisão semanal de ICP"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vera 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3)"
    - "[ ] HITL: Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3)"
    - "[ ] HITL: Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)"
    - "[ ] HITL: Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3)"
    - "[ ] HITL: Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1)"
---

# Monitorar Sinais De Compra

**Task ID:** `zara()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Living ICP Profiler

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais De Compra |
| **status** | `pending` |
| **responsible_executor** | Zara (Zara — Signal & Intent Sensor) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora sinais de compra e demanda em tempo real para identificar quando prospects do ICP estão em janela de compra. Rastreia: funding rounds, job postings em áreas relacionadas, adoção de tecnologias complementares, menções em redes sociais, atividade em review sites (G2, Capterra), sinais de intent Bombora/6sense. Classifica urgência do sinal (Hot/Warm/Cold) e alerta o Maestro.

## Input

- Lista de contas-alvo do ICP (tier 1/2/3), keywords de intent configuradas, thresholds de pontuação de sinal por categoria, janela de tempo de monitoramento

## Output

- Signal Feed diário com contas priorizadas por score de intent, Intent Score por conta (0-100), breakdown de sinais detectados por categoria, alertas de Hot Accounts (score > 70) para ação imediata no CRM, tendências de segmento (quais setores estão mais ativos)

## Trigger

Job de monitoramento diário automático (cron 6h); alerta de funding round detectado via webhook; Maestro solicita análise de sinais para segmento específico; revisão semanal de ICP

## Knowledge base (o que o executor consulta)

- Lista de contas ICP tier 1/2/3, keywords de intent por vertical, historico de sinais anteriores para baseline de anomalia, mapeamento de stack tecnologico por segmento (Technographics)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de contas-alvo do ICP (tier 1/2/3), keywords de intent configuradas, thresholds de pontuação de sinal por categor…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Signal Feed diário com contas priorizadas por score de intent, Intent Score por conta (0-100), breakdown de sinais dete…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Signal Feed diário com contas priorizadas por score de intent, Intent Score por conta (0-100), breakdown de sinais detectados por categoria, alertas de Hot Acc…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vera 2 registrado
- [ ] Gate HITL respeitado: Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento…
- [ ] Gate HITL respeitado: Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (…
- [ ] Gate HITL respeitado: Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3) | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de integração com nova fonte de dados de enriquecimento que implica custo adicional — qualquer nova ferramenta paga requer validação financeira (L3) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Vera 2 | BLOQUEIA entrega |

## Handoff

- **to:** Nox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
