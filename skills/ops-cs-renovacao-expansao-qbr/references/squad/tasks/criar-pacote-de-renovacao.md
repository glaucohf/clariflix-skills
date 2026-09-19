---
task: pulse()
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "QBR Brief + Renewal Package + Expansion Signal Report (todos validados pelo Verity) + link do deck gerado pelo Slides + dados da conta (CSM responsavel, data de renovacao, MRR, segmento) + mapeamento de listas/projetos ClickUp por CSM + configuracao de prazos por tipo de tarefa e nivel de urgencia"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de renovacao criado no ClickUp: task principal com todas as subtasks, campos preenchidos, checklists, prazos e prioridade"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Link da task principal retornado ao Maestro"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Notificacao Slack para o CSM com resumo de 3 linhas (conta, renovacao em X dias, Renewal Readiness Score, maior oportunidade de expansao se aplicavel) e links diretos para task e deck"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Log de ativacao no Supabase"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "Alerta de escalacao se task nao aberta em 48h para ALTA urgencia ou 24h para CRITICA"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Maestro apos todos os artefatos do Briefer/Scout/Slides estarem aprovados pelo Verity para uma conta; cron de monitoramento de tasks nao abertas a cada 6h; cron semanal para relatorio d…"
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

# Criar Pacote De Renovacao

**Task ID:** `pulse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Renovacao, Expansao e QBR Automatizado

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Criar Pacote De Renovacao |
| **status** | `pending` |
| **responsible_executor** | Pulse (Pulse — Agente de Ativacao e Orquestracao de Tarefas) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 5 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Recebe os artefatos aprovados (QBR Brief, Renewal Package, Expansion Signal Report, link do deck) e cria no ClickUp a estrutura completa de tarefas para o CSM executar a renovacao ou QBR. Nao cria apenas uma task — cria um 'pacote de renovacao' no ClickUp: (1) Task principal 'QBR/Renovacao — [Nome da Conta]' com prazo calculado (45 dias antes da data de renovacao para QBR, 15 dias antes para Renewal Review), prioridade correta, brief completo em descricao, link para o deck, Renewal Readiness Score com link para dashboard, e checklist de preparacao (confirmar agenda com cliente, revisar deck, verificar compromissos pendentes, preparar proposta de expansao se aplicavel); (2) Subtask de 'Preparacao de Expansao' se Scout detectou oportunidade de alto valor — com Expansion Signal Report e script de conversa; (3) Subtask de 'Follow-up pos-QBR' com template de follow-up email e prazo de 48h apos a data de reuniao. Monitora abertura e progresso das tasks e escala para manager se task principal nao for aberta em 48h apos criacao.

## Input

- QBR Brief + Renewal Package + Expansion Signal Report (todos validados pelo Verity) + link do deck gerado pelo Slides + dados da conta (CSM responsavel, data de renovacao, MRR, segmento) + mapeamento de listas/projetos ClickUp por CSM + configuracao de prazos por tipo de tarefa e nivel de urgencia

## Output

- Pacote de renovacao criado no ClickUp: task principal com todas as subtasks, campos preenchidos, checklists, prazos e prioridade
- Link da task principal retornado ao Maestro
- Notificacao Slack para o CSM com resumo de 3 linhas (conta, renovacao em X dias, Renewal Readiness Score, maior oportunidade de expansao se aplicavel) e links diretos para task e deck
- Log de ativacao no Supabase
- Alerta de escalacao se task nao aberta em 48h para ALTA urgencia ou 24h para CRITICA

## Trigger

Acionado pelo Maestro apos todos os artefatos do Briefer/Scout/Slides estarem aprovados pelo Verity para uma conta; cron de monitoramento de tasks nao abertas a cada 6h; cron semanal para relatorio de cobertura de renovacoes (% de renovacoes nos proximos 30 dias com pacote criado no ClickUp)

## Knowledge base (o que o executor consulta)

- Mapeamento de CSMs para listas e projetos no ClickUp (atualizado quando CSM muda de carteira)
- templates de task de renovacao/QBR/expansao (campos obrigatorios, checklists padrao, status workflow)
- regras de prazo e prioridade por dias ate renovacao e por Renewal Readiness Score
- mapeamento de CSMs para canais Slack
- historico de tasks criadas (para evitar duplicatas)
- templates de follow-up email pos-QBR por segmento

## Action Items

1. Confirmar o gatilho e carregar a entrada (QBR Brief + Renewal Package + Expansion Signal Report (todos validados pelo Verity) + link do deck gerado pelo Slides +…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de renovacao criado no ClickUp: task principal com todas as subtasks, campos preenchidos, checklists, prazos e p…) e persistir no artefato do squad.
4. Entregar ao critic Verity; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de renovacao criado no ClickUp: task principal com todas as subtasks, campos preenchidos, checklists, prazos e prioridade
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

- **to:** Memory
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
