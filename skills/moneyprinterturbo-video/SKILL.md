---
name: moneyprinterturbo-video
description: Gera vídeos curtos a partir de tema ou roteiro usando o fluxo MoneyPrinterTurbo. Use quando o resultado esperado for um arquivo de vídeo final.
version: 0.5.0
license: MIT
author: Harry
---

# Vídeo que vira entrega

As instruções oficiais e o helper da fonte estão preservados em [references/source/](references/source/).

## When to Use

Use para criar um vídeo final a partir de tema, título, ideia ou roteiro. Leia [references/source/SKILL.md](references/source/SKILL.md) antes de iniciar para verificar sistema operacional, dependências e provedores necessários.

## Quick Reference

O fluxo requer terminal, rede, armazenamento local, `uv` e pode solicitar credenciais de provedores de IA ou de mídia. Use os parâmetros de tema, roteiro, formato e voz fornecidos pelo usuário.

## Procedure

1. Confirme os pré-requisitos e identifique credenciais ausentes sem exibi-las em saídas ou logs.
2. Execute o helper oficial conforme a fonte, com um único trabalho por vez.
3. Informe o caminho do vídeo resultante e o resumo das escolhas usadas.

## Pitfalls

Não exponha chaves de API, não inicie serviços desnecessários e não execute opções que geram cobranças sem confirmação explícita do usuário. Respeite licenças de mídia, direitos de imagem e políticas da plataforma de destino.

## Verification

Confirme que o arquivo final existe, que o formato e o conteúdo correspondem ao pedido e que qualquer custo ou publicação externa recebeu autorização específica.
