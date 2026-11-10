import json
import tempfile
import unittest
from pathlib import Path
from urllib.parse import quote
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_site import BuildError, build_site, external_link


class SiteBuilderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "source"
        self.root.mkdir()
        (self.root / "assets").mkdir()
        for file in ("index.html", "admin.html", "assets/style.css", "assets/app.js"):
            dest = self.root / file
            dest.write_bytes((ROOT / file).read_bytes())
        for folder in ("session1", "session2", "etc"):
            (self.root / folder).mkdir()
        self.output = Path(self.tmp.name) / "dist"

    def build(self):
        return build_site(self.root, self.output)

    def test_empty_catalog(self):
        result = self.build()
        self.assertEqual(result["schemaVersion"], 1)
        self.assertEqual(result["session1"], [])
        self.assertTrue((self.output / "data/catalog.json").exists())
        self.assertFalse((self.output / "README.md").exists())

    def test_korean_filename(self):
        name = "김제 1회차 강의안.html"
        (self.root / "session1" / name).write_text("<html>ok</html>", encoding="utf-8")
        data = self.build()
        self.assertEqual(data["session1"][0]["path"], "session1/" + quote(name, safe="-_.()"))
        self.assertTrue((self.output / "session1" / name).exists())

    def test_separate_sessions(self):
        (self.root / "session1" / "ai.pdf").write_bytes(b"pdf")
        (self.root / "session2" / "canva.pdf").write_bytes(b"pdf")
        result = self.build()
        self.assertEqual(len(result["session1"]), 1)
        self.assertEqual(len(result["session2"]), 1)

    def test_extra_file_and_link(self):
        (self.root / "etc" / "memo.txt").write_text("hello", encoding="utf-8")
        (self.root / "etc" / "site.json").write_text(
            json.dumps({"name": "참고 사이트", "url": "https://example.com"}), encoding="utf-8")
        data = self.build()
        self.assertEqual({x["type"] for x in data["etc"]}, {"file", "link"})
        self.assertFalse((self.output / "etc" / "site.json").exists())

    def test_invalid_scheme_rejected(self):
        for url in ("javascript:alert(1)", "data:text/html,evil", "https://x.test/a b"):
            with self.subTest(url=url), self.assertRaises(BuildError):
                external_link({"name": "bad", "url": url})

    def test_url_credentials_rejected(self):
        with self.assertRaises(BuildError):
            external_link({"name": "bad", "url": "https://user:pass@example.com"})

    def test_invalid_link_json(self):
        (self.root / "etc" / "bad.json").write_text("{bad", encoding="utf-8")
        with self.assertRaises(BuildError):
            self.build()

    def test_disallowed_extension(self):
        (self.root / "session1" / "attack.exe").write_bytes(b"exe")
        with self.assertRaises(BuildError):
            self.build()

    def test_oversized_file(self):
        with (self.root / "session2" / "big.pdf").open("wb") as fp:
            fp.truncate(10_000_001)
        with self.assertRaises(BuildError):
            self.build()

    def test_empty_file(self):
        (self.root / "session1" / "empty.pdf").touch()
        with self.assertRaises(BuildError):
            self.build()

    def test_hidden_files_ignored(self):
        (self.root / "etc" / ".gitkeep").write_text("x", encoding="utf-8")
        data = self.build()
        self.assertEqual(data["etc"], [])

    def test_catalog_matches_artifact(self):
        data = self.build()
        result = json.loads((self.output / "data/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(data, result)


if __name__ == "__main__":
    unittest.main()
