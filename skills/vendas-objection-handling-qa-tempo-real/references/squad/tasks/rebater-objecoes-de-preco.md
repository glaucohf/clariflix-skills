---
task: rebound()
responsavel: "REBOUND"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto da objeção classificada como price_objection ou value_objection, perfil do prospect (setor, tamanho, dor dominante, stage do funil), histórico de interações do deal no CRM, produto/plano sendo ofertado e preço"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Pacote de resposta com: (1) frase principal pronta para falar (max 2 linhas, linguagem conversacional), (2) 2-3 bullets de argumento com dado/numero especifico, (3) pergunta de redirecionamento para retomar controle, (4) flag de 'usar desconto?' com nivel de desconto autorizado se applicavel (L3 gate), (5) taxa de sucesso historica desta abordagem para este perfil"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo MAESTRO quando objeção classificada como price_objection, value_objection, roi_question, contract_terms, ou competitor_price_comparison. SLA: output em < 8 segundos."
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

# Rebater Objeções De Preço

**Task ID:** `rebound()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Rebater Objeções De Preço |
| **status** | `pending` |
| **responsible_executor** | REBOUND (REBOUND — O Rebatedor de Objeções de Preço e Valor) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em objeções de preço, custo, ROI e valor percebido — as mais frequentes e mais letais para o fechamento. Para cada objeção de preço recebida, recupera da base o frame correto (ROI, custo de não fazer, comparação com concorrente de preço similar, parcelamento/flexibilidade), personaliza com o perfil do prospect (setor, tamanho, dor dominante mapeada no CRM) e gera a resposta em três camadas: frase principal + argumento com número/dado + pergunta de redirecionamento. Especializado em objeções como: 'é muito caro', 'não temos orçamento agora', 'o concorrente cobra metade', 'preciso de desconto', 'qual o ROI?'. Também lida com objeções de contrato e modalidade de pagamento.

## Input

- Texto da objeção classificada como price_objection ou value_objection, perfil do prospect (setor, tamanho, dor dominante, stage do funil), histórico de interações do deal no CRM, produto/plano sendo ofertado e preço

## Output

- Pacote de resposta com: (1) frase principal pronta para falar (max 2 linhas, linguagem conversacional), (2) 2-3 bullets de argumento com dado/numero especifico, (3) pergunta de redirecionamento para retomar controle, (4) flag de 'usar desconto?' com nivel de desconto autorizado se applicavel (L3 gate), (5) taxa de sucesso historica desta abordagem para este perfil

## Trigger

Disparo pelo MAESTRO quando objeção classificada como price_objection, value_objection, roi_question, contract_terms, ou competitor_price_comparison. SLA: output em < 8 segundos.

## Knowledge base (o que o executor consulta)

- Base de battlecards de preço do cliente (construída nos encontros de diagnóstico e atualizada continuamente), histórico de win/loss com motivo 'preço' no CRM, casos de ROI documentados de clientes existentes, política de descontos e limites de autorização por nível de vendedor, tabela comparativa de preço vs concorrentes, calculadora de ROI parametrizada por setor

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto da objeção classificada como price_objection ou value_objection, perfil do prospect (setor, tamanho, dor dominant…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Pacote de resposta com: (1) frase principal pronta para falar (max 2 linhas, linguagem conversacional), (2) 2-3 bullets…) e persistir no artefato do squad.
4. Entregar ao critic ARGUS; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de resposta com: (1) frase principal pronta para falar (max 2 linhas, linguagem conversacional), (2) 2-3 bullets de argumento com dado/numero especifico…
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

- **to:** TEMPO
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
