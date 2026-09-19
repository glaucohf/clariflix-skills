---
task: sensei()
responsavel: "Sensei"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Call Score Object completo do Juiz"
  - nome: entrada2
    tipo: object
    obrigatorio: false
    descricao: "Call Analysis Object completo do Sherlock da Call"
  - nome: entrada3
    tipo: object
    obrigatorio: false
    descricao: "Transcript Object com timestamps para referência exata de momentos"
  - nome: entrada4
    tipo: object
    obrigatorio: false
    descricao: "Histórico de coaching do vendedor (para não repetir o mesmo feedback e medir se melhorou)"
  - nome: entrada5
    tipo: object
    obrigatorio: false
    descricao: "Biblioteca de Counter-Scripts por tipo de objeção"
  - nome: entrada6
    tipo: object
    obrigatorio: false
    descricao: "Perfil do vendedor (nível, pontos fortes conhecidos, áreas de desenvolvimento em andamento)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Coaching Card (Markdown + JSON): {call_id, vendedor_id, data, score_geral, resumo_executivo: '3 frases sobre a call', pontos_positivos: [{momento_exato, texto_vendedor, por_quê_funcionou}], áreas_de_melhoria: [{prioridade: 1|2|3, dimensão, momento_exato_seg, o_que_foi_dito: 'transcrição exata', o_que_deveria_ser_dito: 'counter-script sugerido', por_quê_importa: 'impacto no deal', exemplo_alternativo: 'script na voz do vendedor'}], objeções_não_tratadas: [{objeção_exata, counter_script_recomendado, fonte_da_biblioteca}], próximos_passos_coaching: [{ação, prazo, como_medir}], pergunta_reflexiva: 'uma pergunta que faz o vendedor pensar'}"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Entregue via email/WhatsApp direto para o vendedor com link para o trecho exato da call"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Evento call_scored publicado pelo Juiz. Roda em sequencia apos scoring. SLA de entrega do coaching card: maximo 30 minutos apos encerramento da call. Tambem roda em modo batch semanal para consolidar…"
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

# Gerar Coaching Card

**Task ID:** `sensei()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Conversation Intelligence e Coaching

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Gerar Coaching Card |
| **status** | `pending` |
| **responsible_executor** | Sensei (Coach de Vendas (Sênsêi)) |
| **execution_type** | `Agent` |
| **input** | 6 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de geração de coaching acionável. O núcleo intelectual do squad — transforma o Call Score Object e o Call Analysis Object em um Coaching Card ultra-específico para o vendedor: não feedback genérico, mas reprodução do momento exato da call com o que foi dito, o que deveria ter sido dito e por quê. Gera o counter-script ideal para cada objeção não tratada adequadamente, com exemplo de resposta na voz do vendedor (adaptado ao estilo de comunicação identificado na transcrição). Prioriza os 3 insights de maior impacto imediato — o vendedor não precisa mudar tudo de uma vez.

## Input

- Call Score Object completo do Juiz
- Call Analysis Object completo do Sherlock da Call
- Transcript Object com timestamps para referência exata de momentos
- Histórico de coaching do vendedor (para não repetir o mesmo feedback e medir se melhorou)
- Biblioteca de Counter-Scripts por tipo de objeção
- Perfil do vendedor (nível, pontos fortes conhecidos, áreas de desenvolvimento em andamento)

## Output

- Coaching Card (Markdown + JSON): {call_id, vendedor_id, data, score_geral, resumo_executivo: '3 frases sobre a call', pontos_positivos: [{momento_exato, texto_vendedor, por_quê_funcionou}], áreas_de_melhoria: [{prioridade: 1|2|3, dimensão, momento_exato_seg, o_que_foi_dito: 'transcrição exata', o_que_deveria_ser_dito: 'counter-script sugerido', por_quê_importa: 'impacto no deal', exemplo_alternativo: 'script na voz do vendedor'}], objeções_não_tratadas: [{objeção_exata, counter_script_recomendado, fonte_da_biblioteca}], próximos_passos_coaching: [{ação, prazo, como_medir}], pergunta_reflexiva: 'uma pergunta que faz o vendedor pensar'}
- Entregue via email/WhatsApp direto para o vendedor com link para o trecho exato da call

## Trigger

Evento call_scored publicado pelo Juiz. Roda em sequencia apos scoring. SLA de entrega do coaching card: maximo 30 minutos apos encerramento da call. Tambem roda em modo batch semanal para consolidar coaching da semana em Plano de Desenvolvimento Individual.

## Knowledge base (o que o executor consulta)

- Biblioteca de Counter-Scripts com 30+ objeções e respostas validadas pelo cliente no Blueprint
- Histórico de coaching de cada vendedor (armazenado no Supabase) para continuidade e medição de progresso
- Perfis de estilo de comunicação por vendedor (formal vs informal, direto vs consultivo)
- Princípios de coaching de vendas (SPIN, Challenger, MEDDIC) para embasar os counter-scripts
- Biblioteca de perguntas de discovery de alta performance por segmento

## Action Items

1. Confirmar o gatilho e carregar a entrada (Call Score Object completo do Juiz).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Coaching Card (Markdown + JSON): {call_id, vendedor_id, data, score_geral, resumo_executivo: '3 frases sobre a call', p…) e persistir no artefato do squad.
4. Entregar ao critic Calibrador; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Coaching Card (Markdown + JSON): {call_id, vendedor_id, data, score_geral, resumo_executivo: '3 frases sobre a call', pontos_positivos: [{momento_exato, texto_…
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

- **to:** Memória do CRM
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
