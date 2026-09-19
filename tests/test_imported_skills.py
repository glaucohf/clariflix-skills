"""Verify published snapshots and entrypoint references without the local source repo."""
from pathlib import Path
import hashlib
import json
import re
import unittest
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


class ImportedSkillsTests(unittest.TestCase):
    def test_generated_squad_snapshots_match_provenance(self):
        sources = list((ROOT / "skills").glob("*/SOURCE.md"))
        count = 0
        for source in sources:
            text = source.read_text(encoding="utf-8")
            if "generated-by: scripts/import_generated_squads.py" not in text:
                continue
            count += 1
            entries = re.findall(r"\| `([^`]+)` \| `([a-f0-9]{64})` \|", text)
            self.assertTrue(entries, source.parent.name)
            for relative, expected in entries:
                with self.subTest(skill=source.parent.name, file=relative):
                    actual = (source.parent / "references/squad" / relative).read_bytes()
                    self.assertEqual(hashlib.sha256(actual).hexdigest(), expected)
        self.assertEqual(count, 64)

    def test_free_squad_snapshots_match_inventory(self):
        inventories = list((ROOT / "skills").glob("*/references/source-inventory.json"))
        self.assertEqual(len(inventories), 13)
        for inventory in inventories:
            metadata = json.loads(inventory.read_text(encoding="utf-8"))
            for item in metadata["files"]:
                with self.subTest(skill=inventory.parent.parent.name, file=item["path"]):
                    content = (inventory.parent / "squad" / item["path"]).read_bytes()
                    self.assertEqual(len(content), item["bytes"])
                    self.assertEqual(hashlib.sha256(content).hexdigest(), item["sha256"])

    def test_adapter_links_resolve_inside_their_package(self):
        for source in (ROOT / "skills").glob("*/SOURCE.md"):
            skill = source.parent
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if urlparse(target).scheme or target.startswith("#"):
                    continue
                relative = unquote(target.split("#", 1)[0])
                with self.subTest(skill=skill.name, link=target):
                    path = (skill / relative).resolve()
                    self.assertTrue(path.is_relative_to(skill.resolve()))
                    self.assertTrue(path.exists())

    def test_catalog_keeps_all_packages_and_complete_install_sources(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        names = {item["name"] for item in catalog["skills"]}
        package_names = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(names, package_names)
        self.assertGreaterEqual(len(names), 90)
        for item in catalog["skills"]:
            expected = f"/tree/v{catalog['version']}/skills/{item['name']}"
            for key in ("install_cmd", "npx_codex", "npx_claude_code", "npx_any"):
                self.assertIn(expected, item[key])
            self.assertIn(item["row"], catalog["rows"])
        proposal = next(item for item in catalog["skills"] if item["name"] == "proposta-comercial")
        self.assertTrue(proposal["runtime_only"])


if __name__ == "__main__":
    unittest.main()
