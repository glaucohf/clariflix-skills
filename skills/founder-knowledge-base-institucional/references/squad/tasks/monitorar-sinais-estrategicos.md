---
task: radar()
responsavel: "RADAR"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Lista de concorrentes monitorados, palavras-chave estratégicas, domínios de interesse (mercados, tecnologias, regulações), configuração de frequência de varredura, grafo de conhecimento (para contextualização dos sinais)"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Alertas de inteligência contextualizados com: sinal bruto (fonte, data, link), classificação (CONFIRMAÇÃO / AMEAÇA / OPORTUNIDADE / NEUTRO), conexão ao grafo (quais nós são afetados e como), perspectiva histórica do founder sobre o tópico (citação do grafo com data), nível de urgência (IMEDIATO / ESTA SEMANA / PRÓXIMO MÊS), e sugestão de ação ou resposta estratégica"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Entregues via Slack com digest diário e alertas imediatos para sinais de alta urgência"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Execução contínua em background (cron a cada 4h para varredura geral, real-time para menções diretas). Alertas imediatos disparados quando: concorrente anuncia funding, mudança regulatória relevante,…"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic AUDITOR antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] L3: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automaticamente — pausa e apresenta ao founder os dois claims com contexto (data, situacao) para ele determinar qual e a posicao atual e por que evoluiu. Irreversivel porque altera permanentemente o grafo canônico."
    - "[ ] L3: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída para fora da empresa exige leitura e aprovação explícita do founder. O clone fala pela empresa — erro de representação e irreversível reputacionalmente."
    - "[ ] L3: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com anotações de contexto por seção para facilitar a revisão, mas o envio nunca é automático."
    - "[ ] L2: Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para reunião'. O founder decide o que fazer com o sinal, não o squad."
    - "[ ] L2: Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao ha ingestao forçada — o founder controla o ritmo de captura do proprio conhecimento."
---

# Monitorar Sinais Estratégicos

**Task ID:** `radar()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Monitorar Sinais Estratégicos |
| **status** | `pending` |
| **responsible_executor** | RADAR (RADAR — O Monitor de Inteligência Estratégica) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker de monitoramento contínuo que conecta sinais externos ao grafo interno. Opera 24/7 varrendo: movimentos de concorrentes (funding, lançamentos, contratações estratégicas, mudanças de pricing), sinais de mercado (notícias do setor, mudanças regulatórias, tendências emergentes), e menções públicas do founder e da empresa. Para cada sinal detectado, o Radar não apenas reporta o evento — ele CONECTA o sinal aos nós relevantes do grafo e responde: 'Dado o que o founder disse sobre X em [data], esse sinal é uma confirmação / ameaça / oportunidade'. Gera alertas contextualizados que poupam ao founder o trabalho de lembrar o contexto histórico de cada tópico.

## Input

- Lista de concorrentes monitorados, palavras-chave estratégicas, domínios de interesse (mercados, tecnologias, regulações), configuração de frequência de varredura, grafo de conhecimento (para contextualização dos sinais)

## Output

- Alertas de inteligência contextualizados com: sinal bruto (fonte, data, link), classificação (CONFIRMAÇÃO / AMEAÇA / OPORTUNIDADE / NEUTRO), conexão ao grafo (quais nós são afetados e como), perspectiva histórica do founder sobre o tópico (citação do grafo com data), nível de urgência (IMEDIATO / ESTA SEMANA / PRÓXIMO MÊS), e sugestão de ação ou resposta estratégica
- Entregues via Slack com digest diário e alertas imediatos para sinais de alta urgência

## Trigger

Execução contínua em background (cron a cada 4h para varredura geral, real-time para menções diretas). Alertas imediatos disparados quando: concorrente anuncia funding, mudança regulatória relevante, menção da empresa em veículo de alto alcance. Relatório consolidado semanal gerado todo domingo para revisão do founder na segunda-feira.

## Knowledge base (o que o executor consulta)

- Grafo de conhecimento (para contextualização)
- Lista de concorrentes e entidades monitoradas (atualizada pelo ORION)
- APIs de monitoramento: Google Alerts, EXA Web Search, LinkedIn Company Monitor
- Histórico de alertas anteriores (para evitar repetição e identificar padrões)
- Criterios de priorização definidos pelo founder no Discovery (o que é crítico vs ruido)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Lista de concorrentes monitorados, palavras-chave estratégicas, domínios de interesse (mercados, tecnologias, regulaçõe…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Alertas de inteligência contextualizados com: sinal bruto (fonte, data, link), classificação (CONFIRMAÇÃO / AMEAÇA / OP…) e persistir no artefato do squad.
4. Entregar ao critic AUDITOR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Alertas de inteligência contextualizados com: sinal bruto (fonte, data, link), classificação (CONFIRMAÇÃO / AMEAÇA / OPORTUNIDADE / NEUTRO), conexão ao grafo (…
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic AUDITOR registrado
- [ ] Gate L3 respeitado: Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o graf…
- [ ] Gate L3 respeitado: Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, m…
- [ ] Gate L3 respeitado: Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scriv…

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | L3 — Validacao de contradicoes detectadas pelo Cartographer: quando dois chunks do corpus apresentam claims opostos sobre o mesmo topico, o grafo nao decide automat… | BLOQUEIA até decisão humana |
| VETO-002 | L3 — Aprovação antes de qualquer output do Persona Forge ser compartilhado externamente (clientes, investidores, parceiros): uso interno e L2, mas qualquer saída pa… | BLOQUEIA até decisão humana |
| VETO-003 | L3 — Envio de memo finalizado pelo Scrivener para audiência externa (board, investidores): o founder le e assina o draft antes do envio. O Scrivener entrega com ano… | BLOQUEIA até decisão humana |
| VETO-004 | L2 — Classificação de urgência pelo Radar: alertas IMEDIATOS chegam ao founder diretamente via Slack com opção de 'Delegar ao Wargame', 'Arquivar' ou 'Escalar para… | BLOQUEIA até decisão humana |
| VETO-005 | L2 — Sessoes de captura de conhecimento agendadas pelo SCRIBE: o founder confirma disponibilidade e agenda antes de qualquer sessao de entrevista estruturada. Nao h… | BLOQUEIA até decisão humana |
| VETO-006 | L1 — Revisão do mapa de lacunas gerado no Discovery: antes de priorizar quais tópicos capturar, o founder valida se a taxonomia e as lacunas identificadas fazem sen… | BLOQUEIA até decisão humana |
| VETO-007 | Saída sem veredito do critic AUDITOR | BLOQUEIA entrega |

## Handoff

- **to:** CHIEF OF STAFF
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
