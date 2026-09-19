---
task: charonDispatcher()
responsavel: "Charon Dispatcher"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Draft aprovado pelo crític Atena com metadados completos"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Score e trilha do lead (Oráculo Scorer)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Regras de gate L3 configuradas no onboarding (deal size threshold, segmentos estratégicos, leads marcados como 'VIP' no CRM)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Disponibilidade de calendário via API (Calendly ou Cal.com) para booking automático"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Limites de volume por conta de envio e regras de timing por canal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Log de envio verificável e imutável no ClickUp por cada mensagem: { reativação_id, lead_id, trilha, sequência_posição (toque 1/2/3/etc), canal, variação_ab, sent_at, status (sent / queued / blocked_gate_l3 / bounce_detectado), open_tracked, click_tracked, reply_received }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Atualização do CRM com activity de reativação (canal, data, posição na sequência)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para respostas positivas via webhook: link de booking enviado automaticamente + notificação urgente ao vendedor humano para assumir a conversa com contexto completo"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Para gates L3 ativados: notificação ao gestor com draft completo, ficha do lead e score para aprovação ou rejeição com 1 clique"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Para bounces confirmados: update automático no CRM e remoção da sequência ativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Lázaro imediatamente após Atena aprovar o draft. Follow-ups automáticos nos dias configurados pela trilha (exemplo trilha padrão: D0 / D4 / D9). Trigger de aceleramento: lead abre email…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Atena antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex: deal > R$20k) bloqueia completamente e notifica o gestor com draft completo, ficha de arqueologia e sinais novos para aprovacao ou rejeicao com 1 clique — nenhum caracter e enviado antes da aprovacao."
    - "[ ] HITL: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovação humana obrigatória antes de entrar em sequência — agente não envia para dado não verificado."
    - "[ ] HITL: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o gestor de marketing com o feedback completo do critic para reescritura ou descisao de nao envio."
    - "[ ] HITL: Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que disse, sugestão de próximo passo) — o squad paralisa qualquer automação para este lead e o vendedor assume o controle total da conversa."
    - "[ ] HITL: Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções de alto valor merecem resposta humana ou pelo menos validação antes de resposta automática."
---

# Enviar Mensagens Reativação

