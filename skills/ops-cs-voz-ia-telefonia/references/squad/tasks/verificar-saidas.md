---
task: eco2Verificar()
responsavel: "Eco 2"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] HITL: Acao transacional acima do limite de autonomia: refund > R$200, cancelamento de contrato, alteracao de dados bancarios — Onda eleva para L3 e Hertz cria ticket prioritario antes de executar"
    - "[ ] HITL: Confianca ASR < 0.78 em dado critico (CPF, numero de pedido, valor) — Sono solicita confirmacao verbal ao cliente; se terceira tentativa falhar, Hertz escalona para humano"
    - "[ ] HITL: Radar detecta nivel de risco CRITICO: mencao de PROCON, advogado, processo judicial, Reclame Aqui, imprensa — pipeline bloqueia e Hertz transfere imediatamente para supervisor"
    - "[ ] HITL: Critic Eco retorna score total < 30 ou qualquer flag de risco legal, LGPD ou seguranca de dados — nenhuma resposta enviada ao cliente sem revisao humana"
    - "[ ] HITL: Terceira sessao sem resolucao do mesmo problema na semana — padrao de problema recorrente detectado pelo Radar, Hertz agenda callback prioritario com especialista"
---

# Verificar Saídas do Voz-IA para Atendimento Telefônico

**Task ID:** `eco2Verificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Voz-IA para Atendimento Telefônico (PT-BR)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Voz-IA para Atendimento Telefônico |
| **status** | `pending` |
| **responsible_executor** | Eco 2 (Eco — Critic de Qualidade de Voz) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Eco — Critic de Qualidade de Voz — Valida cada resposta gerada pelos workers antes da sintese TTS e envio ao cliente. Rubrica especifica para voz em 5 dimensoes: NATURALIDADE (soa como humano em voz alta, sem bullets ou linguagem de email), BREVIDADE (max 3 frases para telefone, max 5 para WhatsApp audio), FACTUALIDADE (informacoes verificaveis nos sistemas consultados, sem dados inventados), COMPLIANCE (nao cria obrigacoes nao autorizadas, nao promete fora do escopo autonomo), EMPATIA (tom adequado ao sentimento detectado pelo Radar — validacao emocional antes de dados quando cliente esta frustrado). Score minimo para TTS: 42/50. Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve ao worker com feedback especifico e sugestao de reformulacao. Score < 30 ou flag de risco legal/LGPD: bloqueia pipeline e escalona para HITL via Hertz imediatamente.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Critic de Qualidade de Voz
- Valida cada resposta gerada pelos workers antes da sintese TTS e envio ao cliente
- Rubrica especifica para voz em 5 dimensoes: NATURALIDADE (soa como humano em voz alta, sem bullets ou linguagem de email), BREVIDADE (max 3 frases para telefone, max 5 para WhatsApp audio), FACTUALIDADE (informacoes verificaveis nos sistemas consultados, sem dados inventados), COMPLIANCE (nao cria obrigacoes nao autorizadas, nao promete fora do escopo autonomo), EMPATIA (tom adequado ao sentimento detectado pelo Radar
- validacao emocional antes de dados quando cliente esta frustrado)
- Score minimo para TTS: 42/50
- Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve ao worker com feedback especifico e sugestao de reformulacao
- Score < 30 ou flag de risco legal/LGPD: bloqueia pipeline e escalona para HITL via Hertz imediatamente

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Maestro para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** Maestro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
