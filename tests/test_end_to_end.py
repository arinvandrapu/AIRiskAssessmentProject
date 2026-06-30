"""End-to-end: load real FakeOrg data, render the full and skeleton reports."""

from __future__ import annotations

import shutil
from pathlib import Path

from airisk.cli import assess, init_assessment
from airisk.loaders import Paths, load_inventory, load_nist_framework, load_org

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_shipped_data_loads(repo_root: Path) -> None:
    paths = Paths.from_root(repo_root)
    org = load_org(paths)
    inventory = load_inventory(paths)
    framework = load_nist_framework(paths)

    assert org.organization.name == "FakeOrg"
    assert len(inventory.use_cases) == 6
    # Catalog integrity check: NIST AI RMF 1.0 has 72 subcategories.
    assert len(framework.subcategory_ids) == 72


def test_full_report_renders_assessment(project_copy: Path) -> None:
    # project_copy carries the scored ratings + gaps + roadmap + findings (Phase 3 data).
    assess(root=project_copy)
    report = (project_copy / "reports" / "final-report.md").read_text()

    assert "FakeOrg" in report
    assert "Synthetic data" in report
    assert "gaps identified" in report  # real scoring + gap counts
    assert "GAP-01" in report  # gap register rendered
    assert "ACT-01" in report  # roadmap rendered
    assert "Key findings" in report  # executive summary
    assert "Art 27" in report  # EU AI Act obligation table
    assert "scoring methodology" in report.lower()  # §3 methodology section
    assert "Detailed findings" in report  # deep-dive findings
    assert "Regulatory hook" in report  # detailed-finding structure
    assert "Why High" in report  # per-gap severity rationale


def test_skeleton_report_without_phase3_data(tmp_path: Path) -> None:
    # Minimal project: frameworks + org + inventory only, blank ratings.
    shutil.copytree(REPO_ROOT / "frameworks", tmp_path / "frameworks")
    (tmp_path / "data").mkdir()
    for name in ("organization.yaml", "ai_inventory.yaml"):
        shutil.copy(REPO_ROOT / "data" / name, tmp_path / "data" / name)

    init_assessment(root=tmp_path)
    assess(root=tmp_path)
    report = (tmp_path / "reports" / "final-report.md").read_text()

    assert "not assessed" in report  # no ratings entered
    assert "No gap register loaded" in report  # gaps file absent
