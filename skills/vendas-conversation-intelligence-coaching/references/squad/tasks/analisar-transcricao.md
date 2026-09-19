---
task: sherlockDaCall()
responsavel: "Sherlock da Call"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Transcript Object completo da Babel"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Rubrica de Avaliação calibrada no Blueprint (12 dimensões com pesos)"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Biblioteca de Objeções do segmento com padrões de texto"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Perfil do vendedor (senior vs junior, SDR vs Closer) para contextualizar as expectativas"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Call Analysis Object: {call_id, objeções_detectadas: [{texto_exato, tipo: 'preço'|'timing'|'concorrente'|'autoridade'|'necessidade', momento_seg, foi_tratada: bool, qualidade_tratamento: 0-5}], sinais_de_compra: [{texto_exato, tipo, momento_seg, intensidade: 1-3}], sinais_de_risco: [{texto_exato, tipo, momento_seg, severidade: 'baixo'|'médio'|'alto'}], perguntas_vendedor: [{texto, tipo: 'aberta'|'fechada'|'leading', momento_seg}], momentos_críticos: [{descrição, momento_seg, impacto: 'positivo'|'negativo'}], ausências_detectadas: [{competência_esperada, descrição, impacto_estimado}], fase_call_atual: 'discovery'|'apresentação'|'negociação'|'fechamento', próximo_passo_definido: bool, próximo_passo_texto: str}"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento transcript_ready publicado pela Babel. Processamento sequencial obrigatório (não pode rodar sem Transcript Object completo). SLA de processamento: máximo 5 minutos após transcrição disponível."
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

# Analisar Transcricao

**Task ID:** `sherlockDaCall()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Transcricao |
| **status** | `pending` |
| **responsible_executor** | Sherlock da Call (Analisador de Padrões (Sherlock da Call)) |
| **execution_type** | `Worker` |
| **input** | 4 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de análise semântica profunda da transcrição. Executa múltiplas análises em paralelo sobre o Transcript Object: detecção de objeções (explícitas e implícitas), identificação de sinais de compra (frases de interesse, perguntas sobre implementação, perguntas sobre preço como compradores), detecção de sinais de risco de deal (menção de concorrente, comentário sobre orçamento, stakeholder ausente na call), análise de perguntas feitas pelo vendedor (abertas vs fechadas, sequência de discovery), mapeamento de momentos críticos da call (onde a energia caiu, onde o prospect se engajou mais, onde o vendedor perdeu o fio). Também detecta ausências: o que o vendedor NÃO fez que deveria ter feito (não qualificou budget, não perguntou sobre processo de decisão, não definiu próximo passo).

## Input

- Transcript Object completo da Babel
- Rubrica de Avaliação calibrada no Blueprint (12 dimensões com pesos)
- Biblioteca de Objeções do segmento com padrões de texto
- Perfil do vendedor (senior vs junior, SDR vs Closer) para contextualizar as expectativas

## Output

- Call Analysis Object: {call_id, objeções_detectadas: [{texto_exato, tipo: 'preço'|'timing'|'concorrente'|'autoridade'|'necessidade', momento_seg, foi_tratada: bool, qualidade_tratamento: 0-5}], sinais_de_compra: [{texto_exato, tipo, momento_seg, intensidade: 1-3}], sinais_de_risco: [{texto_exato, tipo, momento_seg, severidade: 'baixo'|'médio'|'alto'}], perguntas_vendedor: [{texto, tipo: 'aberta'|'fechada'|'leading', momento_seg}], momentos_críticos: [{descrição, momento_seg, impacto: 'positivo'|'negativo'}], ausências_detectadas: [{competência_esperada, descrição, impacto_estimado}], fase_call_atual: 'discovery'|'apresentação'|'negociação'|'fechamento', próximo_passo_definido: bool, próximo_passo_texto: str}

## Trigger

Evento transcript_ready publicado pela Babel. Processamento sequencial obrigatório (não pode rodar sem Transcript Object completo). SLA de processamento: máximo 5 minutos após transcrição disponível.

## Knowledge base (o que o executor consulta)

- Rubrica de Avaliação calibrada no Diagnóstico com 12 dimensões e pesos por tipo de call (discovery, proposta, negociação)
- Biblioteca de Objeções com 30+ padrões de texto por categoria (preço, timing, concorrente, autoridade, necessidade, produto)
- Dicionário de sinais de compra por segmento (frases que prospects usam quando querem comprar mas ainda não disseram sim)
- Dicionário de sinais de risco de deal com histórico de correlação com perda
- Perfis de vendedor por nível de senioridade com expectativas calibradas

## Action Items

1. Confirmar o gatilho e carregar a entrada (Transcript Object completo da Babel).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Call Analysis Object: {call_id, objeções_detectadas: [{texto_exato, tipo: 'preço'|'timing'|'concorrente'|'autoridade'|'…) e persistir no artefato do squad.
4. Entregar ao critic Calibrador; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Call Analysis Object: {call_id, objeções_detectadas: [{texto_exato, tipo: 'preço'|'timing'|'concorrente'|'autoridade'|'necessidade', momento_seg, foi_tratada:…
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

- **to:** Juiz
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
