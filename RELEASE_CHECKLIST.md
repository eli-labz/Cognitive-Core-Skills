# Release Checklist

Use this checklist for recurring Cognitive Core Skills taxonomy releases.

## 1. Scope and versioning

- Confirm release scope and target version.
- Decide semantic version bump.
- Freeze non-release changes.

## 2. Data and schema integrity

- Confirm `data/cognitive-core-skills.json` and `data/cognitive-core-skills.yaml` are synchronized.
- Validate all skill ids are unique.
- Validate all related skill references resolve.
- Validate schema files are up to date:
  - `schemas/cognitive-core-skill.schema.json`
  - `schemas/cognitive-core-taxonomy.schema.json`

## 3. Generated artifacts

- Regenerate skill cards:

  `py scripts/generate_skills.py`

- Confirm `Skills/index.md` is updated.
- Confirm generated skill file count matches taxonomy skill count.

## 4. Benchmarks and evaluation

- Confirm benchmark fixtures are valid:
  - `benchmarks/rubric-task-traces.json`
- Confirm fixture tests pass.
- Confirm rubric docs still match fixture dimensions.

## 5. Documentation

- Update `docs/cognitive-core-skills/CHANGELOG.md`:
  - Move relevant entries from Unreleased into versioned section.
  - Include added, removed, changed skill ids.
- Update `README.md` status values if changed.
- Update any impacted docs under `docs/cognitive-core-skills/`.

## 6. Test and CI gate

Run before release:

`py -m pytest tests/test_cognitive_core_taxonomy.py tests/test_rubric_benchmark_fixtures.py -q`

- Confirm CI workflow is green:
  - `.github/workflows/taxonomy-ci.yml`

## 7. Release publish steps

- Create release commit.
- Tag release version.
- Publish release notes using changelog highlights.
- Announce major changes and migration notes.

## 8. Post-release hygiene

- Start new `Unreleased` section tracking.
- Create follow-up issues for deferred improvements.
- Verify generated artifacts are discoverable in repository navigation.
