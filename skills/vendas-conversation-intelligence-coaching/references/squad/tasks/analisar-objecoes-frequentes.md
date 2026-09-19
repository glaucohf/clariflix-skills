---
task: radarDoTime()
responsavel: "Radar do Time"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Todos os Call Score Objects da semana (de todos os vendedores)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Todos os Call Analysis Objects da semana (objeções, sinais, ausências)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Histórico das últimas 4 semanas para comparação de tendências"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Meta de conversão do time e pipeline atual do CRM"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Briefing Semanal do Gestor (PDF/Notion): {semana, n_calls_analisadas, score_médio_time, tendência_vs_semana_anterior, top_3_objeções_semana_com_frequência_e_taxa_de_tratamento, ranking_vendedores_por_score_com_delta, vendedor_da_semana, área_de_melhoria_coletiva_mais_crítica, clip_da_semana: link para o melhor momento de call (para compartilhar no time), deals_em_risco_identificados_por_sinais_de_call, recomendação_de_foco_para_próximo_role_play}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Também gera Plano de Role-Play da semana seguinte baseado nas objeções mais frequentes não tratadas"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Job semanal toda Sexta às 17h. Também disparado manualmente pelo gestor via comando. Também gera alerta imediato quando objeção nova aparece em 3+ calls na mesma semana (possível mudança de mercado)."
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

# Analisar Objeções Frequentes

**Task ID:** `radarDoTime()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Objeções Frequentes |
| **status** | `pending` |
| **responsible_executor** | Radar do Time (Inteligência Coletiva (Radar do Time)) |
| **execution_type** | `Agent` |
| **input** | 4 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de analise agregada do time. Opera em nivel de time — nao analisa calls individuais, mas padres agregados. Consolida insights de todas as calls da semana para identificar: objecoes que estao aumentando em frequencia (sinal de problema de mercado ou de produto), dimensoes de performance que todo o time tem dificuldade (gap de treinamento sistemico), os melhores momentos de calls de alta performance (para criar biblioteca de 'calls vencedoras' para treinamento). Gera o Briefing Semanal do Gestor — um documento executivo de 1 pagina com os dados mais importantes da semana.

## Input

- Todos os Call Score Objects da semana (de todos os vendedores)
- Todos os Call Analysis Objects da semana (objeções, sinais, ausências)
- Histórico das últimas 4 semanas para comparação de tendências
- Meta de conversão do time e pipeline atual do CRM

## Output

- Briefing Semanal do Gestor (PDF/Notion): {semana, n_calls_analisadas, score_médio_time, tendência_vs_semana_anterior, top_3_objeções_semana_com_frequência_e_taxa_de_tratamento, ranking_vendedores_por_score_com_delta, vendedor_da_semana, área_de_melhoria_coletiva_mais_crítica, clip_da_semana: link para o melhor momento de call (para compartilhar no time), deals_em_risco_identificados_por_sinais_de_call, recomendação_de_foco_para_próximo_role_play}
- Também gera Plano de Role-Play da semana seguinte baseado nas objeções mais frequentes não tratadas

## Trigger

Job semanal toda Sexta às 17h. Também disparado manualmente pelo gestor via comando. Também gera alerta imediato quando objeção nova aparece em 3+ calls na mesma semana (possível mudança de mercado).

## Knowledge base (o que o executor consulta)

- Todos os artefatos de análise das últimas 8 semanas armazenados no Supabase
- Histórico de metas e resultados do time para contextualizar os dados
- Biblioteca de calls vencedoras (calls com score > 85 e deal fechado) para referência do clip_da_semana
- Framework de priorização de coaching coletivo vs individual (quando o problema é do time vs do vendedor específico)
- Templates de Briefing por perfil de gestor (executivo quer 1 página, head de vendas quer detalhes por vendedor)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Todos os Call Score Objects da semana (de todos os vendedores)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Briefing Semanal do Gestor (PDF/Notion): {semana, n_calls_analisadas, score_médio_time, tendência_vs_semana_anterior, t…) e persistir no artefato do squad.
4. Entregar ao critic Calibrador; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Briefing Semanal do Gestor (PDF/Notion): {semana, n_calls_analisadas, score_médio_time, tendência_vs_semana_anterior, top_3_objeções_semana_com_frequência_e_ta…
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

- **to:** Vigilante
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
