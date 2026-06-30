"""Maturity scoring for NIST AI RMF, plus EU AI Act classification helpers.

Scoring rules (see frameworks/nist_ai_rmf.yaml `meta.scoring`):
  Met = 1.0, Partial = 0.5, Not Met = 0.0.
  Not Applicable is excluded from the denominator.
  Unrated (status is None) is "not assessed" — also excluded, but tracked
  separately as coverage so a skeleton report is honest about what's been done.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .models import STATUS_WEIGHTS, InventoryFile, NistFramework, Status, UseCase


@dataclass
class Summary:
    """Aggregated scoring for a node (overall, function, or category)."""

    total: int  # subcategories in scope of this node
    assessed: int  # have a status (incl. Not Applicable)
    applicable: int  # status in {Met, Partial, Not Met} — the maturity denominator
    weight_sum: float

    @property
    def maturity(self) -> float | None:
        """Maturity as a 0-1 fraction, or None if nothing is applicable yet."""
        if self.applicable == 0:
            return None
        return self.weight_sum / self.applicable

    @property
    def maturity_pct(self) -> float | None:
        m = self.maturity
        return None if m is None else round(m * 100, 1)


def _summarize(statuses: list[Status | None]) -> Summary:
    applicable = [s for s in statuses if s in STATUS_WEIGHTS]
    return Summary(
        total=len(statuses),
        assessed=sum(1 for s in statuses if s is not None),
        applicable=len(applicable),
        weight_sum=sum(STATUS_WEIGHTS[s] for s in applicable),
    )


@dataclass
class CategoryScore:
    id: str
    title: str
    summary: Summary


@dataclass
class FunctionScore:
    id: str
    name: str
    summary: Summary
    categories: list[CategoryScore] = field(default_factory=list)


@dataclass
class ScoreReport:
    overall: Summary
    functions: list[FunctionScore]


def score_nist(framework: NistFramework, statuses: dict[str, Status | None]) -> ScoreReport:
    """Walk the catalog and roll maturity up subcategory -> category -> function."""
    function_scores: list[FunctionScore] = []
    all_statuses: list[Status | None] = []

    for func in framework.functions:
        cat_scores: list[CategoryScore] = []
        func_statuses: list[Status | None] = []

        for cat in func.categories:
            cat_statuses = [statuses.get(sub.id) for sub in cat.subcategories]
            cat_scores.append(CategoryScore(cat.id, cat.title, _summarize(cat_statuses)))
            func_statuses.extend(cat_statuses)

        function_scores.append(
            FunctionScore(func.id, func.name, _summarize(func_statuses), cat_scores)
        )
        all_statuses.extend(func_statuses)

    return ScoreReport(overall=_summarize(all_statuses), functions=function_scores)


# --------------------------------------------------------------------------- #
# EU AI Act helpers
# --------------------------------------------------------------------------- #
# Order tiers most-to-least severe so reports read top-down.
EU_TIER_ORDER = ["prohibited", "high-risk", "limited-risk", "minimal-risk"]


def eu_tier_distribution(inventory: InventoryFile) -> dict[str, list[UseCase]]:
    """Group use cases by their EU AI Act tier, in severity order."""
    dist: dict[str, list[UseCase]] = {tier: [] for tier in EU_TIER_ORDER}
    for uc in inventory.use_cases:
        dist.setdefault(uc.eu_ai_act_tier or "unclassified", []).append(uc)
    # Drop empty buckets while preserving order.
    return {tier: ucs for tier, ucs in dist.items() if ucs}


def high_risk_obligations(eu_ai_act: dict[str, Any]) -> dict[str, list[dict[str, str]]]:
    """Return provider/deployer high-risk obligation lists from the reference file."""
    obligations = eu_ai_act.get("obligations", {})
    return {
        "provider": obligations.get("provider_high_risk", []),
        "deployer": obligations.get("deployer_high_risk", []),
    }
