# rotina-follow-up · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: rotina-follow-up
description: "Monta a cadência de follow-up (ex.: 3-7-30 dias) para quem sumiu, com a mensagem certa por etapa, sem soar insistente. Use: \"monta o follow-up de clientes\", \"quem parou de comprar\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [follow-up, retencao, pme, rotina]
    related_skills: [rotina-agenda, atendimento-tom-de-voz]
---

# FOLLOW-UP · quem sumiu, quem volta

Monta a cadência de contato com quem parou de responder ou de voltar — com a mensagem certa em cada etapa, sem soar insistente — e produz a lista semanal de quem contatar e por quê.

## When to Use

- Diga: "monta o follow-up de [negócio]" ou "quem parou de comprar/agendar".
- Use quando o negócio já tem uma base de clientes e não tem processo definido para reengajar quem sumiu.
- NÃO use para o atendimento da primeira mensagem (`atendimento-triagem-whatsapp`) — aqui o contato já existe, só esfriou.

## Quick Reference

| procedimento | referência |
|---|---|
| cadência 3-7-30 | `references/cadencia.md` |

| apoio | arquivo |
|---|---|
| template da lista semanal | `templates/lista-followup.md` |

## Procedure

1. **Defina o gatilho de "sumiu"** para este negócio: quantos dias sem comprar/agendar/responder é o suficiente para entrar na cadência (varia por tipo de negócio — pergunte ao dono qual é o ciclo normal).
2. **Monte a cadência** (`references/cadencia.md`): 3 toques (ex.: 3, 7 e 30 dias após o gatilho), cada um com objetivo e tom diferentes — o primeiro é leve, o último já assume que a pessoa pode não voltar.
3. **Escreva a mensagem de cada etapa**, coerente com o guia de tom (`atendimento-tom-de-voz`, se existir) — nunca cobrando, sempre oferecendo algo de valor ou perguntando genuinamente.
4. **Defina a saída da cadência**: se a pessoa responder, sai da lista automática e vai para atendimento humano; se não responder após o último toque, marca como "inativo" e não recebe mais mensagens automáticas (para não incomodar).
5. **Gere a lista semanal** com quem está em cada etapa e o motivo (`templates/lista-followup.md`).

## Pitfalls

- Mandar a mesma mensagem genérica nas 3 etapas soa como spam — cada etapa precisa de tom e pedido diferentes.
- Não ter uma saída clara da cadência ("inativo") faz o negócio continuar mandando mensagem pra sempre, o que desgasta a marca.
- Confundir "sumiu" com "cliente satisfeito que só não precisa do serviço agora" — ajuste o gatilho ao ciclo real do negócio antes de disparar.

## Verification

Passou se: existem 3 mensagens diferentes (uma por etapa), nenhuma delas soa como cobrança; há uma regra clara de saída da cadência (respondeu → humano; não respondeu no fim → inativo); a lista semanal mostra nome, etapa e motivo para cada contato.


## Referência: references/cadencia.md

# Cadência 3-7-30 (ajuste os números ao ciclo do negócio)

1. **Dia 3** — leve, sem pedir nada: "Oi [nome], tudo bem? Notei que faz um tempinho — como você está?"
2. **Dia 7** — oferece valor: novidade, dica, ou lembrete de algo que a pessoa gostava.
3. **Dia 30** — último toque, tom de despedida gentil: "Não quero incomodar — se um dia quiser voltar, a porta está aberta. Um abraço!"

Depois do dia 30 sem resposta, marca como inativo e para de mandar mensagem automática.


## Referência: templates/lista-followup.md

# Follow-up da semana — [data]

| nome | último contato | dias sumido | etapa | ação |
|---|---|---|---|---|
