---
task: helios()
responsavel: "Helios"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Timing Profiles de todos os leads ativos (Sirius output)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Channel Health Scores por canal (Pulsar output)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Sequencias de outreach ativas com toques planejados (Vega input)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "configuracao do experimento A/B atual (grupos tratamento e controle, metricas de sucesso, tamanho minimo de amostra para significancia estatistica)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Schedule otimizado por lead/toque (JSON: {lead_id, toque_id, canal_recomendado, data_hora_envio_otima, probabilidade_abertura_estimada, espacamento_desde_ultimo_toque_horas, confianca_modelo})"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Modelo de producao atualizado com metricas de performance"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "A/B Test Report semanal (uplift observado vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "baseline, significancia estatistica, recomendacao de promover/manter/reverter modelo candidato)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job diario de geracao de schedule para proximas 48h (executado 22h D-1); atualizacao de Timing Profile de lead com toque agendado nas proximas 4h (recalculo imediato); Kronos solicita agendamento de…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Aura 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e sequencia sao foco prioritario antes de iniciar o modelo (L3, gate de entrada)"
    - "[ ] HITL: Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualquer envio em producao (L3, gate de seguranca antes de go-live)"
    - "[ ] HITL: Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente do nivel de automacao configurado (L3, por volume e irreversibilidade)"
    - "[ ] HITL: Quando Channel Health Score de qualquer canal cai abaixo de 50 — Aura bloqueia o canal e Kronos escala para decisao humana sobre pausa, reducao de frequencia ou investigacao de causa raiz (L3, saude de canal critica)"
    - "[ ] HITL: Promocao de modelo candidato de Helios para producao — uplift confirmado no A/B test e condição necessaria mas nao suficiente; Head de Aquisicao aprova a troca de modelo que afeta toda a base (L3, decisao de alto impacto)"
---

# Construir Modelo Preditivo Timing

**Task ID:** `helios()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Intelligent Timing Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Construir Modelo Preditivo Timing |
| **status** | `pending` |
| **responsible_executor** | Helios (Helios — Timing Model Builder) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

O cerebro quantitativo do squad: constroi e atualiza o modelo preditivo de timing otimo por usuario. Recebe os Timing Profiles individuais de Sirius e os Channel Health Scores de Pulsar e roda um modelo de otimizacao para determinar, para cada lead e cada toque planejado: (1) melhor canal, (2) melhor janela de horario, (3) melhor dia da semana, (4) espacamento otimo em relacao ao toque anterior. Usa abordagem bayesiana: combina o prior do segmento com o historico individual, ponderando pela confianca do modelo (novos leads tem mais peso no prior; leads com 20+ eventos tem modelo quase 100% individual). Mantém dois modelos em paralelo: o modelo de producao (usado para agendamento) e o modelo de teste (candidato a upgrade), promovendo o candidato quando uplift confirmado em A/B >= 10%.

## Input

- Timing Profiles de todos os leads ativos (Sirius output)
- Channel Health Scores por canal (Pulsar output)
- Sequencias de outreach ativas com toques planejados (Vega input)
- configuracao do experimento A/B atual (grupos tratamento e controle, metricas de sucesso, tamanho minimo de amostra para significancia estatistica)

## Output

- Schedule otimizado por lead/toque (JSON: {lead_id, toque_id, canal_recomendado, data_hora_envio_otima, probabilidade_abertura_estimada, espacamento_desde_ultimo_toque_horas, confianca_modelo})
- Modelo de producao atualizado com metricas de performance
- A/B Test Report semanal (uplift observado vs
- baseline, significancia estatistica, recomendacao de promover/manter/reverter modelo candidato)

## Trigger

Job diario de geracao de schedule para proximas 48h (executado 22h D-1); atualizacao de Timing Profile de lead com toque agendado nas proximas 4h (recalculo imediato); Kronos solicita agendamento de campanha nova; resultado de A/B test acumula amostra minima (trigger de avaliacao de modelo candidato)

## Knowledge base (o que o executor consulta)

- Timing Profiles por lead (Sirius), Channel Health Scores historicos (Pulsar), Modelo de producao atual com seus hiperparametros e metricas de performance, Historico de A/B tests com resultados (para nao repetir experimentos fracassados), Calendario de feriados e eventos setoriais (para ajuste sazonal do modelo)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Timing Profiles de todos os leads ativos (Sirius output)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Schedule otimizado por lead/toque (JSON: {lead_id, toque_id, canal_recomendado, data_hora_envio_otima, probabilidade_ab…) e persistir no artefato do squad.
4. Entregar ao critic Aura 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Schedule otimizado por lead/toque (JSON: {lead_id, toque_id, canal_recomendado, data_hora_envio_otima, probabilidade_abertura_estimada, espacamento_desde_ultim…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Aura 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e s…
- [ ] Gate HITL respeitado: Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualq…
- [ ] Gate HITL respeitado: Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Engagement Baseline Report ao final do Discovery — CMO/Head de Aquisicao valida os dados de baseline e confirma qual canal e sequencia sao foco pr… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Ativacao da Sequencia Otimizada v1 redesenhada por Vega — time de SDR/Outreach revisa e aprova a nova distribuicao de toques antes de qualquer envio em produca… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Qualquer campanha com audiencia > 500 contatos ou que envolva budget de ads — Nexus requer aprovacao manual antes de executar, independente do nivel de automac… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Quando Channel Health Score de qualquer canal cai abaixo de 50 — Aura bloqueia o canal e Kronos escala para decisao humana sobre pausa, reducao de frequencia o… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Promocao de modelo candidato de Helios para producao — uplift confirmado no A/B test e condição necessaria mas nao suficiente; Head de Aquisicao aprova a troca… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Quando Aura detecta violacao de compliance legal (opt-out nao respeitado, envio fora de horario legal, campo LGPD violado) — independente de qualquer autonomia… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao trimestral de thresholds de timing e limites de frequencia — calibracao dos parametros do modelo com Sales Lead e CMO para alinhar com estrategia comer… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Aura 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vega
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
