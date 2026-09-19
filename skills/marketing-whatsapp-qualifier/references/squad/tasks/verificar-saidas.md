---
task: kira2Verificar()
responsavel: "Kira 2"
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
    - "[ ] HITL: Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado (L3, sem aprovacao o squad nao avanca)"
    - "[ ] HITL: Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao. Kira ja auditou conformidade, mas humano decide se o tom esta certo (L3, gate obrigatorio)"
    - "[ ] HITL: Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa manualmente antes de Vance responder (L3, acao irreversivel: primeira impressao com conta estrategica)"
    - "[ ] HITL: Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion antes de Vance ser atualizado (L2, recorrente toda segunda-feira)"
    - "[ ] HITL: Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 com head de vendas e Kira antes de producao"
---

# Verificar Saídas do WhatsApp Qualifier

**Task ID:** `kira2Verificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** WhatsApp Qualifier

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do WhatsApp Qualifier |
| **status** | `pending` |
| **responsible_executor** | Kira 2 (Kira — Compliance & Voice Guardian) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Kira — Compliance & Voice Guardian — Implementa o papel de critic/verifier do squad com foco em dois vetores: (1) Conformidade operacional — cada versao do Playbook Conversacional e auditada contra as restricoes Meta pos-proibicao, LGPD e brand voice antes de ir para producao. Gate L3 obrigatorio: sem aprovacao de Kira, nenhuma mensagem automatizada e enviada. (2) Monitoramento continuo — audita sample diaria de conversas em producao para detectar desvios de conformidade, mensagens que possam violar politicas e padroes que indiquem risco de banimento da conta WhatsApp Business. Age como advogado do diabo do squad: assume que qualquer mensagem automatizada pode ser interpretada de forma adversa pela Meta e forca o playbook a ser explicitamente seguro.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Compliance & Voice Guardian
- Implementa o papel de critic/verifier do squad com foco em dois vetores: (1) Conformidade operacional
- cada versao do Playbook Conversacional e auditada contra as restricoes Meta pos-proibicao, LGPD e brand voice antes de ir para producao
- Gate L3 obrigatorio: sem aprovacao de Kira, nenhuma mensagem automatizada e enviada
- (2) Monitoramento continuo
- audita sample diaria de conversas em producao para detectar desvios de conformidade, mensagens que possam violar politicas e padroes que indiquem risco de banimento da conta WhatsApp Business
- Age como advogado do diabo do squad: assume que qualquer mensagem automatizada pode ser interpretada de forma adversa pela Meta e forca o playbook a ser explicitamente seguro

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Orion para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do s…
- [ ] Gate HITL respeitado: Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e…
- [ ] Gate HITL respeitado: Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior par…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovacao do Mapa de Jornada WhatsApp + Inventario de Objecoes ao final do Discovery — head de vendas valida o que funciona hoje antes do squad ser configurado… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovacao do Playbook Conversacional v1 antes de ir para producao — head de vendas e CMO revisam cada mensagem, pergunta de qualificacao e resposta a objecao.… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Escalada de lead VIP para SDR humano sênior — quando Rex detecta empresa acima do threshold de tamanho/ICP fit, Orion alerta SDR sênior para assumir a conversa… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Gate semanal de 30 minutos — head de vendas revisa 5-10 conversas de baixo desempenho selecionadas por Lilo, aprova ajustes de playbook propostos por Orion ant… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Aprovacao de nova versao do Playbook apos ajustes significativos (> 30% das mensagens alteradas) — qualquer revisao estrutural do playbook passa por gate L3 co… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Decisao de escalada por irritacao detectada — quando Vance detecta 3+ sinais de irritacao em sequencia, Orion alerta SDR humano via notificacao para assumir a… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Revisao mensal de metricas com Nova — CEO/CMO aprova redistribuicao de budget por fonte de lead com base no ROI report de Nova (L3, envolve gasto financeiro) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Kira 2 | BLOQUEIA entrega |

## Handoff

- **to:** Orion
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
