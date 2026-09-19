---
task: vigilante()
responsavel: "Vigilante"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Call Analysis Object (sinais de risco com severidade)"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Histórico de sinais de risco das últimas 3 calls do mesmo deal"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Status do deal no CRM (estágio, valor, dias em estágio, próximo passo agendado ou não)"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Score atual do deal no Lead Scoring Squad (se disponível via integração)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Benchmark de ciclo de vendas saudável por segmento e tamanho de deal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Deal Risk Alert quando risco_deal = ALTO ou CRÍTICO: {deal_id, vendedor_id, nível_risco: 'médio'|'alto'|'crítico', evidências: [{sinal, call_id, momento_exato, texto_exato, interpretação}], diagnóstico: 'o que provavelmente está acontecendo no deal', ação_recomendada: 'o que o gestor deve fazer agora', prazo_para_acão: 'antes de X data ou o deal some', probabilidade_perda_estimada_pct}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Alerta entregue via WhatsApp para o gestor com urgência explícita"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Task criada no ClickUp marcada como URGENTE"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Registro no CRM do deal como Deal_Risk_Flag = ALTO com justificativa"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Ao final de cada Call Analysis quando sinais_de_risco contiver pelo menos 1 item de severidade ALTO. Job de varredura semanal Segunda 08h em todos os deals ativos em estagio Proposta/Negociacao. Even…"
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

# Detectar Risco Deal

**Task ID:** `vigilante()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Detectar Risco Deal |
| **status** | `pending` |
| **responsible_executor** | Vigilante (Detector de Risco de Deal (Vigílante)) |
| **execution_type** | `Hybrid` |
| **input** | 5 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em identificar deals que estão em risco de ser perdidos com base nos sinais das calls — complementando o scoring do Lead Scoring Squad com dados qualitativos da conversa. Opera em tempo real por call e em modo de varredura semanal. Crucialmente, detecta sinais que o scoring quantitativo não captura: o tom de voz do prospect mudou (mais formal, menos engajado), o prospect mencionou um concorrente específico com proposta, o tomador de decisão deixou de aparecer nas calls. Quando detecta risco alto, aciona o HITL imediatamente — este é o agente com mais impacto imediato no revenue.

## Input

- Call Analysis Object (sinais de risco com severidade)
- Histórico de sinais de risco das últimas 3 calls do mesmo deal
- Status do deal no CRM (estágio, valor, dias em estágio, próximo passo agendado ou não)
- Score atual do deal no Lead Scoring Squad (se disponível via integração)
- Benchmark de ciclo de vendas saudável por segmento e tamanho de deal

## Output

- Deal Risk Alert quando risco_deal = ALTO ou CRÍTICO: {deal_id, vendedor_id, nível_risco: 'médio'|'alto'|'crítico', evidências: [{sinal, call_id, momento_exato, texto_exato, interpretação}], diagnóstico: 'o que provavelmente está acontecendo no deal', ação_recomendada: 'o que o gestor deve fazer agora', prazo_para_acão: 'antes de X data ou o deal some', probabilidade_perda_estimada_pct}
- Alerta entregue via WhatsApp para o gestor com urgência explícita
- Task criada no ClickUp marcada como URGENTE
- Registro no CRM do deal como Deal_Risk_Flag = ALTO com justificativa

## Trigger

Ao final de cada Call Analysis quando sinais_de_risco contiver pelo menos 1 item de severidade ALTO. Job de varredura semanal Segunda 08h em todos os deals ativos em estagio Proposta/Negociacao. Evento deal_silence (nenhuma call gravada nos ultimos 7 dias para deal em estagio avancado). Solicitacao manual do gestor.

## Knowledge base (o que o executor consulta)

- Dicionário de sinais de risco com pesos de probabilidade de perda: objeção de preço sem counter-script = +15% chance de perda
- menção de concorrente = +25%
- ausência de tomador de decisão na call de proposta = +35%
- combinação de 3+ sinais = risco crítico
- Histórico de deals perdidos com linha do tempo de sinais para calibrar os pesos (construído no Blueprint com dados reais do cliente)
- Benchmark de ciclo saudável por segmento: imobiliária média 21 dias, agência média 14 dias, B2B serviço média 30 dias
- Lista de stakeholders críticos por deal para detectar ausências

## Action Items

1. Confirmar o gatilho e carregar a entrada (Call Analysis Object (sinais de risco com severidade)).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Deal Risk Alert quando risco_deal = ALTO ou CRÍTICO: {deal_id, vendedor_id, nível_risco: 'médio'|'alto'|'crítico', evid…) e persistir no artefato do squad.
4. Entregar ao critic Calibrador; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Deal Risk Alert quando risco_deal = ALTO ou CRÍTICO: {deal_id, vendedor_id, nível_risco: 'médio'|'alto'|'crítico', evidências: [{sinal, call_id, momento_exato,…
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

- **to:** Calibrador
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
