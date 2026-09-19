---
task: maestroPipeline()
responsavel: "Maestro"
responsavel_type: Agente
atomic_layer: Organism
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Conversation Intelligence Dashboard (ClickUp + Notion + CRM): (1) Coaching Card por call"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "entregue direto ao vendedor via WhatsApp/Notion em até 30 minutos após a call, com transcript, score, top 3 insights acionáveis e counter-scripts específicos"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "(2) Briefing Semanal do Gestor"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "1 página com score médio do time, top objeções da semana, ranking de vendedores, deals em risco e clip da semana"
  - nome: saida5
    tipo: object
    obrigatorio: false
    descricao: "(3) Deal Risk Alerts em tempo real"
  - nome: saida6
    tipo: object
    obrigatorio: false
    descricao: "alerta no WhatsApp do gestor quando call detecta risco alto, com diagnóstico e ação recomendada"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central que recebe o evento de call encerrada (webhook de plataforma de voz/video), verifica se a call atende criterios de processamento (duracao minima, tipo de reuniao, participantes),…"
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

# Orquestrar Pipeline do Conversation Intelligence e Coaching

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Conversation Intelligence e Coaching |
| **status** | `pending` |
| **responsible_executor** | Maestro (Diretor de Inteligência Comercial (Maestro)) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 11 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central que recebe o evento de call encerrada (webhook de plataforma de voz/video), verifica se a call atende criterios de processamento (duracao minima, tipo de reuniao, participantes), decompoe o pipeline de analise em subtarefas sequenciais e paralelas, gerencia o estado de cada call no ciclo de processamento, roteia para workers especializados na ordem correta (transcricao -> analise -> scoring -> coaching -> CRM), consolida os outputs em artefatos finais e distribui para os destinatarios certos (vendedor recebe coaching card, gestor recebe dashboard, CRM recebe deal insights). Monitora proativamente calls processadas ha mais de 24h sem coaching entregue e re-dispara o pipeline se necessario.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Conversation Intelligence Dashboard (ClickUp + Notion + CRM): (1) Coaching Card por call
- entregue direto ao vendedor via WhatsApp/Notion em até 30 minutos após a call, com transcript, score, top 3 insights acionáveis e counter-scripts específicos
- (2) Briefing Semanal do Gestor
- 1 página com score médio do time, top objeções da semana, ranking de vendedores, deals em risco e clip da semana
- (3) Deal Risk Alerts em tempo real
- alerta no WhatsApp do gestor quando call detecta risco alto, com diagnóstico e ação recomendada
- (4) Biblioteca de Counter-Scripts viva
- atualizada automaticamente com novos padrões detectados nas calls, validados pelo gestor via HITL-2
- (5) Plano de Role-Play semanal
- roteiro de simulação gerado a partir das objeções mais frequentes da semana
- Artefato verificável por task no ClickUp: cada call processada gera um Coaching Card rastreável no Langfuse com trace completo do pipeline (Babel -> Sherlock -> Juiz -> Sensei -> Calibrador) e score de qualidade do Calibrador

## Trigger

Orquestrador central que recebe o evento de call encerrada (webhook de plataforma de voz/video), verifica se a call atende criterios de processamento (duracao minima, tipo de reuniao, participantes), decompoe o pipeline de analise em subtarefas sequenciais e paralelas, gerencia o estado de cada call no ciclo de processamento, roteia para workers especializados na ordem correta (transcricao -> analise -> scoring -> coaching -> CRM), consolida os outputs em artefatos finais e distribui para os destinatarios certos (vendedor recebe coaching card, gestor recebe dashboard, CRM recebe deal insights). Monitora proativamente calls processadas ha mais de 24h sem coaching entregue e re-dispara o pipeline se necessario.

## Knowledge base (o que o executor consulta)

- Plataformas de voz/vídeo: Vapi (webhook pós-call com link de gravação), Retell AI, Zoom (webhook recording.completed), Google Meet (Drive API para gravações), Gupshup/AiSensy para calls gravadas via WhatsApp Business
- STT (Speech-to-Text): Deepgram (latência < 1min/hora de áudio, diarização de speakers, vocabulário customizado) ou AssemblyAI como fallback
- CRM: HubSpot (MCP disponível nativamente) ou Pipedrive
- gravação de insights, sinais de risco, score de call, próximo passo como campos customizados no deal e na timeline
- Gestão de tarefas: ClickUp
- Coaching Card como task atribuída ao vendedor com link para o trecho da call, proof-of-work verificável por task, Plano de Role-Play semanal como task coletiva
- Comunicação: WhatsApp Business API (Gupshup ou AiSensy) para entrega do coaching card ao vendedor e alertas de risco ao gestor
- Slack para integração com times que usam Slack como hub
- Armazenamento de artefatos: Supabase (PostgreSQL)
- Transcript Objects, Call Analysis Objects, Call Score Objects, histórico de coaching por vendedor, Feature Store de objeções
- Documentação de coaching: Notion
- Coaching Cards formatados, Biblioteca de Counter-Scripts, Plano de Desenvolvimento Individual por vendedor, Briefing Semanal do Gestor
- Observabilidade/Evals: Langfuse (OTEL)
- traces de todas as chamadas LLM (análise + coaching), quality gates por ambiente (dev 70% / staging 85% / prod 95%), evals de qualidade do coaching card (rastreabilidade, especificidade, tom)
- Orquestração: LangGraph + Claude Agent SDK
- controle de estado do pipeline de análise, workflows determinísticos de sequenciamento (transcrição -> análise -> scoring -> coaching), re-tentativas automáticas em falha
- Armazenamento de áudio: AWS S3 ou Google Cloud Storage
- arquivos de áudio/vídeo das calls com retenção configurável (90 dias default, 365 dias para deals fechados)

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic Calibrador antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Conversation Intelligence Dashboard (ClickUp + Notion + CRM): (1) Coaching Card por call
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

- **to:** Babel
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
