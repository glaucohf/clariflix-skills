---
task: sage()
responsavel: "Sage"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Intenção 'faq' | 'como_funciona' | 'política' | 'plano' | 'recurso' | 'instrução' + texto da pergunta do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta contextualizada com fonte citada do KB + link para artigo completo se relevante"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Se gap detectado: task no ClickUp para KB Curator com a pergunta e contexto"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Task de prova de trabalho com: pergunta, artigo-base usado, confiança do RAG"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orchestrator Nexus roteia intenção de baixa complexidade sem necessidade de ação de sistema; ou quando outros workers não reconhecem intenção específica"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário"
    - "[ ] HITL: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo"
    - "[ ] HITL: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados"
    - "[ ] HITL: Terceira interação na mesma sessão sem resolução confirmada pelo cliente"
    - "[ ] HITL: Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação"
---

# Responder Perguntas Frequentes

**Task ID:** `sage()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Suporte Conversacional Multicanal (Tier-1 Resolver)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Responder Perguntas Frequentes |
| **status** | `pending` |
| **responsible_executor** | Sage (Sage — Worker de FAQ & KB) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 3 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responde perguntas frequentes e consultas de base de conhecimento: horário de funcionamento, políticas, como usar o produto, integrações suportadas, planos e preços, requisitos técnicos. Usa RAG sobre o KB oficial. Detecta quando a pergunta não tem resposta no KB e registra o gap para o KB Curator.

## Input

- Intenção 'faq' | 'como_funciona' | 'política' | 'plano' | 'recurso' | 'instrução' + texto da pergunta do cliente

## Output

- Resposta contextualizada com fonte citada do KB + link para artigo completo se relevante
- Se gap detectado: task no ClickUp para KB Curator com a pergunta e contexto
- Task de prova de trabalho com: pergunta, artigo-base usado, confiança do RAG

## Trigger

Orchestrator Nexus roteia intenção de baixa complexidade sem necessidade de ação de sistema; ou quando outros workers não reconhecem intenção específica

## Knowledge base (o que o executor consulta)

- Base de conhecimento vetorizada (Supabase pgvector), artigos de help center (Intercom/Zendesk KB), documentação de produto, FAQs históricas respondidas por humanos, políticas comerciais atualizadas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Intenção 'faq' | 'como_funciona' | 'política' | 'plano' | 'recurso' | 'instrução' + texto da pergunta do cliente).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resposta contextualizada com fonte citada do KB + link para artigo completo se relevante) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta contextualizada com fonte citada do KB + link para artigo completo se relevante
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
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

- **to:** Vox
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
