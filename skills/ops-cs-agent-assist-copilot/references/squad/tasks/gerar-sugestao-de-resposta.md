---
task: scribe()
responsavel: "Scribe"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Intenção classificada + pacote_de_conta do Vault + texto das últimas 3 mensagens da conversa + preferência de tom do atendente (configurável por usuário)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Array de 1-2 sugestões de resposta com: {texto_sugestão, variante (formal/conversacional), fonte (macro_id | kb_article_id | histórico), confiança, campos_personalizados_preenchidos, aviso_se_dado_ausente}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Formato pronto para 1-click insert no helpdesk"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orchestrator Compass chama apos ter o output do Radar (intenção) e do Vault (contexto), com latência combinada < 1.5s"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Prism antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar conscientemente ou corrigir"
    - "[ ] HITL: Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — responda manualmente'"
    - "[ ] HITL: Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico"
    - "[ ] HITL: Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromisso"
    - "[ ] HITL: Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente"
---

# Gerar Sugestão de Resposta

**Task ID:** `scribe()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Copiloto do Agente Humano (Agent Assist Copilot)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Sugestão de Resposta |
| **status** | `pending` |
| **responsible_executor** | Scribe (Scribe — Worker de Sugestão de Resposta) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gera a sugestão de próxima resposta para o atendente baseando-se na intenção classificada, no pacote de conta do Vault e no KB. Primeiro busca se existe macro/template oficial para aquela intenção; se sim, personaliza com dados da conta (nome, plano, pedido específico); se não, gera draft livre usando as 3-5 melhores respostas históricas como ground-truth via RAG. Produz sempre 2 variantes: uma mais formal e uma mais conversacional, para o atendente escolher. Cita a fonte da sugestão (macro X, artigo KB Y, resposta histórica Z) para que o atendente confie e possa verificar.

## Input

- Intenção classificada + pacote_de_conta do Vault + texto das últimas 3 mensagens da conversa + preferência de tom do atendente (configurável por usuário)

## Output

- Array de 1-2 sugestões de resposta com: {texto_sugestão, variante (formal/conversacional), fonte (macro_id | kb_article_id | histórico), confiança, campos_personalizados_preenchidos, aviso_se_dado_ausente}
- Formato pronto para 1-click insert no helpdesk

## Trigger

Orchestrator Compass chama apos ter o output do Radar (intenção) e do Vault (contexto), com latência combinada < 1.5s

## Knowledge base (o que o executor consulta)

- Base de macros oficiais vetorizada (Supabase pgvector), KB do helpdesk (artigos de suporte, polí­ticas, FAQs), corpus de 200+ melhores respostas históricas por intenção (ground-truth curado), templates de personalização por variável (nome_cliente, plano, data_pedido, valor, prazo), preferências de tom por atendente (configurável)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Intenção classificada + pacote_de_conta do Vault + texto das últimas 3 mensagens da conversa + preferência de tom do at…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Array de 1-2 sugestões de resposta com: {texto_sugestão, variante (formal/conversacional), fonte (macro_id | kb_article…) e persistir no artefato do squad.
4. Entregar ao critic Prism; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Array de 1-2 sugestões de resposta com: {texto_sugestão, variante (formal/conversacional), fonte (macro_id | kb_article_id | histórico), confiança, campos_pers…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Prism registrado
- [ ] Gate HITL respeitado: Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atenden…
- [ ] Gate HITL respeitado: Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'int…
- [ ] Gate HITL respeitado: Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso esp…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Shield detecta violação de LGPD no rascunho do atendente (severidade 'blocker'): pop-up de confirmação obrigatória antes do envio — atendente deve confirmar co… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confianca do Radar < 0.65 na classificacao de intencao: Compass nao exibe sugestao, exibe apenas o contexto da conta (Vault) com aviso 'intencao incerta — resp… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Scribe falha após 2 tentativas (Critic rejeita ambas): exibe aviso ao atendente que nenhuma sugestão adequada foi gerada para este caso específico | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Ticket de cliente em tier VIP/Enterprise ou MRR > R$10k: Lumen dispara alerta 'cliente estratégico' e recomenda envolvimento do CSM antes de qualquer compromis… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lumen detecta SLA em risco (< 20% do tempo restante): alerta visual urgente no overlay para o supervisor e para o atendente | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Vault retorna flag 'cliente_em_risco_de_churn' (health score < 50): todas as sugestões do Scribe são marcadas com indicador visual e Lumen adiciona sugestão de… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Echo detecta que uma macro tem rejection_rate > 60% por 7 dias consecutivos: dispara alerta para gestor de CS no Slack pedindo revisão manual da macro antes de… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Shield detecta promessa de desconto ou benefício financeiro no rascunho do atendente: alerta de policy_violation com valor exato do limite autorizado e botão d… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Prism | BLOQUEIA entrega |

## Handoff

- **to:** Memo
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
