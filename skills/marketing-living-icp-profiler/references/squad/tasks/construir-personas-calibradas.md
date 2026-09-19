---
task: atlas()
responsavel: "Atlas"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de clientes atuais (CRM export), critérios de LTV mínimo, segmentos-alvo definidos pelo Maestro, briefing de concorrentes a pesquisar"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "ICP Hypothesis Canvas (markdown estruturado), Synthetic Persona Cards (3-5 personas por segmento), Competitive ICP Map (como concorrentes definem seu ICP), Research Report com fontes citadas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Início de ciclo Discovery; delta de fit score > 15% detectado pelo Maestro; novo segmento de mercado identificado por Zara; solicitação manual via ClickUp task"
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

# Construir Personas Calibradas

**Task ID:** `atlas()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Living ICP Profiler

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Construir Personas Calibradas |
| **status** | `pending` |
| **responsible_executor** | Atlas (Atlas — ICP Research Agent) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Executa deepresearch estruturado para construção e atualização do ICP. Analisa base de clientes de alto LTV, faz benchmarking de concorrentes, pesquisa tendências setoriais e gera synthetic personas calibradas em dados reais. Principal executor da fase Discovery. Usa frameworks Deepsona e Market Logic para estruturar personas.

## Input

- Lista de clientes atuais (CRM export), critérios de LTV mínimo, segmentos-alvo definidos pelo Maestro, briefing de concorrentes a pesquisar

## Output

- ICP Hypothesis Canvas (markdown estruturado), Synthetic Persona Cards (3-5 personas por segmento), Competitive ICP Map (como concorrentes definem seu ICP), Research Report com fontes citadas

## Trigger

Início de ciclo Discovery; delta de fit score > 15% detectado pelo Maestro; novo segmento de mercado identificado por Zara; solicitação manual via ClickUp task

## Knowledge base (o que o executor consulta)

- Base de clientes ganhos/perdidos com atributos de empresa e contato, histórico de deals no CRM, playbooks de ICP anteriores versionados, research reports de mercado (Gartner, G2, relatórios setoriais), perfis de concorrentes

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de clientes atuais (CRM export), critérios de LTV mínimo, segmentos-alvo definidos pelo Maestro, briefing de conc…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (ICP Hypothesis Canvas (markdown estruturado), Synthetic Persona Cards (3-5 personas por segmento), Competitive ICP Map…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: ICP Hypothesis Canvas (markdown estruturado), Synthetic Persona Cards (3-5 personas por segmento), Competitive ICP Map (como concorrentes definem seu ICP), Res…
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

- **to:** Iris
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
