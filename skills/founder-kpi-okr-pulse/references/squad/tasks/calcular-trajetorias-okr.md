---
task: kalinda()
responsavel: "Kalinda"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Snapshot de KPIs do Pulsar + OKRs e Key Results do trimestre (do Notion/ClickUp) com targets, pesos e owners + dados históricos dos últimos 4 trimestres para calibração de sazonalidade + data atual no ciclo (semana N de Q total)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Painel de status de OKRs: { okr_name, kr_name, owner, target_value, current_value, expected_trajectory_value, deviation_pct, status (Verde/Amarelo/Vermelho), trend (Acelerando/Estável/Desacelerando), priority_score }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Lista de desvios acima do threshold para drill-down pelo Argo"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Lista de OKRs super-performando para revisão de target"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Atlas após Pulsar concluir coleta com sucesso (ou partial com flag). Também ativado quando founder cria ou atualiza OKR via comando '/update-okr'. Re-executa ao final do mês para projeção…"
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

# Calcular Trajetórias Okr

**Task ID:** `kalinda()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KPI/OKR Pulse — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Trajetórias Okr |
| **status** | `pending` |
| **responsible_executor** | Kalinda (Kalinda — A Estrategista de OKR) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em mapeamento de OKRs, cálculo de trajetórias e detecção de desvios. Kalinda carrega os OKRs e Key Results do trimestre do Notion/ClickUp, calcula para cada KR a trajetória esperada de progresso (linear + ajustada por sazonalidade histórica se disponível), compara com o valor atual coletado pelo Pulsar, calcula o desvio percentual e classifica o status (Verde: >=90% da trajetória esperada; Amarelo: 70-89%; Vermelho: <70%). Prioriza desvios por impacto estratégico (OKRs de maior peso recebem prioridade de análise). Identifica também OKRs que estão super-performando (>120% da trajetória) — sinal de recalibração ou oportunidade.

## Input

- Snapshot de KPIs do Pulsar + OKRs e Key Results do trimestre (do Notion/ClickUp) com targets, pesos e owners + dados históricos dos últimos 4 trimestres para calibração de sazonalidade + data atual no ciclo (semana N de Q total)

## Output

- Painel de status de OKRs: { okr_name, kr_name, owner, target_value, current_value, expected_trajectory_value, deviation_pct, status (Verde/Amarelo/Vermelho), trend (Acelerando/Estável/Desacelerando), priority_score }
- Lista de desvios acima do threshold para drill-down pelo Argo
- Lista de OKRs super-performando para revisão de target

## Trigger

Ativado por Atlas após Pulsar concluir coleta com sucesso (ou partial com flag). Também ativado quando founder cria ou atualiza OKR via comando '/update-okr'. Re-executa ao final do mês para projeção de encerramento do trimestre (cenário base, otimista e pessimista).

## Knowledge base (o que o executor consulta)

- OKRs e Key Results do trimestre atual (Notion/ClickUp)
- Histórico de OKRs dos últimos 4 trimestres (para análise de padrão e sazonalidade)
- Pesos e dependências entre OKRs (mapa de impacto)
- Catálogo de KPIs vinculados a cada KR
- Dados de benchmark setorial para contexto de desvio (ex: 'churn de 3% está dentro do benchmark para SaaS B2B?')

## Action Items

1. Confirmar o gatilho e carregar a entrada (Snapshot de KPIs do Pulsar + OKRs e Key Results do trimestre (do Notion/ClickUp) com targets, pesos e owners + dados hi…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Painel de status de OKRs: { okr_name, kr_name, owner, target_value, current_value, expected_trajectory_value, deviation…) e persistir no artefato do squad.
4. Entregar ao critic Véra 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Painel de status de OKRs: { okr_name, kr_name, owner, target_value, current_value, expected_trajectory_value, deviation_pct, status (Verde/Amarelo/Vermelho), t…
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

- **to:** Argo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
