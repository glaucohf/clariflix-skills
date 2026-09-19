"""Contrato dos pacotes distribuídos, sem tocar nos artefatos do repositório."""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_distribution import build  # noqa: E402


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "example"
        self.skill.mkdir(parents=True)
        self.write("SKILL.md", "---\nname: example\n---\n\n## Procedure\nLeia references/guide.md.\n")
        self.write("manifest.yaml", "title: Exemplo\n")
        self.write("references/guide.md", "# Guia\nConteúdo de apoio.\n")
        self.write("assets/template.html", "<html><body>Modelo</body></html>\n")
        self.write("scripts/helper.py", 'raise RuntimeError("este script não deve executar")\n# ```\n')
        self.write("LICENSE", "Aviso de autoria que deve acompanhar a distribuição.\n")
        self.write("__pycache__/helper.pyc", b"cached")
        self.write(".git/config", "não empacotar\n")
        self.write("assets/icon.png", b"\x89PNG\r\n\x00binary")
        self.item = {"name": "example", "path": "skills/example/SKILL.md", "runtime_only": True}
        self.catalog([self.item])

    def write(self, name, content):
        path = self.skill / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8") if isinstance(content, str) else content)

    def catalog(self, skills):
        (self.root / "catalog.json").write_text(
            json.dumps({"version": "0.2.0", "skills": skills}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def test_complete_zip_and_standalone_supports(self):
        self.assertEqual(build(self.root), 1)
        with zipfile.ZipFile(self.root / "dist/example.zip") as archive:
            self.assertEqual(archive.namelist(), [
                "example/LICENSE", "example/SKILL.md", "example/assets/icon.png",
                "example/assets/template.html", "example/references/guide.md", "example/scripts/helper.py",
            ])
            self.assertEqual(archive.read("example/assets/icon.png"), b"\x89PNG\r\n\x00binary")
            self.assertEqual(archive.read("example/scripts/helper.py"), (self.skill / "scripts/helper.py").read_bytes())
        prompt = (self.root / "docs/prompt/example.md").read_text(encoding="utf-8")
        self.assertIn("## Procedure", prompt)
        self.assertIn("## Referência: references/guide.md", prompt)
        self.assertIn("Conteúdo de apoio.", prompt)
        self.assertIn("## Referência: assets/template.html", prompt)
        self.assertIn("<html><body>Modelo</body></html>", prompt)
        self.assertIn("## Referência: scripts/helper.py", prompt)
        self.assertIn("````python", prompt)
        self.assertIn('raise RuntimeError("este script não deve executar")', prompt)
        self.assertIn("## Referência: LICENSE", prompt)
        self.assertIn("Arquivo binário incluído no ZIP", prompt)
        self.assertIn("não instala ferramentas nem integrações", prompt)
        self.assertIn("exige ferramentas de execução", prompt)

    def test_catalog_copies_are_exact_and_nojekyll_exists(self):
        build(self.root)
        original = (self.root / "catalog.json").read_bytes()
        self.assertEqual((self.root / "docs/catalog.json").read_bytes(), original)
        self.assertEqual((self.root / "site/catalog.json").read_bytes(), original)
        self.assertEqual((self.root / "docs/.nojekyll").read_bytes(), b"")

    def test_outputs_are_deterministic_when_source_mtime_changes(self):
        build(self.root)
        outputs = ["dist/example.zip", "docs/prompt/example.md"]
        first = {name: (self.root / name).read_bytes() for name in outputs}
        os.utime(self.skill / "SKILL.md", (1_900_000_000, 1_900_000_000))
        build(self.root)
        self.assertEqual(first, {name: (self.root / name).read_bytes() for name in outputs})

    def test_rejects_traversal_and_invalid_slugs_before_writing(self):
        for slug in ("../outside", "..\\outside", "/absolute", "C:\\absolute", "has space"):
            with self.subTest(slug=slug):
                self.catalog([self.item, {"name": slug, "path": f"skills/{slug}/SKILL.md"}])
                with self.assertRaisesRegex(ValueError, "Slug inválido"):
                    build(self.root)
                self.assertFalse((self.root / "dist").exists())

    def test_rejects_catalog_path_traversal_and_duplicates(self):
        self.catalog([{**self.item, "path": "../outside/SKILL.md"}])
        with self.assertRaisesRegex(ValueError, "Caminho inválido"):
            build(self.root)
        self.catalog([self.item, self.item])
        with self.assertRaisesRegex(ValueError, "duplicada"):
            build(self.root)
        self.assertFalse((self.root / "dist").exists())

    def test_rejects_support_symlink(self):
        target = self.root / "private.txt"
        target.write_text("fora da skill", encoding="utf-8")
        link = self.skill / "references/private.txt"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("Este host não permite criar symlinks")
        with self.assertRaisesRegex(ValueError, "Link não permitido"):
            build(self.root)
        self.assertFalse((self.root / "dist").exists())

    def test_rejects_output_symlink(self):
        target = self.root / "other-docs"
        target.mkdir()
        try:
            (self.root / "docs").symlink_to(target, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Este host não permite criar symlinks")
        with self.assertRaisesRegex(ValueError, "Link não permitido"):
            build(self.root)
        self.assertFalse((self.root / "dist").exists())

    def test_missing_skill_fails_before_copying_catalog(self):
        self.catalog([self.item, {"name": "missing", "path": "skills/missing/SKILL.md"}])
        with self.assertRaisesRegex(ValueError, "não encontrada"):
            build(self.root)
        self.assertFalse((self.root / "docs").exists())


if __name__ == "__main__":
    unittest.main()
