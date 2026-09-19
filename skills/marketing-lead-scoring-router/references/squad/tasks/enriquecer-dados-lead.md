---
task: iris()
responsavel: "Iris"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead normalizado do Scout (email, nome, empresa como inputs primários para lookup), credenciais Clay/Apollo/Cognism via MCP, threshold de completude por tier de lead (tier 1 exige >= 85%, tier 2 >= 70%, tier 3 best-effort), campos prioritários por tier definidos no Score Card Model"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Lead enriquecido com 30+ atributos preenchidos: dados da empresa (tamanho, setor, receita estimada, localizacao, fundacao, stack tecnologico), dados do contato (cargo normalizado, seniority level, LinkedIn URL, telefone direto quando disponıvel), dados de intent de terceiros quando acessıveis via Clay, confidence score por atributo (Alta/Media/Baixa baseado na fonte), lista de campos nao encontrados por nenhuma fonte, custo estimado de enriquecimento por lead (para tracking de ROI)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead normalizado e enfileirado pelo Scout (trigger automatico, roda em paralelo com scoring inicial); Apex solicita re-enriquecimento de lead com score de baixa confianca; ciclo semanal de re-enrique…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Critique 2 antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o threshold de 75 é ajustável) e validar a Routing Matrix antes de ativar em produção (L3)"
    - "[ ] HITL: Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads (L3)"
    - "[ ] HITL: Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique deve ser aprovada pelo Sales Lead antes de Orion aplicar em produção (L3)"
    - "[ ] HITL: Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerteza (L3)"
    - "[ ] HITL: Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3)"
---

# Enriquecer Dados Lead

**Task ID:** `iris()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Lead Scoring & Router

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

Executa o waterfall de enriquecimento em cascata para completar os dados do lead antes ou paralelamente ao scoring. Sequência de fontes: (1) Clay — principal, tenta preencher todos os campos firmográficos e de contato; se completude >= 80%, para. (2) Apollo.io — complementa campos de contato e seniority que Clay não cobriu. (3) Clearbit/Cognism — fallback para dados de empresa e tecnologia (Technographics). (4) LinkedIn scraping via Apify — perfil do contato para validar cargo e empresa quando email/nome disponíveis. Retorna dados enriquecidos para Apex recalcular o score com dados mais completos, e para Vector incluir no brief do SDR. Atua em paralelo com o scoring inicial (Apex pontua com dados parciais, Iris enriquece, Apex re-pontua com dados completos).

## Input

- Lead normalizado do Scout (email, nome, empresa como inputs primários para lookup), credenciais Clay/Apollo/Cognism via MCP, threshold de completude por tier de lead (tier 1 exige >= 85%, tier 2 >= 70%, tier 3 best-effort), campos prioritários por tier definidos no Score Card Model

## Output

- Lead enriquecido com 30+ atributos preenchidos: dados da empresa (tamanho, setor, receita estimada, localizacao, fundacao, stack tecnologico), dados do contato (cargo normalizado, seniority level, LinkedIn URL, telefone direto quando disponıvel), dados de intent de terceiros quando acessıveis via Clay, confidence score por atributo (Alta/Media/Baixa baseado na fonte), lista de campos nao encontrados por nenhuma fonte, custo estimado de enriquecimento por lead (para tracking de ROI)

## Trigger

Lead normalizado e enfileirado pelo Scout (trigger automatico, roda em paralelo com scoring inicial); Apex solicita re-enriquecimento de lead com score de baixa confianca; ciclo semanal de re-enriquecimento de leads Warm sem conversao; importacao de nova lista de prospecting

## Knowledge base (o que o executor consulta)

- Mapeamento de fontes por tipo de atributo (Clay para firmográfico, Apollo para contato, Cognism para GDPR-compliant Europa), regras de cascata e threshold de completude por tier, custo por enriquecimento por fonte (para otimização de budget), campos obrigatórios vs opcionais por tier, histórico de taxa de preenchimento por fonte para otimização da ordem de cascata

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead normalizado do Scout (email, nome, empresa como inputs primários para lookup), credenciais Clay/Apollo/Cognism via…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Lead enriquecido com 30+ atributos preenchidos: dados da empresa (tamanho, setor, receita estimada, localizacao, fundac…) e persistir no artefato do squad.
4. Entregar ao critic Critique 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Lead enriquecido com 30+ atributos preenchidos: dados da empresa (tamanho, setor, receita estimada, localizacao, fundacao, stack tecnologico), dados do contato…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Critique 2 registrado
- [ ] Gate HITL respeitado: Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa…
- [ ] Gate HITL respeitado: Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de p…
- [ ] Gate HITL respeitado: Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) prop…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Definição dos critérios de Lead Hot antes do go-live — Sales Lead e CMO devem definir explicitamente o que é um lead Hot para essa empresa específica (o thresh… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Aprovação do Score Card Model v1 após backtesting no Discovery — o modelo deve ser validado com dados históricos pelo Sales Lead antes de processar novos leads… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Recalibração de pesos do modelo de scoring — qualquer alteração nos pesos por dimensão (Fit vs Intent, firmográfico vs comportamental) proposta por Critique de… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Lead Hot com score entre 65-80 e sinais contraditories — Orion escala para SDR Manager decidir manualmente o roteamento quando o modelo esta em zona de incerte… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Lead Hot sem primeiro contato do SDR em mais de 30 minutos — Pulse escala para SDR Manager via Slack + WhatsApp para intervenção imediata (L3) | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Desvio crítico de performance detectado por Critique — quando Precision@Hot cai abaixo de 40% ou Recall cai abaixo de 50%, o squad entra em modo de revisão e n… | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Ativação de nova fonte de leads (novo canal, novo formulário) — Scout não ativa fonte nova automaticamente, requer validação do schema de campos e regras de no… | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Ajuste de capacidade de SDR na Routing Matrix — quando SDR entra em ferias ou saı da empresa, Vector nao rebalanceia automaticamente sem confirmacao do Sales L… | BLOQUEIA até decisão humana |
| VETO-009 | Saída sem veredito do critic Critique 2 | BLOQUEIA entrega |

## Handoff

- **to:** Vector
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
