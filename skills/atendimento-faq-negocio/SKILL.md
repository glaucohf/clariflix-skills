---
name: atendimento-faq-negocio
description: "Extrai as perguntas reais do histórico de atendimento e monta uma base de FAQ versionada, com dono por resposta. Use: \"monta a FAQ do meu negócio\", \"organiza as perguntas que já respondi\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [atendimento, faq, pme]
    related_skills: [atendimento-triagem-whatsapp, atendimento-tom-de-voz]
---

# FAQ VIVO · monta e mantém a base de respostas

Extrai as perguntas que os clientes realmente fazem (a partir do histórico de conversas ou da memória de quem atende) e monta uma base de FAQ com resposta única, versionada e com dono — não uma lista genérica copiada da internet.

## When to Use

- Diga: "monta a FAQ do meu negócio" ou "organiza as perguntas que eu já respondi mil vezes".
- Use quando já existe algum histórico de conversas (WhatsApp, e-mail) ou quando quem atende consegue listar de memória.
- NÃO use para escrever o roteiro de qualificação (`atendimento-triagem-whatsapp`) nem para definir o tom das respostas (`atendimento-tom-de-voz`, que se aplica depois de a FAQ existir).

## Quick Reference

| procedimento | referência |
|---|---|
| como agrupar perguntas parecidas | `references/agrupamento.md` |

| apoio | arquivo |
|---|---|
| template da base de FAQ | `templates/faq.md` |

## Procedure

1. **Colete as perguntas reais**: peça o histórico de conversas dos últimos 1-3 meses, ou peça a quem atende para listar as 15-20 perguntas mais comuns de memória.
2. **Agrupe por intenção**, não por palavra: perguntas com redação diferente mas mesma intenção viram uma linha só (`references/agrupamento.md`).
3. **Escreva uma resposta única e final** para cada grupo — a versão que o dono aprova, não a que "às vezes" é dada.
4. **Marque o dono de cada resposta**: quem decide se ela muda (preço, prazo, política) — para saber quem procurar quando a realidade mudar.
5. **Versione**: cada resposta leva a data da última confirmação; revise a cada 3 meses ou quando algo mudar (preço, endereço, horário).
6. **Entregue** no formato `templates/faq.md`, pronto para virar `references/` de uma skill de atendimento.

## Pitfalls

- Copiar perguntas "genéricas do setor" em vez de partir do histórico real perde o que os clientes desse negócio específico realmente perguntam.
- FAQ sem dono da resposta fica desatualizada sem ninguém perceber.
- Duas respostas diferentes para a mesma pergunta (uma no WhatsApp, outra no Instagram) é sintoma de que a FAQ não é a fonte única — só existe uma resposta certa por pergunta.

## Verification

Passou se: toda pergunta do histórico amostrado está coberta por algum grupo; cada resposta tem exatamente um dono nomeado e a data da última confirmação; não há duas respostas diferentes para a mesma intenção.
