---
task: arquivo()
responsavel: "ARQUIVO"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Log de cada interação de objection handling (objeção recebida, classificação, worker acionado, resposta entregue, ação do vendedor), resultado da call informado pelo vendedor (via formulário rápido pós-call ou atualização automática de stage no CRM), dados do deal no CRM"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Base de conhecimento atualizada com novas taxas de conversão por resposta, relatório semanal de padrões de objeção (top-5 objeções da semana, objeções em alta, respostas com queda de performance), alertas de novo concorrente ou nova objeção não catalogada, atualização de battlecards com dados de campo, sugestão de novas respostas para objeções frequentes com baixa taxa de conversão"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo automático após cada interação (log contínuo). Relatório consolidado gerado toda segunda-feira. Alerta imediato quando novo padrão de objeção não catalogada aparece 3+ vezes em 7 dias. L3 gat…"
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

# Analisar Objeções Frequentes

**Task ID:** `arquivo()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Analisar Objeções Frequentes |
| **status** | `pending` |
| **responsible_executor** | ARQUIVO (ARQUIVO — O Gestor de Inteligência e Aprendizado Contínuo) |
| **execution_type** | `Hybrid` |
| **input** | 1 item(ns) |
| **output** | 1 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de RevOps especializado em capturar, classificar e retroalimentar a base de conhecimento do squad. Após cada interação de objection handling, registra: qual objeção ocorreu, em qual stage, qual resposta foi entregue, se o vendedor usou a resposta (tracking de abertura/clique), e qual foi o resultado da call (deal avançou / parou / fechou / perdeu). Atualiza as taxas de sucesso de cada resposta na base. Detecta padrões: objeções que estão aumentando em frequência, respostas que pararam de converter, novos concorrentes sendo mencionados, dúvidas técnicas recorrentes que indicam gap no onboarding do produto. Alimenta o MAESTRO com insights de calibragem e alerta a liderança de vendas sobre padrões críticos.

## Input

- Log de cada interação de objection handling (objeção recebida, classificação, worker acionado, resposta entregue, ação do vendedor), resultado da call informado pelo vendedor (via formulário rápido pós-call ou atualização automática de stage no CRM), dados do deal no CRM

## Output

- Base de conhecimento atualizada com novas taxas de conversão por resposta, relatório semanal de padrões de objeção (top-5 objeções da semana, objeções em alta, respostas com queda de performance), alertas de novo concorrente ou nova objeção não catalogada, atualização de battlecards com dados de campo, sugestão de novas respostas para objeções frequentes com baixa taxa de conversão

## Trigger

Disparo automático após cada interação (log contínuo). Relatório consolidado gerado toda segunda-feira. Alerta imediato quando novo padrão de objeção não catalogada aparece 3+ vezes em 7 dias. L3 gate para qualquer escrita em CRM de produção.

## Knowledge base (o que o executor consulta)

- Banco de dados de todas as interações históricas do squad (objeção x resposta x resultado), CRM do cliente para leitura de resultados de deal (HubSpot/Pipedrive via MCP), base de battlecards e respostas (leitura e escrita), analytics de uso por vendedor (quem mais usa, quem mais converte com o squad), base de concorrentes para detecção de novos players

## Action Items

1. Confirmar o gatilho e carregar a entrada (Log de cada interação de objection handling (objeção recebida, classificação, worker acionado, resposta entregue, ação…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Base de conhecimento atualizada com novas taxas de conversão por resposta, relatório semanal de padrões de objeção (top…) e persistir no artefato do squad.
4. Entregar ao critic ARGUS; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Base de conhecimento atualizada com novas taxas de conversão por resposta, relatório semanal de padrões de objeção (top-5 objeções da semana, objeções em alta,…
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

- **to:** ARGUS
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
