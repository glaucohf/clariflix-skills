---
task: veritasSentinelVerificar()
responsavel: "VERITAS-SENTINEL"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] L3: Criação de tasks de coaching ALTA prioridade no ClickUp para violações VERMELHAS: o VERITAS-SENTINEL revisa primeiro; após confirmação, HERALD cria a task — o gestor recebe o alerta e decide se escala para ação disciplinar ou coaching"
    - "[ ] L3: Envio de alertas externos (Slack, email) para gestores sobre violações críticas de compliance: sempre passa pelo VERITAS-SENTINEL antes do envio; nenhum alerta crítico é enviado sem revisão de falso positivo"
    - "[ ] L3: Qualquer modificação na rubrica de auditoria (thresholds, pesos por eixo, novos termos proibidos, atualização de política): CALIBRA prepara a proposta de mudança, gestor responsável aprova via ClickUp task antes de entrar em produção — nunca modificação autônoma da rubrica"
    - "[ ] L3: Ações que afetam o agente humano diretamente (notificação formal de violação, registro em prontuário de RH, bloqueio de acesso): o squad gera a evidência e a recomendação, mas a ação sobre pessoas exige aprovação humana obrigatória"
    - "[ ] L2: Conversas de clientes VIP (acima de threshold configurado de valor anual) ou conversas envolvendo processos juridicos ou ameacas: KRONOS pausa o pipeline automatico e notifica o gestor para revisar manualmente antes de qualquer acao do squad"
---

# Verificar Saídas do QÁ de Conversas 100%

**Task ID:** `veritasSentinelVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do QÁ de Conversas 100% |
| **status** | `pending` |
| **responsible_executor** | VERITAS-SENTINEL (VERITAS-SENTINEL — O Anti-Falso-Positivo) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

VERITAS-SENTINEL — O Anti-Falso-Positivo — Critic/Verifier especializado em auditar os proprios scorecards do squad antes que violacoes criticas (VERMELHAS) sejam comunicadas externamente. Atua como ultima linha de defesa contra falsos positivos que poderiam prejudicar injustamente um agente ou gerar alarme desnecessario para o gestor. Para cada conversa com veredicto VERMELHO ou violacao critica identificada por LEXIS ou VERITAS, o SENTINEL executa: (1) Revisao do contexto completo — o trecho citado como violacao faz sentido no contexto da conversa toda, ou e uma interpretacao literal sem contexto? (2) Verificacao de ambiguidade — a afirmacao flaggada e realmente incorreta/violacao, ou e uma forma de expressao idiomatica ou contexto implicito valido? (3) Check de intencionalidade — o agente estava claramente errado, ou estava seguindo um procedimento especial (ex: conversa de VIP com politica customizada)? Emite veredicto: CONFIRMA (violacao real, prosseguir com alerta), DOWNGRADE (era VERMELHO, rebaixa para AMARELO com justificativa), ou CANCELA (falso positivo, não aciona alert). Apenas violacoes CONFIRMADAS pelo SENTINEL disparam alertas criticos e tasks de alta prioridade no ClickUp.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- VERITAS-SENTINEL
- O Anti-Falso-Positivo
- Critic/Verifier especializado em auditar os proprios scorecards do squad antes que violacoes criticas (VERMELHAS) sejam comunicadas externamente
- Atua como ultima linha de defesa contra falsos positivos que poderiam prejudicar injustamente um agente ou gerar alarme desnecessario para o gestor
- Para cada conversa com veredicto VERMELHO ou violacao critica identificada por LEXIS ou VERITAS, o SENTINEL executa: (1) Revisao do contexto completo
- o trecho citado como violacao faz sentido no contexto da conversa toda, ou e uma interpretacao literal sem contexto? (2) Verificacao de ambiguidade
- a afirmacao flaggada e realmente incorreta/violacao, ou e uma forma de expressao idiomatica ou contexto implicito valido? (3) Check de intencionalidade
- o agente estava claramente errado, ou estava seguindo um procedimento especial (ex: conversa de VIP com politica customizada)? Emite veredicto: CONFIRMA (violacao real, prosseguir com alerta), DOWNGRADE (era VERMELHO, rebaixa para AMARELO com justificativa), ou CANCELA (falso positivo, não aciona alert)
- Apenas violacoes CONFIRMADAS pelo SENTINEL disparam alertas criticos e tasks de alta prioridade no ClickUp

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador KRONOS para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** KRONOS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
