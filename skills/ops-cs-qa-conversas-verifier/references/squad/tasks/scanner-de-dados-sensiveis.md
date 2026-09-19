---
task: lexis()
responsavel: "LEXIS"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto normalizado da conversa completa (todas as mensagens, com speaker label: agente ou cliente), metadados do agente (humano ou IA, nome/ID), setor do cliente para aplicar rubrica específica, lista de termos proibidos e políticas configuradas no onboarding"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de compliance com: score numérico de 0-100, lista de violações encontradas (cada uma com trecho citado + número da mensagem + tipo + severidade), flag de escalação imediata (true/false para violações CRÍTICAS), veredicto de eixo (VERDE/AMARELO/VERMELHO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo KRONOS para cada conversa na fila. Execução paralela com ARIA, VERITAS e NEXUS. SLA: resultado em < 20 segundos para conversas de até 50 mensagens; < 45 segundos para conversas longas (5…"
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

# Scanner De Dados Sensiveis

**Task ID:** `lexis()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Scanner De Dados Sensiveis |
| **status** | `pending` |
| **responsible_executor** | LEXIS (LEXIS — O Guardião de Compliance) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em detecção de violações regulatorias, promessas não autorizadas, exposição de dados sensíveis e linguagem proibida. Para cada conversa recebida, LEXIS executa três passagens: (1) Scan de dados sensíveis — detecta CPF, CNPJ, número de cartão, senha, dado de saúde ou qualquer PII que não deveria estar em texto claro na conversa; (2) Detecção de violações de compliance — verifica contra a lista de termos proibidos (ex: garantia de resultado, promessa de prazo não autorizada, afirmação regulatoria sem disclaimer), adaptada ao setor do cliente (financeiro, saúde, jurídico, e-commerce); (3) Auditoria de autorizações — identifica compromissos assumidos pelo agente que excedem a política da empresa (ex: reembolso prometido fora da janela de política, desconto concedido sem autorização). Cada achado é reportado com: trecho exato da conversa (com número de mensagem), tipo de violação, severidade (CRÍTICA / ALTA / MÉDIA), e ação recomendada. Score de compliance calculado como: 100 - (soma ponderada de violações x severidade). Violação CRÍTICA automaticamente eleva o veredicto da conversa para VERMELHO independente dos outros scores.

## Input

- Texto normalizado da conversa completa (todas as mensagens, com speaker label: agente ou cliente), metadados do agente (humano ou IA, nome/ID), setor do cliente para aplicar rubrica específica, lista de termos proibidos e políticas configuradas no onboarding

## Output

- Relatório de compliance com: score numérico de 0-100, lista de violações encontradas (cada uma com trecho citado + número da mensagem + tipo + severidade), flag de escalação imediata (true/false para violações CRÍTICAS), veredicto de eixo (VERDE/AMARELO/VERMELHO)

## Trigger

Disparo pelo KRONOS para cada conversa na fila. Execução paralela com ARIA, VERITAS e NEXUS. SLA: resultado em < 20 segundos para conversas de até 50 mensagens; < 45 segundos para conversas longas (50+ mensagens). Prioridade máxima para conversas com keywords de risco pré-detectados no Discovery.

## Knowledge base (o que o executor consulta)

- Rubrica de compliance configurada por setor (LGPD para dados sensíveis, regulações BACEN para fintech, CFM para saúde, CONAR para publicidade), lista de termos proibidos e promessas não autorizadas do cliente (levantada no onboarding e atualizada pelo gestor via ClickUp task), políticas de atendimento do cliente (janelas de reembolso, limites de desconto por nível, política de SLA), histórico de violações anteriores para calibragem de threshold, regex patterns para detecção de PII (CPF, CNPJ, cartão, etc.)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto normalizado da conversa completa (todas as mensagens, com speaker label: agente ou cliente), metadados do agente…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de compliance com: score numérico de 0-100, lista de violações encontradas (cada uma com trecho citado + núme…) e persistir no artefato do squad.
4. Entregar ao critic VERITAS-SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de compliance com: score numérico de 0-100, lista de violações encontradas (cada uma com trecho citado + número da mensagem + tipo + severidade), fla…
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

- **to:** ARIA
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
