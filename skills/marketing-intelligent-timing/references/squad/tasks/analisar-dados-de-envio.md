---
task: lumina()
responsavel: "Lumina"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Log de execucao de todos os envios com timestamps (Nexus output)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "eventos de engajamento por toque (abertura, clique, resposta, reuniao agendada) com atribuicao ao toque especifico"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "dados de CRM sobre oportunidades abertas e seus toques de origem"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "configuracao do experimento A/B ativo (grupos, metricas de sucesso, tamanho de amostra)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Timing Performance Report semanal (open/reply rate por canal x horario x segmento, comparando tratamento vs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "controle com significancia estatistica)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Uplift Report mensal (uplift percentual de cada KPI vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "baseline, pipeline incremental estimado, ROI do squad)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Anomaly Alerts (quando metrica cai > 20% vs"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "media das ultimas 4 semanas sem justificativa conhecida)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job semanal de geracao do Performance Report (segunda-feira 7h); fim de mes para Uplift Report; anomalia detectada em monitoramento continuo (alertas near real-time para quedas abruptas); Kronos soli…"
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

# Analisar Dados De Envio

**Task ID:** `lumina()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Intelligent Timing Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Dados De Envio |
| **status** | `pending` |
| **responsible_executor** | Lumina (Lumina — Insights & Attribution Reporter) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 9 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Fecha o loop de aprendizado: transforma os dados de performance de envio em insights acionaveis para o time e em sinais de treinamento para o modelo de Helios. Lumina consolida metricas de open rate, reply rate, click rate e conversao por canal, horario, segmento de ICP e posicao na sequencia — sempre comparando grupo de timing otimizado vs. grupo controle (baseline de envio padrao). Produz o Timing Performance Report semanal e o Uplift Report mensal. Detecta anomalias estatisticas (ex: canal que estava performando bem despenca repentinamente — trigger de investigacao). Tambem calcula o ROI do squad: pipeline incremental gerado pelo uplift de reply rate vs. custo operacional do squad.

## Input

- Log de execucao de todos os envios com timestamps (Nexus output)
- eventos de engajamento por toque (abertura, clique, resposta, reuniao agendada) com atribuicao ao toque especifico
- dados de CRM sobre oportunidades abertas e seus toques de origem
- configuracao do experimento A/B ativo (grupos, metricas de sucesso, tamanho de amostra)

## Output

- Timing Performance Report semanal (open/reply rate por canal x horario x segmento, comparando tratamento vs
- controle com significancia estatistica)
- Uplift Report mensal (uplift percentual de cada KPI vs
- baseline, pipeline incremental estimado, ROI do squad)
- Anomaly Alerts (quando metrica cai > 20% vs
- media das ultimas 4 semanas sem justificativa conhecida)
- Feed de sinais de treinamento para Helios (quais agendamentos resultaram em abertura/resposta vs
- ignorados
- para refinamento do modelo preditivo)

## Trigger

Job semanal de geracao do Performance Report (segunda-feira 7h); fim de mes para Uplift Report; anomalia detectada em monitoramento continuo (alertas near real-time para quedas abruptas); Kronos solicita analise especifica de performance de segmento ou campanha; A/B test acumula amostra suficiente para analise de significancia

## Knowledge base (o que o executor consulta)

- Historico completo de metricas de envio por toque (12 meses), Dados de conversao do CRM com atribuicao multitouch, Configuracao dos experimentos A/B ativos com grupos e metricas, Benchmarks de mercado por canal e setor para contextualizacao dos resultados, Historico de anomalias anteriores e suas causas (para acelerar investigacao de novas anomalias)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Log de execucao de todos os envios com timestamps (Nexus output)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Timing Performance Report semanal (open/reply rate por canal x horario x segmento, comparando tratamento vs) e persistir no artefato do squad.
4. Entregar ao critic Aura 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Timing Performance Report semanal (open/reply rate por canal x horario x segmento, comparando tratamento vs
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

- **to:** Aura 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
