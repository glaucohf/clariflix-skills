---
task: calibra()
responsavel: "CALIBRA"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Historico de todos os scorecards e verditos do squad, log de contestacoes de scorecards abertas no ClickUp, feedback de gestores e agentes sobre qualidade do QA, changelog da base de conhecimento (VERITAS precisa reprocessar conversas se base mudou), metricas de fechamento das tasks de coaching (taxa de conclusao, tempo medio de resolucao)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório mensal de saúde da rubrica (taxa de falso positivo por eixo, thresholds recomendados, exemplos de casos-borda), solicitação de ajuste de rubrica ao gestor para aprovação HITL, lista de conversas para reprocessamento quando base de conhecimento muda, alertas de anomalia quando taxa de violação muda abruptamente (> 20% em 7 dias"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "indica mudança de política não comunicada ou novo agente sem treinamento)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo mensal automático para relatório de saúde. Disparo imediato quando taxa de contestação de scorecards supera 5% das conversas auditadas em 30 dias (indica problema sistemático na rubrica). Dispa…"
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

# Calibrar Rubrica

**Task ID:** `calibra()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calibrar Rubrica |
| **status** | `pending` |
| **responsible_executor** | CALIBRA (CALIBRA — O Curador da Rubrica e do Aprendizado) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de RevOps responsavel pela evolucao continua da qualidade do squad. Dois problemas criticos em qualquer sistema de QA automatizado: (1) falso positivo — o squad penaliza o agente por algo que na verdade estava correto, gerando distrust e resistencia do time; (2) drift da rubrica — as politicas da empresa mudam, mas o QA continua avaliando pela rubrica antiga. CALIBRA resolve ambos. Monitora continuamente: taxa de contestacao de scorecards (quando um gestor ou agente contesta um veredicto via ClickUp task, CALIBRA analisa se e falso positivo sistematico ou caso isolado), acoes corretivas implementadas vs abertas (tasks de coaching que nunca foram fechadas indicam rubrica irrealista ou acao de coaching ineficaz), mudancas na base de conhecimento que invalidam scorecards passados. Mensalmente, gera um relatorio de saude da rubrica: quais eixos tem maior taxa de contestacao, quais thresholds estao gera muito falso positivo/negativo, sugestoes de ajuste calibradas. Qualquer mudanca na rubrica passa por HITL: o gestor responsavel aprova antes de entrar em producao.

## Input

- Historico de todos os scorecards e verditos do squad, log de contestacoes de scorecards abertas no ClickUp, feedback de gestores e agentes sobre qualidade do QA, changelog da base de conhecimento (VERITAS precisa reprocessar conversas se base mudou), metricas de fechamento das tasks de coaching (taxa de conclusao, tempo medio de resolucao)

## Output

- Relatório mensal de saúde da rubrica (taxa de falso positivo por eixo, thresholds recomendados, exemplos de casos-borda), solicitação de ajuste de rubrica ao gestor para aprovação HITL, lista de conversas para reprocessamento quando base de conhecimento muda, alertas de anomalia quando taxa de violação muda abruptamente (> 20% em 7 dias
- indica mudança de política não comunicada ou novo agente sem treinamento)

## Trigger

Ciclo mensal automático para relatório de saúde. Disparo imediato quando taxa de contestação de scorecards supera 5% das conversas auditadas em 30 dias (indica problema sistemático na rubrica). Disparo quando base de conhecimento do VERITAS é atualizada (solicita reprocessamento de conversas dos últimos 30 dias para recalibragem). L3 gate para qualquer modificação na rubrica de produção.

## Knowledge base (o que o executor consulta)

- Histórico completo de scorecards e veredictos com timestamps, log de contestações e resoluções (aprovadas vs rejeitadas), versões anteriores da rubrica para comparativo de impacto de mudanças, métricas de coaching (quantos agentes melhoraram o score após task de coaching
- mede eficácia da ação recomendada), benchmarks de indústria por setor para calibrar thresholds (ex: taxa de violação média em fintech vs e-commerce vs SaaS)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Historico de todos os scorecards e verditos do squad, log de contestacoes de scorecards abertas no ClickUp, feedback de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório mensal de saúde da rubrica (taxa de falso positivo por eixo, thresholds recomendados, exemplos de casos-borda…) e persistir no artefato do squad.
4. Entregar ao critic VERITAS-SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório mensal de saúde da rubrica (taxa de falso positivo por eixo, thresholds recomendados, exemplos de casos-borda), solicitação de ajuste de rubrica ao g…
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

- **to:** VERITAS-SENTINEL
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
