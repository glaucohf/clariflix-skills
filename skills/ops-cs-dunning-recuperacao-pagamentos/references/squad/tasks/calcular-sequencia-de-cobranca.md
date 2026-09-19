---
task: dante()
responsavel: "Dante"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Evento de início de sequência do Cobalt (perfil do cliente, sequência selecionada, canais disponíveis) + estado atual da sequência no Supabase (steps já executados, respostas recebidas, último contato) + configuração do playbook (templates por step, timing por canal e por perfil) + fuso horário e preferências de contato do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Instrução de disparo estruturada para o Dispatcher correto: canal selecionado, template ID, horário agendado, contexto de personalização (nome, valor em atraso, link de pagamento, opções de negociação disponíveis neste step)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registro do step agendado no Supabase com timestamp"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alerta para o Cobalt se a sequência atingiu o step final sem recuperação (sinaliza para escalonamento)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Acionado pelo Cobalt no início de cada nova sequência; acionado via cron do LangGraph quando o horário do próximo step é atingido; acionado por evento de resposta do cliente (recalcular próximo step…"
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

# Calcular Sequência De Cobrança

**Task ID:** `dante()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Cobranca e Recuperacao de Pagamentos (Dunning Agetico)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Sequência De Cobrança |
| **status** | `pending` |
| **responsible_executor** | Dante (Dante — Sequencer de Cadência e Timing) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsavel por calcular e gerenciar o timing preciso de cada etapa da sequencia de recuperacao. Para cada cobranca ativa, Dante determina: (1) QUANDO enviar o proximo contato — janela de maior taxa de resposta por canal (email: 9h-11h e 14h-16h dias uteis; WhatsApp: 8h-20h com pico 10h e 18h; SMS: 9h-18h), ajustada para o fuso horario do cliente e para o dia da semana (evitar sexta > 17h, sabado e domingo para cobracas de menor urgencia); (2) QUAL step da sequencia executar — qual e o proximo contato nao realizado na sequencia do perfil do cliente, levando em conta o que ja foi enviado e qual foi a resposta; (3) QUAL template e canal priorizar neste step — escalada progressiva: informativo > urgente > negociacao > ultima chance, com canal alternado (email > WhatsApp > SMS > combinados); (4) SE deve pausar a sequencia — se o cliente acabou de abrir um ticket de contestacao, se ha pagamento parcial detectado, se o CSM registrou contato manual no CRM. Persiste o estado da sequencia no Supabase e agenda o proximo disparo via cron do LangGraph.

## Input

- Evento de início de sequência do Cobalt (perfil do cliente, sequência selecionada, canais disponíveis) + estado atual da sequência no Supabase (steps já executados, respostas recebidas, último contato) + configuração do playbook (templates por step, timing por canal e por perfil) + fuso horário e preferências de contato do cliente

## Output

- Instrução de disparo estruturada para o Dispatcher correto: canal selecionado, template ID, horário agendado, contexto de personalização (nome, valor em atraso, link de pagamento, opções de negociação disponíveis neste step)
- Registro do step agendado no Supabase com timestamp
- Alerta para o Cobalt se a sequência atingiu o step final sem recuperação (sinaliza para escalonamento)

## Trigger

Acionado pelo Cobalt no início de cada nova sequência; acionado via cron do LangGraph quando o horário do próximo step é atingido; acionado por evento de resposta do cliente (recalcular próximo step com base na resposta); acionado por evento de pagamento parcial (ajustar sequência para saldo remanescente)

## Knowledge base (o que o executor consulta)

- Playbook de dunning calibrado no Deep Dive (sequências por perfil: QUICK_WIN / STANDARD / HIGH_VALUE / ENTERPRISE), regras de timing por canal e por fuso horário, regras de pausa de sequência (contestação aberta, pagamento parcial, contato manual do CSM), histórico de taxas de resposta por horário e canal (calibrado com dados reais após 30 dias de operação), restrições legais de horário de cobrança (CDC: 8h-20h dias úteis, proibido domingos e feriados), mapeamento de templates por step e por canal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Evento de início de sequência do Cobalt (perfil do cliente, sequência selecionada, canais disponíveis) + estado atual d…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Instrução de disparo estruturada para o Dispatcher correto: canal selecionado, template ID, horário agendado, contexto…) e persistir no artefato do squad.
4. Entregar ao critic Sentinel; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Instrução de disparo estruturada para o Dispatcher correto: canal selecionado, template ID, horário agendado, contexto de personalização (nome, valor em atraso…
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

- **to:** Iris
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
