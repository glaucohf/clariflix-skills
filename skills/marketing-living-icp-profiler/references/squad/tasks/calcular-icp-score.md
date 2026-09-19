---
task: rex()
responsavel: "Rex"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Outputs consolidados de todos os agents workers (enrichment records, signal scores, PMF scores, research canvas), ICP versão atual, threshold de mudança configurado pelo Maestro"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "ICP Profile versionado (JSON estruturado com todos os atributos, pesos e scores por dimensão), Changelog de mudanças entre versões, ICP Score composto atualizado no CRM (campo customizado), notificação de nova versão para stakeholders via ClickUp, diff visual entre versão anterior e atual"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Maestro sinaliza ciclo de consolidação concluído; delta de fit score médio > 15% detectado; nova versão de enriquecimento concluída; fim de ciclo mensal automático"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Vera 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do ICP Hypothesis Canvas ao final do Discovery — CEO/CMO valida ou refuta hipóteses de segmentos antes de iniciar enriquecimento em escala (L3)"
    - "[ ] HITL: Publicação de nova versão major do ICP (v1.x -> v2.0) — mudanças estruturais de perfil requerem aprovação do CMO antes de atualizar o CRM (L3)"
    - "[ ] HITL: Ativação de monitoramento de contas em novo segmento adjacente identificado por Nox — expansão de ICP é decisão estratégica (L3)"
    - "[ ] HITL: Quando Vera retorna BLOCKED em auditoria de qualidade — time deve revisar manualmente as inconsistências críticas apontadas antes de Maestro reprocessar (L3)"
    - "[ ] HITL: Calibração de pesos por dimensão do ICP Score — revisão trimestral com Sales Lead e CMO para ajustar o que o time considera mais preditivo de conversão (L1)"
---

# Calcular Icp Score

**Task ID:** `rex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Living ICP Profiler

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Icp Score |
| **status** | `pending` |
| **responsible_executor** | Rex (Rex — ICP Scoring & Versioning Agent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Responsável pela lógica de scoring do ICP e pelo versionamento semântico do perfil. Agrega todos os outputs de Atlas, Iris, Zara e Nox para calcular o ICP Score composto, detecta quando o perfil deve ser incrementado (v1.0->v1.1) ou revisado (v1.x->v2.0). Publica o ICP atualizado no CRM e no ClickUp. Garante rastreabilidade de todas as mudanças com changelog.

## Input

- Outputs consolidados de todos os agents workers (enrichment records, signal scores, PMF scores, research canvas), ICP versão atual, threshold de mudança configurado pelo Maestro

## Output

- ICP Profile versionado (JSON estruturado com todos os atributos, pesos e scores por dimensão), Changelog de mudanças entre versões, ICP Score composto atualizado no CRM (campo customizado), notificação de nova versão para stakeholders via ClickUp, diff visual entre versão anterior e atual

## Trigger

Maestro sinaliza ciclo de consolidação concluído; delta de fit score médio > 15% detectado; nova versão de enriquecimento concluída; fim de ciclo mensal automático

## Knowledge base (o que o executor consulta)

- Todas as versões anteriores do ICP (histórico completo), regras de versionamento semântico (quando é patch vs minor vs major), pesos por dimensão de scoring configurados pelo CMO, histórico de performance por versão de ICP

## Action Items

1. Confirmar o gatilho e carregar a entrada (Outputs consolidados de todos os agents workers (enrichment records, signal scores, PMF scores, research canvas), ICP v…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (ICP Profile versionado (JSON estruturado com todos os atributos, pesos e scores por dimensão), Changelog de mudanças en…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: ICP Profile versionado (JSON estruturado com todos os atributos, pesos e scores por dimensão), Changelog de mudanças entre versões, ICP Score composto atualiza…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Vera 2 registrado
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

- **to:** Vera
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
