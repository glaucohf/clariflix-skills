---
task: nexus()
responsavel: "NEXUS"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto normalizado da conversa com speaker labels e timestamps, histórico de tickets anteriores do mesmo cliente (se disponível via CRM/helpdesk MCP para verificar se é recontato pelo mesmo problema), número de agentes envolvidos na conversa, metadados de escalonamento (se houve transferência de fila/agente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio de resolucao com: score numerico 0-100, veredicto de resolucao (RESOLVIDO / RESOLVIDO PARCIALMENTE / NAO RESOLVIDO / FALSO FECHAMENTO), avaliacao de timing de escalonamento (ADEQUADO / TARDIO / PREMATURO / AUSENTE quando necessario), qualidade do handoff (COMPLETO / CONTEXTO PERDIDO / CLIENTE REPETIU PROBLEMA), flag de re-contato provavel (true se conversa encerrou sem resolucao real ou proximo passo claro), veredicto de eixo (VERDE/AMARELO/VERMELHO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo KRONOS em paralelo. SLA: < 25 segundos. Prioridade elevada para conversas marcadas como 'fechadas/resolvidas' no helpdesk — são as que têm maior risco de falso fechamento."
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

# Avaliar Resolução Problema

**Task ID:** `nexus()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Avaliar Resolução Problema |
| **status** | `pending` |
| **responsible_executor** | NEXUS (NEXUS — O Avaliador de Resolução e Handoff) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em avaliar se o problema do cliente foi efetivamente resolvido e se a jornada de atendimento foi gerenciada com inteligência — especialmente os momentos de escalonamento e handoff. NEXUS avalia quatro aspectos críticos: (1) Resolução real vs aparente — o problema foi resolvido de verdade ou o agente 'fechou' o ticket sem solução (padrões como 'aguardando retorno do cliente' usados como evasão)? O cliente confirmou resolução ou simplesmente parou de responder? (2) Timing do escalonamento — o agente reconheceu nos momentos certos que precisava escalar para um nível superior, especialista ou HITL humano? Escalonamentos tardios (depois de 10 tentativas falhas) e escalonamentos prematuros (escalou algo que poderia resolver) são ambos penalizados; (3) Qualidade do handoff — quando houve transferência entre agentes ou canais, o contexto foi passado corretamente? O cliente precisou repetir o problema? (4) Próximo passo claro — o cliente saiu da conversa sabendo exatamente o que vai acontecer, quando e por quem? Conversas sem próximo passo claro têm alto risco de re-contato desnecessário (first contact resolution rate).

## Input

- Texto normalizado da conversa com speaker labels e timestamps, histórico de tickets anteriores do mesmo cliente (se disponível via CRM/helpdesk MCP para verificar se é recontato pelo mesmo problema), número de agentes envolvidos na conversa, metadados de escalonamento (se houve transferência de fila/agente)

## Output

- Relatorio de resolucao com: score numerico 0-100, veredicto de resolucao (RESOLVIDO / RESOLVIDO PARCIALMENTE / NAO RESOLVIDO / FALSO FECHAMENTO), avaliacao de timing de escalonamento (ADEQUADO / TARDIO / PREMATURO / AUSENTE quando necessario), qualidade do handoff (COMPLETO / CONTEXTO PERDIDO / CLIENTE REPETIU PROBLEMA), flag de re-contato provavel (true se conversa encerrou sem resolucao real ou proximo passo claro), veredicto de eixo (VERDE/AMARELO/VERMELHO)

## Trigger

Disparo pelo KRONOS em paralelo. SLA: < 25 segundos. Prioridade elevada para conversas marcadas como 'fechadas/resolvidas' no helpdesk — são as que têm maior risco de falso fechamento.

## Knowledge base (o que o executor consulta)

- Política de escalonamento do cliente (criterios para quando escalar, níveis de suporte, SLAs por tier de cliente), histórico de tickets do cliente no CRM/helpdesk para detecção de re-contato pelo mesmo problema, padrões linguísticos de falso fechamento ('vou verificar e te retorno', 'aguardando informações') vs resolução real ('seu problema foi resolvido pois X'), métricas de FCR (First Contact Resolution) históricas para calibrar o benchmark do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto normalizado da conversa com speaker labels e timestamps, histórico de tickets anteriores do mesmo cliente (se dis…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio de resolucao com: score numerico 0-100, veredicto de resolucao (RESOLVIDO / RESOLVIDO PARCIALMENTE / NAO RESO…) e persistir no artefato do squad.
4. Entregar ao critic VERITAS-SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio de resolucao com: score numerico 0-100, veredicto de resolucao (RESOLVIDO / RESOLVIDO PARCIALMENTE / NAO RESOLVIDO / FALSO FECHAMENTO), avaliacao de…
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

- **to:** HERALD
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
