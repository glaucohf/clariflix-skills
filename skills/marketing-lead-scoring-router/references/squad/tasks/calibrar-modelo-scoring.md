---
task: critique()
responsavel: "Critique"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sample de leads roteados com Score Card completo + outcome registrado no CRM (converteu/lost/em andamento), feedback qualitativo dos SDRs sobre qualidade dos leads Hot entregues (formulário semanal no ClickUp), dados de conversão por tier dos últimos 30 dias, Score Card Model atual com todos os pesos, proposta de recalibração gerada pelo Pulse"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Auditoria de qualidade: APPROVED/NEEDS_CALIBRATION/ALERT com justificativa detalhada, lista de falsos positivos e falsos negativos identificados com análise de causa raiz, Precision@tier (% de leads Hot que realmente eram qualificados), Recall@tier (% dos leads que converteram que foram corretamente identificados como Hot), proposta de ajuste de pesos com impacto estimado na distribuição de scores, flag de ALERT quando desvio crítico detectado (exige intervenção humana imediata antes de continuar operando)"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ciclo quinzenal automático de auditoria de amostra; lead Hot marcado como não qualificado pelo SDR (trigger imediato); taxa de conversão de tier Hot cai abaixo de 25% em qualquer semana (anomalia crí…"
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

# Calibrar Modelo Scoring

**Task ID:** `critique()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Lead Scoring & Router

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calibrar Modelo Scoring |
| **status** | `pending` |
| **responsible_executor** | Critique (Critique — Critic & Model Calibration Agent) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Agente de verificação crítica e calibração contínua do modelo de scor­ing. Nas primeiras 4 semanas de produção, audita 100% dos leads Hot (todos devem ser validados) e 20% dos demais tiers por amostragem. Apos 4 semanas, auditoria continua de 10% por amostragem + auditoria completa de leads que converteram ou foram marcados como lost. Detecta: falsos positivos (leads Hot que o SDR classificou como não qualificados), falsos negativos (leads Cold/Warm que converte­ram sem ter sido priorizados), sistêmatic bias no modelo (ex: modelo penalizando segmento que na realidade converte bem), dados de enriquecimento incorretos que distorceram o score. Toda calibração do modelo (alteração de pesos) passa obrigatoriamente por Critique antes de Orion aplicar.

## Input

- Sample de leads roteados com Score Card completo + outcome registrado no CRM (converteu/lost/em andamento), feedback qualitativo dos SDRs sobre qualidade dos leads Hot entregues (formulário semanal no ClickUp), dados de conversão por tier dos últimos 30 dias, Score Card Model atual com todos os pesos, proposta de recalibração gerada pelo Pulse

## Output

- Auditoria de qualidade: APPROVED/NEEDS_CALIBRATION/ALERT com justificativa detalhada, lista de falsos positivos e falsos negativos identificados com análise de causa raiz, Precision@tier (% de leads Hot que realmente eram qualificados), Recall@tier (% dos leads que converteram que foram corretamente identificados como Hot), proposta de ajuste de pesos com impacto estimado na distribuição de scores, flag de ALERT quando desvio crítico detectado (exige intervenção humana imediata antes de continuar operando)

## Trigger

Ciclo quinzenal automático de auditoria de amostra; lead Hot marcado como não qualificado pelo SDR (trigger imediato); taxa de conversão de tier Hot cai abaixo de 25% em qualquer semana (anomalia crítica); proposta de recalibração de pesos gerada pelo Pulse; solicitação manual do Sales Lead via ClickUp

## Knowledge base (o que o executor consulta)

- Score Card Model histórico (todas as versões com performance por versão), dataset de leads convertidos vs lost com atributos completos (base de treinamento), definição de Qualified Lead da empresa (criterios que o Sales Lead usa), histórico de feedbacks dos SDRs por lead, métricas de benchmark de indústria (Precision > 60% para leads Hot e considerado bom em B2B SaaS/serviços)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Sample de leads roteados com Score Card completo + outcome registrado no CRM (converteu/lost/em andamento), feedback qu…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Auditoria de qualidade: APPROVED/NEEDS_CALIBRATION/ALERT com justificativa detalhada, lista de falsos positivos e falso…) e persistir no artefato do squad.
4. Entregar ao critic Critique 2; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Auditoria de qualidade: APPROVED/NEEDS_CALIBRATION/ALERT com justificativa detalhada, lista de falsos positivos e falsos negativos identificados com análise de…
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

- **to:** Critique 2
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
