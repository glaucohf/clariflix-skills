---
name: conferencia-planilha
description: "Bate uma planilha contra uma regra (tabela, contrato, orçamento) e lista cada divergência com linha e valor. Use: \"confere esta planilha\", \"bate os números com a tabela\"."
version: 0.1.0
author: "Claricia · Glauco Ferreira"
license: MIT
platforms: [linux, macos, windows]
required_environment_variables: []
metadata:
  hermes:
    tags: [conferencia, planilha, financeiro, pme]
    related_skills: [conferencia-orcamento]
---

# CONFERÊNCIA · bate planilha contra regra

Confere uma planilha (valores, quantidades, datas) contra uma regra de referência — tabela de preço, contrato, orçamento aprovado — e lista toda divergência encontrada, com linha e valor exato. Não aprova nada; aponta.

## When to Use

- Diga: "confere esta planilha contra [a tabela/o contrato/o orçamento]".
- Use sempre que houver uma fonte de verdade (tabela, contrato) e uma planilha que deveria bater com ela.
- NÃO use para montar uma proposta do zero (`conferencia-orcamento`) — aqui já existem os dois lados a comparar.

## Quick Reference

| procedimento | referência |
|---|---|
| como definir tolerância aceitável | `references/tolerancia.md` |

| apoio | arquivo |
|---|---|
| template do relatório de divergência | `templates/relatorio-divergencia.md` |

## Procedure

1. **Confirme a fonte de verdade**: qual tabela/contrato/orçamento é a regra — nunca assuma, pergunte se não estiver explícito.
2. **Alinhe as chaves**: identifique a coluna que liga cada linha da planilha à linha correspondente na regra (código do item, nome, data) — sem isso, a comparação não é confiável.
3. **Compare linha a linha**: valor, quantidade, data — o que diverge da regra.
4. **Aplique a tolerância** definida com quem pediu a conferência (`references/tolerancia.md`) — diferenças de centavo por arredondamento não são o mesmo tipo de erro que um valor 10x maior.
5. **Liste cada divergência** com a linha exata, o valor esperado, o valor encontrado e a diferença — sem resumir ("algumas linhas divergem") e sem arredondar o problema.
6. **Nunca aprove por conta própria**: entregue o relatório para quem decide; a skill aponta, não decide se está "aceitável".

## Pitfalls

- Comparar por posição da linha em vez de por chave (código/nome) gera falso positivo/negativo quando a ordem muda.
- Aplicar tolerância grande demais para "não incomodar" esconde erro real.
- Resumir divergências em vez de listar cada uma faz quem recebe não confiar no relatório.

## Verification

Passou se: toda linha da planilha foi comparada contra a regra usando uma chave explícita; cada divergência tem linha, valor esperado, valor encontrado e diferença; nenhuma divergência foi omitida por parecer pequena, exceto as dentro da tolerância acordada (que aparecem à parte, não escondidas).
