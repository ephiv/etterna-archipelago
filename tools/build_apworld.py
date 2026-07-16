from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
WORLD_DIR = ROOT / "worlds" / "etterna"
DIST_DIR = ROOT / "dist"
OUTPUT = DIST_DIR / "etterna.apworld"


def main() -> None:
    DIST_DIR.mkdir(exist_ok=True)
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as archive:
        for path in sorted(WORLD_DIR.rglob("*")):
            if path.is_file() and path.suffix != ".pyc":
                archive.write(path, path.relative_to(WORLD_DIR.parent))
    print(OUTPUT)


if __name__ == "__main__":
    main()
