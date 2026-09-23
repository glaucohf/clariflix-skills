#!/usr/bin/env python3
"""Importa skills de ativação do AIOX Embaixador com proveniência."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / ".verification" / "aiox-embaixador-pro-20260923"
REPOSITORY = "https://github.com/aiox-embaixadores/aiox-embaixador-pro"

SKILLS = [
    ("design-chief", "operacoes", "Orquestração de design", "DESIGN CHIEF", "Organiza a triagem, o roteamento e a sequência de trabalho de design", "Objetivo de design e contexto do projeto", ["Triagem", "Roteamento", "Sequência"], ["Design", "Operações", "Orquestração"]),
    ("design-md", "operacoes", "Design de uma URL", "DESIGN MD", "Extrai um contrato de design e tokens de uma URL pública", "URL pública e objetivo da análise", ["Tokens", "Componentes", "Contrato"], ["Design", "UI", "Auditoria"]),
    ("research-bench", "gestao", "Benchmark com evidências", "RESEARCH BENCH", "Compara produtos, empresas ou tecnologias com métricas e lacunas", "Dois assuntos e critérios de comparação", ["Matriz", "Pontuação", "Lacunas"], ["Pesquisa", "Estratégia", "Benchmark"]),
    ("research-chief", "gestao", "Pesquisa bem roteada", "RESEARCH CHIEF", "Orquestra pesquisa técnica, competitiva e de marketing", "Pergunta, contexto e profundidade desejada", ["Escopo", "Fontes", "Síntese"], ["Pesquisa", "Estratégia", "Inteligência"]),
    ("research-marketing-deepdive", "marketing", "Marketing em profundidade", "MARKETING DEEPDIVE", "Investiga players, tendências, conteúdo e oportunidades de mercado", "Mercado, player ou tema de pesquisa", ["Players", "Tendências", "Oportunidades"], ["Marketing", "Pesquisa", "Conteúdo"]),
    ("slide-creator", "marketing", "Apresentações que contam", "SLIDE CREATOR", "Cria decks com narrativa, direção visual, roteiro e critérios de qualidade", "Briefing, audiência e objetivo do deck", ["Narrativa", "Slides", "Qualidade"], ["Apresentações", "Storytelling", "Design"]),
    ("sop-chief", "sop", "SOP que roda", "SOP CHIEF", "Cria, extrai, analisa e audita procedimentos operacionais", "Processo, evidências e público executor", ["Processo", "Critérios", "Melhoria"], ["SOP", "Operações", "Qualidade"]),
    ("tech-research", "gestao", "Pesquisa técnica profunda", "TECH RESEARCH", "Conduz pesquisa técnica com cobertura, referências e registro de aprendizado", "Pergunta técnica e profundidade desejada", ["Cobertura", "Fontes", "Dossiê"], ["Pesquisa", "Tecnologia", "Decisão"]),
]


def inventory(path: Path) -> list[dict[str, str]]:
    return [
        {"path": str(file.relative_to(path)).replace("\\", "/"), "sha256": hashlib.sha256(file.read_bytes()).hexdigest()}
        for file in sorted(path.rglob("*"))
        if file.is_file()
    ]


def wrapper(slug: str, subtitle: str, title: str) -> str:
    return f'''---
name: {slug}
description: {subtitle} Use quando o pedido corresponder a {slug.replace('-', ' ')}.
version: 0.4.0
license: Authorized redistribution
author: AIOX Embaixadores
---

# {title}

As instruções originais e seus suportes estão preservados em [references/source/](references/source/).

## When to Use

Use quando a necessidade corresponder à skill de origem. Leia [references/source/SKILL.md](references/source/SKILL.md) antes de iniciar; algumas skills requerem AIOX Core e a squad indicada pela própria fonte.

## Quick Reference

Forneça o contexto solicitado pela fonte e mantenha as dependências externas, integrações e ações de publicação sob revisão humana.

## Procedure

1. Leia a fonte para identificar entradas, dependências e entregáveis.
2. Reúna o contexto mínimo e siga o fluxo documentado pela skill.
3. Apresente o resultado para revisão antes de ações externas ou irreversíveis.

## Pitfalls

Não presuma que AIOX Core, squads, integrações ou credenciais estão disponíveis. Não execute comandos da fonte sem verificar os pré-requisitos locais.

## Verification

Confirme que as dependências necessárias estão instaladas, as entradas foram usadas e os limites e próximos passos ficaram claros.
'''


def main() -> None:
    commit = subprocess.check_output(["git", "-C", str(SOURCE_ROOT), "rev-parse", "HEAD"], text=True).strip()
    for slug, row, title, netflix, subtitle, requires, cast, genres in SKILLS:
        target = ROOT / "skills" / slug
        if target.exists():
            raise RuntimeError(f"Destino já existe: {target}")
        source = SOURCE_ROOT / "skills" / slug
        target_source = target / "references" / "source"
        shutil.copytree(source, target_source)
        (target / "LICENSE.source").write_text(
            "A fonte não declara licença pública. O mantenedor do ClariFlix confirmou autorização dos autores para republicação em 2026-09-23.\n",
            encoding="utf-8",
        )
        (target / "SKILL.md").write_text(wrapper(slug, subtitle, title), encoding="utf-8")
        (target / "manifest.yaml").write_text("\n".join([
            f"row: {row}", f"title: {title}", f"title_netflix: {netflix}", f"subtitle: {subtitle}",
            "genre: procedural", "badge: Nova", "runtime_only: true", "painel:", "  ano: 2026",
            f"  tamanho: {len(inventory(target_source))} arquivo(s) de origem",
            f"  requer: {requires}", "  como_usar: 'Instale a skill e siga os pré-requisitos declarados pela fonte'",
            f"  elenco: [{', '.join(cast)}]", f"  generos: [{', '.join(genres)}]",
            "  esta_skill_e: [Rastreável, Estruturada, Revisável]", ""
        ]), encoding="utf-8")
        metadata = {"source_url": f"{REPOSITORY}/tree/{commit}/skills/{slug}", "source_repository": REPOSITORY, "source_commit": commit, "license": "Authorized redistribution", "files": inventory(target_source)}
        (target / "references" / "aiox-source-inventory.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (target / "SOURCE.md").write_text(
            f"# Proveniência\n\n- Fonte: [{REPOSITORY}]({metadata['source_url']})\n- Commit: `{commit}`\n- Licença: não declarada publicamente; autorização de redistribuição confirmada pelo mantenedor do ClariFlix em 2026-09-23.\n- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/aiox-source-inventory.json`.\n",
            encoding="utf-8",
        )
    print(f"Importadas {len(SKILLS)} skills do AIOX Embaixador.")


if __name__ == "__main__":
    main()
