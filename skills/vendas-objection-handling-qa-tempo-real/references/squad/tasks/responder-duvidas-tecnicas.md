---
task: tecnico()
responsavel: "TECNICO"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Texto da dúvida classificada como product_qa, integration_question, ou implementation_question, cargo e perfil técnico do interlocutor (executivo vs técnico), produto/módulo específico em discussão"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Resposta técnica em três camadas: (1) resposta direta em linguagem do interlocutor (executivo ou técnico), (2) detalhamento técnico opcional (o vendedor expõe se necessário), (3) próximo passo sugerido se a resposta exigir validação interna (ex: 'posso te conectar com nosso técnico para uma call de 20 minutos sobre a integração com o SAP?')"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Flag de HITL se a resposta envolve promessa de prazo, SLA customizado, ou integração não documentada"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo MAESTRO quando input classificado como product_qa, integration_question, implementation_question, technical_spec, ou security_compliance. SLA: < 10 segundos para perguntas catalogadas; H…"
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

# Responder Dúvidas Técnicas

**Task ID:** `tecnico()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Responder Dúvidas Técnicas |
| **status** | `pending` |
| **responsible_executor** | TECNICO (TÉCNICO — O Especialista em Q&A de Produto e Integração) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em dúvidas técnicas de produto, integração, implementação e suporte — o tipo de pergunta que trava closers sem background técnico. Responde: 'isso integra com o nosso ERP?', 'quanto tempo leva para implementar?', 'o que acontece se o sistema cair?', 'vocês tem SLA?', 'precisa de IT para configurar?', 'funciona em mobile?', 'como é a migração dos nossos dados?'. Para cada dúvida, recupera a resposta técnica verificada da base de conhecimento de produto, adapta o nível de linguagem ao perfil do interlocutor (técnico = detalhe; executivo = impacto de negócio) e sinaliza quando a dúvida exige validação com a equipe técnica do cliente antes de responder (HITL gate para promessas técnicas).

## Input

- Texto da dúvida classificada como product_qa, integration_question, ou implementation_question, cargo e perfil técnico do interlocutor (executivo vs técnico), produto/módulo específico em discussão

## Output

- Resposta técnica em três camadas: (1) resposta direta em linguagem do interlocutor (executivo ou técnico), (2) detalhamento técnico opcional (o vendedor expõe se necessário), (3) próximo passo sugerido se a resposta exigir validação interna (ex: 'posso te conectar com nosso técnico para uma call de 20 minutos sobre a integração com o SAP?')
- Flag de HITL se a resposta envolve promessa de prazo, SLA customizado, ou integração não documentada

## Trigger

Disparo pelo MAESTRO quando input classificado como product_qa, integration_question, implementation_question, technical_spec, ou security_compliance. SLA: < 10 segundos para perguntas catalogadas; HITL gate acionado se promessa técnica não documentada.

## Knowledge base (o que o executor consulta)

- Base de conhecimento tecnico do produto do cliente (documentacao, FAQs internas, integradores homologados, SLAs padrao, roadmap compartilhavel), historico de perguntas tecnicas respondidas em calls anteriores (extraido via conversation intelligence), casos de implementacao documentados com prazo real, matriz de integracao por sistema (ERP, CRM, e-commerce, etc.), respostas pre-aprovadas para perguntas de seguranca e compliance

## Action Items

1. Confirmar o gatilho e carregar a entrada (Texto da dúvida classificada como product_qa, integration_question, ou implementation_question, cargo e perfil técnico…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Resposta técnica em três camadas: (1) resposta direta em linguagem do interlocutor (executivo ou técnico), (2) detalham…) e persistir no artefato do squad.
4. Entregar ao critic ARGUS; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Resposta técnica em três camadas: (1) resposta direta em linguagem do interlocutor (executivo ou técnico), (2) detalhamento técnico opcional (o vendedor expõe…
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

- **to:** CLOSER
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
