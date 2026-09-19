# atendimento-tom-de-voz · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: atendimento-tom-de-voz
description: "Escreve o guia de tom (traços + exemplos do que falar e não falar) e testa com 10 casos-limite antes de ir ao ar. Use: \"define o tom do meu atendimento\", \"guia de voz\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [atendimento, tom-de-voz, marca, pme]
    related_skills: [atendimento-triagem-whatsapp, atendimento-faq-negocio]
---

# VOZ DA EMPRESA · guia de tom para o agente

Escreve o guia de tom de voz que o agente de atendimento deve seguir — 3 a 5 traços concretos, exemplos do que falar e do que nunca falar — e testa com 10 casos-limite antes de colocar no ar.

## When to Use

- Diga: "define o tom do atendimento de [negócio]" ou "guia de voz da marca".
- Use depois que a triagem (`atendimento-triagem-whatsapp`) e a FAQ (`atendimento-faq-negocio`) já existem, para garantir que soam como o mesmo negócio.
- NÃO use para escrever o roteiro em si (isso é `atendimento-triagem-whatsapp`) — esta skill define como soa, não o que decide.

## Quick Reference

| procedimento | referência |
|---|---|
| matriz de tom (traço × exemplo) | `references/matriz-de-tom.md` |

| apoio | arquivo |
|---|---|
| template do guia | `templates/guia-de-voz.md` |

## Procedure

1. **Levante 3-5 traços concretos** perguntando ao dono: "se seu atendimento fosse uma pessoa, como ela seria em 3 palavras?" — recuse traços vagos ("profissional", "atencioso") sem um exemplo que os diferencie de qualquer outro negócio.
2. **Para cada traço, escreva um exemplo real** de frase que o agente diria e uma que NÃO diria, usando `references/matriz-de-tom.md`.
3. **Liste o que nunca fazer**: gírias específicas, emojis (quantos, quais), abreviações, formalidade excessiva — o que soaria errado para esse público.
4. **Escreva 10 casos-limite** de teste: uma reclamação, um pedido fora do escopo, um cliente grosseiro, uma dúvida repetida — e a resposta ideal em cada, seguindo o tom definido.
5. **Rode os 10 casos** com o agente configurado e compare com a resposta ideal; ajuste o guia (não o caso) até as respostas baterem.
6. **Entregue** o guia no formato `templates/guia-de-voz.md`.

## Pitfalls

- Traços genéricos ("profissional", "simpático") sem exemplo concreto não mudam o comportamento do agente — todo negócio já diz isso.
- Pular o teste dos 10 casos-limite: é ali que o tom quebra, não nas conversas fáceis.
- Confundir tom de voz com conteúdo: esta skill não decide o que responder (isso é a FAQ/triagem), só como soa.

## Verification

Passou se: existem 3-5 traços, cada um com pelo menos 1 exemplo do que falar e 1 do que não falar; os 10 casos-limite foram testados e as respostas do agente batem com o guia; a lista de "nunca fazer" tem pelo menos 3 itens específicos do negócio (não genéricos).


## Referência: references/matriz-de-tom.md

# Matriz de tom — traço, exemplo do que falar, exemplo do que não falar

| traço | diz | não diz |
|---|---|---|
| [ex.: direto, sem enrolação] | "Fechado! Confirmo para terça 14h." | "Poderíamos, quem sabe, considerar talvez marcar para terça?" |
| [ex.: caloroso mas objetivo] | "Que bom te ver por aqui de novo! Vamos agendar?" | "Prezado(a), informamos que..." |

Regra: se o exemplo de "diz" também servisse para o concorrente sem mudar nada, o traço ainda está genérico demais.


## Referência: templates/guia-de-voz.md

# Guia de voz — [nome do negócio]

## Traços (3-5)
1. **[traço]** — diz: "[exemplo]" · não diz: "[exemplo]"

## Nunca fazer
- [gíria/emoji/abreviação a evitar]

## Casos-limite testados
| caso | resposta ideal | resposta do agente | bateu? |
|---|---|---|---|
| [reclamação] | | | |
