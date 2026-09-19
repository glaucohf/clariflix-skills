---
task: radar()
responsavel: "Radar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Feeds de APIs (Apollo, Clay, LinkedIn Sales Navigator, plataforma de ads, Google Analytics/pixel do site, webhooks de CRM para eventos de retorno de leads inativos)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "ICP configuration (segmentos-alvo, cargos, porte, regiões, tecnologias-gatilho)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alerta de sinal estruturado em JSON: { lead_id, company, signal_type, signal_strength (1-10), signal_timestamp, raw_evidence_url, suggested_priority, icp_match_score }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Persiste no CRM como activity e aciona o Nexus via webhook"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron a cada 15 minutos para polling de APIs de intent; webhook imediato para eventos de alta prioridade (visita de decisor ao site de pricing, abertura de vaga de SDR na empresa-alvo, mudanca de VP d…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação antes do disparo."
    - "[ ] HITL: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial."
    - "[ ] HITL: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual."
    - "[ ] HITL: Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não conduz a negociação, apenas passa o contexto completo."
    - "[ ] HITL: Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach."
---

# Detectar Sinais Intencao

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Signal-Based

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Sinais Intencao |
| **status** | `pending` |
| **responsible_executor** | Radar (Radar — Detector de Sinais de Intenção) |
| **execution_type** | `Worker` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora continuamente as fontes de sinais configuradas (job postings, mudanças de liderança no LinkedIn, expansão tecnográfica via Clay/Apollo, engajamento com conteúdo/ads, visitas ao site, menções em redes sociais) e transforma eventos brutos em alertas estruturados com contexto de negócio. Filtra ruído descartando sinais fora do ICP configurado.

## Input

- Feeds de APIs (Apollo, Clay, LinkedIn Sales Navigator, plataforma de ads, Google Analytics/pixel do site, webhooks de CRM para eventos de retorno de leads inativos)
- ICP configuration (segmentos-alvo, cargos, porte, regiões, tecnologias-gatilho)

## Output

- Alerta de sinal estruturado em JSON: { lead_id, company, signal_type, signal_strength (1-10), signal_timestamp, raw_evidence_url, suggested_priority, icp_match_score }
- Persiste no CRM como activity e aciona o Nexus via webhook

## Trigger

Cron a cada 15 minutos para polling de APIs de intent; webhook imediato para eventos de alta prioridade (visita de decisor ao site de pricing, abertura de vaga de SDR na empresa-alvo, mudanca de VP de Vendas no LinkedIn).

## Knowledge base (o que o executor consulta)

- ICP definition (segmentos, cargos, porte, regiões)
- Dicionário de sinais por força (ex: abrir vaga SDR = força 8, visitar blog = força 3)
- Histórico de sinais que converteram nos últimos 90 dias
- Blacklist de domínios/empresas já em negociação ativa ou clientes existentes

## Action Items

1. Confirmar o gatilho e carregar a entrada (Feeds de APIs (Apollo, Clay, LinkedIn Sales Navigator, plataforma de ads, Google Analytics/pixel do site, webhooks de C…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alerta de sinal estruturado em JSON: { lead_id, company, signal_type, signal_strength (1-10), signal_timestamp, raw_evi…) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alerta de sinal estruturado em JSON: { lead_id, company, signal_type, signal_strength (1-10), signal_timestamp, raw_evidence_url, suggested_priority, icp_match…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossi…
- [ ] Gate HITL respeitado: Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do…
- [ ] Gate HITL respeitado: Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual.

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Envio para contas estratégicas (Tier 1, deal estimado acima do threshold configurado): Vox bloqueia e notifica SDR humano com draft + dossiê para aprovação ant… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Mensagem com desconto, condição especial ou promessa comercial detectada pelo Argus: bloqueio automático e encaminhamento para aprovação do gestor comercial. | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Draft reprovado 2x pelo Argus sem aprovacao: escala para SDR humano com o feedback do critic para reescritura manual. | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead responde com interesse alto (sentiment = positive + intent = interested): notificação imediata ao SDR/Closer humano para assumir a conversa — o agente não… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Score de confiança do dossiê do Sherlock abaixo de 60: alerta ao SDR humano para verificar manualmente antes de autorizar o outreach. | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Unsubscribe ou resposta negativa agressiva: processado pelo Lumen, CRM atualizado, notificação ao SDR para decisão sobre blacklist permanente. | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Sherlock
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
