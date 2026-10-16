#!/usr/bin/env python3
"""Stage vault notes into a Quartz ``content/`` directory.

Copies the Obsidian vault's published folders without moving or rewriting
the originals. ``Home.md`` is also written as ``index.md`` so the landing
page is the vault home note.

:param content_dir: Destination directory (created or replaced).
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent

# Only these vault paths are published. Tooling, .obsidian, and README stay out.
PUBLISH_FILES = ("Home.md",)
PUBLISH_DIRS = (
    "Evergreen Notes",
    "Maps of Content",
    "Transcripts",
    "Resources",
)


def _with_home_title(markdown: str) -> str:
    """Return markdown whose frontmatter sets ``title: Home``.

    Quartz uses the filename as the page title when frontmatter has none, so a
    raw copy of ``Home.md`` → ``index.md`` would render as "index".

    :param markdown: Source of ``Home.md``.
    :returns: Text for staged ``index.md``.
    """
    if markdown.startswith("---"):
        body = markdown[3:].lstrip("\n")
        if body.lower().startswith("title:"):
            return markdown
        return "---\ntitle: Home\n" + body
    return "---\ntitle: Home\n---\n\n" + markdown


def stage_content(content_dir: Path, vault_root: Path = VAULT_ROOT) -> None:
    """Replace ``content_dir`` with a Quartz-ready copy of the vault notes.

    :param content_dir: Quartz content directory to write.
    :param vault_root: Vault root (the Git repository root).
    """
    if content_dir.exists():
        shutil.rmtree(content_dir)
    content_dir.mkdir(parents=True)

    for name in PUBLISH_FILES:
        source = vault_root / name
        if not source.is_file():
            raise FileNotFoundError(f"Expected vault file missing: {source}")
        shutil.copy2(source, content_dir / name)

    for name in PUBLISH_DIRS:
        source = vault_root / name
        if not source.is_dir():
            raise FileNotFoundError(f"Expected vault folder missing: {source}")
        shutil.copytree(
            source,
            content_dir / name,
            ignore=shutil.ignore_patterns(".obsidian", ".DS_Store"),
        )

    # Quartz serves ``index.md`` at ``/``. Do not rename Home.md in the vault.
    home_text = (vault_root / "Home.md").read_text(encoding="utf-8")
    (content_dir / "index.md").write_text(_with_home_title(home_text), encoding="utf-8")

    # Wikilinks to PDFs omit the extension; publish an extensionless copy too.
    resources = content_dir / "Resources"
    if resources.is_dir():
        for pdf in resources.glob("*.pdf"):
            shutil.copy2(pdf, pdf.with_suffix(""))


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    :param argv: Optional argument list (defaults to ``sys.argv[1:]``).
    :returns: Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "content_dir",
        type=Path,
        help="Destination Quartz content directory",
    )
    args = parser.parse_args(argv)
    stage_content(args.content_dir.resolve())
    print(f"Staged vault notes into {args.content_dir.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
