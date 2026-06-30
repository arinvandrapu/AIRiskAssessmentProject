"""Render a radar chart of NIST AI RMF maturity by function."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: render to file, never to a display

import matplotlib.pyplot as plt  # noqa: E402  (must follow backend selection)
import numpy as np  # noqa: E402

from .scoring import ScoreReport  # noqa: E402


def render_maturity_radar(
    report: ScoreReport, out_path: Path, title: str = "AI Governance Maturity"
) -> Path:
    """Write a radar chart (one axis per function) to ``out_path`` as PNG.

    Not-yet-assessed functions (maturity is None) plot at 0 so the chart is valid
    even for a skeleton assessment.
    """
    labels = [f.name for f in report.functions]
    values = [(f.summary.maturity or 0.0) for f in report.functions]

    # Close the polygon by repeating the first point.
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values_closed = values + values[:1]
    angles_closed = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"polar": True})
    ax.plot(angles_closed, values_closed, color="#2563eb", linewidth=2)
    ax.fill(angles_closed, values_closed, color="#2563eb", alpha=0.20)

    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["25%", "50%", "75%", "100%"], fontsize=8, color="#666")
    ax.set_title(title, fontsize=14, pad=20)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path
