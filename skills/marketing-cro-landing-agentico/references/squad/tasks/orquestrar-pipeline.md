---
task: maestroCroPipeline()
responsavel: "Maestro CRO"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "CRO Operations Package"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "artefato verificável completo por ciclo quinzenal: (1) CRO Audit Report inicial com mapa de fricções e top-10 hipóteses priorizadas por ICE Score"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Experiment Packages por wave (hipótese documentada, variações de copy Muse, specs de layout Pixel, configuração Darwin, aprovação Rex)"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "(3) Experiment Conclusion Reports individuais com vencedor/perdedor, lift absoluto/relativo, intervalo de confiança e learning documentado"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(4) CRO Playbook vivo e versionado com todos os learnings acumulados (o ativo mais valioso do squad"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "não vai embora com o agente, fica com o cliente)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Decompoe a meta de conversao em hipoteses testáveis e gerencia o backlog de experimentos. Decide a priorizacao de hipoteses usando o framework ICE Score (Impact x Confidence x Ease), delega producao…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Rex 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3): a empresa precisa concordar com o diagnóstico antes de escalar produção"
    - "[ ] HITL: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de produto ou páginas com > 50% do budget de tráfego (L3): mudanças de alto impacto requerem olho humano final"
    - "[ ] HITL: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qualquer reescrita (L3)"
    - "[ ] HITL: Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão estratégica que requer stakeholders (L3)"
    - "[ ] HITL: Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, métrica primária e budget de tráfego (L3)"
---

# Orquestrar Pipeline do CRO & Landing Page Agêntico

**Task ID:** `maestroCroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** CRO & Landing Page Agêntico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do CRO & Landing Page Agêntico |
| **status** | `pending` |
| **responsible_executor** | Maestro CRO (Maestro CRO — Orquestrador de Experimentação) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Decompoe a meta de conversao em hipoteses testáveis e gerencia o backlog de experimentos. Decide a priorizacao de hipoteses usando o framework ICE Score (Impact x Confidence x Ease), delega producao de variacoes para workers especializados, monitora velocidade de aprendizado (learnings por sprint) e aciona HITL nos gates de publicacao. Opera no padrao orchestrator-worker: nao escreve copy nem configura testes diretamente — orquestra, prioriza e sintetiza. Persona: obcecado com velocidade de iteracao e significancia estatistica. Nunca publica variacao sem gate de qualidade. Alias: 'Maestro' — pois conduz a sinfonia de experimentos como um regente que sabe exatamente quando cada instrumento entra.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- CRO Operations Package
- artefato verificável completo por ciclo quinzenal: (1) CRO Audit Report inicial com mapa de fricções e top-10 hipóteses priorizadas por ICE Score
- (2) Experiment Packages por wave (hipótese documentada, variações de copy Muse, specs de layout Pixel, configuração Darwin, aprovação Rex)
- (3) Experiment Conclusion Reports individuais com vencedor/perdedor, lift absoluto/relativo, intervalo de confiança e learning documentado
- (4) CRO Playbook vivo e versionado com todos os learnings acumulados (o ativo mais valioso do squad
- não vai embora com o agente, fica com o cliente)
- (5) Velocity Dashboard no ClickUp com taxa de conversão por página, experimentos ativos, lift médio e backlog priorizado
- (6) Relatório Executivo Quinzenal para CMO/Growth Lead com resumo de resultados, próximo ciclo planejado e ROI estimado do portfolio de experimentos

## Trigger

Decompoe a meta de conversao em hipoteses testáveis e gerencia o backlog de experimentos. Decide a priorizacao de hipoteses usando o framework ICE Score (Impact x Confidence x Ease), delega producao de variacoes para workers especializados, monitora velocidade de aprendizado (learnings por sprint) e aciona HITL nos gates de publicacao. Opera no padrao orchestrator-worker: nao escreve copy nem configura testes diretamente — orquestra, prioriza e sintetiza. Persona: obcecado com velocidade de iteracao e significancia estatistica. Nunca publica variacao sem gate de qualidade. Alias: 'Maestro' — pois conduz a sinfonia de experimentos como um regente que sabe exatamente quando cada instrumento entra.

## Knowledge base (o que o executor consulta)

- Google Analytics 4
- fonte primária de dados de conversão, funil de comportamento por fonte/dispositivo/segmento, eventos de objetivo configurados por página
- Hotjar ou Microsoft Clarity
- heatmaps, gravações de sessão, scroll depth maps e pesquisas on-exit
- Hera é o principal consumidor desta integração
- Google Optimize / VWO / Unbounce Smart Traffic / Optimizely
- ferramentas de teste A/B e multivariado
- Darwin configura e monitora experimentos aqui (escolha depende da stack do cliente)
- Unbounce / Webflow / WordPress + Elementor
- construtores de landing page onde as variações são implementadas pelo time após aprovação de Rex
- HubSpot CRM
- tracking de leads gerados por variação de landing page (UTM parameters por variação para atribuição de pipeline), integração de formulário com campos de source/medium/experiment_id
- Google Ads / Meta Ads
- source de tráfego das campanhas
- Rex verifica message match entre o ad e a landing page antes de publicar variação
- prova de trabalho: task automática por experimento (hipótese, resultado, learning), dashboard de KPIs de CRO (taxa de conversão por página, experimentos ativos, lift acumulado), backlog de hipóteses como lista priorizada
- Figma / Whimsical
- Pixel deposita wireframes e specs de layout como artefatos verificáveis antes de implementação
- observabilidade OTEL de todos os agentes, quality gates (dev 70% / staging 85% / prod 95% task success), rastreamento de custo por ciclo de experimentação
- orquestração de webhooks entre GA4, ferramentas de teste e ClickUp (alertas de significância estatística, notificações de anomalia de conversão, triggers de ciclo quinzenal)
- Slack / Email
- notificações de experimento encerrado com resultado, alertas de anomalia de conversão e despacho de relatório quinzenal de velocidade de aprendizado para stakeholders

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Rex 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: CRO Operations Package
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Rex 2 registrado
- [ ] Gate HITL respeitado: Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção d…
- [ ] Gate HITL respeitado: Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na pág…
- [ ] Gate HITL respeitado: Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel lega…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do CRO Audit Report ao final do Discovery — CMO/Growth Lead valida a priorização das top-10 hipóteses antes de iniciar produção de copy e layout (L3)… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de variação no ar — Rex retorna APPROVED mas o Maestro aciona HITL para experimentos que alteram elementos above-the-fold na página principal de pro… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Rex retorna BLOCKED em qualquer verificacao — violacao critica de brand/legal nao pode ser resolvida autonomamente; CMO ou responsavel legal revisa antes de qu… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Resultado de experimento que sugere mudança estrutural de posicionamento — se o learning indica que a promessa principal do produto precisa mudar, é decisão es… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovação de novas landing pages adicionadas ao portfolio do squad — cada nova página representa expansão de escopo e precisa de alinhamento sobre objetivos, m… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Escalada de experimento inconclusivo após 4 semanas — Darwin alerta, Maestro analisa, mas decisão de encerrar ou aumentar tráfego para o teste e humana (L1): i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao trimestral do CRO Playbook — Atlas apresenta o estado do conhecimento acumulado, Growth Lead decide quais learnings viram regras permanentes e quais hi… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Rex 2 | BLOQUEIA entrega |

## Handoff

- **to:** Hera
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
