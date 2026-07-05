# Contributing

Thanks for helping improve Cognitive Core Skills.

## Ways to contribute

- Add or improve skill cards
- Improve evaluation fixtures and benchmarks
- Improve schema clarity and validation coverage
- Improve docs, examples, and adoption guidance

## Quick contribution flow

1. Fork the repository.
2. Create a branch with a clear name.
3. Make focused changes.
4. Run tests locally.
5. Open a pull request using the PR template.

## Local checks

```powershell
py -m pytest tests/test_cognitive_core_taxonomy.py tests/test_rubric_benchmark_fixtures.py -q
```

## Add or update a skill

1. Update `data/cognitive-core-skills.json`.
2. Mirror the change in `data/cognitive-core-skills.yaml`.
3. Ensure unique `id` and `name`.
4. Ensure all `related_skills` references exist.
5. Regenerate markdown skill cards:

```powershell
py scripts/generate_skills.py
```

6. Update `docs/cognitive-core-skills/CHANGELOG.md` under `Unreleased`.
7. Re-run tests.

## Pull request standards

- Keep scope tight and reviewable.
- Explain the rationale and expected impact.
- Add or update tests for behavior changes.
- Update docs for any user-visible changes.

## Taxonomy quality checklist

- Domain assignment is correct.
- Model relevance fields are justified.
- Evaluation questions are concrete.
- Failure modes are realistic.
- Skill wording is industry-neutral and non-vendor-specific.
