---
task: argusVerificar()
responsavel: "ARGUS"
responsavel_type: Agente
atomic_layer: Molecule
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Veredito (aprovado / reprovado com feedback específico) registrado no validation_log"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Toda saída de worker que antecede entrega externa ou ação irreversível."
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
  veto-conditions:
    - "[ ] L3: Qualquer resposta que envolva promessa de desconto acima do nível autorizado para o vendedor: MAESTRO pausa, notifica supervisor ou gerente de vendas via Slack/WhatsApp, que aprova ou rejeita em tempo real antes da resposta chegar ao vendedor"
    - "[ ] L3: Qualquer resposta a dúvida técnica que envolva prazo de implementação customizado, SLA não padrão, ou integração não documentada na base: TÉCNICO flag como HITL, vendedor recebe instrução 'vou confirmar com a equipe técnica e te retorno em X horas' em vez de uma promessa não verificada"
    - "[ ] L3: Escrita de resultados de call e atualização de stage no CRM pelo ARQUIVO: vendedor confirma o resultado via formulário rápido (1 click) antes de qualquer persistência em CRM de produção"
    - "[ ] L2: Quando ARGUS emite REJEITADO por factualidade: MAESTRO notifica o vendedor que a resposta está sendo verificada e entrega uma resposta genérica segura enquanto o worker corrige — o vendedor decide se usa a genérica ou aguarda a corrigida"
    - "[ ] L1: Objecão nova não catalogada (aparece pela primeira vez): ARQUIVO sinaliza ao líder de vendas ou product owner que uma nova objecão foi detectada e sugere draft de resposta para validação antes de entrar na base — o líder aprova, edita ou rejeita o draft"
---

# Verificar Saídas do Objection Handling e Q&A em Tempo Real

**Task ID:** `argusVerificar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Verificar Saídas do Objection Handling e Q&A em Tempo Real |
| **status** | `pending` |
| **responsible_executor** | ARGUS (ARGUS — O Verificador de Factualidade e Tom) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

ARGUS — O Verificador de Factualidade e Tom — Critic/Verifier que audita cada resposta gerada pelos workers antes da entrega ao vendedor. Verifica em < 2 segundos (para manter o SLA de tempo real): (1) Factualidade — a resposta contém dado específico (preço, prazo, ROI, feature de produto)? Se sim, o dado está na base de conhecimento verificada ou é inferência? Dados não verificados são substituídos por linguagem qualitativa ou flaggados com 'confirmar antes de usar'; (2) Tom — a resposta ataca o concorrente diretamente? Faz promessa que a empresa não pode cumprir? Usa linguagem agressiva ou desesperada que denota pressão de fechamento? (3) Completude — a resposta tem as três camadas (resposta principal + argumento + pergunta de redirecionamento)? (4) Adequação ao canal — resposta para call tem max 2 linhas? Resposta para WhatsApp está bem formatada? Emite veredicto APROVADO / APROVADO COM RESSALVA (entrega com nota ao vendedor) / REJEITADO (re-roteia para worker com instrução de correção específica).

## Input

- Artefatos produzidos pelos workers do squad, antes de qualquer entrega externa

## Output

- Veredito (aprovado / reprovado com feedback específico) registrado no validation_log

## Trigger

Toda saída de worker que antecede entrega externa ou ação irreversível.

## Knowledge base (o que o executor consulta)

- O Verificador de Factualidade e Tom
- Critic/Verifier que audita cada resposta gerada pelos workers antes da entrega ao vendedor
- Verifica em < 2 segundos (para manter o SLA de tempo real): (1) Factualidade
- a resposta contém dado específico (preço, prazo, ROI, feature de produto)? Se sim, o dado está na base de conhecimento verificada ou é inferência? Dados não verificados são substituídos por linguagem qualitativa ou flaggados com 'confirmar antes de usar'
- a resposta ataca o concorrente diretamente? Faz promessa que a empresa não pode cumprir? Usa linguagem agressiva ou desesperada que denota pressão de fechamento? (3) Completude
- a resposta tem as três camadas (resposta principal + argumento + pergunta de redirecionamento)? (4) Adequação ao canal
- resposta para call tem max 2 linhas? Resposta para WhatsApp está bem formatada? Emite veredicto APROVADO / APROVADO COM RESSALVA (entrega com nota ao vendedor) / REJEITADO (re-roteia para worker com instrução de correção específica)

## Action Items

1. Receber o artefato do worker e identificar qual gate se aplica.
2. Aplicar o checklist do critic (ver `checklists/`) item a item, com evidência.
3. Reprovar com feedback específico quando qualquer item falhar; nunca aprovar tacitamente.
4. Aprovar registrando o veredito no validation_log.
5. Devolver ao orquestrador MAESTRO para a próxima fase ou para o gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Veredito (aprovado / reprovado com feedback específico) registrado no validation_log
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito registrado com evidência por item do checklist
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

- **to:** MAESTRO
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
