"""Put ``site/`` on ``sys.path`` so tests can import the build helpers.

The folder name ``site`` collides with the stdlib ``site`` module, so tests
import ``stage_content`` and ``verify_build`` as top-level modules.
"""

from __future__ import annotations

import sys
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent / "site"
sys.path.insert(0, str(SITE_DIR))
