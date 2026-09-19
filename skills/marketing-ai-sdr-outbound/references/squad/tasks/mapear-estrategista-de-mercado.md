---
task: icpCartografo()
responsavel: "ICP Cartografo"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Histórico de CRM do cliente (deals fechados, churnados, expandidos"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "mínimo 6 meses)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Entrevistas com top 5 clientes (transcrições ou notas)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Dados de churn e NRR"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Acesso a web para deep research de mercado (EXA/WebSearch)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Relatórios de PMF do cliente quando disponíveis"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "ICP vivo estruturado em Markdown com 4 seções: (1) Firmográfico"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "segmentos-alvo, porte (funcionários/receita), verticais, tecnologias em uso como indicadores de fit, regiões prioritárias"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Comportamental"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "triggers de compra (hiring, expansão, mudança de liderança, adoção de tecnologia complementar), sazonalidade, ciclo orçamentário típico"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Psicográfico"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "perfil do decisor por cargo (CEO vs VP Vendas vs Marketing), linguagem que usa, objeções típicas, motivações primárias"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Trigger inicial no onboarding para construção do ICP baseline. Refresh mensal automático via cron. Re-trigger imediato se Pulse Analyst detectar shift significativo em patterns de resposta (ex: objeç…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR humano com draft completo, dossiê e score para aprovação ou rejeição com 1 clique antes de qualquer disparo."
    - "[ ] HITL: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o feedback detalhado do critic para reescritura manual."
    - "[ ] HITL: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente não envia com informação não verificada."
    - "[ ] HITL: Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para assumir a conversa — o squad nao conduz negociacao, apenas entrega o contexto completo e recua."
    - "[ ] HITL: Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do gestor comercial antes de qualquer envio."
---

# Mapear Estrategista De Mercado

**Task ID:** `icpCartografo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Mapear Estrategista De Mercado |
| **status** | `pending` |
| **responsible_executor** | ICP Cartografo (ICP Cartografô — O Estrategista de Mercado) |
| **execution_type** | `Worker` |
| **input** | 6 item(ns) |
| **output** | 10 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Mantém e atualiza continuamente o ICP vivo do cliente a partir de 3 fontes: (1) dados do CRM (quais contas fecharam, churnaram, expandiram — pattern mining de deals reais), (2) deep research de mercado (tendências do setor, movimentos de concorrentes, shifts de demanda detectados via web), (3) synthetic personas geradas a partir de entrevistas com clientes e pesquisa de PMF. Entrega o ICP como um documento vivo estruturado com dimensões firmográficas, comportamentais e psicográficas por tier (Tier 1: maior fit e maior valor, Tier 2: fit médio, Tier 3: experimental). Atualiza o ICP mensalmente ou quando um shift de mercado significativo é detectado. Alimenta diretamente os playbooks do Cyrano e os critérios de scoring do Calibre.

## Input

- Histórico de CRM do cliente (deals fechados, churnados, expandidos
- mínimo 6 meses)
- Entrevistas com top 5 clientes (transcrições ou notas)
- Dados de churn e NRR
- Acesso a web para deep research de mercado (EXA/WebSearch)
- Relatórios de PMF do cliente quando disponíveis

## Output

- ICP vivo estruturado em Markdown com 4 seções: (1) Firmográfico
- segmentos-alvo, porte (funcionários/receita), verticais, tecnologias em uso como indicadores de fit, regiões prioritárias
- (2) Comportamental
- triggers de compra (hiring, expansão, mudança de liderança, adoção de tecnologia complementar), sazonalidade, ciclo orçamentário típico
- (3) Psicográfico
- perfil do decisor por cargo (CEO vs VP Vendas vs Marketing), linguagem que usa, objeções típicas, motivações primárias
- (4) Tier Matrix
- scoring de fit por combinação de atributos
- Artefato salvo no ClickUp e versionado
- ICP Card por persona exportado para consumo do Cyrano e Calibre

## Trigger

Trigger inicial no onboarding para construção do ICP baseline. Refresh mensal automático via cron. Re-trigger imediato se Pulse Analyst detectar shift significativo em patterns de resposta (ex: objeção nova emergindo em >30% das respostas no mês). Re-trigger manual solicitado pelo SDR humano ou pelo Maestro.

## Knowledge base (o que o executor consulta)

- Frameworks de ICP e Jobs-to-be-Done
- Metodologia de synthetic personas (Market Logic DeepSights, frameworks Deepsona)
- Biblioteca de verticais e seus triggers de compra típicos (agências digitais, SaaS B2B, indústria, serviços profissionais, imobiliário, educação)
- Histórico de ICPs anteriores do cliente para tracking de evolução
- Templates de ICP Card por persona para consumo dos workers downstream

## Action Items

1. Confirmar o gatilho e carregar a entrada (Histórico de CRM do cliente (deals fechados, churnados, expandidos).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (ICP vivo estruturado em Markdown com 4 seções: (1) Firmográfico) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: ICP vivo estruturado em Markdown com 4 seções: (1) Firmográfico
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloquei…
- [ ] Gate HITL respeitado: Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para…
- [ ] Gate HITL respeitado: Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Cadence Dispatcher: qualquer envio para contas estratégicas (deal estimado acima do threshold configurado no onboarding) bloqueia e notifica o SDR h… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Reescritura falhou 2x no Sentinel: draft reprovado pelo Sentinel que nao passou nem com a reescritura automatica do Cyrano e escalado para o SDR humano com o f… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Score de confiança do dossiê do Scout Profiler abaixo de 60: alerta ao SDR humano para verificar manualmente os dados antes de autorizar o outreach – agente nã… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Pulse Analyst detecta intent = CONFIRMED_INTEREST ou sentiment = VERY_POSITIVE em qualquer resposta: notificacao imediata e urgente ao SDR/Closer humano para a… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Mensagem com condição comercial detectada pelo Sentinel (desconto, condição especial, prazo garantido): bloqueio automático e encaminhamento para aprovação do… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ICP Cartografo detecta shift significativo de mercado (nova objecao emergindo em >30% das respostas, queda de >20% no reply rate em 2 semanas consecutivas): al… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Opt-out ou resposta negativa agressiva: processado pelo Pulse Analyst, sequência cancelada automaticamente, CRM atualizado, notificação ao SDR para decisão sob… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Scout Profiler
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
