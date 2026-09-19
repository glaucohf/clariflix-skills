---
task: monge()
responsavel: "Monge"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Leads no bucket Nutrir, biblioteca de conteúdo aprovado, sinais de engajamento do lead scoring"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Cadência de nurture ativa com histórico de engajamentos, alertas de reaquecimento ao Orquestrador, transferência de leads quentes para fluxo de recuperação ativa"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato: nurture-status-{leadId}.json atualizado semanalmente"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Classificação Nutrir pelo Radar, sinais de reaquecimento (engajamento acima de threshold), ciclo semanal automático de verificação de status"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Critic e Verifier de Mensagens 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado — gate L3 no Mensageiro)"
    - "[ ] HITL: Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa"
    - "[ ] HITL: Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial"
    - "[ ] HITL: Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção"
    - "[ ] HITL: Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo"
---

# Nutrir Leads Longo Prazo

**Task ID:** `monge()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Recuperação de Oportunidades Estagnadas

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Nutrir Leads Longo Prazo |
| **status** | `pending` |
| **responsible_executor** | Monge (Monge (Worker de Nurture e Cadência Longa)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Gerencia leads no bucket Nutrir com cadencias de longo prazo (30-90 dias). Envia conteudo de valor (cases, artigos, atualizacoes de produto) sem pressao de venda. Monitora sinais de reaquecimento (clicou no link, visitou pagina de precos, abriu email 3x na semana) e sinaliza para o Orquestrador quando o lead esquentou para mover para Salvar Agora. Evita o burnout do lead com frequencia controlada.

## Input

- Leads no bucket Nutrir, biblioteca de conteúdo aprovado, sinais de engajamento do lead scoring

## Output

- Cadência de nurture ativa com histórico de engajamentos, alertas de reaquecimento ao Orquestrador, transferência de leads quentes para fluxo de recuperação ativa
- Artefato: nurture-status-{leadId}.json atualizado semanalmente

## Trigger

Classificação Nutrir pelo Radar, sinais de reaquecimento (engajamento acima de threshold), ciclo semanal automático de verificação de status

## Knowledge base (o que o executor consulta)

- Biblioteca de conteúdo (cases, artigos, vídeos) por segmento e etapa do funil, regras de frequência por canal, threshold de sinais de reaquecimento (configurável), histórico de engajamento do lead

## Action Items

1. Confirmar o gatilho e carregar a entrada (Leads no bucket Nutrir, biblioteca de conteúdo aprovado, sinais de engajamento do lead scoring).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Cadência de nurture ativa com histórico de engajamentos, alertas de reaquecimento ao Orquestrador, transferência de lea…) e persistir no artefato do squad.
4. Entregar ao critic Critic e Verifier de Mensagens 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Cadência de nurture ativa com histórico de engajamentos, alertas de reaquecimento ao Orquestrador, transferência de leads quentes para fluxo de recuperação ati…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Critic e Verifier de Mensagens 2 registrado
- [ ] Gate HITL respeitado: Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeir…
- [ ] Gate HITL respeitado: Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa
- [ ] Gate HITL respeitado: Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável c…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação de envio para deals acima de threshold de valor (ex: oportunidades acima de R$50k exigem OK do gerente comercial antes do primeiro toque automatizado… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Resposta do lead que sinaliza interesse real em negociar (preço, escopo, prazo) — Mensageiro alerta comercial humano para assumir a conversa | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Qualquer mensagem que mencione desconto ou condição especial — bloqueada automaticamente pelo Guardião, vai para aprovação do responsável comercial | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Mudança de playbook baseada em proposta do Forense — ajustes em playbooks existentes exigem aprovação humana antes de entrar em produção | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Primeiro contato via voz (Vapi/Retell) para leads de alto valor — script revisado e aprovado pelo responsavel antes do disparo | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Opt-out recebido — registrado imediatamente, comunicado ao comercial, nenhuma acao adicional automatica alem do registro de compliance | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Critic e Verifier de Mensagens 2 | BLOQUEIA entrega |

## Handoff

- **to:** Forense
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
