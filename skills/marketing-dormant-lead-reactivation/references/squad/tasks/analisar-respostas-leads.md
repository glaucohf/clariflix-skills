---
task: echoAnalyst()
responsavel: "Echo Analyst"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Respostas de email via webhook do ESP"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Mensagens de WhatsApp via WhatsApp Business API"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Transcrições de calls quando existirem"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Histórico completo do lead: ficha de arqueologia + sinais novos + qual mensagem (variação A ou B, posição na sequência) gerou a resposta"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "contexto crítico para análise"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Score e trilha do lead para contexto de interpretação"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Analise de resposta estruturada por lead: { lead_id, resposta_categoria (RESSUSCITADO / MORNO_NOVO / OBJECAO_TRATAVEL / TIMING_NOVO / DEFINITIVAMENTE_NAO / WRONG_PERSON), sentimento (positivo/neutro/negativo), objecao_detectada (quando aplicavel"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "texto exato + categoria: preco / timing / sem_autoridade / sem_necessidade / concorrente_atual), novo_timing_solicitado (data ou periodo quando aplicavel), coaching_note (texto para o vendedor: o que este lead sinalizou e qual e o melhor proximo passo), reply_necessario (booleano)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Se reply_necessario: draft de resposta gerado pelo Lazaro Writer e submetido ao critic Atena"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Notificacao IMEDIATA ao vendedor humano se categoria = RESSUSCITADO (lead quente nao pode esfriar)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Atualizacao do CRM com activity, nova categoria e nota de coaching"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "Relatorio semanal para o Lazaro e gestor: taxa de reativacao por trilha e por archetype, top 3 objecoes do periodo, variacoes A/B vencedoras por cluster, leads RESSUSCITADOS que progrediram para deal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook em tempo real para qualquer mensagem incoming. Processamento batch a cada 4 horas para respostas acumuladas de menor urgência. Trigger imediato se categoria = RESSUSCITADO (notificação urgent…"
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

# Analisar Respostas Leads

**Task ID:** `echoAnalyst()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Dormant Lead Reactivation

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Respostas Leads |
| **status** | `pending` |
| **responsible_executor** | Echo Analyst (Echo Analyst — O Intérprete do Eco) |
| **execution_type** | `Worker` |
| **input** | 6 item(ns) |
| **output** | 6 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Analisa todas as respostas recebidas dos leads nas sequencias de reativacao — emails replies, mensagens de WhatsApp, calls gravadas — e extrai o que o silencio ou a resposta revelam sobre o estado de prontidao do lead. Classifica cada resposta em uma das categorias de reativacao: RESSUSCITADO (interesse explicito, reuniao solicitada), MORNO_NOVO (interesse implicito, resposta positiva mas sem compromisso), OBJECAO_TRATAVEL (razao especifica identificada que o squad pode enderecar), TIMING_NOVO (pediu contato futuro com nova data), DEFINITIVAMENTE_NAO (opt-out claro ou rejeicao definitiva) e WRONG_PERSON (lead certo empresa errada ou mudou de papel). Para cada MORNO_NOVO e OBJECAO_TRATAVEL: gera sugestao de reply e alimenta o Lazaro Writer para construir resposta personalizada antes de encaminhar ao vendedor. Fecha o loop de aprendizado: patterns de resposta retroalimentam a biblioteca do Lazaro Writer e o modelo do Oraculo Scorer.

## Input

- Respostas de email via webhook do ESP
- Mensagens de WhatsApp via WhatsApp Business API
- Transcrições de calls quando existirem
- Histórico completo do lead: ficha de arqueologia + sinais novos + qual mensagem (variação A ou B, posição na sequência) gerou a resposta
- contexto crítico para análise
- Score e trilha do lead para contexto de interpretação

## Output

- Analise de resposta estruturada por lead: { lead_id, resposta_categoria (RESSUSCITADO / MORNO_NOVO / OBJECAO_TRATAVEL / TIMING_NOVO / DEFINITIVAMENTE_NAO / WRONG_PERSON), sentimento (positivo/neutro/negativo), objecao_detectada (quando aplicavel
- texto exato + categoria: preco / timing / sem_autoridade / sem_necessidade / concorrente_atual), novo_timing_solicitado (data ou periodo quando aplicavel), coaching_note (texto para o vendedor: o que este lead sinalizou e qual e o melhor proximo passo), reply_necessario (booleano)
- Se reply_necessario: draft de resposta gerado pelo Lazaro Writer e submetido ao critic Atena
- Notificacao IMEDIATA ao vendedor humano se categoria = RESSUSCITADO (lead quente nao pode esfriar)
- Atualizacao do CRM com activity, nova categoria e nota de coaching
- Relatorio semanal para o Lazaro e gestor: taxa de reativacao por trilha e por archetype, top 3 objecoes do periodo, variacoes A/B vencedoras por cluster, leads RESSUSCITADOS que progrediram para deal

## Trigger

Webhook em tempo real para qualquer mensagem incoming. Processamento batch a cada 4 horas para respostas acumuladas de menor urgência. Trigger imediato se categoria = RESSUSCITADO (notificação urgente ao vendedor). Trigger semanal para relatório de performance de reativação e retroalimentação do modelo. Trigger mensal para relatório executivo de ROI de reativação (pipeline reaberto, custo por lead reativado, comparativo vs novo lead).

## Knowledge base (o que o executor consulta)

- Dicionário de categorização de respostas de reativação: exemplos de texto para cada categoria e sub-categoria com exemplos em português brasileiro
- Scripts de resposta validados por objeção específica no contexto de reativação (diferente do outreach frio
- o lead já conhece a empresa)
- Criterios de handoff para vendedor humano: quais sinais de MORNO_NOVO justificam handoff imediato vs elaboração de mais um reply automático antes
- Histórico anonimizado de respostas de reativação que geraram deals fechados
- padrões linguísticos que indicam alta probabilidade de conversão
- Formato de relatório executivo de ROI de reativação para o gestor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Respostas de email via webhook do ESP).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Analise de resposta estruturada por lead: { lead_id, resposta_categoria (RESSUSCITADO / MORNO_NOVO / OBJECAO_TRATAVEL /…) e persistir no artefato do squad.
4. Entregar ao critic Atena; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Analise de resposta estruturada por lead: { lead_id, resposta_categoria (RESSUSCITADO / MORNO_NOVO / OBJECAO_TRATAVEL / TIMING_NOVO / DEFINITIVAMENTE_NAO / WRO…
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

- **to:** Atena
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
