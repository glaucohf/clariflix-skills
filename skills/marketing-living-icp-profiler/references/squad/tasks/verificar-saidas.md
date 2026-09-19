---
task: vera2Verificar()
responsavel: "Vera 2"
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
    - "[ ] HITL: Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3)"
    - "[ ] HITL: Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3)"
    - "[ ] HITL: Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)"
    - "[ ] HITL: Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3)"
    - "[ ] HITL: Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1)"
---

# Verificar Saídas do Living ICP Profiler

**Task ID:** `vera2Verificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Living ICP Profiler

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Living ICP Profiler |
| **status** | `pending` |
| **responsible_executor** | Vera 2 (Vera — Critic & Data Quality Verifier) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Vera — Critic & Data Quality Verifier — Implementa o padrão Skeptic Protocol para o squad: desafia cada versão do ICP antes de publicação, detecta data quality issues, valida conformidade LGPD/GDPR, identifica inconsistências entre fontes de enriquecimento e alerta quando o ICP proposto contradiz o histórico de performance. Gate L3 obrigatório — nenhuma versão de ICP é publicada sem aprovação de Vera.

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- Critic & Data Quality Verifier
- Implementa o padrão Skeptic Protocol para o squad: desafia cada versão do ICP antes de publicação, detecta data quality issues, valida conformidade LGPD/GDPR, identifica inconsistências entre fontes de enriquecimento e alerta quando o ICP proposto contradiz o histórico de performance
- Gate L3 obrigatório
- nenhuma versão de ICP é publicada sem aprovação de Vera

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
- [ ] Gate HITL respeitado: Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento…
- [ ] Gate HITL respeitado: Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (…
- [ ] Gate HITL respeitado: Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3) | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3) | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3) | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3) | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Aprovação de integração com nova fonte de dados de enriquecimento que implica custo adicional — qualquer nova ferramenta paga requer validação financeira (L3) | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Vera 2 | BLOQUEIA entrega |

## Handoff

- **to:** Maestro
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
