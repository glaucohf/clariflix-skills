---
task: cassandraVerificar()
responsavel: "Cassandra"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia lembrete; sem resposta em 8h, relatório é enviado com disclaimer 'pendente de revisão humana'"
    - "[ ] HITL: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para atendimento) antes de aparecer no backlog ativo; aprovação via bot no Slack com preview da task"
    - "[ ] HITL: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefing imediato e Atlas cria task de emergência; se falso positivo, threshold é ajustado automaticamente"
    - "[ ] HITL: Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-processar histórico; impacto estimado em registros afetados e apresentado antes da aprovação"
    - "[ ] HITL: Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; indica possível drift na linguagem dos clientes ou bug na ingestão"
---

# Verificar Saídas do Voz do Cliente

**Task ID:** `cassandraVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Voz do Cliente |
| **status** | `pending` |
| **responsible_executor** | Cassandra (Cassandra — Critic de Rastreabilidade e Qualidade de Insights) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Cassandra — Critic de Rastreabilidade e Qualidade de Insights — Valida o relatorio semanal do Lyra e os alertas do Rapid antes de qualquer entrega externa (Slack, Notion, ClickUp) em tres dimensoes criticas: (1) RASTREABILIDADE DE EVIDENCIAS — cada afirmacao do relatorio deve ter verbatim citado ou numero concreto que a suporte; afirmacoes como 'os clientes reclamam muito de X' sem volume especifico e contagem de mencoes sao bloqueadas com pedido de correcao; cada tendencia declarada deve ter pelo menos N mencoes acima do threshold configurado (protecao contra tendencias com volume insuficiente para ser estatisticamente significante); (2) QUALIDADE DA CLASSIFICACAO — amostra de 5-10% dos registros classificados pelo Yara e re-avaliada: tema atribuido faz sentido para o texto? Sentimento reflete o conteudo real? Registros de baixa confianca (< 0.6) incluidos no relatorio sao verificados manualmente; se taxa de erro na amostra > 15%, o relatorio e pausado para recalibracao da taxonomia; (3) RISCO DE VIES E HALLUCINATION — o relatorio nao deve amplificar feedback de clientes ruidosos ou de canais com baixo volume representativo; tendencias baseadas em < 15 mencoes sao marcadas como 'sinal fraco, monitorar' e nao como insight definitivo; recomendacoes de acao nao podem extrapolar o que os dados mostram (ex: nao afirmar 'clientes querem feature X' com base em 3 mencoes ambiguas). Aprova o relatorio com classificacao APROVADO / APROVADO COM RESSALVAS (lista de ajustes para proxima semana) / REPROVADO (relatorio reenviado para Lyra com feedback especifico, novo ciclo de 2h antes de re-entregar).

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Cassandra
- Critic de Rastreabilidade e Qualidade de Insights
- Valida o relatorio semanal do Lyra e os alertas do Rapid antes de qualquer entrega externa (Slack, Notion, ClickUp) em tres dimensoes criticas: (1) RASTREABILIDADE DE EVIDENCIAS
- cada afirmacao do relatorio deve ter verbatim citado ou numero concreto que a suporte
- afirmacoes como 'os clientes reclamam muito de X' sem volume especifico e contagem de mencoes sao bloqueadas com pedido de correcao
- cada tendencia declarada deve ter pelo menos N mencoes acima do threshold configurado (protecao contra tendencias com volume insuficiente para ser estatisticamente significante)
- (2) QUALIDADE DA CLASSIFICACAO
- amostra de 5-10% dos registros classificados pelo Yara e re-avaliada: tema atribuido faz sentido para o texto? Sentimento reflete o conteudo real? Registros de baixa confianca (< 0.6) incluidos no relatorio sao verificados manualmente
- se taxa de erro na amostra > 15%, o relatorio e pausado para recalibracao da taxonomia
- (3) RISCO DE VIES E HALLUCINATION
- o relatorio nao deve amplificar feedback de clientes ruidosos ou de canais com baixo volume representativo
- tendencias baseadas em < 15 mencoes sao marcadas como 'sinal fraco, monitorar' e nao como insight definitivo
- recomendacoes de acao nao podem extrapolar o que os dados mostram (ex: nao afirmar 'clientes querem feature X' com base em 3 mencoes ambiguas)
- Aprova o relatorio com classificacao APROVADO / APROVADO COM RESSALVAS (lista de ajustes para proxima semana) / REPROVADO (relatorio reenviado para Lyra com feedback especifico, novo ciclo de 2h antes de re-entregar)

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Orion para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação e…
- [ ] Gate HITL respeitado: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto…
- [ ] Gate HITL respeitado: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmad…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para at… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefin… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-proce… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; in… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Publicacao de insight que menciona concorrente especifico por nome — Lyra sinaliza e o Head de CS aprova antes de distribuir para evitar vazamento de informaca… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Re-calibração de thresholds de alerta após detecção de falsos positivos recorrentes — o Rapid documenta a sugestão de ajuste e aguarda aprovação do PM ou Head… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de canal com volume insuficiente para análise estatística identificado pós-Discovery — Haruki notifica e aguarda decisão humana sobre incluir ou exclu… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Cassandra | BLOQUEIA entrega |

## Handoff

- **to:** Orion
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
