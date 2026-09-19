---
task: rex()
responsavel: "Rex"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Diagnóstico de causa-raiz do Argo (validado pela Véra) + catálogo de alavancas do cliente (playbook de ações por categoria de causa"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "configurado no onboarding e enriquecido ao longo do tempo) + contexto estratégico atual do founder (prioridades do trimestre, restrições de capacidade, budget disponível)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Bloco de recomendações por KR desviado: { recommendation_title, logic_chain, owner, expected_lead_time, confirmation_kpi, effort_score (1-5), impact_score (1-5), urgency_score (1-5), priority_rank, clickup_task_id (criado automaticamente) }"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Seção de 'Quick Wins' (impacto alto, esforço baixo) sempre em destaque"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado por Atlas após Véra validar diagnóstico do Argo. Nunca ativado com diagnóstico não validado. Também ativado por query ad-hoc: '/recommend [KR_name]'. Re-executa ao final do mês para gerar pla…"
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

# Gerar Recomendações Acionáveis

**Task ID:** `rex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KPI/OKR Pulse — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Recomendações Acionáveis |
| **status** | `pending` |
| **responsible_executor** | Rex (Rex — O Motor de Recomendações) |
| **execution_type** | `Agent` |
| **input** | 2 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em geração de recomendações acionáveis baseadas em diagnóstico de causa-raiz. Para cada causa identificada pelo Argo (e validada pela Véra), Rex gera 1-3 recomendações concretas: qual alavanca ativar (ação específica, não genérica), quem é o owner recomendado, qual o prazo esperado para ver efeito (lead time da alavanca), qual KPI de confirmação monitorar para saber se funcionou, e qual é o custo/esforço estimado da ação. Rex não recomenda sem lógica explícita — cada recomendação vem com a chain of reasoning: causa → mecanismo → ação → efeito esperado. Ranqueia recomendações por matriz impacto × esforço × urgência. Cria automaticamente as tasks no ClickUp com os campos preenchidos (título, owner, prazo, descrição da lógica).

## Input

- Diagnóstico de causa-raiz do Argo (validado pela Véra) + catálogo de alavancas do cliente (playbook de ações por categoria de causa
- configurado no onboarding e enriquecido ao longo do tempo) + contexto estratégico atual do founder (prioridades do trimestre, restrições de capacidade, budget disponível)

## Output

- Bloco de recomendações por KR desviado: { recommendation_title, logic_chain, owner, expected_lead_time, confirmation_kpi, effort_score (1-5), impact_score (1-5), urgency_score (1-5), priority_rank, clickup_task_id (criado automaticamente) }
- Seção de 'Quick Wins' (impacto alto, esforço baixo) sempre em destaque

## Trigger

Ativado por Atlas após Véra validar diagnóstico do Argo. Nunca ativado com diagnóstico não validado. Também ativado por query ad-hoc: '/recommend [KR_name]'. Re-executa ao final do mês para gerar plano de aceleração de encerramento de trimestre.

## Knowledge base (o que o executor consulta)

- Playbook de alavancas por categoria de causa (construído no onboarding e enriquecido com o histórico de recomendações aceitas/rejeitadas pelo founder)
- Contexto estratégico do trimestre (OKRs prioritários, restrições, budget
- extraído do Notion)
- Histórico de recomendações anteriores com outcome documentado (o que funcionou e o que não funcionou para este cliente)
- Frameworks de priorização: ICE Score (Impact/Confidence/Ease), RICE, matriz 2x2

## Action Items

1. Confirmar o gatilho e carregar a entrada (Diagnóstico de causa-raiz do Argo (validado pela Véra) + catálogo de alavancas do cliente (playbook de ações por catego…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Bloco de recomendações por KR desviado: { recommendation_title, logic_chain, owner, expected_lead_time, confirmation_kp…) e persistir no artefato do squad.
4. Entregar ao critic Véra 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Bloco de recomendações por KR desviado: { recommendation_title, logic_chain, owner, expected_lead_time, confirmation_kpi, effort_score (1-5), impact_score (1-5…
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

- **to:** Sigma
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
