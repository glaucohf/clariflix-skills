---
task: nexus()
responsavel: "Nexus"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Schedule otimizado aprovado (Helios + Vega output, com flag de aprovacao humana quando aplicavel)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "credenciais de acesso aos sistemas de envio via MCP"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "configuracao de retry policy e limites de rate limit por API"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "lista de leads em blacklist ou com flag de opt-out atualizada"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Log de execucao por toque (lead_id, canal, timestamp_agendado, timestamp_real_de_envio, status: sent/failed/queued, message_id para rastreamento)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatorio de falhas de envio com causa (API down, opt-out detectado, rate limit, bounce)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Feed de eventos de envio para Sirius (para atualizar Timing Profiles com confirmacao de envio vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "abertura)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Timestamp de agendamento atingido (execucao automatica L3 para envios ja aprovados); Novo schedule aprovado pelo time carregado na fila; Kronos aciona disparo imediato de alerta (ex: lead voltou ao s…"
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

# Enviar Mensagens Agendadas

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Intelligent Timing Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagens Agendadas |
| **status** | `pending` |
| **responsible_executor** | Nexus (Nexus — Send Execution & Scheduler) |
| **execution_type** | `Hybrid` |
| **input** | 4 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Camada de execucao: recebe o schedule calculado por Helios e os agendamentos aprovados de Vega e dispara as mensagens nos sistemas de envio via MCP no momento exato calculado. Nexus e o unico agente que tem permissao de escrita nos sistemas de envio externos (HubSpot Sequences, Instantly, LinkedIn Sales Navigator, WhatsApp Business API). Mantem fila de envio com retry logic (se API de envio retorna erro, tenta novamente em 5 minutos ate 3x antes de escalar para Kronos). Registra cada disparo com timestamp real de execucao para fechar o loop de aprendizado de Sirius. Para campanhas com audiencia > 500 contatos ou budget de ads envolvido, exige aprovacao humana antes de executar (L3).

## Input

- Schedule otimizado aprovado (Helios + Vega output, com flag de aprovacao humana quando aplicavel)
- credenciais de acesso aos sistemas de envio via MCP
- configuracao de retry policy e limites de rate limit por API
- lista de leads em blacklist ou com flag de opt-out atualizada

## Output

- Log de execucao por toque (lead_id, canal, timestamp_agendado, timestamp_real_de_envio, status: sent/failed/queued, message_id para rastreamento)
- Relatorio de falhas de envio com causa (API down, opt-out detectado, rate limit, bounce)
- Feed de eventos de envio para Sirius (para atualizar Timing Profiles com confirmacao de envio vs
- abertura)

## Trigger

Timestamp de agendamento atingido (execucao automatica L3 para envios ja aprovados); Novo schedule aprovado pelo time carregado na fila; Kronos aciona disparo imediato de alerta (ex: lead voltou ao site — trigger de toque urgente); Job de limpeza de fila executado diariamente para remover envios de leads que opt-out entre agendamento e execucao

## Knowledge base (o que o executor consulta)

- Blacklist e opt-out list atualizada em tempo real (sincronizada com todos os sistemas de envio), Rate limits e politicas de uso de cada API de envio, Regras de compliance por canal e regiao (CAN-SPAM para email EUA, LGPD para WhatsApp Brasil, limites de mensagem do LinkedIn), Historico de falhas de API para detectar padroes de instabilidade

## Action Items

1. Confirmar o gatilho e carregar a entrada (Schedule otimizado aprovado (Helios + Vega output, com flag de aprovacao humana quando aplicavel)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Log de execucao por toque (lead_id, canal, timestamp_agendado, timestamp_real_de_envio, status: sent/failed/queued, mes…) e persistir no artefato do squad.
4. Entregar ao critic Aura 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Log de execucao por toque (lead_id, canal, timestamp_agendado, timestamp_real_de_envio, status: sent/failed/queued, message_id para rastreamento)
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

- **to:** Aura
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
