---
task: argusVerificar()
responsavel: "Argus"
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
    - "[ ] HITL: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário"
    - "[ ] HITL: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo"
    - "[ ] HITL: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados"
    - "[ ] HITL: Terceira interação na mesma sessão sem resolução confirmada pelo cliente"
    - "[ ] HITL: Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação"
---

# Verificar Saídas do Suporte Conversacional Multicanal

**Task ID:** `argusVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Suporte Conversacional Multicanal (Tier-1 Resolver)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Suporte Conversacional Multicanal |
| **status** | `pending` |
| **responsible_executor** | Argus (Argus — Critic de Qualidade & Compliance) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Argus — Critic de Qualidade & Compliance — Valida cada resposta gerada pelos workers antes do envio externo ao cliente. Rubrica de 5 dimensoes: (1) TOM — adequado ao canal e sentimento do cliente (0-10); (2) COMPLIANCE — nao promete alem da politica, nao cria obrigacoes nao autorizadas (0-10); (3) ALUCINACAO — toda informacao factual e verificavel na KB ou no sistema consultado (0-10); (4) COMPLETUDE — responde o que foi perguntado sem deixar gaps que forcam novo contato (0-10); (5) SEGURANÇA — nao expoe dados de outros clientes, nao viola LGPD (0-10). Score minimo para envio: 42/50. Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve para o worker com feedback especifico. Score < 30 ou flag de risco juridico/LGPD: escalona para HITL via Hermes.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Critic de Qualidade & Compliance
- Valida cada resposta gerada pelos workers antes do envio externo ao cliente
- Rubrica de 5 dimensoes: (1) TOM
- adequado ao canal e sentimento do cliente (0-10)
- (2) COMPLIANCE
- nao promete alem da politica, nao cria obrigacoes nao autorizadas (0-10)
- (3) ALUCINACAO
- toda informacao factual e verificavel na KB ou no sistema consultado (0-10)
- (4) COMPLETUDE
- responde o que foi perguntado sem deixar gaps que forcam novo contato (0-10)
- (5) SEGURANÇA
- nao expoe dados de outros clientes, nao viola LGPD (0-10)
- Score minimo para envio: 42/50
- Abaixo de 42 ou qualquer dimensao < 6: rejeita e devolve para o worker com feedback especifico
- Score < 30 ou flag de risco juridico/LGPD: escalona para HITL via Hermes

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Nexus para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário
- [ ] Gate HITL respeitado: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo
- [ ] Gate HITL respeitado: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Terceira interação na mesma sessão sem resolução confirmada pelo cliente | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Menção de palavras-chave de risco: 'advogado', 'PROCON', 'Reclame Aqui', 'processo', 'imprensa', 'TV' | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Solicitacao de troca/devolucao fora do prazo de politica ou em categoria inelegivel — Volta escalona para decisao humana com contexto | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Health score do cliente cai abaixo de 45 durante a interação — Pulse dispara alerta para CSM responsável | BLOQUEIA até decisão humana |
| VETO-009 | HITL — Áudio com qualidade ASR < 0.80 de confiança — Vox marca para revisão humana antes de processar | BLOQUEIA até decisão humana |
| VETO-010 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Nexus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
