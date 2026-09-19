#!/usr/bin/env python3
"""Gera ZIPs completos e versões para anexar a partir do catálogo existente.

Uso: python scripts/build_distribution.py
Saídas: dist/<slug>.zip, docs/prompt/<slug>.md, docs/.nojekyll e cópias
de catalog.json em docs/ e site/. Não executa nenhum script das skills.
Instaladores devem usar o repositório Git; não há índice .well-known próprio.
"""
from __future__ import annotations

import argparse
import io
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
IGNORED_PARTS = {
    ".git", ".hg", ".svn", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", "node_modules", ".DS_Store", "Thumbs.db",
}
LANGUAGES = {
    ".py": "python", ".sh": "bash", ".ps1": "powershell", ".js": "javascript",
    ".mjs": "javascript", ".ts": "typescript", ".json": "json", ".yaml": "yaml",
    ".yml": "yaml", ".html": "html", ".css": "css", ".xml": "xml", ".sql": "sql",
}


def contained_path(root: Path, path: Path) -> Path:
    """Rejeita traversal, links simbólicos e junctions de entrada ou saída."""
    try:
        relative = path.relative_to(root)
        path.resolve().relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Caminho fora do repositório: {path}") from exc
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink() or getattr(current, "is_junction", lambda: False)():
            raise ValueError(f"Link não permitido na distribuição: {current}")
    return path


def package_files(root: Path, slug: str) -> list[tuple[str, bytes]]:
    """Lê um pacote completo; nomes de arquivos são relativos à raiz da skill."""
    skill_dir = contained_path(root, root / "skills" / slug)
    if not skill_dir.is_dir():
        raise ValueError(f"Pasta da skill não encontrada: {slug}")
    files = []
    for path in sorted(skill_dir.rglob("*"), key=lambda p: p.relative_to(skill_dir).as_posix()):
        relative = path.relative_to(skill_dir)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.suffix.lower() in {".pyc", ".pyo"} or relative.as_posix() == "manifest.yaml":
            continue
        contained_path(root, path)
        if path.is_file():
            # A barra invertida é separador em extratores Windows, mesmo num host Unix.
            if any("\\" in part or ":" in part for part in relative.parts):
                raise ValueError(f"Nome de arquivo não portátil: {relative}")
            files.append((relative.as_posix(), path.read_bytes()))
    if "SKILL.md" not in dict(files):
        raise ValueError(f"SKILL.md não encontrado: {slug}")
    return files


def make_zip(slug: str, files: list[tuple[str, bytes]]) -> bytes:
    """Mantém ordem, permissões e timestamp estáveis, sem copiar metadados locais."""
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, content in files:
            info = zipfile.ZipInfo(f"{slug}/{name}", date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, content, compresslevel=9)
    return output.getvalue()


def as_text(content: bytes) -> str | None:
    if b"\x00" in content:
        return None
    try:
        return content.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    except UnicodeDecodeError:
        return None


def make_prompt(slug: str, files: list[tuple[str, bytes]], runtime_only: bool = False) -> bytes:
    skill = as_text(dict(files)["SKILL.md"])
    if skill is None:
        raise ValueError(f"SKILL.md precisa ser texto UTF-8: {slug}")
    parts = [
        f"# {slug} · arquivo para anexar\n",
        "Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` "
        "no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio "
        "textuais; não instala ferramentas nem integrações. Scripts são apresentados como "
        "código de referência e não devem ser executados apenas por anexar este arquivo. "
        "Para trabalhar com a estrutura de arquivos original, instale o pacote completo.\n",
    ]
    if runtime_only:
        parts.append(
            "Esta skill exige ferramentas de execução para parte do procedimento. "
            "Anexar este arquivo a um chat não habilita essas ferramentas; confira os "
            "requisitos da skill antes de prometer o resultado.\n"
        )
    parts.extend(["---\n", skill.rstrip() + "\n"])
    for name, content in files:
        if name == "SKILL.md":
            continue
        parts.append(f"\n## Referência: {name}\n")
        support = as_text(content)
        if support is None:
            parts.append("Arquivo binário incluído no ZIP da skill; consulte o pacote completo.\n")
        elif Path(name).suffix.lower() in {".md", ".markdown"}:
            parts.append(support.rstrip() + "\n")
        else:
            # O conteúdo pode conter seus próprios blocos de código Markdown.
            longest = max((len(run) for run in re.findall(r"`+", support)), default=0)
            fence = "`" * max(3, longest + 1)
            language = LANGUAGES.get(Path(name).suffix.lower(), "text")
            parts.append(f"{fence}{language}\n{support.rstrip()}\n{fence}\n")
    return "\n".join(parts).encode("utf-8")


def build(root: Path = ROOT) -> int:
    """Valida e prepara tudo antes de atualizar os artefatos de distribuição."""
    root = Path(root).resolve()
    catalog_bytes = contained_path(root, root / "catalog.json").read_bytes()
    catalog = json.loads(catalog_bytes)
    skills = catalog.get("skills")
    if not isinstance(skills, list) or not skills:
        raise ValueError("catalog.json precisa conter uma lista não vazia de skills")
    artifacts: list[tuple[Path, bytes]] = []
    seen = set()
    for item in skills:
        slug = item.get("name") if isinstance(item, dict) else None
        if not isinstance(slug, str) or not SLUG.fullmatch(slug):
            raise ValueError(f"Slug inválido no catálogo: {slug!r}")
        if slug in seen:
            raise ValueError(f"Skill duplicada no catálogo: {slug}")
        seen.add(slug)
        if item.get("path") != f"skills/{slug}/SKILL.md":
            raise ValueError(f"Caminho inválido no catálogo: {slug}")
        files = package_files(root, slug)
        artifacts.extend([
            (root / "dist" / f"{slug}.zip", make_zip(slug, files)),
            (root / "docs" / "prompt" / f"{slug}.md", make_prompt(slug, files, item.get("runtime_only", False))),
        ])
    artifacts.extend([
        (root / "docs" / "catalog.json", catalog_bytes),
        (root / "site" / "catalog.json", catalog_bytes),
        (root / "docs" / ".nojekyll", b""),
    ])
    for path, _ in artifacts:
        contained_path(root, path)
    for path, content in artifacts:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    return len(skills)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        count = build()
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        parser.exit(1, f"Erro de distribuição: {exc}\n")
    print(f"Distribuição gerada: {count} ZIPs, {count} prompts e catálogos sincronizados.")
