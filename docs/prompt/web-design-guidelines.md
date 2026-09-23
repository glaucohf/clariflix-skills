# web-design-guidelines · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

---

---
name: web-design-guidelines
description: Revisa interfaces usando as diretrizes atualizadas de web da Vercel Use quando o pedido corresponder a web design guidelines.
version: 0.3.0
license: MIT
author: Vercel
---

# Interface pronta para revisão

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
MIT, conforme declarado no README da fonte Vercel Labs.
```


## Referência: SOURCE.md

# Proveniência

- Fonte: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines)
- Commit: `063bee94c3f4df8453406c830b0a7df0f2860278`
- Licença: `MIT`
- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/cohort-source-inventory.json`.


## Referência: references/cohort-source-inventory.json

```json
{
  "source_url": "https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines",
  "source_commit": "063bee94c3f4df8453406c830b0a7df0f2860278",
  "source_repository": "https://github.com/vercel-labs/agent-skills",
  "license": "MIT",
  "files": [
    {
      "path": "SKILL.md",
      "sha256": "17e48da905f83a19c174079b50760a98c069527ba50079239b3c187236627c29"
    }
  ]
}
```


## Referência: references/source/SKILL.md

---
name: web-design-guidelines
description: Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <file-or-pattern>
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.
