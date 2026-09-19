---
task: memoriaDoCrm()
responsavel: "Memória do CRM"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Call Analysis Object (objeções, sinais de compra, sinais de risco, próximo passo definido)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Call Score Object (score geral)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Deal ID e Contact ID no CRM"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Coaching Card gerado pelo Sensei"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Mapeamento de campos customizados do CRM do cliente configurado no Blueprint"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Deal atualizado no CRM com: nota de call (resumo de 5 bullets), objeções como propriedades customizadas (Objecão_Preço, Objecão_Timing, Objecão_Autoridade com texto exato), Score_Ultima_Call, Sinais_de_Compra_Detectados, Próximo_Passo_Confirmado (sim/não), Data_Próximo_Passo, Nível_Risco_Deal (calculado pela combinação de sinais de risco)"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Activity log criado na timeline do deal"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Alerta via Slack/WhatsApp para gestor se risco_deal = ALTO"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Task criada no ClickUp para vendedor com link para o Coaching Card"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento coaching_card_generated publicado pelo Sensei. Roda em paralelo com a entrega do coaching. SLA: máximo 10 minutos para CRM atualizado. Alerta de risco alto: imediato, sem esperar o coaching ca…"
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

# Sincronizar Dados Deal CRM

**Task ID:** `memoriaDoCrm()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Sincronizar Dados Deal CRM |
| **status** | `pending` |
| **responsible_executor** | Memória do CRM (Atualizador de Deal (Memória do CRM)) |
| **execution_type** | `Worker` |
| **input** | 5 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de sincronizacao com CRM. Extrai os dados relevantes do ciclo de analise e grava no deal e no contato do CRM de forma estruturada: objecoes levantadas (como propriedades customizadas), sinais de compra detectados, proximo passo confirmado, score da call, nivel de risco do deal atualizado. Garante que o historico da call seja consultavel pelo gestor no CRM sem precisar ouvir a gravacao. Tambem dispara alertas para o Orchestrator quando detecta sinais de risco alto na call (ex: prospect mencionou concorrente especifico com proposta mais barata — requer acao imediata do gestor).

## Input

- Call Analysis Object (objeções, sinais de compra, sinais de risco, próximo passo definido)
- Call Score Object (score geral)
- Deal ID e Contact ID no CRM
- Coaching Card gerado pelo Sensei
- Mapeamento de campos customizados do CRM do cliente configurado no Blueprint

## Output

- Deal atualizado no CRM com: nota de call (resumo de 5 bullets), objeções como propriedades customizadas (Objecão_Preço, Objecão_Timing, Objecão_Autoridade com texto exato), Score_Ultima_Call, Sinais_de_Compra_Detectados, Próximo_Passo_Confirmado (sim/não), Data_Próximo_Passo, Nível_Risco_Deal (calculado pela combinação de sinais de risco)
- Activity log criado na timeline do deal
- Alerta via Slack/WhatsApp para gestor se risco_deal = ALTO
- Task criada no ClickUp para vendedor com link para o Coaching Card

## Trigger

Evento coaching_card_generated publicado pelo Sensei. Roda em paralelo com a entrega do coaching. SLA: máximo 10 minutos para CRM atualizado. Alerta de risco alto: imediato, sem esperar o coaching card.

## Knowledge base (o que o executor consulta)

- Mapeamento de campos customizados do CRM do cliente (configurado no Blueprint
- cada cliente tem campos diferentes)
- Credenciais do CRM via MCP (HubSpot MCP disponivel nativamente)
- Logica de calculo de Nivel_Risco_Deal: combinacao de objecoes nao tratadas, sinais de risco detectados e talk_ratio desequilibrado
- Templates de nota de call padronizados por tipo de reuniao (discovery, proposta, negociacao)
- Regras de SLA de proximo passo por estagio do funil

## Action Items

1. Confirmar o gatilho e carregar a entrada (Call Analysis Object (objeções, sinais de compra, sinais de risco, próximo passo definido)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Deal atualizado no CRM com: nota de call (resumo de 5 bullets), objeções como propriedades customizadas (Objecão_Preço,…) e persistir no artefato do squad.
4. Entregar ao critic Calibrador; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Deal atualizado no CRM com: nota de call (resumo de 5 bullets), objeções como propriedades customizadas (Objecão_Preço, Objecão_Timing, Objecão_Autoridade com…
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

- **to:** Radar do Time
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
