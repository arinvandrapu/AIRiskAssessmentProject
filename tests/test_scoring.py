"""Scoring-math tests with a hand-built framework (no file I/O)."""

from __future__ import annotations

from airisk.models import Category, Function, NistFramework, Status, Subcategory
from airisk.scoring import score_nist


def _framework() -> NistFramework:
    subs = [Subcategory(id=f"GOVERN 1.{i}", title=f"sub {i}") for i in range(1, 6)]
    return NistFramework(
        functions=[
            Function(
                id="GOVERN",
                name="Govern",
                categories=[Category(id="GOVERN 1", title="Policies", subcategories=subs)],
            )
        ]
    )


def test_maturity_excludes_na_and_unrated() -> None:
    statuses = {
        "GOVERN 1.1": Status.MET,  # 1.0
        "GOVERN 1.2": Status.PARTIAL,  # 0.5
        "GOVERN 1.3": Status.NOT_MET,  # 0.0
        "GOVERN 1.4": Status.NOT_APPLICABLE,  # excluded from denominator
        "GOVERN 1.5": None,  # not assessed — excluded
    }
    report = score_nist(_framework(), statuses)
    overall = report.overall

    assert overall.total == 5
    assert overall.assessed == 4  # four have a status (incl. N/A)
    assert overall.applicable == 3  # Met + Partial + Not Met
    assert overall.maturity == (1.0 + 0.5 + 0.0) / 3
    assert overall.maturity_pct == 50.0


def test_unrated_framework_has_no_maturity() -> None:
    report = score_nist(_framework(), {})
    assert report.overall.assessed == 0
    assert report.overall.applicable == 0
    assert report.overall.maturity is None
    assert report.overall.maturity_pct is None


def test_rollup_matches_function_and_category() -> None:
    statuses = {"GOVERN 1.1": Status.MET, "GOVERN 1.2": Status.NOT_MET}
    report = score_nist(_framework(), statuses)
    func = report.functions[0]
    cat = func.categories[0]
    # one function, one category -> identical rollups
    assert func.summary.maturity == cat.summary.maturity == 0.5
    assert report.overall.maturity == 0.5
