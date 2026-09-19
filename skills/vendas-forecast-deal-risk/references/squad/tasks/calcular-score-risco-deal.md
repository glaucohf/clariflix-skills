---
task: oracle()
responsavel: "Oracle"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de risco do Argus + perfil completo do deal (CRM data dump) + modelo de scoring calibrado com histórico do cliente + benchmarks de velocity por segmento/produto"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score de risco por deal (0-100), probabilidade de fechamento no período (%), categoria de risco (Verde/Amarelo/Vermelho/Morto), top-3 fatores de risco com peso, recomendação de ação (intervenção urgente / nurture / monitorar / arquivar)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento de risco recebido da Cassandra + atualização diária do score de todos os deals ativos (job 06h00) + mudança manual de estágio no CRM"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Nemesis antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora da empresa"
    - "[ ] L3: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM"
    - "[ ] L2: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa"
    - "[ ] L2: Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle"
    - "[ ] L1: Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal"
---

# Calcular Score Risco Deal

**Task ID:** `oracle()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Forecast de Pipeline e Risco de Deal

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Score Risco Deal |
| **status** | `pending` |
| **responsible_executor** | Oracle (Oracle — Calculista de Risco) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de scoring preditivo de deal risk. Recebe eventos do Argus e calcula probabilidade de fechamento e score de risco para cada deal usando modelo treinado nos dados históricos do cliente. Considera: velocity do deal vs. benchmark histórico, número de stakeholders engajados, qualidade das últimas interações, proximidade do fim de trimestre, tamanho do deal vs. ciclo médio.

## Input

- Evento de risco do Argus + perfil completo do deal (CRM data dump) + modelo de scoring calibrado com histórico do cliente + benchmarks de velocity por segmento/produto

## Output

- Score de risco por deal (0-100), probabilidade de fechamento no período (%), categoria de risco (Verde/Amarelo/Vermelho/Morto), top-3 fatores de risco com peso, recomendação de ação (intervenção urgente / nurture / monitorar / arquivar)

## Trigger

Evento de risco recebido da Cassandra + atualização diária do score de todos os deals ativos (job 06h00) + mudança manual de estágio no CRM

## Knowledge base (o que o executor consulta)

- Modelo preditivo treinado nos dados históricos do cliente (won/lost/stalled), benchmarks de ciclo de vendas por segmento, matriz de risco por estágio x dias x valor, histórico de intervenções e seus resultados (feedback loop)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de risco do Argus + perfil completo do deal (CRM data dump) + modelo de scoring calibrado com histórico do clien…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score de risco por deal (0-100), probabilidade de fechamento no período (%), categoria de risco (Verde/Amarelo/Vermelho…) e persistir no artefato do squad.
4. Entregar ao critic Nemesis; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score de risco por deal (0-100), probabilidade de fechamento no período (%), categoria de risco (Verde/Amarelo/Vermelho/Morto), top-3 fatores de risco com peso…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Nemesis registrado
- [ ] Gate L3 respeitado: Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem…
- [ ] Gate L3 respeitado: Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM
- [ ] Gate L2 respeitado: Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Envio de alerta de risco para contato externo (cliente/prospect): Nemesis valida, humano confirma antes do Hermes enviar qualquer mensagem que saia para fora d… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Recomendação de arquivar deal (classificado como Morto): gestor deve confirmar antes de qualquer mudança de estágio no CRM | BLOQUEIA até decisão humana |
| VETO-003 | L2 — Sugestão de próximo passo pelo Cronos: closer recebe sugestão no ClickUp/Slack e aprova ou edita antes de criação da tarefa | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Ajuste de thresholds de alerta proposto pela Mnemosine: gestor valida antes de aplicar ao modelo de scoring do Oracle | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Forecast de pipeline enviado para o board: gestor comercial revisa o relatório da Sibila antes do envio formal | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Nemesis | BLOQUEIA entrega |

## Handoff

- **to:** Sibila
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
