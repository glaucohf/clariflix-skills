---
task: memory()
responsavel: "Memory"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Notas de CRM pos-QBR (atividades, emails, calls do CSM) + feedback do CSM sobre o brief (campos de avaliacao na task ClickUp) + decisoes de renovacao registradas no CRM (ganho/perdido/negociado/downgrade) + outcomes de expansao (aceita/rejeitada + motivo) + gravacoes ou transcricoes de chamadas de QBR (se disponivel via integracao de call recording)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Account Memory atualizado no Supabase por conta: historico de QBRs com outcomes, comprometimentos com status, expansoes tentadas e resultados, evolucao temporal de scores, feedback sobre qualidade dos briefs"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Relatorio mensal de aprendizado para o Maestro: quais tipos de brief geraram mais renovacoes saudaveis, quais sinais de expansao tiveram maior taxa de conversao, quais dimensoes do Renewal Readiness Score foram mais preditivas"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Calibracoes sugeridas para o modelo de pesos do Compass"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado quando CSM fecha task de renovacao no ClickUp (status: Renovado/Churn/Negociado/Expandido); acionado quando CSM adiciona nota de QBR no CRM; cron semanal para relatorio de aprendizado; acion…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Verity antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de expansao com status 'Aguardando Aprovacao do CSM/Manager' antes de incluir a proposta no deck final para o cliente"
    - "[ ] HITL: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CSM (deck e gerado, nunca enviado automaticamente ao cliente)"
    - "[ ] HITL: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar qualquer contato de renovacao"
    - "[ ] HITL: Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de entrada antes de reprocessar"
    - "[ ] HITL: Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer alinhamento com equipe comercial (AE ou CSM sênior) antes de abordar o cliente"
---

# Arquivar Resultados QBR

**Task ID:** `memory()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Arquivar Resultados QBR |
| **status** | `pending` |
| **responsible_executor** | Memory (Memory — Arquivista de Resultados e Historico de Conta) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Captura e persiste os resultados de cada QBR e renovacao para enriquecer futuros briefs — fecha o ciclo de aprendizado do squad. Apos cada QBR realizado: extrai do registro do CSM no CRM (notas, email de follow-up, gravacao de chamada se disponivel) os outcomes principais: comprometimentos assumidos pelo fornecedor, problemas sinalizados pelo cliente, decisao de renovacao (sim/nao/negociacao), expansao aceita ou rejeitada com motivo, feedback sobre o QBR. Consolida no Supabase um 'Account Memory' por conta com: timeline de todos os QBRs, comprometimentos e status de entrega, expansoes realizadas e rejeitadas, evolucao do Renewal Readiness Score ao longo do tempo, e NPS/CSAT trends. Este historico e a principal fonte de contexto do Briefer em futuras geracoes de brief — tornando cada QBR mais personalizado que o anterior. Tambem aprende com os briefs: quando CSM edita o deck gerado pelo Slides ou marca um brief como 'nao util', Memory registra o feedback para calibracao futura do Briefer.

## Input

- Notas de CRM pos-QBR (atividades, emails, calls do CSM) + feedback do CSM sobre o brief (campos de avaliacao na task ClickUp) + decisoes de renovacao registradas no CRM (ganho/perdido/negociado/downgrade) + outcomes de expansao (aceita/rejeitada + motivo) + gravacoes ou transcricoes de chamadas de QBR (se disponivel via integracao de call recording)

## Output

- Account Memory atualizado no Supabase por conta: historico de QBRs com outcomes, comprometimentos com status, expansoes tentadas e resultados, evolucao temporal de scores, feedback sobre qualidade dos briefs
- Relatorio mensal de aprendizado para o Maestro: quais tipos de brief geraram mais renovacoes saudaveis, quais sinais de expansao tiveram maior taxa de conversao, quais dimensoes do Renewal Readiness Score foram mais preditivas
- Calibracoes sugeridas para o modelo de pesos do Compass

## Trigger

Acionado quando CSM fecha task de renovacao no ClickUp (status: Renovado/Churn/Negociado/Expandido); acionado quando CSM adiciona nota de QBR no CRM; cron semanal para relatorio de aprendizado; acionado quando deck editado pelo CSM e re-salvo (detectado via Google Drive webhook)

## Knowledge base (o que o executor consulta)

- Schema do Account Memory no Supabase (historico de QBRs, comprometimentos, expansoes, scores)
- campos de CRM relevantes pos-QBR (Deal stage, notes, activity type, outcome)
- mapeamento de campos de feedback na task ClickUp
- modelo de classificacao de feedback de brief (positivo/negativo/sugestao)
- integracao com ferramentas de call recording (Gong, Chorus, ou nativo do CRM) se disponivel

## Action Items

1. Confirmar o gatilho e carregar a entrada (Notas de CRM pos-QBR (atividades, emails, calls do CSM) + feedback do CSM sobre o brief (campos de avaliacao na task Cl…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Account Memory atualizado no Supabase por conta: historico de QBRs com outcomes, comprometimentos com status, expansoes…) e persistir no artefato do squad.
4. Entregar ao critic Verity; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Account Memory atualizado no Supabase por conta: historico de QBRs com outcomes, comprometimentos com status, expansoes tentadas e resultados, evolucao tempora…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Verity registrado
- [ ] Gate HITL respeitado: Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pu…
- [ ] Gate HITL respeitado: Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e…
- [ ] Gate HITL respeitado: Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS a…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Proposta de expansao com valor acima de R$X (threshold configuravel por empresa) incluida no Renewal Package — Verity aprova o brief mas Pulse cria subtask de… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Deck de QBR pronto para envio ao cliente — o Slides gera e o Pulse notifica o CSM, mas o envio do link do deck ao cliente requer revisao e envio manual pelo CS… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Conta Enterprise com ARR > R$100k em janela de renovacao — brief aprovado mas task criada com flag de revisao obrigatoria pelo Head de CS antes do CSM iniciar… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Renewal Readiness Score com queda > 20 pontos em 48h — Verity bloqueia o ciclo, Maestro notifica analista de dados e CSM para validacao manual dos dados de ent… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Expansion Signal Report indicando oportunidade de cross-sell de produto diferente do contrato atual (nao e apenas upgrade de tier, e novo produto) — requer ali… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Comprometimento pendente do fornecedor detectado pelo Memory como nao entregue no periodo anterior — brief inclui o item mas Pulse cria subtask de 'Resolucao d… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Conta com Renewal Readiness Score CRITICO (< 50) e renovacao em < 30 dias — escalacao imediata para Head de CS e Account Executive senior com brief de situacao… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Feedback de Memory indicando que CSM fez edicao significativa no deck (> 30% do conteudo alterado) — Maestro abre HITL para CSM documentar o motivo da edicao e… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Verity | BLOQUEIA entrega |

## Handoff

- **to:** Verity
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
