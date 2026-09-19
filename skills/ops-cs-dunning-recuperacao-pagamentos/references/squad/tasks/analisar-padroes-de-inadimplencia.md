---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Historico completo de cobracas e outcomes no Supabase (tabelas: dunning_sequences, payment_attempts, negotiation_outcomes, message_delivery_log) + dados do gateway de pagamento (categorias de falha, taxas de retry, status de chargebacks) + dados do CRM (segmento, MRR, tempo de casa por cliente) + log de tasks do ClickUp (tempo de resolucao de HITL, outcomes de negociacao manual)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório semanal de recuperação (markdown + tabelas): MRR recuperado vs em risco, taxa de recuperação por sequência e por canal, top-5 causas de falha de pagamento, cohort de inadimplentes por behavior, padrões de recorrência detectados, recomendações de ajuste do playbook priorizadas por impacto estimado"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alerta imediato ao Cobalt quando detecta spike de falhas acima de 2 desvios padrão (sugere problema técnico no gateway)"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Lista de clientes com inadimplência recorrente para ação preventiva (mudança de data de cobrança)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Cron semanal (segunda-feira 07h) para relatório completo; cron diário (09h) para detecção de anomalias e spikes; acionado pelo Cobalt quando uma cobrança é marcada como bad debt (para atualizar cohor…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Sentinel antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes com menos de 3 meses de casa) — Flex classifica e cria task HITL urgente no ClickUp para o time financeiro com histórico completo e valor em risco"
    - "[ ] HITL: Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar no gateway e no CRM, e responde ao cliente confirmando que um humano vai verificar em até X horas"
    - "[ ] HITL: Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task de retenção para o CSM com contexto completo: cliente já estava em inadimplência + agora solicitou cancelamento = risco crítico combinado"
    - "[ ] HITL: Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgente para o Head Financeiro e para o CSM responsável da conta, com sugestão de abordagem via chamada telefônica"
    - "[ ] HITL: Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema no gateway de pagamento, no processador ou na infraestrutura (não é inadimplência — é incidente têcnico)"
---

# Analisar Padroes De Inadimplencia

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Padroes De Inadimplencia |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — Analista de Performance e Padrões de Inadimplência) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora o desempenho global das sequências de recuperação, identifica padrões de inadimplência recorrente, detecta anomalias sistemáticas (ex: spike de falhas por categoria em uma data específica sugere problema técnico no gateway), e gera insights para calibração contínua do playbook. Atlas: (1) Calcula taxas de recuperação por sequência, por step, por canal, por dia da semana e por horário de envio — identifica quais combinações têm melhor performance e sugere ajustes no timing do Dante; (2) Segmenta inadimplentes em cohorts: quem paga no 1º contato, quem precisa de 3-5 tentativas, quem nunca paga (bad debt) — cada cohort tem implicações diferentes para o playbook; (3) Detecta clientes com padrão de inadimplência recorrente (falhando no mesmo período todo mês = saldo insuficiente na data de débito — sugerir mudança de dia de cobrança como ação preventiva); (4) Gera relatório semanal de recuperação para o Head Financeiro/CS com MRR recuperado, MRR em bad debt, distribuição de causas de falha e recomendações de ajuste; (5) Identifica spikes de falha que sugerem problema técnico vs sazonalidade esperada.

## Input

- Historico completo de cobracas e outcomes no Supabase (tabelas: dunning_sequences, payment_attempts, negotiation_outcomes, message_delivery_log) + dados do gateway de pagamento (categorias de falha, taxas de retry, status de chargebacks) + dados do CRM (segmento, MRR, tempo de casa por cliente) + log de tasks do ClickUp (tempo de resolucao de HITL, outcomes de negociacao manual)

## Output

- Relatório semanal de recuperação (markdown + tabelas): MRR recuperado vs em risco, taxa de recuperação por sequência e por canal, top-5 causas de falha de pagamento, cohort de inadimplentes por behavior, padrões de recorrência detectados, recomendações de ajuste do playbook priorizadas por impacto estimado
- Alerta imediato ao Cobalt quando detecta spike de falhas acima de 2 desvios padrão (sugere problema técnico no gateway)
- Lista de clientes com inadimplência recorrente para ação preventiva (mudança de data de cobrança)

## Trigger

Cron semanal (segunda-feira 07h) para relatório completo; cron diário (09h) para detecção de anomalias e spikes; acionado pelo Cobalt quando uma cobrança é marcada como bad debt (para atualizar cohort e modelo); acionado sob demanda pelo Head Financeiro via comando no ClickUp

## Knowledge base (o que o executor consulta)

- Schema completo do Supabase (dunning_sequences, payment_attempts, message_delivery_log, negotiation_outcomes), mapeamento de categorias de falha do gateway (decline_code por provedor: Stripe, Asaas, Iugu), modelo de detecção de anomalia estatística (Z-score sobre taxa de falha diária), histórico de sazonalidades de inadimplência (fim de mês, férias, datas comemorativas com impacto em pagamentos), benchmarks setoriais de taxa de recuperação de dunning (referência: Stripe Radar dados públicos), templates de relatório executivo para Head Financeiro

## Action Items

1. Confirmar o gatilho e carregar a entrada (Historico completo de cobracas e outcomes no Supabase (tabelas: dunning_sequences, payment_attempts, negotiation_outcom…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório semanal de recuperação (markdown + tabelas): MRR recuperado vs em risco, taxa de recuperação por sequência e…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório semanal de recuperação (markdown + tabelas): MRR recuperado vs em risco, taxa de recuperação por sequência e por canal, top-5 causas de falha de paga…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Sentinel registrado
- [ ] Gate HITL respeitado: Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dia…
- [ ] Gate HITL respeitado: Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time fin…
- [ ] Gate HITL respeitado: Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Negociação financeira acima do threshold pre-aprovado (parcelamento em mais de 3x, desconto de multa acima de 50%, extensão acima de 15 dias ou para clientes c… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Cliente contesta a cobranca (afirma nao dever ou que e erro de cobranca) — Flex bloqueia sequencia imediatamente, cria task para o time financeiro/CS verificar… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Cliente solicita cancelamento durante o fluxo de cobrança — Cobalt interrompe sequência de dunning, aciona o Squad de Churn Prediction (se ativo) e cria task d… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Cobrança de alto valor (MRR > R$5k ou fatura acima de R$10k) chegou ao step D7 sem recuperação — Cobalt interrompe sequência automática e cria task HITL urgent… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Spíke de falhas de pagamento acima de 2 desvios padrão detectado pelo Atlas — alerta imediato ao time têcnico e ao Head Financeiro para verificar se é problema… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Sentinel reprova uma mensagem por violação de compliance legal (CDC/LGPD) — bloqueia o disparo, notifica o Head Jurídico e o responsável de CS via Slack, e sus… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Cliente com histórico de chargeback ou de fraude identificado pelo gateway — Cobalt bloqueia a sequência de dunning automática e cria task manual para o time f… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Bad debt confirmado (cobranca nao recuperada apos sequencia completa + tentativas manuais) — Cobalt fecha a sequencia como IRRECUPERAVEL, Atlas atualiza o coho… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Sentinel | BLOQUEIA entrega |

## Handoff

- **to:** Vault
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
