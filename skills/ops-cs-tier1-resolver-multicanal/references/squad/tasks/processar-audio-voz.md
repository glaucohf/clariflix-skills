---
task: vox()
responsavel: "Vox"
responsavel_type: Agente
atomic_layer: Atom
Entrada:
  - nome: entrada1
    tipo: object
    obrigatorio: true
    descricao: "Arquivo de áudio (OGG/MP3/WAV) do WhatsApp ou stream de voz do Aircall + ID do cliente + canal de origem"
Saida:
  - nome: saida1
    tipo: object
    obrigatorio: true
    descricao: "Texto transcrito normalizado para o Orchestrator + (na resposta) áudio sintetizado TTS em PT-BR"
  - nome: saida2
    tipo: object
    obrigatorio: false
    descricao: "Log de qualidade de transcrição (confiança ASR) no Langfuse"
Checklist:
  pre-conditions:
    - "[ ] Gatilho ocorreu: Webhook do WhatsApp Business API detecta mensagem de tipo 'áudio'; webhook do Aircall detecta chamada entrante"
    - "[ ] Entrada principal disponível e conferida contra a fonte (CRM/sistema de origem)"
  post-conditions:
    - "[ ] Saída produzida no formato especificado e persistida no artefato do squad"
    - "[ ] Saída submetida ao critic Argus antes de qualquer entrega externa"
  veto-conditions:
    - "[ ] HITL: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário"
    - "[ ] HITL: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo"
    - "[ ] HITL: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados"
    - "[ ] HITL: Terceira interação na mesma sessão sem resolução confirmada pelo cliente"
    - "[ ] HITL: Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação"
---

# Processar Audio Voz

**Task ID:** `vox()` · **Pattern:** HO-TP-001 (Task Anatomy Standard) · **Squad:** Squad de Suporte Conversacional Multicanal (Tier-1 Resolver)

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Processar Audio Voz |
| **status** | `pending` |
| **responsible_executor** | Vox (Vox — Agente de Voz & Áudio) |
| **execution_type** | `Agent` |
| **input** | 1 item(ns) |
| **output** | 2 item(ns) |
| **action_items** | 4 passos |
| **acceptance_criteria** | 6 critérios |

## Overview (papel do executor, literal da especificação)

Processa áudio recebido via WhatsApp (voice notes) e chamadas telefônicas: transcreve com ASR PT-BR, normaliza o texto, extrai intenção e envia para o Orchestrator Nexus como se fosse texto. Na saída, sintetiza respostas em áudio TTS PT-BR para canais de voz. Garante tratamento nativo de sotaques, gírias e ruído de fundo.

## Input

- Arquivo de áudio (OGG/MP3/WAV) do WhatsApp ou stream de voz do Aircall + ID do cliente + canal de origem

## Output

- Texto transcrito normalizado para o Orchestrator + (na resposta) áudio sintetizado TTS em PT-BR
- Log de qualidade de transcrição (confiança ASR) no Langfuse

## Trigger

Webhook do WhatsApp Business API detecta mensagem de tipo 'áudio'; webhook do Aircall detecta chamada entrante

## Knowledge base (o que o executor consulta)

- Modelos ASR PT-BR (Deepgram Nova-2 ou Whisper Large-v3), vocabulário de domínio customizado (nomes de produtos, SKUs, termos da empresa), mapeamento de intenções verbais para intenções textuais equivalentes, parâmetros TTS por canal (velocidade, voz, tom)

## Action Items

1. Confirmar o gatilho e carregar a entrada (Arquivo de áudio (OGG/MP3/WAV) do WhatsApp ou stream de voz do Aircall + ID do cliente + canal de origem).
2. Executar o papel descrito no Overview consultando a knowledge base; não inventar dado que não esteja na entrada ou na base.
3. Produzir a saída no formato especificado (Texto transcrito normalizado para o Orchestrator + (na resposta) áudio sintetizado TTS em PT-BR) e persistir no artefato do squad.
4. Entregar ao critic Argus; se houver condição de veto, parar e escalar ao gate humano.

## Acceptance Criteria

- [ ] Saída no formato especificado: Texto transcrito normalizado para o Orchestrator + (na resposta) áudio sintetizado TTS em PT-BR
- [ ] Toda afirmação da saída rastreável à entrada ou à knowledge base
- [ ] Veredito do critic Argus registrado
- [ ] Gate HITL respeitado: Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário
- [ ] Gate HITL respeitado: Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo
- [ ] Gate HITL respeitado: Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados

## Veto Conditions

| ID | Condição | Resultado |
|----|----------|-----------|
| VETO-001 | HITL — Refund acima de R$500 ou qualquer caso de chargeback/contestação bancária – Flux eleva para L3 e Hermes cria ticket prioritário | BLOQUEIA até decisão humana |
| VETO-002 | HITL — Confiança do classificador de intenção < 0.72 – Nexus não roteia, Hermes escala com contexto completo | BLOQUEIA até decisão humana |
| VETO-003 | HITL — Crític Argus retorna score total < 30 ou flag de risco jurídico, LGPD ou segurança de dados | BLOQUEIA até decisão humana |
| VETO-004 | HITL — Terceira interação na mesma sessão sem resolução confirmada pelo cliente | BLOQUEIA até decisão humana |
| VETO-005 | HITL — Cliente em tier VIP, Enterprise ou com MRR > R$5k – toda ação irreversível requer aprovação | BLOQUEIA até decisão humana |
| VETO-006 | HITL — Menção de palavras-chave de risco: 'advogado', 'PROCON', 'Reclame Aqui', 'processo', 'imprensa', 'TV' | BLOQUEIA até decisão humana |
| VETO-007 | HITL — Solicitacao de troca/devolucao fora do prazo de politica ou em categoria inelegivel — Volta escalona para decisao humana com contexto | BLOQUEIA até decisão humana |
| VETO-008 | HITL — Health score do cliente cai abaixo de 45 durante a interação — Pulse dispara alerta para CSM responsável | BLOQUEIA até decisão humana |
| VETO-009 | HITL — Áudio com qualidade ASR < 0.80 de confiança — Vox marca para revisão humana antes de processar | BLOQUEIA até decisão humana |
| VETO-010 | Saída sem veredito do critic Argus | BLOQUEIA entrega |

## Handoff

- **to:** Hermes
- **trigger:** saída aprovada pelo critic e sem condição de veto pendente

_Gerado em 2026-09-16. Entrada, saída, gatilho, base de conhecimento e gates copiados da especificação; passos e critérios seguem regra fixa._
