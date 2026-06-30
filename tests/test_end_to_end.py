"""End-to-end: load real FakeOrg data, generate ratings, render reports."""

from __future__ import annotations

from pathlib import Path

from airisk.cli import assess, init_assessment
from airisk.loaders import Paths, load_inventory, load_nist_framework, load_org


def test_shipped_data_loads(repo_root: Path) -> None:
    paths = Paths.from_root(repo_root)
    org = load_org(paths)
    inventory = load_inventory(paths)
    framework = load_nist_framework(paths)

    assert org.organization.name == "FakeOrg"
    assert len(inventory.use_cases) == 6
    # Catalog integrity check: NIST AI RMF 1.0 has 72 subcategories.
    assert len(framework.subcategory_ids) == 72


def test_init_then_assess_renders_reports(project_copy: Path) -> None:
    init_assessment(root=project_copy, force=True)
    assessment_file = project_copy / "data" / "assessments" / "nist_ai_rmf.yaml"
    assert assessment_file.exists()

    assess(root=project_copy)
    reports = project_copy / "reports"
    assert (reports / "scorecard.md").exists()
    assert (reports / "final-report.md").exists()
    assert (reports / "maturity-chart.png").exists()

    report_text = (reports / "final-report.md").read_text()
    assert "FakeOrg" in report_text
    assert "Synthetic data" in report_text
    # High-risk use case present -> obligations checklist rendered.
    assert "High-risk obligations checklist" in report_text
