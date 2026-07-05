# Taxonomy Changelog

This changelog tracks versioned changes to the Cognitive Core Skills taxonomy data model and skill inventory.

## Format

Each release entry should include:

- version
- date
- added skill IDs
- removed skill IDs
- changed skill IDs
- schema changes
- notes

## Unreleased

- Added skill: `ha_consequence_understanding` (Human-Action Consequence Understanding).
- Added skill: `plan_long_horizon_skill` (Long-Horizon Skill).
- Updated data artifacts:
  - data/cognitive-core-skills.json
  - data/cognitive-core-skills.yaml

## 1.0.0 - 2026-07-05

### Added

- Initial release of cognitive core taxonomy with 157 skill entries across 13 domains.
- Initial schema set:
  - schemas/cognitive-core-skill.schema.json
  - schemas/cognitive-core-taxonomy.schema.json
- Initial data artifacts:
  - data/cognitive-core-skills.json
  - data/cognitive-core-skills.yaml

### Removed

- none

### Changed

- none

### Notes

- Includes dedicated sections for LLM Wiki skills and OKF-aligned catalog skills.
- Includes first-pass evaluation and CDI governance documentation.
