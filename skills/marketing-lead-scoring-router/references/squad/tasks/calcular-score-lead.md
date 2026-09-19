---
task: apex()
responsavel: "Apex"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lead normalizado (Scout output) + dados enriquecidos (Iris output quando disponíveis), ICP Data Model versionado com atributos e pesos por dimensão, modelo de scoring calibrado (Score Card Model vN), histórico de interações do lead no CRM/site (se lead recorrente), sinais de intent de Clay/Bombora quando disponíveis via enriquecimento"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Score Card completo por lead: Score de Fit (0-100 com breakdown por dimensao firmografica), Score de Intent (0-100 com breakdown por sinal comportamental), Score Composto final (0-100), Tier classificado (Hot/Warm/Cold/Unfit), Reasoning narrativo em 2-3 linhas explicando o score para o SDR, campos de ICP que contribuıram positiva e negativamente para o score, confianca do score (Alta/Media/Baixa) baseada na completude dos dados de enriquecimento"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Lead normalizado e deduplicado pelo Scout (trigger primário); conclusão do ciclo de enriquecimento pelo Iris (re-score com dados completos); solicitação manual de re-score via ClickUp (quando SDR atu…"
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

# Calcular Score Lead

**Task ID:** `apex()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Lead Scoring & Router

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Score Lead |
| **status** | `pending` |
| **responsible_executor** | Apex (Apex — Scoring Engine Agent) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Calcula o Score de Fit e o Score de Intent de cada lead em menos de 60 segundos apos a normalizacao do Scout. Score de Fit (0-100) baseado em atributos firmograficos e de perfil: tamanho da empresa, setor, cargo/seniority, regiao geografica, stack tecnologico detectado — cruzado com o ICP Data Model (alimentado pelo squad Living ICP Profiler se disponıvel). Score de Intent (0-100) baseado em sinais comportamentais: paginas visitadas, conteudo baixado, UTM de origem, historico de interacoes anteriores, sinais de intent de terceiros (Clay/Bombora quando disponiveis). Score Composto = 0.6 * Fit + 0.4 * Intent. Define o tier: Hot (>= 75), Warm (50-74), Cold (30-49), Unfit (< 30). Registra o score e breakdown no CRM.

## Input

- Lead normalizado (Scout output) + dados enriquecidos (Iris output quando disponíveis), ICP Data Model versionado com atributos e pesos por dimensão, modelo de scoring calibrado (Score Card Model vN), histórico de interações do lead no CRM/site (se lead recorrente), sinais de intent de Clay/Bombora quando disponíveis via enriquecimento

## Output

- Score Card completo por lead: Score de Fit (0-100 com breakdown por dimensao firmografica), Score de Intent (0-100 com breakdown por sinal comportamental), Score Composto final (0-100), Tier classificado (Hot/Warm/Cold/Unfit), Reasoning narrativo em 2-3 linhas explicando o score para o SDR, campos de ICP que contribuıram positiva e negativamente para o score, confianca do score (Alta/Media/Baixa) baseada na completude dos dados de enriquecimento

## Trigger

Lead normalizado e deduplicado pelo Scout (trigger primário); conclusão do ciclo de enriquecimento pelo Iris (re-score com dados completos); solicitação manual de re-score via ClickUp (quando SDR atualiza informações do lead); ciclo semanal de re-score de leads Warm que não converteram (verificar se sinais de intent subiram)

## Knowledge base (o que o executor consulta)

- Score Card Model versionado com pesos por dimensão (atualizado a cada calibração), ICP Data Model com atributos e tier de importância, histórico de scores de leads convertidos vs perdidos (dataset de treinamento/calibração), regras de bônus e penalty por sinal específico (ex: CEO de empresa com 50-500 funcionários no setor alvo = +20 Fit
- lead que visitou página de preço = +25 Intent), thresholds de tier configurados pelo CMO/Sales Lead

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lead normalizado (Scout output) + dados enriquecidos (Iris output quando disponíveis), ICP Data Model versionado com at…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Score Card completo por lead: Score de Fit (0-100 com breakdown por dimensao firmografica), Score de Intent (0-100 com…) e persistir no artefato do squad.
4. Entregar ao critic Critique 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Score Card completo por lead: Score de Fit (0-100 com breakdown por dimensao firmografica), Score de Intent (0-100 com breakdown por sinal comportamental), Sco…
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

- **to:** Iris
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
