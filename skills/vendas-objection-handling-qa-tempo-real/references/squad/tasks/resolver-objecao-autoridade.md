---
task: closer()
responsavel: "CLOSER"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto da objeção classificada como authority_objection ou closing_stall, stage atual do funil (se está em proposta ou fechamento), histórico de interações do deal (quantas calls já houveram, objeções anteriores no mesmo deal), valor do deal"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de resposta com: (1) diagnóstico"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "é objeção real de autoridade ou saída educada? (com indicadores), (2) resposta principal adaptada ao diagnóstico, (3) técnica de fechamento recomendada com script pronto, (4) pergunta de qualificação de decisor se aplicável ('quem mais estaria envolvido nessa decisão?'), (5) proposta de próximo passo concreto que mantém o momentum do deal"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo MAESTRO quando objeção classificada como authority_objection, think_it_over, need_approval, proposal_request, ou closing_stall. SLA: < 8 segundos. Prioridade máxima — é o momento mais cr…"
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

# Resolver Objeção Autoridade

**Task ID:** `closer()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Resolver Objeção Autoridade |
| **status** | `pending` |
| **responsible_executor** | CLOSER (CLOSER — O Especialista em Objeções de Autoridade e Fechamento) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado nas objeções que ocorrem no momento crítico de fechamento — as mais delicadas de todas. Lida com: 'preciso consultar meu sócio/diretor/financeiro', 'não sou eu quem decide', 'preciso pensar', 'me manda uma proposta para eu analisar', 'vamos deixar para o mês que vem'. Estas objeções exigem técnica de fechamento, não apenas argumento. O CLOSER gera resposta que identifica se é uma objeção real (decisor não está na call) ou uma saída educada (prospect não convencido), e oferece ao vendedor o caminho certo: para objeção real de autoridade, como incluir o decisor; para 'preciso pensar', como descobrir o que realmente está impedindo. Especializado em técnicas de fechamento como assumptive close, summary close e urgency close aplicadas de forma consultiva.

## Input

- Texto da objeção classificada como authority_objection ou closing_stall, stage atual do funil (se está em proposta ou fechamento), histórico de interações do deal (quantas calls já houveram, objeções anteriores no mesmo deal), valor do deal

## Output

- Pacote de resposta com: (1) diagnóstico
- é objeção real de autoridade ou saída educada? (com indicadores), (2) resposta principal adaptada ao diagnóstico, (3) técnica de fechamento recomendada com script pronto, (4) pergunta de qualificação de decisor se aplicável ('quem mais estaria envolvido nessa decisão?'), (5) proposta de próximo passo concreto que mantém o momentum do deal

## Trigger

Disparo pelo MAESTRO quando objeção classificada como authority_objection, think_it_over, need_approval, proposal_request, ou closing_stall. SLA: < 8 segundos. Prioridade máxima — é o momento mais crítico do funil.

## Knowledge base (o que o executor consulta)

- Playbook de fechamento do cliente (técnicas aprovadas pela liderança de vendas), histórico de deals fechados e perdidos com análise do que funcionou no momento de fechamento, scripts de inclusão de decisor, templates de follow-up pós-call para deals em 'vou pensar', matriz de sinais de compra vs sinais de fuga para o diagnóstico automático

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto da objeção classificada como authority_objection ou closing_stall, stage atual do funil (se está em proposta ou f…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de resposta com: (1) diagnóstico) e persistir no artefato do squad.
4. Entregar ao critic ARGUS; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de resposta com: (1) diagnóstico
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

- **to:** ARQUIVO
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
