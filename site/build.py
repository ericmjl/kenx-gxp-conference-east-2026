#!/usr/bin/env python3
"""Build the Quartz site from this Obsidian vault without moving notes.

Clones a pinned Quartz v4 release into a cache directory (outside the vault
when possible), copies ``site/quartz.config.ts`` and ``site/quartz.layout.ts``
onto that checkout, stages vault notes into ``content/``, then runs
``npx quartz build``.

:param quartz_dir: Optional Quartz checkout path (CI sets this).
:param output_dir: Optional output directory (defaults to Quartz ``public/``).
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

from stage_content import stage_content
from verify_build import verify_build

VAULT_ROOT = Path(__file__).resolve().parent.parent
QUARTZ_REPO = "https://github.com/jackyzha0/quartz.git"
QUARTZ_VERSION = "v4.5.2"


def _default_quartz_dir() -> Path:
    """Return a cache path for the Quartz checkout.

    Prefer a directory outside the vault so a local Obsidian app does not
    index Quartz source files.

    :returns: Absolute path for the Quartz clone.
    """
    env_dir = os.environ.get("QUARTZ_DIR")
    if env_dir:
        return Path(env_dir).expanduser().resolve()
    cache_home = os.environ.get("XDG_CACHE_HOME")
    if cache_home:
        return Path(cache_home) / "kenx-gxp-quartz" / QUARTZ_VERSION
    return Path.home() / ".cache" / "kenx-gxp-quartz" / QUARTZ_VERSION


def _run(command: list[str], cwd: Path) -> None:
    """Run a subprocess and raise on failure.

    :param command: Argument vector.
    :param cwd: Working directory.
    """
    print("+", " ".join(command), f"(cwd={cwd})")
    subprocess.run(command, cwd=cwd, check=True)


def ensure_quartz(quartz_dir: Path) -> None:
    """Clone or reuse the pinned Quartz v4 checkout.

    :param quartz_dir: Destination for the Quartz git clone.
    """
    git_dir = quartz_dir / ".git"
    if git_dir.exists():
        print(f"Reusing Quartz checkout at {quartz_dir}")
        return
    if quartz_dir.exists():
        shutil.rmtree(quartz_dir)
    quartz_dir.parent.mkdir(parents=True, exist_ok=True)
    _run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--branch",
            QUARTZ_VERSION,
            QUARTZ_REPO,
            str(quartz_dir),
        ],
        cwd=quartz_dir.parent,
    )


def apply_site_config(quartz_dir: Path) -> None:
    """Copy this vault's Quartz config onto the checkout.

    :param quartz_dir: Quartz project root.
    """
    site_dir = Path(__file__).resolve().parent
    shutil.copy2(site_dir / "quartz.config.ts", quartz_dir / "quartz.config.ts")
    shutil.copy2(site_dir / "quartz.layout.ts", quartz_dir / "quartz.layout.ts")


def build_site(quartz_dir: Path, output_dir: Path | None) -> Path:
    """Install Quartz dependencies and build the static site.

    :param quartz_dir: Quartz project root.
    :param output_dir: Optional output directory; ``None`` uses Quartz default.
    :returns: Absolute path of the built ``public`` directory.
    """
    apply_site_config(quartz_dir)
    stage_content(quartz_dir / "content", VAULT_ROOT)
    _run(["npm", "ci"], cwd=quartz_dir)
    command = ["npx", "quartz", "build"]
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
        command.extend(["--output", str(output_dir)])
        public_dir = output_dir
    else:
        public_dir = quartz_dir / "public"
    _run(command, cwd=quartz_dir)
    (public_dir / ".nojekyll").write_text("", encoding="utf-8")
    return public_dir


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    :param argv: Optional argument list (defaults to ``sys.argv[1:]``).
    :returns: Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quartz-dir",
        type=Path,
        default=_default_quartz_dir(),
        help="Quartz v4 checkout directory",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional output directory (default: <quartz-dir>/public)",
    )
    parser.add_argument(
        "--skip-verify",
        action="store_true",
        help="Skip post-build checks",
    )
    args = parser.parse_args(argv)
    quartz_dir = args.quartz_dir.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve() if args.output_dir else None

    ensure_quartz(quartz_dir)
    public_dir = build_site(quartz_dir, output_dir)
    if not args.skip_verify:
        failures = verify_build(public_dir)
        if failures:
            print("Build verification failed:", file=sys.stderr)
            for item in failures:
                print(f"  - {item}", file=sys.stderr)
            return 1
        print(f"Build verification passed: {public_dir}")
    print(f"Site built at {public_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
