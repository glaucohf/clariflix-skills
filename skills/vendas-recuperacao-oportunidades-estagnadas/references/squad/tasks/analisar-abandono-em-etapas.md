---
task: forense()
responsavel: "Forense"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Resultados de todas as tentativas de recuperação (enviadas, respondidas, convertidas, ignoradas), dados de deals arquivados, feedback dos comerciais humanos"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Relatório semanal de perdas com padrões identificados, proposta de ajustes nos playbooks (para aprovação humana), atualização dos thresholds de Score de Urgência"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Artefato: loss-analysis-{week}.md no ClickUp"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo semanal automático, deal movido para Perdido/Arquivado, acumulação de 10+ deals sem resposta no mesmo playbook"
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

# Analisar Abandono Em Etapas

**Task ID:** `forense()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Recuperação de Oportunidades Estagnadas

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Abandono Em Etapas |
| **status** | `pending` |
| **responsible_executor** | Forense (Forense (Worker de Análise de Perdas e Feedback Loop)) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Análisa deals que foram para Arquivar ou não responderam a nenhum toque de recuperação. Identifica padrões: qual etapa tem mais abandono, qual canal tem menor resposta, qual ângulo de mensagem não funcionou, qual playbook gerou resultado. Gera relatório semanal de aprendizado e propõe ajustes nos playbooks e nos parâmetros de detecção do Radar. Fecha o loop de melhoria contínua.

## Input

- Resultados de todas as tentativas de recuperação (enviadas, respondidas, convertidas, ignoradas), dados de deals arquivados, feedback dos comerciais humanos

## Output

- Relatório semanal de perdas com padrões identificados, proposta de ajustes nos playbooks (para aprovação humana), atualização dos thresholds de Score de Urgência
- Artefato: loss-analysis-{week}.md no ClickUp

## Trigger

Ciclo semanal automático, deal movido para Perdido/Arquivado, acumulação de 10+ deals sem resposta no mesmo playbook

## Knowledge base (o que o executor consulta)

- Histórico completo de tentativas de recuperação com resultados, benchmarks de taxa de recuperação por setor, dados de win/loss anteriores, feedback qualitativo dos comerciais

## Action Items

1. Confirmar o gatilho e carregar a entrada (Resultados de todas as tentativas de recuperação (enviadas, respondidas, convertidas, ignoradas), dados de deals arquiv…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Relatório semanal de perdas com padrões identificados, proposta de ajustes nos playbooks (para aprovação humana), atual…) e persistir no artefato do squad.
4. Entregar ao critic Critic e Verifier de Mensagens 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Relatório semanal de perdas com padrões identificados, proposta de ajustes nos playbooks (para aprovação humana), atualização dos thresholds de Score de Urgênc…
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

- **to:** Critic e Verifier de Mensagens 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
