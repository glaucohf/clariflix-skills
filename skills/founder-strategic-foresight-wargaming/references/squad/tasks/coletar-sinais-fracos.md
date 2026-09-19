---
task: pythia()
responsavel: "Pythia"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de monitoramento configurada pelo founder (concorrentes, setores, termos-chave, fontes prioritárias) + thresholds de urgência por tipo de sinal + integração com feeds de notícias, LinkedIn, Crunchbase, alertas de Google"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Modo on-demand: pergunta específica sobre sinal a investigar"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Signal Feed estruturado: { signal_id, signal_type (competitive/macro/regulatory/technology/customer), source_url, date, summary (100 palavras), relevance_score (1-10), urgency_flag (Rotina/Atenção/Urgente/Crítico), affected_scenarios[], affected_assumptions[], recommended_action }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Digest semanal consolidado com top-5 sinais"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alertas imediatos via Slack para sinais classificados como Crítico"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron diário automático para monitoramento de sinais de concorrentes top-3. Cron semanal para sinais macro e regulatórios. Ativado on-demand por Atlas quando wargaming precisa de dados atualizados sob…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Ajax antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificação de stakes, estimativa de custo de tokens). Para decisões classificadas como Alto (R$100k-500k) ou Crítico (R$500k+), aprovação explícita do founder é obrigatória antes de disparar workers. Inclui confirmação do escopo, dos concorrentes a simular e do nível de profundidade desejado."
    - "[ ] HITL: PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e founder recebe notificação urgente com evidências contrárias. O founder deve decidir: (a) revisar a tese antes de prosseguir, (b) validar a premissa com dado adicional, ou (c) aceitar o risco explicitamente e autorizar o prosseguimento. Sem aprovação explícita, Atlas não gera recomendação de GO."
    - "[ ] HITL: PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloqueia automaticamente a recomendação de GO e escalona para o founder. O relatório apresenta: narrativa do caminho de falha, premissas que o geram e opções de mitigação. O founder deve responder com ação concreta (mitigar, aceitar, desistir) antes de qualquer recomendação final."
    - "[ ] HITL: BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita do founder. Todo documento gerado vai primeiro para Notion como draft. Somente após founder marcar como aprovado o envio é permitido. Este gate é inviolável e não pode ser desabilitado."
    - "[ ] HITL: WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades financeiras ou decisões internas), o output é marcado como confidencial e apresentado ao founder antes de ser incluído em qualquer documento compartilhável. Dados de origem não-verificada são explicitamente rotulados."
---

# Coletar Sinais Fracos

**Task ID:** `pythia()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coletar Sinais Fracos |
| **status** | `pending` |
| **responsible_executor** | Pythia (Pythia — A Analista de Sinais Fracos) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em coleta e interpretação de sinais fracos do ambiente externo para alimentar wargamings e atualizar cenários proativamente. Opera em modo contínuo (cron diário) e on-demand. Monitora: job postings de concorrentes (sinalizam direção estratégica), mudanças de pricing e pricing pages, lançamentos de produto e mudanças em roadmaps públicos, movimentos regulatórios relevantes ao setor, sinais macro (taxa, câmbio, regulação, crédito) e micro (NPS público de concorrentes, reviews, churn signals). Não analisa — coleta, classifica por relevância e urgência, e alimenta Atlas e os workers especializados. Quando sinal urgente detectado, dispara notificação ao founder com contexto.

## Input

- Lista de monitoramento configurada pelo founder (concorrentes, setores, termos-chave, fontes prioritárias) + thresholds de urgência por tipo de sinal + integração com feeds de notícias, LinkedIn, Crunchbase, alertas de Google
- Modo on-demand: pergunta específica sobre sinal a investigar

## Output

- Signal Feed estruturado: { signal_id, signal_type (competitive/macro/regulatory/technology/customer), source_url, date, summary (100 palavras), relevance_score (1-10), urgency_flag (Rotina/Atenção/Urgente/Crítico), affected_scenarios[], affected_assumptions[], recommended_action }
- Digest semanal consolidado com top-5 sinais
- Alertas imediatos via Slack para sinais classificados como Crítico

## Trigger

Cron diário automático para monitoramento de sinais de concorrentes top-3. Cron semanal para sinais macro e regulatórios. Ativado on-demand por Atlas quando wargaming precisa de dados atualizados sobre adversário específico. Ativado pelo founder via '/monitor [novo concorrente ou termo]' para expandir watchlist.

## Knowledge base (o que o executor consulta)

- Watchlist configurada de concorrentes, termos e fontes (configurada no onboarding)
- APIs de monitoramento: Google Alerts, RSS feeds setoriais, LinkedIn (via MCP)
- Histórico de sinais coletados e sua materialização posterior (para calibrar relevância_score)
- Base de padrões de sinal por tipo de decisão estratégica do setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de monitoramento configurada pelo founder (concorrentes, setores, termos-chave, fontes prioritárias) + thresholds…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Signal Feed estruturado: { signal_id, signal_type (competitive/macro/regulatory/technology/customer), source_url, date,…) e persistir no artefato do squad.
4. Entregar ao critic Ajax; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Signal Feed estruturado: { signal_id, signal_type (competitive/macro/regulatory/technology/customer), source_url, date, summary (100 palavras), relevance_score…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Ajax registrado
- [ ] Gate HITL respeitado: INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Pr…
- [ ] Gate HITL respeitado: PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o war…
- [ ] Gate HITL respeitado: PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — INTAKE GATE — STAKES ALTO/CRÍTICO (L3): Antes de iniciar qualquer wargaming, Atlas apresenta o Protocolo de Intake ao founder (Árvore de Premissas, classificaç… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — PREMISSA FRÁGIL OU INVÁLIDA (L3): Quando Chisel classifica qualquer premissa crítica (criticality_rank >= 7) como Frágil ou Inválida, o wargaming pausa e found… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — PRE-MORTEM COM PROBABILIDADE DE FALHA > 30% (L3): Se Ajax identificar no Pre-Mortem um caminho de falha com probabilidade estimada acima de 30%, o squad bloque… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — BOARD MEMO E ENVIO EXTERNO (L3): Memo nunca envia qualquer documento para audiência externa (board, investidores, parceiros) sem revisão e aprovação explícita… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — WARGAMING DE CONCORRENTE ESPECÍFICO (L2): Quando Brutus simula um concorrente específico com dados sensíveis (ex: informações não-públicas sobre capacidades fi… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — DECISÃO DE MONITORAMENTO CONTÍNUO (L2): Após wargaming concluído, Atlas apresenta lista de tripwires sugeridos para aprovação do founder antes de ativar Tripwi… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Ajax | BLOQUEIA entrega |

## Handoff

- **to:** Memo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
