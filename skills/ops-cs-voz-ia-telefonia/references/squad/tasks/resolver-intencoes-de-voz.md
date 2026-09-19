---
task: falco()
responsavel: "Falco"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Intencao classificada (status_pedido | info_conta | politica | faq_produto | prazo_entrega) + dados do cliente coletados (numero_pedido, CPF, nome) + contexto do CRM (historico, tier, pedidos ativos) + canal de origem (telefone ou whatsapp_audio)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta conversacional em texto (max 60 palavras para TTS) com: informacao factual verificada, linguagem natural PT-BR, proxima acao clara"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp com: intencao, dados consultados (IDs de sistema), resposta gerada, latencia de resolucao, confianca"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Audio TTS via Sono para o canal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro roteia intencao com confianca >= 0.80 para dominios: 'status_pedido', 'rastreamento', 'prazo_entrega', 'info_conta', 'politica_troca', 'faq_produto', 'horario_funcionamento', 'como_cancelar'"
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

# Resolver Intenções de Voz

**Task ID:** `falco()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Resolver Intenções de Voz |
| **status** | `pending` |
| **responsible_executor** | Falco (Falco — Worker de Resolucao por Voz) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em resolver as intencoes mais frequentes de voz em tempo real durante a chamada: status de pedido/entrega, informacoes de conta, politicas de troca, prazos e FAQs. Otimizado para resposta em < 3 segundos (voz exige latencia muito menor que texto). Consulta ERP, CRM e KB via MCP, monta resposta conversacional natural em PT-BR (sem leitura robotica de dados brutos — transforma '2026-06-15' em 'chega na proxima segunda-feira'), sintetiza em 2-3 frases no maximo (voz nao suporta paredes de texto), e oferece proxima acao clara ('Quer que eu ja abra a solicitacao de troca?'). Especializado nas top-5 intencoes por volume de voz identificadas na Discovery.

## Input

- Intencao classificada (status_pedido | info_conta | politica | faq_produto | prazo_entrega) + dados do cliente coletados (numero_pedido, CPF, nome) + contexto do CRM (historico, tier, pedidos ativos) + canal de origem (telefone ou whatsapp_audio)

## Output

- Resposta conversacional em texto (max 60 palavras para TTS) com: informacao factual verificada, linguagem natural PT-BR, proxima acao clara
- Task no ClickUp com: intencao, dados consultados (IDs de sistema), resposta gerada, latencia de resolucao, confianca
- Audio TTS via Sono para o canal

## Trigger

Maestro roteia intencao com confianca >= 0.80 para dominios: 'status_pedido', 'rastreamento', 'prazo_entrega', 'info_conta', 'politica_troca', 'faq_produto', 'horario_funcionamento', 'como_cancelar'

## Knowledge base (o que o executor consulta)

- API ERP para status e historico de pedidos (resposta em < 1.5s)
- API de transportadoras para rastreamento em tempo real
- KB vetorizada (Supabase pgvector) com FAQs e politicas
- otimizada para busca semantica rapida
- Templates de resposta conversacional por intencao (versao curta para TTS, sem bullets, sem numeracao)
- CRM para dados de conta e tier do cliente
- Tabela de conversao de datas e prazos para linguagem natural PT-BR

## Action Items

1. Confirmar o gatilho e carregar a entrada (Intencao classificada (status_pedido | info_conta | politica | faq_produto | prazo_entrega) + dados do cliente coletado…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resposta conversacional em texto (max 60 palavras para TTS) com: informacao factual verificada, linguagem natural PT-BR…) e persistir no artefato do squad.
4. Entregar ao critic Eco 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta conversacional em texto (max 60 palavras para TTS) com: informacao factual verificada, linguagem natural PT-BR, proxima acao clara
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

- **to:** Onda
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
