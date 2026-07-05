---
id: perc_multimodal_perception
name: Multimodal Perception
domain: perception
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: high
  world_model: high
---

# Multimodal Perception

## Summary
Multimodal Perception within perception for reliable production cognition.

## Definition
Multimodal Perception is the capability to perform perception tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply multimodal perception in an enterprise workflow

## Related Skills
- perc_ui_state_perception
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
