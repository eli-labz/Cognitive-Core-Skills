import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "data" / "cognitive-core-skills.json"
YAML_PATH = ROOT / "data" / "cognitive-core-skills.yaml"
SKILL_SCHEMA_PATH = ROOT / "schemas" / "cognitive-core-skill.schema.json"
TAXONOMY_SCHEMA_PATH = ROOT / "schemas" / "cognitive-core-taxonomy.schema.json"

REQUIRED_DOMAINS = {
    "perception",
    "memory",
    "reasoning",
    "planning",
    "action_selection",
    "verification",
    "grounding",
    "governance",
    "text_based",
    "human_action",
    "world_model",
    "llm_wiki",
    "okf",
}

MIN_DISTRIBUTION = {
    "perception": 8,
    "memory": 8,
    "reasoning": 10,
    "planning": 8,
    "action_selection": 8,
    "verification": 8,
    "grounding": 8,
    "governance": 6,
    "text_based": 10,
    "human_action": 10,
    "world_model": 6,
    "llm_wiki": 8,
    "okf": 8,
}

REQUIRED_EXAMPLE_IDS = {
    "txt_reading_comprehension",
    "txt_intent_routing",
    "ha_crm_record_update_action",
    "wm_state_transition_prediction",
    "llmw_source_ingestion",
    "okf_knowledge_cataloging",
}

VALID_LEVELS = {"none", "low", "medium", "high", "critical"}
VALID_SKILL_TYPES = {"cognitive", "operational", "governance", "knowledge_management", "evaluation"}
VALID_DIFFICULTY = {"basic", "intermediate", "advanced", "frontier"}
VALID_REVIEW = {"never", "sometimes", "often", "always"}


def load_taxonomy():
    return json.loads(JSON_PATH.read_text(encoding="utf-8"))


def test_required_files_exist():
    assert JSON_PATH.exists()
    assert YAML_PATH.exists()
    assert SKILL_SCHEMA_PATH.exists()
    assert TAXONOMY_SCHEMA_PATH.exists()


def test_taxonomy_basic_shape():
    data = load_taxonomy()
    for key in ["taxonomy_id", "version", "title", "description", "domains", "skills", "relationships"]:
        assert key in data

    assert isinstance(data["skills"], list)
    assert len(data["skills"]) >= 80


def test_domain_representation_and_min_distribution():
    data = load_taxonomy()
    domain_ids = {d["id"] for d in data["domains"]}
    assert REQUIRED_DOMAINS.issubset(domain_ids)

    counts = {d: 0 for d in REQUIRED_DOMAINS}
    for skill in data["skills"]:
        counts[skill["domain"]] += 1

    for domain, minimum in MIN_DISTRIBUTION.items():
        assert counts[domain] >= minimum, f"{domain} has {counts[domain]}, expected >= {minimum}"


def test_skill_uniqueness_and_required_fields():
    data = load_taxonomy()
    ids = [s["id"] for s in data["skills"]]
    names = [s["name"] for s in data["skills"]]

    assert len(ids) == len(set(ids)), "Duplicate skill IDs found"
    assert len(names) == len(set(names)), "Duplicate skill names found"

    required_fields = {
        "id",
        "name",
        "domain",
        "summary",
        "definition",
        "model_relevance",
        "skill_type",
        "inputs",
        "outputs",
        "required_capabilities",
        "failure_modes",
        "evaluation_questions",
        "evaluation_signals",
        "difficulty_level",
        "human_review_required",
        "example_tasks",
        "related_skills",
        "source_patterns",
    }

    for skill in data["skills"]:
        assert required_fields.issubset(set(skill.keys())), f"Missing fields in {skill.get('id')}"
        assert skill["domain"] in REQUIRED_DOMAINS
        assert skill["skill_type"] in VALID_SKILL_TYPES
        assert skill["difficulty_level"] in VALID_DIFFICULTY
        assert skill["human_review_required"] in VALID_REVIEW

        mr = skill["model_relevance"]
        assert set(mr.keys()) == {"llm", "slm", "agent", "world_model"}
        assert all(value in VALID_LEVELS for value in mr.values())


def test_related_skill_references_and_relationships_are_valid():
    data = load_taxonomy()
    skill_ids = {s["id"] for s in data["skills"]}

    for skill in data["skills"]:
        for related in skill["related_skills"]:
            assert related in skill_ids, f"Invalid related skill reference {related} in {skill['id']}"

    for rel in data["relationships"]:
        assert rel["parent"] in skill_ids
        assert rel["child"] in skill_ids
        assert rel["relation"] in {"enables", "supports", "constrains", "informs", "specifies", "depends_on", "related_to"}


def test_required_example_skills_present():
    data = load_taxonomy()
    skill_ids = {s["id"] for s in data["skills"]}
    missing = REQUIRED_EXAMPLE_IDS - skill_ids
    assert not missing, f"Missing required example skill IDs: {sorted(missing)}"


def test_yaml_present_and_contains_top_level_markers():
    raw = YAML_PATH.read_text(encoding="utf-8")
    assert "taxonomy_id:" in raw
    assert "skills:" in raw
    assert "relationships:" in raw


def test_optional_jsonschema_validation_if_installed():
    data = load_taxonomy()
    try:
        import jsonschema
    except Exception:
        pytest.skip("jsonschema not installed; structural tests executed instead")

    skill_schema = json.loads(SKILL_SCHEMA_PATH.read_text(encoding="utf-8"))
    taxonomy_schema = json.loads(TAXONOMY_SCHEMA_PATH.read_text(encoding="utf-8"))
    resolver = jsonschema.RefResolver.from_schema(
        taxonomy_schema,
        store={
            "https://example.org/schemas/cognitive-core-taxonomy.schema.json": taxonomy_schema,
            "https://example.org/schemas/cognitive-core-skill.schema.json": skill_schema,
            "./cognitive-core-skill.schema.json": skill_schema,
        },
    )
    jsonschema.validate(instance=data, schema=taxonomy_schema, resolver=resolver)
