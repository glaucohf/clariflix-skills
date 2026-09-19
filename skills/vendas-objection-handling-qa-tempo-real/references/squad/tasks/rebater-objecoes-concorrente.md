---
task: challenger()
responsavel: "CHALLENGER"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto da objeção classificada como competitor_objection ou status_quo_objection, nome do concorrente mencionado (ou top-3 prováveis pelo setor), perfil do prospect, produto/plano sendo ofertado"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de resposta com: (1) resposta principal que reconhece o concorrente sem atacar + posiciona o diferencial relevante para a dor especifica do prospect, (2) 2 perguntas challenger que revelam gaps do concorrente atual sem mencionar o nome, (3) caso de migracao analogona base (cliente que mudou de X para nos com resultado Y), (4) flag se este concorrente tem vulnerabilidade especifica para este perfil de prospect"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo MAESTRO quando objeção classificada como competitor_objection, status_quo, incumbent_vendor, ou quando prospect menciona nome de concorrente específico. SLA: output em < 10 segundos (pre…"
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

# Rebater Objeções Concorrente

**Task ID:** `challenger()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Rebater Objeções Concorrente |
| **status** | `pending` |
| **responsible_executor** | CHALLENGER (CHALLENGER — O Rebatedor de Objeções de Concorrente e Status Quo) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em objecoes de concorrente e status quo — as que exigem mais inteligencia competitiva e precisao. Lida com: 'ja temos um fornecedor', 'estamos usando X e funciona', 'voces sao iguais ao Y', 'o Z e mais barato e faz a mesma coisa', 'nao quero mudar o que esta funcionando'. Para cada objecao, identifica qual concorrente esta em jogo (explicitamente mencionado ou inferido), recupera o battlecard especifico desse concorrente, e monta a resposta que posiciona a diferencacao sem denegrir o concorrente (o que gera desconfianca). Especializado na tecnica de 'Challenger Sale': questionar o status quo com perguntas que revelam gaps que o prospect ainda nao percebeu.

## Input

- Texto da objeção classificada como competitor_objection ou status_quo_objection, nome do concorrente mencionado (ou top-3 prováveis pelo setor), perfil do prospect, produto/plano sendo ofertado

## Output

- Pacote de resposta com: (1) resposta principal que reconhece o concorrente sem atacar + posiciona o diferencial relevante para a dor especifica do prospect, (2) 2 perguntas challenger que revelam gaps do concorrente atual sem mencionar o nome, (3) caso de migracao analogona base (cliente que mudou de X para nos com resultado Y), (4) flag se este concorrente tem vulnerabilidade especifica para este perfil de prospect

## Trigger

Disparo pelo MAESTRO quando objeção classificada como competitor_objection, status_quo, incumbent_vendor, ou quando prospect menciona nome de concorrente específico. SLA: output em < 10 segundos (precisa de busca em base de battlecards).

## Knowledge base (o que o executor consulta)

- Base de battlecards competitivos do cliente (segmentada por concorrente, atualizada pelo ARQUIVO após cada interação), histórico de win/loss contra cada concorrente no CRM, casos de migração documentados com métricas de resultado, fraquezas documentadas de cada concorrente por tipo de prospect, técnicas de Challenger Sale adaptadas ao produto do cliente

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto da objeção classificada como competitor_objection ou status_quo_objection, nome do concorrente mencionado (ou top…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de resposta com: (1) resposta principal que reconhece o concorrente sem atacar + posiciona o diferencial relevan…) e persistir no artefato do squad.
4. Entregar ao critic ARGUS; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de resposta com: (1) resposta principal que reconhece o concorrente sem atacar + posiciona o diferencial relevante para a dor especifica do prospect, (2…
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

- **to:** TECNICO
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
