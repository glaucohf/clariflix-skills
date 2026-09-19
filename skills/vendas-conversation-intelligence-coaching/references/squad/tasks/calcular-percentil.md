---
task: juiz()
responsavel: "Juiz"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Call Analysis Object completo do Sherlock da Call"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Rubrica de Avaliação com pesos por dimensão"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Histórico de scores do vendedor nas últimas 30 calls"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Benchmark do time (P50 e P75 por dimensão)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Perfil do 'closer ideal' com scores de referência"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Call Score Object: {call_id, vendedor_id, score_geral: 0-100, scores_por_dimensao: {abertura: 0-10, descoberta_de_dor: 0-10, qualificação_bant: 0-10, apresentação_solução: 0-10, tratamento_objeções: 0-10, negociação: 0-10, fechamento: 0-10, próximo_passo: 0-10, talk_ratio: 0-10, uso_de_silêncio: 0-10, urgência: 0-10, rapport: 0-10}, percentil_no_time: 0-100, vs_closer_ideal_delta: {dimensão, gap}[], top_3_areas_de_melhoria: [{dimensão, score_atual, score_benchmark, gap, impacto_estimado}], tendência_30_dias: 'melhorando'|'estável'|'piorando', comparativo_semana_anterior: {score_anterior, delta}}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento call_analyzed publicado pelo Sherlock da Call. Roda em sequência após análise. SLA: máximo 2 minutos."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Calibrador antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação tomar (ligar agora, escalar para diretor, ajustar proposta, aceitar perda) antes de qualquer comunicação automatizada com o prospect. SLA de resposta: 4h em dias úteis."
    - "[ ] HITL: HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Humano (gestor ou especialista de produto) deve validar a classificação e criar o counter-script antes que o sistema use-o em coachings futuros. Evita ensinar o time a responder errado."
    - "[ ] HITL: HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para que ele decida se faz uma sessão 1:1 urgente com o vendedor ou se o deal precisar de intervenção direta do gestor. Vendedor não é notificado do score crítico sem acompanhamento humano."
    - "[ ] HITL: HITL-4 (L2): Transcrição com qualidade de áudio abaixo de 75% de confiança — a Babel sinaliza e o gestor decide se envia para transcrição manual, descarta a call da análise ou aceita os resultados com baixa confiança. Garante que coaching baseado em transcrição ruim não chegue ao vendedor."
    - "[ ] HITL: HITL-5 (L2): Calibração quinzenal da Rubrica de Avaliação — o gestor revisa um sample de 5 calls para verificar se os scores do Juiz estão alinhados com sua percepção. Ajusta pesos de dimensões se necessário. Previne drift do modelo de scoring ao longo do tempo."
---

# Calcular Percentil

**Task ID:** `juiz()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Calcular Percentil |
| **status** | `pending` |
| **responsible_executor** | Juiz (Avaliador de Performance (Juiz)) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de scoring quantitativo da call. Recebe o Call Analysis Object e aplica a Rubrica de Avaliação para gerar um score numérico por dimensão e um score geral da call (0-100). Calcula o score percentil do vendedor em relação ao histórico do time e em relação ao perfil do 'closer ideal' calibrado no Blueprint. Identifica as 3 dimensões de maior impacto para melhoria (maior gap entre score atual e benchmark). Rastreia evolução do score do vendedor ao longo do tempo (semana a semana, mês a mês) para medir progresso de coaching.

## Input

- Call Analysis Object completo do Sherlock da Call
- Rubrica de Avaliação com pesos por dimensão
- Histórico de scores do vendedor nas últimas 30 calls
- Benchmark do time (P50 e P75 por dimensão)
- Perfil do 'closer ideal' com scores de referência

## Output

- Call Score Object: {call_id, vendedor_id, score_geral: 0-100, scores_por_dimensao: {abertura: 0-10, descoberta_de_dor: 0-10, qualificação_bant: 0-10, apresentação_solução: 0-10, tratamento_objeções: 0-10, negociação: 0-10, fechamento: 0-10, próximo_passo: 0-10, talk_ratio: 0-10, uso_de_silêncio: 0-10, urgência: 0-10, rapport: 0-10}, percentil_no_time: 0-100, vs_closer_ideal_delta: {dimensão, gap}[], top_3_areas_de_melhoria: [{dimensão, score_atual, score_benchmark, gap, impacto_estimado}], tendência_30_dias: 'melhorando'|'estável'|'piorando', comparativo_semana_anterior: {score_anterior, delta}}

## Trigger

Evento call_analyzed publicado pelo Sherlock da Call. Roda em sequência após análise. SLA: máximo 2 minutos.

## Knowledge base (o que o executor consulta)

- Rubrica de Avaliação com pesos e fórmula de scoring por dimensão
- Histórico de scores de todas as calls do time armazenado no Supabase
- Benchmark do time atualizado semanalmente (P50, P75, P90 por dimensão)
- Perfil do closer ideal com scores de referência por segmento
- Tabela de pesos de impacto por dimensão (tratamento de objeções e qualificação pesam mais do que rapport, por exemplo)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Call Analysis Object completo do Sherlock da Call).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Call Score Object: {call_id, vendedor_id, score_geral: 0-100, scores_por_dimensao: {abertura: 0-10, descoberta_de_dor:…) e persistir no artefato do squad.
4. Entregar ao critic Calibrador; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Call Score Object: {call_id, vendedor_id, score_geral: 0-100, scores_por_dimensao: {abertura: 0-10, descoberta_de_dor: 0-10, qualificação_bant: 0-10, apresenta…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Calibrador registrado
- [ ] Gate HITL respeitado: HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação t…
- [ ] Gate HITL respeitado: HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Hum…
- [ ] Gate HITL respeitado: HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para q…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — HITL-1 (L3): Deal Risk Alert de nível ALTO ou CRÍTICO gerado pelo Vigilante — gestor recebe alerta no WhatsApp e deve confirmar qual ação tomar (ligar agora, e… | BLOQUEIA até decisão humana |
| VETO-002 | HITL — HITL-2 (L3): Objeção de tipo não mapeado detectada pela primeira vez — o Analisador sinaliza objeção nova fora da biblioteca existente. Humano (gestor ou espec… | BLOQUEIA até decisão humana |
| VETO-003 | HITL — HITL-3 (L2): Score da call abaixo de 40/100 (call catastrófica) — além do coaching card automático, o Orchestrator notifica o gestor para que ele decida se faz… | BLOQUEIA até decisão humana |
| VETO-004 | HITL — HITL-4 (L2): Transcrição com qualidade de áudio abaixo de 75% de confiança — a Babel sinaliza e o gestor decide se envia para transcrição manual, descarta a ca… | BLOQUEIA até decisão humana |
| VETO-005 | HITL — HITL-5 (L2): Calibração quinzenal da Rubrica de Avaliação — o gestor revisa um sample de 5 calls para verificar se os scores do Juiz estão alinhados com sua pe… | BLOQUEIA até decisão humana |
| VETO-006 | HITL — HITL-6 (L1): Aprovação do Plano de Role-Play semanal gerado pelo Radar do Time — gestor revisa as objeções priorizadas e o script de simulação antes de compart… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic Calibrador | BLOQUEIA entrega |

## Handoff

- **to:** Sensei
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
