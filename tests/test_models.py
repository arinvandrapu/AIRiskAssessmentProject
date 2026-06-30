"""Schema validation tests."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from airisk.models import OrgFile, Status


def test_valid_org_minimal() -> None:
    org = OrgFile.model_validate(
        {
            "organization": {"name": "FakeOrg"},
            "assessment": {"engagement": "AI Governance Risk Assessment"},
        }
    )
    assert org.organization.name == "FakeOrg"


def test_unknown_field_rejected() -> None:
    # extra="forbid" catches typos in hand-authored YAML.
    with pytest.raises(ValidationError):
        OrgFile.model_validate(
            {
                "organization": {"name": "FakeOrg", "industri": "typo"},
                "assessment": {"engagement": "x"},
            }
        )


def test_missing_required_field_rejected() -> None:
    with pytest.raises(ValidationError):
        OrgFile.model_validate({"organization": {"name": "FakeOrg"}})  # no assessment


def test_status_values() -> None:
    assert Status("Met") is Status.MET
    assert Status("Not Applicable") is Status.NOT_APPLICABLE
