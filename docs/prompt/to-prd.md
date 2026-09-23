# to-prd · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: to-prd
description: Transforma o contexto da conversa em um PRD com escopo e decisões Use quando o pedido corresponder a to prd.
version: 0.3.0
license: MIT
author: Matt Pocock
---

# Conversa em PRD

Esta é uma adaptação de catálogo. As instruções originais e seus arquivos de apoio estão preservados em [references/source/](references/source/).

## When to Use

Use quando a necessidade corresponder ao propósito descrito pela skill de origem. Leia primeiro [references/source/SKILL.md](references/source/SKILL.md) e qualquer referência que ela indicar.

## Quick Reference

Forneça o contexto necessário, siga o fluxo da fonte e mantenha revisões humanas antes de ações externas, configurações ou publicação.

## Procedure

1. Leia as instruções de origem e identifique entradas, entregáveis e limites.
2. Reúna apenas o contexto necessário e execute o fluxo com as ferramentas disponíveis.
3. Apresente o resultado para revisão antes de qualquer ação externa ou irreversível.

## Pitfalls

Não invente acesso a serviços, não exponha credenciais e não trate recomendações da fonte como resultados garantidos.

## Verification

Confirme que o resultado usa as entradas fornecidas, respeita os limites da fonte e deixa explícitos os próximos passos que dependem de revisão humana.


## Referência: LICENSE.source

```text
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


## Referência: SOURCE.md

# Proveniência

- Fonte: [mattpocock/skills](https://github.com/mattpocock/skills/blob/62f43a18177be6ec82da242e59ffbc490a4c22ea/skills/engineering/to-prd/SKILL.md)
- Commit: `62f43a18177be6ec82da242e59ffbc490a4c22ea`
- Licença: `MIT`
- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/cohort-source-inventory.json`.


## Referência: references/cohort-source-inventory.json

```json
{
  "source_url": "https://github.com/mattpocock/skills/blob/62f43a18177be6ec82da242e59ffbc490a4c22ea/skills/engineering/to-prd/SKILL.md",
  "source_commit": "62f43a18177be6ec82da242e59ffbc490a4c22ea",
  "source_repository": "https://github.com/mattpocock/skills",
  "license": "MIT",
  "files": [
    {
      "path": "SKILL.md",
      "sha256": "ce3e32c38f1c9cbb9012ea99e26524a73e19df813c10accb5a8e246d24d8166d"
    }
  ]
}
```


## Referência: references/source/SKILL.md

---
name: to-prd
description: Turn the current conversation context into a PRD and submit it as a GitHub issue. Use when user wants to create a PRD from the current context.
---

This skill takes the current conversation context and codebase understanding and produces a PRD. Do NOT interview the user — just synthesize what you already know.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already.
2. Sketch the modules to build or modify, look for deep modules, and check expectations and tests with the user.
3. Write a PRD with problem statement, solution, user stories, implementation decisions, testing decisions, out of scope, and further notes. Submit it as a GitHub issue.
