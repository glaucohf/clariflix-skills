---
task: hertz()
responsavel: "Hertz"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal de escalonamento do Maestro ou do Critic Eco + transcricao completa da sessao + acoes executadas + sentimento detectado pelo Radar + dados do cliente (tier, MRR, historico) + motivo de escalonamento classificado (confianca_baixa | acao_irreversivel | risco_legal | cliente_agitado | sem_resolucao | vip_cliente)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Transferencia de chamada com briefing verbal ao agente humano (TTS de 15-20 segundos) OU confirmacao de callback agendado com data/hora OU ticket criado no helpdesk com prioridade e resumo em 5 bullets"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Notificacao Slack para fila correta com preview de contexto"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp com motivo de escalonamento, contexto completo e SLA esperado para resolucao humana"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Mensagem de transicao ao cliente ('vou te transferir agora para [nome da fila], tempo de espera estimado: X minutos')"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Critic Eco retorna score < 42 ou flag de risco; Maestro detecta confianca < 0.75 apos 2 turns de coleta; Radar injeta alerta de risco critico (nivel vermelho ou critico); Onda identifica acao acima d…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Eco 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket prioritario antes de executar"
    - "[ ] HITL: Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona para humano"
    - "[ ] HITL: Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente para supervisor"
    - "[ ] HITL: Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana"
    - "[ ] HITL: Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especialista"
---

# Gerenciar Transferência para Humanos

**Task ID:** `hertz()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerenciar Transferência para Humanos |
| **status** | `pending` |
| **responsible_executor** | Hertz (Hertz — Agente de Handoff & Escalonamento Telefonico) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia a transferencia para humanos em contexto de voz — mais critico que em texto porque o cliente esta em tempo real na linha. Especializado em: (1) transferencia quente para agente humano com briefing verbal instantaneo ao atendente antes de conectar o cliente ('transferindo agora, cliente Carlos, pedido #12345, quer cancelar por atraso, ja tentamos oferecer voucher, nao aceitou, tier Gold'); (2) agendamento de callback com janela de horario confirmada pelo cliente ('posso te ligar amanha entre 9h e 11h?'); (3) criacao de ticket no helpdesk com transcricao completa, sentimento, acoes tentadas e sugestao de resolucao para o humano; (4) notificacao de escalonamento urgente no Slack da fila correta. Para clientes VIP/Enterprise: alerta direto para o CSM responsavel via DM no Slack.

## Input

- Sinal de escalonamento do Maestro ou do Critic Eco + transcricao completa da sessao + acoes executadas + sentimento detectado pelo Radar + dados do cliente (tier, MRR, historico) + motivo de escalonamento classificado (confianca_baixa | acao_irreversivel | risco_legal | cliente_agitado | sem_resolucao | vip_cliente)

## Output

- Transferencia de chamada com briefing verbal ao agente humano (TTS de 15-20 segundos) OU confirmacao de callback agendado com data/hora OU ticket criado no helpdesk com prioridade e resumo em 5 bullets
- Notificacao Slack para fila correta com preview de contexto
- Task no ClickUp com motivo de escalonamento, contexto completo e SLA esperado para resolucao humana
- Mensagem de transicao ao cliente ('vou te transferir agora para [nome da fila], tempo de espera estimado: X minutos')

## Trigger

Critic Eco retorna score < 42 ou flag de risco; Maestro detecta confianca < 0.75 apos 2 turns de coleta; Radar injeta alerta de risco critico (nivel vermelho ou critico); Onda identifica acao acima do limite de autonomia; cliente solicita explicitamente 'quero falar com humano'; 3 turns de sessao sem progressao; cliente VIP/Enterprise com qualquer acao irreversivel

## Knowledge base (o que o executor consulta)

- Matriz de escalonamento por motivo x tier de cliente x horario (fila de plantao vs comercial)
- Scripts de briefing verbal por tipo de escalonamento (max 20 segundos para nao deixar cliente esperando)
- SLAs de callback por tier (VIP: 2h, Standard: next business day)
- Disponibilidade de filas humanas em tempo real (via Aircall API)
- Lista de CSMs responsaveis por conta para escalonamento direto
- Templates de ticket por motivo de escalonamento com campos pre-preenchidos

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sinal de escalonamento do Maestro ou do Critic Eco + transcricao completa da sessao + acoes executadas + sentimento det…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Transferencia de chamada com briefing verbal ao agente humano (TTS de 15-20 segundos) OU confirmacao de callback agenda…) e persistir no artefato do squad.
4. Entregar ao critic Eco 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Transferencia de chamada com briefing verbal ao agente humano (TTS de 15-20 segundos) OU confirmacao de callback agendado com data/hora OU ticket criado no hel…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Eco 2 registrado
- [ ] Gate HITL respeitado: Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3…
- [ ] Gate HITL respeitado: Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa fa…
- [ ] Gate HITL respeitado: Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz tra…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especiali… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Cliente VIP, Enterprise ou MRR > R$5k: toda acao irreversivel (cancelamento, mudanca de plano, refund parcial) requer aprovacao do CSM responsavel antes da exe… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Audio com duracao > 3 minutos e confianca media ASR < 0.82 — transcricao marcada para revisao humana antes do processamento completo pelo Maestro | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Intencao nao reconhecida apos 2 turns de coleta pelo Vivo (confianca < 0.55) — Hertz escalona com transcricao completa para o humano interpretar e resolver | BLOQUEIA até decisão humana |
| VETO-009 | HITL — Solicitacao de dados de terceiros, portabilidade de dados, ou qualquer direito LGPD em voz — Hertz bloqueia automacao e direciona para DPO/time juridico | BLOQUEIA até decisão humana |
| VETO-010 | Saída sem veredito do critic Eco 2 | BLOQUEIA entrega |

## Handoff

- **to:** Eco 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
