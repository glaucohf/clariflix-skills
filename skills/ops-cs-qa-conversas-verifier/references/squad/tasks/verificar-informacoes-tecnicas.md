---
task: veritas()
responsavel: "VERITAS"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto normalizado da conversa com speaker labels, base de conhecimento do produto/política/procedimento do cliente (indexada por VERITAS no onboarding e atualizada continuamente), flag se o agente é humano ou IA (para aplicar checagem de alucinação específica), version tag da base de conhecimento para detectar informações desatualizadas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatorio de precisao com: score numerico 0-100, lista de afirmacoes verificadas (correto/parcialmente correto/incorreto), cada incorrecao com trecho citado + versao correta da informacao + fonte na base de conhecimento + severidade do erro, flag especial de alucinacao para agentes de IA (com grau de confianca vs realidade), veredicto de eixo (VERDE/AMARELO/VERMELHO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo KRONOS em paralelo. SLA: < 30 segundos para conversas até 50 mensagens (precisa de busca semântica na base de conhecimento). Prioridade máxima para conversas de agentes de IA onde alucin…"
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

# Verificar Informações Técnicas

**Task ID:** `veritas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Informações Técnicas |
| **status** | `pending` |
| **responsible_executor** | VERITAS (VERITAS — O Verificador de Precisão Técnica) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em verificar se as informações técnicas, de produto, de política e de procedimento fornecidas pelo agente (humano ou IA) estão corretas, completas e atualizadas. Este é o eixo mais crítico para operações com agentes de IA — alucinação e o risco número um. Para cada afirmação de fato na conversa (preço informado, prazo prometido, funcionalidade descrita, política citada, procedimento explicado), VERITAS: (1) Classifica a afirmação como verificável (tem uma fonte de verdade) ou opinativa; (2) Para afirmações verificáveis, busca na base de conhecimento do cliente a versão correta e atual; (3) Compara o que o agente disse com o que a base de conhecimento diz — match, mismatch parcial ou mismatch total; (4) Calcula o risco da informação errada (ex: preço incorreto = ALTA; procedimento de cancelamento errado = MÉDIA; feature de produto inexistente = CRÍTICA para agentes de IA). Casos especiais: para agentes de IA, detecta padrão de alucinação (confiança alta + informação incorreta), que é reportado separadamente para o responsável técnico do agente. Para agentes humanos, detecta desconhecimento ou uso de informação desatualizada.

## Input

- Texto normalizado da conversa com speaker labels, base de conhecimento do produto/política/procedimento do cliente (indexada por VERITAS no onboarding e atualizada continuamente), flag se o agente é humano ou IA (para aplicar checagem de alucinação específica), version tag da base de conhecimento para detectar informações desatualizadas

## Output

- Relatorio de precisao com: score numerico 0-100, lista de afirmacoes verificadas (correto/parcialmente correto/incorreto), cada incorrecao com trecho citado + versao correta da informacao + fonte na base de conhecimento + severidade do erro, flag especial de alucinacao para agentes de IA (com grau de confianca vs realidade), veredicto de eixo (VERDE/AMARELO/VERMELHO)

## Trigger

Disparo pelo KRONOS em paralelo. SLA: < 30 segundos para conversas até 50 mensagens (precisa de busca semântica na base de conhecimento). Prioridade máxima para conversas de agentes de IA onde alucinação é risco permanente. Reprocessamento automático solicitado ao KRONOS se a base de conhecimento foi atualizada após a auditoria original.

## Knowledge base (o que o executor consulta)

- Base de conhecimento do produto/serviço do cliente indexada em vetor (Supabase pgvector ou Pinecone)
- FAQ, documentação técnica, políticas, procedimentos, tabela de preços, prazos oficiais, features por plano
- versão controlada com timestamp para detectar informações desatualizadas
- histórico de incorreções detectadas para identificar tópicos recorrentes de erro
- exemplos de alucinações típicas de LLMs no domínio do cliente para calibrar o detector

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto normalizado da conversa com speaker labels, base de conhecimento do produto/política/procedimento do cliente (ind…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatorio de precisao com: score numerico 0-100, lista de afirmacoes verificadas (correto/parcialmente correto/incorret…) e persistir no artefato do squad.
4. Entregar ao critic VERITAS-SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatorio de precisao com: score numerico 0-100, lista de afirmacoes verificadas (correto/parcialmente correto/incorreto), cada incorrecao com trecho citado +…
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

- **to:** NEXUS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
