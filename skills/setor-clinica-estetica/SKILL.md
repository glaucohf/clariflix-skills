---
name: setor-clinica-estetica
description: "Combina triagem, agenda e follow-up com o vocabulário e os limites de uma clínica estética: sem diagnóstico, sem promessa de resultado. Use: \"monta o atendimento da minha clínica estética\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [setor, clinica-estetica, atendimento, pme]
    related_skills: [atendimento-triagem-whatsapp, rotina-agenda, rotina-follow-up]
---

# CLÍNICA ESTÉTICA · pacote de atendimento + agenda

Combina triagem, agenda e follow-up (as 3 skills genéricas) com o vocabulário e, principalmente, os **limites** de uma clínica estética: o agente nunca diagnostica, nunca promete resultado, e sempre direciona avaliação presencial para qualquer dúvida clínica.

## When to Use

- Diga: "monta o atendimento da minha clínica estética" ou "atendimento para clínica de estética/dermato".
- Use como pacote completo para esse setor específico, combinando o que `atendimento-triagem-whatsapp`, `rotina-agenda` e `rotina-follow-up` já cobrem, mais os limites clínicos abaixo.
- NÃO use isoladamente sem rodar antes as 3 skills genéricas — esta skill referencia o resultado delas, não as substitui.

## Quick Reference

| procedimento | referência |
|---|---|
| limites clínicos obrigatórios | `references/limites-clinicos.md` |
| vocabulário do setor | `references/vocabulario-setor.md` |

## Procedure

1. **Rode `atendimento-triagem-whatsapp`** normalmente, mas ao definir "Nunca dizer" (passo 4 daquela skill), inclua todos os itens de `references/limites-clinicos.md` — nenhum diagnóstico, nenhuma promessa de resultado, nenhuma indicação de procedimento sem avaliação presencial.
2. **Rode `rotina-agenda`**, mas trate toda primeira consulta como "avaliação" (não como o procedimento em si) — a saída "orçar" desta skill sempre aponta para avaliação presencial, nunca para preço fechado por WhatsApp de procedimento não avaliado.
3. **Rode `rotina-follow-up`** normalmente, mas o gatilho de handoff imediato inclui: qualquer menção a reação adversa, dor, ou insatisfação com resultado — sempre humano, nunca resposta automática.
4. **Ajuste o vocabulário** conforme `references/vocabulario-setor.md` (termos que a clínica usa e os que evita).
5. **Entregue o pacote combinado**: os 3 roteiros/regras das skills genéricas, com os limites clínicos aplicados em cada um.

## Pitfalls

- Deixar o agente sugerir qual procedimento é indicado para a pessoa é diagnóstico disfarçado — sempre encaminhar para avaliação presencial.
- Prometer resultado ("vai sumir a linha", "pele de bebê") gera expectativa que a clínica não controla e risco de reclamação.
- Responder dúvida sobre reação adversa ou dor por automação, mesmo que pareça simples — é sempre handoff imediato para humano.

## Verification

Passou se: nenhuma resposta do roteiro combinado sugere diagnóstico, indica procedimento específico ou promete resultado; toda primeira consulta é tratada como avaliação, não como venda fechada; menção a dor/reação adversa/insatisfação está mapeada como gatilho de handoff imediato nos 3 roteiros.
