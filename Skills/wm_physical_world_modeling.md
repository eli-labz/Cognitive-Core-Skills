---
id: wm_physical_world_modeling
name: Physical World Modeling
domain: world_model
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: low
  agent: medium
  world_model: critical
---

# Physical World Modeling

## Summary
Physical World Modeling within world model for reliable production cognition.

## Definition
Physical World Modeling is the capability to perform world model tasks with bounded, auditable behavior in enterprise workflows.

## Inputs
- task context
- current state
- policy constraints

## Outputs
- skill outcome
- trace evidence

## Required Capabilities
- state interpretation
- bounded execution
- result traceability

## Failure Modes
- state misread leading to wrong action
- insufficient verification before completion

## Evaluation Questions
- What evidence supports this outcome?
- What should be verified before action?
- What assumptions were made?

## Evaluation Signals
- accuracy against expected outcome
- consistency across repeated runs
- audit trace completeness

## Example Tasks
- Apply physical world modeling in an enterprise workflow

## Related Skills
- wm_outcome_forecasting
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
