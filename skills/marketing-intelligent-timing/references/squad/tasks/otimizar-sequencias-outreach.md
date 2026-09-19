---
task: vega()
responsavel: "Vega"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sequencia de outreach atual com toques e copy ja definidos (input externo do time de SDR/Copywriter)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Schedule otimizado por lead (Helios output)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "regras de negocio de sequencia configuradas (limites de frequencia, logica de escalada de canal, condicoes de exit da sequencia)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Channel Health Scores (Pulsar output, para nao alocar toques em canal com saude critica)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Sequencia Redesenhada (JSON e visualizacao em formato de timeline: cada toque com canal, dia relativo, janela de horario, condicao de avanco ou saida)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatorio de ajustes feitos vs"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "sequencia original com justificativa para cada mudanca"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Sequencia Otimizada pronta para aprovacao humana (HITL gate L3 antes de ativar em producao)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Time de SDR submete nova sequencia para otimizacao; Kronos inicia ciclo de Deep Dive; Pulsar detecta queda de performance em sequencia ativa que justifica redesign; revisao mensal de sequencias ativa…"
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

# Otimizar Sequências Outreach

**Task ID:** `vega()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Intelligent Timing Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Otimizar Sequências Outreach |
| **status** | `pending` |
| **responsible_executor** | Vega (Vega — Sequence Architect) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Redesenha e otimiza as sequencias de outreach com base nos insights de timing. Vega nao cria copy — recebe as sequencias ja escritas e redistribui os toques pelos canais e horarios otimos calculados por Helios. Garante coerencia da sequencia como um todo: se o lead nao respondeu ao toque 1 (email), Vega decide se o toque 2 deve ser LinkedIn (escalada de canal), WhatsApp (mais urgente) ou um segundo email com horario diferente. Implementa regras de negocio de sequencia: nunca dois toques no mesmo dia a menos que o lead tenha respondido; nunca WhatsApp antes de email exceto em sequencias de aceleracao pos-reuniao; limite de toques por canal por semana. Ao final de cada ciclo mensal, propoe ajustes de sequencia baseados em performance observada.

## Input

- Sequencia de outreach atual com toques e copy ja definidos (input externo do time de SDR/Copywriter)
- Schedule otimizado por lead (Helios output)
- regras de negocio de sequencia configuradas (limites de frequencia, logica de escalada de canal, condicoes de exit da sequencia)
- Channel Health Scores (Pulsar output, para nao alocar toques em canal com saude critica)

## Output

- Sequencia Redesenhada (JSON e visualizacao em formato de timeline: cada toque com canal, dia relativo, janela de horario, condicao de avanco ou saida)
- Relatorio de ajustes feitos vs
- sequencia original com justificativa para cada mudanca
- Sequencia Otimizada pronta para aprovacao humana (HITL gate L3 antes de ativar em producao)

## Trigger

Time de SDR submete nova sequencia para otimizacao; Kronos inicia ciclo de Deep Dive; Pulsar detecta queda de performance em sequencia ativa que justifica redesign; revisao mensal de sequencias ativas (ciclo recorrente); resultado de A/B test mostra sequencia controle superando sequencia tratamento (trigger de revisao urgente)

## Knowledge base (o que o executor consulta)

- Biblioteca de sequencias ativas e historicas com metricas de performance, Regras de negocio de sequencia configuradas pelo time (limites, logica de canal, exits), Playbook de escalada de canal (quando usar cada canal em cada momento da sequencia), Benchmarks de sequencia por segmento de ICP (quantos toques, qual mix de canal, qual espacamento funciona melhor em cada vertical)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sequencia de outreach atual com toques e copy ja definidos (input externo do time de SDR/Copywriter)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Sequencia Redesenhada (JSON e visualizacao em formato de timeline: cada toque com canal, dia relativo, janela de horari…) e persistir no artefato do squad.
4. Entregar ao critic Aura 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Sequencia Redesenhada (JSON e visualizacao em formato de timeline: cada toque com canal, dia relativo, janela de horario, condicao de avanco ou saida)
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

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
