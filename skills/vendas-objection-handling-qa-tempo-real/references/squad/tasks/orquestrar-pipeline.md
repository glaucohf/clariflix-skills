---
task: maestroPipeline()
responsavel: "MAESTRO"
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
    descricao: "Pacote de Resposta de Objeção"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "entregue em < 15 segundos ao vendedor em qualquer canal ativo (widget de call, WhatsApp, chat do CRM): (1) Resposta Principal pronta para falar ou copiar/colar (max 2 linhas, linguagem conversacional do canal), (2) Argumento de Suporte com 2-3 bullets de dado/caso/lógica para aprofundar, (3) Pergunta de Redirecionamento para retomar controle da conversa após a resposta"
  - nome: saida3
    tipo: object
    obrigatorio: false
    descricao: "Artefato verificável registrado no ClickUp por deal com: objeção recebida, worker acionado, resposta entregue, resultado da call"
  - nome: saida4
    tipo: object
    obrigatorio: false
    descricao: "Relatório semanal de inteligência de objeções entregue à liderança de vendas via Slack/email: top objeções da semana, taxas de conversão por tipo, novos padrões detectados, sugestões de atualização de playbook"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Orquestrador central do squad de objection handling. Recebe o sinal bruto (texto da objecao, transcricao de call ou duvida tecnica), classifica o tipo e urgencia, injeta contexto do prospect via CRM,…"
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

# Orquestrar Pipeline do Objection Handling e Q&A em Tempo Real

**Task ID:** `maestroPipeline()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Objection Handling e Q&A em Tempo Real

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Orquestrar Pipeline do Objection Handling e Q&A em Tempo Real |
| **status** | `pending` |
| **responsible_executor** | MAESTRO (MAESTRO — O Regente Comercial) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 4 item(ns) |
| **action_items** | 5 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Orquestrador central do squad de objection handling. Recebe o sinal bruto (texto da objecao, transcricao de call ou duvida tecnica), classifica o tipo e urgencia, injeta contexto do prospect via CRM, roteia para o worker especializado correto com os parametros certos, coordena o retorno em multicamadas (resposta + suporte + redirecionamento), aciona o ARGUS para verificacao pre-entrega e despacha o output ao vendedor dentro do SLA de < 15 segundos. Mantem o estado da sessao de vendas — se o mesmo deal gerou 3 objecoes na mesma call, MAESTRO tem contexto acumulado e evita respostas repetitivas ou contraditórias. Nao executa nenhuma resposta diretamente — seu trabalho e garantir que a resposta certa chegue na hora certa.

## Input

- Sinal ou evento de entrada do squad (webhook, evento de CRM, cron) e estado atual do pipeline

## Output

- Pacote de Resposta de Objeção
- entregue em < 15 segundos ao vendedor em qualquer canal ativo (widget de call, WhatsApp, chat do CRM): (1) Resposta Principal pronta para falar ou copiar/colar (max 2 linhas, linguagem conversacional do canal), (2) Argumento de Suporte com 2-3 bullets de dado/caso/lógica para aprofundar, (3) Pergunta de Redirecionamento para retomar controle da conversa após a resposta
- Artefato verificável registrado no ClickUp por deal com: objeção recebida, worker acionado, resposta entregue, resultado da call
- Relatório semanal de inteligência de objeções entregue à liderança de vendas via Slack/email: top objeções da semana, taxas de conversão por tipo, novos padrões detectados, sugestões de atualização de playbook

## Trigger

Orquestrador central do squad de objection handling. Recebe o sinal bruto (texto da objecao, transcricao de call ou duvida tecnica), classifica o tipo e urgencia, injeta contexto do prospect via CRM, roteia para o worker especializado correto com os parametros certos, coordena o retorno em multicamadas (resposta + suporte + redirecionamento), aciona o ARGUS para verificacao pre-entrega e despacha o output ao vendedor dentro do SLA de < 15 segundos. Mantem o estado da sessao de vendas — se o mesmo deal gerou 3 objecoes na mesma call, MAESTRO tem contexto acumulado e evita respostas repetitivas ou contraditórias. Nao executa nenhuma resposta diretamente — seu trabalho e garantir que a resposta certa chegue na hora certa.

## Knowledge base (o que o executor consulta)

- CRM: HubSpot (MCP disponível) ou Pipedrive
- leitura de contexto do deal e prospect em tempo real pelo MAESTRO
- escrita de resultados e atualização de battlecards pelo ARQUIVO (L3 gate)
- WhatsApp Business API (Gupshup, AiSensy, ou QuickReply.ai)
- canal primário de acionamento do squad por SDRs e closers no Brasil
- entrega de resposta como mensagem rápida copiável
- Interface de call em tempo real: integração com Vapi ou Retell AI para captura de transcrição ao vivo
- widget de overlay na tela do vendedor durante a call com resposta em < 15 segundos
- STT em tempo real: Deepgram para transcrição da fala do prospect durante calls, alimentando o MAESTRO com o texto da objeção antes mesmo do vendedor digitar
- Conversation Intelligence: Gong ou Chorus
- analise pos-call para identificar objecoes que ocorreram e se foram superadas
- dados alimentam ARQUIVO para aprendizado continuo
- ClickUp: registro de cada interação de objection handling como tarefa/artefato verificável com resultado
- prova de trabalho do squad por deal
- Slack: notificações de HITL para supervisores (aprovação de desconto, nova objeção detectada)
- relatório semanal de padrões de objeção para liderança de vendas
- Base vetorial: Supabase pgvector ou Pinecone
- armazenamento e busca semântica da base de battlecards, respostas históricas e casos de uso para recuperação em < 3 segundos
- Observabilidade: Langfuse (OTEL)
- rastreamento de latência por worker, taxa de aprovação do ARGUS, taxa de uso pelo vendedor (resposta entregue vs resposta efetivamente usada), quality gates dev 70% / staging 85% / prod 95%
- Orquestração: LangGraph ou Claude Agent SDK
- controle de estado por sessão de call, paralelismo dos workers de recuperação (battlecard + contexto), retry logic com fallback para resposta genérica se SLA estourar

## Action Items

1. Receber o sinal de entrada e decompor em subtarefas na ordem do workflow.
2. Acionar cada worker na sequência definida e manter o estado do pipeline.
3. Submeter cada saída ao critic ARGUS antes de avançar.
4. Parar e escalar ao humano em toda condição de gate L3; notificar nos gates L2/L1.
5. Consolidar o entregável do squad e registrar KPIs.

## Acceptance Criteria

- [ ] Saída no formato especificado: Pacote de Resposta de Objeção
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

- **to:** REBOUND
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
