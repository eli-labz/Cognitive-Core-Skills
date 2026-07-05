---
id: perc_environmental_state_tracking
name: Environmental State Tracking
domain: perception
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: high
  agent: critical
  world_model: high
---

# Environmental State Tracking

## Summary
Environmental State Tracking within perception for reliable production cognition.

## Definition
Environmental State Tracking is the capability to perform perception tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply environmental state tracking in an enterprise workflow

## Related Skills
- perc_entity_recognition
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
