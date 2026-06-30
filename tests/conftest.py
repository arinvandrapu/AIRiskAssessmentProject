"""Shared pytest fixtures."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def repo_root() -> Path:
    """The real project root (read-only loads against shipped FakeOrg data)."""
    return REPO_ROOT


@pytest.fixture
def project_copy(tmp_path: Path) -> Path:
    """An isolated copy of the project's inputs for tests that write outputs."""
    shutil.copytree(REPO_ROOT / "frameworks", tmp_path / "frameworks")
    shutil.copytree(REPO_ROOT / "data", tmp_path / "data")
    return tmp_path
