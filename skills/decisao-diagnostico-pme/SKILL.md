---
name: decisao-diagnostico-pme
description: "Mapeia tarefas repetitivas, estima horas/mês e custo de oportunidade, e aponta os 3 processos onde IA devolve tempo primeiro. Use: \"onde eu começo com IA\", \"diagnóstico do negócio\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [decisao, diagnostico, pme, priorizacao]
    related_skills: [decisao-proxima-acao, sop-extrair]
---

# DIAGNÓSTICO · onde a IA devolve tempo primeiro

Mapeia as tarefas repetitivas do dono ou da equipe de uma PME, estima quanto tempo cada uma consome por mês e aponta, com números, os 3 processos onde vale automatizar primeiro — pela regra 80/20, não por preferência ou modismo.

## When to Use

- Diga: "faz o diagnóstico de [negócio]" ou "onde eu começo a usar IA no meu negócio".
- Use no início de qualquer projeto de automação — antes de escolher qual skill ou ferramenta implementar.
- NÃO use para decidir a próxima ação de uma semana específica (`decisao-proxima-acao`, que parte deste diagnóstico) nem para escrever o processo em si (`sop-extrair`).

## Quick Reference

| procedimento | referência |
|---|---|
| mapa de tarefas repetitivas | `references/mapa-de-tarefas.md` |
| cálculo de custo de oportunidade | `references/custo-de-oportunidade.md` |

| apoio | arquivo |
|---|---|
| template do diagnóstico | `templates/diagnostico.md` |

## Procedure

1. **Liste as tarefas da semana** com a pessoa: peça para descrever um dia típico e uma semana típica, sem julgar o que é "importante" — só o que ela realmente faz, seguindo `references/mapa-de-tarefas.md`.
2. **Marque o que é repetitivo**: toda tarefa que se repete de forma parecida mais de 1x por semana entra na lista de candidatas.
3. **Estime horas/mês** de cada uma (frequência × duração média). Não precisa de precisão — precisão de +-20% já basta para priorizar.
4. **Calcule o custo de oportunidade** de cada tarefa (`references/custo-de-oportunidade.md`): horas/mês × o que essa pessoa poderia estar fazendo em vez disso (vender, atender, criar) — não o salário-hora contábil.
5. **Aplique 80/20**: ordene por custo de oportunidade e pegue as 3 do topo. Se duas tarefas tiverem custo parecido, prefira a que tem regra mais simples de automatizar (menos exceções).
6. **Entregue o diagnóstico** no formato `templates/diagnostico.md`: top-3 processos, horas/mês de cada, e uma frase do porquê aquele é o primeiro.

## Pitfalls

- Confundir "tarefa que incomoda" com "tarefa que consome mais tempo" — o diagnóstico é sobre horas e custo de oportunidade, não sobre irritação.
- Priorizar a tarefa mais fácil de automatizar em vez da que mais custa — às vezes vale começar pela 2ª mais cara, se a 1ª tiver exceções demais.
- Fechar o diagnóstico sem confirmar os números com a pessoa: ela precisa reconhecer a própria semana no resultado.

## Verification

Passou se: existem pelo menos 5 tarefas mapeadas antes de cortar para 3; cada uma das top-3 tem horas/mês e custo de oportunidade estimados (não só "parece muito tempo"); e a pessoa confirmou que o top-3 bate com a percepção dela do que mais consome o dia.
