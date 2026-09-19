---
task: onda()
responsavel: "Onda"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Intencao de acao transacional (abrir_troca | registrar_reclamacao | atualizar_cadastro | agendar_callback | solicitar_cancelamento | solicitar_refund) + dados coletados e validados pelo Vivo + contexto do CRM + confirmacao verbal do cliente (obrigatoria para acoes irreversiveis) + tier do cliente e limites de autonomia aplicaveis"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Confirmacao de acao executada com numero de protocolo, prazo de resolucao e proximo passo"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Registro de consentimento verbal (timestamp + transcricao da confirmacao) como prova juridica"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp com: acao executada, sistema(s) afetados, IDs de referencia, confirmacao do cliente, nivel de autonomia usado"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Audio TTS de confirmacao para o cliente"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro roteia intencao de acao com verbos de escrita: 'abrir', 'cancelar', 'trocar', 'registrar', 'agendar', 'atualizar', 'solicitar'; Falco conclui consulta e cliente pede para executar acao na mes…"
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

# Escrever Ações Transacionais

**Task ID:** `onda()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Escrever Ações Transacionais |
| **status** | `pending` |
| **responsible_executor** | Onda (Onda — Worker de Acao & Transacao por Voz) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em executar acoes transacionais solicitadas por voz que requerem escrita em sistemas: abertura de solicitacao de troca/devolucao, registro de reclamacao formal, atualizacao de dados cadastrais, agendamento de callback humano, cancelamento de servico. Diferente do Falco (que so lê dados), o Onda escreve nos sistemas. Para acoes financeiras (refund) ou irreversiveis (cancelamento): obrigatoriamente pede confirmacao verbal ao cliente ('Para confirmar o cancelamento, diga SIM ou pressione 1') e registra essa confirmacao como prova de consentimento no log. Acima dos limites de autonomia L2, eleva para L3 e aciona HITL antes de executar.

## Input

- Intencao de acao transacional (abrir_troca | registrar_reclamacao | atualizar_cadastro | agendar_callback | solicitar_cancelamento | solicitar_refund) + dados coletados e validados pelo Vivo + contexto do CRM + confirmacao verbal do cliente (obrigatoria para acoes irreversiveis) + tier do cliente e limites de autonomia aplicaveis

## Output

- Confirmacao de acao executada com numero de protocolo, prazo de resolucao e proximo passo
- Registro de consentimento verbal (timestamp + transcricao da confirmacao) como prova juridica
- Task no ClickUp com: acao executada, sistema(s) afetados, IDs de referencia, confirmacao do cliente, nivel de autonomia usado
- Audio TTS de confirmacao para o cliente

## Trigger

Maestro roteia intencao de acao com verbos de escrita: 'abrir', 'cancelar', 'trocar', 'registrar', 'agendar', 'atualizar', 'solicitar'; Falco conclui consulta e cliente pede para executar acao na mesma sessao ('ja que e isso, pode abrir a troca pra mim?')

## Knowledge base (o que o executor consulta)

- API do helpdesk (Zendesk/Intercom) para abertura de tickets por tipo
- API do sistema de logistica reversa para abertura de solicitacoes de troca
- API do ERP para atualizacao de cadastro
- Sistema de agendamento de callbacks (Google Calendar ou Aircall scheduling)
- Politicas de autonomia por tipo de acao e valor (limite de R$200 automatico, R$200-500 L3, acima HITL)
- Scripts de confirmacao verbal por acao ('Para confirmar [acao], diga SIM claramente')
- Regras de LGPD para registro de consentimento verbal

## Action Items

1. Confirmar o gatilho e carregar a entrada (Intencao de acao transacional (abrir_troca | registrar_reclamacao | atualizar_cadastro | agendar_callback | solicitar_c…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Confirmacao de acao executada com numero de protocolo, prazo de resolucao e proximo passo) e persistir no artefato do squad.
4. Entregar ao critic Eco 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Confirmacao de acao executada com numero de protocolo, prazo de resolucao e proximo passo
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

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
