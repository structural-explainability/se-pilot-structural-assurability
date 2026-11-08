"""Tests for the query-violation finite-model experiment."""

from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "experiments" / "tevv-athlon" / "query_violation.py"


def run_experiment() -> str:
    """Run the experiment script and return its standard output."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def test_candidate_1_does_not_resolve_four_scenario_claim() -> None:
    """Tested-scenario evidence leaves the untested scenario undetermined."""
    out = run_experiment()
    assert "resolves claim over all 4: False" in out
    assert "(True, True, True, True) vs (True, True, True, False)" in out


def test_candidate_2_red_teaming_alone_does_not_resolve_organic_claim() -> None:
    """Red Teaming alone leaves organic behavior undetermined."""
    out = run_experiment()
    assert "tested scenarios: False" in out
    assert "organic: (True, True, True) vs (True, True, False)" in out
