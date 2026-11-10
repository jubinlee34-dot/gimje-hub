#!/usr/bin/env python3
"""Generate the public Pages artifact from approved course folders only."""
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ("session1", "session2", "etc")
EXTENSIONS = {
    ".html", ".htm", ".pdf", ".ppt", ".pptx", ".doc", ".docx",
    ".xls", ".xlsx", ".txt", ".csv", ".zip",
    ".png", ".jpg", ".jpeg", ".gif", ".webp"
}
MAX_BYTES = 10_000_000


class BuildError(ValueError):
    pass


def external_link(value):
    if not isinstance(value, dict):
        raise BuildError("링크 JSON은 객체여야 함")
    name, url = value.get("name"), value.get("url")
    if not isinstance(name, str) or not name.strip() or len(name) > 180:
        raise BuildError("링크 이름 오류")
    if not isinstance(url, str) or len(url) > 2048:
        raise BuildError("링크 URL 오류")
    if any(ord(char) < 33 or ord(char) == 127 for char in url) or "\\" in url:
        raise BuildError("링크 URL에 공백·제어문자 포함")
    parsed = urlsplit(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username or parsed.password:
        raise BuildError("HTTP(S) 주소만 등록 가능")
    return {"type": "link", "name": name.strip(), "url": url}


def build_site(root=ROOT, output=None):
    root = Path(root).resolve()
    output = Path(output or root / "dist").resolve()
    if output == root or output in [root / name for name in CATEGORIES]:
        raise BuildError("출력 경로가 프로젝트 루트 또는 자료 폴더임")
    for path in ("index.html", "admin.html", "assets/style.css", "assets/app.js"):
        if not (root / path).is_file():
            raise BuildError("필수 웹 파일 누락: " + path)
    if output.exists():
        if output.is_symlink():
            raise BuildError("출력 경로 심볼릭 링크 금지")
        shutil.rmtree(output)
    output.mkdir(parents=True)
    for name in ("index.html", "admin.html"):
        shutil.copy2(root / name, output / name)
    shutil.copytree(root / "assets", output / "assets")
    (output / ".nojekyll").write_text("", encoding="utf-8")
    catalog = {"schemaVersion": 1, "generatedAt": datetime.now(timezone.utc).isoformat()}
    for category in CATEGORIES:
        catalog[category] = []
        source = root / category
        dest = output / category
        dest.mkdir()
        if not source.exists():
            continue
        for file in sorted(source.iterdir(), key=lambda item: item.name.casefold()):
            if file.name.startswith("."):
                continue
            if file.is_symlink() or not file.is_file():
                raise BuildError("허용되지 않는 자료 경로: " + category + "/" + file.name)
            if len(file.name) > 180 or any(ord(ch) < 32 for ch in file.name):
                raise BuildError("파일명 오류: " + file.name)
            if category == "etc" and file.suffix.lower() == ".json":
                if file.stat().st_size > 16_384:
                    raise BuildError("링크 JSON 크기 초과: " + file.name)
                try:
                    data = json.loads(file.read_text(encoding="utf-8"))
                except (ValueError, UnicodeError) as exc:
                    raise BuildError("링크 JSON 파싱 실패: " + file.name) from exc
                catalog[category].append(external_link(data))
                continue
            if file.suffix.lower() not in EXTENSIONS:
                raise BuildError("지원하지 않는 확장자: " + file.name)
            size = file.stat().st_size
            if size < 1 or size > MAX_BYTES:
                raise BuildError("파일 용량 1~10,000,000바이트만 허용: " + file.name)
            shutil.copy2(file, dest / file.name)
            catalog[category].append({
                "type": "file",
                "name": file.name,
                "path": category + "/" + quote(file.name, safe="-_.()")
            })
    (output / "data").mkdir()
    (output / "data/catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return catalog


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "dist"))
    args = parser.parse_args()
    data = build_site(ROOT, args.output)
    print("QA build OK: " + ", ".join(key + "=" + str(len(data[key])) for key in CATEGORIES))


if __name__ == "__main__":
    main()
