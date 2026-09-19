---
task: iris()
responsavel: "Iris"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Export do CRM (lista de clientes atuais + deals perdidos), critérios de ICP definidos pelo cliente, acesso read-only ao HubSpot/Salesforce, lista de empresas-alvo (se existir)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "ICP Master Profile (documento): 3-5 clusters de ICP rankeados por LTV e propensão, atributos firmográficos e tecnográficos por cluster, padrões comportamentais identificados, ICP Fit Score model (fórmula de scoring) e lista de 50-100 empresas que se encaixam no ICP #1 para validação"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ativado pelo Orion no início da fase Discovery, em paralelo com Vesper. Re-ativado quando cliente fornece novos dados de CRM ou quando Brutus detecta incongruência no perfil."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Brutus 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias de pesquisa na direção errada"
    - "[ ] HITL: Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx simular entrevistas"
    - "[ ] HITL: Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva documentada"
    - "[ ] HITL: Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução (Copywriter, Media Buying) — gate L3 porque decisões de mídia são financeiramente irreversíveis"
    - "[ ] HITL: Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser incluído no documento final"
---

# Gerar Scoring De Fit

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** PMF & Market Deep Research Squad

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Scoring De Fit |
| **status** | `pending` |
| **responsible_executor** | Iris (Íris — ICP Profiler) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de enriquecimento e profiling de ICP. Cruza dados do CRM do cliente com sinais externos (LinkedIn, Clay waterfall, Apollo) para construir o perfil quantitativo do cliente ideal — firmograficos, tecnograficos, comportamentais e psicograficos. Gera scoring de fit e identifica clusters de ICP com maior propensao a fechar.

## Input

- Export do CRM (lista de clientes atuais + deals perdidos), critérios de ICP definidos pelo cliente, acesso read-only ao HubSpot/Salesforce, lista de empresas-alvo (se existir)

## Output

- ICP Master Profile (documento): 3-5 clusters de ICP rankeados por LTV e propensão, atributos firmográficos e tecnográficos por cluster, padrões comportamentais identificados, ICP Fit Score model (fórmula de scoring) e lista de 50-100 empresas que se encaixam no ICP #1 para validação

## Trigger

Ativado pelo Orion no início da fase Discovery, em paralelo com Vesper. Re-ativado quando cliente fornece novos dados de CRM ou quando Brutus detecta incongruência no perfil.

## Knowledge base (o que o executor consulta)

- Dados do CRM do cliente (HubSpot/Salesforce), dados públicos do LinkedIn via Clay/Apollo, sinais de intent do G2/Bombora (se disponível), histórico de wins/losses do cliente, framework de ICP do board (Profiling de ICP via Gateways de dados)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Export do CRM (lista de clientes atuais + deals perdidos), critérios de ICP definidos pelo cliente, acesso read-only ao…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (ICP Master Profile (documento): 3-5 clusters de ICP rankeados por LTV e propensão, atributos firmográficos e tecnográfi…) e persistir no artefato do squad.
4. Entregar ao critic Brutus 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: ICP Master Profile (documento): 3-5 clusters de ICP rankeados por LTV e propensão, atributos firmográficos e tecnográficos por cluster, padrões comportamentais…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Brutus 2 registrado
- [ ] Gate HITL respeitado: Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começ…
- [ ] Gate HITL respeitado: Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a re…
- [ ] Gate HITL respeitado: Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Aprovação do Briefing de Contexto (fim da fase Discovery): cliente valida ICP draft, top-10 dores e mapa de fontes antes do deep dive começar — evita 3-5 dias… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Revisão do PMF Score draft + aprovação das Persona Cards (meio da fase Deep Dive): cliente confirma se as personas sintéticas refletem a realidade antes de Nyx… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Auditoria de Brutus com reprovação > 30% em qualquer artefato: Orion escala para humano decidir entre retrabalhar o agente ou aceitar claim com ressalva docume… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Aprovação final do PMF Framework Document + Angle Test Kit (fim da fase Framework): cliente/board aprova antes do artefato ser passado para squads de execução… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Qualquer claim de TAM/SAM/SOM acima de R$500M ou abaixo de R$10M que impacte decisão de alocação de budget: requer validação humana independente antes de ser i… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic Brutus 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vesper
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
