---
task: spark()
responsavel: "Spark"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Brief de retenção validado pelo Critic + dados da conta (CSM responsável, ID no CRM, MRR, renovação) + mapeamento de projetos/listas do ClickUp por CSM + configuração de prazos por nível de risco"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Task criada no ClickUp com todos os campos preenchidos e link retornado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Notificação Slack enviada ao CSM com resumo executivo de 2 linhas e link direto para a task"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Se task não aberta em 24h (CRÍTICO) ou 48h (ALTO): alerta de escalação criado para manager do CS"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Log de ativação no Supabase com timestamp e ID da task"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Orchestrator Nexus após Critic Argus aprovar o brief; acionado diariamente para batch de contas em risco; webhook de monitoramento de tarefas não iniciadas a cada 6h"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguardando Aprovação' antes de ativar o CSM com essa ação específica"
    - "[ ] HITL: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualquer contato"
    - "[ ] HITL: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analista de dados"
    - "[ ] HITL: Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo batch"
    - "[ ] HITL: Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar"
---

# Criar Task Retenção

**Task ID:** `spark()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Predição e Prevenção de Churn

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Criar Task Retenção |
| **status** | `pending` |
| **responsible_executor** | Spark (Spark — Agente de Ativação no ClickUp) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe o brief validado pelo Critic Argus e cria a task de retencao no ClickUp para o CSM responsavel. A task e criada no projeto correto do CSM, com prioridade correta (URGENTE para CRITICO, ALTA para ALTO), prazo automatico calculado (conta CRITICO com renovacao em < 30 dias: prazo 24h; demais: 72h), todos os campos preenchidos (titulo padronizado, descricao com brief completo, checklist de steps recomendados, campo de health score com link para dashboard, campo de next-best-action), e notificacao via Slack para o CSM. Monitora se a task foi aberta e iniciada dentro do prazo — se nao, escalona para o manager do CS com alerta de risco de SLA de retencao.

## Input

- Brief de retenção validado pelo Critic + dados da conta (CSM responsável, ID no CRM, MRR, renovação) + mapeamento de projetos/listas do ClickUp por CSM + configuração de prazos por nível de risco

## Output

- Task criada no ClickUp com todos os campos preenchidos e link retornado
- Notificação Slack enviada ao CSM com resumo executivo de 2 linhas e link direto para a task
- Se task não aberta em 24h (CRÍTICO) ou 48h (ALTO): alerta de escalação criado para manager do CS
- Log de ativação no Supabase com timestamp e ID da task

## Trigger

Acionado pelo Orchestrator Nexus após Critic Argus aprovar o brief; acionado diariamente para batch de contas em risco; webhook de monitoramento de tarefas não iniciadas a cada 6h

## Knowledge base (o que o executor consulta)

- Mapeamento de CSMs para listas/projetos no ClickUp, template de task de retenção (campos obrigatórios, checklists, status workflow), regras de prazo e prioridade por nível de risco e por dias até renovação, mapeamento de CSMs para canais Slack, histórico de tasks criadas (para evitar duplicatas e para tracking de save rate)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Brief de retenção validado pelo Critic + dados da conta (CSM responsável, ID no CRM, MRR, renovação) + mapeamento de pr…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Task criada no ClickUp com todos os campos preenchidos e link retornado) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Task criada no ClickUp com todos os campos preenchidos e link retornado
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cri…
- [ ] Gate HITL respeitado: Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de…
- [ ] Gate HITL respeitado: Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Ações de retenção com desconto financeiro (qualquer percentual de desconto em contrato ou crédito) — Mira gera a recomendação mas Spark cria task como 'Aguarda… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Conta Enterprise com MRR > R$15k em risco CRITICO — brief aprovado pelo Critic mas task criada com flag de revisao obrigatoria pelo Head de CS antes de qualque… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Health score com queda > 25 pontos em 24h sem evento crítico documentado — Argus bloqueia o disparo, solicita validação manual dos dados de entrada pelo analis… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Detecção de intenção explícita de cancelamento (via Iris) — task criada com prioridade URGENTE e notificação imediata para CSM e manager, sem esperar o ciclo b… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Ação de retenção que envolve reunião com Executive Sponsor ou C-level do cliente — requer aprovação do Head de CS antes do CSM agendar | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Brief com conflito entre next-best-action do Mira e comprometimento prévio do CSM registrado no CRM — Argus detecta e eleva para revisão humana antes de criar… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Primeiro alerta de churn em conta que nunca teve nenhuma ação de CS registrada (conta 'orphan') — escalona para Head de CS para atribuição e onboarding de rela… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Critic Argus reprova brief por evidência insuficiente (score < 36/40) após 2 iterações de melhoria — escalona para analista humano revisar os dados de entrada… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Iris
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
