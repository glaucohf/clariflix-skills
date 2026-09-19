---
task: pulsar()
responsavel: "Pulsar"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Metricas agregadas de envio por canal e por lista (open rate, click rate, reply rate, unsubscribe rate, spam report rate, bounce rate) com granularidade semanal"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "configuracao de thresholds de fadiga por canal (defaults: email unsubscribe > 0.5%, spam report > 0.1%)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "historico de 12 semanas para calculo de tendencia"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Channel Health Score semanal por canal (0-100 com breakdown de sub-metricas)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Fatigue Alert quando threshold e violado (severidade: warning/critical/emergency)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Canal Rebalancing Recommendation (se email esta saturado, sugerir shift para LinkedIn ou reducao de frequencia com dados de suporte)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Fadiga por posicao na sequencia (qual toque 1, 2, 3, 4 tem o maior drop de engajamento"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "detecta onde a sequencia perde o usuario)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job diario de calculo de Channel Health Score (6h); spike de unsubscribe ou spam report > 2x baseline detectado em tempo real (webhook); Kronos solicita analise antes de ativar campanha nova em um ca…"
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

# Monitorar Saúde De Canal

**Task ID:** `pulsar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Intelligent Timing Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Saúde De Canal |
| **status** | `pending` |
| **responsible_executor** | Pulsar (Pulsar — Channel & Fatigue Analyst) |
| **execution_type** | `Agent` |
| **input** | 3 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Especialista em saude de canal e deteccao de fadiga. Enquanto Sirius olha para o individuo, Pulsar olha para o canal: monitora metricas agregadas de performance e fadiga por canal (email, LinkedIn, WhatsApp, SMS) e por lista/segmento. Detecta sinais precoces de fadiga antes que virem problema: incremento de unsubscribes, queda progressiva de open rate em sequencias, aumento de spam reports, queda de reply rate em toques subsequentes da mesma sequencia. Calcula o Channel Health Score (0-100) por canal por semana. Quando Channel Health Score cai abaixo de 70, emite alerta para Kronos rebalancear a distribuicao de toques. Quando cai abaixo de 50, eleva para HITL L3 para decisao humana sobre pausa de canal.

## Input

- Metricas agregadas de envio por canal e por lista (open rate, click rate, reply rate, unsubscribe rate, spam report rate, bounce rate) com granularidade semanal
- configuracao de thresholds de fadiga por canal (defaults: email unsubscribe > 0.5%, spam report > 0.1%)
- historico de 12 semanas para calculo de tendencia

## Output

- Channel Health Score semanal por canal (0-100 com breakdown de sub-metricas)
- Fatigue Alert quando threshold e violado (severidade: warning/critical/emergency)
- Canal Rebalancing Recommendation (se email esta saturado, sugerir shift para LinkedIn ou reducao de frequencia com dados de suporte)
- Fadiga por posicao na sequencia (qual toque 1, 2, 3, 4 tem o maior drop de engajamento
- detecta onde a sequencia perde o usuario)

## Trigger

Job diario de calculo de Channel Health Score (6h); spike de unsubscribe ou spam report > 2x baseline detectado em tempo real (webhook); Kronos solicita analise antes de ativar campanha nova em um canal; fim de ciclo mensal para relatorio executivo

## Knowledge base (o que o executor consulta)

- Historico de metricas de envio por canal (12 meses), Benchmarks de saude de canal por setor (email B2B SaaS: open rate esperado 20-28%, reply rate 2-5%
- LinkedIn: acceptance rate 20-35%
- WhatsApp: read rate 80-95%), Thresholds de fadiga configurados pelo time, Calendario de campanhas ativas (para correlacionar spikes com eventos especificos)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Metricas agregadas de envio por canal e por lista (open rate, click rate, reply rate, unsubscribe rate, spam report rat…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Channel Health Score semanal por canal (0-100 com breakdown de sub-metricas)) e persistir no artefato do squad.
4. Entregar ao critic Aura 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Channel Health Score semanal por canal (0-100 com breakdown de sub-metricas)
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

- **to:** Helios
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
