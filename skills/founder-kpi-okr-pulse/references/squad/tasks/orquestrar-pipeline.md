---
task: atlasPipeline()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pulse Report Semanal"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "entregue toda segunda-feira via Slack (resumo em 5 bullets acionáveis) + Notion (relatório completo permanente) + ClickUp (tasks de recomendação já criadas)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Estrutura do relatório completo: (1) Semáforo Geral do Portfólio de OKRs (Verde/Amarelo/Vermelho por OKR, % de progresso vs"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "trajetória esperada)"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(2) Desvios da Semana"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "para cada KR desviado: valor atual vs"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Atlas é o orquestrador central do squad KPI/OKR Pulse. Opera em dois modos: (1) PULSE SEMANAL — disparo automático via cron que coordena coleta, análise e entrega do relatório completo; (2) QUERY AVU…"
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

# Orquestrar Pipeline do KPI/OKR Pulse

**Task ID:** `atlasPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** KPI/OKR Pulse — Founder Intelligence Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do KPI/OKR Pulse |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — O Controlador de Performance) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 18 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Atlas é o orquestrador central do squad KPI/OKR Pulse. Opera em dois modos: (1) PULSE SEMANAL — disparo automático via cron que coordena coleta, análise e entrega do relatório completo; (2) QUERY AVULSA — responde perguntas ad-hoc do founder tipo 'como está minha Receita vs. meta?' ou 'por que o Churn subiu esse mês?'. Atlas mantém o catálogo de métricas do cliente (lista de KPIs, owners, fontes de dados, targets, fórmulas de cálculo), gerencia o estado do ciclo semanal via LangGraph, roteia KPIs desviados para análise de causa-raiz no Argo, aguarda validação da Véra antes da síntese, e entrega o Pulse Report via integrações configuradas. Nunca entrega análise sem passar pelo ciclo completo Discovery → Deep Dive → Framework. Responsável pelo SLA de entrega (target: relatório completo em <90 min após coleta iniciar).

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pulse Report Semanal
- entregue toda segunda-feira via Slack (resumo em 5 bullets acionáveis) + Notion (relatório completo permanente) + ClickUp (tasks de recomendação já criadas)
- Estrutura do relatório completo: (1) Semáforo Geral do Portfólio de OKRs (Verde/Amarelo/Vermelho por OKR, % de progresso vs
- trajetória esperada)
- (2) Desvios da Semana
- para cada KR desviado: valor atual vs
- esperado, desvio percentual, diagnóstico de causa-raiz com evidência numérica, categoria (Operacional/Mercado/Produto/Financeiro/Pessoas) e nível de confiança do diagnóstico
- (3) Recomendações Acionáveis
- 1-3 recomendações por KR desviado com lógica explícita, owner sugerido, prazo esperado de efeito e KPI de confirmação
- (4) Quick Wins
- top 3 ações de alto impacto e baixo esforço da semana
- (5) Tendências de Médio Prazo
- projeção de encerramento do trimestre em cenário base, otimista e pessimista
- (6) Log de Dados
- quais sistemas foram coletados, quais falharam, qualidade geral dos dados desta semana
- (7) Pulse em 5 Bullets (Sigma)
- versão ultra-condensada para consumo imediato
- Audit trail completo (timestamp de cada etapa, custo de tokens, agentes acionados) armazenado no Langfuse

## Trigger

Atlas é o orquestrador central do squad KPI/OKR Pulse. Opera em dois modos: (1) PULSE SEMANAL — disparo automático via cron que coordena coleta, análise e entrega do relatório completo; (2) QUERY AVULSA — responde perguntas ad-hoc do founder tipo 'como está minha Receita vs. meta?' ou 'por que o Churn subiu esse mês?'. Atlas mantém o catálogo de métricas do cliente (lista de KPIs, owners, fontes de dados, targets, fórmulas de cálculo), gerencia o estado do ciclo semanal via LangGraph, roteia KPIs desviados para análise de causa-raiz no Argo, aguarda validação da Véra antes da síntese, e entrega o Pulse Report via integrações configuradas. Nunca entrega análise sem passar pelo ciclo completo Discovery → Deep Dive → Framework. Responsável pelo SLA de entrega (target: relatório completo em <90 min após coleta iniciar).

## Knowledge base (o que o executor consulta)

- HubSpot / Salesforce (CRM
- pipeline de vendas, MRR, churn, NPS, métricas de CS via MCP)
- Stripe / Conta Azul / Omie (financeiro
- receita, MRR, ARR, inadimplência, unit economics via MCP ou API)
- Google Analytics 4 / Mixpanel / Amplitude (produto/analytics
- DAU, MAU, activation, retention, engagement via MCP)
- Meta Ads / Google Ads (mídia paga
- CPL, CAC, ROAS, impressões, conversões via MCP ou API)
- Google Sheets / Airtable (planilhas operacionais
- KPIs que ainda não têm sistema dedicado, coletados via MCP)
- ClickUp (OKRs source-of-truth + criação automática de tasks de recomendação + prova de trabalho do squad)
- Notion (Knowledge Base
- armazenamento permanente do Pulse Report, OKRs, histórico de diagnósticos e playbook de alavancas)
- Slack (entrega do Pulse semanal via canal privado #founder-pulse + alertas de desvio crítico em tempo real)
- WhatsApp Business API (versão ultra-curta do Pulse em 5 bullets via Sigma
- opcional, para founders mobile-first)
- Claude Agent SDK + LangGraph (orquestração stateful do grafo multi-agente
- gerencia ciclo semanal e queries ad-hoc)
- Langfuse (observabilidade OTEL
- tracing de custo por agente/token, evals de qualidade do diagnóstico, dashboard de KPIs do squad)
- Vector DB
- Pinecone ou Qdrant (histórico de KPIs, corpus do founder para Sigma, playbook de alavancas, heurísticas de Véra)
- MCP Servers (camada de integração universal
- cada sistema exposto como tool para Pulsar via protocolo MCP)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Véra 2 antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pulse Report Semanal
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

- **to:** Pulsar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
