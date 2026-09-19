---
task: scribe()
responsavel: "SCRIBE"
responsavel_type: Worker
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Arquivos de áudio/vídeo (MP3, MP4, WAV), transcrições brutas, exports de Slack/email, documentos (PDF, DOCX, Notion), agenda de entrevistas com o founder, mapa de lacunas do Discovery"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "JSON de chunks semânticos com: claim, contexto, fonte (URL ou referência), data, interlocutores, tópicos (array), entidades (array), nível de confiança, flag de verificação pendente"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Volume esperado: 50-200 chunks por sessão de ingestão"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Disparo pelo ORION após upload de nova fonte pelo founder ou equipe. Também acionado automaticamente quando nova transcrição é detectada em integração com Sembly/Fireflies/Notion. Sessões de entrevis…"
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

# Transformar Conhecimento Tacito

**Task ID:** `scribe()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad Knowledge Base Institucional do Founder

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Transformar Conhecimento Tacito |
| **status** | `pending` |
| **responsible_executor** | SCRIBE (SCRIBE — O Ingestor de Conhecimento Tácito) |
| **execution_type** | `Worker` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Worker especializado em transformar conhecimento não estruturado em dados estruturados para o grafo. Processa todas as fontes: transcreve áudio e vídeo (reuniões, podcasts, palestras), parseia threads de Slack e emails exportados, chunka documentos em segmentos semânticos, e conduz entrevistas estruturadas de captura de conhecimento com o founder usando perguntas derivadas das lacunas mapeadas no Discovery. Para cada chunk, extrai: claim principal, contexto (quando foi dito, para quem, em qual situação), nível de confiança (alta / média / especulativa), tópicos relacionados e entidades mencionadas. Gera JSON estruturado com metadados completos de proveniência.

## Input

- Arquivos de áudio/vídeo (MP3, MP4, WAV), transcrições brutas, exports de Slack/email, documentos (PDF, DOCX, Notion), agenda de entrevistas com o founder, mapa de lacunas do Discovery

## Output

- JSON de chunks semânticos com: claim, contexto, fonte (URL ou referência), data, interlocutores, tópicos (array), entidades (array), nível de confiança, flag de verificação pendente
- Volume esperado: 50-200 chunks por sessão de ingestão

## Trigger

Disparo pelo ORION após upload de nova fonte pelo founder ou equipe. Também acionado automaticamente quando nova transcrição é detectada em integração com Sembly/Fireflies/Notion. Sessões de entrevista agendadas pelo ORION com base nas lacunas prioritárias do grafo.

## Knowledge base (o que o executor consulta)

- Taxonomia de tópicos críticos definida no Discovery (hierarquia de 4 níveis)
- Histórico de chunks já processados para evitar duplicatas
- Templates de entrevista por domínio (estratégia, produto, mercado, cultura, financeiro)
- Integrações: Sembly API (transcrições), Notion MCP (documentos), Google Drive (exports), Slack export

## Action Items

1. Confirmar o gatilho e carregar a entrada (Arquivos de áudio/vídeo (MP3, MP4, WAV), transcrições brutas, exports de Slack/email, documentos (PDF, DOCX, Notion), a…).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (JSON de chunks semânticos com: claim, contexto, fonte (URL ou referência), data, interlocutores, tópicos (array), entid…) e persistir no artefato do squad.
4. Entregar ao critic AUDITOR; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: JSON de chunks semânticos com: claim, contexto, fonte (URL ou referência), data, interlocutores, tópicos (array), entidades (array), nível de confiança, flag d…
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

- **to:** CARTOGRAPHER
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
