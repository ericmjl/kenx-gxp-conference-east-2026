"""Tests for Quartz staging and build verification helpers."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from stage_content import stage_content
from verify_build import verify_build


def test_stage_content_copies_home_as_index_and_skips_obsidian(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Staging copies published folders and writes index.md from Home.md."""
    vault = tmp_path / "vault"
    (vault / "Evergreen Notes").mkdir(parents=True)
    (vault / "Maps of Content").mkdir()
    (vault / "Transcripts").mkdir()
    (vault / "Resources").mkdir()
    (vault / ".obsidian").mkdir()
    (vault / "Home.md").write_text("# Home\n\nHello.\n", encoding="utf-8")
    (vault / "Evergreen Notes" / "A claim.md").write_text("note\n", encoding="utf-8")
    (vault / ".obsidian" / "app.json").write_text("{}\n", encoding="utf-8")
    (vault / "Resources" / "agenda.pdf").write_bytes(b"%PDF-fake")

    dest = tmp_path / "content"
    stage_content(dest, vault_root=vault)

    assert (dest / "Home.md").is_file()
    index_text = (dest / "index.md").read_text(encoding="utf-8")
    assert "title: Home" in index_text
    assert "# Home" in index_text
    assert (dest / "Evergreen Notes" / "A claim.md").is_file()
    assert not (dest / ".obsidian").exists()
    assert (dest / "Resources" / "agenda.pdf").is_file()
    assert (dest / "Resources" / "agenda").is_file()


def test_verify_build_accepts_a_minimal_valid_output(tmp_path: Path) -> None:
    """Verification passes when pages, wikilinks, and graph data are present."""
    public = tmp_path / "public"
    moc = public / "Maps-of-Content"
    evergreen = public / "Evergreen-Notes"
    static = public / "static"
    moc.mkdir(parents=True)
    evergreen.mkdir()
    static.mkdir()
    resources = public / "Resources"
    resources.mkdir()
    (resources / "agenda.pdf").write_bytes(b"%PDF")

    index_body = """
    <html><body>
      <div>Maps of Content</div>
      <div class="explorer">files</div>
      <div class="graph-container"></div>
      <div class="global-graph-container"></div>
      <input placeholder="Search" />
      <a href="./Maps-of-Content/Conference-Agenda-MOC">Conference Agenda MOC</a>
      <a href="./Evergreen-Notes/Validation-is-data,-not-an-event">Validation is data, not an event</a>
    </body></html>
    """
    (public / "index.html").write_text(index_body, encoding="utf-8")

    moc_body = """
    <html><body>
      <div class="backlinks">Backlinks</div>
      <a href="../Transcripts/2026-09-15-0822-bill-morgano-ai-continuous-validation-life-sciences">talk</a>
    </body></html>
    """
    (moc / "Conference-Agenda-MOC.html").write_text(moc_body, encoding="utf-8")

    evergreen_body = """
    <html><body>
      <div class="backlinks">Backlinks</div>
      <a href="../Transcripts/2026-09-15-0822-bill-morgano-ai-continuous-validation-life-sciences">source</a>
    </body></html>
    """
    (evergreen / "Validation-is-data,-not-an-event.html").write_text(
        evergreen_body, encoding="utf-8"
    )
    (public / "Home.html").write_text(evergreen_body, encoding="utf-8")

    nodes = {
        "index": {"title": "Home", "links": ["Home", "Maps-of-Content/Conference-Agenda-MOC"]},
        "Home": {"title": "Home", "links": ["Maps-of-Content/Conference-Agenda-MOC"]},
        "Maps-of-Content/Conference-Agenda-MOC": {
            "title": "Conference Agenda MOC",
            "links": [
                "Transcripts/2026-09-15-0822-bill-morgano-ai-continuous-validation-life-sciences"
            ],
        },
        "Evergreen-Notes/Validation-is-data,-not-an-event": {
            "title": "Validation is data, not an event",
            "links": [
                "Transcripts/2026-09-15-0822-bill-morgano-ai-continuous-validation-life-sciences"
            ],
        },
    }
    for i in range(60):
        nodes[f"pad-{i}"] = {"title": f"pad {i}", "links": ["Home"]}
    (static / "contentIndex.json").write_text(json.dumps(nodes), encoding="utf-8")

    failures = verify_build(public)
    assert failures == []


def test_verify_build_fails_when_output_missing(tmp_path: Path) -> None:
    """Verification reports a missing public directory."""
    failures = verify_build(tmp_path / "does-not-exist")
    assert failures
    assert "does not exist" in failures[0]
