# Cognitive Core Skill Card Example

## Template

id: txt_reading_comprehension
name: Reading Comprehension
domain: text_based
summary: Understands explicit and implicit meaning in operational text.
definition: Ability to interpret source text accurately before synthesis, extraction, or action.
model_relevance:
  llm: critical
  slm: high
  agent: high
  world_model: medium
skill_type: cognitive
inputs:
  - source text
  - task context
outputs:
  - comprehension map
required_capabilities:
  - semantic parsing
  - context retention
failure_modes:
  - misses key constraints
  - confuses assumptions with evidence
evaluation_questions:
  - What evidence supports the interpretation?
  - Which assumptions require verification?
evaluation_signals:
  - high fact recall
  - low contradiction rate
difficulty_level: intermediate
human_review_required: often
example_tasks:
  - summarize policy obligations from a contract
related_skills:
  - txt_claim_extraction
  - grd_retrieval_augmented_grounding
source_patterns:
  - policies
  - reports
  - tickets

## Notes

Use this card structure for all new skills so schema validation and cross-skill linking remain consistent.