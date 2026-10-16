#!/usr/bin/env python3
"""Verify a Quartz build of this vault.

Checks that the landing page rendered, representative wikilinks resolved to
real pages, ``.obsidian`` was excluded, and the content index has graph nodes
with edges.

:param public_dir: Quartz ``public/`` output directory.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MIN_GRAPH_NODES = 50
MIN_GRAPH_EDGES = 50

# (built html relative to public/, substring that must appear as an href)
# Quartz keeps punctuation in slugs (commas, apostrophes).
WIKILINK_CHECKS: tuple[tuple[str, str], ...] = (
    ("index.html", "Conference-Agenda-MOC"),
    ("index.html", "Validation-is-data,-not-an-event"),
    (
        "Maps-of-Content/Conference-Agenda-MOC.html",
        "2026-09-15-0822-bill-morgano-ai-continuous-validation-life-sciences",
    ),
    (
        "Evergreen-Notes/Validation-is-data,-not-an-event.html",
        "2026-09-15-0822-bill-morgano-ai-continuous-validation-life-sciences",
    ),
)

BACKLINK_PAGES = (
    "Home.html",
    "Evergreen-Notes/Validation-is-data,-not-an-event.html",
)


def _load_content_index(public_dir: Path) -> dict[str, object]:
    """Return the Quartz content index used by search and the graph.

    :param public_dir: Build output directory.
    :returns: Mapping of slug to page records.
    """
    candidates = [
        public_dir / "static" / "contentIndex.json",
        public_dir / "contentIndex.json",
    ]
    for path in candidates:
        if path.is_file():
            raw = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                raise TypeError(f"content index is not an object: {path}")
            return raw
    raise FileNotFoundError(
        f"No contentIndex.json under {public_dir} (looked in static/)"
    )


def _count_edges(index: dict[str, object]) -> int:
    """Count directed wikilink edges in the content index.

    :param index: Quartz content index.
    :returns: Number of link entries across all nodes.
    """
    edges = 0
    for record in index.values():
        if not isinstance(record, dict):
            continue
        links = record.get("links", [])
        if isinstance(links, list):
            edges += len(links)
    return edges


def verify_build(public_dir: Path) -> list[str]:
    """Run checks and return a list of failure messages (empty if ok).

    :param public_dir: Quartz ``public/`` directory.
    :returns: Human-readable failure strings.
    """
    failures: list[str] = []

    if not public_dir.is_dir():
        return [f"Build output directory does not exist: {public_dir}"]

    index_html = public_dir / "index.html"
    if not index_html.is_file():
        failures.append("Missing public/index.html (Home.md landing page)")
    else:
        html = index_html.read_text(encoding="utf-8", errors="replace")
        if "Maps of Content" not in html:
            failures.append("index.html does not contain Home.md heading/content")
        if "graph-container" not in html:
            failures.append("index.html is missing the local graph container")
        if "global-graph-container" not in html:
            failures.append("index.html is missing the global graph container")
        if "search" not in html.lower():
            failures.append("index.html does not include search UI")
        if "explorer" not in html.lower():
            failures.append("index.html does not include the file explorer")

    obs_hits = list(public_dir.rglob(".obsidian"))
    if obs_hits:
        failures.append(f".obsidian leaked into the site: {obs_hits[:3]}")

    pdf_hits = list(public_dir.rglob("*.pdf"))
    if not pdf_hits:
        failures.append("Agenda PDF was not copied into the site output")

    for rel, needle in WIKILINK_CHECKS:
        page = public_dir / rel
        if not page.is_file():
            failures.append(f"Expected page missing (wikilink target): {rel}")
            continue
        body = page.read_text(encoding="utf-8", errors="replace")
        if needle not in body:
            failures.append(f"{rel} does not contain resolved wikilink '{needle}'")

    for rel in BACKLINK_PAGES:
        page = public_dir / rel
        if not page.is_file():
            failures.append(f"Expected page missing (backlinks check): {rel}")
            continue
        body = page.read_text(encoding="utf-8", errors="replace")
        if "backlink" not in body.lower():
            failures.append(f"{rel} is missing backlinks UI")

    try:
        index = _load_content_index(public_dir)
    except (FileNotFoundError, TypeError, json.JSONDecodeError) as exc:
        failures.append(f"Could not read content index: {exc}")
        return failures

    node_count = len(index)
    edge_count = _count_edges(index)
    if node_count < MIN_GRAPH_NODES:
        failures.append(
            f"Graph has too few nodes: {node_count} (expected >= {MIN_GRAPH_NODES})"
        )
    if edge_count < MIN_GRAPH_EDGES:
        failures.append(
            f"Graph has too few edges: {edge_count} (expected >= {MIN_GRAPH_EDGES})"
        )

    slugs = " ".join(index.keys())
    for required in (
        "index",
        "Home",
        "Maps-of-Content/Conference-Agenda-MOC",
        "Evergreen-Notes/Validation-is-data-not-an-event",
    ):
        if required not in slugs and required.lower() not in slugs.lower():
            # Allow Quartz slug variants (apostrophes, etc.)
            slug_pat = re.sub(r"[^A-Za-z0-9]+", ".*", required)
            if not re.search(slug_pat, slugs, re.IGNORECASE):
                failures.append(f"Content index missing expected slug: {required}")

    print(f"Graph nodes: {node_count}")
    print(f"Graph edges: {edge_count}")
    return failures


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    :param argv: Optional argument list (defaults to ``sys.argv[1:]``).
    :returns: Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "public_dir",
        type=Path,
        help="Quartz public/ output directory",
    )
    args = parser.parse_args(argv)
    public_dir = args.public_dir.resolve()
    failures = verify_build(public_dir)
    if failures:
        print("Build verification failed:", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1
    print(f"Build verification passed: {public_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
