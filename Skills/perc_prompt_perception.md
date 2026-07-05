---
id: perc_prompt_perception
name: Prompt Perception
domain: perception
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: critical
  slm: high
  agent: critical
  world_model: low
---

# Prompt Perception

## Summary
Prompt Perception within perception for reliable production cognition.

## Definition
Prompt Perception is the capability to perform perception tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply prompt perception in an enterprise workflow

## Related Skills
- perc_environmental_state_tracking
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
