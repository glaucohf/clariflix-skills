---
name: atendimento-triagem-whatsapp
description: "Responde a 1ª mensagem no WhatsApp, qualifica em 3 perguntas e encaminha para 1 de 4 saídas fixas (agendar, orçar, humano, encerrar). Use: \"monta o atendimento do WhatsApp\", \"triagem de lead\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [atendimento, whatsapp, pme, triagem]
    related_skills: [atendimento-tom-de-voz, rotina-agenda, decisao-proxima-acao]
---

# TRIAGEM · responde, qualifica e encaminha no WhatsApp

Escreve o roteiro de triagem da primeira conversa no WhatsApp do negócio: recebe a mensagem, faz no máximo 3 perguntas de qualificação e termina sempre em uma de 4 saídas fixas. Não inventa preço, não promete prazo, não substitui o humano quando o caso pede humano.

## When to Use

- Diga: "monta o atendimento do WhatsApp de [negócio]" ou "escreve a triagem para [tipo de negócio]".
- Use quando o negócio já sabe quem atende (clínica, escola, agência, comércio) mas ainda não tem um roteiro escrito.
- NÃO use para follow-up de quem já é cliente (`rotina-follow-up`) nem para montar a base de FAQ (`atendimento-faq-negocio`).

## Quick Reference

| procedimento | referência |
|---|---|
| árvore de intenção | `references/arvore-de-intencao.md` |
| as 4 saídas fixas | `references/saidas-fixas.md` |

| apoio | arquivo |
|---|---|
| template do roteiro | `templates/roteiro-triagem.md` |

## Procedure

1. **Levante o essencial** perguntando à pessoa (não ao agente): tipo de negócio, o que se agenda/vende, quem faz o atendimento humano hoje, horário de funcionamento, e o que NUNCA deve ser respondido automaticamente (preço fechado, diagnóstico, prazo legal). Se faltar algo, pergunte antes de escrever — não invente.
2. **Desenhe a árvore de intenção** com no máximo 3 perguntas de qualificação, seguindo `references/arvore-de-intencao.md`: (a) o que a pessoa quer, (b) urgência/quando, (c) já é cliente ou é novo contato.
3. **Escreva o roteiro** no formato de `templates/roteiro-triagem.md`: mensagem de abertura, as perguntas na ordem certa, e a regra de corte para cada uma das 4 saídas de `references/saidas-fixas.md` (agendar · orçar · encaminhar para humano · encerrar educadamente).
4. **Marque os limites** explicitamente no roteiro: liste as 3–5 frases que o agente NUNCA deve dizer (preço fora da tabela, prazo médico, promessa de resultado) e o gatilho de handoff imediato para humano (reclamação, urgência médica, pedido de cancelamento).
5. **Entregue** o roteiro pronto para colar na configuração do agente (Hermes, WhatsApp Business API, ou o bot que o negócio já usa).

## Pitfalls

- Mais de 3 perguntas antes de qualificar cansa a pessoa e derruba a taxa de resposta — corte, não acrescente.
- Roteiro sem gatilho de handoff vira reclamação pública quando o caso foge do script.
- Prometer preço ou prazo que a tabela do negócio não confirma gera atrito depois — deixe a saída "orçar" sempre humana ou baseada em tabela fixa fornecida pelo dono.

## Verification

Passou se: toda mensagem simulada de entrada termina em exatamente uma das 4 saídas fixas; nenhuma pergunta de qualificação passa de 3; o roteiro lista pelo menos 1 gatilho de handoff imediato; nenhuma frase do roteiro promete preço, prazo ou resultado não confirmado pelo dono do negócio.
