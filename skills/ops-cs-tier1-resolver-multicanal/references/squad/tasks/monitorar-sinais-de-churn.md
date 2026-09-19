---
task: pulse()
responsavel: "Pulse"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcrição completa da interação + sentiment score por mensagem + histórico de tickets dos últimos 30 dias + dados de uso do produto (logins, features ativas) + tier e MRR do cliente"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Health score atualizado no CRM (0-100)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alert no Slack do time de CS se score < 60"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Brief de retenção com: sinais detectados, risco percentual de churn em 30 dias, next-best-action sugerida"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Task no ClickUp com evidências"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda interação de suporte concluída (independente de resolução); queda > 15 pontos no health score; detecção de keyword de churn na transcrição; cliente com > 3 tickets nos últimos 7 dias"
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

# Monitorar Sinais De Churn

**Task ID:** `pulse()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Suporte Conversacional Multicanal (Tier-1 Resolver)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais De Churn |
| **status** | `pending` |
| **responsible_executor** | Pulse (Pulse — Agente de Health Score & Churn Signal) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Monitora silenciosamente cada interação de suporte buscando sinais de churn: sentimento acumulado negativo, frequência de problemas recorrentes, menção de concorrentes, redução de uso. Atualiza o health score do cliente no CRM após cada interação, gera alertas para o time de CS quando o score cai abaixo do threshold e sugere next-best-action (oferta de retenção, contato proativo do CSM, upgrade de plano).

## Input

- Transcrição completa da interação + sentiment score por mensagem + histórico de tickets dos últimos 30 dias + dados de uso do produto (logins, features ativas) + tier e MRR do cliente

## Output

- Health score atualizado no CRM (0-100)
- Alert no Slack do time de CS se score < 60
- Brief de retenção com: sinais detectados, risco percentual de churn em 30 dias, next-best-action sugerida
- Task no ClickUp com evidências

## Trigger

Toda interação de suporte concluída (independente de resolução); queda > 15 pontos no health score; detecção de keyword de churn na transcrição; cliente com > 3 tickets nos últimos 7 dias

## Knowledge base (o que o executor consulta)

- Modelo de churn scoring (features: frequência de tickets, sentimento, uso do produto, tempo desde última renovação, NPS histórico), playbooks de retenção por perfil de cliente, dados de MRR/ARR e histórico de renovação do CRM, benchmarks de health score por segmento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcrição completa da interação + sentiment score por mensagem + histórico de tickets dos últimos 30 dias + dados de…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Health score atualizado no CRM (0-100)) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Health score atualizado no CRM (0-100)
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

- **to:** Argus
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
