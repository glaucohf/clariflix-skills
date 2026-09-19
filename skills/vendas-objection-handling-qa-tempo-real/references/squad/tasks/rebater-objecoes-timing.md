---
task: tempo()
responsavel: "TEMPO"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto da objeção classificada como timing_objection ou priority_objection, contexto do momento do prospect (notícias recentes da empresa se disponíveis, stage do funil, quando foi o primeiro contato, número de interações anteriores), produto sendo ofertado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de resposta com: (1) resposta principal personalizada ao momento do prospect, (2) argumento de urgencia baseado em dado concreto (ex: 'empresas do seu setor que adiaram esse investimento em Q4 perderam X% de conversao até o verão'), (3) micro-compromisso sugerido caso prospect nao esteja pronto, (4) pergunta de redirecionamento para qualificar se 'nao agora' e objecao real ou stall, (5) sugestao de data de follow-up automatico para o ARQUIVO registrar no CRM"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo MAESTRO quando objeção classificada como timing_objection, priority_objection, budget_cycle, ou 'call_me_later'. SLA: output em < 8 segundos."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic ARGUS antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Qualquer resposta que envolva promessa de desconto acima do nível autorizado para o vendedor: MAESTRO pausa, notifica supervisor ou gerente de vendas via Slack/WhatsApp, que aprova ou rejeita em tempo real antes da resposta chegar ao vendedor"
    - "[ ] L3: Qualquer resposta a dúvida técnica que envolva prazo de implementação customizado, SLA não padrão, ou integração não documentada na base: TÉCNICO flag como HITL, vendedor recebe instrução 'vou confirmar com a equipe técnica e te retorno em X horas' em vez de uma promessa não verificada"
    - "[ ] L3: Escrita de resultados de call e atualização de stage no CRM pelo ARQUIVO: vendedor confirma o resultado via formulário rápido (1 click) antes de qualquer persistência em CRM de produção"
    - "[ ] L2: Quando ARGUS emite REJEITADO por factualidade: MAESTRO notifica o vendedor que a resposta está sendo verificada e entrega uma resposta genérica segura enquanto o worker corrige — o vendedor decide se usa a genérica ou aguarda a corrigida"
    - "[ ] L1: Objecão nova não catalogada (aparece pela primeira vez): ARQUIVO sinaliza ao líder de vendas ou product owner que uma nova objecão foi detectada e sugere draft de resposta para validação antes de entrar na base — o líder aprova, edita ou rejeita o draft"
---

# Rebater Objecoes Timing

**Task ID:** `tempo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Rebater Objecoes Timing |
| **status** | `pending` |
| **responsible_executor** | TEMPO (TÉMPO — O Rebatedor de Objeções de Timing e Prioridade) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em objeções de timing, urgência e prioridade — a segunda categoria mais frequente pos-preço. Lida com: 'não é o momento', 'estamos em período de corte', 'volte no próximo trimestre', 'precisamos resolver X antes', 'não é prioridade agora'. O TÉMPO analisa o contexto do negócio do prospect (sinais de momento detectados no CRM ou na conversa) e gera resposta que ou (a) cria urgência real baseada em consequências concretas de não agir agora, ou (b) propõe um micro-compromisso que mantém o deal vivo sem pressionar (ex: 'posso te mandar um resumo de 1 página para você ter quando o momento chegar?'). Evita o 'ok, quando você quiser me liga' que enterra o deal.

## Input

- Texto da objeção classificada como timing_objection ou priority_objection, contexto do momento do prospect (notícias recentes da empresa se disponíveis, stage do funil, quando foi o primeiro contato, número de interações anteriores), produto sendo ofertado

## Output

- Pacote de resposta com: (1) resposta principal personalizada ao momento do prospect, (2) argumento de urgencia baseado em dado concreto (ex: 'empresas do seu setor que adiaram esse investimento em Q4 perderam X% de conversao até o verão'), (3) micro-compromisso sugerido caso prospect nao esteja pronto, (4) pergunta de redirecionamento para qualificar se 'nao agora' e objecao real ou stall, (5) sugestao de data de follow-up automatico para o ARQUIVO registrar no CRM

## Trigger

Disparo pelo MAESTRO quando objeção classificada como timing_objection, priority_objection, budget_cycle, ou 'call_me_later'. SLA: output em < 8 segundos.

## Knowledge base (o que o executor consulta)

- Base de objeções de timing com respostas que converteram historicamente (segmentada por setor e por stage do funil), dados setoriais de sazonalidade e ciclos de compra (ex: imobiliárias compram mais em fev-abr e ago-out), argumentos de custo de atraso por vertical, templates de micro-compromisso por tipo de produto, regras de follow-up automático por cenário

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto da objeção classificada como timing_objection ou priority_objection, contexto do momento do prospect (notícias re…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de resposta com: (1) resposta principal personalizada ao momento do prospect, (2) argumento de urgencia baseado…) e persistir no artefato do squad.
4. Entregar ao critic ARGUS; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de resposta com: (1) resposta principal personalizada ao momento do prospect, (2) argumento de urgencia baseado em dado concreto (ex: 'empresas do seu s…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic ARGUS registrado
- [ ] Gate L3 respeitado: Qualquer resposta que envolva promessa de desconto acima do nível autorizado para o vendedor: MAESTRO pausa, notifica supervisor ou gerente…
- [ ] Gate L3 respeitado: Qualquer resposta a dúvida técnica que envolva prazo de implementação customizado, SLA não padrão, ou integração não documentada na base: T…
- [ ] Gate L3 respeitado: Escrita de resultados de call e atualização de stage no CRM pelo ARQUIVO: vendedor confirma o resultado via formulário rápido (1 click) ant…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Qualquer resposta que envolva promessa de desconto acima do nível autorizado para o vendedor: MAESTRO pausa, notifica supervisor ou gerente de vendas via Slack… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Qualquer resposta a dúvida técnica que envolva prazo de implementação customizado, SLA não padrão, ou integração não documentada na base: TÉCNICO flag como HIT… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Escrita de resultados de call e atualização de stage no CRM pelo ARQUIVO: vendedor confirma o resultado via formulário rápido (1 click) antes de qualquer persi… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Quando ARGUS emite REJEITADO por factualidade: MAESTRO notifica o vendedor que a resposta está sendo verificada e entrega uma resposta genérica segura enquanto… | BLOQUEIA até decisão humana |
| VETO-005 | L1 — Objecão nova não catalogada (aparece pela primeira vez): ARQUIVO sinaliza ao líder de vendas ou product owner que uma nova objecão foi detectada e sugere draft… | BLOQUEIA até decisão humana |
| VETO-006 | Saída sem veredito do critic ARGUS | BLOQUEIA entrega |

## Handoff

- **to:** CHALLENGER
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
