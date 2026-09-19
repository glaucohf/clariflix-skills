---
task: chisel()
responsavel: "Chisel"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Árvore de Premissas da decisão com premissas rankeadas por criticidade para a tese + dados históricos de mercado + outputs de Cassandra (premissas que variam por cenário) + critérios de classificação configurados pelo founder (o que é 'sólida' vs 'frágil' no contexto do cliente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Assumption Stress Report: { assumption_id, assumption_text, criticality_rank (1-10), breakeven_value, current_estimated_value, gap_to_breakeven (%), contrary_evidence[], supporting_evidence[], classification (Sólida/Frágil/Inválida), confidence_score (%), recommended_action (Aceitar/Validar antes de alocar/Reavaliar tese) }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Ranking das top-3 premissas mais arriscadas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Flag de HITL obrigatório para qualquer premissa crítica classificada como Frágil ou Inválida"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Atlas roteia em paralelo com Cassandra e Brutus. Ativado individualmente pelo founder via '/stress [premissa específica]' para análise pontual. Re-ativado por Atlas quando novo dado de mercado invali…"
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

# Destruir Premissas

**Task ID:** `chisel()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Strategic Foresight & Wargaming — Founder Decision Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Destruir Premissas |
| **status** | `pending` |
| **responsible_executor** | Chisel (Chisel — O Destruidor de Premissas) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em análise de sensibilidade e stress-testing de premissas. Opera como o 'advogado do diabo' sistemático da tese do founder. Para cada premissa da Árvore gerada no intake, executa: (1) análise de ponto de quebra — qual valor mínimo/máximo a variável precisa ter para a tese ainda funcionar? (2) busca ativa de evidências contrárias — existe dado público que contradiz esta premissa? (3) análise histórica de premissas similares em decisões passadas — quantas vezes esse tipo de premissa se provou incorreta? (4) classificação final: Sólida (evidência forte, ponto de quebra distante), Frágil (evidência mista ou ponto de quebra próximo), Inválida (evidência contrária dominante). Premissas classificadas como Frágeis ou Inválidas disparam alertas de HITL antes que a decisão prossiga.

## Input

- Árvore de Premissas da decisão com premissas rankeadas por criticidade para a tese + dados históricos de mercado + outputs de Cassandra (premissas que variam por cenário) + critérios de classificação configurados pelo founder (o que é 'sólida' vs 'frágil' no contexto do cliente)

## Output

- Assumption Stress Report: { assumption_id, assumption_text, criticality_rank (1-10), breakeven_value, current_estimated_value, gap_to_breakeven (%), contrary_evidence[], supporting_evidence[], classification (Sólida/Frágil/Inválida), confidence_score (%), recommended_action (Aceitar/Validar antes de alocar/Reavaliar tese) }
- Ranking das top-3 premissas mais arriscadas
- Flag de HITL obrigatório para qualquer premissa crítica classificada como Frágil ou Inválida

## Trigger

Atlas roteia em paralelo com Cassandra e Brutus. Ativado individualmente pelo founder via '/stress [premissa específica]' para análise pontual. Re-ativado por Atlas quando novo dado de mercado invalida uma premissa previamente classificada como Sólida (monitoramento contínuo).

## Knowledge base (o que o executor consulta)

- Histórico de decisões estratégicas e seus outcomes (base de calibração para frequência de erros por tipo de premissa)
- Dados de mercado do setor do cliente para verificação de premissas empíricas
- Biblioteca de 'premissas comuns que se mostraram falsas' por setor (heurísticas de calibração)
- Outputs de pesquisa do Deep Research Squad (se integrado)
- Fontes financeiras e de mercado para verificação quantitativa (faturamento setorial, taxas de crescimento históricas)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Árvore de Premissas da decisão com premissas rankeadas por criticidade para a tese + dados históricos de mercado + outp…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Assumption Stress Report: { assumption_id, assumption_text, criticality_rank (1-10), breakeven_value, current_estimated…) e persistir no artefato do squad.
4. Entregar ao critic Ajax; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Assumption Stress Report: { assumption_id, assumption_text, criticality_rank (1-10), breakeven_value, current_estimated_value, gap_to_breakeven (%), contrary_e…
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

- **to:** Pythia
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
