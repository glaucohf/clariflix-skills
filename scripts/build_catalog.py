#!/usr/bin/env python3
"""Gera catalog.json a partir de skills/<slug>/manifest.yaml + frontmatter do SKILL.md.

Uso: python3 scripts/build_catalog.py [--tag v0.1.0]
Sem --tag, usa "version" do catalog.json anterior (ou 0.1.0 na primeira vez).
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from hub_common import REPO_SLUG, WELLKNOWN, HUB_URL, DESC_MAX, RUNTIME_ONLY, cap200  # noqa: E402

ROWS = {
    "atendimento": "Atendimento & WhatsApp",
    "rotina": "Agendamento & Rotina",
    "conferencia": "Conferência & Cálculo",
    "sop": "Processos",
    "decisao": "Decisão & Clareza",
    "setores": "Por setor",
    "vendas": "Vendas & Receita",
    "marketing": "Marketing & Aquisição",
    "operacoes": "Operações & Customer Success",
    "gestao": "Gestão & Estratégia",
    "especialistas": "Squads Especialistas",
}
ROW_ORDER = list(ROWS)


def parse_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{skill_md} sem frontmatter"
    end = text.index("\n---", 4)
    return yaml.safe_load(text[4:end])


def count_files(skill_dir: Path) -> int:
    return sum(1 for p in skill_dir.rglob("*") if p.is_file()
               and p.name != "manifest.yaml" and "__pycache__" not in p.parts
               and p.suffix != ".pyc")


def build(tag: str) -> dict:
    skills_dir = ROOT / "skills"
    items = []
    for skill_dir in sorted(skills_dir.iterdir()):
        skill_md = skill_dir / "SKILL.md"
        manifest_path = skill_dir / "manifest.yaml"
        if not skill_md.exists() or not manifest_path.exists():
            continue
        fm = parse_frontmatter(skill_md)
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        slug = fm["name"]
        version = fm.get("version", tag.lstrip("v"))
        source_url = f"https://github.com/{REPO_SLUG}/tree/{tag}/skills/{slug}"
        install_url = f"https://raw.githubusercontent.com/{REPO_SLUG}/{tag}/skills/{slug}/SKILL.md"
        item = {
            "name": slug,
            "version": version,
            "license": fm["license"],
            "author": fm.get("author", ""),
            "path": f"skills/{slug}/SKILL.md",
            "description": cap200(fm["description"]),
            "row": manifest["row"],
            "title": manifest["title"],
            "title_netflix": manifest["title_netflix"],
            "subtitle": manifest["subtitle"],
            "genre": manifest.get("genre", "procedural"),
            "since": version,
            "files": count_files(skill_dir),
            "badge": manifest.get("badge", ""),
            "install_url": install_url,
            "install_cmd": f"npx skills add {source_url} --skill {slug} -a hermes-agent -g",
            "chat_cmd": (
                f"Inspecione e instale esta skill com todos os arquivos de apoio: {source_url}\n"
                "Antes de instalar, leia a licença, o SKILL.md e qualquer arquivo de apoio. "
                "Não execute scripts nem forneça credenciais sem explicar antes o que acontecerá."
            ),
            "github_url": f"https://github.com/{REPO_SLUG}/blob/main/skills/{slug}/SKILL.md",
            "painel": manifest["painel"],
            "runtime_only": manifest.get("runtime_only", slug in RUNTIME_ONLY),
            "zip_url": f"https://github.com/{REPO_SLUG}/releases/download/{tag}/{slug}.zip",
            "prompt_url": f"{WELLKNOWN}/prompt/{slug}.md",
            "npx_claude_code": f"npx skills add {source_url} --skill {slug} -a claude-code -g",
            "npx_codex": f"npx skills add {source_url} --skill {slug} -a codex -g",
            "npx_any": f"npx skills add {source_url} --skill {slug} -g",
        }
        image_path = f"images/skills/{slug}.webp"
        if (ROOT / "site" / image_path).is_file():
            item["image"] = image_path
        items.append(item)

    catalog = {
        "name": "ClariFlix",
        "brand": "CLARIFLIX",
        "tagline": "Instale clareza, não um prompt.",
        "version": tag.lstrip("v"),
        "repo": REPO_SLUG,
        "tap": f"hermes skills tap add {REPO_SLUG}",
        "wellknown": WELLKNOWN,
        "rows": ROWS,
        "row_order": ROW_ORDER,
        "featured": "decisao-diagnostico-pme",
        "curated": [
            {
                "id": "comecar",
                "title": "Para começar",
                "note": "Uma semana: descubra onde a IA devolve tempo primeiro, monte o SOP e coloque o agente para responder.",
                "slugs": ["decisao-diagnostico-pme", "sop-extrair", "atendimento-triagem-whatsapp"],
            }
        ],
        "skills": items,
    }
    return catalog


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    previous = ROOT / "catalog.json"
    default_tag = "v" + json.loads(previous.read_text(encoding="utf-8"))["version"] if previous.exists() else "v0.1.0"
    ap.add_argument("--tag", default=default_tag)
    args = ap.parse_args()
    catalog = build(args.tag)
    out = ROOT / "catalog.json"
    out.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"catalog.json gerado com {len(catalog['skills'])} skills (tag {args.tag})")
