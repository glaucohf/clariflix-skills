---
name: sop-extrair
description: "Entrevista quem faz o processo hoje e reconstrói o procedimento: gatilho, passos, exceções, dono. Use: \"extrai o processo de\", \"não tem nada escrito\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [processos, sop, entrevista, pme]
    related_skills: [sop-criar, sop-auditar]
---

# DA CABEÇA PRO PAPEL · entrevista quem faz, reconstrói o processo

Entrevista a pessoa que executa um processo hoje (mesmo que "de cabeça", sem nada escrito) e reconstrói o procedimento completo: gatilho, passos, decisões, exceções, ferramentas, dono. Usa Análise de Tarefa Cognitiva (CTA) para puxar as decisões implícitas que quem faz o processo não pensa em contar.

## When to Use

- Diga: "extrai o processo de [tarefa]" com a pessoa que faz disponível para responder perguntas.
- Use quando o processo só existe na cabeça de alguém (o dono, um funcionário-chave) e nunca foi escrito.
- NÃO use para escrever a versão final formatada (`sop-criar`, que recebe a saída desta) nem para auditar um SOP já existente (`sop-auditar`).

## Quick Reference

| procedimento | referência |
|---|---|
| roteiro de entrevista CTA | `references/roteiro-cta.md` |
| os 5 porquês para achar exceção | `references/cinco-porques.md` |

| apoio | arquivo |
|---|---|
| template de saída | `templates/processo-bruto.md` |

## Procedure

1. **Pergunte o gatilho**: "o que precisa acontecer para você começar essa tarefa?" — se a resposta for vaga ("quando aparece"), insista até virar um evento concreto (um pedido chega, um horário bate, um cliente liga).
2. **Peça os passos na ordem real**, não na ordem ideal: "me conta o que você faz, do primeiro ao último passo, como você realmente faz — não como deveria ser." Anote verbos de ação, não intenções.
3. **Aplique CTA nas decisões**: sempre que a pessoa disser "eu vejo se dá" ou "depende", pare e pergunte: "depende de quê, exatamente? O que você olha para decidir?" — siga `references/roteiro-cta.md`. É aqui que mora o conhecimento tácito que o processo escrito costuma perder.
4. **Cace exceções com os 5 porquês** (`references/cinco-porques.md`): pergunte "isso sempre acontece assim?" e, a cada exceção mencionada, pergunte "por quê" mais uma vez até chegar na causa, não no sintoma.
5. **Confirme ferramentas e dono**: liste cada sistema/planilha/app usado em cada passo, e quem é o responsável por cada decisão (nem sempre é quem executa).
6. **Devolva um resumo** no formato `templates/processo-bruto.md` e peça confirmação da pessoa antes de considerar pronto: "ficou assim — bateu com o que você faz?"

## Pitfalls

- Aceitar "depende" sem perguntar do quê é a forma mais comum de perder a regra de decisão real.
- Entrevistar só o dono do negócio, sem falar com quem executa no dia a dia, gera um processo idealizado que ninguém segue.
- Pular a confirmação final: a pessoa que faz o processo é quem valida se o que foi escrito bate com a realidade.

## Verification

Passou se: o processo tem gatilho concreto (não vago), toda decisão citada como "depende" tem o critério explícito, pelo menos 1 exceção foi documentada com sua causa (não só o sintoma), cada passo tem ferramenta e dono nomeados, e a pessoa entrevistada confirmou que o resumo bate com o que ela faz.
