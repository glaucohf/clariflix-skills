---
task: haruki()
responsavel: "Haruki"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Cron diário 07h00 acionado pelo Orchestrator Orion + lista de canais configurados com credenciais MCP por canal + timestamp da última ingestão bem-sucedida por canal (para ingestão incremental) + schema de normalização versionado no Supabase"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Registros normalizados persistidos no Supabase (tabela: voc_raw_feedback) com campos: id, canal, data_criação, data_ingestão, account_id, segmento, texto_normalizado, score_numérico, idioma_detectado, qualidade_flag (OK / TEXTO_VAZIO / IDIOMA_OUTRO / DUPLICATA)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatório de ingestão em JSON para o Orchestrator Orion: {canal: string, registros_novos: int, registros_inválidos: int, anomalia_volume: bool, detalhes_anomalia: string}"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alerta imediato se queda > 50% no volume de qualquer canal vs baseline (possível falha de integração)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron job diário 07h00 pelo Orchestrator Orion para batch completo; webhook de integração quando canal envia evento em tempo real (NPS response crítico, ticket com keyword configurada); acionado manua…"
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

# Coletar E Normalizar Feedback

**Task ID:** `haruki()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz do Cliente – Análise de Sentimento e Tendências

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coletar E Normalizar Feedback |
| **status** | `pending` |
| **responsible_executor** | Haruki (Haruki — Coletor e Normalizador de Feedback Multicanal) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável pela ingestão diária de todos os canais de feedback configurados, normalização para schema unificado e validação de qualidade dos dados antes de qualquer análise. Conecta-se via MCP a: helpdesk (Zendesk/Intercom — tickets fechados nas últimas 24h com campos: texto do ticket, CSAT se respondido, tag de categoria existente, account_id, agent_id, tempo de resolução); NPS (Delighted/Typeform/Wootric — novos responses com score e verbatim); reviews públicos (G2/Capterra via API semanal — título, texto, rating, data, setor do reviewer); WhatsApp Business API (mensagens de atendimento das últimas 24h por conta — anonimizadas, sem PII); pesquisas de CSAT pós-onboarding se configuradas. Para cada registro: normaliza para schema unificado (strip de PII, encoding UTF-8, detecção de idioma, truncamento de textos > 2000 chars), calcula métricas de qualidade do campo texto (vazio, muito curto < 10 chars, idioma não PT-BR), deduplica usando hash do conteúdo + account_id + data. Persiste no Supabase com metadata de qualidade por registro. Gera relatório de ingestão: volume por canal, % de registros com texto válido, anomalias detectadas (queda ou pico de volume vs média dos 7 dias anteriores).

## Input

- Cron diário 07h00 acionado pelo Orchestrator Orion + lista de canais configurados com credenciais MCP por canal + timestamp da última ingestão bem-sucedida por canal (para ingestão incremental) + schema de normalização versionado no Supabase

## Output

- Registros normalizados persistidos no Supabase (tabela: voc_raw_feedback) com campos: id, canal, data_criação, data_ingestão, account_id, segmento, texto_normalizado, score_numérico, idioma_detectado, qualidade_flag (OK / TEXTO_VAZIO / IDIOMA_OUTRO / DUPLICATA)
- Relatório de ingestão em JSON para o Orchestrator Orion: {canal: string, registros_novos: int, registros_inválidos: int, anomalia_volume: bool, detalhes_anomalia: string}
- Alerta imediato se queda > 50% no volume de qualquer canal vs baseline (possível falha de integração)

## Trigger

Cron job diário 07h00 pelo Orchestrator Orion para batch completo; webhook de integração quando canal envia evento em tempo real (NPS response crítico, ticket com keyword configurada); acionado manualmente para re-ingestão de período específico em caso de falha

## Knowledge base (o que o executor consulta)

- Schema de normalização versionado com mapeamento de campos por canal (Zendesk ticket fields -> schema unificado, Delighted response -> schema unificado, etc.), lista de PII patterns para strip automático (CPF, email, telefone, nome próprio via NER PT-BR), lista de canais ativos com endpoint, credenciais e parâmetros de paginação, histórico de volume por canal por dia (últimos 30 dias) para detecção de anomalia, configuração de keywords para alerta em tempo real por canal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Cron diário 07h00 acionado pelo Orchestrator Orion + lista de canais configurados com credenciais MCP por canal + times…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Registros normalizados persistidos no Supabase (tabela: voc_raw_feedback) com campos: id, canal, data_criação, data_ing…) e persistir no artefato do squad.
4. Entregar ao critic Cassandra; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Registros normalizados persistidos no Supabase (tabela: voc_raw_feedback) com campos: id, canal, data_criação, data_ingestão, account_id, segmento, texto_norma…
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

- **to:** Yara
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
