---
task: memo()
responsavel: "Memo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Wargaming Report completo do Atlas + audiência-alvo do documento (board, investidor, parceiro, time interno) + formato preferido (memo narrativo, one-pager, deck outline, tabela executiva) + tom configurado (formal/direto/consultivo) + corpus do founder para alinhamento de voz (se integrado com Founder Clone Squad)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Documento executivo formatado pronto para revisão: { document_type, target_audience, executive_summary (200 palavras), decision_framing, scenario_summary (3 bullets), risk_matrix (simplificada), recommendation, next_steps, appendix_reference }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Versão draft salva em Notion para revisão obrigatória do founder antes de qualquer envio externo"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Atlas após Wargaming Report aprovado pelo founder (ou após aprovação do HITL gate). Ativado diretamente pelo founder via '/draft-memo [audiência] [decisão]'. NUNCA ativado automaticamente…"
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

# Sintetizar Wargaming Report

**Task ID:** `memo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sintetizar Wargaming Report |
| **status** | `pending` |
| **responsible_executor** | Memo (Memo — O Redator de Board Packs) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em transformar o Wargaming Report técnico em artefatos de comunicação executiva: board memos, investor updates, one-pagers de decisão para C-level e cartas de tese para parceiros. Recebe o output sintetizado do Atlas e produz documentos formatados para diferentes audiências — cada um no nível de detalhe e linguagem adequados ao receptor. Para board packs: estrutura com contexto da decisão, análise de cenários resumida, recomendação clara, riscos mapeados e próximos passos. Para memos a investidores: narrativa de tese + evidências + como a decisão fortalece a posição estratégica. Todos os documentos gerados são 100% source-grounded — cada claim rastreia a um achado do wargaming.

## Input

- Wargaming Report completo do Atlas + audiência-alvo do documento (board, investidor, parceiro, time interno) + formato preferido (memo narrativo, one-pager, deck outline, tabela executiva) + tom configurado (formal/direto/consultivo) + corpus do founder para alinhamento de voz (se integrado com Founder Clone Squad)

## Output

- Documento executivo formatado pronto para revisão: { document_type, target_audience, executive_summary (200 palavras), decision_framing, scenario_summary (3 bullets), risk_matrix (simplificada), recommendation, next_steps, appendix_reference }
- Versão draft salva em Notion para revisão obrigatória do founder antes de qualquer envio externo

## Trigger

Ativado por Atlas após Wargaming Report aprovado pelo founder (ou após aprovação do HITL gate). Ativado diretamente pelo founder via '/draft-memo [audiência] [decisão]'. NUNCA ativado automaticamente para envio externo — sempre requer aprovação explícita do founder (L3).

## Knowledge base (o que o executor consulta)

- Templates de board memo e investor update aprovados pelo founder
- Corpus de decisões e comunicações anteriores do founder (estilo, vocabulário, frameworks)
- Histórico de board packs e memos aprovados (para calibrar formato e nível de detalhe por audiência)
- Wargaming Reports históricos como referência de estrutura

## Action Items

1. Confirmar o gatilho e carregar a entrada (Wargaming Report completo do Atlas + audiência-alvo do documento (board, investidor, parceiro, time interno) + formato…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Documento executivo formatado pronto para revisão: { document_type, target_audience, executive_summary (200 palavras),…) e persistir no artefato do squad.
4. Entregar ao critic Ajax; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Documento executivo formatado pronto para revisão: { document_type, target_audience, executive_summary (200 palavras), decision_framing, scenario_summary (3 bu…
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

- **to:** Tripwire
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
