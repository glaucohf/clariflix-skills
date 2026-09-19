---
task: argo()
responsavel: "Argo"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "KR desviado com metadata (desvio %, trend, owner) do Kalinda + dados brutos de todos os drivers do KR (coletados pelo Pulsar) + log de eventos do período (campanhas, deploys, mudanças de equipe"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "extraído do ClickUp/Notion) + dados históricos de 12 meses para comparação"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Diagnóstico de causa-raiz estruturado por KR: { kr_name, root_cause_hypothesis, cause_category, evidence_data (dados numéricos que suportam a hipótese), confidence_level (Alto/Médio/Baixo), contributing_factors (fatores secundários), anomaly_vs_trend (Anomalia Pontual / Tendência Estrutural), time_to_impact (quando o efeito é esperado reverter se causa for endereçada) }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Máximo 3 hipóteses de causa por KR, rankeadas por confiança"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Atlas para cada KR com status Amarelo ou Vermelho na análise do Kalinda. Quantidade de KRs em análise simultânea limitada a 5 para controle de custo de tokens. KRs Vermelhos recebem prior…"
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

# Analisar Causa-Raiz

**Task ID:** `argo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KPI/OKR Pulse — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Causa-Raiz |
| **status** | `pending` |
| **responsible_executor** | Argo (Argo — O Detetive de Causa-Raiz) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em análise de causa-raiz de desvios de KPI/OKR. Para cada desvio classificado como Amarelo ou Vermelho pelo Kalinda, Argo executa drill-down multi-camada: (1) decompõe o KR desviado em seus drivers primários usando árvore de métricas (ex: Receita = Volume × Ticket Médio × Conversão), (2) identifica qual driver específico é o responsável pelo desvio, (3) correlaciona temporalmente com eventos registrados (campanhas iniciadas/encerradas, lançamentos, mudanças de produto, saídas de equipe), (4) compara com períodos equivalentes históricos para distinguir anomalia pontual de tendência, (5) classifica a categoria de causa (Operacional/Mercado/Produto/Financeiro/Pessoas) com evidência quantitativa. Argo não especula — toda hipótese de causa deve ser suportada por dado ou correlação temporal mensurável.

## Input

- KR desviado com metadata (desvio %, trend, owner) do Kalinda + dados brutos de todos os drivers do KR (coletados pelo Pulsar) + log de eventos do período (campanhas, deploys, mudanças de equipe
- extraído do ClickUp/Notion) + dados históricos de 12 meses para comparação

## Output

- Diagnóstico de causa-raiz estruturado por KR: { kr_name, root_cause_hypothesis, cause_category, evidence_data (dados numéricos que suportam a hipótese), confidence_level (Alto/Médio/Baixo), contributing_factors (fatores secundários), anomaly_vs_trend (Anomalia Pontual / Tendência Estrutural), time_to_impact (quando o efeito é esperado reverter se causa for endereçada) }
- Máximo 3 hipóteses de causa por KR, rankeadas por confiança

## Trigger

Ativado por Atlas para cada KR com status Amarelo ou Vermelho na análise do Kalinda. Quantidade de KRs em análise simultânea limitada a 5 para controle de custo de tokens. KRs Vermelhos recebem prioridade absoluta. Também ativado por query ad-hoc do founder: '/diagnose [KPI_name]'.

## Knowledge base (o que o executor consulta)

- Árvore de métricas do cliente (mapa de drivers primários e secundários de cada KR
- configurado no onboarding)
- Dados históricos de 12 meses de todos os KPIs (Vector DB ou time-series DB)
- Log de eventos de negócio (campanhas, lançamentos, contratações, mudanças estruturais
- extraído do ClickUp)
- Benchmarks setoriais para classificação de desvio como anômalo
- Heurísticas de causa-raiz por categoria (ex: 'se Churn sobe e CSAT cai no mesmo período → provável causa de produto/suporte')

## Action Items

1. Confirmar o gatilho e carregar a entrada (KR desviado com metadata (desvio %, trend, owner) do Kalinda + dados brutos de todos os drivers do KR (coletados pelo P…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Diagnóstico de causa-raiz estruturado por KR: { kr_name, root_cause_hypothesis, cause_category, evidence_data (dados nu…) e persistir no artefato do squad.
4. Entregar ao critic Véra 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Diagnóstico de causa-raiz estruturado por KR: { kr_name, root_cause_hypothesis, cause_category, evidence_data (dados numéricos que suportam a hipótese), confid…
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

- **to:** Rex
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
