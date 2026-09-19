---
task: iris()
responsavel: "Iris"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de empresas/leads para enriquecer, ICP Data Model v{N} com atributos e pesos, credenciais de acesso Clay/Apollo/Cognism via MCP, threshold de completude por tier de lead"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead enrichment records com 40+ atributos preenchidos, ICP Fit Score por lead (0-10 com breakdown por dimensão), confidence score por atributo, lista de atributos ausentes por fonte, relatório de cobertura de enriquecimento"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Novo lead entra no CRM (webhook HubSpot/Salesforce); ciclo semanal de re-enriquecimento de pipeline ativa; Maestro dispara Deep Dive; lista de prospecting nova importada"
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

# Enriquecer Dados Lead

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Living ICP Profiler

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Enriquecer Dados Lead |
| **status** | `pending` |
| **responsible_executor** | Iris (Íris — Enrichment Cascade Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa o waterfall de enriquecimento em cascata via Clay, Apollo, Cognism e fontes abertas. Para cada lead ou empresa, tenta enriquecer sequencialmente — se Clay retorna >80% dos campos, para; se não, aciona Apollo; se ainda incompleto, Cognism; fallback para scraping estruturado via MCP. Calcula ICP Fit Score (0-10) por lead com base nos atributos do ICP vivo. Principal executor da fase Deep Dive e do loop contínuo.

## Input

- Lista de empresas/leads para enriquecer, ICP Data Model v{N} com atributos e pesos, credenciais de acesso Clay/Apollo/Cognism via MCP, threshold de completude por tier de lead

## Output

- Lead enrichment records com 40+ atributos preenchidos, ICP Fit Score por lead (0-10 com breakdown por dimensão), confidence score por atributo, lista de atributos ausentes por fonte, relatório de cobertura de enriquecimento

## Trigger

Novo lead entra no CRM (webhook HubSpot/Salesforce); ciclo semanal de re-enriquecimento de pipeline ativa; Maestro dispara Deep Dive; lista de prospecting nova importada

## Knowledge base (o que o executor consulta)

- ICP Data Model versionado com todos os atributos e pesos por dimensao, mapping de fontes por tipo de atributo (Clay para firmographic, Apollo para contatos, Cognism para dados de compliance GDPR), historico de enriquecimentos anteriores para delta tracking

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de empresas/leads para enriquecer, ICP Data Model v{N} com atributos e pesos, credenciais de acesso Clay/Apollo/C…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead enrichment records com 40+ atributos preenchidos, ICP Fit Score por lead (0-10 com breakdown por dimensão), confid…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead enrichment records com 40+ atributos preenchidos, ICP Fit Score por lead (0-10 com breakdown por dimensão), confidence score por atributo, lista de atribu…
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

- **to:** Zara
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
