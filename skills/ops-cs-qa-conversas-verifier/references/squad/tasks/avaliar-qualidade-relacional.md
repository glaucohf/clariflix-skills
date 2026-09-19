---
task: aria()
responsavel: "ARIA"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto normalizado da conversa com speaker labels, sentimento detectado pelo canal de origem (se disponível), perfil do cliente (tier, histórico de reclamações se disponível no CRM), persona de atendimento do cliente (tom de voz oficial da empresa: formal, descontraído, técnico)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório de tom com: score numérico 0-100 (média ponderada das 5 dimensões), pontuação por dimensão, trechos citados de boas práticas e oportunidades de melhoria, curva de sentimento do cliente ao longo da conversa (melhora/piora/estável), flag de risco de churn (true se cliente encerrou com sentimento negativo sem resolução), veredicto de eixo (VERDE/AMARELO/VERMELHO)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo KRONOS em paralelo com os outros workers. SLA: < 25 segundos para conversas até 50 mensagens. Prioridade elevada para conversas de clientes com score de saúde baixo no CS platform (Churn…"
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

# Avaliar Qualidade Relacional

**Task ID:** `aria()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de QÁ de Conversas 100% (Quality Verifier)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Avaliar Qualidade Relacional |
| **status** | `pending` |
| **responsible_executor** | ARIA (ARIA — A Auditora de Tom e Empatia) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em avaliar a qualidade relacional da interacao: tom, empatia, personalizacao, clareza e desfecho emocional. ARIA nao busca violacoes — busca a diferenca entre um atendimento que retém o cliente e um que o empurra para o churn silencioso. Para cada conversa, avalia cinco dimensoes: (1) Acolhimento inicial — o agente reconheceu o estado emocional do cliente (frustrado, confuso, urgente) ou respondeu com script generico ignorando o contexto? (2) Personalizacao — o agente usou o nome do cliente, referenciou historico de interacoes anteriores, tratou o problema como unico ou como ticket 347? (3) Clareza e objetividade — as respostas foram diretas, ou longas demais com jargao desnecessario e CYA burocratico? (4) Empatia em momentos criticos — quando o cliente expressou frustacao ou reclamou, o agente demonstrou compreensao antes de oferecer solucao? (5) Desfecho — a conversa encerrou com proximo passo claro, cliente ciente do que esperar, ou ficou em aberto de forma ambigua? Cada dimensao recebe uma nota de 1-5 e o score final e a media ponderada. Identifica tambem o sentimento do cliente ao longo da conversa (melhora ou piora) como sinal de efetividade do agente.

## Input

- Texto normalizado da conversa com speaker labels, sentimento detectado pelo canal de origem (se disponível), perfil do cliente (tier, histórico de reclamações se disponível no CRM), persona de atendimento do cliente (tom de voz oficial da empresa: formal, descontraído, técnico)

## Output

- Relatório de tom com: score numérico 0-100 (média ponderada das 5 dimensões), pontuação por dimensão, trechos citados de boas práticas e oportunidades de melhoria, curva de sentimento do cliente ao longo da conversa (melhora/piora/estável), flag de risco de churn (true se cliente encerrou com sentimento negativo sem resolução), veredicto de eixo (VERDE/AMARELO/VERMELHO)

## Trigger

Disparo pelo KRONOS em paralelo com os outros workers. SLA: < 25 segundos para conversas até 50 mensagens. Prioridade elevada para conversas de clientes com score de saúde baixo no CS platform (ChurnZero/Custify) quando integração disponível.

## Knowledge base (o que o executor consulta)

- Guia de tom e voz da marca do cliente (levantado no onboarding
- formalidade, palavras de marca, expressoes proibidas como 'isso nao e comigo'), rubrica de empatia adaptada ao setor (B2B enterprise tem expectativa diferente de B2C varejo), biblioteca de exemplos de respostas empáticas vs mecanicas para calibragem do modelo, perfis de sentimento de clientes em risco de churn (padroes de linguagem que precederam cancelamentos historicos)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto normalizado da conversa com speaker labels, sentimento detectado pelo canal de origem (se disponível), perfil do…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório de tom com: score numérico 0-100 (média ponderada das 5 dimensões), pontuação por dimensão, trechos citados d…) e persistir no artefato do squad.
4. Entregar ao critic VERITAS-SENTINEL; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório de tom com: score numérico 0-100 (média ponderada das 5 dimensões), pontuação por dimensão, trechos citados de boas práticas e oportunidades de melho…
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

- **to:** VERITAS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