**Task ID:** `charonDispatcher()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enviar Mensagens Reativação |
| **status** | `pending` |
| **responsible_executor** | Charon Dispatcher (Charon Dispatcher — O Operador da Travessia) |
| **execution_type** | `Hybrid` |
| **input** | 5 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável pelo envio efetivo de todas as mensagens de reativação aprovadas pelo crític Atena. Gerencia o timing de cada toque por canal (evitando os horários que historicamente geram baixa abertura para o segmento), controla o espaço entre mensagens da sequência (nunca comprimir demais — reativação precisa de respiração entre toques), monitora o volume diário de envio por conta para proteger a reputação de domínio, e processa as respostas recebidas reenviando para o Echo Analyst. Para qualquer lead classificado como RESSURGIR com deal estimado acima do threshold L3 configurado no onboarding: BLOQUEIA completamente o envio e notifica o gestor humano com o draft completo, ficha de arqueologia e sinais novos para aprovação com 1 clique antes de qualquer disparo. Opera com princípio de reversibilidade mínima: para leads com dados de baixa confiança, envia primeiro um email de 'atualização de contato' para validar o dado antes de entrar na sequência completa.

## Input

- Draft aprovado pelo crític Atena com metadados completos
- Score e trilha do lead (Oráculo Scorer)
- Regras de gate L3 configuradas no onboarding (deal size threshold, segmentos estratégicos, leads marcados como 'VIP' no CRM)
- Disponibilidade de calendário via API (Calendly ou Cal.com) para booking automático
- Limites de volume por conta de envio e regras de timing por canal

## Output

- Log de envio verificável e imutável no ClickUp por cada mensagem: { reativação_id, lead_id, trilha, sequência_posição (toque 1/2/3/etc), canal, variação_ab, sent_at, status (sent / queued / blocked_gate_l3 / bounce_detectado), open_tracked, click_tracked, reply_received }
- Atualização do CRM com activity de reativação (canal, data, posição na sequência)
- Para respostas positivas via webhook: link de booking enviado automaticamente + notificação urgente ao vendedor humano para assumir a conversa com contexto completo
- Para gates L3 ativados: notificação ao gestor com draft completo, ficha do lead e score para aprovação ou rejeição com 1 clique
- Para bounces confirmados: update automático no CRM e remoção da sequência ativa

## Trigger

Ativado pelo Lázaro imediatamente após Atena aprovar o draft. Follow-ups automáticos nos dias configurados pela trilha (exemplo trilha padrão: D0 / D4 / D9). Trigger de aceleramento: lead abre email ou clica em link = prioriza o próximo toque da sequência para o dia seguinte. Trigger de cancelamento: lead responde com opt-out = cancela toda a sequência, atualiza CRM com 'opt-out reativação' e nunca mais envia sem reinscrição explícita. Trigger de upgrade: lead responde positivamente = cancela a sequência, notifica Echo Analyst e vendedor humano.

## Knowledge base (o que o executor consulta)

- Regras de timing por canal para reativação B2B: email (Ter-Qui 9h-11h e 14h-16h, evitar segunda manhã e sexta tarde), WhatsApp para reativação (mais delicado que cold outreach
- apenas horário comercial, Ter-Qui preferencial, nunca primeiro toque via WhatsApp sem email anterior)
- Espaçamento mínimo entre toques de reativação por archetype: leads que nunca responderam = 4-5 dias de espaço (não parecer spam), leads que engajaram antes = 3-4 dias (maior urgência), timing prometido expirado = pode ser D0/D2/D5 mais agressivo
- Limites de volume diário por conta
- Regras de gate L3 configuradas
- Template de notificação de gate L3 para gestor com contexto suficiente para decidir em 30 segundos
- Política de tratamento de bounce: hard bounce = remoção imediata e alerta ao CRM
- soft bounce = retry em 24h x3 antes de remoção

## Action Items

1. Confirmar o gatilho e carregar a entrada (Draft aprovado pelo crític Atena com metadados completos).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Log de envio verificável e imutável no ClickUp por cada mensagem: { reativação_id, lead_id, trilha, sequência_posição (…) e persistir no artefato do squad.
4. Entregar ao critic Atena; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Log de envio verificável e imutável no ClickUp por cada mensagem: { reativação_id, lead_id, trilha, sequência_posição (toque 1/2/3/etc), canal, variação_ab, se…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Atena registrado
- [ ] Gate HITL respeitado: Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configura…
- [ ] Gate HITL respeitado: Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança…
- [ ] Gate HITL respeitado: Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrig…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Gate L3 no Charon Dispatcher: qualquer envio para leads classificados como RESSURGIR cujo deal estimado esteja acima do threshold configurado no onboarding (ex… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Dados de baixa confiança detectados pela Arqueologa ou Radar: email com mais de 12 meses sem verificação ou lead com indicativo de mudança de empresa = aprovaç… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Atena reprova draft duas vezes consecutivas: draft que falha no checklist e que a reescritura automatica do Lazaro Writer tambem nao corrigiu e escalado para o… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Echo Analyst classifica resposta como RESSUSCITADO: notificação urgente e imediata ao vendedor humano com contexto completo (ficha do lead, histórico, o que di… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lead responde com OBJEÇÃO_TRATÁVEL de alto valor: Echo Analyst gera sugestão de reply mas coloca o draft em fila de aprovação humana antes de enviar — objeções… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Sinais de oportunidade detectados em lead que estava em ARQUIVO (score < 40): Radar detecta mudança significativa (investimento, mudança de decisor, sinal de i… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Relatório semanal de performance: Echo Analyst gera relatório de taxa de reativação por trilha e archetype entregue ao gestor todo friday — ponto de HITL estru… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Opt-out recebido: processamento automático cancela a sequência e atualiza o CRM, mas a decisão de blacklist permanente (nunca mais contatar) é sempre humana —… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Atena | BLOQUEIA entrega |

## Handoff

- **to:** Echo Analyst
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
