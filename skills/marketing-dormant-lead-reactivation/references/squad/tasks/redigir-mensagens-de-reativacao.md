---
task: lazaroWriter()
responsavel: "Lázaro Writer"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Ficha de Arqueologia (Arqueologa) com ângulo falhado e histórico completo"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Ficha de Sinais Novos (Radar) com mudanças detectadas e ângulo de reativação sugerido"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Score e trilha definitiva (Oráculo Scorer)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Canal(is) disponível(is) para o lead (email verificado, WhatsApp, LinkedIn"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "baseado na qualidade dos dados)"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Guia de voz da marca do cliente (configurado no onboarding)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pack de reativação completo por lead: 2 variações (A/B) para cada mensagem na sequência da trilha atribuída"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Para sequência de 3 toques: 6 mensagens totais (3 x 2 variações)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Cada mensagem inclui: subject line (email, max 50 chars"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "nunca 'Re:' falso, nunca 'follow-up'), preview text, corpo (max 120 palavras para email de reativação"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "brevidade e respeito pelo tempo), CTA único (reunião de 20min / download de recurso / resposta simples dependendo da trilha), P.S"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "quando aplicável para toque pessoal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Lazaro apos Oraculo Scorer classificar o lead como RESSURGIR ou QUENTE e o score de qualidade dos dados ser >= 70. Re-trigger (reescritura) se Atena reprovar — max 1 reescritura automati…"
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

# Redigir Mensagens De Reativacao

**Task ID:** `lazaroWriter()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Redigir Mensagens De Reativacao |
| **status** | `pending` |
| **responsible_executor** | Lázaro Writer (Lázaro Writer — O Alquimista de Segunda Chance) |
| **execution_type** | `Agent` |
| **input** | 7 item(ns) |
| **output** | 8 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Redige as mensagens de reativacao para cada lead com base obrigatoriamente em tres elementos simultaneos: (1) o que NAO funcionou antes (angulo falhado identificado pela Arqueologa — jamais repetir), (2) o que mudou no contexto do lead (sinais do Radar — a mudanca e a abertura para re-engajamento), e (3) a trilha de reativacao atribuida pelo Oraculo Scorer (que dita o tom, a proposta de valor e o CTA). Gera 2 variacoes (A/B) por canal com angulos levemente diferentes. A mensagem de reativacao NUNCA soa como mais um cold outreach — ela referencia o contato anterior de forma respeitosa, reconhece o tempo passado, e apresenta uma razao genuina para a conversa se renovar agora (a mudanca de contexto detectada pelo Radar). Para sequencias de 3-5 toques: cada mensagem e construida sobre o silencio da anterior com escalada gradual de valor (mensagem 1: contextual e soft, mensagem 3: prova social, mensagem 5: fechamento de sequencia com porta aberta). Nunca envia — entrega ao critic Atena para validacao.

## Input

- Ficha de Arqueologia (Arqueologa) com ângulo falhado e histórico completo
- Ficha de Sinais Novos (Radar) com mudanças detectadas e ângulo de reativação sugerido
- Score e trilha definitiva (Oráculo Scorer)
- Canal(is) disponível(is) para o lead (email verificado, WhatsApp, LinkedIn
- baseado na qualidade dos dados)
- Guia de voz da marca do cliente (configurado no onboarding)
- Biblioteca de sequências de reativação por trilha e por archetype

## Output

- Pack de reativação completo por lead: 2 variações (A/B) para cada mensagem na sequência da trilha atribuída
- Para sequência de 3 toques: 6 mensagens totais (3 x 2 variações)
- Cada mensagem inclui: subject line (email, max 50 chars
- nunca 'Re:' falso, nunca 'follow-up'), preview text, corpo (max 120 palavras para email de reativação
- brevidade e respeito pelo tempo), CTA único (reunião de 20min / download de recurso / resposta simples dependendo da trilha), P.S
- quando aplicável para toque pessoal
- Metadados obrigatórios por draft: referência_ao_contato_anterior (como menciona o histórico), elemento_de_mudança_usado (qual sinal do Radar foi incorporado), ângulo_original_evitado (confirmação de que o ângulo falhado não está presente), canal_formato, compliance_flags
- Formato JSON para consumo do crític Atena

## Trigger

Ativado pelo Lazaro apos Oraculo Scorer classificar o lead como RESSURGIR ou QUENTE e o score de qualidade dos dados ser >= 70. Re-trigger (reescritura) se Atena reprovar — max 1 reescritura automatica com feedback especifico antes de escalar para HITL. Trigger para follow-up de resposta quando Echo Analyst identifica necessidade de reply (objecao ou interesse parcial).

## Knowledge base (o que o executor consulta)

- Biblioteca de templates de reativação por archetype x trilha x canal: Nunca Respondeu (reintrodução contextual), Engajou Sem Converter (retomar de onde parou com novo ângulo), Disse Não por Timing (reconhecer o compromisso, apresentar a mudança), Perdido para Concorrente (não mencionar concorrente, focar no que mudou), Fantasma Qualificado (assumir boa-fé, apresentar nova razão)
- Frameworks de narrativa de reativação: AIDA adaptado para reativação, PAS (Problema-Agitação-Solução) com o problema sendo a mudança de contexto
- Exemplos de mensagens de reativação vencedoras (reply rate > 12%) anonimizadas por segmento e archetype
- Regras LGPD para reativação: menção ao contato anterior e ao opt-out, não usar dados sensíveis que o lead não tornou públicos
- Política de 'última mensagem com graça': a mensagem 5 (fechamento de sequência) sempre encerra com porta aberta e opção de opt-out explícita

## Action Items

1. Confirmar o gatilho e carregar a entrada (Ficha de Arqueologia (Arqueologa) com ângulo falhado e histórico completo).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pack de reativação completo por lead: 2 variações (A/B) para cada mensagem na sequência da trilha atribuída) e persistir no artefato do squad.
4. Entregar ao critic Atena; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pack de reativação completo por lead: 2 variações (A/B) para cada mensagem na sequência da trilha atribuída
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

- **to:** Charon Dispatcher
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
