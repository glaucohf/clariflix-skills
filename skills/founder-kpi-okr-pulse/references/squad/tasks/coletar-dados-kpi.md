---
task: pulsar()
responsavel: "Pulsar"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Catálogo de métricas do cliente (lista de KPIs com: nome, fórmula, fonte de dados, granularidade, owner) + credenciais de acesso via MCP servers + janela temporal de coleta (default: semana anterior + YTD + rolling 12 meses)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Snapshot estruturado: { kpi_name, current_value, period, source_system, extraction_timestamp, calculation_method, data_quality_flag (OK/PARTIAL/FAILED) }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatório de falhas de coleta por sistema"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Tempo total de coleta por fonte"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparado por Atlas no início de cada ciclo semanal (cron). Também ativado por Atlas em queries ad-hoc quando founder pede KPI específico. Re-disparado automaticamente se dado de uma fonte chegar com…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Véra 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estratégico Alto (ex: OKR de receita principal) — Argo retém a hipótese e Atlas notifica o founder: 'Detectei desvio em [KR] mas não tenho dados suficientes para confirmar a causa. Possível hipótese: [X]. Você pode me dar contexto adicional?' O founder responde e Argo reprocessa com o contexto fornecido."
    - "[ ] HITL: RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação financeira' (ex: cancelar contrato, cortar budget de campanha, demitir fornecedor, alterar pricing) sem aprovação explícita do founder. Essas recomendações chegam como rascunho com flag APPROVAL_REQUIRED — founder aprova, rejeita ou modifica antes de qualquer task ser criada."
    - "[ ] HITL: ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de integração, dado zerado, timeout), Atlas pausa o ciclo e envia alerta imediato: 'Pulse desta semana comprometido — [N] KPIs sem dados confiáveis de [sistema X]. Envio relatório parcial ou aguardo resolução?' Founder decide antes do relatório ser publicado."
    - "[ ] HITL: CLONE SIGMA PUBLICAÇÃO EXTERNA (L1→L3): Sigma pode gerar e entregar o Pulse no Slack e Notion de uso interno do founder sem aprovação. Se o founder solicitar versão do Pulse para compartilhar com time, board ou investidores — Sigma gera o draft mas entrega APENAS ao founder para revisão antes de qualquer distribuição externa."
    - "[ ] HITL: RECALIBRAÇÃO DE TARGET DE OKR (L2): Quando Kalinda detecta que um OKR está >120% da trajetória esperada por 2 semanas consecutivas (super-performance) ou que a tendência matemática torna o target inalcançável mesmo com ação corretiva — Atlas sinaliza ao founder para deliberar sobre recalibração de target. Nunca recalibra automaticamente. Founder decide em reunião de check-in mensal."
---

# Coletar Dados Kpi

**Task ID:** `pulsar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KPI/OKR Pulse — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Coletar Dados Kpi |
| **status** | `pending` |
| **responsible_executor** | Pulsar (Pulsar — O Coletor de Dados) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em extração e normalização de dados de múltiplas fontes heterogêneas. Pulsar conecta via MCP servers a cada sistema integrado (CRM, ERP/financeiro, plataforma de ads, produto/analytics, planilhas, BI) e extrai os valores atuais de cada KPI do catálogo. Normaliza unidades, moedas e granularidades (diário, semanal, mensal) para uma camada semântica única. Detecta e reporta falhas de coleta por fonte (timeout, credencial expirada, dado inconsistente) para que Atlas decida se o relatório prossegue com dado parcial ou aguarda. Garante que cada KPI coletado tenha metadata de origem (fonte, timestamp de extração, método de cálculo) para rastreabilidade.

## Input

- Catálogo de métricas do cliente (lista de KPIs com: nome, fórmula, fonte de dados, granularidade, owner) + credenciais de acesso via MCP servers + janela temporal de coleta (default: semana anterior + YTD + rolling 12 meses)

## Output

- Snapshot estruturado: { kpi_name, current_value, period, source_system, extraction_timestamp, calculation_method, data_quality_flag (OK/PARTIAL/FAILED) }
- Relatório de falhas de coleta por sistema
- Tempo total de coleta por fonte

## Trigger

Disparado por Atlas no início de cada ciclo semanal (cron). Também ativado por Atlas em queries ad-hoc quando founder pede KPI específico. Re-disparado automaticamente se dado de uma fonte chegar com atraso (retry com backoff de 15 min, máximo 3 tentativas).

## Knowledge base (o que o executor consulta)

- Catálogo de métricas do cliente (configurado no onboarding e atualizado pelo founder via /add-kpi)
- Credenciais de acesso a sistemas via MCP secrets
- Mapeamento de campo por sistema (ex: 'Receita MRR' = campo X no HubSpot + tabela Y no financeiro)
- Histórico de falhas de coleta por fonte (para priorizar alertas recorrentes)
- Regras de normalização de dados (moeda, timezone, deduplicação)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Catálogo de métricas do cliente (lista de KPIs com: nome, fórmula, fonte de dados, granularidade, owner) + credenciais…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Snapshot estruturado: { kpi_name, current_value, period, source_system, extraction_timestamp, calculation_method, data_…) e persistir no artefato do squad.
4. Entregar ao critic Véra 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Snapshot estruturado: { kpi_name, current_value, period, source_system, extraction_timestamp, calculation_method, data_quality_flag (OK/PARTIAL/FAILED) }
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Véra 2 registrado
- [ ] Gate HITL respeitado: DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estrat…
- [ ] Gate HITL respeitado: RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação fina…
- [ ] Gate HITL respeitado: ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de i…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — DIAGNÓSTICO DE BAIXA CONFIANÇA (L3): Quando Véra classifica diagnóstico de causa-raiz como confiança Baixa e o KR associado tem peso estratégico Alto (ex: OKR… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — RECOMENDAÇÃO COM IMPACTO FINANCEIRO DIRETO (L3): Rex nunca cria task automática no ClickUp para recomendações classificadas como 'ação financeira' (ex: cancela… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — ALERTA DE DADOS COMPROMETIDOS (L2→L3): Se Véra detectar que >30% dos KPIs de um OKR crítico vieram com data_quality_flag=FAILED (falha de integração, dado zera… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — CLONE SIGMA PUBLICAÇÃO EXTERNA (L1→L3): Sigma pode gerar e entregar o Pulse no Slack e Notion de uso interno do founder sem aprovação. Se o founder solicitar v… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — RECALIBRAÇÃO DE TARGET DE OKR (L2): Quando Kalinda detecta que um OKR está >120% da trajetória esperada por 2 semanas consecutivas (super-performance) ou que a… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — ONBOARDING DE NOVO KPI/SISTEMA (L1): Ao adicionar nova fonte de dados ao catálogo, o primeiro ciclo de coleta opera em modo 'dry-run' — Pulsar coleta e Kalinda… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Véra 2 | BLOQUEIA entrega |

## Handoff

- **to:** Kalinda
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
