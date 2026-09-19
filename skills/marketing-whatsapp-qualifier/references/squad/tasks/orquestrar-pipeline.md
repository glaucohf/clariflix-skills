---
task: orionPipeline()
responsavel: "Orion"
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
    descricao: "Artefato principal verificavel no ClickUp: Lead Qualification Record"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "por cada lead processado pelo squad, um registro estruturado contendo: (1) Transcript da conversa WhatsApp com etapas de qualificacao marcadas, (2) BANT Score preenchido por campo (0-3 por dimensao), (3) Lead Score total pos-qualificacao (0-10), (4) Enrichment Record de Rex com dados da empresa e contato, (5) Status final (Qualificado+Agendado / Qualificado+Pendente / Desqualificado com motivo / Escalado para SDR com motivo), (6) Link do evento de calendario criado por Mia (se agendado), (7) Briefing pre-reuniao de 5 linhas para o closer"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefatos secundarios: Playbook Conversacional versionado (Kira-approved), Dashboard semanal de metricas (Lilo), ROI Report mensal (Nova), Audit Log de conformidade Meta (Kira)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orion e o cerebro do squad: decompoe a meta de qualificacao (X leads -> Y reunioes agendadas no mes) em tasks delegadas aos workers. Monitora metricas em tempo real via Langfuse — se taxa de qualific…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Kira 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado (L3, sem aprovacao o squad nao avanca)"
    - "[ ] HITL: Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao. Kira ja auditou conformidade, mas humano decide se o tom esta certo (L3, gate obrigatorio)"
    - "[ ] HITL: Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa manualmente antes de Vance responder (L3, acao irreversivel: primeira impressao com conta estrategica)"
    - "[ ] HITL: Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion antes de Vance ser atualizado (L2, recorrente toda segunda-feira)"
    - "[ ] HITL: Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 com head de vendas e Kira antes de producao"
---

# Orquestrar Pipeline do WhatsApp Qualifier

**Task ID:** `orionPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do WhatsApp Qualifier |
| **status** | `pending` |
| **responsible_executor** | Orion (Orion — Maestro Comercial) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orion e o cerebro do squad: decompoe a meta de qualificacao (X leads -> Y reunioes agendadas no mes) em tasks delegadas aos workers. Monitora metricas em tempo real via Langfuse — se taxa de qualificacao cair abaixo do threshold, dispara analise de Lilo e propoe ajuste de playbook para aprovacao humana. Decide quando um lead deve ser escalado para SDR humano vs seguir no fluxo automatizado. Nao executa conversas diretamente — orquestra, prioriza, ajusta e sintetiza. Persona: SDR sênior com 10 anos de experiencia, pragmatico, orientado a numero, zero tolerancia a lead esfriando. Opera no padrao orchestrator-worker: um Opus lead coordenando Sonnet workers para otimizar custo/performance.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Artefato principal verificavel no ClickUp: Lead Qualification Record
- por cada lead processado pelo squad, um registro estruturado contendo: (1) Transcript da conversa WhatsApp com etapas de qualificacao marcadas, (2) BANT Score preenchido por campo (0-3 por dimensao), (3) Lead Score total pos-qualificacao (0-10), (4) Enrichment Record de Rex com dados da empresa e contato, (5) Status final (Qualificado+Agendado / Qualificado+Pendente / Desqualificado com motivo / Escalado para SDR com motivo), (6) Link do evento de calendario criado por Mia (se agendado), (7) Briefing pre-reuniao de 5 linhas para o closer
- Artefatos secundarios: Playbook Conversacional versionado (Kira-approved), Dashboard semanal de metricas (Lilo), ROI Report mensal (Nova), Audit Log de conformidade Meta (Kira)

## Trigger

Orion e o cerebro do squad: decompoe a meta de qualificacao (X leads -> Y reunioes agendadas no mes) em tasks delegadas aos workers. Monitora metricas em tempo real via Langfuse — se taxa de qualificacao cair abaixo do threshold, dispara analise de Lilo e propoe ajuste de playbook para aprovacao humana. Decide quando um lead deve ser escalado para SDR humano vs seguir no fluxo automatizado. Nao executa conversas diretamente — orquestra, prioriza, ajusta e sintetiza. Persona: SDR sênior com 10 anos de experiencia, pragmatico, orientado a numero, zero tolerancia a lead esfriando. Opera no padrao orchestrator-worker: um Opus lead coordenando Sonnet workers para otimizar custo/performance.

## Knowledge base (o que o executor consulta)

- WhatsApp Business API via BSP purpose-built pos-proibicao Meta
- Patagon AI (LATAM-first, recomendado), Leadsales ou BotPenguin como fallback
- Gateway principal de entrada e saida de mensagens
- HubSpot CRM
- registro automatico de leads qualificados, campos customizados de BANT (Budget, Authority, Need, Timeline), Lead Score pos-qualificacao, historico de conversa estruturado, trigger de criacao de oportunidade pos-qualificacao
- Google Calendar / Calendly
- disponibilidade em tempo real para Mia agendar reunioes, criacao de eventos com dados do lead, link de videoconferencia automatico (Google Meet / Zoom)
- waterfall enrichment em tempo real por Rex (firmographic, technographic, intent signals)
- Opcional se cliente ja tem Clay
- fallback para Apollo direto
- Apollo.io
- prospecting e enriquecimento de contatos B2B como fonte primaria ou backup do Clay
- prova de trabalho central: task automatica por lead qualificado, dashboard de metricas do squad (taxa de qualificacao, show-rate, ROI), briefing pre-reuniao para o closer, historico de playbook versions
- observabilidade OTEL de todos os agents, quality gates por ambiente (dev 70% / staging 85% / prod 95% task success), rastreamento de cada conversa como trace completo, evals de qualidade de resposta de Vance
- orquestracao de webhooks e workflows de notificacao (complemento no-code): alerta de lead VIP para SDR, notificacao de no-show para reengajamento, relatorio semanal de Lilo para Slack/email
- Slack / Email
- notificacoes de escalada para SDR humano (lead VIP, irritacao, objecao critica), alertas de anomalia de Lilo, relatorio semanal de performance do squad
- Meta Business Suite / BSP Dashboard
- monitoramento de saude da conta WhatsApp Business (Quality Rating, Phone Number Status, Message Template Status) integrado com Kira para alertas precoces de risco de banimento

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Kira 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Artefato principal verificavel no ClickUp: Lead Qualification Record
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Kira 2 registrado
- [ ] Gate HITL respeitado: Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do s…
- [ ] Gate HITL respeitado: Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e…
- [ ] Gate HITL respeitado: Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior par…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao.… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion ant… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 co… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Decisao de escalada por irritacao detectada — quando Vance detecta 3+ sinais de irritacao em sequencia, Orion alerta SDR humano via notificacao para assumir a… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao mensal de metricas com Nova — CEO/CMO aprova redistribuicao de budget por fonte de lead com base no ROI report de Nova (L3, envolve gasto financeiro) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Kira 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vance
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
