---
name: sop-criar
description: "Escreve o procedimento 2x: versão para pessoa (com checklist) e versão para agente (YAML com estados e decisões). Use: \"escreve o SOP de\", \"versão para agente deste processo\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [processos, sop, documentacao, pme]
    related_skills: [sop-extrair, sop-auditar]
---

# POR ESCRITO · SOP para pessoa, SOP para agente, checklist

Escreve o procedimento duas vezes, de propósito: uma versão para pessoa, clara e curta o bastante para ser seguida sem dúvida, e uma versão para agente, em YAML, com estados e decisões explícitas. Do SOP sai também o checklist operacional do dia a dia.

## When to Use

- Diga: "escreve o SOP de [processo]" ou "versão para agente deste SOP".
- Use depois de ter o processo levantado (com `sop-extrair`, ou já sabido de cabeça e confirmado).
- NÃO use para extrair o processo da cabeça de alguém (`sop-extrair`) nem para auditar um SOP existente (`sop-auditar`).

## Quick Reference

| procedimento | referência |
|---|---|
| padrão do SOP para pessoa | `references/padrao-sop-humano.md` |
| padrão do SOP para agente (YAML) | `references/padrao-sop-agente.md` |

| apoio | arquivo |
|---|---|
| template SOP humano | `templates/sop-humano.md` |
| template SOP agente | `templates/sop-agente.yaml` |
| template checklist | `templates/checklist.md` |

## Procedure

1. **Confira a entrada**: se vier de `sop-extrair`, use o `processo-bruto.md` como fonte; se não, pergunte gatilho, passos, decisões, exceções, ferramentas e dono antes de escrever qualquer coisa.
2. **Escreva o SOP para pessoa** seguindo `references/padrao-sop-humano.md`: título, objetivo em 1 frase, quando se aplica, passos numerados curtos (verbo no imperativo), o que fazer em cada exceção, e quem chamar quando o critério não cobrir o caso.
3. **Escreva o SOP para agente** seguindo `references/padrao-sop-agente.md`: mesma lógica em YAML — `states`, `transitions`, `decisions` com o critério de cada uma, e `tools` usadas em cada estado. É o formato que um agente de IA consegue seguir sem ambiguidade.
4. **Extraia o checklist**: cada passo do SOP humano vira um item de checklist verificável (feito/não feito), na ordem de execução — não na ordem de escrita.
5. **Confira equivalência**: releia as duas versões lado a lado — todo passo do humano tem um estado correspondente no agente, e toda decisão do agente tem o mesmo critério do humano. Se não bater, corrija antes de entregar.

## Pitfalls

- SOP humano longo demais não é seguido; corte para o que realmente muda o resultado.
- YAML do agente sem critério explícito em cada decisão obriga o agente a "adivinhar" — sempre escreva a condição (`if valor > X`), nunca só o nome da decisão.
- Checklist que reordena os passos "para ficar bonito" confunde quem executa; a ordem é sempre a de execução real.

## Verification

Passou se: as duas versões (humana e agente) cobrem exatamente os mesmos passos e decisões; toda decisão no YAML tem `criterio` explícito; o checklist tem um item por passo, na ordem de execução; e existe uma linha de "quando chamar humano" tanto na versão humana quanto na de agente.
