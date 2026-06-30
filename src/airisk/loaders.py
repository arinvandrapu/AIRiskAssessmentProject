"""Locate and load the project's YAML files into validated models."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from .models import AssessmentFile, InventoryFile, NistFramework, OrgFile


class DataError(Exception):
    """Raised when an input file is missing or fails schema validation."""


@dataclass(frozen=True)
class Paths:
    """Resolves every input/output path relative to a project root."""

    root: Path

    @classmethod
    def from_root(cls, root: str | Path | None = None) -> Paths:
        return cls(Path(root).resolve() if root else Path.cwd())

    @property
    def organization(self) -> Path:
        return self.root / "data" / "organization.yaml"

    @property
    def inventory(self) -> Path:
        return self.root / "data" / "ai_inventory.yaml"

    @property
    def nist_framework(self) -> Path:
        return self.root / "frameworks" / "nist_ai_rmf.yaml"

    @property
    def eu_ai_act(self) -> Path:
        return self.root / "frameworks" / "eu_ai_act.yaml"

    @property
    def nist_assessment(self) -> Path:
        return self.root / "data" / "assessments" / "nist_ai_rmf.yaml"

    @property
    def reports_dir(self) -> Path:
        return self.root / "reports"


def _read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise DataError(f"File not found: {path}")
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:  # pragma: no cover - exercised via malformed fixture
        raise DataError(f"Invalid YAML in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise DataError(f"Expected a mapping at the top of {path}, got {type(data).__name__}")
    return data


def _validate(model: type, data: dict[str, Any], path: Path):
    try:
        return model.model_validate(data)
    except ValidationError as exc:
        raise DataError(f"Schema validation failed for {path}:\n{exc}") from exc


def load_org(paths: Paths) -> OrgFile:
    return _validate(OrgFile, _read_yaml(paths.organization), paths.organization)


def load_inventory(paths: Paths) -> InventoryFile:
    return _validate(InventoryFile, _read_yaml(paths.inventory), paths.inventory)


def load_nist_framework(paths: Paths) -> NistFramework:
    return _validate(NistFramework, _read_yaml(paths.nist_framework), paths.nist_framework)


def load_assessment(paths: Paths) -> AssessmentFile:
    return _validate(AssessmentFile, _read_yaml(paths.nist_assessment), paths.nist_assessment)


def load_eu_ai_act(paths: Paths) -> dict[str, Any]:
    """The EU AI Act file is reference content; loaded as a raw mapping."""
    return _read_yaml(paths.eu_ai_act)
