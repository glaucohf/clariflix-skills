# decisao-proxima-acao · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: decisao-proxima-acao
description: "A partir de uma lista de possibilidades, escolhe uma ação, um dono e uma data para esta semana, usando impacto×esforço. Use: \"o que eu faço essa semana\", \"qual a próxima ação\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [decisao, priorizacao, pme, semana]
    related_skills: [decisao-diagnostico-pme]
---

# PRÓXIMA AÇÃO · o que fazer esta semana

Parte de uma lista de possibilidades (vinda de um diagnóstico ou apenas do que está na cabeça da pessoa) e sai com uma ação, um dono e uma data para esta semana — nunca uma lista de boas intenções.

## When to Use

- Diga: "o que eu faço essa semana" ou "qual a próxima ação, com tanta coisa pra fazer".
- Use depois de um diagnóstico (`decisao-diagnostico-pme`) ou sempre que houver mais opções do que tempo.
- NÃO use para o diagnóstico em si (esta skill parte de uma lista já existente).

## Quick Reference

| procedimento | referência |
|---|---|
| matriz impacto × esforço | `references/impacto-esforco.md` |
| gate de informação faltante | `references/gate-informacao.md` |

| apoio | arquivo |
|---|---|
| template da decisão da semana | `templates/proxima-acao.md` |

## Procedure

1. **Liste as possibilidades** em aberto (do diagnóstico, ou perguntando: "o que está pendente na sua cabeça agora?").
2. **Posicione cada uma na matriz impacto × esforço** (`references/impacto-esforco.md`) — sem número exato, só relativo entre as opções.
3. **Verifique o gate de informação** (`references/gate-informacao.md`): se a ação de maior impacto depende de uma informação que ainda falta, a ação desta semana é conseguir essa informação, não a ação final.
4. **Escolha uma única ação** — não três, uma — de alto impacto e o menor esforço possível dentro do que tem impacto real.
5. **Defina o dono e a data**: sempre uma pessoa nomeada e um dia da semana, nunca "eu vejo isso" sem prazo.
6. **Entregue** no formato `templates/proxima-acao.md`.

## Pitfalls

- Escolher a ação mais fácil em vez da de maior impacto só porque é mais confortável de começar.
- Escolher uma ação de alto impacto que na verdade depende de informação que ainda não existe — vira trabalho parado no meio.
- Sair com mais de uma ação "prioritária" é o mesmo que sair sem nenhuma.

## Verification

Passou se: existe exatamente 1 ação escolhida (não uma lista); ela tem 1 dono nomeado e 1 data; se dependia de informação faltante, o gate foi verificado e a ação escolhida reflete isso (buscar a informação, não pular direto para a decisão final).


## Referência: references/gate-informacao.md

# Gate de informação faltante

Antes de fechar a ação da semana, pergunte: "eu tenho toda a informação para executar isso até o fim, ou vou travar no meio esperando alguém/algo?"

Se a resposta for "vou travar", a ação desta semana muda: em vez da ação final, a ação é conseguir a informação que falta (uma pergunta, um dado, uma aprovação) — e a ação final vira a próxima semana.


## Referência: references/impacto-esforco.md

# Matriz impacto × esforço

Para cada possibilidade, pergunte:
- **Impacto**: se isso funcionar, quanto muda de verdade? (alto/médio/baixo, relativo às outras opções)
- **Esforço**: quanto tempo/dinheiro/coordenação exige até dar o primeiro resultado visível?

Prioridade: alto impacto + baixo esforço primeiro. Alto impacto + alto esforço entra na lista, mas não é "desta semana" a menos que já esteja em andamento. Baixo impacto, seja qual for o esforço, sai da lista.


## Referência: templates/proxima-acao.md

# Próxima ação — semana de [data]

**Ação escolhida:** [1 frase]
**Por quê (impacto × esforço):** [1 frase]
**Dono:** [nome] · **Data:** [dia da semana]
**Depende de informação faltante?** [não / sim — qual, e como conseguir]
