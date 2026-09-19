---
task: herald()
responsavel: "HERALD"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Scores e relatórios dos quatro workers (LEXIS, ARIA, VERITAS, NEXUS), score compósito e veredicto final calculados pelo KRONOS, metadados da conversa (agente, canal, cliente, timestamp), configuração de alertas do cliente (quem recebe o que, por qual canal, em qual threshold)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Scorecard individual por conversa (PDF ou card no ClickUp com: score total + score por eixo + veredicto + trechos evidenciados + ação recomendada), task de coaching/correção no ClickUp (para conversas AMARELA/VERMELHA), alerta Slack para gestor (para violações VERMELHAS críticas), relatório consolidado de tendências (diário/semanal em formato markdown + dados para dashboard), métricas de produção do squad (volume auditado, taxa de violação, distribuição por eixo) para o dashboard de qualidade"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo KRONOS apos receber todos os scores dos workers e o veredicto final. SLA: < 10 segundos para gerar scorecard e abrir task. Relatório consolidado gerado diariamente as 07h (ou no horário…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic VERITAS-SENTINEL antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HERALD cria a task — o gestor recebe o alerta e decide se escala para ação disciplinar ou coaching"
    - "[ ] L3: Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do envio; nenhum alerta crítico é enviado sem revisão de falso positivo"
    - "[ ] L3: Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara a proposta de mudança, gestor responsável aprova via ClickUp task antes de entrar em produção — nunca modificação autônoma da rubrica"
    - "[ ] L3: Ações que afetam o agente humano diretamente (notificação formal de violação, registro em prontuário de RH, bloqueio de acesso): o squad gera a evidência e a recomendação, mas a ação sobre pessoas exige aprovação humana obrigatória"
    - "[ ] L2: Conversas de clientes VIP (acima de threshold configurado de valor anual) ou conversas envolvendo processos juridicos ou ameacas: KRONOS pausa o pipeline automatico e notifica o gestor para revisar manualmente antes de qualquer acao do squad"
---

# Gerar Scorecard Completo

**Task ID:** `herald()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Scorecard Completo |
| **status** | `pending` |
| **responsible_executor** | HERALD (HERALD — O Repórter e Gestor de Acoes) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de output responsavel por transformar os scores brutos dos quatro eixos em artefatos verificaveis e acionaveis. Para cada conversa auditada: (1) Gera o scorecard completo com evidencias citadas, organizado em formato legivel para gestores e para o agente auditado; (2) Para conversas AMARELAS, abre task de coaching no ClickUp com template padronizado: agente responsavel, eixo com menor score, trechos especificos como evidencia, acao de coaching recomendada (ex: 'revisar politica de reembolso', 'assistir a treinamento de empatia', 'calibrar prompt do agente de IA'), prazo de 72h, prioridade MEDIA; (3) Para conversas VERMELHAS com violacao critica, dispara alerta imediato via Slack para o gestor responsavel com resumo em 3 linhas + link para o scorecard completo, e abre task ALTA prioridade no ClickUp; (4) Ao final de cada ciclo (diario ou semanal, configuravel), consolida o relatorio de tendencias: top 5 agentes com mais conversas AMARELAS/VERMELHAS, evolucao da taxa de violacao por eixo, ranking de conversas mais criticas da semana, comparativo com periodo anterior. O HERALD nunca age diretamente sobre o agente ou o cliente — sua funcao e garantir que a evidencia chegue a quem pode agir.

## Input

- Scores e relatórios dos quatro workers (LEXIS, ARIA, VERITAS, NEXUS), score compósito e veredicto final calculados pelo KRONOS, metadados da conversa (agente, canal, cliente, timestamp), configuração de alertas do cliente (quem recebe o que, por qual canal, em qual threshold)

## Output

- Scorecard individual por conversa (PDF ou card no ClickUp com: score total + score por eixo + veredicto + trechos evidenciados + ação recomendada), task de coaching/correção no ClickUp (para conversas AMARELA/VERMELHA), alerta Slack para gestor (para violações VERMELHAS críticas), relatório consolidado de tendências (diário/semanal em formato markdown + dados para dashboard), métricas de produção do squad (volume auditado, taxa de violação, distribuição por eixo) para o dashboard de qualidade

## Trigger

Disparo pelo KRONOS apos receber todos os scores dos workers e o veredicto final. SLA: < 10 segundos para gerar scorecard e abrir task. Relatório consolidado gerado diariamente as 07h (ou no horário configurado pelo cliente) e semanalmente toda segunda-feira as 08h. Alerta crítico enviado em < 2 minutos apos veredicto VERMELHO com violação crítica. L3 gate para criação de tasks no ClickUp e envio de alertas externos.

## Knowledge base (o que o executor consulta)

- Templates de scorecard e relatório (configurados por cliente no onboarding), estrutura de workspace ClickUp do cliente (listas, responsáveis, campos customizados para tasks de coaching), canais Slack de alerta por tipo de violação e por gestor responsável, histórico de scorecards anteriores para o relatório de tendências e comparativo histórico, regras de roteamento de alertas (ex: violação de compliance vai para o jurídico E para o CS Manager
- violação de tom vai apenas para o supervisor direto)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Scores e relatórios dos quatro workers (LEXIS, ARIA, VERITAS, NEXUS), score compósito e veredicto final calculados pelo…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Scorecard individual por conversa (PDF ou card no ClickUp com: score total + score por eixo + veredicto + trechos evide…) e persistir no artefato do squad.
4. Entregar ao critic VERITAS-SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Scorecard individual por conversa (PDF ou card no ClickUp com: score total + score por eixo + veredicto + trechos evidenciados + ação recomendada), task de coa…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic VERITAS-SENTINEL registrado
- [ ] Gate L3 respeitado: Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HER…
- [ ] Gate L3 respeitado: Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do…
- [ ] Gate L3 respeitado: Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HERALD cria a task — o… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do envio; nenhum alerta… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara a proposta de mudan… | BLOQUEIA até decisão humana |
| VETO-004 | L3 — Ações que afetam o agente humano diretamente (notificação formal de violação, registro em prontuário de RH, bloqueio de acesso): o squad gera a evidência e a r… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Conversas de clientes VIP (acima de threshold configurado de valor anual) ou conversas envolvendo processos juridicos ou ameacas: KRONOS pausa o pipeline autom… | BLOQUEIA até decisão humana |
| VETO-006 | L2 — Contestação de scorecard pelo agente auditado: CALIBRA recebe a contestação, analisa e gera recomendação (confirmar ou reverter veredicto), mas a decisão final… | BLOQUEIA até decisão humana |
| VETO-007 | L1 — Calibragem inicial da rubrica no onboarding: os pesos dos eixos, os thresholds de VERDE/AMARELO/VERMELHO e a lista inicial de termos proibidos são definidos pe… | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic VERITAS-SENTINEL | BLOQUEIA entrega |

## Handoff

- **to:** CALIBRA
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
