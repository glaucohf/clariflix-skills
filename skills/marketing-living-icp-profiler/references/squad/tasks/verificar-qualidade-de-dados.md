---
task: vera()
responsavel: "Vera"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "ICP draft para publicação (Rex output), regras de qualidade configuradas, histórico de performance do ICP anterior, checklist de conformidade LGPD, threshold de completude por tier"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Quality Report com APPROVED/NEEDS_REVISION/BLOCKED, lista de inconsistências detectadas com severity (critical/warning/info), Score de qualidade dos dados (0-100), sugestões de correção específicas, flag de conformidade LGPD com itens a corrigir antes de publicar"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Sempre que Rex prepara nova versão de ICP para publicação (gate obrigatório); Maestro solicita auditoria de qualidade; anomalia de dados detectada no pipeline de enriquecimento"
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

# Verificar Qualidade De Dados

**Task ID:** `vera()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Living ICP Profiler

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Qualidade De Dados |
| **status** | `pending` |
| **responsible_executor** | Vera (Vera — Critic & Data Quality Verifier) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de verificação crítica e qualidade de dados. Antes de qualquer publicação ou atualização do ICP no CRM, Vera valida: consistência dos dados enriquecidos (campos conflitantes entre fontes), coerência lógica do ICP (score alto em segmento com histórico de churn alto e um red flag), completude mínima por tier de lead, conformidade GDPR/LGPD nos dados coletados, alinhamento entre ICP proposto e histórico de wins. Implementa o padrão Skeptic Protocol.

## Input

- ICP draft para publicação (Rex output), regras de qualidade configuradas, histórico de performance do ICP anterior, checklist de conformidade LGPD, threshold de completude por tier

## Output

- Quality Report com APPROVED/NEEDS_REVISION/BLOCKED, lista de inconsistências detectadas com severity (critical/warning/info), Score de qualidade dos dados (0-100), sugestões de correção específicas, flag de conformidade LGPD com itens a corrigir antes de publicar

## Trigger

Sempre que Rex prepara nova versão de ICP para publicação (gate obrigatório); Maestro solicita auditoria de qualidade; anomalia de dados detectada no pipeline de enriquecimento

## Knowledge base (o que o executor consulta)

- Regras de qualidade de dados por atributo, checklist de conformidade LGPD/GDPR para dados B2B, histórico de erros de enriquecimento por fonte, regras de negócio do ICP (ex: empresa com < 10 funcionários não é ICP independente do score), playbook de inconsistências conhecidas

## Action Items

1. Confirmar o gatilho e carregar a entrada (ICP draft para publicação (Rex output), regras de qualidade configuradas, histórico de performance do ICP anterior, che…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Quality Report com APPROVED/NEEDS_REVISION/BLOCKED, lista de inconsistências detectadas com severity (critical/warning/…) e persistir no artefato do squad.
4. Entregar ao critic Vera 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Quality Report com APPROVED/NEEDS_REVISION/BLOCKED, lista de inconsistências detectadas com severity (critical/warning/info), Score de qualidade dos dados (0-1…
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

- **to:** Vera 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
