#!/usr/bin/env python3
"""Importa a skill oficial do MoneyPrinterTurbo com proveniência."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / ".verification" / "money-printer-turbo-20260923"
SLUG = "moneyprinterturbo-video"
SOURCE_DIR = SOURCE_ROOT / "docs" / "skill"


def inventory(path: Path) -> list[dict[str, str]]:
    return [
        {"path": str(file.relative_to(path)).replace("\\", "/"), "sha256": hashlib.sha256(file.read_bytes()).hexdigest()}
        for file in sorted(path.rglob("*"))
        if file.is_file()
    ]


def main() -> None:
    target = ROOT / "skills" / SLUG
    if target.exists():
        raise RuntimeError(f"Destino já existe: {target}")
    commit = subprocess.check_output(["git", "-C", str(SOURCE_ROOT), "rev-parse", "HEAD"], text=True).strip()
    target_source = target / "references" / "source"
    shutil.copytree(SOURCE_DIR, target_source)
    shutil.copy2(SOURCE_ROOT / "LICENSE", target / "LICENSE.source")
    (target / "SKILL.md").write_text('''---
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
''', encoding="utf-8")
    (target / "manifest.yaml").write_text('''row: marketing
title: Vídeo que vira entrega
title_netflix: MONEYPRINTER TURBO
subtitle: Gera vídeos curtos a partir de tema ou roteiro com script, voz, mídia e legendas
genre: procedural
badge: Nova
runtime_only: true
painel:
  ano: 2026
  tamanho: 2 arquivos de origem
  requer: Terminal, uv, rede e credenciais dos provedores escolhidos
  como_usar: 'Instale a skill, forneça o tema ou roteiro e revise custos e direitos de mídia'
  elenco: [Tema, Roteiro, Voz, Mídia]
  generos: [Vídeo, Marketing, Automação]
  esta_skill_e: [Rastreável, Estruturada, Revisável]
''', encoding="utf-8")
    metadata = {
        "source_url": f"https://github.com/harry0703/MoneyPrinterTurbo/tree/{commit}/docs/skill",
        "source_repository": "https://github.com/harry0703/MoneyPrinterTurbo",
        "source_commit": commit,
        "license": "MIT",
        "files": inventory(target_source),
    }
    (target / "references" / "moneyprinterturbo-source-inventory.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (target / "SOURCE.md").write_text(
        f"# Proveniência\n\n- Fonte: [harry0703/MoneyPrinterTurbo]({metadata['source_url']})\n- Commit: `{commit}`\n- Licença: MIT, preservada em `LICENSE.source`.\n- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/moneyprinterturbo-source-inventory.json`.\n",
        encoding="utf-8",
    )
    print("Importada moneyprinterturbo-video.")


if __name__ == "__main__":
    main()
