---
task: sirius()
responsavel: "Sirius"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Stream de eventos de engajamento com timestamp (abertura, clique, resposta, ignore, unsubscribe, spam report) de email platforms (HubSpot, Instantly, Mailchimp), LinkedIn Sales Navigator, WhatsApp Business API"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Timing Profiles atuais por lead"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "configuracao de janela de lookback (padrao: 90 dias)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "mapeamento lead -> segmento de ICP"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Timing Profile atualizado por lead (JSON: {lead_id, canal, janela_otima_inicio, janela_otima_fim, probabilidade_abertura, frequencia_max_por_semana, indice_saturacao, ultimo_update, confianca_do_modelo})"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Heatmap de engajamento agregado por segmento de ICP (para usar como prior em novos leads)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Delta report de mudancas de perfil na semana (leads que mudaram janela otima ou canal preferido)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook de novo evento de engajamento (near real-time); Job semanal de recalculo completo da base ativa (domingo 2h); Kronos solicita perfil especifico para agendamento de toque iminente; novo lead e…"
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

# Calcular Janelas Receptividade

**Task ID:** `sirius()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Intelligent Timing Orchestrator

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Janelas Receptividade |
| **status** | `pending` |
| **responsible_executor** | Sirius (Sirius — Behavioral Historian) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Constroi e mantém o Timing Profile de cada lead/conta: um modelo comportamental temporal que registra quando o usuario demonstrou receptividade em cada canal. Processa eventos de abertura de email, clique em link, resposta a mensagem, visualizacao de perfil LinkedIn e leitura de WhatsApp (quando disponivel) — todos com timestamp preciso. Calcula janelas de receptividade por canal (ex: 'Joao Silva: email 7h30-9h, probabilidade 72%; WhatsApp 12h-13h, probabilidade 58%'), velocidade de resposta media por canal, e indice de saturacao (quantos toques antes de queda de engajamento). Atualiza o perfil a cada novo evento de forma incremental — o modelo e sempre o mais recente. Para novos leads sem historico, aplica o perfil do segmento de ICP mais proximo como prior bayesiano ate acumular dados suficientes (threshold: 3 eventos por canal).

## Input

- Stream de eventos de engajamento com timestamp (abertura, clique, resposta, ignore, unsubscribe, spam report) de email platforms (HubSpot, Instantly, Mailchimp), LinkedIn Sales Navigator, WhatsApp Business API
- Timing Profiles atuais por lead
- configuracao de janela de lookback (padrao: 90 dias)
- mapeamento lead -> segmento de ICP

## Output

- Timing Profile atualizado por lead (JSON: {lead_id, canal, janela_otima_inicio, janela_otima_fim, probabilidade_abertura, frequencia_max_por_semana, indice_saturacao, ultimo_update, confianca_do_modelo})
- Heatmap de engajamento agregado por segmento de ICP (para usar como prior em novos leads)
- Delta report de mudancas de perfil na semana (leads que mudaram janela otima ou canal preferido)

## Trigger

Webhook de novo evento de engajamento (near real-time); Job semanal de recalculo completo da base ativa (domingo 2h); Kronos solicita perfil especifico para agendamento de toque iminente; novo lead entra na base sem historico (trigger de inicializacao de prior)

## Knowledge base (o que o executor consulta)

- Historico completo de eventos de engajamento por lead (90-365 dias dependendo do tier), Timing Profiles versionados (mantém ultimas 4 versoes para detectar tendencias), Priors por segmento de ICP (perfil medio de timing do segmento para bootstrapping de novos leads), Padroes sazonais conhecidos (feriados, periodos de ferias, conferencias do setor que afetam receptividade)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Stream de eventos de engajamento com timestamp (abertura, clique, resposta, ignore, unsubscribe, spam report) de email…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Timing Profile atualizado por lead (JSON: {lead_id, canal, janela_otima_inicio, janela_otima_fim, probabilidade_abertur…) e persistir no artefato do squad.
4. Entregar ao critic Aura 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Timing Profile atualizado por lead (JSON: {lead_id, canal, janela_otima_inicio, janela_otima_fim, probabilidade_abertura, frequencia_max_por_semana, indice_sat…
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

- **to:** Pulsar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
