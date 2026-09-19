---
task: sigma2Verificar()
responsavel: "Sigma 2"
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
    - "[ ] HITL: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresholds de urgência antes de qualquer monitoramento ir ao ar (L3, gate obrigatório)"
    - "[ ] HITL: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squad ser colocado em produção (L3, calibração crítica)"
    - "[ ] HITL: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e financeiro)"
    - "[ ] HITL: Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprovar a mensagem antes do envio (L3)"
    - "[ ] HITL: Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L1, ciclo recorrente)"
---

# Verificar Saídas do Demand Sensing Radar

**Task ID:** `sigma2Verificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Demand Sensing Radar

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Demand Sensing Radar |
| **status** | `pending` |
| **responsible_executor** | Sigma 2 (Sigma — Crític & Compliance Verifier) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Sigma — Critic & Compliance Verifier — Implementa o padrão Skeptic Protocol para o squad: desafia cada ação externa antes de executar, valida conformidade LGPD/GDPR no uso de sinais como contexto de abordagem, verifica alinhamento de brand voice, detecta falsos positivos de sinal (conta parece Hot mas evidências são fracas), e bloqueia playbooks com personalização inadequada ou frequência excessiva por conta. Gate L3 obrigatório — nenhum outreach, campanha paga ou ação de tier 1 sai sem aprovação de Sigma. Responsável por garantir que o 'radar' não vire spam sofisticado.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Critic & Compliance Verifier
- Implementa o padrão Skeptic Protocol para o squad: desafia cada ação externa antes de executar, valida conformidade LGPD/GDPR no uso de sinais como contexto de abordagem, verifica alinhamento de brand voice, detecta falsos positivos de sinal (conta parece Hot mas evidências são fracas), e bloqueia playbooks com personalização inadequada ou frequência excessiva por conta
- Gate L3 obrigatório
- nenhum outreach, campanha paga ou ação de tier 1 sai sem aprovação de Sigma
- Responsável por garantir que o 'radar' não vire spam sofisticado

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador Radar para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
- [ ] Gate HITL respeitado: Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o…
- [ ] Gate HITL respeitado: Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cad…
- [ ] Gate HITL respeitado: Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Signal Taxonomy Canvas no Discovery (Semana 2) — CMO e Head de Vendas validam quais categorias de sinal são relevantes para o ICP e definem thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Validação manual das primeiras 10 contas Hot identificadas no Deep Dive — time de vendas confirma se o sinal detectado faz sentido para cada conta antes do squ… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Aprovação de campanha paga (ads) gerada por Bolt — qualquer investimento de budget requer aprovação humana antes de subir para Google/Meta (L3, irreversível e… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Abordagem direta de contas tier 1 estratégicas — quando o playbook envolve contato direto com C-level de conta de alto valor, o AE ou CEO deve revisar e aprova… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração mensal de thresholds de sinal — Head de Vendas e CMO revisam com Sage os thresholds de Hot/Warm/Cold e ajustam conforme aprendizados de conversão (L… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Ativação de novo tipo de sinal ou integração de nova fonte de dados que implica custo adicional — aprovação financeira antes de habilitar (L3) | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Quando Sigma retorna BLOCKED em gate de compliance LGPD — revisão jurídica humana obrigatória antes de reprocessar (L3, risco legal) | BLOQUEIA até decisão humana |
| VETO-008 | Saída sem veredito do critic Sigma 2 | BLOQUEIA entrega |

## Handoff

- **to:** Radar
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
