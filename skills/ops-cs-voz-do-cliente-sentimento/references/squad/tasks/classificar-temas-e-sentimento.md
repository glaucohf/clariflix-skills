---
task: yara()
responsavel: "Yara"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Registros do dia com qualidade_flag = OK da tabela voc_raw_feedback (Supabase) + taxonomia de temas versionada com exemplos por têma (carregada do Supabase) + modelo de sentimento PT-BR configurado + lista de entidades de negócio (features, integrações, concorrentes) para NER"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Registros enriquecidos persistidos no Supabase (tabela: voc_analyzed_feedback) com campos adicionais: sentimento_score (float), sentimento_categoria (POSITIVO/NEUTRO/NEGATIVO), sentimento_intensidade (string), temas_primarios (array de 1-3 tema IDs), subtemas (array), entidades_extraidas (JSON: {features, integracoes, concorrentes, erros}), flag_churn (bool), flag_concorrente (bool + nome), flag_bug (bool), flag_sugestao (bool), confianca_classificacao (float 0-1)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Metricas de processamento para o Orchestrator: volume processado, distribuicao de sentimento, top-5 temas do dia, registros com baixa confianca (< 0.6) para revisao amostral"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orchestrator Orion após Haruki confirmar conclusão da ingestão diária (evento no Supabase: vóc_ingestion_completed); acionado para re-processamento quando PM ou Head de CS atualiza a ta…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Cassandra antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do relatório semanal antes de distribuição — PM ou Head de CS recebe o relatório no Slack com botão de aprovação; sem aprovação em 4h, sistema envia lembrete; sem resposta em 8h, relatório é enviado com disclaimer 'pendente de revisão humana'"
    - "[ ] HITL: Criação de tasks no ClickUp pelo Atlas — qualquer task gerada automaticamente pelo squad requer confirmação do responsável (PM para produto, Head de CS para atendimento) antes de aparecer no backlog ativo; aprovação via bot no Slack com preview da task"
    - "[ ] HITL: Alertas de emergência classificados como CRÍTICO — Rapid envia para canal Slack com botão 'Confirmar Alerta / Falso Positivo'; se confirmado, Lyra gera briefing imediato e Atlas cria task de emergência; se falso positivo, threshold é ajustado automaticamente"
    - "[ ] HITL: Atualização de taxonomia de temas — qualquer alteração nos 15-25 temas da taxonomia (adição, remoção, renomeação) requer aprovação do PM antes de Yara re-processar histórico; impacto estimado em registros afetados e apresentado antes da aprovação"
    - "[ ] HITL: Relatório reprovado pelo Critic Cassandra após 2 iterações — escalonado para analista humano revisar os dados de entrada e a taxonomia antes de reprocessar; indica possível drift na linguagem dos clientes ou bug na ingestão"
---

# Classificar Temas E Sentimento

**Task ID:** `yara()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Classificar Temas E Sentimento |
| **status** | `pending` |
| **responsible_executor** | Yara (Yara — Analista de Sentimento e Classificadora de Temas) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Processa os registros ingeridos pelo Haruki e enriquece cada um com: (1) SENTIMENTO — score de -1.0 a +1.0 usando modelo de sentimento PT-BR fine-tuned para linguagem B2B; categoriza em POSITIVO (> 0.3), NEUTRO (-0.3 a 0.3) e NEGATIVO (< -0.3); identifica intensidade emocional (frustrado, indignado, satisfeito, entusiasmado) e presenca de linguagem de urgencia ('urgente', 'bloqueado', 'nao consigo'); (2) TEMAS — classifica o registro na taxonomia validada no Deep Dive (lista de 15-25 temas macro); um registro pode ter ate 3 temas primarios; usa classificacao hierarquica: tema macro > subtema > intencao especifica; (3) ENTIDADES — extrai entidades relevantes: nome de feature/modulo mencionado, nome de integracao citada, nome de concorrente, tipo de erro descrito, etapa do processo referenciada; (4) INDICADORES DE ACAO — flags binarios: mencao_de_churn (bool), comparacao_com_concorrente (bool + nome do concorrente), bug_reportado (bool), sugestao_de_produto (bool), elogio_especifico (bool). Processa em batch os registros do dia e re-processa amostras historicas quando taxonomia e atualizada.

## Input

- Registros do dia com qualidade_flag = OK da tabela voc_raw_feedback (Supabase) + taxonomia de temas versionada com exemplos por têma (carregada do Supabase) + modelo de sentimento PT-BR configurado + lista de entidades de negócio (features, integrações, concorrentes) para NER

## Output

- Registros enriquecidos persistidos no Supabase (tabela: voc_analyzed_feedback) com campos adicionais: sentimento_score (float), sentimento_categoria (POSITIVO/NEUTRO/NEGATIVO), sentimento_intensidade (string), temas_primarios (array de 1-3 tema IDs), subtemas (array), entidades_extraidas (JSON: {features, integracoes, concorrentes, erros}), flag_churn (bool), flag_concorrente (bool + nome), flag_bug (bool), flag_sugestao (bool), confianca_classificacao (float 0-1)
- Metricas de processamento para o Orchestrator: volume processado, distribuicao de sentimento, top-5 temas do dia, registros com baixa confianca (< 0.6) para revisao amostral

## Trigger

Acionado pelo Orchestrator Orion após Haruki confirmar conclusão da ingestão diária (evento no Supabase: vóc_ingestion_completed); acionado para re-processamento quando PM ou Head de CS atualiza a taxonomia via painel de configuração; acionado para processamento de amostra em novo canal antes de colocar em produção

## Knowledge base (o que o executor consulta)

- Taxonomia de temas versionada com 15-25 têmas macro, definições e 5-10 exemplos por têma (construída no Deep Dive, versionada no Supabase), modelo de sentimento PT-BR B2B fine-tuned com exemplos de feedback de SaaS (ex: 'o sistema trava' = crítico mesmo sem palavras fortes), lista de features e módulos do produto com aliases e nomes informais como clientes mencionam, lista de concorrentes com aliases, dicionário de intensificadores e atenuadores PT-BR para calibrar sentimento, exemplos de linguagem de churn iminênte em PT-BR, thresholds de confiança para cada têma (têmas com alta ambiguidade tem threshold maior)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Registros do dia com qualidade_flag = OK da tabela voc_raw_feedback (Supabase) + taxonomia de temas versionada com exem…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Registros enriquecidos persistidos no Supabase (tabela: voc_analyzed_feedback) com campos adicionais: sentimento_score…) e persistir no artefato do squad.
4. Entregar ao critic Cassandra; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Registros enriquecidos persistidos no Supabase (tabela: voc_analyzed_feedback) com campos adicionais: sentimento_score (float), sentimento_categoria (POSITIVO/…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Cassandra registrado
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

- **to:** Orion 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
