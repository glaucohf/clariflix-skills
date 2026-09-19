---
task: cyranoCopywriter()
responsavel: "Cyrano Copywriter"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Dossiê de conta completo (Scout Profiler) com ângulos de personalização ranqueados"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Score e tier do lead (Calibre Scorer)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "ICP Card da persona do decisor alvo (ICP Cartografo)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Canal de envio e sequência determinados pelo Maestro"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Guia de voz da marca do cliente (tom, vocabulário permitido/proibido, nível de formalidade, exemplos de mensagens aprovadas)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pack de outreach completo: 2 variacoes (A/B) por canal ativo com subject line (email, max 50 chars), preview text, corpo da mensagem, CTA unico e P.S"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "quando aplicavel"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Para sequencias: 4 mensagens completas (D0/D2/D5/D10) por variacao"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Cada draft inclui metadados obrigatorios: personalizacao_score (quantos elementos especificos do dossie foram usados"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "meta minimo: 3), compliance_flags (campos a verificar pelo Sentinel), estimated_read_time, canal_e_formato"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Formato JSON estruturado para consumo do Sentinel"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Maestro após Calibre Scorer classificar o lead como FIRE ou HOT e o dossiê estar com score de confiança >= 70. Re-trigger (reescritura) se Sentinel reprovar — max 1 reescritura automátic…"
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

# Redigir Mensagens Personalizadas

**Task ID:** `cyranoCopywriter()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad AI SDR Outbound Agentico

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Redigir Mensagens Personalizadas |
| **status** | `pending` |
| **responsible_executor** | Cyrano Copywriter (Cyrano Copywriter — O Mestre da Mensagem) |
| **execution_type** | `Agent` |
| **input** | 5 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Redige os drafts de outreach personalizados para cada canal (email, LinkedIn message, WhatsApp, script de voz) usando obrigatoriamente pelo menos 3 elementos especificos do dossie do Scout Profiler — nunca frases genericas. Adapta estrutura, tom, comprimento e CTA ao canal, ao cargo do decisor e ao angulo de personalizacao selecionado. Gera 2 variacoes (A/B) de cada mensagem para teste. Para sequencias: gera o fluxo completo D0 + D2 + D5 + D10 com cada mensagem construida sobre o contexto da anterior. Nunca envia — entrega ao Sentinel Critic para validacao. Se reprovado, reescreve uma vez com o feedback especifico antes de escalar para HITL.

## Input

- Dossiê de conta completo (Scout Profiler) com ângulos de personalização ranqueados
- Score e tier do lead (Calibre Scorer)
- ICP Card da persona do decisor alvo (ICP Cartografo)
- Canal de envio e sequência determinados pelo Maestro
- Guia de voz da marca do cliente (tom, vocabulário permitido/proibido, nível de formalidade, exemplos de mensagens aprovadas)

## Output

- Pack de outreach completo: 2 variacoes (A/B) por canal ativo com subject line (email, max 50 chars), preview text, corpo da mensagem, CTA unico e P.S
- quando aplicavel
- Para sequencias: 4 mensagens completas (D0/D2/D5/D10) por variacao
- Cada draft inclui metadados obrigatorios: personalizacao_score (quantos elementos especificos do dossie foram usados
- meta minimo: 3), compliance_flags (campos a verificar pelo Sentinel), estimated_read_time, canal_e_formato
- Formato JSON estruturado para consumo do Sentinel

## Trigger

Ativado pelo Maestro após Calibre Scorer classificar o lead como FIRE ou HOT e o dossiê estar com score de confiança >= 70. Re-trigger (reescritura) se Sentinel reprovar — max 1 reescritura automática antes de escalar para HITL. Trigger para mensagem de follow-up baseada em resposta analisada pelo Pulse Analyst.

## Knowledge base (o que o executor consulta)

- Biblioteca de playbooks de mensagem por vertical x sinal x cargo (agência, SaaS, indústria, serviços, imobiliário)
- Templates de sequência por tipo de trigger: hiring trigger, mudança de liderança, expansão de headcount, engajamento com conteúdo, cold outreach sem sinal
- Guia de voz da marca configurado no onboarding do cliente
- Biblioteca de mensagens vencedoras (com reply rate >15%) anonimizadas por segmento
- Regras de compliance LGPD para comunicação comercial no Brasil (opt-out, proibições, dados sensíveis)
- Regras de formato por canal: email (max 150 palavras cold), WhatsApp (max 3 blocos curtos, sem links no primeiro toque), LinkedIn (tom mais formal, conexão antes de InMail), voz (script de 45-60s, abertura de curiosidade, não pitch)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Dossiê de conta completo (Scout Profiler) com ângulos de personalização ranqueados).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pack de outreach completo: 2 variacoes (A/B) por canal ativo com subject line (email, max 50 chars), preview text, corp…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pack de outreach completo: 2 variacoes (A/B) por canal ativo com subject line (email, max 50 chars), preview text, corpo da mensagem, CTA unico e P.S
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

- **to:** Cadence Dispatcher
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
