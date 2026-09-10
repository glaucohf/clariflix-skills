#!/usr/bin/env python3
"""Confere a forma de cada skills/<slug>/SKILL.md + manifest.yaml. Sai com código != 0 se algo falhar."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_SECTIONS = ["## When to Use", "## Quick Reference", "## Procedure", "## Pitfalls", "## Verification"]
REQUIRED_FRONTMATTER = ["name", "description", "version", "license"]


def check_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_md = skill_dir / "SKILL.md"
    manifest = skill_dir / "manifest.yaml"
    if not skill_md.exists():
        return [f"{skill_dir.name}: falta SKILL.md"]
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{skill_dir.name}: SKILL.md sem frontmatter"]
    end = text.find("\n---", 4)
    fm = yaml.safe_load(text[4:end])
    for key in REQUIRED_FRONTMATTER:
        if key not in fm:
            errors.append(f"{skill_dir.name}: frontmatter sem '{key}'")
    if fm.get("name") != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name='{fm.get('name')}' != pasta")
    if len(fm.get("description", "")) > 200:
        errors.append(f"{skill_dir.name}: description > 200 caracteres")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{skill_dir.name}: falta seção '{section}'")
    if not manifest.exists():
        errors.append(f"{skill_dir.name}: falta manifest.yaml")
    else:
        m = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        for key in ["row", "title", "title_netflix", "subtitle", "painel"]:
            if key not in m:
                errors.append(f"{skill_dir.name}: manifest.yaml sem '{key}'")
    return errors


if __name__ == "__main__":
    all_errors: list[str] = []
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if skill_dir.is_dir():
            all_errors.extend(check_skill(skill_dir))
    if all_errors:
        print("\n".join(all_errors))
        print(f"\n{len(all_errors)} problema(s) encontrado(s).")
        sys.exit(1)
    print("Todas as skills passaram na validação de forma.")
