"""Render the scorecard and final report from the scored assessment."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import (
    EUAssessmentFile,
    Findings,
    GapsFile,
    InventoryFile,
    OrgFile,
    RoadmapFile,
)
from .scoring import (
    ScoreReport,
    eu_tier_distribution,
    gap_summary,
    high_risk_obligations,
)

_TEMPLATES_DIR = Path(__file__).parent / "templates"


def _env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(_TEMPLATES_DIR),
        autoescape=select_autoescape(enabled_extensions=()),  # Markdown output, no HTML escaping
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["pct"] = lambda v: "not assessed" if v is None else f"{v:.1f}%"
    return env


def build_context(
    org: OrgFile,
    inventory: InventoryFile,
    score: ScoreReport,
    eu_ai_act: dict[str, Any],
    chart_filename: str | None,
    *,
    gaps: GapsFile | None = None,
    roadmap: RoadmapFile | None = None,
    findings: Findings | None = None,
    eu_assessment: EUAssessmentFile | None = None,
) -> dict[str, Any]:
    # Pre-join inline/looped strings in Python so the Markdown templates stay
    # simple and don't fight Jinja's trim_blocks whitespace handling.
    a = org.assessment
    meta_bits = [f"**Engagement:** {a.engagement}"]
    if a.period:
        meta_bits.append(f"**Period:** {a.period}")
    if a.depth:
        meta_bits.append(f"**Depth:** {a.depth}")

    distribution = eu_tier_distribution(inventory)
    eu_rows = [
        {"tier": tier, "count": len(ucs), "names": ", ".join(uc.name for uc in ucs)}
        for tier, ucs in distribution.items()
    ]

    gap_list = gaps.gaps if gaps else []
    # Only show use-case obligation tables for cases that actually carry obligations.
    eu_cases = [uc for uc in (eu_assessment.use_cases if eu_assessment else []) if uc.obligations]

    return {
        "org": org.organization,
        "assessment": a,
        "inventory": inventory.use_cases,
        "score": score,
        "meta_line": " · ".join(meta_bits),
        "frameworks_str": ", ".join(a.frameworks),
        "stakeholders_str": "; ".join(f"{s.function} ({s.title})" for s in a.stakeholders),
        "evidence_str": "; ".join(a.evidence_collected),
        "eu_rows": eu_rows,
        "has_high_risk": "high-risk" in distribution,
        "eu_obligations": high_risk_obligations(eu_ai_act),
        "eu_cases": eu_cases,
        "gaps": gap_list,
        "gap_counts": gap_summary(gap_list) if gap_list else None,
        "roadmap": roadmap.actions if roadmap else [],
        "findings": findings,
        "chart_filename": chart_filename,
    }


def render(template_name: str, context: dict[str, Any]) -> str:
    return _env().get_template(template_name).render(**context)


def write_reports(reports_dir: Path, context: dict[str, Any]) -> list[Path]:
    """Render scorecard + final report into ``reports_dir`` and return the paths."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for template_name, out_name in (
        ("scorecard.md.j2", "scorecard.md"),
        ("final-report.md.j2", "final-report.md"),
    ):
        out_path = reports_dir / out_name
        out_path.write_text(render(template_name, context))
        written.append(out_path)
    return written
