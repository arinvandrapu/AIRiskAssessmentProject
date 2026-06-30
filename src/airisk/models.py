"""Pydantic schemas for every YAML input the tool consumes.

Validation happens at load time so malformed data fails fast with a clear error
rather than producing a silently-wrong report.
"""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class Status(StrEnum):
    """Implementation status of a NIST AI RMF subcategory."""

    MET = "Met"
    PARTIAL = "Partial"
    NOT_MET = "Not Met"
    NOT_APPLICABLE = "Not Applicable"


# Numeric weight per status. Not Applicable is intentionally absent: it is
# excluded from maturity denominators rather than scored as zero.
STATUS_WEIGHTS: dict[Status, float] = {
    Status.MET: 1.0,
    Status.PARTIAL: 0.5,
    Status.NOT_MET: 0.0,
}


class _Model(BaseModel):
    # Inputs are hand-authored YAML; reject unknown keys to catch typos early.
    model_config = ConfigDict(extra="forbid")


# --------------------------------------------------------------------------- #
# Organization (data/organization.yaml)
# --------------------------------------------------------------------------- #
class OrgSize(_Model):
    employees: int
    arr_usd_millions: float | None = None


class AIGovernancePosture(_Model):
    maturity: str
    summary: str | None = None
    notable_conditions: list[str] = []


class Organization(_Model):
    name: str
    industry: str | None = None
    headquarters: str | None = None
    size: OrgSize | None = None
    markets: list[str] = []
    business_units: list[str] = []
    ai_governance_posture: AIGovernancePosture | None = None


class Stakeholder(_Model):
    function: str
    title: str


class Assessment(_Model):
    engagement: str
    assessor_role: str | None = None
    period: str | None = None
    depth: str | None = None
    ai_use_reviewed: str | None = None
    in_scope: list[str] = []
    out_of_scope: list[str] = []
    frameworks: list[str] = []
    stakeholders: list[Stakeholder] = []
    evidence_collected: list[str] = []


class OrgFile(_Model):
    organization: Organization
    assessment: Assessment


# --------------------------------------------------------------------------- #
# AI inventory (data/ai_inventory.yaml)
# --------------------------------------------------------------------------- #
class UseCase(_Model):
    id: str
    name: str
    business_unit: str | None = None
    owner: str | None = None
    vendor_model: str | None = None
    purpose: str | None = None
    deployment_status: str | None = None
    customer_facing: bool | None = None
    data_used: list[str] = []
    personal_data: bool | None = None
    special_category_data: bool | None = None
    human_review: str | None = None
    eu_ai_act_tier: str | None = None
    notes: str | None = None


class InventoryFile(_Model):
    use_cases: list[UseCase]


# --------------------------------------------------------------------------- #
# NIST AI RMF catalog (frameworks/nist_ai_rmf.yaml)
# --------------------------------------------------------------------------- #
class Subcategory(_Model):
    id: str
    title: str
    intent: str | None = None


class Category(_Model):
    id: str
    title: str
    subcategories: list[Subcategory]


class Function(_Model):
    id: str
    name: str
    purpose: str | None = None
    categories: list[Category]


class NistFramework(_Model):
    # meta/trustworthiness are reference content; keep them loose.
    model_config = ConfigDict(extra="allow")

    functions: list[Function]

    @property
    def subcategory_ids(self) -> list[str]:
        return [s.id for f in self.functions for c in f.categories for s in c.subcategories]


# --------------------------------------------------------------------------- #
# Control ratings (data/assessments/nist_ai_rmf.yaml) — produced by init-assessment,
# filled in during Phase 3.
# --------------------------------------------------------------------------- #
class Rating(_Model):
    id: str
    status: Status | None = None
    evidence: list[str] = []
    notes: str | None = None


class AssessmentFile(_Model):
    model_config = ConfigDict(extra="allow")

    ratings: list[Rating]

    def status_by_id(self) -> dict[str, Status | None]:
        return {r.id: r.status for r in self.ratings}


# --------------------------------------------------------------------------- #
# Gap register (data/gaps.yaml) and roadmap (data/roadmap.yaml) — Phase 3
# --------------------------------------------------------------------------- #
class Severity(StrEnum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Gap(_Model):
    id: str
    title: str
    description: str | None = None
    framework: str | None = None
    mapping: list[str] = []
    risk: str | None = None
    evidence: list[str] = []
    severity: Severity
    severity_rationale: str | None = None  # why this gap got this severity


class GapsFile(_Model):
    gaps: list[Gap]


class RoadmapAction(_Model):
    id: str
    action: str
    owner: str | None = None
    target: str | None = None
    resources: str | None = None
    success_measure: str | None = None
    addresses: list[str] = []
    priority: Severity


class RoadmapFile(_Model):
    actions: list[RoadmapAction]


# --------------------------------------------------------------------------- #
# EU AI Act per-use-case assessment (data/assessments/eu_ai_act.yaml)
# --------------------------------------------------------------------------- #
class EUObligation(_Model):
    ref: str
    requirement: str | None = None
    status: Status | None = None
    note: str | None = None


class EUUseCaseAssessment(_Model):
    id: str
    name: str | None = None
    tier: str | None = None
    role: str | None = None
    rationale: str | None = None
    obligations: list[EUObligation] = []


class EUAssessmentFile(_Model):
    use_cases: list[EUUseCaseAssessment]


# --------------------------------------------------------------------------- #
# Executive narrative (data/findings.yaml)
# --------------------------------------------------------------------------- #
class DetailedFinding(_Model):
    title: str
    use_case: str | None = None
    severity: Severity | None = None
    regulatory_hook: str | None = None
    impact: str | None = None
    affected: str | None = None
    recommendation: str | None = None


class Findings(_Model):
    executive_summary: str | None = None
    key_findings: list[str] = []
    detailed_findings: list[DetailedFinding] = []
