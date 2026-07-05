---
id: wm_state_transition_prediction
name: State Transition Prediction
domain: world_model
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: critical
  world_model: critical
---

# State Transition Prediction

## Summary
State Transition Prediction within world model for reliable production cognition.

## Definition
State Transition Prediction is the capability to perform world model tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply state transition prediction in an enterprise workflow

## Related Skills
- wm_enterprise_process_modeling
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
