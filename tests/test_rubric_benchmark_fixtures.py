import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "benchmarks" / "rubric-task-traces.json"
TAXONOMY_PATH = ROOT / "data" / "cognitive-core-skills.json"
RUBRIC_PATH = ROOT / "docs" / "cognitive-core-skills" / "evaluation-rubric.md"

REQUIRED_DIMENSIONS = {
    "accuracy",
    "consistency",
    "latency",
    "generalization",
    "recoverability",
    "grounding",
    "explainability",
    "auditability",
    "human_oversight_compatibility",
    "production_readiness",
}


def test_benchmark_fixture_file_exists():
    assert FIXTURE_PATH.exists()
    assert RUBRIC_PATH.exists()


def test_fixture_shape_and_rubric_mapping():
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    assert "fixtures" in payload
    assert isinstance(payload["fixtures"], list)
    assert len(payload["fixtures"]) >= 6

    dims = set(payload.get("dimensions", []))
    assert dims == REQUIRED_DIMENSIONS

    for fx in payload["fixtures"]:
        assert "fixture_id" in fx
        assert "skill_id" in fx
        assert "task" in fx
        assert "trace_ref" in fx
        assert "scores" in fx
        assert "expected_level" in fx

        scores = fx["scores"]
        assert set(scores.keys()) == REQUIRED_DIMENSIONS
        for value in scores.values():
            assert isinstance(value, int)
            assert 0 <= value <= 5

        assert isinstance(fx["expected_level"], int)
        assert 0 <= fx["expected_level"] <= 5

        avg = round(sum(scores.values()) / len(scores))
        assert abs(avg - fx["expected_level"]) <= 1


def test_fixture_skill_ids_exist_in_taxonomy():
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    taxonomy = json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))

    skill_ids = {s["id"] for s in taxonomy["skills"]}
    for fx in payload["fixtures"]:
        assert fx["skill_id"] in skill_ids, f"Unknown skill_id in fixture: {fx['skill_id']}"
